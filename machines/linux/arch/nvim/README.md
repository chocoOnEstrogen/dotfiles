# NvChad Configuration

A customized NvChad setup with Catppuccin theme, GitHub Copilot integration, and enhanced LSP support.

![Theme Preview](/.github/resources/machines/linux/arch/neovim/nvim.png)
![Theme Preview](/.github/resources/machines/linux/arch/neovim/nvim2.png)

## 🎨 Features

### Visual Elements
- **Theme**: Catppuccin with transparency
- **UI Components**:
  - Borderless Telescope
  - VSCode-colored statusline
  - Custom NEOVIM dashboard
  - Smart tab line

### Plugin Integration
- **Core Plugins**:
  - Conform.nvim (formatting)
  - LSP Configuration
  - Treesitter
  - Telescope
  - nvim-tree
  - gitsigns

### Key Mappings
- **Custom Shortcuts**:
  - `;` remapped to `:`
  - `jk` for ESC in insert mode
  - `<S-Tab>` for Copilot completion

### LSP Support
- Built-in language server configuration
- Signature help enabled
- Format on save capability (commented by default)

## 📦 Installation

1. Backup existing Neovim configuration:
```bash
mv ~/.config/nvim ~/.config/nvim.backup
```

2. Clone NvChad:
```bash
git clone https://github.com/NvChad/NvChad ~/.config/nvim --depth 1
```

3. Copy custom configuration:
```bash
cp -r neovim/* ~/.config/nvim/
```

## 🔧 Required Components

### Core
- Neovim (>= 0.9.0)
- Git
- A Nerd Font
- ripgrep (for Telescope)

### Language Servers
- lua-language-server
- Additional LSPs as needed

### Formatters
- stylua (for Lua)
- Additional formatters as needed

## 🎯 Configuration Structure

```
nvim/
├── init.lua              # Entry point
├── lua/
│   ├── chadrc.lua       # NvChad configuration
│   ├── mappings.lua     # Custom keymaps
│   ├── options.lua      # Neovim options
│   ├── configs/         # Plugin configs
│   │   ├── lazy.lua     # Package manager
│   │   ├── lspconfig.lua# LSP settings
│   │   └── conform.lua  # Formatter settings
│   └── plugins/         # Plugin specifications
│       └── init.lua     # Core plugins
```

## 🔍 Plugin Configuration

### Formatting
```lua
{
    "stevearc/conform.nvim",
    opts = {
        formatters_by_ft = {
            lua = { "stylua" },
            -- Add more formatters here
        },
    },
}
```

## 🤝 Integration

Works seamlessly with:
- Git
- LSP servers
- GitHub Copilot
- Terminal tools

## 📝 Customization

### Adding New Plugins
Add to `plugins/init.lua`:
```lua
return {
    {
        "plugin-author/plugin-name",
        config = function()
            -- Configuration here
        end
    },
}
```

### Modifying Theme
Edit in `chadrc.lua`:
```lua
M.base46 = {
    theme = "catppuccin",
    transparency = true,
}
```

## 📚 Resources

- [NvChad Documentation](https://nvchad.com/)
- [Neovim Documentation](https://neovim.io/doc/)
- [Catppuccin Theme](https://github.com/catppuccin/nvim)