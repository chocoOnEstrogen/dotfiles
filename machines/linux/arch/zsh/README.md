# Zsh Configuration

A feature-rich Zsh setup with Oh My Zsh, custom plugins, enhanced history management, and useful aliases.

![Theme Preview](/.github/resources/machines/linux/arch/zsh/zsh.png)

## 🎨 Features

### Oh My Zsh Integration
- **Theme**: robbyrussell
- **Plugins**:
  - git (version control)
  - zsh-autosuggestions (command suggestions)
  - zsh-syntax-highlighting (syntax coloring)
  - docker (container management)
  - history-substring-search (better history search)

### Enhanced History
- Large history size (1,000,000 entries)
- Duplicate removal
- Blank line reduction
- Improved search functionality

### Completion System
- Case-insensitive completion
- Menu-driven selection
- Smart matching

### Custom Functions
- **mkcd**: Create and enter directory
- **extract**: Universal archive extractor
  - Supports: tar.bz2, tar.gz, bz2, rar, gz, tar, tbz2, tgz, zip, Z, 7z

### Comprehensive Aliases
- **Navigation**:
  - `..`: Go up one directory
  - `...`: Go up two directories
  - `....`: Go up three directories
  - `.....`: Go up four directories

- **File Operations**:
  - `ll`: Detailed list
  - `la`: Show all files
  - `l`: Simplified list
  - `ls`: Colorized output

- **System Tools**:
  - `cls`: Clear screen
  - `df`: Human-readable disk usage
  - `du`: Human-readable file sizes
  - `free`: Human-readable memory info
  - `top`: Replaced with htop

- **Development**:
  - `vim`: Redirects to neovim
  - `zshrc`: Edit zsh config
  - `reload`: Reload zsh config

- **Git Shortcuts**:
  - `gs`: git status
  - `ga`: git add
  - `gc`: git commit
  - `gp`: git push
  - `gl`: git pull
  - `gd`: git diff

## 📦 Installation

1. Install Oh My Zsh:
```bash
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

2. Install required plugins:
```bash
# zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

# zsh-syntax-highlighting
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```

3. Copy configuration:
```bash
cp .zshrc ~/.zshrc
```

## 🔧 Required Components

### Core
- Zsh
- Oh My Zsh
- Node Version Manager (nvm)

### Additional Tools
- neovim (text editor)
- htop (system monitor)
- docker (containerization)

## 🎯 Configuration Sections

### Oh My Zsh Setup
```bash
export ZSH="$HOME/.oh-my-zsh"
ZSH_THEME="robbyrussell"
plugins=(
    git
    zsh-autosuggestions
    zsh-syntax-highlighting
    docker
    history-substring-search
)
```

### History Configuration
```bash
HISTSIZE=1000000
SAVEHIST=1000000
setopt HIST_IGNORE_ALL_DUPS
setopt HIST_FIND_NO_DUPS
setopt HIST_REDUCE_BLANKS
```

### Completion System
```bash
autoload -Uz compinit
compinit
zstyle ':completion:*' menu select
zstyle ':completion:*' matcher-list 'm:{a-zA-Z}={A-Za-z}'
```

## 🔍 Troubleshooting

### Common Issues
1. **Plugin Not Loading**: Verify plugin installation
2. **History Issues**: Check permissions on history file
3. **Completion Problems**: Run `compinit`
4. **NVM Issues**: Verify installation path

## 🤝 Integration

Works seamlessly with:
- Git
- Docker
- NVM
- Neovim

## 📝 Notes

- Uses Neovim as default editor
- Includes NVM integration
- Custom PATH additions
- Smart archive extraction

## 🎨 Customization

### Adding New Aliases
Add to the aliases section:
```bash
alias new-command='your-command'
```

### Adding Functions
Add to the functions section:
```bash
function new-function() {
    # Your function code
}
```

## 📚 Resources

- [Oh My Zsh](https://ohmyz.sh/)
- [Zsh Documentation](http://zsh.sourceforge.net/Doc/)
- [NVM Repository](https://github.com/nvm-sh/nvm) 