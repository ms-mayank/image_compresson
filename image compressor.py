import os
import tinify
tinify.key="your_API KEY"
# To Changes the current working directory of this file to the "original" folder , used chdir 
os.chdir(os.getcwd()+'\\original')

# getcwd - get current working directory- gives the path of the newly changed directory of the file
# listdir - lists all the files present in the path returned by os.getcwd() - Note - current working directory is now inside original folder.
for filename in os.listdir(os.getcwd()):
    source=tinify.from_file(filename)
    source.to_file("D:\\Users\\User-name\\Desktop\\compressed\\"+filename)
    
