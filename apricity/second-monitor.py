import os

home = input('Your username linux (example: omarkdev): ')

# second_monitor command
aliasxrandr = "xrandr --newmode '1440x900_59.90'  106.29  1440 1520 1672 1904  900 901 904 932  -HSync +Vsync;"
aliasxrandr += 'xrandr --addmode DVI-I-1 1440x900_59.90;'
aliasxrandr += 'xrandr --output DVI-I-1 --mode 1440x900_59.90;'

aliasxrandr = 'alias second_monitor="'+aliasxrandr+'"'

# second_monitor_rotate command
aliasrotate = '\nalias second_monitor_rotate="xrandr --output DVI-I-1 --rotate left"'

# second_monitor_rotate_normal command
aliasrotatenormal = '\nalias second_monitor_rotate_normal="xrandr --output DVI-I-1 --rotate normal"'

# Write this commands in .zshrc and .bashrc
with open("/home/"+home+"/.zshrc", "a") as myfile:
    myfile.write(aliasxrandr)
    myfile.write(aliasrotate)
    myfile.write(aliasrotatenormal)

with open("/home/"+home+"/.bashrc", "a") as myfile:
    myfile.write(aliasxrandr)
    myfile.write(aliasrotate)
    myfile.write(aliasrotatenormal)