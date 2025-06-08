import re
from markdown_blocks import markdown_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode

def read_contents(file):
    with open(file, "r")as f:
        content = f.read()

    return content 

def extract_title(markdown):
    header = re.search(r"^\s*#\s+(.*)", markdown, re.MULTILINE)
    if header:
        return header.group(1).strip()
    else: 
        raise Exception("There is no header in this file")
    

def generate_pages(from_path, template_path , dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown = read_contents(from_path)
    template = read_contents(template_path)

    html_content = markdown_to_html_node(markdown) 
    html = html_content.to_html()
    
    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    print(template)

generate_pages("content/index.md", "./template.html", "public/")