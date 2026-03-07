#!/bin/bash
# compile.sh -- Quyển XI: Những Cái Bẫy Người Trẻ Tự Bước Vào
set -e
cd "$(dirname "$0")"
echo "=== Lần 1 / Pass 1 ==="
pdflatex -interaction=nonstopmode main.tex
echo "=== Lần 2 / Pass 2 ==="
pdflatex -interaction=nonstopmode main.tex
echo "=== Lần 3 / Pass 3 ==="
pdflatex -interaction=nonstopmode main.tex
echo "=== Hoàn tất: $(ls -lh main.pdf) ==="
