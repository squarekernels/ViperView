import unittest
from block_markdown import (
    markdown_to_blocks,
    check_block_type
)


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_check_block_type_heading(self):
        md = "### This is subtitle"
        self.assertEqual(check_block_type(md), "heading")

    def test_check_block_type_code(self):
        md = """```import re

def all_lines_match(text: str, pattern: str) -> bool:
    lines = text.strip().splitlines()
    return all(re.fullmatch(pattern, line.strip()) for line in lines)```"""
        self.assertEqual(check_block_type(md), "code")

    def test_check_block_type_quote(self):
        md = """> I am your Father!
> I'm always angry
> I'm raging fire
> I am Iron Man"""
        self.assertEqual(check_block_type(md), "quote")

    def test_check_block_type_unordered(self):
        md = """- This is an item
- This is another item"""
        self.assertEqual(check_block_type(md), "unordered_list")

    def test_check_block_type_ordered(self):
        md = """1. This is an ordered item
2. Number two
3. Three is a charm"""
        self.assertEqual(check_block_type(md), "ordered_list")

    def test_check_block_type_paragraph(self):
        md = """This is a paragraph.
with just 2 lines."""
        self.assertEqual(check_block_type(md), "paragraph")

    def test_check_block_type_code(self):
        md = """
```import re

def all_lines_match(text: str, pattern: str) -> bool:
    lines = text.strip().splitlines()
    return all(re.fullmatch(pattern, line.strip()) for line in lines)```
"""
        block_type = check_block_type(md)
        self.assertEqual(
           block_type,
           "code" 
        )

def test_check_block_type_quote(self):
        md = """
> I am your Father!
> I'm always angry
> I'm raging fire
> I am Iron Man
"""
        block_type = check_block_type(md)
        self.assertEqual(
           block_type,
           "quote" 
        )

def test_check_block_type_unordered(self):
        md = """
- This is an item
- This is another item
"""
        block_type = check_block_type(md)
        self.assertEqual(
           block_type,
           "unordered_list" 
        )


def test_check_block_type_ordered(self):
        md = """
1. This is an orered item
2. Number two
3. Three is a charm
"""
        block_type = check_block_type(md)
        self.assertEqual(
           block_type,
           "ordered_list" 
        )

def test_check_block_type_paragragh(self):
        md = """This is a paragraph. 
        with just 2 lines. 
"""
        block_type = check_block_type(md)
        self.assertEqual(
           block_type,
           "paragraph" 
        )

if __name__ == "__main__":
    unittest.main()
