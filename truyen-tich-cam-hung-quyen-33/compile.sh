#!/bin/bash
# Quyển XXXIII: Da Giac Hoc Duong
set -e
cd "$(dirname "$0")"
OUTPUT_NAME="Quyển 33 - Đa Giác Học Đường - V4.pdf"
for i in 1 2 3; do
  echo "=== Pass $i ==="
  pdflatex -interaction=nonstopmode main.tex
done
cp -f main.pdf "$OUTPUT_NAME"
echo "=== Hoàn tất: $(ls -lh main.pdf 2>/dev/null) ==="
echo "=== File in: $(ls -lh "$OUTPUT_NAME" 2>/dev/null) ==="