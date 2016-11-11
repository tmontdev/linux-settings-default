import os

os.system("sudo dnf install -y php php-mysql mysql mysql-server zsh nodejs phpmyadmin vim composer")

os.system("sudo systemctl start mariadb")

os.system("sudo mysql_secure_installation")

os.system("curl -L git.io/sublimetext | sh")

os.system("curl -L http://install.ohmyz.sh | sh")

os.system("chsh -s /bin/zsh")

os.system("sudo wget -O /usr/local/bin/gogh http://git.io/vGz67 && sudo chmod +x /usr/local/bin/gogh")

os.system("sudo wget -O /usr/local/bin/gogh https://git.io/vKOB6 && sudo chmod +x /usr/local/bin/gogh")