def write_File_Xml():
    with open("Monitor_Night_Sleep.xml", "r") as f:
        lines = f.readlines()
        lines = str(lines)
        g = open('Monitor_Night_Sleep.xml' , 'w')
        for index in range(len(lines)):
            if index <= 0 and index <= 49:
                g.write('<?xml version="1.0" encoding="ISO-8859-1"?><pnml> \n')
            elif lines[index] == '>' and index > 50 and lines[index + 1] == '<':
                g.write('> \n')
            elif lines[index] == '>' and index > 50 and lines[index + 1] != '<':
                g.write('>')
            elif index > 50 and lines[index] != '\'' and lines[index] != ']':
                g.write(lines[index]) 
            else:
                g.write('')           
        g.close()