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

If you prefer to compile the executable yourself instead of downloading the pre-built version, follow these steps:

### Prerequisites
- **Python 3.8+** installed on your system
- **Git** (optional, for cloning)

### Step-by-Step Compilation Guide

1. **Clone or Download the Repository**
   ```bash
   git clone https://github.com/srmooon/RDP-Wrapper-installer.git
   cd RDP-Wrapper-installer
   ```
   *Or download and extract the ZIP from the green "Code" button above*

2. **Install Required Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install PyInstaller** (if not included in requirements)
   ```bash
   pip install pyinstaller
   ```

4. **Compile to Executable**
   ```bash
   pyinstaller --onefile --windowed --icon=icon.ico rdp_wrapper_installer.py
   ```
   *Note: If you don't have an icon file, remove the `--icon=icon.ico` part*

5. **Find Your Compiled EXE**
   - The executable will be created in the `dist/` folder
   - File name: `rdp_wrapper_installer.exe`
   - This is YOUR personally compiled version - 100% safe!

### Alternative One-Line Compilation
```bash
pyinstaller --onefile --windowed rdp_wrapper_installer.py
```

### Why Compile Yourself?
- **🔒 Maximum Security**: You control the entire build process
- **🛡️ No False Positives**: Your antivirus won't flag your own compilation
- **✅ Source Code Verification**: You can review every line before compiling
- **🎯 Custom Modifications**: Modify the code if needed before compilation

**💡 Pro Tip:** After compilation, you can even scan your own EXE with VirusTotal to confirm it's clean!

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
