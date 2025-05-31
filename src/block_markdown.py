

def markdown_to_blocks(markdown):
    blocks = markdown.strip(" ").strip("\n").split("\n\n")
    return blocks