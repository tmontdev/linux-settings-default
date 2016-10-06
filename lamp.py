import os
# Script to install LAMP

# Install Apache
os.system("sudo python lamp/apache.py")

# Install MySQL
os.system("sudo python lamp/mysql.py")

# Install PHP
os.system("sudo python lamp/php.py")