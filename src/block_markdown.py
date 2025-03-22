from enum import Enum

def markdown_to_blocks(markdown):
    x = markdown.split('\n\n')
    y = []
    for i in x:
        if not i:
            continue
        y.append(i.strip())
    return y

class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered list'
    ORDERED_LIST = 'ordered list'

# def block_to_block_type(block):
#     for i in markdown_to_blocks(block):
#         if i[0] == '#':
#             return i, BlockType.HEADING
#         if i[0:3] == '```':
#             return i, BlockType.CODE
#         if i[0] == '>':
#             return i, BlockType.QUOTE
#         if i[0] == '-':
#             return i, BlockType.UNORDERED_LIST
#         if i[0:3] == '1. ':
#             return i, BlockType.ORDERED_LIST
#         else:
#             return BlockType.PARAGRAPH
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