import re
import glob

files = glob.glob('chapters/ch*.tex')

for path in files:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    content = re.sub(r'\\section\{[^{}]+\}\n*', '', content)
    
    def repl(m):
        title = m.group(1).strip()
        return f"\\section{{{title}}}\n"
        
    content = re.sub(r'\\subsection\*\{(?:Câu|Truyện)\s+\d+\s+(?:\\quad|[-—:])?\s*(.*?)\}', repl, content)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Headings fixed in chapters!")
