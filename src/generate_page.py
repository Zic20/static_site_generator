import os
from block_markdown import extract_title, markdown_to_html_node



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
    
    
    
    
