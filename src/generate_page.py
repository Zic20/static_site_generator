import os
from block_markdown import extract_title, markdown_to_html_node
from pathlib import Path


def generate_page(from_path,template_path,dest_path):
    print(f"Generating a page from {from_path} to {dest_path} using {template_path}")
    from_file = open(from_path,"r")
    md = from_file.read()
    from_file.close()
    temp =  open(template_path,"r")
    template = temp.read()
    temp.close()
    
    node = markdown_to_html_node(md)
    html = node.to_html()
    title = extract_title(md)
    template = template.replace("{{ Title }}",title)
    template = template.replace("{{ Content }}",html)
    
    if not os.path.exists(os.path.dirname(dest_path)):
        os.mkdir(dir)
    
    with open(dest_path,"w") as f:
        f.write(template)
    
    
def generate_pages_recursive(dir_path_content,template_path,dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    
    if not os.path.exists(dir_path_content):
        raise Exception("invalid source path provided")
    
    p = Path(dir_path_content)
    
    for subdir in p.iterdir():
        if subdir.is_dir():
            dest = dest_dir_path + f"/{subdir.name}"
            generate_pages_recursive(subdir,template_path,dest)
        else:
            to_file_path = dest_dir_path + f"/{subdir.name}"
            generate_page(subdir,template_path,to_file_path.replace("md","html"))   
    
    
