import os
import shutil
import sys
from generate_page import generate_page,generate_pages_recursive

public_dir = "./docs"
static_dir = "./static"

def main():
    shutil.rmtree(public_dir)
    basepath = "/"
    if len(sys.argv) > 0:
        basepath = sys.argv[1]
    print(basepath)
    copy_to_public("./static",public_dir)
    generate_pages_recursive("./content","./template.html",public_dir,basepath)

def copy_to_public(source,destination):
    if not os.path.exists(source):
        raise Exception("invalid source path provided")
    
    if not os.path.exists(destination):
        os.mkdir(destination)
    
    items = os.listdir(source)
    for item in items:
        file_path = os.path.join(source,item)
        destination_dir = os.path.join(f"{destination}/{item}")
        if not os.path.isfile(file_path):
            copy_to_public(file_path,destination_dir)
        else:
            shutil.copy(file_path,f"{destination}")
        
main()