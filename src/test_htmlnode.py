import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_single(self):
        node = HTMLNode(props={"href": "https://example.com"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com"')

    def test_props_to_html_multiple(self):
        node = HTMLNode(props={"href": "https://example.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com" target="_blank"')
    
    def test_props_to_html_empty(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), '')

    def test_repr(self):
        node = HTMLNode(tag="a", value="Link", props={"href": "https://boot.dev"})
        self.assertEqual(
            repr(node),
            "HTMLNode(tag=a, value=Link, children=[], props={'href': 'https://boot.dev'})"
        )

class TestLeafNode(unittest.TestCase):
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

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_multiple_children(self):
        children = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ]
        node = ParentNode("p", children)
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_raises_without_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("p", "test")])

    def test_to_html_raises_without_children(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None)

    def test_nested_parent_nodes(self):
        nested = ParentNode("div", [
            ParentNode("section", [
                ParentNode("article", [
                    LeafNode("p", "deep")
                ])
            ])
        ])
        self.assertEqual(nested.to_html(), "<div><section><article><p>deep</p></article></section></div>")


if __name__ == "__main__":
    unittest.main()

