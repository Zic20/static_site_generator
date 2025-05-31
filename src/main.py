from block_markdown import markdown_to_blocks
from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from inline_markdown import (split_nodes_image,split_nodes_link)
import re

def main():
    md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
    """
    
    blocks = markdown_to_blocks(md)
    print(blocks)
        
main()