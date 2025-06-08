from textnode import TextNode, TextType
from generate_files import copy_files
from generate_pages import generate_pages
def main():
    generate_pages("content/index.md", "template.html", "static/index.html")
    copy_files("static/", "public/")

if __name__ == "__main__":
    main()