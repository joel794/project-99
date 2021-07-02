import os 
import shutil
import time

def main ():
    deletedFiles = 0
    deletedFolders = 0

    path  = '/PATH_TO_DELETE'
    days  = 30
    seconds  = time.time()-(days*24*60*60)
    if os.path.exists():
        for root_folders, files, folders in os.walk(path):
            if seconds>= get_file_or_folder_age(root_folders):
                remove_folder(root_folders)
                deletedFolders += 1
                break

            else:
                for folder in folders :
                    folder_path = os.path.join(root_folders,folder)
                    if seconds>= get_file_or_folder_age(folder_path):
                        remove_folder(folder_path)
                        deletedFolders += 1
                for file in files :
                    file_path = os.path.join(root_folders,file)
                    if seconds>= get_file_or_folder_age(file_path):
                        remove_file(file_path)
                        deletedFiles += 1  :
    else:
       print(f'"{path}" is not found') 
       deletedFiles += 1
    print(f'Total Files Deleted: {deletedFiles}')          
    print(f'Total Folders Deleted: {deletedFolders}') 

def remove_file(path):
    if not os.remove(path):
        print (f'{path}removed succesfully')
    else:
        print ('unable to find path'+ path)

def remove_folders(path):
    if not shutil.rmtree(path):
        print (f'{path}removed succesfully')
    else:
        print ('unable to delete path'+ path)
def get_file_or_folder_age(path):
    ctime = os.stat(path).st_ctime
    return ctime

if __name__ == '__main__'():
    main()
                               

                     
