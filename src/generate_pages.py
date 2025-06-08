import re

def extract_title(markdown):
    header = re.search(r"^\s*#\s+(.*)", markdown, re.MULTILINE)
    if header:
        return header.group(1).strip()
    else: 
        raise Exception("There is no header in this file")
    

def generate_pages(from_path, template_path , dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as from_file:
        content = from_file.readlines()
        print(content)
    
generate_pages("content/index.md", "template.html", "public/")