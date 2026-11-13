#import "template.typ": *

// ---------- BÌA ----------
#page(margin: 0pt, fill: navy, header: none, footer: none)[
  #place(top + left, dx: 0pt, dy: 0pt, rect(width: 100%, height: 9cm, fill: rgb("162F4D")))
  #place(top + left, dx: 2.2cm, dy: 3.2cm, text(font: sans, size: 10pt, weight: "bold", tracking: 3pt, fill: gold)[SỔ TAY THẦY CÔ])
  #place(top + left, dx: 2.2cm, dy: 4.4cm, block(width: 15cm, text(font: serif, size: 54pt, weight: "bold", fill: white)[Phạt Mà\ Thương]))
  #place(top + left, dx: 2.2cm, dy: 11cm, block(width: 14cm)[
    #text(font: serif, size: 15pt, style: "italic", fill: rgb("CBD5E1"))[Những chiêu phạt vui, nhẹ, tình cảm mà vẫn có sức răn, để học sinh nhớ lỗi mà không mất mặt.]
  ])
  #place(top + left, dx: 2.2cm, dy: 16.5cm, block(width: 14cm)[
    #text(font: sans, size: 12pt, weight: "bold", fill: gold)[14 chương · 69 tình huống]\
    #text(font: sans, size: 10pt, fill: rgb("94A3B8"))[Mỗi tình huống: một chiêu phạt, lời thầy nói, ranh giới dừng ở đâu, biến tấu thêm.]
  ])
  #place(bottom + left, dx: 2.2cm, dy: -2.4cm, text(font: serif, size: 14pt, fill: white)[Nguyễn Văn Sang])
  #place(bottom + left, dx: 2.2cm, dy: -1.7cm, text(font: sans, size: 9pt, fill: rgb("94A3B8"))[Giáo viên THPT Nguyễn Hữu Cảnh, TP.HCM])
]

// ---------- LỜI TỰA ----------
#pagebreak(weak: true)
#heading(level: 1, numbering: none, outlined: true)[Lời tựa: vì sao thầy cô cần nhiều chiêu hơn]
Thầy cô nào cũng từng đứng trước một học sinh phạm lỗi và nghĩ: phạt thế nào cho vừa? Nặng quá thì sợ làm tổn thương, nhẹ quá thì sợ lớp nhờn. Nhiều thầy cô tâm sự rằng mình phạt khá thường xuyên, nhưng cảm thấy kho ý tưởng cứ cạn dần, đến lúc chỉ còn nhắc nhở, chép phạt, đứng ngoài hành lang. Những cách ấy không sai, nhưng dùng mãi thì chai, và nhiều khi học sinh chỉ nhớ cảm giác bị phạt chứ không nhớ vì sao.

Cuốn sách này gom lại những chiêu phạt có bốn điểm chung. *Ngắn*: không quá vài phút. *Riêng tư*: không làm em mất mặt trước bạn bè. *Gắn đúng lỗi*: em làm gì thì sửa đúng cái đó. *Kết thúc bằng một việc có ích hoặc một nụ cười*: em ra về với cảm giác mình đã trả được món nợ, chứ không phải mình bị hạ thấp.

Mỗi tình huống trong sách đi theo một lối quen thuộc: chuyện xảy ra, chiêu phạt, lời thầy nói gợi ý, vì sao chiêu này có tác dụng, ranh giới dừng ở đâu, biến tấu thêm, và một câu thầy cô có thể nói ngay. Phần ranh giới là phần quan trọng nhất. Chiêu hay đến mấy mà dùng sai lúc, sai người cũng thành tổn thương.

Sách không hứa mọi chiêu hợp mọi học sinh. Mỗi lớp, mỗi em khác nhau. Hãy lấy chiêu nào hợp, đổi cho vừa tay, và bỏ chiêu nào không hợp. Chương cuối còn cho thầy cô những khung để tự sinh chiêu mới khi chiêu cũ đã nhàm.

#v(1em)
#align(right)[#text(style: "italic")[Nguyễn Văn Sang]]

// ---------- NGUYÊN TẮC ----------
#pagebreak(weak: true)
#heading(level: 1, numbering: none, outlined: true)[Bảy nguyên tắc trước khi phạt]
#v(0.3em)
#listbox1("BẢY NGUYÊN TẮC", rgb("1E293B"), softbg, (
  "Hỏi trước khi phạt: em đang thiếu gì, mệt gì, lo gì? Hành vi chỉ là phần nổi.",
  "Phạt riêng, khen chung. Không bao giờ làm em mất mặt trước bạn bè.",
  "Gắn đúng lỗi. Em ồn thì giúp lớp yên, em làm hỏng thì giúp sửa, em làm tổn thương thì làm điều tử tế cho người bị tổn thương.",
  "Phạt không tập thể cho lỗi của một người. Học sinh tha thứ cho nghiêm khắc nhưng không tha thứ cho bất công.",
  "Kết thúc bằng một việc có ích hoặc một nụ cười. Em phải ra về nhẹ lòng mà vẫn nhớ.",
  "Không phạt khi lỗi là tín hiệu: em đói, em mệt vì làm việc nhà, em đang có chuyện, em có nhu cầu đặc biệt.",
  "Thầy cô sai thì xin lỗi. Một lời xin lỗi thật là bài giảng đạo đức mạnh nhất.",
))
#v(1.2em)
#block(fill: rgb("FFF7ED"), stroke: (left: 3pt + amber), inset: 12pt, radius: (right: 4pt), width: 100%)[
  #text(font: sans, size: 9pt, weight: "bold", fill: amber, tracking: 1pt)[LƯU Ý QUAN TRỌNG]\
  #v(2pt)
  Những chiêu trong sách dành cho lỗi nề nếp và lỗi học đường thông thường. Với bạo lực, quấy rối, bắt nạt kéo dài, tự hại, hay dấu hiệu em bị xâm hại, hãy dừng chiêu nhẹ, bảo vệ em và báo ngay nhà trường, gia đình và người có trách nhiệm. Mọi chiêu cần phù hợp với quy chế của trường và quy định pháp luật.
]

// ---------- MỤC LỤC ----------
#pagebreak(weak: true)
#heading(level: 1, numbering: none, outlined: false)[Mục lục]
#outline(title: none, depth: 1)
