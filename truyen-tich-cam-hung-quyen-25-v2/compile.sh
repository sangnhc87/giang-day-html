#!/bin/bash
set -e

for i in 1 2 3; do
  echo "=== Pass $i ==="
  pdflatex -interaction=nonstopmode main.tex
done