f = open("output.txt", 'w')
for i in range(104):
    num = "0"
    if i < 9:
        num = num + str(i+1)
    else:
        num = str(i+1)
    if i % 4 == 0:
        f.write("<tr>\n")
    f.write("<td> <a href=\"../images/magazine/" + num + ".jpg\" rel=\"lightbox-cat\"><img src=\"../images/magazine/" + num + ".jpg\" width=\"207\" height=\"293\" /></a></td>\n")
    if i % 4 == 3:
        f.write("</tr>\n")

f.close()
