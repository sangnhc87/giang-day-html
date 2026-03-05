#!/bin/bash
set -e
cd "$(dirname "$0")"
echo "=========================================="
echo " Bien dich Quyen IV: Triet Ly Nhan Sinh"
echo "=========================================="
echo "[1/3] Lan bien dich dau tien..."
pdflatex -interaction=nonstopmode main.tex
echo "[2/3] Lan bien dich thu hai..."
pdflatex -interaction=nonstopmode main.tex
echo "[3/3] Lan bien dich cuoi cung..."
pdflatex -interaction=nonstopmode main.tex
echo ""
echo "OK Thanh cong! File xuat ra: main.pdf"
rm -f *.aux *.log *.toc *.out *.lof *.lot *.fls *.fdb_latexmk
echo "Da don dep file tam."
