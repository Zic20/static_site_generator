from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from inline_markdown import (split_nodes_image,split_nodes_link)
import re

def main():
    node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
    new_nodes = split_nodes_image([node])
    
    print(new_nodes)
   
    # node2 = TextNode(
    #     "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    #     TextType.TEXT,
    # )
    # new_nodes = split_nodes_link([node2])
    # print(new_nodes)
   
    # split_nodes_image([node])
    

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