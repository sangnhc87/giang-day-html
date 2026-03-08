#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sinh lại trang bìa (cover.tex) cho Q3–Q24 theo phong cách đồng bộ với Quyển I:
- Nền sáng (truyenred!5)
- Khung viền đôi truyengold + hoa văn góc
- Vòng tròn trang trí
- tcolorbox nhãn QUYỂN X
- Tiêu đề chính (2-3 dòng, fontsize lớn)
- Tiêu đề phụ italic
- Quote riêng từng quyển
- afterpage{\nopagecolor}

Màu sắc dùng truyenred/truyengold/truyenblue của từng quyển (đã định nghĩa trong main.tex).
Các quyển dùng màu riêng (Q11+) — dùng màu thứ nhất làm "main accent", thứ hai làm "gold", thứ ba làm "blue".
"""

import os

BASE = "/Users/admin/Giang-Day-html"

# Dữ liệu từng quyển
# key: số quyển
# main_color: màu chính (cho viền, tcolorbox, tiêu đề \bfseries)
# accent_color: màu accent (cho tiêu đề dòng 2, đường kẻ)
# blue_color: màu trang trí vòng tròn
# volume_label: nhãn quyển
# title_lines: list 2-3 dòng tiêu đề chính
# subtitle: tiêu đề phụ italic
# quote: câu trích dẫn (không có ``...'')
# tagline: dòng giới thiệu ngắn dưới đường kẻ

COVERS = {
    3: {
        "main_color": "truyenred",
        "accent_color": "truyengold",
        "blue_color": "truyenblue",
        "header": "Muôn Loài Dạy Ta",
        "label": "QUYỂN III",
        "title_lines": ["Điển Tích \\&", "Chuyện Kể"],
        "subtitle": "Bài Học Từ Thiên Nhiên \\& Muôn Loài",
        "quote": "Lắng nghe thiên nhiên, ta học được muôn điều.\\\\\n   Nhện chăng tơ, kiến tha hồ, nước chảy đá mòn~--- tất cả đều dạy.",
        "author": True,
    },
    4: {
        "main_color": "truyenred",
        "accent_color": "truyengold",
        "blue_color": "truyenblue",
        "header": "Chuyện Xưa, Lẽ Sống Nay",
        "label": "QUYỂN IV",
        "title_lines": ["Điển Tích \\&", "Chuyện Kể"],
        "subtitle": "Triết Lý Nhân Sinh \\& Đối Nhân Xử Thế",
        "quote": "Từ những câu chuyện xưa, ta tìm thấy chính mình.\\\\\n   Người trí không chỉ học từ kinh nghiệm bản thân, mà còn học từ lịch sử.",
        "author": True,
    },
    5: {
        "main_color": "truyenred",
        "accent_color": "truyengold",
        "blue_color": "truyenblue",
        "header": "Nhìn Hai Mặt Cuộc Đời",
        "label": "QUYỂN V",
        "title_lines": ["Hai Mặt Của", "Một Đồng Xu"],
        "subtitle": "Tư Duy Biện Chứng~--- Âm Dương \\& Cân Bằng",
        "quote": "Kẻ trí nhìn thấy cả hai mặt của mỗi đồng xu.\\\\\n   Sự thật thường nằm ở giữa, không phải ở một phía.",
        "author": True,
    },
    6: {
        "main_color": "truyenred",
        "accent_color": "truyengold",
        "blue_color": "truyenblue",
        "header": "Đi Qua Những Vòng Quay",
        "label": "QUYỂN VI",
        "title_lines": ["Vòng Quay", "Cuộc Đời"],
        "subtitle": "Nhân Quả, Bản Sắc \\& Người Thầy Vô Hình",
        "quote": "Cuộc đời có quy luật riêng~--- kẻ trí học nó sớm.\\\\\n   Biết buông bỏ và giữ bản sắc là nền tảng của người trưởng thành.",
        "author": True,
    },
    7: {
        "main_color": "truyenred",
        "accent_color": "truyengold",
        "blue_color": "truyenblue",
        "header": "Nghe Người Xưa Dặn",
        "label": "QUYỂN VII",
        "title_lines": ["Lời Dạy Của", "Bậc Hiền Nhân"],
        "subtitle": "Triết Lý \\& Lời Dạy Từ Đông Sang Tây, Từ Xưa Đến Nay",
        "quote": "Lời dạy hay nhất là lời em tự đưa vào thực hành.\\\\\n   Học khôn từ người trước là con đường ngắn nhất đến sự trưởng thành.",
        "author": True,
    },
    8: {
        "main_color": "truyenred",
        "accent_color": "truyengold",
        "blue_color": "truyenblue",
        "header": "Sự Thật Tuổi Học Trò",
        "label": "QUYỂN VIII",
        "title_lines": ["Thô Nhưng", "Thật"],
        "subtitle": "Chuyện Học Sinh~--- Thẳng, Thật, Không Tô Hồng",
        "quote": "Thất bại không có nghĩa là em hỏng.\\\\\n   Nó chỉ có nghĩa là em phải học cách đứng dậy cho đúng.",
        "author": True,
    },
    9: {
        "main_color": "truyenred",
        "accent_color": "truyengold",
        "blue_color": "truyenblue",
        "header": "Bước Vào Đời Thật",
        "label": "QUYỂN IX",
        "title_lines": ["Ra Đời Không", "Có Bản Nháp"],
        "subtitle": "Tập 1: Đi Vào Đời Không Còn Bản Nháp",
        "quote": "Không ai phát cho em một bản nháp trước khi sống.\\\\\n   Vì vậy, tỉnh táo cũng là một kiểu tự cứu mình.",
        "author": True,
    },
    10: {
        "main_color": "truyenred",
        "accent_color": "truyengold",
        "blue_color": "truyenblue",
        "header": "Vỡ Ảo Tưởng Để Lớn",
        "label": "QUYỂN X",
        "title_lines": ["Những Ảo Tưởng", "Của Tuổi Trẻ"],
        "subtitle": "Tập 2: Bóc Những Ngộ Nhận Rất Đau Nhưng Rất Thật",
        "quote": "Tuổi trẻ đau không chỉ vì đời khó.\\\\\n   Nhiều khi còn vì mình tin nhầm vào những điều quá đẹp.",
        "author": True,
    },
    # Q11+ dùng màu riêng (không dùng truyenred/truyengold/truyenblue)
    11: {
        "main_color": "trapgreen",
        "accent_color": "trapgold",
        "blue_color": "trapbrown",
        "header": "Nhận Diện Những Cái Bẫy",
        "label": "QUYỂN XI",
        "title_lines": ["Những Cái Bẫy", "Người Trẻ", "Tự Bước Vào"],
        "subtitle": "Tỉnh Ra Trước Khi Trả Giá Quá Đắt",
        "quote": "Nhiều cái bẫy của tuổi trẻ không mang hình thù đáng sợ.\\\\\n   Nó mặc áo tử tế, cơ hội, tình yêu và lời khen.",
        "author": True,
    },
    12: {
        "main_color": "teacherblue",
        "accent_color": "chalkgold",
        "blue_color": "inkbrown",
        "header": "Điều Thầy Thấy, Trò Chưa Thấy",
        "label": "QUYỂN XII",
        "title_lines": ["Những Điều", "Thầy Giáo", "Nhìn Thấy"],
        "subtitle": "Tự Đọc, Học Ngữ, Và Lấy Chuyện Thật Mà Dạy Học Trò",
        "quote": "Có những điều học sinh không nói trong bài viết.\\\\\n   Nhưng thầy nào tinh ý đều nhìn thấy.",
        "author": True,
    },
    13: {
        "main_color": "nightblue",
        "accent_color": "lamporange",
        "blue_color": "deepbrown",
        "header": "Những Câu Hỏi Chưa Thành Lời",
        "label": "QUYỂN XIII",
        "title_lines": ["Những Câu Hỏi", "Học Trò", "Không Nói Thẳng"],
        "subtitle": "Đi Từ Những Câu Học Sinh Không Dám Hỏi Ra Thành Lời",
        "quote": "Có những đứa trẻ không hỏi: `Thầy cô có hiểu em không?'\\\\\n   Nhưng câu hỏi đó vẫn ở đó, ngày qua ngày.",
        "author": True,
    },
    14: {
        "main_color": "oliveink",
        "accent_color": "papergold",
        "blue_color": "warmbrown",
        "header": "Điều Học Trò Muốn Biết",
        "label": "QUYỂN XIV",
        "title_lines": ["100 Câu Hỏi", "Học Trò Hay Hỏi", "Về Chuyện Học"],
        "subtitle": "Những Câu Hỏi Về Việc Học, Điểm Số Và Đường Đời",
        "quote": "Có những câu hỏi học sinh hỏi bằng miệng.\\\\\n   Và có những câu hỏi chỉ được hỏi bằng ánh mắt.",
        "author": True,
    },
    15: {
        "main_color": "deepblue",
        "accent_color": "softcopper",
        "blue_color": "earthink",
        "header": "Lời Thầy Nói Thật",
        "label": "QUYỂN XV",
        "title_lines": ["Những Điều", "Thầy Muốn Nói", "Với Học Sinh"],
        "subtitle": "Thầy Nói Chuyện Thẳng, Gần Và Chậm Về Học Tập \\& Đường Đời",
        "quote": "Có những điều học sinh cần nghe không phải vì các em không biết,\\\\\n   mà vì nghe từ thầy thì mới chịu tin.",
        "author": True,
    },
    16: {
        "main_color": "slateink",
        "accent_color": "dustgold",
        "blue_color": "brickred",
        "header": "Bài Học Từ Mỗi Tiết Học",
        "label": "QUYỂN XVI",
        "title_lines": ["Những Bài Học", "Nhỏ Trong", "Lớp Học"],
        "subtitle": "Những Câu Nói Nhỏ, Khoảnh Khắc Thật Trong Lớp Học",
        "quote": "Trong một lớp học bình thường,\\\\\n   có những khoảnh khắc nhỏ thay đổi cả một đời người.",
        "author": True,
    },
    17: {
        "main_color": "inkgray",
        "accent_color": "warmgold",
        "blue_color": "mossgreen",
        "header": "Hiểu Sớm Đỡ Vấp",
        "label": "QUYỂN XVII",
        "title_lines": ["Những Điều", "Học Sinh Nên", "Hiểu Sớm"],
        "subtitle": "Hiểu Sớm Để Đỡ Vấp, Sống Tốt Hơn Từ Bây Giờ",
        "quote": "Có những điều hiểu sớm sẽ không làm tuổi học trò nặng hơn,\\\\\n   mà làm nó nhẹ hơn, sáng hơn.",
        "author": True,
    },
    18: {
        "main_color": "inkdark",
        "accent_color": "honeygold",
        "blue_color": "edugreen",
        "header": "Lời Thầy Còn Ở Lại",
        "label": "QUYỂN XVIII",
        "title_lines": ["Những Lời", "Thầy Nói", "Trong Lớp Học"],
        "subtitle": "50 Câu Nói Ngắn, Sâu~--- Mỗi Câu Một Câu Chuyện Nhỏ",
        "quote": "Học không phải để hơn người khác,\\\\\n   mà để hơn chính mình ngày hôm qua.",
        "author": True,
    },
    19: {
        "main_color": "inkdark",
        "accent_color": "silver",
        "blue_color": "deepnavy",
        "header": "Những Câu Nói Khiến Ta Nghĩ",
        "label": "QUYỂN XIX",
        "title_lines": ["100 Câu Nói", "Làm Học Sinh", "Im Lặng Suy Nghĩ"],
        "subtitle": "Những Câu Thầy Nói Khiến Cả Lớp Im Lặng Và Nghĩ",
        "quote": "Im lặng đôi khi là câu trả lời hay nhất.\\\\\n   Và lớp học im lặng vì đang nghĩ mới là lớp học thật.",
        "author": True,
    },
    20: {
        "main_color": "inkdark",
        "accent_color": "teal",
        "blue_color": "warmorange",
        "header": "Cười Rồi Ngẫm",
        "label": "QUYỂN XX",
        "title_lines": ["50 Câu Nói", "Hài Hước", "Nhưng Sâu Sắc"],
        "subtitle": "Thầy Cười Mà Học Trò Nghĩ",
        "quote": "Cười xong nhớ mới là hay.\\\\\n   Câu nói hài hước mà sâu sắc là nghệ thuật dạy học khó nhất.",
        "author": True,
    },
    21: {
        "main_color": "inkdark",
        "accent_color": "accentsgold",
        "blue_color": "darkred",
        "header": "Giật Mình Để Kịp Đổi Mình",
        "label": "QUYỂN XXI",
        "title_lines": ["30 Câu Nói Khiến", "Học Sinh Lười Học", "Phải Giật Mình"],
        "subtitle": "Thẳng Thắn, Rõ Ràng~--- Để Tỉnh Ra Trước Khi Trả Giá",
        "quote": "Lười hôm nay, trả giá ngày mai.\\\\\n   Giật mình sớm vẫn còn kịp hơn là nhận ra quá muộn.",
        "author": True,
    },
    22: {
        "main_color": "inkdark",
        "accent_color": "amber",
        "blue_color": "deepviolet",
        "header": "Nâng Em Dậy Khi Em Nản",
        "label": "QUYỂN XXII",
        "title_lines": ["50 Câu Nói", "Đỉnh Cao Sư Phạm", "Khi Học Sinh Nản Học"],
        "subtitle": "Nâng Đỡ, Động Viên, Mở Lối~--- Không La Mắng",
        "quote": "Nản một lúc không sao; đứng dậy mới quan trọng.\\\\\n   Thầy giỏi không là người không để học sinh nản, mà là người giúp các em đứng dậy.",
        "author": True,
    },
    23: {
        "main_color": "inkdark",
        "accent_color": "softrose",
        "blue_color": "softblue",
        "header": "Lời Cuối Năm Còn Nhớ",
        "label": "QUYỂN XXIII",
        "title_lines": ["50 Câu Nói", "Thầy Nói", "Cuối Năm Học"],
        "subtitle": "Rất Xúc Động~--- Để Tặng Và Giữ Lại",
        "quote": "Thầy tin em. Dù đi đâu, nhớ câu đó.\\\\\n   Những lời nói đúng lúc có thể thay đổi cả một cuộc đời.",
        "author": True,
    },
    24: {
        "main_color": "inkdark",
        "accent_color": "earthgold",
        "blue_color": "sepia",
        "header": "Những Sự Thật Làm Ta Lớn",
        "label": "QUYỂN XXIV",
        "title_lines": ["Bí Quyết", "Nhân Sinh"],
        "subtitle": "Những Câu Chuyện Đau Nhưng Rất Thật~--- 13 Chương, 190 Truyện",
        "quote": "Đọc xong thấy hơi đau nhưng hiểu thêm về cuộc sống.\\\\\n   Đau mà hiểu được vẫn là may mắn.",
        "author": True,
    },
}


def make_cover(num, data):
    mc = data["main_color"]
    ac = data["accent_color"]
    bc = data["blue_color"]
    label = data["label"]
    lines = data["title_lines"]
    subtitle = data["subtitle"]
    quote = data["quote"]

    # Title font size: smaller if 3 lines
    if len(lines) == 3:
        fs_main = "\\fontsize{28}{34}\\selectfont"
    else:
        fs_main = "\\fontsize{38}{45}\\selectfont"

    header = data.get("header", "Những Câu Chuyện Để Lớn Lên")

    # Build title lines LaTeX
    title_tex = ""
    for i, ln in enumerate(lines):
        color = mc if i % 2 == 0 else ac
        title_tex += f"  {{{fs_main}\\bfseries\\color{{{color}!80!black}}\n    {ln}}}\\\\[0.4cm]\n"

    out = f"""%============================================================
% TRANG BÌA SÁCH KHANG TRANG HƠN
%============================================================
\\begin{{titlepage}}
\\thispagestyle{{empty}}
\\pagecolor{{{mc}!5}} % Màu nền nhẹ nhàng, thanh lịch hơn

% Vẽ khung viền hoàng gia
\\begin{{tikzpicture}}[remember picture, overlay]
  % Khung nền lớn
  \\fill[white, opacity=0.6, rounded corners=20pt]
    ($(current page.north west)+(1.5cm,-1.5cm)$) rectangle
    ($(current page.south east)+(-1.5cm,1.5cm)$);

  % Viền mạ vàng đậm (Double lines)
  \\draw[{ac}!80!black, line width=3pt, rounded corners=15pt]
    ($(current page.north west)+(1.8cm,-1.8cm)$) rectangle
    ($(current page.south east)+(-1.8cm,1.8cm)$);

  \\draw[{ac}, line width=1pt, rounded corners=12pt]
    ($(current page.north west)+(2cm,-2cm)$) rectangle
    ($(current page.south east)+(-2cm,2cm)$);

  % Hoa văn góc
  \\foreach \\x/\\y/\\xsign/\\ysign in {{%
    north west/1.8cm/1/-1,
    north east/1.8cm/-1/-1,
    south west/1.8cm/1/1,
    south east/1.8cm/-1/1%
  }} {{
    \\draw[{ac}!80!black, line width=1.5pt]
      ($(current page.\\x) + (\\xsign*0.8cm, \\ysign*2.8cm)$) --
      ($(current page.\\x) + (\\xsign*2.8cm, \\ysign*2.8cm)$) --
      ($(current page.\\x) + (\\xsign*2.8cm, \\ysign*0.8cm)$);

    \\fill[{ac}!60!white] ($(current page.\\x) + (\\xsign*2cm, \\ysign*2cm)$) circle (3pt);
  }}

  % Khung phụ trang trí
  \\node[anchor=center] at ($(current page.center)-(0, 2cm)$) {{
    \\begin{{tikzpicture}}
      \\draw[{bc}!20, line width=0.5pt] (0,0) circle (5cm);
      \\draw[{ac}!40, line width=1pt] (0,0) circle (4.8cm);
    \\end{{tikzpicture}}
  }};
\\end{{tikzpicture}}

\\vspace*{{2cm}}

\\begin{{center}}
  % Phần trên
  {{\\color{{{ac}!90!black}}\\large$\\star\\;\\star\\;\\star$}}\\\\[0.3cm]
    {{\\fontsize{{14}}{{16}}\\selectfont\\color{{{bc}!80!black}}\\bfseries {header}}}\\\\[1.5cm]

  % Quyển
  \\begin{{tcolorbox}}[
    width=6.5cm,
    colback={ac}!20,
    colframe={ac}!80!black,
    arc=4pt,
    boxrule=1.5pt,
    halign=center
  ]
    {{\\fontsize{{18}}{{22}}\\selectfont\\bfseries\\color{{{mc}!80!black}}
     {label}}}
  \\end{{tcolorbox}}
  \\vspace{{0.8cm}}

  % Tiêu đề chính
{title_tex}
  % Tiêu đề phụ
  {{\\fontsize{{16}}{{20}}\\selectfont\\color{{{ac}!90!black}}\\itshape
    {subtitle}}}\\\\[1cm]

  % Đường kẻ giữa
  {{\\color{{{bc}!60}}\\rule{{6cm}}{{1pt}}}}\\\\[5pt]
  {{\\color{{{ac}!80!black}}\\large$\\diamond$\\hspace{{1cm}}$\\diamond$\\hspace{{1cm}}$\\diamond$}}\\\\[5pt]
  {{\\color{{{bc}!60}}\\rule{{6cm}}{{1pt}}}}\\\\[1.5cm]

  % Text giới thiệu
  {{\\normalsize\\itshape\\color{{{bc}!90!black}}
   ``{quote}''}}

  \\vfill

  % Tác giả
  {{\\fontsize{{16}}{{20}}\\selectfont\\bfseries\\color{{{bc}!90!black}}
    Sưu tầm \\& Tổng hợp: \\textbf{{Nguyễn Văn Sang}}}}\\\\[0.4cm]

  {{\\small\\color{{gray}} Bản mềm phát hành --- Năm 2026}}\\\\[0.5cm]
\\end{{center}}

\\afterpage{{\\nopagecolor}}
\\end{{titlepage}}"""
    return out


def main():
    for num in range(3, 25):
        if num not in COVERS:
            print(f"Q{num}: no data, skip")
            continue
        data = COVERS[num]
        cover_path = os.path.join(BASE, f"truyen-tich-cam-hung-quyen-{num}", "cover.tex")
        content = make_cover(num, data)
        with open(cover_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Q{num}: cover.tex written ({len(content)} chars)")


if __name__ == "__main__":
    main()
