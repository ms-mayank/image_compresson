import os
import tinify
tinify.key="your_API KEY"
os.chdir(os.getcwd()+'\\original')
for filename in os.listdir(os.getcwd()):
    source=tinify.from_file(filename)
    source.to_file("D:\\Users\\SHUKLM14\\Desktop\\Thailand portal\\compressed\\"+filename)
