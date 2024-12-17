# Catppuccin Arch Linux Configuration

A comprehensive and aesthetically pleasing Arch Linux desktop environment configuration using i3wm, with a focus on the Catppuccin color scheme and modern functionality.

![Desktop Preview](/.github/resources/machines/linux/arch/preview.png)

## 🎨 Features

### Core Components
- **i3wm**: Tiling window manager with gaps and rounded corners
- **Polybar**: Customized status bar with system monitoring
- **Rofi**: Modern application launcher
- **Picom**: Compositor for transparency effects
- **Neovim**: Feature-rich text editor with NvChad
- **Zsh**: Enhanced shell with Oh My Zsh

### Theme
- **Color Scheme**: Catppuccin palette
- **Fonts**: JetBrains Nerd Font + Font Awesome
- **Icons**: Papirus icon theme

## 🚀 Quick Install

1. Clone the repository:
```bash
git clone https://github.com/chocoOnEstrogen/dotfiles.git
cd dotfiles/machines/linux/arch
```

2. Run the installation script:
```bash
python3 install.py
```

## 📦 Manual Installation

### 1. Install Required Packages
```bash
# Core packages
sudo pacman -S i3-wm polybar rofi picom neovim zsh

# Additional tools
sudo pacman -S kitty thunar nitrogen dunst flameshot

# Development tools
sudo pacman -S git base-devel
```

### 2. Install Configurations
```bash
# Create necessary directories
mkdir -p ~/.config/{i3,polybar,rofi,picom,nvim}

# Copy configurations
cp -r machines/linux/arch/i3/* ~/.config/i3/
cp -r machines/linux/arch/polybar/* ~/.config/polybar/
cp -r machines/linux/arch/rofi/* ~/.config/rofi/
cp -r machines/linux/arch/picom/* ~/.config/picom/
cp -r machines/linux/arch/nvim/* ~/.config/nvim/
cp machines/linux/arch/zsh/.zshrc ~/.zshrc
```

## 🔧 Components

| Component | Description | Config Location |
|-----------|-------------|-----------------|
| i3wm | Window Manager | `~/.config/i3/` |
| Polybar | Status Bar | `~/.config/polybar/` |
| Rofi | Application Launcher | `~/.config/rofi/` |
| Picom | Compositor | `~/.config/picom/` |
| Neovim | Text Editor | `~/.config/nvim/` |
| Zsh | Shell | `~/.zshrc` |

## 📝 Post-Installation

1. Set Zsh as default shell:
```bash
chsh -s $(which zsh)
```

2. Install Oh My Zsh:
```bash
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

3. Install NvChad:
```bash
git clone https://github.com/NvChad/NvChad ~/.config/nvim --depth 1
```

## 🎨 Customization

Each component can be customized by editing its respective configuration files. See individual README files in each component's directory for detailed customization options.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.

## 🙏 Acknowledgments

- [Catppuccin](https://github.com/catppuccin/catppuccin) for the color scheme
- [NvChad](https://github.com/NvChad/NvChad) for the Neovim configuration
- [Oh My Zsh](https://ohmyz.sh/) for the Zsh framework