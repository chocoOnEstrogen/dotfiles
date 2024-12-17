# i3 Window Manager Configuration

A modern and functional i3wm setup with a focus on aesthetics and usability, featuring Catppuccin colors and seamless integration with other tools.

![Theme Preview](/.github/resources/machines/linux/arch/i3/i3.png)

## 🎨 Features

### Visual Elements
- **Custom Color Scheme**: Catppuccin-based colors
  - Focused: `#6E6A8D`
  - Inactive: `#5C4F6C`
  - Unfocused: `#1E1E2E`
  - Urgent: `#F28FAD`
- **Modern Appearance**:
  - 2px borders
  - Inner gaps: 8px
  - Outer gaps: 4px
  - Top gap: 24px for Polybar
  - Centered window titles

### Key Bindings
- **Core Functions**:
  - `Mod + Return`: Launch terminal (kitty)
  - `Mod + d`: Application launcher (rofi)
  - `Mod + Shift + q` or `Mod + q`: Close window
  
- **Quick Launch**:
  - `Mod + t`: File manager (thunar)
  - `Mod + b`: Web browser (brave)

- **Window Management**:
  - `Mod + h/v`: Horizontal/vertical splits
  - `Mod + s/w/e`: Stack/tabbed/toggle split layouts
  - `Mod + f`: Fullscreen toggle
  - Vim-style movement keys (`h,j,k,l`)

### System Integration
- **Media Controls**:
  - Volume control
  - Brightness adjustment
  - Media playback controls
- **Status Bar**: i3status with:
  - Memory usage
  - Disk space
  - Volume level
  - Date/time

## 📦 Installation

1. Copy the configuration files:
```bash
cp -r i3 ~/.config/
cp -r i3status ~/.config/
```

2. Install dependencies:
```bash
# Arch Linux
pacman -S i3-wm i3status polybar rofi picom dunst nitrogen flameshot
```

## 🔧 Required Components

### Core
- i3-wm
- i3status
- polybar
- rofi

### Additional Tools
- picom (compositing)
- dunst (notifications)
- nitrogen (wallpaper)
- flameshot (screenshots)
- polkit-gnome (authentication)
- kitty (terminal)
- thunar (file manager)
- brave (web browser)

## 🎯 Optional Enhancements

### Recommended Fonts
- JetBrains Nerd Font
- Font Awesome 6

### Additional Software
- brightnessctl
- playerctl
- pactl (PulseAudio)

## 🔍 Troubleshooting

### Common Issues
1. **Missing Gaps**: Ensure i3-gaps is installed
2. **No Transparency**: Check picom configuration
3. **Status Bar Issues**: Verify i3status configuration

### Status Bar Modules
The i3status configuration includes:
- Memory usage
- Disk space
- Volume level
- Date/time

Optional modules (commented out):
- CPU usage
- CPU temperature
- Network status
- Battery status

## 🤝 Integration

This configuration works seamlessly with:
- Polybar
- Rofi
- Picom
- Dunst
- Other Catppuccin-themed applications

## 📝 Notes

- Uses Windows key as Mod key
- Smart gaps enabled
- Workspace switching: Mod + 1-0
- Window movement: Mod + Shift + 1-0
- Resize mode: Mod + r

## 🎨 Customization

### Colors
Edit the color scheme in the i3 config:
```conf
client.focused          #6E6A8D #6E6A8D #F4DBD6 #6E6A8D #6E6A8D
client.focused_inactive #5C4F6C #5C4F6C #F4DBD6 #5C4F6C #5C4F6C
client.unfocused       #1E1E2E #1E1E2E #B5A8CC #1E1E2E #1E1E2E
client.urgent          #F28FAD #F28FAD #F4DBD6 #F28FAD #F28FAD
```

### Gaps
Adjust gaps in the i3 config:
```conf
gaps inner 8
gaps outer 4
gaps top 24
``` 