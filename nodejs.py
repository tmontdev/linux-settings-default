import os

# Install NodeJS and dependencies
os.system("sudo pacman -S nodejs npm")

# Install npm libraries global
os.system("sudo npm install -g pug stylus gulp")