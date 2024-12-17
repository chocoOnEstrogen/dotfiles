# Polybar Configuration

A sleek and functional Polybar setup featuring Catppuccin colors and comprehensive system monitoring.

![Theme Preview](/.github/resources/machines/linux/arch/polybar/polybar.png)

## 🎨 Features

### Visual Elements
- **Catppuccin Color Scheme**:
  - Background: `#FF1E1E2E`
  - Foreground: `#F4DBD6`
  - Primary: `#B5A8CC`
  - Secondary: `#6E6A8D`
  - Alert: `#F28FAD`
- **Modern Design**:
  - 24pt height
  - 6px radius corners
  - 2px borders
  - Clean separator style
  - Nerd Font icons

### Bar Modules
- **Left Side**:
  - Workspace indicators
  - Active window title
- **Right Side**:
  - Filesystem usage
  - PulseAudio volume
  - Memory usage
  - CPU status
  - Date/Time
  - System tray

### Optional Modules
- Network status
- Battery monitoring

## 📦 Installation

1. Copy configuration files:
```bash
cp -r polybar ~/.config/
```

2. Make launch script executable:
```bash
chmod +x ~/.config/polybar/launch.sh
```

3. Install dependencies:
```bash
# Arch Linux
pacman -S polybar ttf-jetbrains-mono-nerd ttf-font-awesome
```

## 🔧 Required Components

### Core
- Polybar
- i3wm (or compatible WM)

### Fonts
- JetBrainsMono Nerd Font
- Font Awesome 6
  - Free Solid
  - Brands Regular

### Additional Tools
- pavucontrol (volume control)
- gsimplecal (calendar)

## 🎯 Module Configuration

### Active Modules
- **Workspaces**:
  - Dynamic workspace switching
  - Active/inactive indicators
  - Urgent state support
- **Window Title**:
  - Truncates to 60 characters
- **Filesystem**:
  - Root partition monitoring
  - Space usage percentage
- **Volume**:
  - PulseAudio integration
  - Mute status
  - Click to launch pavucontrol
- **Memory**:
  - Usage percentage
  - Warning threshold at 90%
- **CPU**:
  - Usage percentage
  - Temperature monitoring
- **Date/Time**:
  - Toggleable format
  - Click to launch calendar

### Optional Modules
- **Network**:
  - WiFi signal strength
  - ESSID display
  - Connection status icons
- **Battery**:
  - Charging status
  - Percentage display
  - Time remaining

## 🔍 Troubleshooting

### Common Issues
1. **Missing Icons**: Ensure all required fonts are installed
2. **Module Errors**: Check module dependencies
3. **Tray Issues**: Verify tray position and scaling
4. **Multi-monitor**: Set `MONITOR` variable in launch script

## 🤝 Integration

Works seamlessly with:
- i3wm
- Rofi
- Dunst
- Other Catppuccin-themed applications

## 📝 Launch Script

The included `launch.sh`:
- Terminates existing instances
- Waits for clean shutdown
- Supports multi-monitor setups
- Provides debug logging

## 🎨 Customization

### Colors
Edit the color scheme in `config.ini`:
```ini
[colors]
background = #FF1E1E2E
background-alt = #FF5C4F6C
foreground = #F4DBD6
primary = #B5A8CC
secondary = #6E6A8D
alert = #F28FAD
```

### Bar Settings
Adjust appearance in `config.ini`:
```ini
[bar/main]
width = 100%
height = 24pt
radius = 6
border-size = 2
```

### Module Order
Modify module positioning:
```ini
modules-left = xworkspaces xwindow
modules-right = filesystem pulseaudio memory cpu date
```

## 📚 Resources

- [Polybar Wiki](https://github.com/polybar/polybar/wiki)
- [Nerd Fonts](https://www.nerdfonts.com/)
- [Font Awesome](https://fontawesome.com/)
- [Catppuccin](https://github.com/catppuccin/catppuccin) 