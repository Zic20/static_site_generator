from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    text_node = TextNode("This is some anchor text",TextType.LINK,"https://www.boot.dev")
    print(text_node)
    
    html_node = HTMLNode("<a>","Read more",props={"href":"https://www.google.com","target":"_blank"})
    print(html_node)
    
main()