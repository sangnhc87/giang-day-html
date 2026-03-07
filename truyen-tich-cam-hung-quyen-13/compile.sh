#!/bin/bash
# compile.sh -- Quyển XIII: Những Câu Hỏi Học Trò Không Nói Thẳng
set -e
cd "$(dirname "$0")"
echo "=== Lần 1 / Pass 1 ==="
pdflatex -interaction=nonstopmode main.tex
echo "=== Lần 2 / Pass 2 ==="
pdflatex -interaction=nonstopmode main.tex
echo "=== Lần 3 / Pass 3 ==="
pdflatex -interaction=nonstopmode main.tex
echo "=== Hoàn tất: $(ls -lh main.pdf) ==="
