# Picom Configuration

A minimal Picom compositor configuration focused on clean transparency and performance using the GLX backend.

## 🎨 Features

### Transparency Settings
- **Active Windows**: 98% opacity
- **Inactive Windows**: 90% opacity
- **Smart Opacity**: Respects application-specific settings

### Performance
- **GLX Backend**: Optimized for better performance
- **Smart Detection**:
  - Window manager hints
  - Rounded corners
  - Client opacity

### Window Handling
- Proper transparency detection
- Window manager hint support
- Override control for inactive opacity

## 📦 Installation

1. Copy configuration file:
```bash
cp picom.conf ~/.config/picom/
```

2. Install Picom:
```bash
# Arch Linux
pacman -S picom
```

## 🔧 Configuration

### Basic Settings
```conf
backend = "glx";    # GLX backend for better performance
```

### Opacity Rules
```conf
active-opacity = 0.98
inactive-opacity = 0.90
inactive-opacity-override = false
```

### Window Detection
```conf
mark-wmwin-focused = true
mark-ovredir-focused = true
detect-rounded-corners = true
detect-client-opacity = true
```

## 🎯 Integration

Works seamlessly with:
- i3wm
- Polybar
- Rofi
- Other window managers and applications

## 🔍 Troubleshooting

### Common Issues
1. **Screen Tearing**: Ensure GLX backend is enabled
2. **Performance Issues**: Check for conflicting compositors
3. **Transparency Problems**: Verify opacity rules
4. **Application Conflicts**: Check application-specific settings

## 📝 Notes

- Uses GLX backend for optimal performance
- Respects application-specific transparency settings
- Minimal configuration for better stability
- Easy to extend with additional features

## 🎨 Customization

### Opacity
Adjust window transparency in `picom.conf`:
```conf
active-opacity = 0.98          # More opaque
inactive-opacity = 0.90        # More transparent
```

### Application-Specific Rules
Add custom rules using:
```conf
opacity-rule = [
    "100:class_g = 'Application'",
    "90:class_g = 'Another'"
];
```

## 📚 Resources

- [Picom GitHub](https://github.com/yshui/picom)
- [Arch Wiki - Picom](https://wiki.archlinux.org/title/Picom)
- [GLX vs XRender](https://wiki.archlinux.org/title/Picom#GLX_vs_XRender) 