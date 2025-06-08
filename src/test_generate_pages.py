import unittest
from generate_pages import extract_title

class TextExtractFiles(unittest.TestCase):
    def test_extract_title_single_world(self):
        markdown = """
        # Hello
        """
        header = extract_title(markdown) 
        self.assertEqual(header, "Hello")

    def test_extract_title_multi_world(self):
        markdown = """
        #   Welcome World  
        """
        header = extract_title(markdown)
        self.assertEqual(header, "Welcome World")

    def test_extract_title_heading_2_before(self):
        markdown = """
        ## Not an H1\n# Real H1
        """
        header = extract_title(markdown)
        self.assertEqual(header, "Real H1")

    def test_extract_title_error(self):
        markdown ="""
No header in this
"""     
        self.assertRaises(Exception, extract_title, markdown)

if __name__ == "__main__":
    unittest.main()
