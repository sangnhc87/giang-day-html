#!/bin/bash
# compile.sh -- Quyển XIV: 100 Câu Hỏi Học Trò Hay Hỏi Về Chuyện Học
set -e
cd "$(dirname "$0")"
echo "=== Lần 1 / Pass 1 ==="
pdflatex -interaction=nonstopmode main.tex
echo "=== Lần 2 / Pass 2 ==="
pdflatex -interaction=nonstopmode main.tex
echo "=== Lần 3 / Pass 3 ==="
pdflatex -interaction=nonstopmode main.tex
echo "=== Hoàn tất: $(ls -lh main.pdf) ==="
