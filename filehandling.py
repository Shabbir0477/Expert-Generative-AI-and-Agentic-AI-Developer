#file=open("demo.txt",mode="r")
#c=file.readlines()[3]
#print(c)
#file.close()


"""
file=open("test.txt","w")

c=file.write("This is my world")

print(c)

file.close()"""

"""

with open("test.txt","w+") as fd:

    print(fd.tell())
    print(fd.write("Hello World"))
    print(fd.read())
    print(fd.tell())
"""
"""

file=open("test.txt","r+")
content=file.read()
v=str(content)
print(v)
f=v.split()
print(f)
f.insert(1,"chetan")
print(f)
print(file.tell())
file.close()
file=open("test.txt",mode="w")
print(f)
for i in f:
    file.writelines([i])
"""