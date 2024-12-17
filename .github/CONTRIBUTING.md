# Contributing Guidelines

Thank you for considering contributing to our dotfiles repository! Whether you're fixing a bug, improving existing configurations, or adding new features, your contributions are welcome.

## 🚀 Quick Start

1. Fork the repository
2. Clone your fork:
```bash
git clone https://github.com/your-username/dotfiles.git
cd dotfiles
```

3. Create a new branch:
```bash
git checkout -b feature/your-feature-name
```

## 📝 Guidelines

### Commit Messages

Follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
type(scope): description

[optional body]
[optional footer]
```

Types:
- `feat`: New feature or enhancement
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style/formatting changes
- `refactor`: Code refactoring
- `test`: Adding/modifying tests
- `chore`: Maintenance tasks

Examples:
```
feat(i3): add new workspace keybindings
fix(polybar): correct network module display
docs(neovim): update configuration instructions
```

### Directory Structure

- Keep configurations organized by component
- Use clear, descriptive file names
- Include README files for complex configurations
- Document dependencies and requirements

### Code Style

- Use consistent indentation (2 spaces for YAML, 4 for Python)
- Add comments for complex configurations
- Keep lines under 80 characters when possible
- Use descriptive variable names

### Testing

Before submitting:
1. Test configurations on a clean system
2. Verify all components work together
3. Check for conflicts with existing configurations
4. Ensure installation scripts work properly

## 📋 Pull Request Process

1. Update documentation if needed
2. Test your changes thoroughly
3. Update the README if required
4. Create a Pull Request with:
   - Clear description of changes
   - Screenshots (if visual changes)
   - Reference to related issues

## 🐛 Reporting Issues

When reporting issues, include:
- Your system information
- Steps to reproduce
- Expected vs actual behavior
- Relevant logs or error messages
- Screenshots if applicable

## 💡 Feature Requests

For feature requests:
- Describe the feature in detail
- Explain why it would be useful
- Provide examples if possible
- Consider implementation details

## ❓ Questions

If you have questions:
1. Check existing documentation
2. Search closed issues
3. Open a new issue with the "question" label

## 📜 License

By contributing, you agree that your contributions will be licensed under the same license as the original project.

Thank you for contributing! 🎉
