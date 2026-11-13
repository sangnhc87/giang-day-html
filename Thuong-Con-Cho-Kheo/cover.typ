// ============================================================
// BÌA — THƯƠNG CON CHO KHÉO
// ============================================================
#import "template.typ": *

#let night = rgb("0A1B2E")
#let cream = rgb("FFF8E7")
#let sun   = rgb("F5B841")
#let wine  = rgb("7C2D12")

#let bubble(who, t, fill, fg, tag-bg, side) = {
  let tail = polygon(fill: fill, (0pt, 0pt), (22pt, 0pt), (if side == left { 2pt } else { 20pt }, 17pt))
  align(side, block(width: 11.8cm)[
    #block(width: 100%, fill: fill, radius: 14pt, inset: (x: 17pt, y: 13pt), spacing: 0pt)[
      #set align(left)
      #set par(justify: false, leading: 0.6em)
      #box(fill: tag-bg, radius: 3pt, inset: (x: 7pt, y: 2.5pt),
        text(font: sans, size: 7.2pt, weight: "bold", fill: white, tracking: 1.2pt)[#who])
      #v(0.25em)
      #text(font: serif, size: 14.5pt, weight: "bold", fill: fg)[#t]
    ]
    #v(-1pt)
    #align(side, pad(left: if side == left { 30pt } else { 0pt }, right: if side == right { 30pt } else { 0pt }, tail))
  ])
}

#page(margin: 0pt, header: none, footer: none,
  fill: gradient.linear(night, navy, rgb("0E4A54"), angle: 65deg))[
  #place(top + right, dx: 5.5cm, dy: -5.5cm, circle(radius: 8.2cm, fill: white.transparentize(95%)))
  #place(top + right, dx: 3.2cm, dy: -3.2cm, circle(radius: 5cm, fill: sun.transparentize(84%)))
  #place(bottom + left, dx: -6cm, dy: -1.5cm, circle(radius: 7.5cm, fill: teal.transparentize(72%)))
  // Hai vòng tròn lồng nhau: vòng tay lớn ôm vòng tròn nhỏ
  #place(top + right, dx: -1.6cm, dy: 11.2cm, circle(radius: 3.6cm, stroke: 14pt + white.transparentize(93%)))
  #place(top + right, dx: -3.1cm, dy: 13.6cm, circle(radius: 1.5cm, fill: sun.transparentize(80%)))
  #place(top + left, rect(width: 9pt, height: 100%, fill: sun))

  #pad(left: 2.3cm, right: 1.9cm, top: 2.1cm)[
    #text(font: sans, size: 9pt, weight: "bold", fill: sun, tracking: 3pt)[TỦ SÁCH HỌC ĐƯỜNG]
    #h(1fr)
    #box(stroke: 0.9pt + white.transparentize(45%), radius: 20pt, inset: (x: 11pt, y: 4pt),
      text(font: sans, size: 8pt, weight: "bold", fill: white, tracking: 1.6pt)[SÁCH CHO BA MẸ · VIỆT – ANH])

    #v(1.5cm)
    #set par(justify: false, leading: 0.4em)
    #text(font: serif, size: 64pt, weight: "bold", fill: white)[Thương Con]
    #v(-1.25cm)
    #text(font: serif, size: 64pt, weight: "bold", style: "italic", fill: sun)[Cho Khéo]
    #v(-0.5cm)
    #box(width: 3.2cm, height: 4pt, fill: sun, radius: 2pt)
    #v(0.35cm)
    #set par(leading: 0.62em)
    #block(width: 13.8cm, text(font: serif, size: 14pt, style: "italic", fill: white.transparentize(10%))[
      76 tình huống con gặp phải, từ tờ điểm kém tới những ngày con không ổn. Ba mẹ nói gì, làm gì, để con vẫn còn muốn quay về kể. Song ngữ Việt – Anh.
    ])

    #v(1cm)
    #bubble("CON", "Con xin lỗi... Con sợ ba mẹ la nên con không dám nói.", white, ink, crimson, left)
    #v(0.2cm)
    #bubble("BA MẸ", "Con nói ra được là đúng rồi. Từ giây này con không còn một mình nữa.", sun, night, navy, right)
  ]

  #place(bottom + left, block(width: 100%, fill: cream, inset: (left: 2.3cm, right: 1.9cm, top: 0.75cm, bottom: 0.95cm))[
    #grid(columns: (1fr, auto), align: (left + horizon, right + horizon),
      [
        #text(font: sans, size: 7.6pt, weight: "bold", fill: slate, tracking: 2pt)[BIÊN SOẠN]
        #v(0.1cm)
        #text(font: serif, size: 21pt, weight: "bold", fill: night)[Thầy Nguyễn Văn Sang]
        #v(0.02cm)
        #text(font: sans, size: 8.6pt, fill: teal)[Giáo viên THPT Nguyễn Hữu Cảnh — TP. Hồ Chí Minh · 2026]
      ],
      grid(columns: 3, column-gutter: 14pt,
        ..(("6", "PHẦN"), ("18", "CHƯƠNG"), ("76", "TÌNH HUỐNG")).map(x => align(center)[
          #text(font: serif, size: 21pt, weight: "bold", fill: crimson)[#x.at(0)] \
          #text(font: sans, size: 6.6pt, weight: "bold", fill: slate, tracking: 1.3pt)[#x.at(1)]
        ])
      )
    )
  ])
]
