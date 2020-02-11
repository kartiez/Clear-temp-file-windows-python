import os, shutil
folder = "YOUR TEMP LOCATION HERE"
filescount= 0
foldercount = 0
notdeletedfiles = 0
filesize = 0
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        else:  
            shutil.rmtree(file_path)
            foldercount += 1
    except Exception as e:
       notdeletedfiles +=1


print("\n\n---------Result---------")
print("Cleared : {}".format(filesize))
print("File deleted : {}".format(filescount))
print("Folders deleted : {}".format(foldercount))
print("File/Folders not deleted : {}".format(notdeletedfiles))
print("----------------------------")
