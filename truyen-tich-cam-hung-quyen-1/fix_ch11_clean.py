import re

path = 'chapters/ch11-moi-ngay-mot-cau-chuyen.tex'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# removing old sections
content = re.sub(r'\\section\{[^\}]+\}\n*', '', content)

def add_section(m):
    title = m.group(1).strip()
    return f"\\section{{{title}}}\n" + m.group(0)
    
# Match \begin{truyen}{TITLE}
content = re.sub(r'\\begin\{truyen\}\{([^}]+)\}', add_section, content)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed Chapter 11 Clean!")
