import re

path = 'chapters/ch11-moi-ngay-mot-cau-chuyen.tex'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Removing artifacts
content = re.sub(r'\$\w+\}\}\n*', '', content)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed Chapter 11 artifacts!")
