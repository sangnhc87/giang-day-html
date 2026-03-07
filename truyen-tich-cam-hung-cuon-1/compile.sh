#!/bin/bash
# Cuốn 1: Gộp quyển 18 + 19 + 20
set -e
cd "$(dirname "$0")"
for i in 1 2 3; do echo "=== Pass $i ==="; pdflatex -interaction=nonstopmode main.tex; done
echo "=== Hoàn tất: $(ls -lh main.pdf 2>/dev/null) ==="
