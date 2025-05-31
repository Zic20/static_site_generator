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
    
        
main()