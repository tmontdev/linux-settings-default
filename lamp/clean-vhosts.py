#Clean vhosts
def cleanVHosts(filename):
    file_open = None
    with open(filename, 'r') as file :
        file_open = file.read()

    text = file_open.split('\n')
    clean_lines = []

    for line in text:
        if line == "":
            continue
        
        firstLetter = line[0]

        if firstLetter == "#":
            continue
        
        file_open = file_open.replace(line, '')

    with open(filename, 'w') as file:
        file.write(file_open)

    clean_lines = []
    with open(filename, "r") as file:
        lines = file.readlines()
        clean_lines = [l.strip() for l in lines if l.strip()]

    with open(filename, "w") as file:
        file.writelines('\n'.join(clean_lines))