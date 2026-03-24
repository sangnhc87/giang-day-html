#!/bin/bash
set -e

TARGET_FILE=${1:-main.tex}
PASSES=${PASSES:-2}

for ((i=1; i<=PASSES; i++)); do
  echo "=== Pass $i ==="
  pdflatex -interaction=nonstopmode "$TARGET_FILE"
done