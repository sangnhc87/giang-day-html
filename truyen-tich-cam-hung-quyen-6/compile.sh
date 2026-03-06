#!/bin/bash
cd "$(dirname "$0")"
pdflatex -interaction=batchmode main.tex
pdflatex -interaction=batchmode main.tex
pdflatex -interaction=batchmode main.tex
echo "Done: $(ls -lh main.pdf 2>/dev/null)"
