def markdown_to_blocks(text): 
    markdown_blocks = text.split("\n\n")
    filtered_blocks = []
    for block in markdown_blocks:
        if block == "":
            continue
        filtered_blocks.append(block.strip())
    return filtered_blocks