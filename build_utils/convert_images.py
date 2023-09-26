import sys
import os
from romanize_headings import romanize_top_level_heading

def find_image_syntax(line):
    start_pos = line.find("![")
    if start_pos == -1:
        return None, None, None
    
    end_pos = line.find(")", start_pos)
    if end_pos == -1:
        return None, None, None
    
    alt_text_start = start_pos + 2
    alt_text_end = line.find("]", alt_text_start)
    if alt_text_end == -1:
        return None, None, None
    
    img_link_start = alt_text_end + 2  # Skipping over "]("
    img_link_end = end_pos
    
    alt_text = line[alt_text_start:alt_text_end]
    img_link = line[img_link_start:img_link_end]
    
    return start_pos, end_pos, (alt_text, img_link)

def convert_images(input_file, output_folder):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    figure_count = 0

    for line in lines:
        start_pos, end_pos, image_data = find_image_syntax(line)
        if image_data:
            alt_text, img_link = image_data
            if not img_link.startswith("http"): img_link = "../images/" + img_link
            figure_count += 1

            new_line = \
            f'<figure style="text-align:center;"> \n\
                <img src="{img_link}" alt="{alt_text}" style="width: 65%;"> \n\
                <figcaption> \n\
                    Slika {figure_count}: {alt_text} \n\
                </figcaption> \n\
              </figure> \n'

            new_lines.append(line[:start_pos] + new_line + line[end_pos + 1:])
        else:
            new_lines.append(line)

    return new_lines

              
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_images.py <input_markdown_file> <output_folder>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_folder = sys.argv[2]
    
    new_lines = convert_images(input_file, output_folder)
    new_lines = romanize_top_level_heading(new_lines)

    output_file = os.path.join(output_folder, os.path.basename(input_file).replace('.md', '_2.md'))

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
