from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE =  "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    
def markdown_to_blocks(markdown):
    blocks = markdown.strip(" ").strip("\n").split("\n\n")
    return blocks

def block_to_block_type(block):
    match(block[0]):
        case("#"):
            count,isValid = is_leading_char_valid("#",block,6)
            if isValid == True:
                if block.startswith("#"*count + " "):
                    return BlockType.HEADING            
            raise ValueError("invalid heading construction")
        case("`"):
            _,valid_opening_tags = is_leading_char_valid("`",block,3,3)
            _,valid_closing_tags = is_closing_char_valid("`",block,3,3)
            
            if valid_opening_tags == True and valid_closing_tags == True:
                if block.startswith("`"*3 + " ") and block.endswith(" "+"`"*3):
                    return BlockType.CODE
            raise ValueError("invalid code block formation")
        case(">"):
            lines = block.split("\n").strip(" ")
            for line in lines:
                if line.startswith("> "):
                    continue
                else: 
                    raise ValueError("invalid quote line")
            return BlockType.QUOTE
        case("-"):
            lines = block.split("\n").strip(" ")
            for line in lines:
                if line.startswith("- "):
                    continue
                else: 
                    raise ValueError("invalid unordered list line")
            return BlockType.UNORDERED_LIST
        case("."):
            lines = block.strip(" ").split("\n")
            for line in lines:
                if line.startswith(". "):
                    continue
                else: 
                    raise ValueError("invalid ordered list line")
            return BlockType.ORDERED_LIST
        case _:
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