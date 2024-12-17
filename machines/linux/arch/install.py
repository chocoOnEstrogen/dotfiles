#!/usr/bin/env python3

import os
import subprocess
import shutil
from pathlib import Path
import sys
from typing import Optional, Dict, List, Callable, Any
import re
from functools import wraps
import time
import threading

def loading_bar(message: str, color: str = "white"):
    """Decorator to show a loading animation while a function executes"""
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Animation characters for spinner
            chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
            stop_spinner = threading.Event()
            
            def show_spinner() -> None:
                while not stop_spinner.is_set():
                    for char in chars:
                        if stop_spinner.is_set():
                            break
                        sys.stdout.write(f'\r{color_codes[color]}{char} {message}{color_codes["reset"]}')
                        sys.stdout.flush()
                        time.sleep(0.1)
            
            spinner = threading.Thread(target=show_spinner)
            spinner.daemon = True
            spinner.start()
            
            try:
                result = func(*args, **kwargs)
                sys.stdout.write(f'\r{color_codes["green"]}✓ {message} Complete!{color_codes["reset"]}\n')
                return result
            except Exception as e:
                sys.stdout.write(f'\r{color_codes["red"]}✗ {message} Failed!{color_codes["reset"]}\n')
                raise e
            finally:
                stop_spinner.set()
                spinner.join()
                
        return wrapper
    return decorator

def ran_with_sudo() -> bool:
    """Check if script was run with sudo privileges"""
    return os.geteuid() == 0

# Required packages to install, organized by category
packages: List[str] = [
    # Window Manager and Core
    "i3-wm", "polybar", "rofi", "picom", "dunst", "nitrogen",
    
    # Terminal and Shell
    "kitty", "zsh",
    
    # Development and Utilities
    "neovim", "git", "base-devel", "curl", "wget",
    
    # File Management
    "thunar", "xdg-user-dirs",
    
    # System Tools
    "flameshot", "brightnessctl", "playerctl", "pavucontrol", "polkit-gnome",
    
    # Fonts and Themes
    "ttf-jetbrains-mono-nerd", "ttf-font-awesome", "papirus-icon-theme",
    
    # Additional Dependencies
    "python-pip", "python-wheel", "python-setuptools"
]

# ANSI color codes for terminal output
color_codes: Dict[str, str] = {
    "red": "\033[31m",     # Errors
    "green": "\033[32m",   # Success
    "yellow": "\033[33m",  # Warnings
    "blue": "\033[34m",    # Info
    "magenta": "\033[35m", # Debug
    "cyan": "\033[36m",    # Status
    "white": "\033[37m",   # Default
    "reset": "\033[0m"     # Reset color
}

def log(type: Optional[str], message: str, color: str = "white") -> None:
    """Print a formatted log message with color and type indicator."""
    if color not in color_codes:
        color = "white"
    
    type_str = type if type else "*"
    type_indicator = f"[{type_str:^7}]"
    timestamp = time.strftime("%H:%M:%S")
    
    print(f"{color_codes[color]}[{timestamp}] {type_indicator}{color_codes['reset']} {message}")

def ask_user(message: str, default: bool = True) -> bool:
    """Prompt user for yes/no response with default option"""
    prompt = " [Y/n]: " if default else " [y/N]: "
    response = input(f"{message}{prompt}").lower().strip()
    if not response:
        return default
    return response.startswith('y')

def menu(message: str, options: List[str], default: int = 1) -> Optional[str]:
    """Display a menu and return selected option with default choice"""
    print(f"\n{message}")
    for i, option in enumerate(options, 1):
        print(f"({i}) {option}{' (default)' if i == default else ''}")
    
    while True:
        data = input("> ").strip()
        if not data and default:
            return options[default - 1]
        
        try:
            index = int(data) - 1
            if 0 <= index < len(options):
                return options[index]
            log("ERROR", "Invalid option selected", "red")
        except ValueError:
            log("ERROR", "Please enter a number", "red")

@loading_bar("Installing system packages", "blue")
def install_packages() -> bool:
    """Install required system packages using pacman"""
    try:
        # Update package database
        subprocess.run(["sudo", "pacman", "-Sy", "--noconfirm"], check=True, capture_output=True)
        
        # Install packages in smaller batches to avoid potential issues
        batch_size = 10
        for i in range(0, len(packages), batch_size):
            batch = packages[i:i + batch_size]
            subprocess.run(["sudo", "pacman", "-S", "--needed", "--noconfirm"] + batch, 
                         check=True, capture_output=True)
            
        return True
    except subprocess.CalledProcessError as e:
        log("ERROR", f"Package installation failed: {e.stderr.decode()}", "red")
        return False

@loading_bar("Installing AUR helper", "blue")
def install_aur_helper(helper: str) -> bool:
    """Install selected AUR helper"""
    try:
        temp_dir = Path("/tmp/aur_helper")
        temp_dir.mkdir(parents=True, exist_ok=True)
        os.chdir(temp_dir)
        
        subprocess.run(["git", "clone", f"https://aur.archlinux.org/{helper}.git"], 
                     check=True, capture_output=True)
        os.chdir(helper)
        subprocess.run(["makepkg", "-si", "--noconfirm"], check=True, capture_output=True)
        
        return True
    except subprocess.CalledProcessError as e:
        log("ERROR", f"AUR helper installation failed: {e.stderr.decode()}", "red")
        return False
    finally:
        os.chdir(Path.home())

@loading_bar("Installing Oh My Zsh", "blue")
def install_oh_my_zsh() -> bool:
    """Install Oh My Zsh and plugins"""
    try:
        # Install Oh My Zsh
        install_cmd = 'sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended'
        subprocess.run(install_cmd, shell=True, check=True)
        
        # Install plugins
        plugins_dir = Path.home() / ".oh-my-zsh/custom/plugins"
        plugins_dir.mkdir(parents=True, exist_ok=True)
        
        # Define plugins to install
        plugins = {
            "zsh-autosuggestions": "https://github.com/zsh-users/zsh-autosuggestions",
            "zsh-syntax-highlighting": "https://github.com/zsh-users/zsh-syntax-highlighting",
            "zsh-completions": "https://github.com/zsh-users/zsh-completions"
        }
        
        # Install each plugin
        for plugin_name, repo_url in plugins.items():
            plugin_path = plugins_dir / plugin_name
            if not plugin_path.exists():
                subprocess.run(["git", "clone", repo_url, str(plugin_path)], check=True)
        
        return True
    except subprocess.CalledProcessError as e:
        log("ERROR", f"Oh My Zsh installation failed: {e}", "red")
        return False

@loading_bar("Installing NvChad", "blue")
def install_nvchad() -> bool:
    """Install NvChad"""
    try:
        nvim_config = Path.home() / ".config/nvim"
        
        # Backup existing config if it exists
        if nvim_config.exists():
            backup_path = Path(f"{nvim_config}.backup")
            shutil.move(str(nvim_config), str(backup_path))
            log("INFO", f"Backed up existing Neovim config to {backup_path}", "yellow")
        
        # Clone NvChad
        subprocess.run([
            "git", "clone",
            "https://github.com/NvChad/NvChad",
            str(nvim_config),
            "--depth", "1"
        ], check=True)
        
        return True
    except subprocess.CalledProcessError as e:
        log("ERROR", f"NvChad installation failed: {e}", "red")
        return False

@loading_bar("Copying configuration files", "blue")
def copy_dotfiles() -> bool:
    """Copy configuration files to appropriate locations"""
    try:
        config_dir = Path.home() / ".config"
        current_dir = Path(__file__).parent
        
        # Create .config directory if it doesn't exist
        config_dir.mkdir(parents=True, exist_ok=True)
        
        # Directories to copy
        dirs = ["i3", "polybar", "rofi", "picom", "nvim"]
        
        for dir_name in dirs:
            src = current_dir / dir_name
            dst = config_dir / dir_name
            
            if src.exists():
                # Backup existing config if it exists
                if dst.exists():
                    backup_path = Path(f"{dst}.backup")
                    shutil.move(str(dst), str(backup_path))
                    log("INFO", f"Backed up existing {dir_name} config to {backup_path}", "yellow")
                
                # Copy new config
                shutil.copytree(src, dst, dirs_exist_ok=True)
        
        # Copy .zshrc
        zshrc_src = current_dir / "zsh/.zshrc"
        zshrc_dst = Path.home() / ".zshrc"
        if zshrc_src.exists():
            if zshrc_dst.exists():
                shutil.move(str(zshrc_dst), f"{zshrc_dst}.backup")
            shutil.copy2(str(zshrc_src), str(zshrc_dst))
        
        return True
    except Exception as e:
        log("ERROR", f"Failed to copy configuration files: {e}", "red")
        return False

def main() -> None:
    """Main installation process"""
    if ran_with_sudo():
        log("ERROR", "Please do not run this script with sudo", "red")
        sys.exit(1)

    log("INFO", "Starting installation process...", "blue")
    
    # Install system packages
    if ask_user("Install required system packages?"):
        if not install_packages():
            if not ask_user("Package installation failed. Continue anyway?", default=False):
                sys.exit(1)
    
    # Install AUR helper
    if ask_user("Install an AUR helper?"):
        helper = menu("Select AUR helper:", ["yay", "paru"], default=1)
        if helper:
            install_aur_helper(helper)
    
    # Install Oh My Zsh
    if ask_user("Install Oh My Zsh?"):
        install_oh_my_zsh()
    
    # Install NvChad
    if ask_user("Install NvChad?"):
        install_nvchad()
    
    # Copy configuration files
    if ask_user("Copy configuration files?"):
        copy_dotfiles()
    
    # Set Zsh as default shell
    if ask_user("Set Zsh as default shell?"):
        try:
            subprocess.run(["chsh", "-s", "/bin/zsh"], check=True)
            log("SUCCESS", "Zsh set as default shell", "green")
        except subprocess.CalledProcessError as e:
            log("ERROR", f"Failed to set Zsh as default shell: {e}", "red")
    
    log("SUCCESS", "Installation completed! Please log out and back in for all changes to take effect.", "green")
    log("INFO", "You may want to run 'source ~/.zshrc' to load the new shell configuration.", "blue")

if __name__ == "__main__":
    main()
