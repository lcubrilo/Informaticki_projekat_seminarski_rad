import sys
import os

def replace_iframes(input_file):
    try:
        with open(src_file, "r", encoding="utf-8") as f:
            replacement_content = f.read()
        print(f"Successfully read {src_file}. Replacing iframe content.")
    except FileNotFoundError:
        print(f"Error: File {src_file} referenced in 'src' not found.")
        return

    start = 0  # Position to start searching for '<iframe' and '</iframe>'
    
    while True:
        iframe_start = content.find('<iframe', start)
        
        # Break if no more '<iframe' found
        if iframe_start == -1:
            break

        iframe_end = content.find('</iframe>', iframe_start)

        # Check for malformed '<iframe>'
        if iframe_end == -1:
            print(f"Warning: No matching </iframe> for <iframe> at position {iframe_start}.")
            break
        
        # Find 'src' attribute within found '<iframe...>'
        src_start = content.find('src="./', iframe_start) + 5  # We look for 'src="./' specifically to match your case

        if src_start == 4:  # src_start will be 4 if 'src="./' was not found
            print(f"Warning: No 'src' attribute found for <iframe> at position {iframe_start}.")
            break

        src_end = content.find('"', src_start)
        src_file = content[src_start:src_end]

        # Modify the src_file here to add another dot, given that the file location has changed
        modified_src_file = "." + src_file

        # Replace the original 'src' with the modified one in the content
        content = content[:src_start] + modified_src_file + content[src_end:]

        # Update start position for next search
        start = iframe_end + 9  # Update to end of </iframe>

    try:
        with open(input_file, "w", encoding="utf-8") as f:
            f.write(content)
    except Exception as e:
        print(f"Error writing to {input_file}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python convert_iframes.py <input_html_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    replace_iframes(input_file)
