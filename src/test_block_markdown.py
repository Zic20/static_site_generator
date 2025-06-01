import unittest

from block_markdown import (markdown_to_blocks,block_to_block_type,BlockType)


class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_block_to_block_type_heading(self):
        md = """
##### This is a heading
"""
        block_type = block_to_block_type(markdown_to_blocks(md)[0])
        self.assertEqual(block_type,BlockType.HEADING)
        
    def test_block_to_block_type_heading_error(self):
        md = """
#####This is a heading
"""
        with self.assertRaises(ValueError) as context:
            self.assertTrue("invalid heading construction",block_to_block_type(markdown_to_blocks(md)[0]))
    
    def test_block_to_block_type_ordered_list(self):
        md = """
. This is a list
. With two items        
"""
        self.assertEqual(block_to_block_type(markdown_to_blocks(md)[0]),BlockType.ORDERED_LIST)