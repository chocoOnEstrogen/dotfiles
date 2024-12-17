#!/bin/bash
# Display system information

echo "💻 System Information"
echo "-------------------"

# OS Info
echo "🐧 OS: $(cat /etc/os-release | grep PRETTY_NAME | cut -d'"' -f2)"

# Hardware Info
echo "🔧 CPU: $(grep "model name" /proc/cpuinfo | head -n1 | cut -d':' -f2)"
echo "🧮 RAM: $(free -h | awk '/^Mem:/ {print $3 "/" $2}')"
echo "💽 Disk: $(df -h / | awk 'NR==2 {print $3 "/" $2}')"

# Network Info
echo "🌐 IP: $(ip route get 1 | awk '{print $7;exit}')"

# Package Info
echo "📦 Packages: $(pacman -Q | wc -l)"

# System Uptime
echo "⏰ Uptime: $(uptime -p)" 