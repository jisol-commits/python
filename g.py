x=open("file.txt","rt")
print(x.readline())
x.readline()
print(x.readline())
x.close()


f=open("wr.txt","wt")
f.write("this is write")