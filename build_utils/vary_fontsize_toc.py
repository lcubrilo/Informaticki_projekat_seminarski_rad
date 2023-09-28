from bs4 import BeautifulSoup
from toc_start_end_detect import detect_toc_foolproof
from romanize_headings import is_top_level_heading, is_in_ToC

def transform_toc_in_file(lines):
    top_size = 14
    bot_size = 10

    # Detect ToC boundaries
    start, end = detect_toc_foolproof(lines)
    if start == -1:
        raise Exception("ToC not found")

    # Initialize BeautifulSoup object and ul tag
    soup = BeautifulSoup('', 'html.parser')
    ul_tag = soup.new_tag("ul")
    ul_tag['style'] = f"font-size:{bot_size}px"
    
    # Iterate through ToC lines
    for i in range(start, end):
        line = lines[i]
        if not is_in_ToC(line): 
            raise Exception("wtf")

        # Create a new <li> tag
        li_tag = soup.new_tag("li")

        # Set the font size based on whether it's a top-level heading
        font_size = top_size if is_top_level_heading(line) else bot_size
        li_tag['style'] = f"font-size:{font_size}px"

        li_tag.string = line
        ul_tag.append(li_tag)

    # Replace the original ToC lines with the new HTML ul tag
    lines[start-1:end] = [str(ul_tag)]

    return lines

# Sample lines for testing (you'll need to import or define test_string)
# from sample import test_string
# for line in transform_toc_in_file(test_string.split("\n")):
#    print(line)
