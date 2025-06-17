import os
import shutil
from generate_page import generate_page

public_dir = "./public"
static_dir = "./static"

def main():
    copy_to_public("./static","./public")
    generate_page("./content/index.md","./template.html","public/index.html")

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