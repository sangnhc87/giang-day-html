#!/bin/bash
# ============================================================
# Script biên dịch sách LaTeX "Điển tích & Chuyện kể"
# Yêu cầu: XeLaTeX + TeX Live hoặc MikTeX
# Chạy: bash compile.sh
# ============================================================

set -e
cd "$(dirname "$0")"

echo "=========================================="
echo " Biên dịch sách: Điển tích & Chuyện kể"
echo "=========================================="

# Lần 1: tạo .aux, .toc
echo "[1/3] Lần biên dịch đầu tiên..."
pdflatex -interaction=nonstopmode main.tex

# Lần 2: cập nhật tham chiếu chéo
echo "[2/3] Lần biên dịch thứ hai..."
pdflatex -interaction=nonstopmode main.tex

# Lần 3: hoàn thiện
echo "[3/3] Lần biên dịch cuối cùng..."
pdflatex -interaction=nonstopmode main.tex

echo ""
echo "OK Thanh cong! File xuat ra: main.pdf"
echo ""

# Dọn dẹp file phụ
rm -f *.aux *.log *.toc *.out *.lof *.lot *.fls *.fdb_latexmk
echo "🗑  Đã dọn dẹp file tạm."
