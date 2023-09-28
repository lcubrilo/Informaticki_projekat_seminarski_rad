import sys
from bs4 import BeautifulSoup

def clean_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    main_ul = soup.find('ul')
    
    new_main_ul = soup.new_tag('ul')
    new_main_ul['style'] = main_ul['style']
    
    for li in main_ul.find_all('li', recursive=False):
        nested_ul = li.find('ul')
        if nested_ul:
            nested_li = nested_ul.find('li')
            if nested_li and nested_li.string:
                #li.string = nested_li.string  # Replace the inner HTML content of the parent li with that of the nested li
                li.append(nested_li.find('a'))
            
            # Remove the original nested structure
            nested_ul.decompose()
        
        new_main_ul.append(li)
        
    main_ul.replace_with(new_main_ul)
    
    return str(soup.prettify())

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fix_html_toc.py <input_html_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    
    with open(file_path, 'r', encoding='utf-8') as f:
        original_html = f.read()
        
    cleaned_html = clean_html(original_html)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(cleaned_html)

    print(f"Cleaned HTML has been saved to {file_path}")


if __name__ == "__main2__":
    from sample import test_html
    cleaned_html = clean_html(test_html)
    print(cleaned_html)