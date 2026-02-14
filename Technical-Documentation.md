# Folder Analysis Report Generator - Technical Documentation

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)

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

<details>
<summary><b>🪟 Windows</b></summary>

```bash
- Download Python 3.7+ from [python.org](https://www.python.org/downloads/)
- **IMPORTANT:** During installation, check ✅ "Add Python to PATH"
- Click "Install Now"
```
</details>

<details>
<summary><b>🍎 Mac</b></summary>

```bash
- **Option 1:** Download from [python.org](https://www.python.org/downloads/)
- **Option 2:** Use Homebrew: `brew install python3`
```
</details>

<details>
<summary><b>🐧 Linux</b></summary>

```bash
- Most distributions come with Python pre-installed
- **Ubuntu/Debian:** `sudo apt-get install python3 python3-pip`
- **Fedora:** `sudo dnf install python3 python3-pip`
```
</details>

### **2. Install Dependencies**

**Windows:**
```bash
pip install matplotlib reportlab
# If pip doesn't work:
python -m pip install matplotlib reportlab
```

**Mac:**
```bash
pip3 install matplotlib reportlab
# If you get permission errors:
pip3 install --user matplotlib reportlab
```

**Linux:**
```bash
pip3 install matplotlib reportlab
# Or use system package manager (easier):
# Ubuntu/Debian:
sudo apt-get install python3-matplotlib python3-reportlab
# Fedora:
sudo dnf install python3-matplotlib
pip3 install reportlab
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

**Windows:**
```bash
# Method 1: Command Prompt
python folder_report_generator.py

# Method 2: Double-click the .py file
# Right-click → Open with → Python

# Method 3: PowerShell
python folder_report_generator.py
```

**Mac:**
```bash
# Open Terminal and navigate to script location
cd /Users/yourname/Downloads
python3 folder_report_generator.py
```

**Linux:**
```bash
# Open Terminal and navigate to script location
cd /home/yourname/Downloads
python3 folder_report_generator.py

# Or make it executable:
chmod +x folder_report_generator.py
./folder_report_generator.py
```

That's it! The script will:
1. Scan your folder ✅
2. Generate a PDF report ✅
3. Email it to the recipient ✅

---

## 🚦 Success Status Indicator

When running, you'll see the following example of a success status indicator:
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

### **Understanding Raw Strings vs Regular Strings (Windows Users)**

**The Problem:**
Windows paths use backslashes `\`, but backslashes are special characters in Python strings.

**Three Solutions:**

#### **Option 1: Forward Slashes (Recommended - Simplest)**
```python
# ✅ RECOMMENDED - Works on all platforms
target_folder = 'C:/Users/John/Documents'
output_pdf = 'C:/Users/John/Desktop/report.pdf'
```
**Why it works:** Python and Windows both accept forward slashes in paths.

#### **Option 2: Raw Strings (Use r prefix)**
```python
# ✅ Raw string - backslashes treated literally
target_folder = r'C:\Users\John\Documents'
output_pdf = r'C:\Users\John\Desktop\report.pdf'

# Notice the 'r' before the quote - this makes it a "raw string"
```
**What the 'r' does:** Tells Python to treat backslashes as literal characters, not escape sequences.

#### **Option 3: Double Backslashes**
```python
# ✅ Escape backslashes by doubling them
target_folder = 'C:\\Users\\John\\Documents'
output_pdf = 'C:\\Users\\John\\Desktop\\report.pdf'

# Each \\ becomes a single \ in the actual path
```

**Comparison:**

| Method | Example | Pros | Cons |
|--------|---------|------|------|
| **Forward Slashes** | `'C:/Users/John/Documents'` | ✅ Simple<br>✅ Works everywhere<br>✅ Easy to type | None |
| **Raw Strings** | `r'C:\Users\John\Documents'` | ✅ Looks like Windows paths<br>✅ Copy-paste from Explorer | ⚠️ Must remember 'r' prefix |
| **Double Backslashes** | `'C:\\Users\\John\\Documents'` | ✅ No prefix needed | ❌ Tedious to type<br>❌ Easy to forget one |

**Examples That Won't Work:**

```python
# ❌ WRONG - Single backslashes without 'r' prefix
target_folder = 'C:\Users\John\Documents'
# Python interprets \U as Unicode escape, causes error

# ❌ WRONG - Common mistake
target_folder = 'C:\New Folder\Data'
# \N is interpreted as escape sequence, causes error

# ❌ WRONG - Mixing styles
target_folder = 'C:/Users\John\Documents'
# Inconsistent, confusing
```

**Examples That Work:**

```python
# ✅ CORRECT - Forward slashes (RECOMMENDED)
target_folder = 'C:/Users/John/Documents'
target_folder = 'C:/Program Files/MyApp/data'
target_folder = 'D:/Backups/2024/February'

# ✅ CORRECT - Raw string
target_folder = r'C:\Users\John\Documents'
target_folder = r'C:\Program Files\MyApp\data'
target_folder = r'D:\Backups\2024\February'

# ✅ CORRECT - Double backslashes
target_folder = 'C:\\Users\\John\\Documents'
target_folder = 'C:\\Program Files\\MyApp\\data'
target_folder = 'D:\\Backups\\2024\\February'
```

**Quick Copy-Paste Guide:**

If you copy a path from Windows File Explorer:
```
C:\Users\John\Documents
```

Transform it using one of these methods:

**Method 1 (Easiest):**
```python
# Replace \ with /
target_folder = 'C:/Users/John/Documents'
```

**Method 2:**
```python
# Add r before the opening quote
target_folder = r'C:\Users\John\Documents'
```

**Method 3:**
```python
# Double every backslash
target_folder = 'C:\\Users\\John\\Documents'
```

**Mac/Linux Users:**
You don't have this issue! Just use paths as-is:
```python
# Mac
target_folder = '/Users/john/Documents'

# Linux
target_folder = '/home/john/Documents'
```

### **"pip is not recognized as an internal or external command" (Windows)**
**Problem:** pip not in system PATH

**Solutions:**
```bash
# Option 1: Use python -m pip
python -m pip install matplotlib reportlab

# Option 2: Reinstall Python
# Download from python.org and check "Add Python to PATH"

# Option 3: Add to PATH manually
# Search "Environment Variables" → Edit PATH → Add Python Scripts folder
```

### **"command not found: pip" (Mac/Linux)**
**Problem:** pip or pip3 not installed

**Mac Solutions:**
```bash
# Option 1: Use pip3
pip3 install matplotlib reportlab

# Option 2: Use python3 -m pip
python3 -m pip install matplotlib reportlab

# Option 3: Install pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```

**Linux Solutions:**
```bash
# Ubuntu/Debian
sudo apt-get install python3-pip
pip3 install matplotlib reportlab

# Fedora
sudo dnf install python3-pip
pip3 install matplotlib reportlab
```

### **"Username and Password not accepted"**
**All Platforms:**
- ❌ Using regular Gmail password
- ✅ Use Gmail App Password (16 characters)
- ✅ Enable 2-Factor Authentication first

### **"ModuleNotFoundError: No module named 'matplotlib'"**

**Windows:**
```bash
# Standard install
pip install matplotlib reportlab

# If that doesn't work
python -m pip install matplotlib reportlab

# Run as Administrator
# Right-click Command Prompt → Run as Administrator
pip install matplotlib reportlab
```

**Mac:**
```bash
# Standard install
pip3 install matplotlib reportlab

# With user flag (if permission denied)
pip3 install --user matplotlib reportlab

# Using Homebrew Python
brew install python3
pip3 install matplotlib reportlab
```

**Linux:**
```bash
# Option 1: System packages (recommended)
sudo apt-get install python3-matplotlib python3-reportlab  # Ubuntu/Debian
sudo dnf install python3-matplotlib; pip3 install reportlab  # Fedora

# Option 2: pip install
pip3 install matplotlib reportlab

# Option 3: With --break-system-packages (newer Linux)
pip3 install matplotlib reportlab --break-system-packages
```

### **"Permission denied" when scanning folders**

**Windows:**
```bash
# Run Command Prompt as Administrator
# Right-click Command Prompt → Run as Administrator
python folder_report_generator.py
```

**Mac:**
```bash
# Grant Full Disk Access
# System Preferences → Security & Privacy → Privacy → Full Disk Access
# Add Terminal or your Python IDE

# Or use a folder you own
target_folder = '/Users/yourname/Documents'
```

**Linux:**
```bash
# Use sudo only if analyzing system folders
sudo python3 folder_report_generator.py

# Better: Choose a folder you own
target_folder = '/home/yourname/Documents'
```

### **"FileNotFoundError" - Folder doesn't exist**

**Windows:**
```python
# ✅ Use forward slashes
target_folder = 'C:/Users/John/Documents'

# ✅ Or double backslashes
target_folder = 'C:\\Users\\John\\Documents'

# ❌ Don't use single backslashes
target_folder = 'C:\Users\John\Documents'  # Wrong!
```

**Mac:**
```python
# ✅ Full path starting with /Users
target_folder = '/Users/john/Documents'

# ✅ Can also use home directory
target_folder = '/Users/john/Desktop'
```

**Linux:**
```python
# ✅ Full path starting with /home
target_folder = '/home/john/Documents'

# ✅ Network mounts
target_folder = '/mnt/shared/projects'
```

### **Output PDF location issues**

**Windows:**
```python
# ✅ Desktop
output_pdf = 'C:/Users/YourName/Desktop/report.pdf'

# ✅ Documents
output_pdf = 'C:/Users/YourName/Documents/report.pdf'

# ✅ Temp folder (always works)
output_pdf = 'C:/Temp/report.pdf'
```

**Mac:**
```python
# ✅ Desktop
output_pdf = '/Users/yourname/Desktop/report.pdf'

# ✅ Documents
output_pdf = '/Users/yourname/Documents/report.pdf'

# ✅ Downloads
output_pdf = '/Users/yourname/Downloads/report.pdf'
```

**Linux:**
```python
# ✅ Desktop
output_pdf = '/home/yourname/Desktop/report.pdf'

# ✅ Home directory
output_pdf = '/home/yourname/report.pdf'

# ✅ Tmp (always writable)
output_pdf = '/tmp/report.pdf'
```

### **Email sent but not received**
**All Platforms:**
- Check spam/junk folder
- Verify `recipient_email` is correct
- Wait a few minutes (delays can happen)
- Gmail daily sending limit: ~100-500 emails

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

## 🖥️ Platform-Specific Quick Reference

### **Windows Users**

**Installation:**
```bash
# Install Python from python.org (check "Add to PATH"!)
pip install matplotlib reportlab
```

**Common Paths:**
```python
target_folder = 'C:/Users/YourName/Documents'
output_pdf = 'C:/Users/YourName/Desktop/report.pdf'
```

**Running:**
```bash
python folder_report_generator.py
# or double-click the .py file
```

**Tips:**
- ✅ Use `python -m pip` if pip doesn't work
- ✅ Run Command Prompt as Administrator for permissions
- ✅ Use forward slashes `/` in paths (not backslashes `\`)

### **Mac Users**

**Installation:**
```bash
# Option 1: From python.org
# Option 2: brew install python3
pip3 install matplotlib reportlab
```

**Common Paths:**
```python
target_folder = '/Users/yourname/Documents'
output_pdf = '/Users/yourname/Desktop/report.pdf'
```

**Running:**
```bash
python3 folder_report_generator.py
```

**Tips:**
- ✅ Use `pip3` instead of `pip`
- ✅ Use `python3` instead of `python`
- ✅ Grant Full Disk Access in System Preferences if needed
- ✅ Use `--user` flag if permission denied

### **Linux Users**

**Installation:**
```bash
# Ubuntu/Debian (recommended - uses system packages)
sudo apt-get install python3-matplotlib python3-reportlab

# Fedora
sudo dnf install python3-matplotlib
pip3 install reportlab
```

**Common Paths:**
```python
target_folder = '/home/yourname/Documents'
output_pdf = '/home/yourname/Desktop/report.pdf'
```

**Running:**
```bash
python3 folder_report_generator.py
# or make executable: chmod +x folder_report_generator.py
```

**Tips:**
- ✅ Use system package manager for easier installation
- ✅ Use `pip3` with `--break-system-packages` on newer distros
- ✅ Use `sudo` only if analyzing system folders
- ✅ Choose folders you own to avoid permission issues

---

## 👤 Author

- **Author:** Eric Jang
- **Email:** thericman05@gmail.com
- **LinkedIn:** [Connect with me](https://www.linkedin.com/in/eric-jang666/)

---

⭐ **If you find this useful, please consider starring the repository!**
