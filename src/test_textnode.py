import unittest

from textnode import TextNode,TextType
from main import text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node,node2)
    
    def test_not_eq(self):
        node = TextNode("This is a text node",TextType.NORMAL)
        node2 = TextNode("This is a text node",TextType.ITALIC)
        self.assertNotEqual(node,node2)
    
    def test_text_diff(self):
        node = TextNode("This is a text node",TextType.NORMAL)
        node2 = TextNode("This is another text node",TextType.NORMAL)
        self.assertNotEqual(node.text,node2.text)
    
    def test_url_is_none(self):
        node = TextNode("This is a text node",TextType.BOLD)
        self.assertEqual(node.url,None)
    
    def test_text_node_to_html_node(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    def test_text_to_link(self):
        node = TextNode("Read more",TextType.LINK,"https://scissors-short.netlify.app")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(),'<a href="https://scissors-short.netlify.app" target="_blank">Read more</a>')
    def test_text_to_image(self):
        node = TextNode("test_image",TextType.IMAGE,"https://shorts.zictracks.com/link_image")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(),'<img src="https://shorts.zictracks.com/link_image" alt="test_image"></img>')
        
if __name__ == "__main__":
    unittest.main()