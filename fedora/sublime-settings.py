import os
import urllib

repository = "https://raw.githubusercontent.com/omarkdev/sublime-settings/master/"
path = "~/.config/sublime-text-3/Packages/User/"

def curl(file):
	quoteFile = urllib.quote(file)
	curlCommand = "curl %s%s > %s'%s'" % (repository,quoteFile,path,file)

	os.system(curlCommand)

def packageControl():
	file = "Package Control.sublime-settings"
	
	return curl(file)

def settingsSublime():
	file = "Preferences.sublime-settings"

	curl(file)

	os.system("curl -LOk https://github.com/mrmartineau/SetiUI-Icons-Sublime/archive/master.zip ; unzip master.zip")

	movePath = "%sMaterial-Theme-Darker/" % (path)

	os.system("mv SetiUI-Icons-Sublime-master/ "+ movePath)
	os.system("rm master.zip")

def menu():
	print """If you already have the 
sublime and the package 
controll installed, 
select an option below:

Option 1: Install sublime dependencies
Option 2: Dependencies already installed, configure sublime"""

	optionMenu = input('Your option: ')
	if(optionMenu not in [1, 2]):
		print("\nYour options is not valid \n")

		return menu()

	if(optionMenu == 1):
		return packageControl()

	return settingsSublime()

menu()