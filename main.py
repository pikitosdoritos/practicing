# i = 1

# while i < 9:
#     j = 1
#     line = ''
    
#     while j < 9:
#         if j % 2 == 0:
#             line += '   '
#         else:
#             line += '▮▮'

#         j += 1
    
#     if i % 2 == 0:
#         line = line[2:]

#     print(line)
    
#     i += 1
    
y = 1

svaston = []

while y < 21:
    x = 1
    lines = ""
    while x < 21:
        if x == 10 and y == 10:
            lines += "▮▮"
        elif x == 10:
            lines += "▮▮"
        elif y == 10:
            lines += "▮▮"
        elif y == 1 and x >= 11:
            lines += "▮▮"
        elif y >= 10 and x == 20:
            lines += "▮▮"
        elif 1 <= y <= 10 and x == 1:
            lines += "▮▮"
        elif y == 20 and 0 < x < 11:
            lines += "▮▮"
        else:
            lines += "  "
        
        x += 1
    
    svaston.append(lines)   
    y += 1
    
    print(lines)

