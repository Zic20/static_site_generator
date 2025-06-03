import unittest

from block_markdown import (markdown_to_blocks,block_to_block_type,BlockType, markdown_to_html_node)


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
def test_paragraphs(self):
    md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )

def test_codeblock(self):
    md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
    )