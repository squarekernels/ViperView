import re
from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def check_block_type(block: str) -> str:
    block = block.strip()
    lines = block.splitlines()

    # Code block: starts and ends with ```
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE.value

    # Heading: starts with 1–6 hashes followed by space
    if re.fullmatch(r'#{1,6} .+', lines[0]):
        return BlockType.HEADING.value

    # Quote: every line starts with >
    if all(line.strip().startswith('>') for line in lines):
        return BlockType.QUOTE.value

    # Unordered list: every line starts with "- "
    if all(line.strip().startswith('- ') for line in lines):
        return BlockType.UNORDERED_LIST.value

    # Ordered list: lines must start with incrementing numbers like 1. 2. 3.
    ordered_match = True
    for i, line in enumerate(lines):
        if not re.match(fr'{i + 1}\. ', line.strip()):
            ordered_match = False
            break
    if ordered_match:
        return BlockType.ORDERED_LIST.value

    return BlockType.PARAGRAPH.value

def markdown_to_blocks(text): 
    markdown_blocks = text.split("\n\n")
    filtered_blocks = []
    for block in markdown_blocks:
        if block == "":
            continue
        filtered_blocks.append(block.strip())
    return filtered_blocks