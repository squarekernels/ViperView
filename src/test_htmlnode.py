import unittest

from htmlnode import HTMLNode

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

if __name__ == "__main__":
    unittest.main()