#!/bin/bash
# Quyển XXIII: 50 Câu Thầy Nói Cuối Năm (Rất Xúc Động)
set -e
cd "$(dirname "$0")"
for i in 1 2 3; do echo "=== Pass $i ==="; pdflatex -interaction=nonstopmode main.tex; done
echo "=== Hoàn tất: $(ls -lh main.pdf 2>/dev/null) ==="
