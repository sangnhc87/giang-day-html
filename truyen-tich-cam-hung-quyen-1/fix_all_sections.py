import re
import glob

files = glob.glob('chapters/ch*.tex')

for path in files:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Clean up ANY existing \section{...} or \subsection{...} or \subsection*{...}
    content = re.sub(r'\\section\*?\{[^\}]+\}\n*', '', content)
    content = re.sub(r'\\subsection\*?\{[^\}]+\}\n*', '', content)
    
    # Also clean up \addcontentsline if any
    content = re.sub(r'\\addcontentsline[^\n]+\n*', '', content)
    
    # Now, find every \begin{truyen}{TITLE}{...} and insert \section{TITLE} right before it
    def add_section(m):
        title = m.group(1).strip()
        # Some titles have "1. The Cup of Tea", let's strip the number "1. " if present
        clean_title = re.sub(r'^\d+\.\s*', '', title)
        return f"\\section{{{clean_title}}}\n" + m.group(0)
        
    content = re.sub(r'\\begin\{truyen\}\{([^}]+)\}\{[^}]+\}', add_section, content)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("TOC sections injected into all chapters!")
