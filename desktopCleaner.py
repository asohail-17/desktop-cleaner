import os
import shutil

lis = []

sourcedir = r'C:\users\asoha\desktop\\'
destinationdir = r'C:\Users\asoha\cleanup'


if not os.path.exists(destinationdir): 
    os.makedirs(destinationdir)

lis = os.listdir(sourcedir)
for x in lis:
    print(sourcedir + x)
    if x == __file__:
        continue
    shutil.move((sourcedir + x),destinationdir)