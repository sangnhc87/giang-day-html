#!/bin/bash
# Quyển XXXII: 100 Nghịch Lý Nhân Sinh
set -e
cd "$(dirname "$0")"
OUTPUT_NAME="100 Nghịch Lý Nhân Sinh - Một Cuốn Sách 3 Phần Được và Mất, Thắng và Thua, Đúng và Sai.pdf"
for i in 1 2 3; do
  echo "=== Pass $i ==="
  pdflatex -interaction=nonstopmode main.tex
done
cp -f main.pdf "$OUTPUT_NAME"
echo "=== Hoàn tất: $(ls -lh main.pdf 2>/dev/null) ==="
echo "=== File in: $(ls -lh "$OUTPUT_NAME" 2>/dev/null) ==="