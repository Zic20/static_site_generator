from enum import Enum

from inline_markdown import text_node_to_html_node, text_to_textnodes
from parentnode import ParentNode
from textnode import TextNode, TextType
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE =  "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    
def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def is_leading_char_valid(char,text,target_count,minimunCount = 1):
    count = 0
    while text.startswith(char):
        count+=1
        text = text[len(char):]
    if count > target_count or count < minimunCount:
        return count,False
    return count, True

def is_closing_char_valid(char,text,target_count,minimunCount = 1):
    count = 0
    while text.endswith(char):
        count+=1
        text = text[:len(text)-1]
    if count > target_count or count < minimunCount:
        return count,False
    return count, True

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html = block_to_html_node(block)
        children.append(html)
    return ParentNode("div",children,None)


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    
    match(block_type):
        case(BlockType.PARAGRAPH):
            return paragraph_to_html_node(block)
        case(BlockType.HEADING):
            return heading_to_html_node(block)
        case(BlockType.CODE):
            return code_to_html_node(block)
        case(BlockType.UNORDERED_LIST):
            return unordered_list_to_html_list(block)
        case(BlockType.ORDERED_LIST):
            return ordered_list_to_html_node(block)
        case(BlockType.QUOTE):
            return quote_to_html_node(block)
        case _:
            raise ValueError("invalid block type")


def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p",children)

def heading_to_html_node(block):
    count,is_heading_valid = is_leading_char_valid("#",block,6,1)
    if is_heading_valid == False:
        raise ValueError(f"invalid heading level: {count}")
    text = block[count + 1:]
    children = text_to_children(text)
    return ParentNode(f"h{count}", children)

def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError('invalid code blockl')
    text = block[4:-3]
    raw_text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(raw_text_node)
    code = ParentNode("code",[child])
    return ParentNode("pre",[code])

def ordered_list_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

def unordered_list_to_html_list(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li",children))
    return ParentNode("ul",html_items)

def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def extract_title(markdown):
    matches = re.findall(r"^# (.+)",markdown,re.MULTILINE)
    if len(matches) < 1:
        raise Exception("no header found in the markdown")
    return matches[0].strip()