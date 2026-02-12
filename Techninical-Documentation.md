# Folder Analysis Report Generator - Technical Documentation

Automatically analyze folder contents, generate professional PDF reports with charts and tables, and email them using Gmail.

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)

---

## 🎯 What It Does

1. **Scans** any folder and all its subfolders
2. **Analyzes** file types and sizes
3. **Generates** a professional PDF report with:
   - Visual charts (bar graphs)
   - Detailed tables with statistics
   - Total file counts and sizes
4. **Emails** the report automatically via Gmail

**Perfect for:** Storage audits, project monitoring, backup planning, file organization.

---

## ✨ Features

- 📈 **Visual charts** - Top 10 file types by frequency
- 📋 **Detailed tables** - File counts, percentages, and total sizes
- 📊 **Size categories** - Files grouped as <1MB, 1MB-1GB, >1GB
- ⏱️ **Unique timestamps** - Every report has a unique identifier
- 📧 **Email automation** - Sends reports via Gmail SMTP
- 🎨 **Professional formatting** - Clean, readable PDF output

---

## 📋 Requirements

- **Python:** 3.7 or higher
- **Operating System:** Windows, Mac, Linux
- **Dependencies:** 
  - `matplotlib` (for charts)
  - `reportlab` (for PDF generation)
- **Email:** Gmail account for sending (recipient can be any email)

---

## 📦 Installation

### **1. Install Python**
Download Python 3.7+ from [python.org](https://www.python.org/downloads/)

### **2. Install Dependencies**
```bash
pip install matplotlib reportlab
```

### **3. Download the Script**
Download `folder_report_generator.py` from this repository.

---

## 🚀 Quick Start

### **Step 1: Set Up Gmail**

1. **Create a Gmail account** for automation (don't use your personal account!)
   - Example: `yourname.automation@gmail.com`

2. **Enable 2-Factor Authentication**
   - Go to: [Google Account Security](https://myaccount.google.com/security)

3. **Generate App Password**
   - Go to: [App Passwords](https://myaccount.google.com/apppasswords)
   - Select "Mail" and your device
   - Copy the 16-character password (e.g., `abcd efgh ijkl mnop`)

### **Step 2: Configure the Script**

Open `folder_report_generator.py` and edit these lines (18-31):

```python
# 1. Folder to analyze
target_folder = 'C:/Users/YourName/Documents'

# 2. Who receives the report (any email)
recipient_email = 'john.doe@company.com'

# 3. Gmail sender (your automation Gmail)
sender_email = 'yourname.automation@gmail.com'

# 4. Gmail App Password (16 characters with spaces)
sender_password = 'abcd efgh ijkl mnop'

# 5. Where to save the PDF
output_pdf = 'C:/Users/YourName/Desktop/report.pdf'
```

### **Step 3: Run the Script**

```bash
python folder_report_generator.py
```

That's it! The script will:
1. Scan your folder ✅
2. Generate a PDF report ✅
3. Email it to the recipient ✅

---

## 🚦 Sample Success Status Indicator

When running the py script, you'll see the following success status indicator:
```
============================================================
FOLDER ANALYSIS WORKFLOW
============================================================
Scanning folder: C:/Users/John/Documents
Found 1,247 files

============================================================
GENERATING REPORT
============================================================
PDF report generated successfully

============================================================
SENDING EMAIL VIA GMAIL
============================================================
Email sent successfully to john@company.com

============================================================
WORKFLOW COMPLETED SUCCESSFULLY!
============================================================
```

---

## 📊 Sample Report Output

```
┌─────────────────────────────────────────────────────────┐
│  Folder Analysis Report - 2024-02-13 14:30:00          │
│                                                          │
│  Target Folder: C:/Users/John/Documents                │
│  Total Files Found: 1,247                              │
│  Total File Size: 3.45 GB                              │
└─────────────────────────────────────────────────────────┘

Section 1: File Type Distribution (Top 10)
┌─────────────────────────────────────────────────┐
│  [Bar Chart - Visual Overview]                  │
│  .pdf      ████████████ 320                     │
│  .jpg      ██████████ 250                       │
│  .docx     ██████ 150                           │
└─────────────────────────────────────────────────┘

┌────────────────────────────────────────────────┐
│ File Type │ Count │ % │ Total Size            │
├───────────┼───────┼───┼───────────────────────┤
│ .pdf      │  320  │26%│ 1.23 GB               │
│ .jpg      │  250  │20%│ 890.45 MB             │
│ .docx     │  150  │12%│ 456.78 MB             │
└────────────────────────────────────────────────┘

Section 2: File Size Distribution
┌─────────────────────────────────────────────────┐
│  [Bar Chart]                                    │
│  <1MB      ████████████████████ 900             │
│  1MB-1GB   ██████ 330                           │
│  >1GB      █ 17                                 │
└─────────────────────────────────────────────────┘

┌────────────────────────────────────────────────┐
│ Category  │ Count │ % │ Total Size            │
├───────────┼───────┼───┼───────────────────────┤
│ <1MB      │  900  │72%│ 456.78 MB             │
│ 1MB-1GB   │  330  │26%│ 2.34 GB               │
│ >1GB      │   17  │ 1%│ 34.56 GB              │
└────────────────────────────────────────────────┘
```

---

## 🔧 Configuration Options

### **Required Settings:**

| Variable | Description | Example |
|----------|-------------|---------|
| `target_folder` | Folder to analyze | `'C:/Users/John/Documents'` |
| `recipient_email` | Who gets the report | `'john@company.com'` |
| `sender_email` | Gmail sender (must be Gmail) | `'automation@gmail.com'` |
| `sender_password` | Gmail App Password | `'abcd efgh ijkl mnop'` |
| `output_pdf` | Where to save PDF | `'C:/Desktop/report.pdf'` |

### **Path Examples:**

**Windows:**
```python
target_folder = 'C:/Users/John/Documents'
output_pdf = 'C:/Users/John/Desktop/report.pdf'
```

**Mac:**
```python
target_folder = '/Users/john/Documents'
output_pdf = '/Users/john/Desktop/report.pdf'
```

**Linux:**
```python
target_folder = '/home/john/Documents'
output_pdf = '/home/john/Desktop/report.pdf'
```

---

## 🆘 Troubleshooting

### **"pip is not recognized as an internal or external command"**
- **Problem:** pip not in system PATH
- **Solution:** Use `python -m pip` instead of `pip`
- **Permanent fix:** Reinstall Python and check "Add Python to PATH"

### **"Username and Password not accepted"**
- ❌ Using regular Gmail password
- ✅ Use Gmail App Password (16 characters)
- ✅ Enable 2-Factor Authentication first

### **"ModuleNotFoundError: No module named 'matplotlib'"**
```bash
pip install matplotlib reportlab
```

### **"FileNotFoundError" - Folder doesn't exist**
- Check that `target_folder` path is correct
- Use forward slashes `/` even on Windows

### **"Permission denied"**
- Choose a folder you have access to
- Save output to Desktop or Documents

### **Email sent but not received**
- Check spam/junk folder
- Verify `recipient_email` is correct
- Wait a few minutes (delays can happen)

---

## 💡 Use Cases

- **📁 Storage Audit:** See what's taking up space
- **🗂️ Project Monitoring:** Track file changes over time
- **💾 Backup Planning:** Understand what needs backing up
- **🧹 Cleanup Guide:** Identify files to archive/delete
- **📊 Team Reports:** Share folder statistics with colleagues
- **🔍 File Discovery:** Find file types you didn't know you had

---

## 🔐 Security Notes

### **Why Use a Dummy Gmail Account?**
- ✅ Protects your personal email
- ✅ Easy to disable if compromised
- ✅ Separates automation from personal use

### **Gmail App Password Security:**
- 🔒 Never share your App Password
- 🔒 Can be revoked anytime at [App Passwords](https://myaccount.google.com/apppasswords)
- 🔒 Each script should have its own App Password

---

## ⭐ Quick Examples

### **Example 1: Analyze Downloads Folder**
```python
target_folder = 'C:/Users/Sarah/Downloads'
recipient_email = 'sarah@gmail.com'
sender_email = 'sarahs.automation@gmail.com'
sender_password = 'wxyz abcd efgh ijkl'
output_pdf = 'C:/Users/Sarah/Desktop/downloads_report.pdf'
```

### **Example 2: Weekly Project Reports**
```python
target_folder = 'Z:/Projects/Website2024'
recipient_email = 'manager@company.com'
sender_email = 'reports.bot@gmail.com'
sender_password = 'mnop qrst uvwx yzab'
output_pdf = 'Z:/Reports/weekly_report.pdf'
```

### **Example 3: Multiple Recipients**
```python
target_folder = '/Users/john/Projects'
recipient_email = 'john@gmail.com,sarah@outlook.com,boss@yahoo.com'
sender_email = 'johns.automation@gmail.com'
sender_password = 'abcd efgh ijkl mnop'
output_pdf = '/Users/john/Desktop/report.pdf'
```

---

## 🎯 Features at a Glance

| Feature | Details |
|---------|---------|
| **File Analysis** | Scans all files in target folder and subfolders |
| **File Types** | Shows top 10 most common file types |
| **Size Categories** | Groups files as <1MB, 1MB-1GB, >1GB |
| **Visual Charts** | Bar charts for quick insights |
| **Detailed Tables** | Exact counts, percentages, total sizes |
| **PDF Export** | Professional, formatted PDF report |
| **Email Delivery** | Automatic email via Gmail SMTP |
| **Unique Reports** | Each report has timestamp identifier |

---

## 👤 Author

- **Author:** Eric Jang
- **Email:** thericman05@gmail.com
- **LinkedIn:** [Connect with me](https://www.linkedin.com/in/eric-jang666/)

---

⭐ **If you find this useful, please consider starring the repository!**
