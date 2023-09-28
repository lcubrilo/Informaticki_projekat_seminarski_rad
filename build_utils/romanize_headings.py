import pdb
from romanize_data import heading_D2R, empty_head

def is_heading(line):
    def toc(i, dictio): 
        # Difference to is_in_ToC??? 
        return (i < len(dictio)//2)
    
    for i, (num_head, rom_head) in enumerate(heading_D2R().items()):
        if num_head in line.strip():
            #return True, num_head, rom_head, empty_head(toc(i,heading_D2R())) #this was correct
            # Changed my mind about the prefernce, making the code ugly
            toc_val = toc(i,heading_D2R())
            return True, num_head, rom_head, empty_head(toc_val) if toc_val else rom_head[:-1]+"-"

    return False, None, None, None

def is_in_ToC(line): return not line.startswith("#")

def is_top_level_heading(line):  # Heading can be in Table of Contents or main text
    return line.count(".") == 1  if is_in_ToC(line) else line.startswith("# ")


def romanize_top_level_heading(new_lines):
    # Convert all heading lines into a roman-first enumeration
    for i, line in enumerate(new_lines):
        boolean, num_head, rom_head, empty = is_heading(line)
        if boolean:
            replacer = rom_head if is_top_level_heading(line) else empty
            new_lines[i] = line.replace(num_head, replacer)

    return new_lines

if __name__ == "__main__":
    from sample import test_md  
    test = test_md

    lines = test.split("\n")
    for line in lines:
        """yo"""
        # print(f"{is_heading(line)[0]}, {is_top_level_heading(line)}: {line}")
    for line in romanize_top_level_heading(lines):
        print(line)
  