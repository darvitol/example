f = open('hi.txt', 'wt')
f.write('new information')
f.close()

f = open('hi.txt', 'r')
print(f.read())
f.close()
