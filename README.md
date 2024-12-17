# Dotfiles

My personal dotfiles and system configurations, organized by machine and operating system.

## Structure

```plaintext
dotfiles/
├── machines/
│   ├── linux/
│       └── arch/          # Arch Linux configurations
├── docs/                  # Documentation
├── .github/              # GitHub specific files
└── README.md
```

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/chocoOnEstrogen/dotfiles.git
cd dotfiles
```

2. Navigate to your system's configuration:
```bash
cd machines/linux/arch  # For Arch Linux
```

3. Run the installation script:
```bash
python3 install.py
```

## Available Configurations

### Linux
- **[Arch Linux](machines/linux/arch/README.md)**: Complete desktop environment with i3wm


## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/YourFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'feat: add new feature'`)
5. Push to the branch (`git push origin feature/YourFeature`)
6. Create a Pull Request

## License

This project is licensed under the CC0 1.0 License - see the [LICENSE](LICENSE) file for details.



