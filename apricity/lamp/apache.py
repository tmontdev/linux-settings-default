import os

# Install Apache
os.system("sudo pacman -S apache")

# Remove KeepAlive from httpd-default.conf
os.system("sudo sed -i -e 's/KeepAlive On/KeepAlive Off/g' /etc/httpd/conf/extra/httpd-default.conf")

# Set Apache to start at boot
os.system("sudo systemctl enable httpd.service")

# Change DocumentRoot to localhost
httpdconf = '/etc/httpd/conf/httpd.conf'
httpdfile = None

with open(httpdconf, 'r') as file :
    httpdfile = file.read()

httpdfile = httpdfile.replace('DocumentRoot "/srv/http"', 'DocumentRoot "/srv/http/localhost"')
httpdfile = httpdfile.replace('#Include conf/extra/httpd-vhosts.conf', 'Include conf/extra/httpd-vhosts.conf')

with open(httpdconf, 'w') as file:
    file.write(httpdfile)

#Copy default vhosts
os.system('sudo cp apache/vhost-default.txt /etc/httpd/conf/extra/httpd-vhosts.conf')

#Create folders and add -R 777 permission
os.system('sudo mkdir -p /srv/http/localhost; sudo mkdir -p /srv/http/localhost/logs')

os.system('sudo chmod -R 777 /srv/http/localhost')

#Start apache
os.system('sudo systemctl start httpd.service')

print("Apache installed")

