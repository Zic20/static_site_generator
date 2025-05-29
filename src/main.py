from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
import re

def main():
    text_node = TextNode("This is some anchor text",TextType.LINK,"https://www.boot.dev")
    print(text_node)
    
    html_node = HTMLNode("<a>","Read more",props={"href":"https://www.google.com","target":"_blank"})
    print(html_node)
    

def text_node_to_html_node(text_node):
    match(text_node.text_type):
        case (TextType.TEXT):
            return LeafNode(None,value=text_node.text)
        case (TextType.BOLD):
            return LeafNode("b",text_node.text)
        case (TextType.ITALIC):
            return LeafNode("i",text_node.text)
        case (TextType.CODE):
            return LeafNode("code",text_node.text)
        case (TextType.LINK):
            return LeafNode("a",text_node.text,{"href":text_node.url,"target":"_blank"})
        case (TextType.IMAGE):
            return LeafNode("img","",{"src":text_node.url,"alt":text_node.text})
        case _:
            raise Exception("invalid text type given to text_node")
        
main()