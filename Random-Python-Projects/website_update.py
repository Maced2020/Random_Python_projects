#this is used to update the webgames website automaticlly so that I dont have to run
# multiple commands everytime. 

import os
import time
import sys

# Global Variables
webgames_folder_path = "/home/ubuntu/webgames" #respository location
htmlfolder = "/var/www/html/" #html location
githubcommand = "sudo git clone https://github.com/Maced2020/webgames.git"
directoryfound = False
filedeleted = False
question1 = "no"
htmlfolderhascontents = False
backupfolder = '/home/ubuntu/backup/'
htmlfolderbackedup = False
deletebackupfoldercommand = "sudo rm -r /home/ubuntu/backup/* "
backuphtmlfolder = "sudo cp /var/www/html/* -r /home/ubuntu/backup/"
deletehtmlfolder = 'sudo rm -r /var/www/html/*'
copywebgamescontentsintohtml = 'sudo cp /home/ubuntu/webgames/* -r /var/www/html/'
copywebgamesfolderintohtml = 'sudo cp /home/ubuntu/webgames/ -r /var/www/html/'


# this will check for the webgames folder and give the user the option to delete it
if os.path.exists(webgames_folder_path) and os.path.isdir(webgames_folder_path):
    directoryfound = True
else:
    os.mkdir(webgames_folder_path)
    directoryfound = True

if directoryfound == True:
    question1 = input(webgames_folder_path + " has been found would you like to delete this directory: ")

if question1.upper() == "Y" or question1.upper() == "YES":
    os.system("sudo rm -r " + webgames_folder_path)
    print(webgames_folder_path + " has been deleted.")
    filedeleted = True
else:
    print("no folder deleted")
    print("aborting")
    time.sleep(2)
    sys.exit(1)

time.sleep(2)

# if the webgames folder is not already there or has been deleted then this will
# clone the webgames repo

if filedeleted or directoryfound == False:
    os.system(githubcommand)
    print("repository downloaded")

time.sleep(2)


# Check if the HTML directory has contents
if any(os.scandir(htmlfolder)):  
    htmlfolderhascontents = True
    print("The HTML folder has stuff in it.")
    if not os.path.exists(backupfolder):
        time.sleep(2)
        print("making backup folder as one does not exist")
        os.mkdir(backupfolder)
        time.sleep(2)



time.sleep(2)

# verifies if anything is in the backup folder
# if there is stuff in the folder then it deletes everything.
if any(os.scandir(backupfolder)):
    os.system(deletebackupfoldercommand)
    print('The backup folder has been cleaned out.')
else:
    print('Nothing in the backup folder')

time.sleep(2)

# if the HTML folder has anything in it, it will be backed up into the backup folder
if htmlfolderhascontents:
    os.system(backuphtmlfolder)
    print("The items from the webpage have been backed up.")
    htmlfolderbackedup = True

time.sleep(2)
# deleting everyting in the HTML folder
if htmlfolderbackedup:
    os.system(deletehtmlfolder)
    htmlfolderhascontents2 = False
    print("HTML directory emptied")

time.sleep(2)

# Updating the HTML directory with the updated webgames code.
if htmlfolderhascontents2 == False:
    os.system(copywebgamescontentsintohtml)
    os.system(copywebgamesfolderintohtml)
    print("HTML directory updated")
    time.sleep(2)
    print("automation finished.")
    sys.exit(1)




