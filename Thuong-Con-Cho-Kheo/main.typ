// ============================================================
// THƯƠNG CON CHO KHÉO — sách dành cho ba mẹ
// Sinh chương: python3 gen.py
// Biên dịch:   typst compile main.typ
// ============================================================
#import "template.typ": *

// Điền tên người mua vào đây (hoặc truyền qua --input buyer="..."):
#let nguoimua = sys.inputs.at("buyer", default: "Quý Phụ Huynh")

#show: book.with(
  title: "Thương Con Cho Khéo",
  author: "Nguyễn Văn Sang",
  nguoimua: nguoimua,
)

#include "cover.typ"
#include "front.typ"
#include "chapters.typ"
#include "back.typ"
#include "catalog.typ"
