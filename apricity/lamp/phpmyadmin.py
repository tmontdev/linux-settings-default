import os

# Install phpmyadmin
os.system("sudo pacman -Syu phpmyadmin")

phpmyadminconf = "/etc/httpd/conf/extra/phpmyadmin.conf"

# Copy default phpmyadmin conf
os.system("sudo cp php/default-phpmyadmin.txt "+phpmyadminconf)

#Change php.ini
httpdconf = '/etc/httpd/conf/httpd.conf'
httpdfile = None

with open(httpdconf, 'r') as file :
    httpdfile = file.read()

httpdfile += "\n\n # phpMyAdmin configuration"
httpdfile += "\nInclude conf/extra/phpmyadmin.conf"

with open(httpdconf, 'w') as file:
    file.write(httpdfile)

os.system("sudo systemctl restart httpd.service")