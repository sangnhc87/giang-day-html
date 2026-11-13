#import "template.typ": *

// ------------------------------------------------ THƯ GỬI BA MẸ
#accent.update(palette.at(1))
#heading(level: 1, numbering: none)[Thư Cuối Sách: Gửi Ba Mẹ]

#block(fill: white, stroke: 0.8pt + mist, radius: 16pt, inset: 20pt, width: 100%)[
#set par(justify: true, leading: 0.78em, spacing: 1.15em)
#text(font: serif, size: 12pt, style: "italic")[
Anh chị thân mến,

Nếu anh chị đọc tới trang này, tôi đoán anh chị đang mệt. Người tìm đọc một cuốn sách về cách nói chuyện với con thường là người đang lo, đang thương mà chưa biết làm sao. Riêng việc anh chị còn tìm cách đã nói lên nhiều điều tốt về anh chị rồi.

Tôi đứng lớp, tôi được nghe phía bên kia của câu chuyện. Tôi xin kể lại với anh chị ba điều mà học trò hay nói với tôi nhất, khi các em chắc rằng ba mẹ mình không nghe thấy.

Một: các em thương ba mẹ nhiều hơn anh chị tưởng. Đứa lì nhất lớp, hỏi tới nhà là mắt đỏ. Đứa cãi anh chị tối qua, sáng nay ngồi trong lớp thấy có lỗi suốt hai tiết.

Hai: các em sợ làm ba mẹ thất vọng hơn sợ mọi hình phạt. Rất nhiều lời nói dối, nhiều lần giấu điểm, bắt đầu từ nỗi sợ đó chứ không phải từ sự coi thường.

Ba: các em nhớ rất lâu những lần được ba mẹ nghe. Có em kể với tôi về một buổi tối ba ngồi nghe em nói hết mà không la, kể như kể một kỳ tích. Chỉ một buổi tối, mà em mang theo mấy năm.

Nên xin anh chị đừng nản khi thử một cách nói mới mà con chưa đáp lại. Con đang nhìn. Con đang kiểm tra xem lần này có thật không. Cứ làm đều. Cửa khép từ từ thì cũng mở lại từ từ.

Và xin anh chị thương luôn cả mình. Anh chị cũng từng là một đứa trẻ, có khi chưa từng được ai nói với mình những câu trong sách này. Cho đi một thứ mình chưa từng được nhận là việc rất khó. Anh chị đang làm việc đó.

Chúc cho bữa cơm tối nay ở nhà anh chị có thêm một câu chuyện.

#align(right)[Thầy Nguyễn Văn Sang]
]
#v(0.5em)
#set par(justify: true, leading: 0.7em)
#text(font: serif, size: 9.6pt, style: "italic", fill: slate)[
Dear parents,

#v(0.2em)
If you have read this far, I suspect you are tired. People who look for a book on how to talk to their children are usually worried, loving and unsure what to do. That you are still looking for a way already says a great deal that is good about you.

#v(0.2em)
I stand in a classroom, so I hear the other side of the story. Let me tell you the three things students say to me most, when they are sure their parents cannot hear.

#v(0.2em)
One: they love their parents more than you think. The most stubborn child in the class tears up when I mention home. The one who argued with you last night sits in lessons feeling guilty for two periods.

#v(0.2em)
Two: they fear disappointing their parents more than any punishment. Many lies, many hidden marks, begin in that fear, not in contempt.

#v(0.2em)
Three: they remember for a very long time the times their parents listened. One student told me about an evening when Dad listened all the way through without shouting, told like a miracle. A single evening, and the child carried it for years.

#v(0.2em)
So please do not be discouraged when you try a new way of speaking and your child does not respond. They are watching. They are testing whether it is real this time. Keep at it. A door that closed slowly opens slowly too.

#v(0.2em)
And please be kind to yourselves. You were once a child as well, perhaps never told the sentences in this book. Giving what you never received is very hard. You are doing it.

#v(0.2em)
May dinner at your house tonight have one more story in it.
]
]

// ------------------------------------------------ CHÍN NGUYÊN TẮC
#accent.update(palette.at(0))
#heading(level: 1, numbering: none)[Sổ Tay: 9 Nguyên Tắc Thương Con Cho Khéo]

#let nt = (
  ("Giữ mình trước, rồi mới giữ con", "Đang nóng thì chưa dạy. Bước ra, thở, quay lại. Chín mươi giây im lặng cứu được những câu nói mười năm không rút lại được.", "Steady yourself first, then your child", "While you are hot, do not teach. Step out, breathe, return. Ninety seconds of silence saves sentences that cannot be taken back in ten years."),
  ("An toàn trước, đúng sai sau", "Câu đầu tiên khi con gây chuyện là con có sao không. Đứa trẻ thấy mình an toàn mới có sức để hối lỗi.", "Safety first, right and wrong second", "The first sentence when your child causes trouble is: are you all right? A child who feels safe has strength to feel remorse."),
  ("Nghe cho hết rồi mới nói", "Dừng tay, quay người lại, nhắc lại ý con bằng lời mình. Con chỉ nghe lời khuyên sau khi thấy mình đã được nghe.", "Listen all the way before speaking", "Stop your hands, turn your body, repeat your child's point in your own words. Children only hear advice after feeling heard."),
  ("Gọi tên cảm xúc, giới hạn hành vi", "Con được quyền giận, buồn, ghen, sợ. Con không được quyền đánh, phá, xúc phạm. Hai vế đi cùng nhau.", "Name the feeling, limit the behaviour", "Your child may be angry, sad, jealous, afraid. They may not hit, destroy or insult. The two halves go together."),
  ("Chê việc, không chê người", "Việc này chưa ổn khác hẳn với con là đứa hư. Đừng bao giờ gọi con bằng tên của lỗi con vừa phạm.", "Criticise the deed, not the person", "This isn't right yet is very different from you are bad. Never call a child by the name of the mistake they just made."),
  ("Nhắc riêng, khen cụ thể", "Giữ thể diện cho con trước người khác. Khen công sức và cách làm, những thứ con làm chủ được.", "Correct in private, praise specifically", "Protect your child's face before others. Praise effort and method, things they can control."),
  ("Hậu quả để sửa, không để trả đũa", "Hậu quả tốt thì liên quan tới việc sai, tương xứng, có điểm kết thúc. Xong rồi là xong, không lôi lại.", "Consequences to repair, not to retaliate", "A good consequence is tied to what went wrong, proportionate, and has an end. When it is done, it is done."),
  ("Làm cho sự thật rẻ hơn lời nói dối", "Con nói thật thì được giúp, không bị làm nhục. Giữ lời hứa đó cả khi sự thật làm mình choáng.", "Make the truth cheaper than a lie", "Tell the truth and you get help, not humiliation. Keep that promise even when the truth staggers you."),
  ("Sai thì quay lại", "Xin lỗi con cho đàng hoàng, không kèm chữ nhưng. Va chạm rồi nối lại làm sợi dây với con chắc hơn.", "When wrong, come back", "Apologise properly, with no but. Clashing and reconnecting makes the bond stronger."),
)
#for (i, n) in nt.enumerate() [
  #block(breakable: false, width: 100%, fill: white, stroke: 0.8pt + mist, radius: 12pt, inset: 12pt, spacing: 0.75em)[
    #grid(columns: (2.6em, 1fr), column-gutter: 8pt, align: top,
      box(width: 2.1em, height: 2.1em, radius: 50%, fill: palette.at(calc.rem(i, 6)), align(center + horizon, text(font: sans, weight: "bold", fill: white)[#str(i + 1)])),
      [#text(font: sans, weight: "bold", size: 12pt, fill: navy)[#n.at(0)]
       #v(0.1em)
       #set par(justify: false, leading: 0.62em)
       #text(font: serif, size: 0.96em, fill: ink)[#n.at(1)]
       #text(font: serif, size: 0.8em, style: "italic", fill: slate)[ #n.at(2): #n.at(3)]])
  ]
]

// ------------------------------------------------ SƠ CỨU 90 GIÂY
#accent.update(palette.at(3))
#heading(level: 1, numbering: none)[Sơ Cứu 90 Giây Khi Ba Mẹ Sắp Nổi Nóng]

#para1("Cơn giận lên rất nhanh và cũng dịu khá nhanh nếu mình không đổ thêm dầu. Năm bước dưới đây chỉ mất chừng một phút rưỡi. Chép ra giấy, dán ở tủ lạnh.", en: "Anger rises very fast and also settles fairly fast if we do not pour on more oil. These five steps take about a minute and a half. Copy them out and stick them on the fridge.")

#let sc = (
  ("DỪNG", "Ngậm miệng lại. Chưa nói câu nào hết. Câu đầu tiên bật ra lúc này gần như chắc chắn là câu mình sẽ hối hận.", "STOP", "Close your mouth. Say nothing yet. The first sentence that comes out now is almost certainly one you will regret."),
  ("LÙI", "Lùi một bước, hoặc ra khỏi phòng. Nói đúng một câu: ba mẹ cần vài phút, ba mẹ sẽ quay lại.", "STEP BACK", "Take a step back or leave the room. Say exactly one sentence: I need a few minutes, I will come back."),
  ("THỞ", "Thở ra thật dài, dài hơn hít vào. Năm hơi. Rửa mặt nước lạnh hoặc uống một ly nước.", "BREATHE", "Breathe out long, longer than you breathe in. Five breaths. Splash cold water on your face or drink a glass of water."),
  ("HỎI", "Tự hỏi ba câu: Con có đang an toàn không? Chuyện này một năm nữa còn quan trọng không? Mình muốn con học được gì sau chuyện này?", "ASK", "Ask yourself three things: Is my child safe? Will this matter in a year? What do I want my child to learn from this?"),
  ("QUAY LẠI", "Quay lại trong ngày, ngồi ngang tầm con, bắt đầu bằng: lúc nãy ba mẹ giận quá. Giờ mình nói chuyện.", "RETURN", "Come back within the day, sit at your child's level, and begin: I was too angry earlier. Now let's talk."),
)
#for (i, s) in sc.enumerate() [
  #block(breakable: false, width: 100%, fill: palette.at(calc.rem(i + 3, 6)).lighten(93%), stroke: (left: 4pt + palette.at(calc.rem(i + 3, 6))), radius: (right: 8pt), inset: (x: 14pt, y: 10pt), spacing: 0.7em)[
    #grid(columns: (7.2em, 1fr), column-gutter: 8pt, align: (left + horizon, left + horizon),
      text(font: sans, size: 12pt, weight: "bold", fill: palette.at(calc.rem(i + 3, 6)).darken(10%))[#str(i + 1). #s.at(0)],
      { set par(justify: false, leading: 0.62em); text(font: serif, size: 0.98em, fill: ink)[#s.at(1)]; parbreak(); text(font: serif, size: 0.8em, style: "italic", fill: slate)[#s.at(2): #s.at(3)] })
  ]
]

// ------------------------------------------------ BẢNG 30 CÂU
#accent.update(palette.at(2))
#heading(level: 1, numbering: none)[30 Câu Con Hay Nói: Nghe Gì Phía Sau Và Đáp Sao]

#let rows = (
  ("Bình thường.", "Câu hỏi nghe như kiểm tra, hoặc con mệt.", "Ừ. Hôm nay có gì mắc cười không con?", "Fine.", "The question sounds like an inspection, or the child is tired.", "Okay. Did anything make you laugh today?"),
  ("Con không sao.", "Có sao, nhưng chưa chắc ba mẹ chịu nghe.", "Ừ. Lúc nào muốn kể thì mẹ ở đây nha.", "I'm fine.", "Not fine, but not sure you will listen.", "Okay. Whenever you want to talk, I'm here."),
  ("Kệ con.", "Đau hoặc giận, không muốn bị sửa.", "Mẹ kệ được khi con ổn. Hôm nay mẹ thấy con chưa ổn.", "Whatever.", "Hurt or angry; does not want to be fixed.", "I'll let it go when you're okay. Today I don't think you are."),
  ("Ba mẹ không hiểu đâu.", "Từng kể mà bị gạt đi.", "Đúng, ba chưa hiểu. Con chỉ ba đi.", "You wouldn't understand.", "Told you once and was brushed off.", "You're right, I don't yet. Show me."),
  ("Con ghét mẹ!", "Giận lắm, và tin mẹ đủ vững để nghe.", "Con đang giận mẹ dữ lắm. Mẹ vẫn thương con.", "I hate you!", "Very angry, and trusts you to be strong enough to hear it.", "You're very angry with me. I still love you."),
  ("Con không làm.", "Sợ bị phạt hơn sợ nói dối.", "Mẹ không hỏi ai làm. Mình tính coi sửa sao.", "I didn't do it.", "More afraid of punishment than of lying.", "I'm not asking who did it. Let's work out how to fix it."),
  ("Tại nó trước!", "Muốn được coi là công bằng.", "Mẹ không xử ai trước. Con muốn gì, nói mẹ nghe.", "He started it!", "Wants to be seen as fair.", "I'm not ruling on who was first. Tell me what you want."),
  ("Ai cũng có, chỉ con không có.", "Sợ lạc khỏi nhóm bạn.", "Không có mà bạn bè có thì khó chịu thiệt. Kể mẹ nghe.", "Everyone has one except me.", "Afraid of falling out of the group.", "It's hard when others have it and you don't. Tell me about it."),
  ("Con ngu lắm.", "Vừa thất bại, đang tự mắng mình.", "Bài này khó chứ không phải con ngu. Kẹt chỗ nào?", "I'm so stupid.", "Has just failed and is scolding themselves.", "This one is hard; you're not stupid. Where did you get stuck?"),
  ("Con xấu quá.", "Bị chê, hoặc so mình với trên mạng.", "Có ai nói gì làm con buồn hả? Kể mẹ nghe.", "I'm ugly.", "Been mocked, or comparing with what they see online.", "Did someone say something that hurt? Tell me."),
  ("Con không muốn đi học.", "Mệt, sợ, hoặc có chuyện ở trường.", "Chắc có chuyện gì làm con nặng lắm. Chuyện gì vậy con?", "I don't want to go to school.", "Tired, scared, or something happened at school.", "Something must feel very heavy. What is it?"),
  ("Con đau bụng.", "Có thể là lo âu đang nói qua cơ thể.", "Mẹ tin con đau. Ở trường có gì làm con lo không?", "My tummy hurts.", "Anxiety may be speaking through the body.", "I believe it hurts. Is anything at school worrying you?"),
  ("Học làm gì.", "Kiệt sức hoặc mất phương hướng.", "Con đang mệt hay đang thấy vô nghĩa? Hai cái khác nhau.", "What's the point of studying?", "Exhausted or lost direction.", "Are you tired, or does it feel pointless? Those are different."),
  ("Chút nữa.", "Chưa biết bắt đầu từ đâu, hoặc bị giục nhiều.", "Mấy giờ thì con bắt đầu? Con tự chọn giờ đi.", "In a minute.", "Does not know where to start, or has been nagged too much.", "What time will you start? You choose."),
  ("Con làm rồi.", "Chưa làm, sợ bị la.", "Con đem ra mình coi chung. Chưa xong cũng không sao.", "I already did it.", "Has not, and is afraid of a scolding.", "Bring it and we'll look together. Unfinished is fine."),
  ("Cô ghét con.", "Từng bị làm quê trước lớp.", "Chuyện gì làm con thấy vậy? Kể chuyện đầu tiên con nhớ.", "The teacher hates me.", "Was once humiliated in front of the class.", "What made you feel that? Tell me the first thing you remember."),
  ("Tụi nó giỡn thôi mà.", "Đang bị trêu mà ngại nói.", "Giỡn là hai bên cùng vui. Con có vui không?", "They were only joking.", "Is being teased but too embarrassed to say.", "A joke is when both sides enjoy it. Did you?"),
  ("Con không có bạn.", "Cô đơn, thấy mình khác người.", "Con chỉ cần một hai đứa hợp. Mình tìm chỗ có những đứa giống con.", "I have no friends.", "Lonely, feels different from others.", "You only need one or two who suit you. Let's find where they are."),
  ("Mẹ đừng nói với ai.", "Sợ bị trả đũa, sợ mất mặt.", "Mẹ không làm gì sau lưng con. Mình cùng tính.", "Don't tell anyone.", "Fears revenge and embarrassment.", "I won't do anything behind your back. Let's decide together."),
  ("Ba mẹ thương em hơn.", "Nhớ thời gian riêng với ba mẹ.", "Con thấy mình bị bỏ quên hả? Tối nay mẹ là của riêng con.", "You love the baby more.", "Misses time alone with parents.", "Do you feel forgotten? Tonight I'm yours alone."),
  ("Không công bằng!", "Thường là đúng một phần.", "Chỗ nào con thấy lệch? Nói từng chuyện, ba nghe.", "It's not fair!", "Often right in part.", "Where does it look lopsided? Tell me one thing at a time; I'll listen."),
  ("Con lớn rồi.", "Cần thêm quyền tự quyết.", "Ừ, con lớn rồi. Việc này con tự quyết, mẹ chỉ giữ ba cái mốc.", "I'm grown up.", "Needs more say over their own life.", "Yes, you are. You decide this; I only keep three markers."),
  ("Mẹ hỏi hoài.", "Thấy bị kiểm soát.", "Mẹ hỏi nhiều thiệt. Mẹ hỏi một câu thôi rồi mẹ nghe.", "You keep asking.", "Feels controlled.", "I do ask a lot. I'll ask one thing and then listen."),
  ("Con chỉ thử thôi mà.", "Tò mò, bị bạn rủ.", "Cảm ơn con nói thật. Lúc thử con thấy sao?", "I only tried it.", "Curious, was pressed by friends.", "Thank you for telling me the truth. How did it feel when you tried?"),
  ("Con sợ.", "Cần chỗ dựa, không cần lời bảo đừng sợ.", "Sợ là phải. Mẹ ở đây. Con sợ nhất cái gì?", "I'm scared.", "Needs support, not to be told not to be scared.", "Being scared makes sense. I'm here. What scares you most?"),
  ("Con xin lỗi được chưa?", "Muốn kết thúc cho nhanh.", "Mẹ nghe rồi. Giờ mình tính coi sửa chuyện đó ra sao.", "Sorry, okay?", "Wants it over quickly.", "I hear you. Now let's work out how to put that right."),
  ("Con mệt lắm rồi.", "Quá tải, có thể cần giúp đỡ.", "Mệt trong người hay trong lòng? Hôm nay nghỉ đã.", "I'm so tired.", "Overloaded, may need help.", "Tired in your body or your heart? Rest today first."),
  ("Không ai thương con hết.", "Cô đơn sâu, cần được ôm.", "Có mẹ thương. Lại đây. Kể mẹ nghe chuyện gì.", "Nobody loves me.", "Deep loneliness, needs a hug.", "I love you. Come here. Tell me what happened."),
  ("Con là gánh nặng.", "Dấu hiệu cần chú ý nghiêm túc.", "Con chưa bao giờ là gánh nặng. Con có nghĩ tới chuyện tự hại mình không?", "I'm a burden.", "A sign needing serious attention.", "You have never been a burden. Are you thinking of hurting yourself?"),
  ("Con muốn biến mất.", "Báo động. Xem chương 17.", "Mẹ tin con. Mẹ ở đây, không đi đâu hết. Nói mẹ nghe.", "I want to disappear.", "Alarm. See chapter 17.", "I believe you. I'm here and not going anywhere. Tell me."),
)
#set text(size: 9.2pt)
#table(
  columns: (1.4fr, 1.5fr, 2.4fr),
  stroke: (x, y) => (bottom: 0.5pt + mist),
  inset: (x: 7pt, y: 6pt),
  fill: (x, y) => if y == 0 { navy } else if calc.even(y) { rgb("F6F8FB") } else { white },
  align: left + horizon,
  table.header(
    text(font: sans, weight: "bold", fill: white, size: 8.5pt)[Câu con nói · What your child says],
    text(font: sans, weight: "bold", fill: white, size: 8.5pt)[Điều có thể đang ẩn · What may lie beneath],
    text(font: sans, weight: "bold", fill: white, size: 8.5pt)[Ba mẹ thử đáp · Try replying],
  ),
  ..rows.enumerate().map(((i, r)) => (
    [#text(font: serif, weight: "bold", fill: navy)[#str(i + 1). #r.at(0)] \
     #text(font: serif, size: 8pt, style: "italic", weight: "regular", fill: slate)[#r.at(3)]],
    [#text(font: sans, size: 8.5pt, fill: slate)[#r.at(1)] \
     #text(font: serif, size: 7.8pt, style: "italic", fill: slate)[#r.at(4)]],
    [#text(font: serif, fill: ink)[#r.at(2)] \
     #text(font: serif, size: 8pt, style: "italic", fill: slate)[#r.at(5)]],
  )).flatten()
)

// ------------------------------------------------ 21 NGÀY
#set text(size: 11.6pt)
#accent.update(palette.at(4))
#heading(level: 1, numbering: none)[21 Ngày Nối Lại Với Con]

#para1("Ba tuần, mỗi ngày một việc nhỏ, phần lớn chỉ mất mười phút. Không cần làm đủ, không cần làm đúng thứ tự. Lỡ một ngày thì hôm sau làm tiếp. Tô màu vào ô sau khi làm xong.", en: "Three weeks, one small thing a day, most taking ten minutes. You need not do them all or in order. If you miss a day, carry on the next. Colour a box when done.")

#let weeks = (
  ("Tuần 1 · Có mặt", palette.at(0), (
    "Mười phút bên con, không dạy, không nhắc",
    "Hỏi: hôm nay có gì vui, có gì chán?",
    "Bữa cơm không điện thoại",
    "Khen một việc cụ thể con đã làm",
    "Gõ cửa phòng con và chờ",
    "Kể con nghe một chuyện của mình",
    "Ghé phòng con chúc ngủ ngon",
  )),
  ("Tuần 2 · Lắng nghe", palette.at(1), (
    "Nghe con nói hết, không chen vào",
    "Hỏi: con muốn mẹ nghe hay góp ý?",
    "Nhờ con chỉ một thứ con thích",
    "Không nhắc con học cả ngày",
    "Kể một lần mình từng thất bại",
    "Nói: giận cũng được, mẹ vẫn thương",
    "Làm chung với con một việc con chọn",
  )),
  ("Tuần 3 · Nói điều khó nói", palette.at(3), (
    "Xin lỗi con một chuyện cũ",
    "Nói: mấy giờ cũng gọi, ba mẹ tới đón",
    "Nói: điểm nào nói thật mẹ cũng không la",
    "Nói một điểm mạnh của con, có bằng chứng",
    "Hỏi: ba mẹ làm gì khiến con khó chịu nhất?",
    "Viết cho con một lá thư ngắn",
    "Nói: ba mẹ tự hào về con",
  )),
)
#let en21 = ("Ten minutes beside your child, no teaching, no reminding", "Ask: what was fun, what was dull today?", "A dinner with no phones", "Praise one specific thing your child did", "Knock on your child's door and wait", "Tell your child one story of your own", "Look in at bedtime and say goodnight", "Listen to your child to the end, no interrupting", "Ask: do you want me to listen or advise?", "Ask your child to show you something they like", "Do not remind them to study all day", "Tell a time you failed", "Say: be angry; I still love you", "Do one thing together that your child picks", "Apologise for one old matter", "Say: any hour, we will come and get you", "Say: tell the truth about marks and I won't shout", "Name one strength of your child, with evidence", "Ask: what do we do that bothers you most?", "Write your child a short letter", "Say: we are proud of you")
#for (wi, w) in weeks.enumerate() [
  #block(breakable: false, width: 100%, fill: w.at(1).lighten(93%), stroke: 0.8pt + w.at(1).lighten(50%), radius: 14pt, inset: 13pt, spacing: 0.9em)[
    #text(font: sans, weight: "bold", size: 13pt, fill: w.at(1).darken(15%))[#w.at(0)]
    #v(0.5em)
    #grid(columns: (1fr,) * 7, column-gutter: 5pt,
      ..w.at(2).enumerate().map(((d, t)) =>
        box(width: 100%, height: 3.6cm, fill: white, stroke: 1pt + w.at(1), radius: 9pt, inset: 5pt)[
          #set par(justify: false, leading: 0.5em)
          #align(center)[#text(font: sans, size: 7.5pt, weight: "bold", fill: w.at(1))[NGÀY #str(wi * 7 + d + 1)]]
          #v(0.15em)
          #align(center + horizon)[#text(font: serif, size: 7.8pt, fill: ink)[#t] #parbreak() #text(font: serif, size: 6.6pt, style: "italic", fill: slate)[#en21.at(wi * 7 + d)]]]))
  ]
]

#cotloi("Mục tiêu không phải tô đủ 21 ô. Mục tiêu là sau ba tuần, con bắt đầu kể với ba mẹ nhiều hơn một câu.")

// ------------------------------------------------ KHI CẦN NGƯỜI GIÚP
#accent.update(palette.at(5))
#heading(level: 1, numbering: none)[Khi Thương Thôi Chưa Đủ: Tìm Ai Giúp]

#para1("Có những việc tình thương của ba mẹ không thay được chuyên môn, cũng như ba mẹ không tự bó được cái tay gãy của con. Tìm người giúp đúng lúc là một việc làm của người thương con và có trách nhiệm.", en: "Some things a parent's love cannot replace expertise for, just as you cannot set your child's broken arm yourself. Finding help at the right time is what a loving and responsible parent does.")

#listbox1("NHỮNG CÁNH CỬA BA MẸ CÓ THỂ GÕ", teal, rgb("F0FDFA"), (
  "Tổng đài 111: tổng đài quốc gia bảo vệ trẻ em, miễn phí, hoạt động suốt ngày đêm. Gọi khi con bị bạo lực, xâm hại, bắt nạt, đe dọa, tống tiền, hoặc khi ba mẹ cần được hướng dẫn nên làm gì.",
  "Cấp cứu 115 hoặc bệnh viện gần nhất: khi con đã tự gây thương tích, uống thuốc, hoặc có kế hoạch tự hại cụ thể. Không chờ.",
  "Khoa tâm lý, khoa tâm thần nhi ở bệnh viện nhi và bệnh viện tâm thần: khi con buồn bã, lo âu, mất ngủ, bỏ ăn kéo dài quá hai tuần; tự làm đau bản thân; nghi rối loạn ăn uống; lệ thuộc game hoặc chất gây nghiện.",
  "Giáo viên chủ nhiệm, phòng tham vấn học đường, ban giám hiệu: khi chuyện liên quan tới trường lớp, bạn bè, bắt nạt. Mang theo sự việc cụ thể và đề nghị một kế hoạch.",
  "Công an: khi có dấu hiệu phạm pháp với con như xâm hại, đe dọa phát tán hình ảnh, lừa đảo, ép buộc. Giữ nguyên bằng chứng, không tự thương lượng với kẻ đe dọa.",
  "Cho chính ba mẹ: một người bạn, người thân tin cậy, hoặc chuyên viên tham vấn. Ba mẹ cũng cần một chỗ để nói.",
), mark: sym.triangle.filled.small.r, en: (
  "Hotline 111: Vietnam's national child protection hotline, free, day and night. Call for violence, abuse, bullying, threats, blackmail, or when you need guidance on what to do.",
  "Emergency 115 or the nearest hospital: when your child has hurt themselves, swallowed pills, or has a specific plan to self-harm. Do not wait.",
  "Psychology or child psychiatry departments of children's and psychiatric hospitals: sadness, anxiety, sleeplessness or loss of appetite lasting over two weeks; self-harm; suspected eating disorder; dependence on games or substances.",
  "Form teacher, school counselling, school leadership: for matters of school, friends, bullying. Bring specific facts and ask for a plan.",
  "Police: when there are signs of crime against your child: abuse, threats to share images, fraud, coercion. Keep the evidence; do not negotiate with the threatener yourself.",
  "For parents too: a trusted friend, relative, or counsellor. You also need somewhere to talk.",
))

#cotloi("Đưa con đi tìm người giúp không phải là ba mẹ đã thất bại. Đó là ba mẹ đang làm đúng việc của mình.", en: "Taking your child to find help is not parents failing. It is parents doing their job.")
