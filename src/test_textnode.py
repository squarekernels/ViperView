import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_textnode_equality(self):
        node1 = TextNode("Hello", TextType.TEXT, None)
        node2 = TextNode("Hello", TextType.TEXT, None)
        self.assertEqual(node1, node2)

    def test_textnode_inequality_different_url(self):
        node1 = TextNode("Click here", TextType.LINK, "https://example.com")
        node2 = TextNode("Click here", TextType.LINK, "https://boot.dev")
        self.assertNotEqual(node1, node2)

    def test_textnode_inequality_different_text_type(self):
        node1 = TextNode("This is text", TextType.TEXT, None)
        node2 = TextNode("This is text", TextType.BOLD, None)
        self.assertNotEqual(node1, node2)

    def test_textnode_inequality_different_text(self):
        node1 = TextNode("Text A", TextType.TEXT, None)
        node2 = TextNode("Text B", TextType.TEXT, None)
        self.assertNotEqual(node1, node2)
    

if __name__ == "__main__":
    unittest.main()