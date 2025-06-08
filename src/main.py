import sys
from textnode import TextNode, TextType
from generate_files import copy_files
from generate_pages import generate_pages_recursive

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[0]
    else: 
        basepath = "/"
        
    generate_pages_recursive(basepath, "content/", "template.html", "static/")
    copy_files("static/", "docs/")

if __name__ == "__main__":
    main()