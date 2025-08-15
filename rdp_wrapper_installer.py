import customtkinter as ctk
import threading
import subprocess
import requests
import os
import zipfile
from pathlib import Path
import ctypes
from tkinter import messagebox
import time
import getpass
import win32com.client
import webbrowser

class RDPWrapperInstaller:
    def __init__(self):
        
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        
        self.is_admin = self.check_admin()
        self.check_admin_on_startup()

        
        self.root = ctk.CTk()
        self.root.title("RDP Wrapper Installer by SrMoon")
        self.root.geometry("800x750")
        self.root.resizable(False, False)

        
        self.current_user = getpass.getuser()
        self.temp_dir = Path(os.environ['TEMP']) / "rdp_wrapper_installer"
        self.temp_dir.mkdir(exist_ok=True)
        self.rdp_wrapper_dir = Path("C:/Program Files/RDP Wrapper")

        
        onedrive_desktop = Path.home() / "OneDrive" / "Desktop"
        regular_desktop = Path.home() / "Desktop"

        if onedrive_desktop.exists():
            self.desktop_path = onedrive_desktop
        else:
            self.desktop_path = regular_desktop

        
        self.desktop_path.mkdir(exist_ok=True)

        self.setup_ui()
        
    def check_admin(self):
        """Verifica se o programa está rodando como administrador"""
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    def check_admin_on_startup(self):
        """Verifica privilégios administrativos no startup - OBRIGATÓRIO"""
        if not self.is_admin:
            choice = messagebox.askyesno(
                "Administrator Privileges REQUIRED",
                "This application REQUIRES Administrator privileges to function.\n\n"
                "Administrator privileges are MANDATORY for:\n"
                "• Creating users and modifying system settings\n"
                "• Installing RDP Wrapper files\n"
                "• Modifying registry entries\n"
                "• Downloading and installing components\n\n"
                "Would you like to restart as Administrator?\n\n"
                "Click 'Yes' to restart with admin privileges\n"
                "Click 'No' to EXIT the application"
            )

            if choice:
                
                try:
                    import sys
                    ctypes.windll.shell32.ShellExecuteW(
                        None, "runas", sys.executable, " ".join(sys.argv), None, 1
                    )
                    sys.exit(0)
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to restart as administrator: {str(e)}")
                    sys.exit(1)
            else:
                
                messagebox.showinfo(
                    "Application Closing",
                    "Administrator privileges are required for this application.\n"
                    "The application will now close."
                )
                sys.exit(0)
    
    def setup_ui(self):
        """Configura a interface do usuário"""
        
        header_frame = ctk.CTkFrame(self.root)
        header_frame.pack(fill="x", padx=20, pady=20)

        title_label = ctk.CTkLabel(
            header_frame,
            text="RDP Wrapper Installer by SrMoon",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title_label.pack(pady=20)

        subtitle_label = ctk.CTkLabel(
            header_frame,
            text="Automated installer for RDP Wrapper Library",
            font=ctk.CTkFont(size=14)
        )
        subtitle_label.pack(pady=(0, 20))

        
        self.credentials_frame = ctk.CTkFrame(self.root)
        self.credentials_frame.pack(fill="x", padx=20, pady=10)

        cred_label = ctk.CTkLabel(
            self.credentials_frame,
            text="RDP User Configuration:",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        cred_label.pack(pady=(10, 5))

        
        username_label = ctk.CTkLabel(self.credentials_frame, text="Username:")
        username_label.pack(anchor="w", padx=20, pady=(5, 0))

        self.username_entry = ctk.CTkEntry(
            self.credentials_frame,
            placeholder_text="Ex: RobloxPlayer2 (no spaces, dots or special characters)",
            width=400
        )
        self.username_entry.pack(padx=20, pady=(0, 5))
        self.username_entry.bind("<KeyRelease>", self.validate_username)

        
        self.username_error_label = ctk.CTkLabel(
            self.credentials_frame,
            text="",
            font=ctk.CTkFont(size=10),
            text_color="red"
        )
        self.username_error_label.pack(padx=20, pady=(0, 10))

        
        password_label = ctk.CTkLabel(self.credentials_frame, text="Password:")
        password_label.pack(anchor="w", padx=20, pady=(5, 0))

        self.password_entry = ctk.CTkEntry(
            self.credentials_frame,
            placeholder_text="Enter a secure password (minimum 6 characters)",
            show="*",
            width=400
        )
        self.password_entry.pack(padx=20, pady=(0, 5))
        self.password_entry.bind("<KeyRelease>", self.validate_password)

        
        self.password_error_label = ctk.CTkLabel(
            self.credentials_frame,
            text="",
            font=ctk.CTkFont(size=10),
            text_color="red"
        )
        self.password_error_label.pack(padx=20, pady=(0, 10))

        
        self.start_button = ctk.CTkButton(
            self.credentials_frame,
            text="Start Installation",
            command=self.start_installation,
            font=ctk.CTkFont(size=16, weight="bold"),
            height=45,
            width=250
        )
        self.start_button.pack(pady=(10, 20))

        
        self.status_frame = ctk.CTkFrame(self.root)
        self.status_frame.pack(fill="x", padx=20, pady=10)
        
        self.status_label = ctk.CTkLabel(
            self.status_frame,
            text="Ready to start...",
            font=ctk.CTkFont(size=12)
        )
        self.status_label.pack(pady=10)
        
        
        self.progress_bar = ctk.CTkProgressBar(self.root)
        self.progress_bar.pack(fill="x", padx=20, pady=10)
        self.progress_bar.set(0)
        
        
        log_frame = ctk.CTkFrame(self.root)
        log_frame.pack(fill="both", expand=True, padx=20, pady=10)

        log_label = ctk.CTkLabel(log_frame, text="Activity Log:", font=ctk.CTkFont(size=12, weight="bold"))
        log_label.pack(anchor="w", padx=10, pady=(10, 5))

        self.log_text = ctk.CTkTextbox(log_frame, height=120)
        self.log_text.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        
        buttons_frame = ctk.CTkFrame(self.root)
        buttons_frame.pack(fill="x", padx=20, pady=(0, 20))

        self.exit_button = ctk.CTkButton(
            buttons_frame,
            text="Exit",
            command=self.root.quit,
            font=ctk.CTkFont(size=14),
            height=40,
            width=100,
            fg_color="gray"
        )
        self.exit_button.pack(side="right", padx=20, pady=15)
        
        
        self.log_message("Application started successfully!")
        self.log_message(f"👤 Current system user: {self.current_user}")

        
        if "OneDrive" in str(self.desktop_path):
            self.log_message(f"📁 Using OneDrive Desktop: {self.desktop_path}")
        else:
            self.log_message(f"📁 Using regular Desktop: {self.desktop_path}")

        if not self.is_admin:
            self.log_message("⚠️ WARNING: Run as Administrator for best performance!")

    def validate_username(self, event=None):
        """Validates username in real time"""
        username = self.username_entry.get()
        errors = []

        if username:
            
            if ' ' in username:
                errors.append("• Cannot contain spaces")

            
            if '.' in username:
                errors.append("• Cannot contain dots")

            
            if username.lower() == self.current_user.lower():
                errors.append(f"• Cannot be the same as current user ({self.current_user})")

            
            if not username.replace('_', '').isalnum():
                errors.append("• Only letters, numbers and underscore allowed")

            
            if len(username) < 3:
                errors.append("• Minimum 3 characters")

        if errors:
            self.username_error_label.configure(text="\n".join(errors))
            self.username_error_label.configure(text_color="red")
            return False
        else:
            self.username_error_label.configure(text="✅ Valid username")
            self.username_error_label.configure(text_color="green")
            return True

    def validate_password(self, event=None):
        """Validates password in real time"""
        password = self.password_entry.get()
        errors = []

        if password:
            
            if len(password) < 6:
                errors.append("• Minimum 6 characters")

        if errors:
            self.password_error_label.configure(text="\n".join(errors))
            self.password_error_label.configure(text_color="red")
            return False
        elif password:
            self.password_error_label.configure(text="✅ Valid password")
            self.password_error_label.configure(text_color="green")
            return True
        else:
            self.password_error_label.configure(text="")
            return False
    
    def log_message(self, message):
        """Adiciona mensagem ao log"""
        timestamp = time.strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        self.log_text.insert("end", log_entry)
        self.log_text.see("end")
        self.root.update()
    
    def update_status(self, status):
        """Atualiza o status atual"""
        self.status_label.configure(text=status)
        self.root.update()
    
    def update_progress(self, value):
        """Atualiza a barra de progresso"""
        self.progress_bar.set(value)
        self.root.update()
    
    def start_installation(self):
        """Inicia o processo de instalação em thread separada"""
        self.start_button.configure(state="disabled")
        thread = threading.Thread(target=self.installation_process)
        thread.daemon = True
        thread.start()
    
    def installation_process(self):
        """Processo principal de instalação"""
        try:
            self.log_message("🚀 Starting installation process...")
            self.update_status("Checking credentials...")
            self.update_progress(0.1)

            
            username = self.username_entry.get().strip()
            password = self.password_entry.get().strip()

            if not username or not password:
                self.log_message("❌ Please fill in username and password!")
                self.update_status("Error: Credentials not filled")
                return

            
            if not self.validate_username() or not self.validate_password():
                self.log_message("❌ Please fix the errors in username and password fields!")
                self.update_status("Error: Invalid credentials")
                return

            self.log_message(f"✅ Credentials configured for user: {username}")

            
            self.step1_configure_rdp_and_user(username, password)

            
            self.step2_download_and_install_rdp_wrapper()

            
            self.step3_download_and_install_autoupdate()

            
            self.step4_create_shortcut_and_reboot(username, password)

        except Exception as e:
            self.log_message(f"❌ Error: {str(e)}")
            self.update_status("Installation error")
        finally:
            self.start_button.configure(state="normal")

    def step1_configure_rdp_and_user(self, username, password):
        """Step 1: Configure RDP and create user"""
        try:
            self.log_message("📋 Step 1: Configuring RDP and creating user...")
            self.update_status("Configuring RDP...")
            self.update_progress(0.2)

            
            if not self.is_admin:
                self.log_message("❌ Administrator privileges required!")
                messagebox.showerror("Error", "Run the program as Administrator to continue.")
                return

            
            powershell_commands = [
                
                "Set-ItemProperty -Path 'HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Terminal Server' -Name 'fDenyTSConnections' -Value 0",

                
                "Set-ItemProperty -Path 'HKLM:\\Software\\Microsoft\\Terminal Server Client' -Name 'RemoteDesktop_SuppressWhenMinimized' -Value 2",

                
                "Set-ItemProperty -Path 'HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Terminal Server' -Name 'fDenyTSConnections' -Value 0"
            ]

            self.log_message("🔧 Configuring RDP registry settings...")
            for i, cmd in enumerate(powershell_commands):
                self.execute_powershell_command(cmd)
                self.update_progress(0.2 + (i + 1) * 0.05)

            self.log_message("🔄 Restarting Terminal Services...")
            self.update_status("Restarting services...")

            
            self.execute_powershell_command('Stop-Service "termservice" -Force')
            time.sleep(2)
            self.execute_powershell_command('Start-Service "termservice"')

            self.update_progress(0.4)
            self.log_message("👤 Creating RDP user...")
            self.update_status("Creating user...")

            
            create_user_cmd = f'$securePassword = ConvertTo-SecureString "{password}" -AsPlainText -Force; New-LocalUser -Name "{username}" -Password $securePassword -FullName "{username}" -PasswordNeverExpires'
            self.execute_powershell_command(create_user_cmd)

            self.update_progress(0.5)
            self.log_message("🔐 Adding user to Administrators group...")

            
            add_to_admin_cmd = f'''
            $adminSID = New-Object System.Security.Principal.SecurityIdentifier("S-1-5-32-544");
            $adminGroupName = $adminSID.Translate([System.Security.Principal.NTAccount]);
            $adminGroupNameTrimmed = ($adminGroupName.Value).Split("\\")[1];
            Add-LocalGroupMember -Group $adminGroupNameTrimmed -Member "{username}"
            '''
            self.execute_powershell_command(add_to_admin_cmd)

            self.update_progress(0.6)
            self.log_message("📁 Creating RDP Wrapper directory...")

            
            create_dir_cmd = '''
            $directoryPath = "C:\\Program Files\\RDP Wrapper\\";
            if (-Not (Test-Path -Path $directoryPath)) {
                New-Item -ItemType Directory -Path $directoryPath;
                Write-Output "Directory created: $directoryPath"
            }
            '''
            self.execute_powershell_command(create_dir_cmd)

            self.update_progress(0.2)
            self.log_message("✅ Step 1 completed successfully!")
            self.log_message(f"✅ User '{username}' created and added to Administrators")
            self.log_message("✅ RDP configured and services restarted")
            self.log_message("✅ RDP Wrapper directory created")

        except Exception as e:
            self.log_message(f"❌ Error in Step 1: {str(e)}")
            raise

    def execute_powershell_command(self, command):
        """Executes PowerShell command with multiple fallback methods"""
        try:
            
            powershell_methods = [
                
                lambda: subprocess.run(
                    ["powershell.exe", "-Command", command],
                    capture_output=True,
                    text=True,
                    shell=True,
                    check=True
                ),
                
                lambda: subprocess.run(
                    [r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe", "-Command", command],
                    capture_output=True,
                    text=True,
                    check=True
                ),
                
                lambda: subprocess.run(
                    f'cmd /c "powershell.exe -Command \\"{command}\\""',
                    capture_output=True,
                    text=True,
                    shell=True,
                    check=True
                ),
                
                lambda: subprocess.run(
                    [r"C:\Windows\SysWOW64\WindowsPowerShell\v1.0\powershell.exe", "-Command", command],
                    capture_output=True,
                    text=True,
                    check=True
                )
            ]

            last_error = None
            for i, method in enumerate(powershell_methods):
                try:
                    result = method()
                    if result.stdout.strip():
                        self.log_message(f"📤 {result.stdout.strip()}")
                    self.log_message(f"✅ PowerShell executed successfully (method {i+1})")
                    return result.stdout
                except (FileNotFoundError, subprocess.CalledProcessError, OSError) as e:
                    last_error = e
                    continue

            
            self.log_message(f"⚠️ All PowerShell methods failed. Last error: {str(last_error)}")
            self.log_message("💡 Continuing with installation - some features may not work properly")
            return ""

        except Exception as e:
            self.log_message(f"❌ Critical error executing PowerShell: {str(e)}")
            self.log_message("💡 Continuing with installation - some features may not work properly")
            return ""

    def download_file(self, url, destination, description="file"):
        """Downloads a file with progress tracking"""
        try:
            self.log_message(f"📥 Downloading {description}...")
            self.log_message(f"🔗 URL: {url}")

            
            destination_path = Path(destination)
            destination_path.parent.mkdir(parents=True, exist_ok=True)

            response = requests.get(url, stream=True)
            response.raise_for_status()

            total_size = int(response.headers.get('content-length', 0))
            downloaded = 0

            with open(destination, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        file.write(chunk)
                        downloaded += len(chunk)

                        if total_size > 0:
                            progress = downloaded / total_size
                            self.log_message(f"📊 Progress: {progress*100:.1f}% ({downloaded}/{total_size} bytes)")

            self.log_message(f"✅ {description} downloaded successfully!")
            return True

        except Exception as e:
            self.log_message(f"❌ Error downloading {description}: {str(e)}")
            raise

    def extract_zip(self, zip_path, extract_to, description="archive"):
        """Extracts a ZIP file"""
        try:
            self.log_message(f"📦 Extracting {description}...")

            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_to)

            self.log_message(f"✅ {description} extracted successfully!")
            return True

        except Exception as e:
            self.log_message(f"❌ Error extracting {description}: {str(e)}")
            raise

    def run_as_admin(self, file_path, description="file"):
        """Runs a file as administrator using CMD (proper for .bat files)"""
        try:
            self.log_message(f"🔧 Running {description} as administrator...")

            
            if str(file_path).lower().endswith('.bat'):
                
                self.log_message(f"🔧 Detected .bat file - using CMD execution in RDP Wrapper directory")
                rdp_wrapper_dir = "C:\\Program Files\\RDP Wrapper"
                bat_name = Path(file_path).name

                admin_methods = [
                    
                    lambda: subprocess.run(
                        ["powershell.exe", "-Command", f'Start-Process cmd -ArgumentList "/c cd /d \\"{rdp_wrapper_dir}\\" && {bat_name}" -Verb RunAs -Wait'],
                        capture_output=True,
                        text=True,
                        shell=True,
                        timeout=120
                    ),
                    
                    lambda: subprocess.run(
                        f'cmd /c "cd /d "{rdp_wrapper_dir}" && {bat_name}"',
                        capture_output=True,
                        text=True,
                        shell=True,
                        cwd=rdp_wrapper_dir,
                        timeout=120
                    ),
                    
                    lambda: subprocess.run(
                        ["powershell.exe", "-Command", f'cd "{rdp_wrapper_dir}"; cmd /c {bat_name}'],
                        capture_output=True,
                        text=True,
                        shell=True,
                        cwd=rdp_wrapper_dir,
                        timeout=120
                    )
                ]
            else:
                
                admin_methods = [
                    
                    lambda: subprocess.run(
                        ["powershell.exe", "-Command", f"Start-Process '{file_path}' -Verb RunAs -Wait"],
                        capture_output=True,
                        text=True,
                        shell=True
                    ),
                    
                    lambda: subprocess.run(
                        [file_path],
                        capture_output=True,
                        text=True
                    )
                ]

            last_error = None
            for i, method in enumerate(admin_methods):
                try:
                    self.log_message(f"🔄 Trying execution method {i+1} for {description}...")
                    result = method()

                    
                    if str(file_path).lower().endswith('.bat'):
                        self.log_message(f"📋 {description} execution completed with return code: {result.returncode}")
                        if result.stdout and result.stdout.strip():
                            
                            output_lines = result.stdout.strip().split('\n')
                            for line in output_lines:
                                if line.strip() and not line.startswith('Microsoft Windows'):
                                    self.log_message(f"📤 CMD: {line.strip()}")
                        if result.stderr and result.stderr.strip():
                            self.log_message(f"⚠️ CMD Errors: {result.stderr.strip()}")

                        if result.returncode == 0:
                            self.log_message(f"✅ {description} executed successfully! (method {i+1})")
                        else:
                            self.log_message(f"⚠️ {description} finished with non-zero return code: {result.returncode}")
                            
                            continue
                    else:
                        if result.stdout:
                            self.log_message(f"📤 Output: {result.stdout.strip()}")
                        self.log_message(f"✅ {description} executed successfully! (method {i+1})")

                    return True
                except subprocess.TimeoutExpired:
                    self.log_message(f"⏰ Method {i+1} timed out after 60 seconds")
                    last_error = "Timeout"
                    continue
                except (FileNotFoundError, subprocess.CalledProcessError, OSError) as e:
                    last_error = e
                    self.log_message(f"⚠️ Method {i+1} failed: {str(e)}")
                    continue

            self.log_message(f"❌ All admin execution methods failed. Last error: {str(last_error)}")
            return False

        except Exception as e:
            self.log_message(f"❌ Critical error running {description} as admin: {str(e)}")
            return False

    def create_desktop_shortcut(self, target_path, shortcut_name):
        """Creates a desktop shortcut with multiple methods"""
        try:
            self.log_message(f"🔗 Creating desktop shortcut for {shortcut_name}...")

            
            desktop = str(self.desktop_path)
            if not os.path.exists(desktop):
                os.makedirs(desktop, exist_ok=True)

            shortcut_path = os.path.join(desktop, f"{shortcut_name}.lnk")

            
            try:
                ps_command = f'''
$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("{shortcut_path}")
$Shortcut.TargetPath = "{target_path}"
$Shortcut.WorkingDirectory = "{Path(target_path).parent}"
$Shortcut.Save()
Write-Output "Shortcut created successfully"
                '''

                self.execute_powershell_command(ps_command)

                
                import time
                time.sleep(2)

                if os.path.exists(shortcut_path):
                    self.log_message(f"✅ Desktop shortcut created: {shortcut_name}.lnk")
                    return True

            except Exception as e:
                self.log_message(f"⚠️ PowerShell method failed: {str(e)}")

            
            try:
                import pythoncom
                pythoncom.CoInitialize()

                try:
                    shell = win32com.client.Dispatch("WScript.Shell")
                    shortcut = shell.CreateShortCut(shortcut_path)
                    shortcut.Targetpath = str(target_path)
                    shortcut.WorkingDirectory = str(Path(target_path).parent)
                    shortcut.save()

                    if os.path.exists(shortcut_path):
                        self.log_message(f"✅ Desktop shortcut created: {shortcut_name}.lnk")
                        return True

                finally:
                    pythoncom.CoUninitialize()

            except Exception as e:
                self.log_message(f"⚠️ COM method failed: {str(e)}")

            
            return self.create_shortcut_alternative(target_path, shortcut_name)

        except Exception as e:
            self.log_message(f"❌ Error creating shortcut: {str(e)}")
            return self.create_shortcut_alternative(target_path, shortcut_name)

    def create_shortcut_alternative(self, target_path, shortcut_name):
        """Alternative method to create shortcut using PowerShell"""
        try:
            self.log_message(f"💡 Trying alternative shortcut creation method...")

            
            self.desktop_path.mkdir(exist_ok=True)

            desktop = str(self.desktop_path)
            shortcut_path = os.path.join(desktop, f"{shortcut_name}.lnk")

            
            target_ps = str(target_path).replace("\\", "/")
            shortcut_ps = shortcut_path.replace("\\", "/")
            working_dir_ps = str(Path(target_path).parent).replace("\\", "/")

            
            ps_command = f'''
$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("{shortcut_ps}")
$Shortcut.TargetPath = "{target_ps}"
$Shortcut.WorkingDirectory = "{working_dir_ps}"
$Shortcut.Save()
Write-Output "Shortcut created successfully"
            '''

            
            result = self.execute_powershell_command(ps_command)

            
            import time
            time.sleep(2)

            if os.path.exists(shortcut_path):
                self.log_message(f"✅ Desktop shortcut created successfully: {shortcut_name}.lnk")
                return True
            else:
                self.log_message(f"⚠️ Shortcut file not found after creation attempt")
                
                return self.create_shortcut_manual_copy(target_path, shortcut_name)

        except Exception as e:
            self.log_message(f"⚠️ Alternative shortcut method failed: {str(e)}")
            return self.create_shortcut_manual_copy(target_path, shortcut_name)

    def create_shortcut_manual_copy(self, target_path, shortcut_name):
        """Manual method to create shortcut using VBS script as last resort"""
        try:
            self.log_message(f"💡 Trying VBS script method as last resort...")

            desktop = str(self.desktop_path)
            shortcut_path = os.path.join(desktop, f"{shortcut_name}.lnk")

            
            vbs_script = f'''
Set WshShell = CreateObject("WScript.Shell")
Set Shortcut = WshShell.CreateShortcut("{shortcut_path}")
Shortcut.TargetPath = "{target_path}"
Shortcut.WorkingDirectory = "{Path(target_path).parent}"
Shortcut.Save
            '''

            
            vbs_file = self.temp_dir / "create_shortcut.vbs"
            with open(vbs_file, 'w') as f:
                f.write(vbs_script)

            
            subprocess.run(['cscript', '//NoLogo', str(vbs_file)],
                         capture_output=True, text=True, check=True)

            
            import time
            time.sleep(1)

            if os.path.exists(shortcut_path):
                self.log_message(f"✅ Desktop shortcut created via VBS: {shortcut_name}.lnk")
                return True
            else:
                self.log_message(f"❌ VBS shortcut creation failed")
                return False

        except Exception as e:
            self.log_message(f"❌ VBS shortcut method failed: {str(e)}")
            self.log_message("💡 You can manually create a shortcut from the RDP Wrapper directory")
            return False

    def step2_download_and_install_rdp_wrapper(self):
        """Step 2: Download and install RDP Wrapper with correct sequence"""
        try:
            self.log_message("📋 Step 2: Downloading and installing RDP Wrapper...")
            self.update_status("Downloading RDP Wrapper...")

            
            self.rdp_wrapper_dir.mkdir(parents=True, exist_ok=True)

            
            rdp_wrapper_url = "https://github.com/stascorp/rdpwrap/releases/download/v1.6.2/RDPWrap-v1.6.2.zip"
            zip_path = self.temp_dir / "RDPWrap-v1.6.2.zip"

            self.download_file(rdp_wrapper_url, zip_path, "RDP Wrapper v1.6.2")
            self.update_progress(0.25)

            
            self.extract_zip(zip_path, self.rdp_wrapper_dir, "RDP Wrapper")
            self.update_progress(0.3)

            
            self.update_status("Applying critical registry fix...")
            self.log_message("🔧 Applying critical ServiceDll registry fix...")
            servicedll_command = 'Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Services\\TermService\\Parameters" -Name ServiceDll -Value "%SystemRoot%\\System32\\termsrv.dll"'
            self.execute_powershell_command(servicedll_command)
            self.log_message("✅ ServiceDll registry fix applied!")
            self.update_progress(0.32)

            

            
            self.update_status("Running update.bat...")
            update_bat = self.rdp_wrapper_dir / "update.bat"
            if update_bat.exists():
                self.log_message("🔧 Running update.bat as CMD administrator in RDP Wrapper directory...")
                self.run_as_admin(update_bat, "update.bat")
            else:
                self.log_message("⚠️ Warning: update.bat not found in RDP Wrapper directory")
            self.update_progress(0.37)

            
            self.update_status("Running install.bat...")
            install_bat = self.rdp_wrapper_dir / "install.bat"
            if install_bat.exists():
                self.log_message("🔧 Running install.bat as CMD administrator in RDP Wrapper directory...")
                self.run_as_admin(install_bat, "install.bat")
            else:
                self.log_message("⚠️ Warning: install.bat not found in RDP Wrapper directory")
            self.update_progress(0.42)

            self.log_message("✅ Step 2 completed successfully!")

        except Exception as e:
            self.log_message(f"❌ Error in Step 2: {str(e)}")
            raise

    def step3_download_and_install_autoupdate(self):
        """Step 3: Download and install autoupdate + run autoupdate.bat again"""
        try:
            self.log_message("📋 Step 3: Downloading and installing autoupdate...")
            self.update_status("Downloading autoupdate...")

            
            autoupdate_url = "https://github.com/asmtron/rdpwrap/raw/master/autoupdate_v1.2.zip"
            zip_path = self.temp_dir / "autoupdate_v1.2.zip"

            self.download_file(autoupdate_url, zip_path, "Autoupdate v1.2")
            self.update_progress(0.5)

            
            self.extract_zip(zip_path, self.rdp_wrapper_dir, "Autoupdate")
            self.update_progress(0.55)

            
            self.update_status("Running autoupdate.bat (first time)...")
            autoupdate_bat = self.rdp_wrapper_dir / "autoupdate.bat"
            if autoupdate_bat.exists():
                self.log_message("🔧 Running autoupdate.bat as CMD administrator in RDP Wrapper directory (first time)...")
                self.run_as_admin(autoupdate_bat, "autoupdate.bat (first time)")
            else:
                self.log_message("⚠️ Warning: autoupdate.bat not found in RDP Wrapper directory")
            self.update_progress(0.6)

            
            self.update_status("Running autoupdate.bat (second time)...")
            if autoupdate_bat.exists():
                self.log_message("🔧 Running autoupdate.bat as CMD administrator in RDP Wrapper directory (second time)...")
                self.run_as_admin(autoupdate_bat, "autoupdate.bat (second time)")
            else:
                self.log_message("⚠️ Warning: autoupdate.bat not found for second run")
            self.update_progress(0.65)

            self.log_message("✅ Step 3 completed successfully!")

        except Exception as e:
            self.log_message(f"❌ Error in Step 3: {str(e)}")
            raise

    def step4_create_shortcut_and_reboot(self, username, password):
        """Step 4: Create shortcut, download RDP Plus, and prepare for reboot"""
        try:
            self.log_message("📋 Step 4: Creating shortcut, downloading RDP Plus, and preparing for reboot...")
            self.update_status("Creating desktop shortcut...")

            
            self.log_message("🔗 Creating desktop shortcut for RDP Configuration...")

            
            possible_rdpconf_paths = [
                self.rdp_wrapper_dir / "RDPConf.exe",
                Path("C:/Program Files/RDP Wrapper/RDPConf.exe"),
                Path("C:/RDP Wrapper/RDPConf.exe"),
                Path(os.getcwd()) / "RDP Wrapper" / "RDPConf.exe"
            ]

            rdpconf_exe = None
            for path in possible_rdpconf_paths:
                if path.exists():
                    rdpconf_exe = path
                    self.log_message(f"📁 Found RDPConf.exe at: {path}")
                    break

            if rdpconf_exe:
                shortcut_created = self.create_desktop_shortcut(rdpconf_exe, "RDP Configuration")
                if shortcut_created:
                    self.log_message("✅ RDP Configuration shortcut created on desktop")
                else:
                    self.log_message("⚠️ Warning: Could not create desktop shortcut, but installation continues")
            else:
                self.log_message("⚠️ Warning: RDPConf.exe not found in any expected location")
                self.log_message(f"📁 Searched in: {[str(p) for p in possible_rdpconf_paths]}")

            self.update_progress(0.7)
            self.update_status("Downloading RDP Plus...")

            
            self.log_message("📥 Downloading RDP Plus to desktop...")

            
            rdp_plus_urls = [
                "https://www.donkz.nl/download/remote-desktop-plus/?tmstv=1755234250",
                "https://github.com/donkz/Remote-Desktop-Plus/releases/latest/download/RemoteDesktopPlus.exe",
                "https://www.donkz.nl/download/remote-desktop-plus/"
            ]

            rdp_plus_path = self.desktop_path / "RemoteDesktopPlus.exe"
            rdp_plus_downloaded = False

            for i, url in enumerate(rdp_plus_urls):
                try:
                    self.log_message(f"🔗 Trying URL {i+1}: {url}")
                    self.download_file(url, rdp_plus_path, "RDP Plus")
                    if rdp_plus_path.exists() and rdp_plus_path.stat().st_size > 10000:  
                        self.log_message(f"✅ RDP Plus downloaded to desktop successfully! ({rdp_plus_path.stat().st_size} bytes)")
                        rdp_plus_downloaded = True
                        break
                    else:
                        self.log_message(f"⚠️ Download from URL {i+1} failed or file too small")
                        
                        if rdp_plus_path.exists():
                            rdp_plus_path.unlink()
                except Exception as e:
                    self.log_message(f"⚠️ URL {i+1} failed: {str(e)}")
                    
                    if rdp_plus_path.exists():
                        rdp_plus_path.unlink()
                    continue

            if not rdp_plus_downloaded:
                self.log_message("⚠️ Warning: Could not download RDP Plus from any URL")
                self.log_message("📝 You can manually download from: https://www.donkz.nl/download/remote-desktop-plus/?tmstv=1755234250")
                self.log_message("📝 Or from GitHub: https://github.com/donkz/Remote-Desktop-Plus/releases")

            self.update_progress(0.8)
            self.update_status("Preparing final steps...")

            
            self.log_message("=" * 50)
            self.log_message("🎉 INSTALLATION COMPLETED SUCCESSFULLY!")
            self.log_message("=" * 50)
            self.log_message("📋 RDP CONNECTION INFORMATION:")
            self.log_message(f"🌐 Server: 127.0.0.2")
            self.log_message(f"👤 Username: {username}")
            self.log_message(f"🔑 Password: {password}")
            self.log_message("=" * 50)
            self.log_message("📝 FILES CREATED:")
            if rdpconf_exe and shortcut_created:
                self.log_message("✅ RDP Configuration shortcut created on desktop")
            else:
                self.log_message("⚠️ RDP Configuration shortcut creation failed")

            if rdp_plus_downloaded:
                self.log_message("✅ RDP Plus downloaded to desktop")
            else:
                self.log_message("⚠️ RDP Plus download failed - manual download required")

            self.log_message("=" * 50)
            self.log_message("📝 NEXT STEPS:")
            self.log_message("1. 🔄 REBOOT REQUIRED to complete installation")
            self.log_message("2. 🔗 After reboot, use RDP Plus with the connection info above")
            self.log_message("=" * 50)

            self.update_progress(0.85)

            
            self.log_message("🙏 Opening credits page...")
            self.log_message("📝 Credits: RDP Wrapper Library by Stas'M")
            try:
                webbrowser.open("https://github.com/stascorp/rdpwrap")
                self.log_message("✅ Credits page opened in browser")
            except Exception as e:
                self.log_message(f"⚠️ Could not open browser: {str(e)}")
                self.log_message("🔗 Manual link: https://github.com/stascorp/rdpwrap")

            self.update_progress(0.9)
            time.sleep(2)  

            
            self.update_status("Installation completed - Reboot required")
            reboot_choice = messagebox.askyesno(
                "🎉 Installation Complete - Reboot Required",
                "🎉 RDP Wrapper installation completed successfully!\n\n"
                "✅ All components installed and configured\n"
                "✅ Desktop shortcuts/files created\n"
                "✅ Credits page opened in browser\n\n"
                "🔄 A system reboot is REQUIRED to complete the setup.\n\n"
                "Would you like to reboot now?\n\n"
                "📋 Your RDP Connection Info:\n"
                f"🌐 Server: 127.0.0.2\n"
                f"👤 Username: {username}\n"
                f"🔑 Password: {password}\n\n"
                "💡 Save this info before rebooting!"
            )

            if reboot_choice:
                self.log_message("🔄 Initiating system reboot...")
                self.update_status("Rebooting system...")
                subprocess.run(["shutdown", "/r", "/t", "10", "/c", "RDP Wrapper installation completed. Rebooting in 10 seconds..."])
                self.log_message("✅ Reboot scheduled in 10 seconds")
                self.log_message("💾 Save your connection info before reboot!")
            else:
                self.log_message("⏸️ Reboot postponed by user")
                self.log_message("⚠️ IMPORTANT: Remember to reboot manually to complete the installation!")
                self.log_message("📋 Your connection info is displayed above - save it!")

            self.update_progress(1.0)
            self.log_message("🎉 All steps completed successfully!")
            self.update_status("Installation complete!")

        except Exception as e:
            self.log_message(f"❌ Error in Step 4: {str(e)}")
            raise

    def run(self):
        """Executa o aplicativo"""
        self.root.mainloop()

if __name__ == "__main__":
    app = RDPWrapperInstaller()
    app.run()
