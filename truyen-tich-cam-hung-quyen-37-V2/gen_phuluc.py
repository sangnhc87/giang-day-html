import os
import re

tex_files = [os.path.join("chapters", f) for f in sorted(os.listdir("chapters")) if f.endswith(".tex") and f.startswith("ch")]

with open("phu-luc.tex", "w", encoding="utf-8") as out:
    out.write("\\chapter*{Phụ Lục: Bảng Phong Thần Thất Ngôn Tứ Tuyệt}\n")
    out.write("\\addcontentsline{toc}{chapter}{Phụ Lục: Bảng Phong Thần Tứ Tuyệt}\n")
    out.write("\\chapterintro{160 bài xúi quẩy, đâm thọc và xát muối vào nỗi đau học đường.}{Dành cho những tâm hồn đã nát tan vì điểm số mà vẫn còn sức để đọc thơ...}\n\n")
    out.write("\\begin{multicols}{2}\n")
    out.write("\\raggedright\n")
    
    for file in tex_files:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            chap_match = re.search(r"\\chapter\{([^}]+)\}", content)
            chap_title = chap_match.group(1) if chap_match else file.split("/")[-1]
            poems = re.findall(r"\\begin\{tutuyetbox\}\{[^:]*:\s*([^}]+)\}", content)
            
            if poems:
                out.write(f"\\textbf{{\\color{{chapterline}}{chap_title}}}\n")
                out.write("\\begin{itemize}[leftmargin=1.2em, itemsep=0.1em, label=\\textcolor{titlecolor}{\\tiny$\\blacksquare$}]\n")
                for p in poems:
                    out.write(f"  \\item {p.strip()}\n")
                out.write("\\end{itemize}\n\\vspace{0.8em}\n")
    out.write("\\end{multicols}\n")
