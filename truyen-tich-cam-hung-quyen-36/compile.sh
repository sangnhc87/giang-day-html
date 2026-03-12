#!/bin/bash
# Quyển 36: Thơ tứ tuyệt thất ngôn song ngữ
set -e
cd "$(dirname "$0")"
for i in 1 2; do
	echo "=== pdfLaTeX pass $i ==="
	pdflatex -interaction=nonstopmode main.tex
done
echo "=== Hoàn tất: $(ls -lh main.pdf 2>/dev/null) ==="
