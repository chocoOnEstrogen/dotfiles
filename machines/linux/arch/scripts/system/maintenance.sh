#!/bin/bash
# System maintenance and cleanup script

echo "🧹 Starting system maintenance..."

# Update pacman mirrors
echo "📡 Updating mirror list..."
sudo reflector --latest 20 --protocol https --sort rate --save /etc/pacman.d/mirrorlist

# System updates
echo "📦 Updating system packages..."
sudo pacman -Syu

# Clean package cache
echo "🗑️ Cleaning package cache..."
sudo paccache -r

# Remove orphaned packages
echo "🧹 Removing orphaned packages..."
sudo pacman -Rns $(pacman -Qtdq) 2>/dev/null || echo "No orphaned packages found"

# Clean journal logs
echo "📝 Cleaning old journal logs..."
sudo journalctl --vacuum-time=7d

echo "✨ Maintenance complete!" 