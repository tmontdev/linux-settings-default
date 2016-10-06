import os

# Install Composer
os.system("curl -sS https://getcomposer.org/installer | php")

os.system("sudo mv composer.phar /usr/local/bin/composer")

# composr global require in terminal
home = input('Your username linux (example: omarkdev): ')

composer_path = '\nPATH=~/.config/composer/vendor/bin:$PATH'

with open("/home/"+home+"/.zshrc", "a") as myfile:
    myfile.write(composer_path)