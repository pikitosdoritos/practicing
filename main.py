i = 1

while i < 9:
    j = 1
    line = ''
    
    while j < 9:
        if j % 2 == 0:
            line += '   '
        else:
            line += '▮▮'

        j += 1
    
    if i % 2 == 0:
        line = line[2:]

    print(line)
    
    i += 1