
from shutil import make_archive

#with open('C:/Users/USER/Documents/GitHub/automation/file.txt') as f:
f = open("C:/Users/USER/Documents/GitHub/automation/file.txt", "r")
for lines in f.readlines():
    root, filedir = lines.rstrip('\n').split(',')
    make_archive(filedir, 'zip',root)
        
        
