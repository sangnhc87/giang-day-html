// ============================================================
// BÌA SAU - TOÀN BỘ HỆ THỐNG TỦ SÁCH HỌC ĐƯỜNG SONG NGỮ (42 TẬP)
// TÁC GIẢ: THẦY NGUYỄN VĂN SANG
// ============================================================
#import "template.typ": *

#let cat-box(title, col, items) = block(
  width: 100%,
  breakable: false,
  fill: white,
  stroke: 0.75pt + col.lighten(30%),
  radius: 4pt,
  clip: true,
  spacing: 6pt,
)[
  #block(width: 100%, fill: col, inset: (x: 7pt, y: 4pt))[
    #text(font: sans, size: 7.4pt, weight: "bold", fill: white, tracking: 0.5pt)[#title]
  ]
  #block(width: 100%, inset: (x: 7pt, y: 5pt))[
    #set par(justify: false, leading: 0.45em, spacing: 0.28em)
    #set text(font: serif, size: 7.4pt, fill: ink)
    #for it in items [
      #let hl = it.at(2)
      #if hl {
        text(weight: "bold", fill: crimson)[#it.at(0) #it.at(1)]
      } else {
        text(weight: "bold", fill: navy)[#it.at(0)]
        [ ]
        it.at(1)
      }
      \
    ]
  ]
]

#page(margin: (x: 1.4cm, y: 1.3cm), header: none, footer: none, fill: white)[
  // Khung viền đôi ngoài bìa sau
  #place(top + left, dx: -0.5cm, dy: -0.45cm,
    rect(width: 100% + 1cm, height: 100% + 0.9cm, stroke: 1.8pt + gold, radius: 8pt))
  #place(top + left, dx: -0.32cm, dy: -0.27cm,
    rect(width: 100% + 0.64cm, height: 100% + 0.54cm, stroke: 0.7pt + navy, radius: 6pt))

  #align(center)[
    #text(font: sans, size: 8pt, fill: gold)[#sym.star.filled #h(6pt) #sym.star.filled #h(6pt) #sym.star.filled] \
    #v(2pt)
    #text(font: serif, size: 14.5pt, weight: "bold", fill: navy)[HỆ THỐNG TỦ SÁCH HỌC ĐƯỜNG SONG NGỮ] \
    #text(font: serif, size: 9.5pt, style: "italic", fill: teal)[Bộ Tác Phẩm Giáo Dục & Kỹ Năng Sư Phạm Của Thầy Nguyễn Văn Sang] \
    #v(4pt)
    #line(length: 68%, stroke: 0.8pt + gold)
  ]

  #v(6pt)

  #grid(
    columns: (1fr, 1fr),
    column-gutter: 10pt,
    [
      #cat-box("I. ĐIỂN TÍCH & NHÂN SINH (Q.I – VII)", teal, (
        ("Q.I:", "Điển Tích & Chuyện Cảm Hứng", false),
        ("Q.II:", "Đạo Làm Người & Ứng Xử", false),
        ("Q.III:", "Thiên Nhiên Quanh Ta", false),
        ("Q.IV:", "Triết Lý Nhân Sinh Sâu Sắc", false),
        ("Q.V:", "Hai Mặt Của Một Đồng Xu", false),
        ("Q.VI:", "Vòng Quay Cuộc Đời", false),
        ("Q.VII:", "Lời Dạy Bậc Hiền Nhân", false),
      ))
      #cat-box("II. TÂM LÝ TUỔI TRẺ (Q.VIII – XIV)", crimson, (
        ("Q.VIII:", "Thơ Nhưng Thật: Chuyện Học Trò", false),
        ("Q.IX:", "Ra Đời Không Có Bản Nháp", false),
        ("Q.X:", "Những Ảo Tưởng Của Tuổi Trẻ", false),
        ("Q.XI:", "Những Cái Bẫy Tự Bước Vào", false),
        ("Q.XII:", "Điều Thầy Giáo Nhìn Thấy", false),
        ("Q.XIII:", "Câu Hỏi Trò Không Nói Thẳng", false),
        ("Q.XIV:", "100 Câu Hỏi Hay Gặp Về Chuyện Học", false),
      ))
      #cat-box("III. LỜI THẦY TRÊN LỚP (Q.XV – XXI)", amber, (
        ("Q.XV:", "Điều Thầy Muốn Nói Với Học Sinh", false),
        ("Q.XVI:", "Những Bài Học Nhỏ Trong Lớp", false),
        ("Q.XVII:", "Những Điều Nên Hiểu Sớm", false),
        ("Q.XVIII:", "80 Lời Thầy Nói Trong Lớp Học", false),
        ("Q.XIX:", "100 Câu Nói Khiến Trò Im Lặng", false),
        ("Q.XX:", "80 Câu Hài Hước Nhưng Sâu Sắc", false),
        ("Q.XXI:", "60 Câu Khiến Trò Phải Giật Mình", false),
      ))
    ],
    [
      #cat-box("IV. BẢN LĨNH & NGHỊCH LÝ (Q.XXII – XXVIII)", navy, (
        ("Q.XXII:", "Đỉnh Cao Sư Phạm Khi Trò Nản", false),
        ("Q.XXIII:", "50 Lời Thầy Nói Cuối Năm Học", false),
        ("Q.XXIV:", "Bí Quyết Nhân Sinh & Trưởng Thành", false),
        ("Q.XXV:", "Lý Sự Cùn Của Học Sinh", false),
        ("Q.XXVI:", "Phụ Huynh Và Con Cái", false),
        ("Q.XXVII:", "Những Điều Ta Hiểu Khi Đã Muộn", false),
        ("Q.XXVIII:", "100 Nghịch Lý Nhân Sinh", false),
      ))
      #cat-box("V. CHUYÊN ĐỀ SƯ PHẠM ĐỘT PHÁ", rgb("0369A1"), (
        ("Q.XXXIII:", "Đa Giác Học Đường – Toàn Cảnh Tâm Lý", false),
        ("Q.XXXV:", "Cái Màn Hình Nuốt Mất Đời Sống", false),
        ("Q.XXXVI:", "Thơ Học Trò Vui (Đọc Xuôi Có Duyên)", false),
        ("Q.XXXVII:", "Nghệ Thuật Khịa Học Đường", false),
        ("Q.XXXVIII:", "Cứu Tiết Học Đang Trôi", false),
        ("Q.XXXIX:", "Đối Đáp Thầy Trò Thông Minh", false),
        ("Q.XL:", "Một Câu Hỏi Kéo Cả Lớp Nói", false),
        ("Q.XLI:", "5 Phút Khởi Động Cả Lớp", false),
        ("Q.XLII:", "Dạy Học Vui Trên Lớp (Bản Gộp Song Ngữ)", false),
      ))
    ]
  )

  #v(8pt)

  // Khung Thông Tin Liên Hệ & Thỉnh Sách
  #block(
    width: 100%,
    fill: rgb("F8FAFC"),
    stroke: 1pt + crimson,
    radius: 6pt,
    clip: true,
  )[
    #block(width: 100%, fill: crimson, inset: (x: 10pt, y: 4.5pt))[
      #align(center, text(font: sans, size: 7.8pt, weight: "bold", fill: white, tracking: 1pt)[
        THÔNG TIN LIÊN HỆ & ĐĂNG KÝ THỈNH SÁCH
      ])
    ]
    #block(width: 100%, inset: (x: 12pt, y: 8pt))[
      #align(center)[
        #set par(justify: false, leading: 0.48em)
        #text(font: serif, size: 10pt, weight: "bold", fill: navy)[TÁC GIẢ: THẦY NGUYỄN VĂN SANG] \
        #text(font: serif, size: 8.2pt, style: "italic", fill: teal)[Giáo viên THPT Nguyễn Hữu Cảnh — TP. Hồ Chí Minh] \
        #v(4pt)
        #text(font: serif, size: 8pt, fill: ink)[
          Tủ sách được biên soạn song ngữ Việt – Anh, thiết kế trang nhã theo chuẩn học đường hiện đại. \
          Phục vụ đắc lực cho công tác giảng dạy, đổi mới tiết học, làm quà tặng học sinh, phụ huynh và đồng nghiệp.
        ] \
        #v(4pt)
        #text(font: serif, size: 8.2pt, weight: "bold", fill: crimson)[
          Quý Thầy Cô & Bạn Đọc có nhu cầu đặt trọn bộ hoặc từng quyển theo chuyên đề, \
          xin vui lòng liên hệ trực tiếp Tác giả để nhận bản in hoặc file PDF cá nhân hóa theo tên riêng!
        ]
      ]
    ]
  ]

  #v(1fr)
  #align(center, text(font: sans, size: 7pt, fill: slate)[
    Bản quyền thuộc về Tác giả Thầy Nguyễn Văn Sang  ·  Tủ Sách Học Đường Song Ngữ
  ])
]
