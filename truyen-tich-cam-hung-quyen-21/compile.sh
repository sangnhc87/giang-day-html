#!/bin/bash
# Quyển XXI: 30 Câu Khiến Học Sinh Lười Phải Giật Mình
set -e
cd "$(dirname "$0")"
for i in 1 2 3; do echo "=== Pass $i ==="; pdflatex -interaction=nonstopmode main.tex; done
echo "=== Hoàn tất: $(ls -lh main.pdf 2>/dev/null) ==="
