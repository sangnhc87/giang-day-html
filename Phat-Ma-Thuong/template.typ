// ============================================================
// TEMPLATE V3 (mở rộng từ PRO V2) - LÝ SỰ CÙN RẤT ĐỜI (ĐỘT PHÁ · NỀN TRẮNG TINH KHIẾT)
// Font: New Computer Modern (chuẩn LaTeX) + Avenir Next
// ============================================================
#let navy       = rgb("0F2942")
#let sapphire   = rgb("1D4ED8")
#let teal       = rgb("0F766E")
#let amber      = rgb("B45309")
#let crimson    = rgb("BE123C")
#let gold       = rgb("D97706")
#let ink        = rgb("0F172A")
#let slate      = rgb("475569")
#let paper      = rgb("FFFFFF")   // Nền trắng tinh khiết, không nền giấy vàng
#let softbg     = rgb("F8FAFC")
#let mist       = rgb("E2E8F0")
#let coral      = crimson

#let palette = (
  rgb("0F766E"), // Emerald Teal
  rgb("1D4ED8"), // Royal Sapphire
  rgb("B45309"), // Rich Amber
  rgb("BE123C"), // Deep Crimson
  rgb("4338CA"), // Indigo
  rgb("0369A1"), // Ocean Blue
)
#let serif = ("New Computer Modern", "Baskerville", "Times New Roman")
#let sans  = ("Avenir Next", "Helvetica Neue", "Arial")
#let accent = state("accent", palette.at(0))
#let buyer  = state("buyer", "Quý Độc Giả")

// ---------- TYPOGRAPHY HELPERS ----------
#let vi-en(vi, en, vsize: 1em, esize: 0.85em) = [
  #text(font: serif, size: vsize, fill: ink)[#vi]
  #parbreak()
  #v(-0.14em)
  #text(font: serif, size: esize, style: "italic", fill: rgb("334155"))[#en]
]

#let badge(t, bg, fg: white) = box(
  fill: bg,
  radius: 3pt,
  inset: (x: 6pt, y: 2pt),
  baseline: 1pt,
  text(font: sans, size: 7pt, weight: "bold", fill: fg, tracking: 0.9pt)[#upper(t)]
)

// ---------- KHUNG 1: CLASSROOM TALK (Header dải màu + đối thoại sắc nét) ----------
#let hs(vi, en) = block(
  breakable: false,
  spacing: 0.65em,
  width: 100%,
  inset: (x: 10pt, y: 6pt),
  fill: rgb("FFF5F5"),
  stroke: (left: 2.5pt + crimson),
  radius: (right: 5pt),
)[
  #badge("Học sinh", crimson)
  #v(-0.05em)
  #set par(justify: false, leading: 0.62em, spacing: 0.5em)
  #vi-en(vi, en, vsize: 0.98em, esize: 0.78em)
]

#let th(vi, en) = block(
  breakable: false,
  spacing: 0.65em,
  width: 100%,
  inset: (x: 10pt, y: 6pt),
  fill: rgb("F0F7FF"),
  stroke: (left: 2.5pt + sapphire),
  radius: (right: 5pt),
)[
  #badge("Thầy giáo", navy)
  #v(-0.05em)
  #set par(justify: false, leading: 0.62em, spacing: 0.5em)
  #vi-en(vi, en, vsize: 0.98em, esize: 0.78em)
]

#let scene(tag, body) = context {
  let c = accent.get()
  block(
    width: 100%,
    breakable: false,
    fill: white,
    stroke: 0.9pt + c.lighten(30%),
    radius: 7pt,
    clip: true,
    spacing: 0.85em,
  )[
    // Thanh tiêu đề đặc sắc nét kiểu tcolorbox hiện đại
    #block(
      width: 100%,
      fill: gradient.linear(navy, c, angle: 0deg),
      inset: (x: 14pt, y: 7pt),
    )[
      #grid(
        columns: (1fr, auto),
        align: (left + horizon, right + horizon),
        text(font: sans, size: 8.5pt, weight: "bold", fill: white, tracking: 1.1pt)[#upper(tag)],
        text(font: sans, size: 7.8pt, style: "italic", fill: white.transparentize(15%))[Gợi ý để thầy cô tham khảo],
      )
    ]
    #block(width: 100%, inset: (x: 12pt, top: 9pt, bottom: 8pt))[
      #body
    ]
  ]
}

// ---------- KHUNG 2: BÀI HỌC CUỐI GIỜ ----------
#let baihoc(vi, en) = block(
  width: 100%,
  breakable: false,
  fill: white,
  stroke: 0.9pt + navy.lighten(35%),
  radius: 7pt,
  clip: true,
  spacing: 0.8em,
)[
  #block(width: 100%, fill: navy, inset: (x: 14pt, y: 6pt))[
    #text(font: sans, size: 8.2pt, weight: "bold", fill: white, tracking: 1.1pt)[★  BÀI HỌC CUỐI GIỜ]
  ]
  #block(width: 100%, fill: softbg, inset: (x: 14pt, y: 9pt))[
    #set par(justify: false, leading: 0.62em)
    #text(font: serif, size: 1.04em, weight: "bold", fill: ink)[#vi]
    #parbreak()
    #v(-0.14em)
    #text(font: serif, size: 0.82em, style: "italic", fill: slate)[#en]
  ]
]

// ---------- KHUNG 3: EASY ENGLISH ----------
#let ghinhoanh(l1, l2) = block(
  width: 100%,
  breakable: false,
  fill: white,
  stroke: 1.1pt + teal,
  radius: 7pt,
  clip: true,
  spacing: 0.8em,
)[
  #block(width: 100%, fill: gradient.linear(teal, rgb("0D9488"), angle: 0deg), inset: (x: 14pt, y: 6.5pt))[
    #grid(
      columns: (1fr, auto),
      align: (left + horizon, right + horizon),
      text(font: sans, size: 8.4pt, weight: "bold", fill: white, tracking: 1.2pt)[EASY ENGLISH],
      text(font: sans, size: 7.5pt, style: "italic", fill: white.transparentize(15%))[Key Takeaways],
    )
  ]
  #block(width: 100%, fill: rgb("E6F7F5"), inset: (x: 14pt, y: 10pt))[
    #set par(justify: false, leading: 0.58em, spacing: 0.35em)
    #text(font: serif, size: 1.1em, weight: "bold", fill: navy)[#l1]
    #parbreak()
    #text(font: serif, size: 1em, style: "italic", weight: "medium", fill: teal.darken(30%))[#l2]
  ]
]

// ---------- KHUNG 4: GỢI Ý TỰ NGHĨ ----------
#let tuhocnhanh(items) = block(
  width: 100%,
  breakable: false,
  fill: white,
  stroke: 0.9pt + amber.lighten(35%),
  radius: 7pt,
  clip: true,
  spacing: 0.8em,
)[
  #block(width: 100%, fill: amber, inset: (x: 14pt, y: 6pt))[
    #text(font: sans, size: 8.2pt, weight: "bold", fill: white, tracking: 1.1pt)[GỢI Ý TỰ NGHĨ  ·  SELF-REFLECTION]
  ]
  #block(width: 100%, fill: rgb("FFFBEB"), inset: (x: 14pt, y: 9pt))[
    #for (i, it) in items.enumerate() [
      #grid(
        columns: (1.6em, 1fr),
        column-gutter: 6pt,
        align: top,
        box(
          width: 1.4em, height: 1.4em,
          radius: 50%,
          fill: amber,
          align(center + horizon, text(font: sans, size: 0.72em, weight: "bold", fill: white)[#str(i + 1)])
        ),
        {
          set par(justify: false, leading: 0.6em)
          vi-en(it.at(0), it.at(1), vsize: 0.95em, esize: 0.78em)
        }
      )
      #if i < items.len() - 1 { v(0.3em) }
    ]
  ]
]

// ---------- GÓC THẦY CÔ & PHỤ HUYNH ----------
#let gvbox(items) = block(
  width: 100%,
  breakable: false,
  fill: white,
  stroke: 0.9pt + navy.lighten(40%),
  radius: 7pt,
  clip: true,
  spacing: 1.1em,
)[
  #block(width: 100%, fill: rgb("1E293B"), inset: (x: 14pt, y: 6.5pt))[
    #text(font: sans, size: 8.2pt, weight: "bold", fill: white, tracking: 1.1pt)[GÓC THẦY CÔ & PHỤ HUYNH]
  ]
  #block(width: 100%, fill: softbg, inset: (x: 14pt, y: 10pt))[
    #for (i, it) in items.enumerate() [
      #grid(
        columns: (1.2em, 1fr),
        column-gutter: 6pt,
        align: top,
        text(font: sans, fill: amber, weight: "bold")[#sym.arrow.r],
        {
          set par(justify: false, leading: 0.6em)
          vi-en(it.at(0), it.at(1), vsize: 0.93em, esize: 0.78em)
        }
      )
      #if i < items.len() - 1 { v(0.3em) }
    ]
  ]
]

#let para(vi, en) = block(spacing: 1em)[
  #set par(justify: true, leading: 0.7em)
  #vi-en(vi, en, vsize: 1.02em, esize: 0.82em)
]

// ---------- TIÊU ĐỀ MỤC ----------
#let sec(title) = {
  pagebreak(weak: true)
  heading(level: 2)[#title]
}

// ---------- TRANG MỞ CHƯƠNG (Nền trắng tinh khiết + dải màu hiện đại) ----------
#let chapter-open(n, title, col-i, epi, lead, secs) = {
  let col = palette.at(calc.rem(col-i - 1, palette.len()))
  accent.update(col)
  page(margin: (x: 2.1cm, top: 2.1cm, bottom: 2cm), header: none, footer: none, fill: white)[
    #place(top + left, {
      show heading: none
      heading(level: 1, numbering: "1")[#title]
    })
    // Thanh màu kiến trúc dọc sát mép trái trang + số chương lớn mờ tinh tế
    #place(top + left, dx: -2.1cm, dy: -2.1cm, rect(width: 12pt, height: 29.7cm, fill: col))
    #place(top + right, dx: 0.4cm, dy: -0.3cm)[
      #text(font: sans, size: 110pt, weight: "bold", fill: col.lighten(88%))[
        #if n < 10 [0#str(n)] else [#str(n)]
      ]
    ]

    #v(0.5cm)
    #badge("CHƯƠNG " + if n < 10 { "0" + str(n) } else { str(n) }, col)
    #v(0.4cm)
    #set par(justify: false, leading: 0.48em)
    #block(width: 82%)[
      #text(font: serif, size: 27pt, weight: "bold", fill: ink)[#title]
    ]
    #v(0.3cm)
    #line(length: 45%, stroke: 2pt + col)
    #v(0.7cm)

    // Trích dẫn Epigraph
    #block(
      width: 100%,
      fill: softbg,
      stroke: (left: 3.5pt + col, rest: 0.6pt + mist),
      radius: (right: 6pt),
      inset: (x: 16pt, y: 12pt),
    )[
      #set par(justify: false, leading: 0.65em)
      #text(font: serif, size: 12.5pt, style: "italic", fill: ink)[“#epi.at(0)”]
      #parbreak()
      #v(-0.2em)
      #text(font: serif, size: 9.2pt, style: "italic", fill: slate)[#epi.at(1)]
    ]

    #v(0.7cm)
    #text(font: sans, size: 8pt, weight: "bold", fill: col, tracking: 1.4pt)[MỞ ĐẦU CHƯƠNG]
    #v(0.25em)
    #{
      set par(justify: true, leading: 0.7em)
      vi-en(lead.at(0), lead.at(1), vsize: 0.98em, esize: 0.8em)
    }

    #v(0.9cm)
    #block(
      width: 100%,
      fill: white,
      stroke: 0.9pt + mist,
      radius: 7pt,
      clip: true,
    )[
      #block(width: 100%, fill: col, inset: (x: 14pt, y: 6.5pt))[
        #text(font: sans, size: 8.2pt, weight: "bold", fill: white, tracking: 1.2pt)[NỘI DUNG TRONG CHƯƠNG]
      ]
      #block(width: 100%, inset: (x: 14pt, y: 10pt))[
        #for (i, s) in secs.enumerate() [
          #grid(
            columns: (2.8em, 1fr),
            column-gutter: 6pt,
            align: top,
            text(font: sans, size: 0.85em, weight: "bold", fill: col)[#str(n).#str(i + 1)],
            text(font: serif, size: 0.94em, fill: ink)[#s]
          )
          #if i < secs.len() - 1 {
            v(0.25em)
            line(length: 100%, stroke: 0.4pt + mist)
            v(0.25em)
          }
        ]
      ]
    ]
  ]
}

// ---------- TOÀN SÁCH ----------
#let book(title: "Lý Sự Cùn Rất Đời", author: "Nguyễn Văn Sang", nguoimua: "Quý Độc Giả", body) = {
  buyer.update(nguoimua)
  set document(title: title, author: author)
  set text(font: serif, size: 11.6pt, lang: "vi", fill: ink)
  set par(justify: true, leading: 0.68em, spacing: 0.8em)
  set page(
    paper: "a4",
    fill: white,
    margin: (x: 1.85cm, top: 2.2cm, bottom: 2.3cm),
    header-ascent: 28%,
    header: context {
      let p = here().page()
      let chs = query(heading.where(level: 1)).filter(h => h.location().page() <= p)
      let cur = if chs.len() > 0 { chs.last().body } else { [] }
      let c = accent.get()
      block(width: 100%)[
        #grid(
          columns: (auto, 1fr),
          align: (left + horizon, right + horizon),
          text(font: sans, size: 7.5pt, weight: "bold", tracking: 1.3pt, fill: c)[#upper[Phạt mà thương · Sổ tay thầy cô]],
          text(font: serif, size: 8.5pt, style: "italic", fill: slate)[#cur],
        )
        #v(3pt)
        #line(length: 100%, stroke: 0.7pt + c.lighten(45%))
      ]
    },
    footer: context {
      let c = accent.get()
      let b = buyer.get()
      block(width: 100%)[
        #line(length: 100%, stroke: 0.5pt + c.lighten(55%))
        #v(3pt)
        #grid(
          columns: (1fr, auto),
          align: (left + horizon, right + horizon),
          text(font: serif, size: 8pt, style: "italic", fill: slate)[
            Bản lưu hành cá nhân #h(4pt) • #h(4pt) Dành riêng cho: #text(weight: "bold", style: "normal", fill: navy)[#b]
          ],
          box(
            fill: c.lighten(90%),
            stroke: 0.6pt + c.lighten(50%),
            radius: 10pt,
            inset: (x: 9pt, y: 2.5pt),
            text(font: sans, size: 8.2pt, weight: "bold", fill: c)[#counter(page).display()]
          )
        )
      ]
    },
  )
  set heading(numbering: none)
  show heading.where(level: 1): it => {
    pagebreak(weak: true)
    v(0.6cm)
    block(width: 100%)[
      #set par(justify: false)
      #context {
        let c = accent.get()
        box(width: 1.8cm, height: 3.5pt, fill: c, radius: 2pt)
      }
      #v(0.3em)
      #text(font: serif, size: 25pt, weight: "bold", fill: navy)[#it.body]
      #v(0.2em)
      #line(length: 100%, stroke: 0.7pt + mist)
    ]
    v(0.5cm)
  }
  show heading.where(level: 2): it => context {
    let c = accent.get()
    set par(justify: false)
    block(sticky: true, above: 0.25em, below: 0.75em, width: 100%)[
      #grid(
        columns: (auto, 1fr),
        column-gutter: 10pt,
        align: horizon,
        if it.numbering != none {
          box(
            fill: c,
            radius: 5pt,
            inset: (x: 9pt, y: 4.5pt),
            text(font: sans, size: 10pt, weight: "bold", fill: white)[#counter(heading).display("1.1")]
          )
        },
        text(font: serif, size: 14.5pt, weight: "bold", fill: navy)[#it.body]
      )
      #v(-0.15em)
      #line(length: 100%, stroke: 0.8pt + c.lighten(50%))
    ]
  }
  show outline.entry.where(level: 1): it => {
    let p = it.prefix()
    let has-num = p != none and p != []
    v(0.55em, weak: true)
    link(it.element.location(), block(
      width: 100%,
      breakable: false,
      fill: if has-num { rgb("F1F5F9") } else { rgb("F8FAFC") },
      stroke: (left: 3pt + if has-num { teal } else { gold }),
      radius: (right: 4pt),
      inset: (x: 10pt, y: 5pt),
    )[
      #grid(
        columns: (auto, 1fr, auto),
        column-gutter: 8pt,
        align: (left + horizon, left + horizon, right + horizon),
        if has-num {
          box(
            fill: teal,
            radius: 3pt,
            inset: (x: 6pt, y: 2pt),
            text(font: sans, size: 7.5pt, weight: "bold", fill: white, tracking: 0.8pt)[CHƯƠNG #p]
          )
        } else {
          box(
            fill: gold.lighten(80%),
            radius: 3pt,
            inset: (x: 5pt, y: 2pt),
            text(font: sans, size: 7pt, weight: "bold", fill: amber)[★]
          )
        },
        text(font: sans, weight: "bold", fill: navy, size: 9.8pt)[#it.body()],
        box(
          fill: if has-num { navy } else { amber.lighten(85%) },
          radius: 3pt,
          inset: (x: 6pt, y: 2pt),
          text(font: sans, size: 8.2pt, weight: "bold", fill: if has-num { white } else { amber })[#it.page()]
        )
      )
    ])
  }
  show outline.entry.where(level: 2): it => {
    v(0.18em, weak: true)
    link(it.element.location(), pad(left: 14pt, right: 6pt)[
      #grid(
        columns: (auto, 1fr, auto),
        column-gutter: 6pt,
        align: (left + bottom, center + bottom, right + bottom),
        text(font: serif, size: 9pt, fill: rgb("334155"))[#it.body()],
        box(width: 1fr, clip: true, repeat(gap: 3pt)[#text(font: sans, size: 8pt, fill: rgb("CBD5E1"))[·]]),
        text(font: sans, size: 8.2pt, weight: "bold", fill: teal)[#it.page()]
      )
    ])
  }
  body
}

// ============================================================
// PHẦN MỞ RỘNG V3
// ============================================================
#let indigo = rgb("4338CA")
#let green  = rgb("15803D")

// ---------- KHUNG: HIỂU SÂU HƠN ----------
#let hieusau(vi, en) = block(
  width: 100%, breakable: false, fill: rgb("EEF2FF"),
  stroke: (left: 3pt + indigo), radius: (right: 6pt),
  inset: (x: 13pt, y: 9pt), spacing: 0.8em,
)[
  #text(font: sans, size: 8pt, weight: "bold", fill: indigo, tracking: 1.1pt)[HIỂU SÂU HƠN  ·  WHY IT WORKS]
  #v(0.15em)
  #set par(justify: true, leading: 0.62em)
  #vi-en(vi, en, vsize: 0.95em, esize: 0.78em)
]

// ---------- KHUNG: LÀM NGAY HÔM NAY ----------
#let lamngay(vi, en) = block(
  width: 100%, breakable: false, fill: white,
  stroke: 1.1pt + green, radius: 7pt, clip: true, spacing: 0.8em,
)[
  #block(width: 100%, fill: green, inset: (x: 14pt, y: 6pt))[
    #text(font: sans, size: 8.2pt, weight: "bold", fill: white, tracking: 1.1pt)[LÀM NGAY HÔM NAY  ·  TRY IT TODAY]
  ]
  #block(width: 100%, fill: rgb("F0FDF4"), inset: (x: 14pt, y: 9pt))[
    #grid(columns: (1.5em, 1fr), column-gutter: 6pt, align: top,
      box(width: 1.05em, height: 1.05em, stroke: 1.2pt + green, radius: 2pt, baseline: 1pt),
      {
        set par(justify: false, leading: 0.62em)
        vi-en(vi, en, vsize: 0.98em, esize: 0.78em)
      })
  ]
]

// ---------- KHUNG DANH SÁCH CHUNG (góc thầy cô / phụ huynh / hoạt động) ----------
#let listbox(title, color, bg, items, mark: sym.arrow.r) = block(
  width: 100%, breakable: false, fill: white,
  stroke: 0.9pt + color.lighten(40%), radius: 7pt, clip: true, spacing: 0.9em,
)[
  #block(width: 100%, fill: color, inset: (x: 14pt, y: 6.5pt))[
    #text(font: sans, size: 8.2pt, weight: "bold", fill: white, tracking: 1.1pt)[#title]
  ]
  #block(width: 100%, fill: bg, inset: (x: 14pt, y: 10pt))[
    #for (i, it) in items.enumerate() [
      #grid(columns: (1.2em, 1fr), column-gutter: 6pt, align: top,
        text(font: sans, fill: color, weight: "bold")[#mark],
        {
          set par(justify: false, leading: 0.6em)
          vi-en(it.at(0), it.at(1), vsize: 0.93em, esize: 0.78em)
        })
      #if i < items.len() - 1 { v(0.3em) }
    ]
  ]
]

// ---------- KHUNG: ĐỔI MỘT CÂU NÓI ----------
#let doicau(items) = block(
  width: 100%, breakable: false, fill: white,
  stroke: 0.9pt + mist, radius: 7pt, clip: true, spacing: 0.9em,
)[
  #block(width: 100%, fill: rgb("1E293B"), inset: (x: 14pt, y: 6.5pt))[
    #text(font: sans, size: 8.2pt, weight: "bold", fill: white, tracking: 1.1pt)[ĐỔI MỘT CÂU NÓI  ·  SAY THIS INSTEAD]
  ]
  #table(
    columns: (1fr, 1fr), stroke: 0.5pt + mist, inset: (x: 10pt, y: 7pt),
    fill: (x, y) => if x == 0 { rgb("FFF5F5") } else { rgb("F0FDF4") },
    text(font: sans, size: 7.6pt, weight: "bold", fill: crimson)[✗ NÊN TRÁNH],
    text(font: sans, size: 7.6pt, weight: "bold", fill: green)[✓ NÊN THỬ],
    ..items.map(it => (
      { set par(justify: false, leading: 0.58em); vi-en("“" + it.at(0) + "”", it.at(2), vsize: 0.9em, esize: 0.74em) },
      { set par(justify: false, leading: 0.58em); vi-en("“" + it.at(1) + "”", it.at(3), vsize: 0.9em, esize: 0.74em) },
    )).flatten()
  )
]

// ---------- TRANG NGĂN PHẦN ----------
#let part-colors = (rgb("0F766E"), rgb("1D4ED8"), rgb("B45309"), rgb("BE123C"), rgb("4338CA"))
#let part-open(n, title, en, desc, chapters, idx: 1) = {
  let col = part-colors.at(calc.rem(idx - 1, part-colors.len()))
  accent.update(col)
  page(margin: 0pt, header: none, footer: none, fill: rgb("FFFBF5"))[
    #place(top + left, { show heading: none; heading(level: 1, numbering: none, outlined: true, supplement: [Phan])[Phần #n: #title] })
    #place(top + left, rect(width: 100%, height: 7.5cm, fill: col.lighten(86%)))
    #place(top + left, rect(width: 10pt, height: 100%, fill: col))
    #place(top + right, dx: -1.6cm, dy: 0.6cm, text(font: serif, size: 200pt, weight: "bold", fill: col.lighten(62%))[#n])
    #pad(left: 2.4cm, right: 2cm, top: 3.4cm)[
      #box(fill: col, radius: 3pt, inset: (x: 10pt, y: 4pt),
        text(font: sans, size: 9.5pt, weight: "bold", fill: white, tracking: 3pt)[PHẦN #n])
      #v(0.6cm)
      #set par(justify: false, leading: 0.42em)
      #block(width: 13cm, text(font: serif, size: 40pt, weight: "bold", fill: navy)[#title])
      #v(0.1cm)
      #block(width: 14cm, text(font: serif, size: 15pt, style: "italic", fill: col.darken(15%))[#en])
    ]
    #pad(left: 2.4cm, right: 2cm, top: 9.2cm)[
      #box(width: 3cm, height: 4pt, fill: col, radius: 2pt)
      #v(0.5cm)
      #set par(leading: 0.72em, justify: false)
      #block(width: 14.2cm, text(font: serif, size: 13pt, fill: ink)[#desc])
    ]
    #place(bottom + left, block(width: 100%, inset: (left: 2.4cm, right: 2cm, bottom: 2cm))[
      #text(font: sans, size: 8pt, weight: "bold", fill: slate, tracking: 2.4pt)[TRONG PHẦN NÀY]
      #v(0.35cm)
      #for c in chapters [
        #block(width: 100%, spacing: 0pt, stroke: (top: 0.6pt + mist), inset: (y: 8.5pt))[
          #grid(columns: (1.5cm, 1fr), align: (left + horizon, left + horizon),
            text(font: serif, size: 22pt, weight: "bold", fill: col)[#if c.at(0) < 10 [0]#c.at(0)],
            { set par(justify: false, leading: 0.5em); text(font: serif, size: 13pt, fill: ink)[#c.at(1)] })
        ]
      ]
    ])
  ]
}

// V3: tình huống nối tiếp nhau (không ép sang trang mới) để sách gọn, đỡ trang trống.
// Muốn mỗi tình huống bắt đầu ở trang mới như bản PRO: đổi sec-newpage thành true.
#let sec-newpage = false
#let sec(title) = {
  if sec-newpage { pagebreak(weak: true) } else { v(1.6em, weak: true) }
  heading(level: 2)[#title]
}

// ============================================================
// PHẦN RIÊNG CHO SÁCH PHỤ HUYNH: THƯƠNG CON CHO KHÉO (một ngôn ngữ)
// ============================================================
#let rose  = rgb("BE185D")
#let warm  = rgb("FFF7ED")

// ---------- CHUYỆN XẢY RA ----------
#let boicanh(t) = block(
  width: 100%, breakable: false, spacing: 0.8em,
  inset: (left: 12pt, right: 4pt, y: 3pt), stroke: (left: 2.5pt + mist),
)[
  #text(font: sans, size: 7.6pt, weight: "bold", fill: slate, tracking: 1.2pt)[CHUYỆN XẢY RA]
  #v(-0.25em)
  #set par(justify: true, leading: 0.66em)
  #text(font: serif, size: 1em, style: "italic", fill: ink)[#t]
]

// ---------- CÂU DỄ BUỘT MIỆNG ----------
#let phanxa(noi, visao) = block(
  width: 100%, breakable: false, fill: rgb("FFF5F5"),
  stroke: 0.8pt + crimson.lighten(55%), radius: 7pt,
  inset: (x: 13pt, y: 9pt), spacing: 0.8em,
)[
  #let hanhvi = noi.starts-with("(")
  #text(font: sans, size: 7.8pt, weight: "bold", fill: crimson, tracking: 1.1pt)[#if hanhvi [PHẢN XẠ DỄ GẶP] else [CÂU DỄ BUỘT MIỆNG]]
  #v(-0.1em)
  #set par(justify: false, leading: 0.62em)
  #text(font: serif, size: 1em, weight: "bold", fill: ink)[#if hanhvi { noi } else { "“" + noi + "”" }]
  #parbreak()
  #v(-0.1em)
  #text(font: sans, size: 7.6pt, weight: "bold", fill: slate)[CON NGHE THÀNH: ]
  #text(font: serif, size: 0.94em, fill: rgb("334155"))[#visao]
]

// ---------- LƯỢT LỜI ----------
#let loi(who, t, bg, bar, tag) = block(
  breakable: false, spacing: 0.6em, width: 100%,
  inset: (x: 10pt, y: 6pt), fill: bg,
  stroke: (left: 2.5pt + bar), radius: (right: 5pt),
)[
  #badge(who, tag)
  #v(-0.05em)
  #set par(justify: false, leading: 0.62em, spacing: 0.5em)
  #text(font: serif, size: 0.99em, fill: ink)[#t]
]
#let con(t) = loi("Con", t, rgb("FFF5F5"), crimson, crimson)
#let me(t)  = loi("Mẹ", t, rgb("F0F7FF"), sapphire, navy)
#let ba(t)  = loi("Ba", t, rgb("F0FDFA"), teal, teal.darken(20%))

// ---------- HIỂU SÂU / CỐT LÕI / LÀM NGAY / CÂU NÓI / TỰ SOI ----------
#let hieusau1(t) = block(
  width: 100%, breakable: false, fill: rgb("EEF2FF"),
  stroke: (left: 3pt + indigo), radius: (right: 6pt),
  inset: (x: 13pt, y: 9pt), spacing: 0.8em,
)[
  #text(font: sans, size: 8pt, weight: "bold", fill: indigo, tracking: 1.1pt)[HIỂU SÂU HƠN  ·  CHUYỆN GÌ ĐANG DIỄN RA TRONG CON]
  #v(0.1em)
  #set par(justify: true, leading: 0.64em)
  #text(font: serif, size: 0.96em, fill: ink)[#t]
]

#let cotloi(t) = block(
  width: 100%, breakable: false, fill: white,
  stroke: 0.9pt + navy.lighten(35%), radius: 7pt, clip: true, spacing: 0.8em,
)[
  #block(width: 100%, fill: navy, inset: (x: 14pt, y: 6pt))[
    #text(font: sans, size: 8.2pt, weight: "bold", fill: white, tracking: 1.1pt)[★  ĐIỀU CỐT LÕI]
  ]
  #block(width: 100%, fill: softbg, inset: (x: 14pt, y: 9pt))[
    #set par(justify: false, leading: 0.62em)
    #text(font: serif, size: 1.05em, weight: "bold", fill: ink)[#t]
  ]
]

#let lamngay1(t) = block(
  width: 100%, breakable: false, fill: white,
  stroke: 1.1pt + green, radius: 7pt, clip: true, spacing: 0.8em,
)[
  #block(width: 100%, fill: green, inset: (x: 14pt, y: 6pt))[
    #text(font: sans, size: 8.2pt, weight: "bold", fill: white, tracking: 1.1pt)[BA MẸ LÀM NGAY TỐI NAY]
  ]
  #block(width: 100%, fill: rgb("F0FDF4"), inset: (x: 14pt, y: 9pt))[
    #grid(columns: (1.5em, 1fr), column-gutter: 6pt, align: top,
      box(width: 1.05em, height: 1.05em, stroke: 1.2pt + green, radius: 2pt, baseline: 1pt),
      { set par(justify: false, leading: 0.62em); text(font: serif, size: 0.98em, fill: ink)[#t] })
  ]
]

#let caunoi(t) = block(
  width: 100%, breakable: false, fill: warm,
  stroke: 1.1pt + amber.lighten(30%), radius: 7pt,
  inset: (x: 14pt, y: 10pt), spacing: 0.8em,
)[
  #text(font: sans, size: 7.8pt, weight: "bold", fill: amber, tracking: 1.2pt)[MỘT CÂU ĐỂ DÀNH NÓI VỚI CON]
  #v(0.05em)
  #set par(justify: false, leading: 0.6em)
  #text(font: serif, size: 1.12em, weight: "bold", style: "italic", fill: navy)[“#t”]
]

#let tusoi(items) = block(
  width: 100%, breakable: false, spacing: 0.8em,
  inset: (x: 13pt, y: 8pt), fill: white, stroke: 0.8pt + mist, radius: 7pt,
)[
  #text(font: sans, size: 7.8pt, weight: "bold", fill: slate, tracking: 1.1pt)[BA MẸ TỰ HỎI MÌNH]
  #v(0.1em)
  #for (i, it) in items.enumerate() [
    #grid(columns: (1.5em, 1fr), column-gutter: 5pt, align: top,
      box(width: 1.3em, height: 1.3em, radius: 50%, fill: slate,
        align(center + horizon, text(font: sans, size: 0.7em, weight: "bold", fill: white)[#str(i + 1)])),
      { set par(justify: false, leading: 0.6em); text(font: serif, size: 0.95em, fill: ink)[#it] })
    #if i < items.len() - 1 { v(0.2em) }
  ]
]

// ---------- KHUNG DANH SÁCH / ĐỔI CÂU (một ngôn ngữ) ----------
#let listbox1(title, color, bg, items, mark: sym.arrow.r) = block(
  width: 100%, breakable: false, fill: white,
  stroke: 0.9pt + color.lighten(40%), radius: 7pt, clip: true, spacing: 0.9em,
)[
  #block(width: 100%, fill: color, inset: (x: 14pt, y: 6.5pt))[
    #text(font: sans, size: 8.2pt, weight: "bold", fill: white, tracking: 1.1pt)[#title]
  ]
  #block(width: 100%, fill: bg, inset: (x: 14pt, y: 10pt))[
    #for (i, it) in items.enumerate() [
      #grid(columns: (1.2em, 1fr), column-gutter: 6pt, align: top,
        text(font: sans, fill: color, weight: "bold")[#mark],
        { set par(justify: false, leading: 0.62em); text(font: serif, size: 0.96em, fill: ink)[#it] })
      #if i < items.len() - 1 { v(0.3em) }
    ]
  ]
]

#let doicau1(items) = block(
  width: 100%, breakable: false, fill: white,
  stroke: 0.9pt + mist, radius: 7pt, clip: true, spacing: 0.9em,
)[
  #block(width: 100%, fill: rgb("1E293B"), inset: (x: 14pt, y: 6.5pt))[
    #text(font: sans, size: 8.2pt, weight: "bold", fill: white, tracking: 1.1pt)[ĐỔI MỘT CÂU NÓI]
  ]
  #table(
    columns: (1fr, 1fr), stroke: 0.5pt + mist, inset: (x: 10pt, y: 7pt),
    fill: (x, y) => if x == 0 { rgb("FFF5F5") } else { rgb("F0FDF4") },
    text(font: sans, size: 7.6pt, weight: "bold", fill: crimson)[✗ NÊN TRÁNH],
    text(font: sans, size: 7.6pt, weight: "bold", fill: green)[✓ NÊN THỬ],
    ..items.map(it => (
      { set par(justify: false, leading: 0.6em); text(font: serif, size: 0.94em)[“#it.at(0)”] },
      { set par(justify: false, leading: 0.6em); text(font: serif, size: 0.94em)[“#it.at(1)”] },
    )).flatten()
  )
]

#let para1(t) = block(spacing: 1em)[
  #set par(justify: true, leading: 0.72em)
  #text(font: serif, size: 1.02em, fill: ink)[#t]
]

// ---------- TRANG MỞ CHƯƠNG (một ngôn ngữ) ----------
#let chapter-open(n, title, col-i, epi, lead, secs) = {
  let col = palette.at(calc.rem(col-i - 1, palette.len()))
  accent.update(col)
  page(margin: (x: 2.1cm, top: 2.1cm, bottom: 2cm), header: none, footer: none, fill: white)[
    #place(top + left, { show heading: none; heading(level: 1, numbering: "1")[#title] })
    #place(top + left, dx: -2.1cm, dy: -2.1cm, rect(width: 12pt, height: 29.7cm, fill: col))
    #place(top + right, dx: 0.4cm, dy: -0.3cm)[
      #text(font: sans, size: 110pt, weight: "bold", fill: col.lighten(88%))[#if n < 10 [0#str(n)] else [#str(n)]]
    ]
    #v(0.5cm)
    #badge("CHƯƠNG " + if n < 10 { "0" + str(n) } else { str(n) }, col)
    #v(0.4cm)
    #set par(justify: false, leading: 0.48em)
    #block(width: 82%)[#text(font: serif, size: 27pt, weight: "bold", fill: ink)[#title]]
    #v(0.3cm)
    #line(length: 45%, stroke: 2pt + col)
    #v(0.7cm)
    #block(width: 100%, fill: softbg, stroke: (left: 3.5pt + col, rest: 0.6pt + mist),
      radius: (right: 6pt), inset: (x: 16pt, y: 13pt))[
      #set par(justify: false, leading: 0.65em)
      #text(font: serif, size: 13pt, style: "italic", fill: ink)[“#epi”]
    ]
    #v(0.7cm)
    #text(font: sans, size: 8pt, weight: "bold", fill: col, tracking: 1.4pt)[MỞ ĐẦU CHƯƠNG]
    #v(0.25em)
    #{ set par(justify: true, leading: 0.72em); text(font: serif, size: 1.02em, fill: ink)[#lead] }
    #v(0.9cm)
    #block(width: 100%, fill: white, stroke: 0.9pt + mist, radius: 7pt, clip: true)[
      #block(width: 100%, fill: col, inset: (x: 14pt, y: 6.5pt))[
        #text(font: sans, size: 8.2pt, weight: "bold", fill: white, tracking: 1.2pt)[CÁC TÌNH HUỐNG TRONG CHƯƠNG]
      ]
      #block(width: 100%, inset: (x: 14pt, y: 10pt))[
        #for (i, s) in secs.enumerate() [
          #grid(columns: (2.8em, 1fr), column-gutter: 6pt, align: top,
            text(font: sans, size: 0.85em, weight: "bold", fill: col)[#str(n).#str(i + 1)],
            text(font: serif, size: 0.96em, fill: ink)[#s])
          #if i < secs.len() - 1 { v(0.25em); line(length: 100%, stroke: 0.4pt + mist); v(0.25em) }
        ]
      ]
    ]
  ]
}

// ---------- KHUNG ĐỐI THOẠI (cho phép ngắt trang) ----------
#let scene(tag, body) = context {
  let c = accent.get()
  block(width: 100%, breakable: true, fill: white, stroke: 0.9pt + c.lighten(30%), radius: 7pt, spacing: 0.85em)[
    #block(width: 100%, fill: gradient.linear(navy, c, angle: 0deg), inset: (x: 14pt, y: 7pt), radius: (top: 6pt), sticky: true)[
      #grid(columns: (1fr, auto), align: (left + horizon, right + horizon),
        text(font: sans, size: 8.5pt, weight: "bold", fill: white, tracking: 1.1pt)[#upper(tag)],
        text(font: sans, size: 7.8pt, style: "italic", fill: white.transparentize(15%))[Gợi ý để thầy cô tham khảo])
    ]
    #block(width: 100%, inset: (x: 12pt, top: 2pt, bottom: 8pt))[#body]
  ]
}

// ============================================================
// LỚP SONG NGỮ: mọi khung nhận thêm en: (tùy chọn). Không có en thì in một ngôn ngữ.
// ============================================================
#let ensub(en, size: 0.8em, fill: rgb("334155")) = if en != none {
  parbreak()
  v(-0.2em)
  text(font: serif, size: size, style: "italic", weight: "regular", fill: fill)[#en]
}

#let boicanh(t, en: none) = block(
  width: 100%, breakable: false, spacing: 0.8em,
  inset: (left: 12pt, right: 4pt, y: 3pt), stroke: (left: 2.5pt + mist),
)[
  #text(font: sans, size: 7.6pt, weight: "bold", fill: slate, tracking: 1.2pt)[CHUYỆN XẢY RA  ·  WHAT HAPPENED]
  #v(-0.25em)
  #set par(justify: true, leading: 0.66em)
  #text(font: serif, size: 1em, fill: ink)[#t]
  #ensub(en)
]

#let phanxa(noi, visao, en: none) = block(
  width: 100%, breakable: false, fill: rgb("FFF5F5"),
  stroke: 0.8pt + crimson.lighten(55%), radius: 7pt,
  inset: (x: 13pt, y: 9pt), spacing: 0.8em,
)[
  #let hanhvi = noi.starts-with("(")
  #let qq(s) = if s.starts-with("(") { s } else { "“" + s + "”" }
  #text(font: sans, size: 7.8pt, weight: "bold", fill: crimson, tracking: 1.1pt)[#if hanhvi [PHẢN XẠ DỄ GẶP  ·  THE COMMON REFLEX] else [CÂU DỄ BUỘT MIỆNG  ·  WHAT SLIPS OUT]]
  #v(-0.1em)
  #set par(justify: false, leading: 0.62em)
  #text(font: serif, size: 1em, weight: "bold", fill: ink)[#qq(noi)]
  #if en != none { ensub(qq(en.at(0))) }
  #parbreak()
  #v(0.1em)
  #text(font: sans, size: 7.6pt, weight: "bold", fill: slate)[CON NGHE THÀNH · WHAT THE CHILD HEARS: ]
  #text(font: serif, size: 0.94em, fill: rgb("334155"))[#visao]
  #if en != none { ensub(en.at(1), size: 0.78em, fill: slate) }
]

#let loi(who, t, bg, bar, tag, en: none) = block(
  breakable: false, spacing: 0.6em, width: 100%,
  inset: (x: 10pt, y: 6pt), fill: bg,
  stroke: (left: 2.5pt + bar), radius: (right: 5pt),
)[
  #badge(who, tag)
  #v(-0.05em)
  #set par(justify: false, leading: 0.62em, spacing: 0.5em)
  #text(font: serif, size: 0.99em, fill: ink)[#t]
  #ensub(en, size: 0.78em)
]
#let con(t, en: none) = loi(if en == none { "Con" } else { "Con · Child" }, t, rgb("FFF5F5"), crimson, crimson, en: en)
#let me(t, en: none)  = loi(if en == none { "Mẹ" } else { "Mẹ · Mum" }, t, rgb("F0F7FF"), sapphire, navy, en: en)
#let ba(t, en: none)  = loi(if en == none { "Ba" } else { "Ba · Dad" }, t, rgb("F0FDFA"), teal, teal.darken(20%), en: en)

#let hieusau1(t, en: none) = block(
  width: 100%, breakable: false, fill: rgb("EEF2FF"),
  stroke: (left: 3pt + indigo), radius: (right: 6pt),
  inset: (x: 13pt, y: 9pt), spacing: 0.8em,
)[
  #text(font: sans, size: 8pt, weight: "bold", fill: indigo, tracking: 1.1pt)[HIỂU SÂU HƠN  ·  WHAT IS GOING ON INSIDE YOUR CHILD]
  #v(0.1em)
  #set par(justify: true, leading: 0.64em)
  #text(font: serif, size: 0.96em, fill: ink)[#t]
  #ensub(en, size: 0.78em)
]

#let cotloi(t, en: none) = block(
  width: 100%, breakable: false, fill: white,
  stroke: 0.9pt + navy.lighten(35%), radius: 7pt, clip: true, spacing: 0.8em,
)[
  #block(width: 100%, fill: navy, inset: (x: 14pt, y: 6pt))[
    #text(font: sans, size: 8.2pt, weight: "bold", fill: white, tracking: 1.1pt)[★  ĐIỀU CỐT LÕI  ·  THE HEART OF IT]
  ]
  #block(width: 100%, fill: softbg, inset: (x: 14pt, y: 9pt))[
    #set par(justify: false, leading: 0.62em)
    #text(font: serif, size: 1.05em, weight: "bold", fill: ink)[#t]
    #ensub(en, size: 0.82em, fill: slate)
  ]
]

#let lamngay1(t, en: none) = block(
  width: 100%, breakable: false, fill: white,
  stroke: 1.1pt + green, radius: 7pt, clip: true, spacing: 0.8em,
)[
  #block(width: 100%, fill: green, inset: (x: 14pt, y: 6pt))[
    #text(font: sans, size: 8.2pt, weight: "bold", fill: white, tracking: 1.1pt)[BA MẸ LÀM NGAY TỐI NAY  ·  TRY IT TONIGHT]
  ]
  #block(width: 100%, fill: rgb("F0FDF4"), inset: (x: 14pt, y: 9pt))[
    #grid(columns: (1.5em, 1fr), column-gutter: 6pt, align: top,
      box(width: 1.05em, height: 1.05em, stroke: 1.2pt + green, radius: 2pt, baseline: 1pt),
      { set par(justify: false, leading: 0.62em); text(font: serif, size: 0.98em, fill: ink)[#t]; ensub(en, size: 0.78em) })
  ]
]

#let caunoi(t, en: none) = block(
  width: 100%, breakable: false, fill: warm,
  stroke: 1.1pt + amber.lighten(30%), radius: 7pt,
  inset: (x: 14pt, y: 10pt), spacing: 0.8em,
)[
  #text(font: sans, size: 7.8pt, weight: "bold", fill: amber, tracking: 1.2pt)[MỘT CÂU ĐỂ DÀNH NÓI VỚI CON  ·  A LINE TO KEEP READY]
  #v(0.05em)
  #set par(justify: false, leading: 0.6em)
  #text(font: serif, size: 1.12em, weight: "bold", style: "italic", fill: navy)[“#t”]
  #if en != none { ensub("“" + en + "”", size: 0.92em, fill: teal.darken(30%)) }
]

#let tusoi(items, en: none) = block(
  width: 100%, breakable: false, spacing: 0.8em,
  inset: (x: 13pt, y: 8pt), fill: white, stroke: 0.8pt + mist, radius: 7pt,
)[
  #text(font: sans, size: 7.8pt, weight: "bold", fill: slate, tracking: 1.1pt)[BA MẸ TỰ HỎI MÌNH  ·  ASK YOURSELF]
  #v(0.1em)
  #for (i, it) in items.enumerate() [
    #grid(columns: (1.5em, 1fr), column-gutter: 5pt, align: top,
      box(width: 1.3em, height: 1.3em, radius: 50%, fill: slate,
        align(center + horizon, text(font: sans, size: 0.7em, weight: "bold", fill: white)[#str(i + 1)])),
      { set par(justify: false, leading: 0.6em); text(font: serif, size: 0.95em, fill: ink)[#it]
        if en != none { ensub(en.at(i), size: 0.78em) } })
    #if i < items.len() - 1 { v(0.2em) }
  ]
]

#let listbox1(title, color, bg, items, mark: sym.arrow.r, en: none) = block(
  width: 100%, breakable: false, fill: white,
  stroke: 0.9pt + color.lighten(40%), radius: 7pt, clip: true, spacing: 0.9em,
)[
  #block(width: 100%, fill: color, inset: (x: 14pt, y: 6.5pt))[
    #text(font: sans, size: 8.2pt, weight: "bold", fill: white, tracking: 1.1pt)[#title]
  ]
  #block(width: 100%, fill: bg, inset: (x: 14pt, y: 10pt))[
    #for (i, it) in items.enumerate() [
      #grid(columns: (1.2em, 1fr), column-gutter: 6pt, align: top,
        text(font: sans, fill: color, weight: "bold")[#mark],
        { set par(justify: false, leading: 0.62em); text(font: serif, size: 0.96em, fill: ink)[#it]
          if en != none { ensub(en.at(i), size: 0.78em) } })
      #if i < items.len() - 1 { v(0.3em) }
    ]
  ]
]

// items: (tránh, thử) hoặc (tránh, thử, en tránh, en thử)
#let doicau1(items) = block(
  width: 100%, breakable: false, fill: white,
  stroke: 0.9pt + mist, radius: 7pt, clip: true, spacing: 0.9em,
)[
  #block(width: 100%, fill: rgb("1E293B"), inset: (x: 14pt, y: 6.5pt))[
    #text(font: sans, size: 8.2pt, weight: "bold", fill: white, tracking: 1.1pt)[ĐỔI MỘT CÂU NÓI  ·  SAY THIS INSTEAD]
  ]
  #table(
    columns: (1fr, 1fr), stroke: 0.5pt + mist, inset: (x: 10pt, y: 7pt),
    fill: (x, y) => if x == 0 { rgb("FFF5F5") } else { rgb("F0FDF4") },
    text(font: sans, size: 7.6pt, weight: "bold", fill: crimson)[✗ NÊN TRÁNH · AVOID],
    text(font: sans, size: 7.6pt, weight: "bold", fill: green)[✓ NÊN THỬ · TRY],
    ..items.map(it => (
      { set par(justify: false, leading: 0.6em); text(font: serif, size: 0.94em)[“#it.at(0)”]
        if it.len() > 2 { ensub("“" + it.at(2) + "”", size: 0.76em) } },
      { set par(justify: false, leading: 0.6em); text(font: serif, size: 0.94em)[“#it.at(1)”]
        if it.len() > 2 { ensub("“" + it.at(3) + "”", size: 0.76em) } },
    )).flatten()
  )
]

#let para1(t, en: none) = block(spacing: 1em)[
  #set par(justify: true, leading: 0.72em)
  #text(font: serif, size: 1.02em, fill: ink)[#t]
  #ensub(en, size: 0.82em)
]

#let sec(title, en: none) = {
  v(1.6em, weak: true)
  heading(level: 2)[#title]
  if en != none {
    block(above: 0.2em, below: 0.8em, sticky: true, text(font: serif, size: 10.5pt, style: "italic", fill: slate)[#en])
  }
}

// en: (title, epi, lead, secs)
#let chapter-open(n, title, col-i, epi, lead, secs, en: none) = {
  let col = palette.at(calc.rem(col-i - 1, palette.len()))
  accent.update(col)
  page(margin: (x: 2.1cm, top: 2.1cm, bottom: 2cm), header: none, footer: none, fill: white)[
    #place(top + left, { show heading: none; heading(level: 1, numbering: "1")[#title] })
    #place(top + left, dx: -2.1cm, dy: -2.1cm, rect(width: 12pt, height: 29.7cm, fill: col))
    #place(top + right, dx: 0.4cm, dy: -0.3cm)[
      #text(font: sans, size: 110pt, weight: "bold", fill: col.lighten(88%))[#if n < 10 [0#str(n)] else [#str(n)]]
    ]
    #v(0.5cm)
    #badge("CHƯƠNG " + if n < 10 { "0" + str(n) } else { str(n) }, col)
    #v(0.4cm)
    #set par(justify: false, leading: 0.48em)
    #block(width: 72%)[#text(font: serif, size: 26pt, weight: "bold", fill: ink)[#title]]
    #if en != none { v(-0.1cm); block(width: 82%, text(font: serif, size: 14pt, style: "italic", fill: col.darken(10%))[#en.at(0)]) }
    #v(0.3cm)
    #line(length: 45%, stroke: 2pt + col)
    #v(0.6cm)
    #block(width: 100%, fill: softbg, stroke: (left: 3.5pt + col, rest: 0.6pt + mist),
      radius: (right: 6pt), inset: (x: 16pt, y: 13pt))[
      #set par(justify: false, leading: 0.65em)
      #text(font: serif, size: 13pt, style: "italic", fill: ink)[“#epi”]
      #if en != none { ensub("“" + en.at(1) + "”", size: 9.4pt, fill: slate) }
    ]
    #v(0.6cm)
    #text(font: sans, size: 8pt, weight: "bold", fill: col, tracking: 1.4pt)[MỞ ĐẦU CHƯƠNG]
    #v(0.25em)
    #{ set par(justify: true, leading: 0.7em); text(font: serif, size: 1em, fill: ink)[#lead]
       if en != none { ensub(en.at(2), size: 0.8em) } }
    #v(0.7cm)
    #block(width: 100%, fill: white, stroke: 0.9pt + mist, radius: 7pt, clip: true)[
      #block(width: 100%, fill: col, inset: (x: 14pt, y: 6.5pt))[
        #text(font: sans, size: 8.2pt, weight: "bold", fill: white, tracking: 1.2pt)[CÁC TÌNH HUỐNG TRONG CHƯƠNG  ·  IN THIS CHAPTER]
      ]
      #block(width: 100%, inset: (x: 14pt, y: 9pt))[
        #for (i, s) in secs.enumerate() [
          #grid(columns: (2.8em, 1fr), column-gutter: 6pt, align: top,
            text(font: sans, size: 0.85em, weight: "bold", fill: col)[#str(n).#str(i + 1)],
            { set par(leading: 0.55em); text(font: serif, size: 0.96em, fill: ink)[#s]
              if en != none { ensub(en.at(3).at(i), size: 0.78em, fill: slate) } })
          #if i < secs.len() - 1 { v(0.2em); line(length: 100%, stroke: 0.4pt + mist); v(0.2em) }
        ]
      ]
    ]
  ]
}

// ============================================================
// KHUNG RIÊNG CHO SÁCH THẦY CÔ: PHẠT MÀ THƯƠNG
// ============================================================
#let tinhhuong(n, ten, loi, en: none) = block(
  width: 100%, breakable: false, spacing: 0.8em, fill: softbg,
  stroke: (left: 3pt + crimson), radius: (right: 6pt), inset: (x: 12pt, y: 8pt),
)[
  #text(font: sans, size: 7.6pt, weight: "bold", fill: crimson, tracking: 1.2pt)[TÌNH HUỐNG #n#if en != none [  ·  SITUATION #n]]
  #v(0.1em)
  #set par(justify: true, leading: 0.64em)
  #text(font: serif, size: 0.97em, fill: ink)[#loi]
  #ensub(en)
]

#let chieu(ten, cach, en: none) = block(
  width: 100%, breakable: false, fill: white,
  stroke: 1.1pt + amber, radius: 7pt, clip: true, spacing: 0.8em,
)[
  #block(width: 100%, fill: amber, inset: (x: 14pt, y: 6pt))[
    #text(font: sans, size: 8.2pt, weight: "bold", fill: white, tracking: 1.1pt)[CHIÊU PHẠT  ·  #upper(ten)#if en != none [  ·  #upper(en.at(0))]]
  ]
  #block(width: 100%, fill: warm, inset: (x: 14pt, y: 9pt))[
    #set par(justify: false, leading: 0.64em)
    #text(font: serif, size: 1em, fill: ink)[#cach]
    #if en != none { ensub(en.at(1)) }
  ]
]

#let thay(t, en: none) = loi("Thầy", t, rgb("F0F7FF"), sapphire, navy, en: en)
#let tro(t, en: none)  = loi("Trò", t, rgb("FFF5F5"), crimson, crimson, en: en)

#let visao(t, en: none) = block(
  width: 100%, breakable: false, fill: rgb("EEF2FF"),
  stroke: (left: 3pt + indigo), radius: (right: 6pt), inset: (x: 13pt, y: 8pt), spacing: 0.8em,
)[
  #text(font: sans, size: 8pt, weight: "bold", fill: indigo, tracking: 1.1pt)[VÌ SAO CHIÊU NÀY CÓ TÁC DỤNG#if en != none [  ·  WHY IT WORKS]]
  #v(0.1em)
  #set par(justify: true, leading: 0.62em)
  #text(font: serif, size: 0.95em, fill: ink)[#t]
  #ensub(en)
]

#let ranhgioi(t, en: none) = block(
  width: 100%, breakable: false, fill: rgb("FFF5F5"),
  stroke: 0.8pt + crimson.lighten(55%), radius: 7pt, inset: (x: 13pt, y: 8pt), spacing: 0.8em,
)[
  #text(font: sans, size: 7.8pt, weight: "bold", fill: crimson, tracking: 1.1pt)[RANH GIỚI: DỪNG Ở ĐÂU#if en != none [  ·  WHERE TO STOP]]
  #v(0.05em)
  #set par(justify: false, leading: 0.62em)
  #text(font: serif, size: 0.94em, fill: ink)[#t]
  #ensub(en)
]

#let bientau(t, en: none) = block(
  width: 100%, breakable: false, fill: rgb("F0FDF4"),
  stroke: (left: 3pt + green), radius: (right: 6pt), inset: (x: 13pt, y: 8pt), spacing: 0.8em,
)[
  #text(font: sans, size: 8pt, weight: "bold", fill: green, tracking: 1.1pt)[BIẾN TẤU THÊM#if en != none [  ·  VARIATIONS]]
  #v(0.05em)
  #set par(justify: false, leading: 0.62em)
  #text(font: serif, size: 0.94em, fill: ink)[#t]
  #ensub(en)
]

#let caunoi(t, en: none) = block(
  width: 100%, breakable: false, fill: warm,
  stroke: 1.1pt + amber.lighten(30%), radius: 7pt, inset: (x: 14pt, y: 10pt), spacing: 0.8em,
)[
  #text(font: sans, size: 7.8pt, weight: "bold", fill: amber, tracking: 1.2pt)[MỘT CÂU THẦY CÔ CÓ THỂ NÓI#if en != none [  ·  A LINE TO KEEP READY]]
  #v(0.05em)
  #set par(justify: false, leading: 0.6em)
  #text(font: serif, size: 1.1em, weight: "bold", style: "italic", fill: navy)[“#t”]
  #if en != none { ensub("“" + en + "”", size: 0.92em, fill: teal.darken(30%)) }
]
