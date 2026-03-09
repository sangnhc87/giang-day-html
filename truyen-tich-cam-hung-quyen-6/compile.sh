#!/bin/bash
<<<<<<< .merge_file_A3CgTd
# compile.sh -- Quyển VI: Vòng Quay Cuộc Đời
set -e
cd "$(dirname "$0")"
echo "=== Lần 1 / Pass 1 ==="
pdflatex -interaction=nonstopmode main.tex
echo "=== Lần 2 / Pass 2 ==="
pdflatex -interaction=nonstopmode main.tex
echo "=== Lần 3 / Pass 3 ==="
pdflatex -interaction=nonstopmode main.tex
echo "=== Hoàn tất: $(ls -lh main.pdf) ==="
=======
cd "$(dirname "$0")"
pdflatex -interaction=batchmode main.tex
pdflatex -interaction=batchmode main.tex
pdflatex -interaction=batchmode main.tex
echo "Done: $(ls -lh main.pdf 2>/dev/null)"
>>>>>>> .merge_file_3OCajm
