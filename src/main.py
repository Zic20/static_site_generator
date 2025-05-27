from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode

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
        
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes
    
main()