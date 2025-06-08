import re
import os
from pathlib import Path
from markdown_blocks import markdown_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from generate_files import copy_files

def read_contents(file):
    with open(file, "r") as f:
        return f.read()

def write_contents(file, data):
    os.makedirs(os.path.dirname(file), exist_ok=True)
    with open(file, "w") as f:
        f.write(data)

def extract_title(markdown):
    header = re.search(r"^\s*#\s+(.*)", markdown, re.MULTILINE)
    if header:
        return header.group(1).strip()
    else: 
        raise Exception("There is no header in this file")

def check_folders(current_path, template_path, dest_path, rel_path=""):
    for item in os.listdir(current_path):
        full_path = os.path.join(current_path, item)
        rel_item_path = os.path.join(rel_path, item)

        if os.path.isdir(full_path):
            check_folders(full_path, template_path, dest_path, rel_item_path)
        elif item.endswith(".md"):
            from_path = full_path
            to_rel_path = os.path.splitext(rel_item_path)[0] + ".html"
            to_path = os.path.join(dest_path, to_rel_path)
            generate_pages(from_path, template_path, to_path)

def generate_pages(from_path, template_path , dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown = read_contents(from_path)
    template = read_contents(template_path)

    html_content = markdown_to_html_node(markdown) 
    html = html_content.to_html()
    
    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    write_contents(dest_path, template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    check_folders(dir_path_content, template_path, dest_dir_path)