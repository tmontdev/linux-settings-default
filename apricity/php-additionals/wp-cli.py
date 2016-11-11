import os

# Install wp-cli
os.system("curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar")

os.system("chmod +x wp-cli.phar")

os.system("sudo mv wp-cli.phar /usr/local/bin/wp")