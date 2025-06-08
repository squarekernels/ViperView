import re

def extract_title(markdown):
    header = re.search(r"^\s*#\s+(.*)", markdown, re.MULTILINE)
    if header:
        return header.group(1).strip()
    else: 
        raise Exception("There is no header in this file")
    
