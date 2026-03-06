#!/bin/bash
# Biên dịch Quyển VI - Trọn Vẹn Nhân Sinh
set -e
cd "$(dirname "$0")"
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
echo "Biên dịch Quyển VI hoàn tất: main.pdf"
