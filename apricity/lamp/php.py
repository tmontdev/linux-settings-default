import os

#Install PHP and PHP Apache
os.system("sudo pacman -Syu php php-apache php-mcrypt")

#Change php.ini
phpini = '/etc/php/php.ini'
phpfile = None

with open(phpini, 'r') as file :
    phpfile = file.read()

#Enable extensions necessary
extensions = ['pdo_mysql.so', 'mcrypt.so', 'mysqli.so']

for extension in extensions:
    rep_extension = "extension="+extension
    find_extension = ";"+rep_extension

    phpfile = phpfile.replace(find_extension, rep_extension)

#Add error_log
phpfile += "\nerror_log = /var/log/php/error.log"
phpfile = phpfile.replace("display_errors = Off", "display_errors = On")

with open(phpini, 'w') as file:
    file.write(phpfile)

#Create folders for log's
os.system("sudo mkdir /var/log/php; sudo chown http /var/log/php")

#Change httpd.conf
httpdconf = '/etc/httpd/conf/httpd.conf'
httpdfile = None

with open(httpdconf, 'r') as file :
    httpdfile = file.read()

# include php7 module
httpdfile += "\nLoadModule php7_module modules/libphp7.so"
httpdfile += "\nInclude conf/extra/php7_module.conf"
httpdfile += "\n\n"
httpdfile += "\nAddType application/x-httpd-php .php"
httpdfile += "\nAddType application/x-httpd-php-source .phps"

with open(httpdconf, 'w') as file:
    file.write(httpdfile)

# Disable mpm_event_module and enable mpm_prefork_module
os.system("sudo sed -i -e 's/LoadModule mpm_event_module/#LoadModule mpm_event_module/g' "+httpdconf)
os.system("sudo sed -i -e 's/#LoadModule mpm_prefork_module/LoadModule mpm_prefork_module/g' "+httpdconf)

# Restart apache
os.system("sudo systemctl restart httpd.service")