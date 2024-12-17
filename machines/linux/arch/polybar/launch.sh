#!/bin/bash

# Terminate already running bar instances
killall -q polybar

# Wait until the processes have been shut down
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

# Launch Polybar with debug output
MONITOR=$(polybar -m|tail -1|sed -e 's/:.*$//g') polybar main -l trace 2>&1 | tee -a /tmp/polybar.log & disown

echo "Polybar launched..."
