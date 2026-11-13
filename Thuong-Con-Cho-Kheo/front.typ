#import "template.typ": *

// ------------------------------------------------ TRANG ĐỀ TẶNG
#let royal = rgb("0A2540")
#let kim   = rgb("C59B27")
#page(margin: (x: 2.2cm, y: 2.2cm), header: none, footer: none, fill: rgb("FAFBFD"))[
  #place(top + left, dx: -0.7cm, dy: -0.7cm,
    rect(width: 100% + 1.4cm, height: 100% + 1.4cm, stroke: 0.8pt + kim.lighten(30%), radius: 6pt))
  #align(center)[
    #v(1.2cm)
    #text(font: sans, size: 8.5pt, weight: "bold", fill: kim.darken(10%), tracking: 2.6pt)[TỦ SÁCH HỌC ĐƯỜNG  ·  SÁCH DÀNH CHO BA MẸ]
    #v(0.3cm)
    #text(font: serif, size: 30pt, weight: "bold", fill: royal)[Thương Con Cho Khéo]
    #v(0.1cm)
    #text(font: serif, size: 11.5pt, style: "italic", fill: teal)[6 phần  ·  18 chương  ·  76 tình huống con gặp phải]
    #v(0.15cm)
    #text(font: serif, size: 10pt, style: "italic", fill: slate)[Six parts · eighteen chapters · seventy-six situations your child may face]
    #v(0.5cm)
    #line(length: 40%, stroke: 0.8pt + kim.lighten(30%))
    #v(1.4cm)
    #text(font: serif, size: 11.5pt, style: "italic", fill: slate)[Bản sách này dành riêng cho]
    #v(0.4cm)
    #context text(font: serif, size: 28pt, weight: "bold", fill: royal)[#buyer.get()]
    #v(0.5cm)
    #block(width: 78%)[
      #set par(justify: false, leading: 0.8em)
      #text(font: serif, size: 12.5pt, style: "italic", fill: ink)[
        Thương con thì ba mẹ nào cũng thương. \
        Cuốn sách này chỉ góp thêm một chữ: khéo. \
        Để tình thương đó tới được chỗ con, \
        nguyên vẹn như lúc nó rời khỏi lòng ba mẹ.
      ]
      #v(0.3em)
      #text(font: serif, size: 10pt, style: "italic", fill: slate)[Every parent loves their child. This book adds only one word: wisely. So that love reaches the child as whole as when it left the parent's heart.]
    ]
    #v(1fr)
    #block(width: 86%, fill: white, stroke: 0.8pt + mist, radius: 9pt, inset: 16pt)[
      #set par(justify: true, leading: 0.72em)
      #set align(left)
      #text(font: sans, size: 8pt, weight: "bold", fill: crimson, tracking: 1.2pt)[LƯU Ý TRƯỚC KHI ĐỌC]
      #v(0.2em)
      #text(font: serif, size: 10pt, fill: ink)[
        Sách được biên soạn từ kinh nghiệm đứng lớp, trò chuyện với học sinh và phụ huynh, cùng những hiểu biết phổ thông về tâm lý lứa tuổi. Tên nhân vật và tình tiết là hư cấu, ghép từ nhiều chuyện thường gặp. Sách không thay thế ý kiến của bác sĩ hay chuyên viên tâm lý. Khi con có dấu hiệu nguy hiểm tới sức khỏe và tính mạng, xin ba mẹ đưa con tới cơ sở y tế, hoặc gọi *111* (tổng đài quốc gia bảo vệ trẻ em, miễn phí, suốt ngày đêm) và *115* (cấp cứu).
      ]
      #v(0.2em)
      #text(font: serif, size: 8.4pt, style: "italic", fill: slate)[This book draws on classroom experience, conversations with students and parents, and popular knowledge of child development. Names and details are fictional composites. It does not replace a doctor or psychologist. If your child shows signs of danger to health or life, take them to a medical facility or call 111 (Vietnam's free national child protection hotline) or 115 (emergency).]
    ]
    #v(0.8cm)
    #text(font: serif, size: 12pt, weight: "bold", fill: royal)[Thầy Nguyễn Văn Sang] \
    #text(font: serif, size: 9pt, style: "italic", fill: slate)[GV THPT Nguyễn Hữu Cảnh, TP. Hồ Chí Minh]
  ]
]

// ------------------------------------------------ LỜI TỰA
#accent.update(palette.at(1))
#heading(level: 1, numbering: none)[Lời Tựa]

#para1("Có một cảnh tôi gặp đi gặp lại trong những buổi họp phụ huynh. Người mẹ ngồi trước mặt tôi, mắt đỏ, nói: thầy ơi, tôi thương nó lắm, tôi làm tất cả vì nó, mà sao nó không nói với tôi một câu. Rồi ngay hôm sau, đứa con của chị ngồi đúng cái ghế đó, cũng mắt đỏ, nói: thầy ơi, ở nhà không ai hiểu em hết.", en: "There is a scene I have met again and again at parents\' meetings. The mother sits before me, eyes red, and says: I love him so much, I do everything for him, so why won\'t he say one word to me? The very next day her child sits in the same chair, eyes red too, and says: nobody at home understands me.")

#para1("Hai người đó thương nhau. Tôi không nghi ngờ điều ấy một giây nào. Nhưng tình thương của người mẹ rời khỏi lòng chị dưới dạng một câu hỏi về điểm số, một lời so sánh, một tiếng thở dài. Tới chỗ đứa con, nó đã thành một thứ khác hẳn: sự thất vọng, sự kiểm soát, cảm giác mình không bao giờ đủ. Tình thương bị thất lạc dọc đường, ngay trong một căn nhà.", en: "These two love each other. I do not doubt that for a second. But the mother\'s love leaves her in the form of a question about marks, a comparison, a sigh. By the time it reaches the child it has become something else entirely: disappointment, control, the feeling of never being enough. Love gets lost along the way, inside a single house.")

#para1("Cuốn sách này được viết cho quãng đường đó. Nó không dạy ba mẹ thương con, vì chuyện ấy không ai phải dạy. Nó chỉ bàn về chữ khéo: nói câu gì trước, câu gì sau, lúc nào nên im, lúc nào phải nói thẳng, để điều ba mẹ muốn trao tới được tay con mà không rơi vỡ.", en: "This book is written for that stretch of road. It does not teach parents to love; nobody needs teaching that. It only discusses the word wisely: which sentence to say first, which second, when to stay silent, when to speak plainly, so that what parents want to give reaches the child\'s hand without breaking.")

#para1("Sách gom 76 tình huống, xếp thành 18 chương và sáu phần, đi từ chuyện rất thường như tờ điểm kém, cái điện thoại, hai anh em giành nhau cái điều khiển, cho tới những chuyện làm ba mẹ mất ngủ: con bị bắt nạt, con nói dối, con lỡ gửi một tấm ảnh, con nói con không muốn sống nữa. Tôi cố ý không né những chuyện khó. Chính ở những chuyện đó, phản ứng của ba mẹ trong năm phút đầu tiên có sức nặng nhất.", en: "The book gathers 76 situations in 18 chapters and six parts, moving from very ordinary things, a poor mark, the phone, two siblings fighting over the remote, to things that cost parents sleep: a child who is bullied, who lies, who sent a photo they should not have, who says they do not want to live. I deliberately do not avoid the hard ones. It is exactly there that a parent\'s reaction in the first five minutes carries the most weight.")

#para1("Mỗi tình huống đi theo một nhịp: chuyện xảy ra, câu ba mẹ dễ buột miệng và điều con nghe được từ câu ấy, một cách nói khác, phần giải thích điều gì đang diễn ra trong con, và một việc nhỏ làm được ngay tối nay. Những lời thoại trong sách không phải kịch bản để học thuộc. Con của ba mẹ sẽ không trả lời y như đứa trẻ trong sách, và nhiều hôm con sẽ không trả lời gì cả. Không sao. Điều đáng giữ là cái hướng: nghe trước, hiểu rồi mới dạy, và giữ cho con một đường quay về.", en: "Each situation follows one rhythm: what happened, the sentence parents are likely to blurt and what the child hears in it, a different way of saying it, an explanation of what is going on inside the child, and one small thing to do tonight. The dialogues are not scripts to memorise. Your child will not answer exactly like the child in the book, and on many days will not answer at all. That is fine. What is worth keeping is the direction: listen first, understand before teaching, and keep a road home open for your child.")

#para1("Tôi cũng xin nói trước một điều. Khi đọc khung màu đỏ, ba mẹ sẽ gặp lại chính mình, có khi là mình của ngày hôm qua. Tôi cũng vậy, cả trong vai người thầy lẫn trong nhà mình. Đừng dùng cuốn sách này để dằn vặt. Không có ba mẹ nào không sai. Chương cuối cùng được viết riêng cho chuyện đó: sai thì quay lại, và không có tuổi nào của con là quá muộn để bắt đầu.", en: "I must also say one thing in advance. Reading the red boxes, parents will meet themselves, sometimes the self of yesterday. So do I, both as a teacher and in my own home. Do not use this book to torment yourself. No parent is never wrong. The last chapter is written for exactly that: when you are wrong, come back, and no age of your child is too late to begin.")

#cotloi("Con không cần ba mẹ hoàn hảo. Con cần ba mẹ đủ bình tĩnh để nghe, đủ vững để giữ giới hạn, và đủ khiêm tốn để quay lại nói: lúc nãy ba mẹ sai.", en: "Your child does not need perfect parents. They need parents calm enough to listen, steady enough to hold a limit, and humble enough to come back and say: earlier, I was wrong.")

#align(right)[
  #text(font: serif, style: "italic", fill: ink)[Thầy Nguyễn Văn Sang] \
  #text(font: sans, size: 9pt, fill: slate)[GV THPT Nguyễn Hữu Cảnh · TP. Hồ Chí Minh]
]

// ------------------------------------------------ CÁCH DÙNG SÁCH
#accent.update(palette.at(0))
#heading(level: 1, numbering: none)[Cách Dùng Cuốn Sách Này]

#para1("Sách không cần đọc từ đầu tới cuối. Nhà đang có chuyện gì thì lật tới chuyện đó trước, bảng tra nhanh ở trang sau sẽ chỉ đường. Riêng ba chương đầu là cái nền cho mọi tình huống khác, đáng đọc sớm.", en: "You need not read this book from start to finish. Turn first to whatever is happening at home; the quick-reference table overleaf will point the way. The first three chapters are the foundation for all the others and worth reading early.")

#text(font: sans, size: 12pt, weight: "bold", fill: navy)[Bảy khung trong mỗi tình huống  ·  Seven boxes in each situation]
#v(0.5em)

#boicanh("Một cảnh thường gặp trong nhà, kể ngắn gọn. Tên và tuổi của đứa trẻ chỉ để dễ hình dung, ba mẹ cứ thay bằng tên con mình.", en: "A common scene at home, told briefly. The child's name and age are only for picturing it; substitute your own child's.")
#phanxa("Câu mà phần lớn chúng ta sẽ nói theo phản xạ.", "Điều đứa trẻ thật sự nghe được từ câu đó. Đây là phần đáng đọc chậm nhất.", en: ("The sentence most of us say by reflex.", "What the child actually hears in it. The part most worth reading slowly."))
#scene("Ví dụ · Thử nói cách khác")[
  #con("Lời của con, cố giữ đúng giọng thật của trẻ.", en: "The child's line, in a child's real voice.")
  #me("Lời của ba hoặc mẹ: ghi nhận trước, hỏi thật, giữ giới hạn, và để con tự nói ra điều con nhận thấy.", en: "The parent's line: acknowledge first, ask sincerely, hold the limit, and let the child say what they notice.")
]
#hieusau1("Điều gì đang diễn ra trong con ở tuổi này, vì sao cách nói cũ dội ngược, vì sao cách mới có tác dụng. Một chút tâm lý lứa tuổi, nói bằng lời thường.", en: "What is happening inside the child at this age, why the old way backfires, why the new way works. A little developmental psychology in everyday words.")
#cotloi("Một hai câu gói lại điều đáng nhớ nhất của tình huống.", en: "One or two sentences holding what is most worth remembering.")
#lamngay1("Một việc nhỏ, cụ thể, làm được trong tối nay. Đọc mười tình huống không bằng làm một việc.", en: "One small, concrete thing you can do tonight. Doing one is worth more than reading ten.")
#caunoi("Một câu ngắn để dành sẵn trong miệng, dùng được khi cần.", en: "A short sentence to keep ready in your mouth for when you need it.")
#tusoi(("Hai câu hỏi để ba mẹ soi lại mình, không phải để trả lời cho ai.", "Hai vợ chồng đọc chung rồi nói với nhau thì càng tốt."), en: ("Two questions for parents to look at themselves, not to answer to anyone.", "Even better if a couple reads them together and talks."))

#v(0.6em)
#text(font: sans, size: 12pt, weight: "bold", fill: navy)[Ba điều nên biết trước khi áp dụng  ·  Three things to know before applying]
#v(0.4em)
#listbox1("ĐỌC CHO ĐÚNG", indigo, rgb("EEF2FF"), (
  "Lời thoại là để lấy hướng, không phải để đọc thuộc. Hãy nói bằng giọng của nhà mình. Con nhận ra ngay một câu học từ sách, nhưng con cũng nhận ra ngay khi ba mẹ thật lòng muốn hiểu.",
  "Lần đầu đổi cách nói, con có thể ngờ vực, im lặng, thậm chí thử ba mẹ. Đó là dấu hiệu bình thường. Điều thuyết phục con là sự đều đặn trong nhiều tuần, không phải một buổi tối đẹp.",
  "Nghe con và hiểu con không có nghĩa là chiều con. Hầu hết tình huống trong sách đều kết thúc bằng một giới hạn được giữ nguyên hoặc một hậu quả con phải tự sửa. Khác biệt chỉ nằm ở chỗ con không bị làm nhục trên đường tới đó.",
), mark: sym.triangle.filled.small.r, en: (
  "The dialogues are for direction, not for reciting. Speak in your own family's voice. A child spots a sentence borrowed from a book at once, but also spots at once when parents truly want to understand.",
  "The first time you change how you speak, your child may be wary, silent, even test you. That is normal. What persuades a child is steadiness over many weeks, not one lovely evening.",
  "Listening to and understanding your child does not mean indulging them. Most situations in the book end with a limit held or a consequence the child must repair. The difference is only that the child is not humiliated on the way there.",
))

#block(fill: rgb("FFF1EE"), stroke: 1pt + coral, radius: 12pt, inset: 14pt, width: 100%, breakable: false)[
  #text(font: sans, size: 11pt, weight: "bold", fill: coral.darken(10%))[Khi con đang gặp nguy hiểm  ·  When your child is in danger]
  #v(0.3em)
  #set par(justify: false)
  #text(size: 10.5pt)[Con nói về việc muốn chết, con tự làm đau mình, con bị xâm hại, bị đe dọa, tống tiền: đừng chờ đọc xong sách. Ở bên con, cất vật nguy hiểm, và gọi *111* (tổng đài quốc gia bảo vệ trẻ em, miễn phí, hoạt động suốt ngày đêm) hoặc *115* (cấp cứu), hoặc đưa con tới bệnh viện gần nhất. Chương 17 có hướng dẫn chi tiết.] \
  #text(font: serif, size: 9pt, style: "italic", fill: slate)[If your child talks of wanting to die, harms themselves, is abused, threatened or blackmailed: do not wait to finish the book. Stay with them, remove dangerous objects, and call 111 (Vietnam's free national child protection hotline, day and night) or 115 (emergency), or go to the nearest hospital. Chapter 17 has detailed guidance.]
]

// ------------------------------------------------ MỤC LỤC: CON ĐANG GẶP CHUYỆN GÌ?
#accent.update(navy)
#heading(level: 1, numbering: none, outlined: false)[Mục Lục]
#block(spacing: 0.9em)[
  #set par(justify: false)
  #text(font: serif, size: 11pt, style: "italic", fill: slate)[Mỗi chương là một nhóm chuyện thường gặp. Nhà đang có chuyện gì, tìm dòng đó rồi lật tới trang ghi bên phải. Contents, arranged by what your child may be going through.]
]

#let gist = (
  ("Mình sắp nổi nóng, sắp quát, sắp đánh con", "When you are about to lose your temper"),
  ("Con ít nói, hỏi gì cũng bình thường", "When your child says little"),
  ("Không biết khen chê sao cho đúng; hay so sánh con", "How to praise, correct and stop comparing"),
  ("Con điểm kém, giấu điểm, thi rớt", "Bad marks, hidden marks, a failed exam"),
  ("Con lười học, trì hoãn, mất gốc, chán học", "Lazy, procrastinating, behind, bored"),
  ("Mùa thi căng thẳng, chọn ngành, học quá sức", "Exam stress, choosing a path, overstudying"),
  ("Nhà trường gọi: quay cóp, đánh bạn, bị phạt, hỗn với cô", "When the school calls"),
  ("Con bị bắt nạt, bị tẩy chay, không có bạn", "Bullied, shut out, friendless"),
  ("Con bắt nạt bạn, hùa theo, chơi với bạn xấu, bị rủ làm sai", "When your child wrongs a friend"),
  ("Con có người yêu, thất tình, hỏi về giới tính, lỡ gửi ảnh riêng tư", "Romance, heartbreak, questions about sex, a private photo"),
  ("Con ôm điện thoại, mê game, thức khuya, lén nạp tiền", "Phones, games, late nights, secret top-ups"),
  ("Con nói dối, lấy tiền, hút vape, uống bia", "Lying, taking money, vaping, drinking"),
  ("Con cãi lại, đóng sầm cửa, nói ghét ba mẹ", "Talking back, slammed doors, I hate you"),
  ("Anh chị em đánh nhau, ganh tị, kêu ba mẹ bất công", "Siblings, jealousy, you are unfair"),
  ("Ba mẹ cãi nhau, ly hôn, nhà túng thiếu, người thân mất", "Quarrels, divorce, money trouble, a death"),
  ("Con tự ti, chê mình xấu, thua là bỏ, không dám thử", "Low self-worth, quitting, not daring to try"),
  ("Con buồn kéo dài, hoảng sợ, tự làm đau mình, nói muốn chết", "Lasting sadness, panic, self-harm, wanting to die"),
  ("Mình đã sai với con và muốn làm lại", "When you were wrong and want to make it right"),
)

#let toc-dots = box(width: 1fr, clip: true, repeat(gap: 3pt)[#text(font: sans, size: 7pt, fill: rgb("CBD5E1"))[·]])

#context {
  let hs = query(heading.where(level: 1).or(heading.where(level: 2))).filter(h => h.outlined)
  let seen-part = false
  let seen-back = false
  let ch = 0
  let pcount = 0
  let i = 0
  while i < hs.len() {
    let h = hs.at(i)
    if h.level == 1 and h.supplement == [Phan] {
      // ---- dải phần
      seen-part = true
      pcount += 1
      let col = part-colors.at(calc.rem(pcount - 1, part-colors.len()))
      v(0.7em, weak: true)
      link(h.location(), block(width: 100%, breakable: false, above: 1em, below: 0.6em, sticky: true,
        fill: gradient.linear(rgb("0A1B2E"), col, angle: 0deg), radius: 6pt, inset: (x: 12pt, y: 8pt))[
        #grid(columns: (1fr, auto), align: (left + horizon, right + horizon),
          text(font: serif, size: 12.5pt, weight: "bold", fill: white)[#h.body],
          text(font: sans, size: 8.5pt, weight: "bold", fill: rgb("F5B841"))[tr. #h.location().page()])
      ])
      i += 1
    } else if h.level == 1 and h.numbering != none {
      // ---- thẻ chương
      ch += 1
      let col = palette.at(calc.rem(ch - 1, palette.len()))
      let j = i + 1
      let secs = ()
      while j < hs.len() and hs.at(j).level == 2 {
        secs.push(hs.at(j)); j += 1
      }
      let g = gist.at(ch - 1)
      block(width: 100%, breakable: false, above: 0.55em, below: 0.55em, fill: white,
        stroke: (left: 3.5pt + col, rest: 0.6pt + mist), radius: (right: 6pt), inset: (x: 11pt, y: 7pt))[
        #link(h.location(), grid(columns: (2.1em, 1fr, auto), column-gutter: 7pt, align: (center + horizon, left + horizon, right + horizon),
          box(width: 2.1em, height: 2.1em, radius: 5pt, fill: col, align(center + horizon, text(font: sans, size: 11pt, weight: "bold", fill: white)[#ch])),
          [#text(font: serif, size: 11pt, weight: "bold", fill: navy)[#h.body] \
           #text(font: sans, size: 7.4pt, fill: col.darken(15%))[Dành cho lúc: #g.at(0)]],
          text(font: sans, size: 8.5pt, weight: "bold", fill: col)[#h.location().page()]))
        #v(0.2em)
        #for (k, sh) in secs.enumerate() [
          #link(sh.location(), grid(columns: (2.3em, auto, 1fr, auto), column-gutter: 3pt, align: (left + horizon, left + horizon, left + horizon, right + horizon),
            text(font: sans, size: 7.6pt, weight: "bold", fill: col)[#ch.#(k + 1)],
            text(font: serif, size: 9.3pt, fill: ink)[#sh.body],
            toc-dots,
            text(font: sans, size: 8pt, weight: "bold", fill: slate)[#sh.location().page()]))
          #v(0.12em)
        ]
      ]
      i = j
    } else if h.level == 1 {
      // ---- đầu sách / cuối sách
      let lead = []
      if seen-part and not seen-back {
        seen-back = true
        v(0.9em)
        block(width: 100%, above: 1em, below: 0.6em, sticky: true, fill: gradient.linear(rgb("0A1B2E"), teal, angle: 0deg), radius: 6pt, inset: (x: 12pt, y: 8pt))[
          #text(font: serif, size: 12.5pt, weight: "bold", fill: white)[Công cụ dùng ngay & phụ lục  ·  Tools & appendices]
        ]
      }
      link(h.location(), block(width: 100%, breakable: false, above: 0.35em, below: 0.35em,
        fill: if seen-part { rgb("F0FDFA") } else { softbg }, stroke: (left: 3pt + if seen-part { teal } else { gold }), radius: (right: 4pt), inset: (x: 10pt, y: 5pt))[
        #grid(columns: (auto, 1fr, auto), column-gutter: 6pt, align: (left + horizon, left + horizon, right + horizon),
          text(font: serif, size: 10.5pt, weight: "bold", fill: navy)[#h.body], toc-dots,
          text(font: sans, size: 8.5pt, weight: "bold", fill: if seen-part { teal } else { amber })[#h.location().page()])
      ])
      i += 1
    } else {
      i += 1
    }
  }
}
