from textnode import TextNode, TextType
from generate_files import copy_files
from generate_pages import generate_pages_recursive
def main():
    generate_pages_recursive("content/", "template.html", "static/")
    copy_files("static/", "public/")

if __name__ == "__main__":
    main()