#!/usr/bin/env python3
"""
Folder Analysis Report Generator
Scans a target folder, generates a PDF report with file statistics and charts,
and emails the report securely.
"""

# ============================================================================
# INPUT PARAMETERS - CONFIGURE THESE BEFORE RUNNING
# ============================================================================

# SECURITY NOTE: For sender_email and sender_password, use a DUMMY/THROWAWAY 
# email account created specifically for automation purposes. NEVER use your 
# personal or primary email account credentials in code for security reasons.
# Create a dedicated Gmail/Outlook account just for sending automated reports.

# 1. Target folder to analyze (full path)
target_folder = '/path/to/your/folder'

# 2. Email address to receive the report
recipient_email = 'recipient@example.com'

# 3. Sender email (MUST be Gmail - use a dummy/automation-only Gmail account)
sender_email = 'automation_dummy@gmail.com'

# 4. Sender Gmail App Password (for the dummy Gmail account)
# IMPORTANT: You MUST use a Gmail App Password, not your regular password
# Steps to get Gmail App Password:
# 1. Enable 2-Factor Authentication on your Gmail account
# 2. Go to: https://myaccount.google.com/apppasswords
# 3. Generate App Password for "Mail"
# 4. Copy the 16-character password (with spaces) below
sender_password = 'your_app_password_here'

# 5. Output PDF directory (filename will be auto-generated with timestamp)
# The script will automatically create a unique filename like:
# 'folder_analysis_report - 2026-02-13 20.36.36.pdf'
# Just specify the directory where you want to save the PDF:
output_pdf = '/home/claude/folder_analysis_report.pdf'  # Directory from this path will be used

# ============================================================================
# SMTP CONFIGURATION (Gmail Only - Do Not Modify)
# ============================================================================
# The sender MUST be a Gmail account. These settings are fixed for Gmail.
smtp_server = 'smtp.gmail.com'
smtp_port = 587
use_ssl = False  # Gmail uses TLS on port 587

# NOTE: The recipient email (specified above) can be ANY email platform
# (Gmail, Outlook, Yahoo, etc.) - only the SENDER must be Gmail.

# ============================================================================
# END OF INPUT PARAMETERS
# ============================================================================

import os
import smtplib
from pathlib import Path
from collections import Counter
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from datetime import datetime
import tempfile
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_LEFT


class FolderAnalyzer:
    """Analyzes folder contents and generates statistics."""
    
    def __init__(self, target_folder):
        self.target_folder = Path(target_folder)
        self.files = []
        self.file_types = Counter()
        self.file_sizes = Counter()
        # Track total file size by type and category
        self.file_type_sizes = {}  # {extension: total_bytes}
        self.file_size_category_sizes = {}  # {category: total_bytes}
        self.total_size = 0  # Total size of all files
        
    def scan_folder(self):
        """Recursively scan folder and collect file information."""
        print(f"Scanning folder: {self.target_folder}")
        
        if not self.target_folder.exists():
            raise ValueError(f"Folder does not exist: {self.target_folder}")
        
        for root, dirs, files in os.walk(self.target_folder):
            for file in files:
                file_path = Path(root) / file
                try:
                    file_size = file_path.stat().st_size
                    file_ext = file_path.suffix.lower() if file_path.suffix else '(no extension)'
                    
                    self.files.append({
                        'path': file_path,
                        'name': file,
                        'extension': file_ext,
                        'size': file_size
                    })
                    
                    # Count file types
                    self.file_types[file_ext] += 1
                    
                    # Track total size by file type
                    if file_ext not in self.file_type_sizes:
                        self.file_type_sizes[file_ext] = 0
                    self.file_type_sizes[file_ext] += file_size
                    
                    # Categorize by size
                    if file_size < 1024 * 1024:  # < 1MB
                        category = '<1MB'
                        self.file_sizes[category] += 1
                    elif file_size < 1024 * 1024 * 1024:  # 1MB - 1GB
                        category = '1MB-1GB'
                        self.file_sizes[category] += 1
                    else:  # > 1GB
                        category = '>1GB'
                        self.file_sizes[category] += 1
                    
                    # Track total size by category
                    if category not in self.file_size_category_sizes:
                        self.file_size_category_sizes[category] = 0
                    self.file_size_category_sizes[category] += file_size
                    
                    # Track overall total size
                    self.total_size += file_size
                        
                except (PermissionError, OSError) as e:
                    print(f"Warning: Could not access {file_path}: {e}")
                    continue
        
        print(f"Found {len(self.files)} files")
        
    def format_size(self, bytes_size):
        """Convert bytes to human-readable format."""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes_size < 1024.0:
                return f"{bytes_size:.2f} {unit}"
            bytes_size /= 1024.0
        return f"{bytes_size:.2f} PB"
        
    def get_file_type_stats(self):
        """Return file type statistics sorted by frequency."""
        return sorted(self.file_types.items(), key=lambda x: x[1], reverse=True)
    
    def get_file_size_stats(self):
        """Return file size statistics in proper order."""
        # Define order for size categories
        size_order = ['<1MB', '1MB-1GB', '>1GB']
        return [(size, self.file_sizes.get(size, 0)) for size in size_order]


class ReportGenerator:
    """Generates PDF reports with charts and tables."""
    
    def __init__(self, analyzer, output_path):
        self.analyzer = analyzer
        self.output_path = output_path
        self.chart_paths = []
        # Create temporary directory for charts
        self.temp_dir = tempfile.mkdtemp()
        
    def create_bar_chart(self, data, title, filename, xlabel='Count'):
        """Create a horizontal bar chart ranked from top to bottom."""
        if not data:
            return None
            
        labels, values = zip(*data)
        
        fig, ax = plt.subplots(figsize=(10, max(6, len(labels) * 0.4)))
        
        # Create horizontal bar chart
        y_pos = range(len(labels))
        ax.barh(y_pos, values, color='steelblue')
        
        # Customize chart
        ax.set_yticks(y_pos)
        ax.set_yticklabels(labels)
        ax.invert_yaxis()  # Top to bottom
        ax.set_xlabel(xlabel)
        ax.set_title(title, fontsize=14, fontweight='bold')
        ax.grid(axis='x', alpha=0.3)
        
        # Add value labels
        for i, v in enumerate(values):
            ax.text(v, i, f' {v}', va='center')
        
        plt.tight_layout()
        # Save to temporary directory
        chart_path = os.path.join(self.temp_dir, filename)
        plt.savefig(chart_path, dpi=150, bbox_inches='tight')
        plt.close()
        
        self.chart_paths.append(chart_path)
        return chart_path
    
    def generate_pdf(self):
        """Generate the complete PDF report."""
        print(f"Generating PDF report: {self.output_path}")
        
        doc = SimpleDocTemplate(self.output_path, pagesize=letter)
        story = []
        styles = getSampleStyleSheet()
        
        # Custom styles
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            textColor=colors.HexColor('#2c3e50'),
            spaceAfter=30,
            alignment=TA_CENTER
        )
        
        heading_style = ParagraphStyle(
            'CustomHeading',
            parent=styles['Heading2'],
            fontSize=16,
            textColor=colors.HexColor('#34495e'),
            spaceAfter=12,
            spaceBefore=20
        )
        
        # Title with timestamp for uniqueness
        report_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        title = Paragraph(f"Folder Analysis Report - {report_timestamp}", title_style)
        story.append(title)
        
        # Report metadata
        metadata = f"""
        <b>Target Folder:</b> {self.analyzer.target_folder}<br/>
        <b>Report Generated:</b> {report_timestamp}<br/>
        <b>Total Files Found:</b> {len(self.analyzer.files)}<br/>
        <b>Total File Size:</b> {self.analyzer.format_size(self.analyzer.total_size)}
        """
        story.append(Paragraph(metadata, styles['Normal']))
        story.append(Spacer(1, 0.3*inch))
        
        # Section 1: File Type Distribution
        story.append(Paragraph("1. File Type Distribution", heading_style))
        
        file_type_stats = self.analyzer.get_file_type_stats()
        if file_type_stats:
            # Chart FIRST (Top 10)
            chart_path = self.create_bar_chart(
                file_type_stats[:10],  # Limit to top 10
                'File Types by Frequency (Top 10)',
                'file_types_chart.png'
            )
            
            if chart_path:
                img = Image(chart_path, width=6*inch, height=4*inch)
                story.append(img)
                story.append(Spacer(1, 0.3*inch))
            
            # Table SECOND (Top 10)
            table_data = [['File Type', 'Count', 'Percentage', 'Total File Size']]
            total_files = len(self.analyzer.files)
            
            for ext, count in file_type_stats[:10]:  # Limit to top 10
                percentage = (count / total_files * 100) if total_files > 0 else 0
                total_size = self.analyzer.file_type_sizes.get(ext, 0)
                size_formatted = self.analyzer.format_size(total_size)
                table_data.append([ext, str(count), f'{percentage:.1f}%', size_formatted])
            
            table = Table(table_data, colWidths=[2*inch, 1.2*inch, 1.2*inch, 1.5*inch])
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3498db')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 12),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.grey),
                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey])
            ]))
            
            story.append(table)
        
        story.append(PageBreak())
        
        # Section 2: File Size Distribution
        story.append(Paragraph("2. File Size Distribution", heading_style))
        
        file_size_stats = self.analyzer.get_file_size_stats()
        if file_size_stats:
            # Chart FIRST
            # Sort by count for ranking
            sorted_size_stats = sorted(file_size_stats, key=lambda x: x[1], reverse=True)
            chart_path = self.create_bar_chart(
                sorted_size_stats,
                'Files by Size Category',
                'file_sizes_chart.png'
            )
            
            if chart_path:
                img = Image(chart_path, width=6*inch, height=3*inch)
                story.append(img)
                story.append(Spacer(1, 0.3*inch))
            
            # Table SECOND
            table_data = [['Size Category', 'Count', 'Percentage', 'Total File Size']]
            total_files = len(self.analyzer.files)
            
            for category, count in file_size_stats:
                percentage = (count / total_files * 100) if total_files > 0 else 0
                total_size = self.analyzer.file_size_category_sizes.get(category, 0)
                size_formatted = self.analyzer.format_size(total_size)
                table_data.append([category, str(count), f'{percentage:.1f}%', size_formatted])
            
            table = Table(table_data, colWidths=[2*inch, 1.2*inch, 1.2*inch, 1.5*inch])
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#e74c3c')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 12),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.grey),
                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey])
            ]))
            
            story.append(table)
        
        # Build PDF
        doc.build(story)
        print(f"PDF report generated successfully: {self.output_path}")
        
        # Clean up temporary directory and all chart files
        import shutil
        try:
            shutil.rmtree(self.temp_dir)
        except Exception as e:
            print(f"Warning: Could not clean up temporary files: {e}")
    

class EmailSender:
    """Sends email with PDF attachment securely using Gmail."""
    
    def __init__(self, smtp_server, smtp_port, sender_email, sender_password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password
    
    def send_report(self, recipient_email, pdf_path, subject=None):
        """Send the PDF report via email using Gmail SMTP."""
        if subject is None:
            subject = f"Folder Analysis Report - {datetime.now().strftime('%Y-%m-%d')}"
        
        print(f"Preparing to send email to: {recipient_email}")
        
        # Create message
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        # Email body
        body = f"""
Hello,

Please find attached the folder analysis report generated on {datetime.now().strftime('%Y-%m-%d at %H:%M:%S')}.

This is an automated report. Please do not reply to this email.

Best regards,
Folder Analysis System
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Attach PDF
        try:
            with open(pdf_path, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
            
            encoders.encode_base64(part)
            part.add_header(
                'Content-Disposition',
                f'attachment; filename= {os.path.basename(pdf_path)}'
            )
            
            msg.attach(part)
        except Exception as e:
            print(f"Error attaching PDF: {e}")
            raise
        
        # Send email via Gmail SMTP
        try:
            print(f"Connecting to Gmail SMTP server: {self.smtp_server}:{self.smtp_port}")
            print(f"Connection type: TLS (STARTTLS)")
            
            # Gmail uses TLS on port 587
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()  # Upgrade to secure TLS connection
            server.login(self.sender_email, self.sender_password)
            
            text = msg.as_string()
            server.sendmail(self.sender_email, recipient_email, text)
            server.quit()
            
            print(f"Email sent successfully to {recipient_email}")
            
        except Exception as e:
            print(f"Error sending email: {e}")
            raise


def main():
    """Main execution function."""
    
    # Use the input parameters defined at the top of the file
    TARGET_FOLDER = target_folder
    RECIPIENT_EMAIL = recipient_email
    SMTP_SERVER = smtp_server
    SMTP_PORT = smtp_port
    SENDER_EMAIL = sender_email
    SENDER_PASSWORD = sender_password
    
    # Generate unique PDF filename with timestamp
    # Format: folder_analysis_report - YYYY-MM-DD HH.MM.SS.pdf
    timestamp = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
    
    # Parse the original output_pdf path
    pdf_path = Path(output_pdf)
    pdf_directory = pdf_path.parent
    
    # Create new filename with timestamp
    new_filename = f'folder_analysis_report - {timestamp}.pdf'
    OUTPUT_PDF = str(pdf_directory / new_filename)
    
    try:
        # Step 1 & 2: Scan folder
        print("=" * 60)
        print("FOLDER ANALYSIS WORKFLOW")
        print("=" * 60)
        
        analyzer = FolderAnalyzer(TARGET_FOLDER)
        analyzer.scan_folder()
        
        # Step 3: Generate PDF report
        print("\n" + "=" * 60)
        print("GENERATING REPORT")
        print("=" * 60)
        
        report_gen = ReportGenerator(analyzer, OUTPUT_PDF)
        report_gen.generate_pdf()
        
        # Step 4: Email the report via Gmail
        print("\n" + "=" * 60)
        print("SENDING EMAIL VIA GMAIL")
        print("=" * 60)
        
        email_sender = EmailSender(SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD)
        email_sender.send_report(RECIPIENT_EMAIL, OUTPUT_PDF)
        
        print("\n" + "=" * 60)
        print("WORKFLOW COMPLETED SUCCESSFULLY!")
        print("=" * 60)
        
    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == '__main__':
    exit(main())
