#! python3
#backuoToZip.py - Copies an entire folder and its contents into a Zip file
#whose filename increments.

import os , zipfile

def backupToZip(folder):

    #backup the entire contents of 'folder into a Zip file.

    folder = os.path.abspath('/home/sanker/kids')    #make sure folder is absolute
    # Figure out the filename this code should use based on what files already exist.
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1
    print(f'Creating {zipFilename}.....')
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Walk the entire folder tree and compress the files in each folder.
    for foldername , subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}....')
        #add the current folder to the Zip file.
        backupZip.write(foldername)

        #add all the files in this folder to the zip file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue                   #dont backup up the backup zip files
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')


backupToZip('/home/sanker/kids')



