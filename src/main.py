from textnode import TextNode, TextType
from generate_files import generate_files

def main():
    generate_files("static/", "public/")
    
if __name__ == "__main__":
    main()