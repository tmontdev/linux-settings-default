import os

# to cd in home folder
home = input('Your username linux (example: omarkdev): ')

# email to second key
email = input('Your email for second key: ')

# go to home and generate new key
os.system('cd /home/'+home+'/.ssh/ ; ssh-keygen -t rsa -f id_rsa_second -C "'+email+'"')

# copy config default to config ssh
os.system('cp second-key/config.txt /home/'+home+'/.ssh/config')