import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_prop_to_html(self):
        htmlnode = HTMLNode("<a>","Read more",props={"href":"https://www.google.com","target":"_blank"})
        self.assertEqual(htmlnode.props_to_html(),' href="https://www.google.com" target="_blank"')
        
    def test_no_prop_passed(self):
        htmlnode = HTMLNode("<a>","Read more")
        self.assertEqual(htmlnode.props_to_html(),"")
    
    
    def test_children_is_none(self):
        htmlnode = HTMLNode("<a>","Read more",props={"href":"https://www.google.com","target":"_blank"})
        self.assertEqual(htmlnode.children,None)
    