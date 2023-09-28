import sys
import re
from bs4 import BeautifulSoup

def extract_body_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    start_idx = content.find('<body>')
    end_idx = content.find('</body>')
    if start_idx != -1 and end_idx != -1:
        return content[start_idx + 6:end_idx].strip()
    else:
        return content.strip()

def replace_iframes(content):
    start = 0  # Position to start searching for '<iframe' and '</iframe>'
    
    while True:
        iframe_start = content.find('<iframe', start)
        
        if iframe_start == -1: break

        iframe_end = content.find('</iframe>', iframe_start)

        # Check for malformed '<iframe>'
        if iframe_end == -1:
            print(f"Warning: No matching </iframe> for <iframe> at position {iframe_start}.")
            break
        
        # Find 'src' attribute within found '<iframe...>'
        src_start = content.find('src="./', iframe_start) + 5

        if src_start == 4:  # src_start will be 4 if 'src="./' was not found
            print(f"Warning: No 'src' attribute found for <iframe> at position {iframe_start}.")
            break

        src_end = content.find('"', src_start)
        src_file = content[src_start:src_end]

        # Read the src_file content to replace iframe
        replacement_content = extract_body_content(src_file)

        # Replace the iframe with the content from src_file
        content = content[:iframe_start] + replacement_content + content[iframe_end + 9:]

        # Update start position for next search
        start = iframe_end + 9
    
    return content

def wrap_html(content):
    return \
f"""<!DOCTYPE html>
<html>
<head>
    <title></title>
    <link rel="stylesheet" type="text/css" href="{css}">
</head>
<body>
    {content}
</body>
</html>
"""


def traverse_tree(tag, depth):
    try:
        if tag.children == None: return
    except: return
    for child in tag.children:
        if child.name == 'li':
            child['style'] = f"font-size: {16 - depth}px;"
        traverse_tree(child, depth + 1)


if __name__ == "__main__":
    #import pdb; print(sys.argv); pdb.set_trace()

    if len(sys.argv) != 3:
        input_file = "C:\\Users\\Admin\\Documents\\git_clones\\Informaticki_projekat_seminarski_rad\\.outputs\\seminarski_2.html"
        css = "../build_utils/styles.css"
    else:
        input_file = sys.argv[1]
        css = sys.argv[2]
        
    
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    content = replace_iframes(content)

    # Wrapping the entire content with proper HTML structure
    final_content = wrap_html(content)

    
    soup = BeautifulSoup(final_content, 'html.parser')
    root = soup.find('ul')
    root['class'] = "toc"

    traverse_tree(root, 0)

    final_content = str(soup)

    try:
        with open(input_file, "w", encoding="utf-8") as f:
            f.write(final_content)
    except Exception as e:
        print(f"Error writing to {input_file}: {e}")
