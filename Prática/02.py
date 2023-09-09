# I/O Operations

f = open("text.txt", "w")
f.write("criando um arquivo txt")
f.close()

f = open("text.txt", "r")
print(f.read(7))
print(f.read())
f.close()