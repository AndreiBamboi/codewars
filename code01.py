import os
print("root prints out directories only from what you specified")
print("dirs prints out sub-directories from root")
print("files prints out all files from root and directories")
print("*" * 20)
for root, dirs, files in os.walk("C:/Users/abamboi/PycharmProjects/codewars/Client_script"):
    print (root)
    print (dirs)
    print (files)