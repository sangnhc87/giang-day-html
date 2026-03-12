#!/bin/bash
set -e
cd "$(dirname "$0")"
OUTPUT_NAME="100 Cap Doi Xung Triet Ly Nhan Sinh - Quyen 32 V2.pdf"
for i in 1 2 3; do
  echo "=== Pass $i ==="
  pdflatex -interaction=nonstopmode main.tex
done
cp -f main.pdf "$OUTPUT_NAME"
echo "=== Hoan tat: $(ls -lh main.pdf 2>/dev/null) ==="
echo "=== File in: $(ls -lh "$OUTPUT_NAME" 2>/dev/null) ==="
