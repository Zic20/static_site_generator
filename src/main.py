import os
import shutil

def main():
    copy_to_public("./static","./public")

def copy_to_public(source,destination):
    if not os.path.exists(source):
        raise Exception("invalid source path provided")
    
    items = os.listdir(source)
    for item in items:
        file_path = os.path.join(source,item)
        destination_dir = os.path.join(f"{destination}/{item}")
        if not os.path.isfile(file_path):
            if os.path.exists(destination_dir) and destination_dir != "./public":
                shutil.rmtree(destination_dir)
            os.mkdir(destination_dir)
            copy_to_public(file_path,destination_dir)
        else:
            shutil.copy(file_path,f"{destination}")
        
main()