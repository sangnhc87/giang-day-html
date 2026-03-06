#!/bin/bash
# compile.sh -- Quyển V
set -e
cd "$(dirname "$0")"
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
echo "=== Done: $(ls -lh main.pdf) ==="
