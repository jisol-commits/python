f=open("newfile.txt","x")
f.close()
import os
os.remove("newfile.txt")