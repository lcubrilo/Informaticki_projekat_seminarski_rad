
#region Function to detect the start of the ToC
def detect_toc_start_title(lines, start_string="# Sadržaj"):
    for i, line in enumerate(lines):
        if line.strip().startswith(start_string):
            return i+1
    return -1

def detect_toc_start_syntax(lines, heading_string="- ["):
    for i, line in enumerate(lines):
        if line.strip().startswith(heading_string):
            return i
    return -1
#endregion

#region Functions to detect the end of the ToC
def detect_toc_end_syntax(lines, start_idx):
    for i, line in enumerate(lines[start_idx:]):
        if not line.strip().startswith("- ["):
            return start_idx + i
    return -1

def detect_toc_end_triple_line(lines, start_idx):
    for i, line in enumerate(lines[start_idx:]):
        if line.strip() == "---":
            return start_idx + i -1
    return -1

def detect_toc_end_div(lines, start_idx):
    for i, line in enumerate(lines[start_idx:]):
        if line.strip() == '<div style="page-break-before: always;"></div>':
            return start_idx + i
    return -1
#endregion

detect_toc_start = [detect_toc_start_syntax, detect_toc_start_title]
detect_toc_end = [detect_toc_end_syntax, detect_toc_end_triple_line, detect_toc_end_div]

def detect_toc_range(lines, start_index, end_index):
    start_method = detect_toc_start[start_index]
    end_method = detect_toc_end[end_index]
    print(f"Using '{start_method.__name__}' and '{end_method.__name__}'")

    start = start_method(lines)
    end = end_method(lines, start)

    return start, end

def detect_toc_foolproof(lines):
    for i in range(2):
        for j in range(3):
            tmp = detect_toc_range(lines, i, j)
            if tmp[0] != -1 and tmp[1] != -1:
                return tmp

def test1(test_string):
    def run_test(i, j, doPrint=False):
        if doPrint: print("\n\n=====================================")
        lines = test_string.split("\n")
        start, end = detect_toc_range(lines, i, j)

        if doPrint: print("=====================================")
        if doPrint: print(f"From: {start} to: {end}")
        if doPrint: print("=====================================")

        start_line = "\n\t".join(lines[start-1:start+2]) if start != -1 else 'NOT_FOUND'
        end_line = "\n\t".join(lines[end-1:end+2]) if end != -1 else 'NOT_FOUND'
        if doPrint: print("Start: \n", start_line)
        if doPrint: print("--------")
        if doPrint: print("End: \n", end_line)
        if doPrint: print("=====================================\n\n")

        return start, end

    results = {}
    for i in range(2):
        for j in range(3):
            results[f"{i}, {j}"] = run_test(i, j)
    
    for input, res in results.items():
        print(f"{input} - > {res}")
    
    return results

if __name__ == "__main__":
    from sample import test_md
    test1(test_md)
    lines = test_md.split("\n")
    print(detect_toc_foolproof(lines))
    