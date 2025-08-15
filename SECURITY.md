# 🛡️ Security Information

## ⚠️ Antivirus False Positives

### Why Some Antivirus Software May Flag This Tool

**RDP Wrapper Installer** may trigger false positive detections from some antivirus software due to:

1. **PyInstaller Packaging** - Python executables are commonly flagged
2. **System Modifications** - The tool modifies Windows registry and system files
3. **Administrative Privileges** - Requires elevated permissions to function
4. **Network Downloads** - Downloads components from GitHub during installation
5. **Batch File Execution** - Runs .bat files as administrator

### 🔍 VirusTotal Analysis

Current detection status: **6/70+ engines** (typical for PyInstaller executables)

**Common False Positive Engines:**
- Generic heuristic scanners
- Behavior-based detection systems
- Engines that flag PyInstaller bootstraps

### ✅ Verification Steps

To verify the safety of this tool:

1. **Source Code Review** - All source code is available in this repository
2. **Build Process** - Executable built with standard PyInstaller
3. **No Obfuscation** - Code is not obfuscated or packed maliciously
4. **Open Source** - MIT License, fully transparent

### 🔒 What This Tool Actually Does

**Registry Modifications:**
- Configures RDP settings in Windows registry
- Sets ServiceDll parameter for Terminal Services
- Enables multiple RDP sessions

**File Operations:**
- Downloads official RDP Wrapper from GitHub
- Extracts files to `C:\Program Files\RDP Wrapper`
- Creates desktop shortcuts
- Downloads Remote Desktop Plus client

**Network Activity:**
- Downloads from trusted sources only:
  - `github.com/stascorp/rdpwrap` (official)
  - `github.com/asmtron/rdpwrap` (community)
  - `donkz.nl` (Remote Desktop Plus)

### 🚫 What This Tool Does NOT Do

- ❌ Does not connect to suspicious servers
- ❌ Does not install backdoors or malware
- ❌ Does not steal personal information
- ❌ Does not modify system files maliciously
- ❌ Does not hide its activities

### 🛠️ For Security-Conscious Users

If you're concerned about security:

1. **Review Source Code** - Check `rdp_wrapper_installer.py`
2. **Build From Source** - Use the provided Python script
3. **Run in VM** - Test in a virtual machine first
4. **Monitor Activity** - Use Process Monitor to watch file/registry changes

### 📞 Reporting Security Issues

If you discover a legitimate security issue:

1. **Do NOT** open a public issue
2. **Email** security concerns privately
3. **Provide** detailed information about the issue
4. **Allow** reasonable time for response

### 🔐 Building From Source

To build your own executable:

```bash
# Install dependencies
pip install customtkinter requests pyinstaller

# Build executable
pyinstaller --onefile --windowed rdp_wrapper_installer.py
```

### 🏷️ Digital Signatures

Currently, this tool is **not digitally signed** due to cost constraints of code signing certificates. This is common for open-source projects and contributes to antivirus false positives.

### ⚖️ Legal Disclaimer

This tool is provided "as-is" under MIT License. Users are responsible for:
- Ensuring compliance with local laws
- Understanding the security implications
- Using the tool at their own risk

---

**🔍 When in doubt, always review the source code and build from source yourself.**
