# 🚀 RDP Wrapper Installer by SrMoon

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](https://microsoft.com/windows)
[![GUI](https://img.shields.io/badge/GUI-CustomTkinter-orange.svg)](https://github.com/TomSchimansky/CustomTkinter)

> **Automated and intelligent installer for RDP Wrapper Library with modern graphical interface**

## 📋 About the Project

**RDP Wrapper Installer by SrMoon** is a complete and automated tool that dramatically simplifies the installation of RDP Wrapper Library on Windows. With a modern and intuitive graphical interface, the installer executes all necessary steps automatically, eliminating the manual complexity of the process.

### 🎯 Key Features

- ✅ **Modern Graphical Interface** - Built with CustomTkinter (dark theme)
- ✅ **Fully Automated Installation** - Zero manual intervention
- ✅ **Smart Desktop Detection** - OneDrive and standard Desktop support
- ✅ **Privileged Execution** - Automatic admin verification and request
- ✅ **Detailed Logs** - Follow each step in real-time
- ✅ **Credential Validation** - Intuitive interface for username/password
- ✅ **Automatic Downloads** - RDP Plus and necessary components
- ✅ **Optimized Sequence** - Correct installation order guaranteed

## 🔧 Features

### 🎮 Intuitive Interface
- **Modern Dark Theme** with CustomTkinter
- **Real-time Validation** of username and password
- **Visual Progress Bar** with detailed status
- **Colored Logs** for easy tracking

### 📁 Files Created
- **RDPConf.exe Shortcut** on desktop
- **RemoteDesktopPlus.exe** automatically downloaded
- **RDP User** configured and ready to use

## 🚀 How to Use

### Prerequisites
- Windows 10/11
- Internet connection
- Administrator privileges

### Installation
1. **Download** the latest executable from [Releases](../../releases) section
2. **Run** as administrator (mandatory)
3. **Configure** username and password in the interface
4. **Click** "Start Installation"
5. **Wait** for automatic completion
6. **Reboot** when prompted

### Post-Installation
After reboot, use the configured credentials to connect via RDP:
- **Server:** `127.0.0.2`
- **Username:** [configured by you]
- **Password:** [configured by you]

## 📸 Screenshots

### Main Interface
![Main Interface](https://files.catbox.moe/teky0x.png)

## 🔍 Technical Details

### Architecture
- **Language:** Python 3.13
- **GUI Framework:** CustomTkinter
- **Packaging:** PyInstaller
- **Execution:** Single executable (.exe)

### Installed Components
- **RDP Wrapper Library** v1.6.2 (official)
- **Autoupdate** v1.2 (community)
- **RDP Configuration Tool** (RDPConf.exe)
- **Remote Desktop Plus** (advanced RDP client)

### Execution Sequence
```bash
1. Registry Fix (ServiceDll)
2. update.bat (CMD admin)
3. install.bat (CMD admin)
4. autoupdate.bat (CMD admin - 2x)
5. Shortcuts & Downloads
6. Reboot Request
```

## 🤝 Credits

### Base Project
- **RDP Wrapper Library** - [Stas'M](https://github.com/stascorp/rdpwrap)
- **Autoupdate Script** - [asmtron](https://github.com/asmtron/rdpwrap)

### Tools Used
- **CustomTkinter** - [TomSchimansky](https://github.com/TomSchimansky/CustomTkinter)
- **Remote Desktop Plus** - [donkz](https://www.donkz.nl/)

### Developed by
**SrMoon** - Automation and Graphical Interface

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🛡️ Security & Antivirus Information

**⚠️ Important:** Some antivirus software may flag this tool as a false positive due to:
- PyInstaller packaging (common with Python executables)
- Administrative privileges requirement
- System registry modifications
- Batch file execution

**✅ This is completely normal and expected.** The tool is open source, and you can:
- Review all source code in this repository
- Build from source yourself using the provided Python script
- Check our [Security Information](SECURITY.md) for detailed analysis

**🔍 VirusTotal Status:** Typically 6-8 false positives out of 70+ engines (standard for PyInstaller)

## 🔨 Build from Source (For Security-Conscious Users)

**Don't trust pre-built executables?** No problem! You can compile your own EXE file from the source code. This tutorial is designed for **complete beginners** - no programming experience required!

### 📋 What You'll Need
- A Windows computer
- Internet connection
- 15-20 minutes of your time

### 🚀 Complete Step-by-Step Guide

#### Step 1: Install Python (If You Don't Have It)
1. **Download Python:**
   - Go to [python.org/downloads](https://python.org/downloads)
   - Click the big yellow "Download Python" button
   - This will download the latest version (3.12+)

2. **Install Python:**
   - Run the downloaded installer
   - ⚠️ **IMPORTANT**: Check the box "Add Python to PATH" at the bottom
   - Click "Install Now"
   - Wait for installation to complete

3. **Verify Installation:**
   - Press `Windows Key + R`
   - Type `cmd` and press Enter
   - Type `python --version` and press Enter
   - You should see something like "Python 3.12.x"

#### Step 2: Download the Source Code
**Option A: Easy Way (No Git Required)**
1. Click the green "Code" button at the top of this page
2. Click "Download ZIP"
3. Extract the ZIP file to your Desktop
4. You'll have a folder called "RDP-Wrapper-installer-main"

**Option B: Using Git (If You Have It)**
1. Open Command Prompt (`Windows Key + R`, type `cmd`)
2. Type: `git clone https://github.com/srmooon/RDP-Wrapper-installer.git`

#### Step 3: Install Required Libraries
1. **Open Command Prompt in the project folder:**
   - Navigate to the extracted folder
   - Hold `Shift` and right-click in the folder
   - Select "Open PowerShell window here" or "Open command window here"

2. **Install dependencies:**
   ```bash
   pip install customtkinter requests pywin32 pyinstaller
   ```
   *This will download and install all needed libraries*

#### Step 4: Compile Your EXE
1. **In the same command window, type:**
   ```bash
   pyinstaller --onefile --windowed rdp_wrapper_installer.py
   ```

2. **Wait for compilation** (this may take 2-5 minutes)

3. **Find your EXE:**
   - Look for a new folder called `dist`
   - Inside you'll find `rdp_wrapper_installer.exe`
   - **This is YOUR compiled version - 100% safe!**

### 🎯 Quick One-Command Method (Advanced Users)
```bash
pip install customtkinter requests pywin32 pyinstaller && pyinstaller --onefile --windowed rdp_wrapper_installer.py
```

### 🛡️ Why Compile Yourself?
- **🔒 Maximum Security**: You control the entire build process
- **🛡️ No False Positives**: Your antivirus won't flag your own compilation
- **✅ Source Code Verification**: You can review every line before compiling
- **🎯 Custom Modifications**: Modify the code if needed before compilation
- **🏆 Peace of Mind**: 100% certainty that your EXE is clean and safe

### 🔧 Troubleshooting Common Issues

**❌ "Python is not recognized"**
- Solution: Reinstall Python and make sure to check "Add Python to PATH"

**❌ "pip is not recognized"**
- Solution: Python wasn't installed correctly. Reinstall with PATH option checked

**❌ "No module named 'customtkinter'"**
- Solution: Run `pip install customtkinter requests pywin32 pyinstaller` again

**❌ Compilation takes too long**
- This is normal! First compilation can take 5-10 minutes depending on your computer

**❌ Antivirus blocks the compilation**
- Temporarily disable real-time protection during compilation
- Add the project folder to antivirus exclusions

**💡 Pro Tip:** After compilation, you can scan your own EXE with VirusTotal to confirm it's clean!

## ⚠️ Disclaimer

This software is provided "as is", without warranties. Use at your own risk. The developer is not responsible for damages caused by using this tool.

## 🔗 Useful Links

- [Original RDP Wrapper](https://github.com/stascorp/rdpwrap)
- [Autoupdate Community](https://github.com/asmtron/rdpwrap)
- [Remote Desktop Plus](https://www.donkz.nl/download/remote-desktop-plus/)
- [CustomTkinter Docs](https://customtkinter.tomschimansky.com/)

---

<div align="center">

**⭐ If this project was useful, consider giving it a star! ⭐**

Made with ❤️ by [SrMoon](https://github.com/srmooon)

</div>
