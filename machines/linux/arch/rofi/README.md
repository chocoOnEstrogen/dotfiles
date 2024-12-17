# Catppuccin Rofi Theme

A sleek and modern Rofi theme based on the Catppuccin color palette, designed for minimalism and functionality.

![Theme Preview](/.github/resources/machines/linux/arch/rofi/rofi.png) <!-- You might want to add a screenshot -->

## 🎨 Features

- **Clean Design**: Minimalist interface with carefully chosen padding and margins
- **Two-Column Layout**: Efficient space usage with 2-column application listing
- **Custom Colors**: Based on the Catppuccin palette with:
  - Primary accent: `#B5A8CC`
  - Background: `#1E1E2E`
  - Foreground: `#F4DBD6`
  - Borders: `#6E6A8D`
- **Modern Elements**:
  - Rounded corners (3-6px radius)
  - Subtle borders
  - Icon support
  - Smooth hover effects

## 📦 Installation

1. Copy `catppuccin.rasi` to your Rofi config directory:

```bash
cp catppuccin.rasi ~/.config/rofi/
```

2. Copy `config.rasi` to your Rofi config directory:

```bash
cp config.rasi ~/.config/rofi/
```


## 🔧 Configuration

### Window Properties
- Width: 600px
- Height: 360px
- Border: 3px solid

### Layout
- 5 lines of items
- 2 columns
- Icon size: 25px
- Custom padding and margins for optimal spacing

### Customization
To modify colors, edit the following variables at the top of the file:

```css
{
    bg-col: #1E1E2E; /* Background color */
    bg-col-light: #5C4F6C; /* Light background variant */
    border-col: #6E6A8D; /* Border color */
    selected-col: #B5A8CC; /* Selection highlight */
    primary: #B5A8CC; /* Primary accent color */
    fg-col: #F4DBD6; /* Main text color */
    fg-col2: #F4DBD6; /* Secondary text color */
    grey: #6E6A8D; /* Inactive elements */
}
```

## 🤝 Integration

This theme works best with:
- i3wm
- Polybar
- Picom
- Other Catppuccin-themed applications

## 📝 Notes

- Requires a Nerd Font for icons
- Designed for 1080p+ displays
- Supports both light and dark window managers
- Includes mode switcher styling

## 🎯 Dependencies

- Rofi version 1.7.0+
- A compatible Nerd Font
- Icon theme (recommended: Papirus)

## 🔍 Troubleshooting

If icons aren't displaying:
1. Verify your icon theme is properly installed
2. Ensure Rofi is configured to show icons
3. Check that your Rofi configuration includes: