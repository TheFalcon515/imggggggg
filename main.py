import os
import sys

# create a folder variable that is set to the current working directory
folder = os.getcwd()

for filename in os.listdir(folder):
    infilename = os.path.join(folder, filename)
    if not os.path.isfile(infilename): continue
    oldbase = os.path.splitext(filename)
    newname = infilename+".jpg"
    output = os.rename(infilename, newname)
