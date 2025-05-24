import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_single(self):
        node = HTMLNode(props={"href": "https://example.com"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com"')

    def test_props_to_html_multiple(self):
        node = HTMLNode(props={"href": "https://example.com", "target": "_blank"})
        self.assertIn(' href="https://example.com"', node.props_to_html())
        self.assertIn(' target="_blank"', node.props_to_html())

    def test_props_to_html_empty(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), '')

    def test_repr(self):
        node = HTMLNode(tag="a", value="Link", props={"href": "https://boot.dev"})
        self.assertEqual(
            repr(node),
            "HTMLNode(tag=a, value=Link, children=[], props={'href': 'https://boot.dev'})"
        )

    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Just text.")
        self.assertEqual(node.to_html(), "Just text.")

    def test_leaf_to_html_raises_without_value(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)

    def test_leaf_to_html_with_multiple_props(self):
        node = LeafNode("a", "Boot.dev", {"href": "https://boot.dev", "target": "_blank"})
        result = node.to_html()
        # Since props can be in any order, we'll check for substrings instead of full equality
        self.assertTrue(result.startswith("<a"))
        self.assertIn('href="https://boot.dev"', result)
        self.assertIn('target="_blank"', result)
        self.assertTrue(result.endswith(">Boot.dev</a>"))

if __name__ == "__main__":
    unittest.main()

