import os

# Install MySQL
os.system("sudo pacman -Syu mariadb mariadb-clients libmariadbclient")

# Install MariaDB data directory
os.system("sudo mysql_install_db --user=mysql --basedir=/usr --datadir=/var/lib/mysql")

# Start MySQL and set it to run at boot
os.system("sudo systemctl start mysqld.service; sudo systemctl enable mysqld.service")

# Configure mysql
os.system("mysql_secure_installation")