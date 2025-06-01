from block_markdown import (markdown_to_blocks,block_to_block_type)
from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from inline_markdown import (split_nodes_image,split_nodes_link)
import re

def main():
    md = """
##### This is a heading
"""
    
    blocks = markdown_to_blocks(md)
    try:
        block_type = block_to_block_type(blocks[0])
        print(block_type)
    except ValueError as e:
        print(e)
    
        
main()