from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if text_type == TextType.TEXT:
        return old_nodes
    if text_type == TextType.CODE:
        positions = [old_nodes.text.find(part) for part in old_nodes.text.split(delimiter)]
        positions.remove(0)
        if len(positions)%2 != 0 or not positions:
            return old_nodes
        
        pairs = []
        for i in range(len(positions)-1):
            tup = (positions[i],positions[i+1])
            pairs.append(tup)
        
        markdown_strings = []
        for tups in pairs:
            markdown_strings.append(old_nodes.text[tups[0]:tups[1]-1])

        for i in markdown_strings:
            i = f'{delimiter}{i}{delimiter}'

        print(markdown_strings)        
    
        node_list = old_nodes.text.split(delimiter)
        for i in node_list:
            for j in markdown_strings:
                if i == j:
                    node_list.remove(j)
        
        

            




node = TextNode("This is text with a `code block` word", TextType.TEXT)
new_nodes = split_nodes_delimiter(node, "`", TextType.CODE)

print(new_nodes)