#!/bin/bash
set -e
cd "$(dirname "$0")"
echo "=========================================================="
echo " Biên dịch Quyển IV: Triết Lý Nhân Sinh & Đối Nhân Xử Thế"
echo "=========================================================="
echo "[1/3] Lần biên dịch đầu tiên..."
pdflatex -interaction=nonstopmode main.tex
echo "[2/3] Lần biên dịch thứ hai..."
pdflatex -interaction=nonstopmode main.tex
echo "[3/3] Lần biên dịch cuối cùng..."
pdflatex -interaction=nonstopmode main.tex
echo ""
echo "OK Thành công! File xuất ra: main.pdf"
rm -f *.aux *.log *.toc *.out *.lof *.lot *.fls *.fdb_latexmk
echo "Đã dọn dẹp file tạm."
