#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate chapter .tex files for Quyển 19-23 from quote data."""

import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def section_tex(quote_vi, quote_en, story_vi, story_en, baihoc_vi, baihoc_en, eng_short, q1_vi, q1_en, q2_vi, q2_en):
    return r"""
\section{%s}
\begin{truyen}{%s}{%s}
\chuhoa{C}{%s}
\textit{(%s)}
\end{truyen}

\begin{baihoc}
%s
\textit{(%s)}
\end{baihoc}

\begin{ghinhoanh}
\textbf{Short English to remember:}

%s

\end{ghinhoanh}

\begin{tuhocnhanh}
1. %s \textit{%s}

2. %s \textit{%s}
\end{tuhocnhanh}
\ngancach
""" % (
        quote_vi.replace('\n', ' '),
        quote_vi[:60] + ('...' if len(quote_vi) > 60 else ''),
        quote_en.replace('\n', ' ')[:50],
        story_vi,
        story_en,
        baihoc_vi,
        baihoc_en,
        eng_short,
        q1_vi, q1_en,
        q2_vi, q2_en,
    )

def make_chapter(book_dir, ch_num, title_vi, title_en, sections):
    out = []
    out.append(r"\chapter{%s}" % title_vi)
    out.append(r"\markboth{%s}{%s}" % (title_vi, title_en))
    out.append("")
    for s in sections:
        out.append(section_tex(
            s["quote_vi"], s.get("quote_en", s["quote_vi"]),
            s["story_vi"], s["story_en"],
            s["baihoc_vi"], s["baihoc_en"],
            s["eng_short"],
            s["q1_vi"], s["q1_en"],
            s["q2_vi"], s["q2_en"],
        ))
    path = os.path.join(book_dir, "chapters", "ch%02d.tex" % ch_num)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print("Wrote", path)

def build_section(quote_vi, quote_en, story_vi, story_en, baihoc_vi, baihoc_en, eng_short, q1_vi, q1_en, q2_vi, q2_en):
    return {
        "quote_vi": quote_vi,
        "quote_en": quote_en,
        "story_vi": story_vi,
        "story_en": story_en,
        "baihoc_vi": baihoc_vi,
        "baihoc_en": baihoc_en,
        "eng_short": eng_short,
        "q1_vi": q1_vi,
        "q1_en": q1_en,
        "q2_vi": q2_vi,
        "q2_en": q2_en,
    }

def simple_section(quote_vi, theme_en, theme_vi="suy nghĩ"):
    """One paragraph story from quote."""
    story_vi = "âu thầy nói câu ấy. Cả lớp im lặng — không ai nói, mỗi người đang nghĩ về điều vừa nghe."
    story_en = "The teacher said that. The class fell silent — no one spoke; everyone was thinking about what they had just heard."
    baihoc_vi = "Im lặng sau câu nói đúng lúc là dấu hiệu của tư duy."
    baihoc_en = "Silence after the right sentence is a sign of thinking."
    eng_short = "Some sentences make the whole class think in silence."
    return build_section(
        quote_vi, theme_en, story_vi, story_en,
        baihoc_vi, baihoc_en, eng_short,
        "Câu này khiến em nghĩ đến điều gì?", "What does this make you think of?",
        "Em có thể dùng câu này trong tình huống nào?", "When could you use this sentence?",
    )

def q19_section(quote_vi, quote_en, idx):
    q = quote_vi.lower()

    def pick(items):
        return items[idx % len(items)]

    if "câu hỏi" in q or "hỏi" in q:
        story_vi, story_en = pick([
            (
                "âu thầy viết câu ấy lên bảng rồi lùi lại. Mấy cánh tay đang định giơ lên chậm rãi hạ xuống, vì cả lớp nhận ra muốn trả lời cho trúng thì trước hết phải hiểu mình đang được hỏi điều gì.",
                "The teacher wrote that sentence on the board and stepped back. A few hands that were about to rise slowly came down, because the class realized that to answer well, they first had to understand what was being asked.",
            ),
            (
                "âu hỏi vừa dứt, phòng học yên đi. Không ai bị ép phải nói ngay; sự im lặng ấy là lúc từng bạn tự lật lại suy nghĩ của mình trước khi mở lời.",
                "As soon as the question ended, the room grew quiet. No one was forced to answer at once; that silence was the moment each student turned their own thoughts over before speaking.",
            ),
            (
                "âu thầy nói nghe rất ngắn, nhưng nó làm cả lớp chậm lại. Có khi một câu hỏi hay không cho đáp án; nó mở ra con đường để người học tự tìm đáp án.",
                "What the teacher said sounded brief, but it slowed the whole class down. Sometimes a good question gives no answer; it opens a path for learners to find one themselves.",
            ),
        ])
        baihoc_vi, baihoc_en = pick([
            ("Một câu hỏi tốt buộc người học đi chậm lại để nghĩ sâu hơn.", "A good question makes learners slow down and think more deeply."),
            ("Hiểu đúng câu hỏi thường quan trọng hơn trả lời thật nhanh.", "Understanding the question is often more important than answering quickly."),
            ("Câu hỏi đúng không đóng lại buổi học; nó mở buổi học ra.", "The right question does not close a lesson; it opens it."),
        ])
        eng_short = pick([
            "Good questions create thoughtful silence.",
            "Do not race to answer; learn to understand first.",
            "A strong question opens the mind before the mouth.",
        ])
        q1_vi, q1_en = "Câu hỏi nào trong mục này khiến em phải nghĩ lại cách học của mình?", "Which question in this section makes you rethink the way you study?"
        q2_vi, q2_en = "Nếu em hỏi lại câu này theo cách của mình, em sẽ hỏi thế nào?", "If you rewrote this question in your own words, how would you ask it?"
    elif "lớp học" in q or "cả lớp" in q or "trong lớp" in q or "phòng" in q:
        story_vi, story_en = pick([
            (
                "âu nói ấy không nhắm vào một ai, nhưng cả lớp cùng nghe thấy mình trong đó. Tiếng quạt, tiếng lật vở bỗng rõ hơn, như thể phòng học vừa chuyển từ ồn ào sang một kiểu làm việc sâu hơn.",
                "The sentence was not aimed at anyone in particular, yet the whole class heard themselves in it. The fan, the turning pages, suddenly sounded clearer, as if the room had shifted from noise into a deeper kind of work.",
            ),
            (
                "âu thầy nói xong, lớp không còn chen nhau trả lời nữa. Chính khoảnh khắc không ai lên tiếng đã làm buổi học có chiều sâu hơn bất kỳ lời giảng dài nào.",
                "When the teacher finished speaking, the class stopped rushing to respond. That moment when no one spoke gave the lesson more depth than any long explanation could.",
            ),
            (
                "âu ấy đi qua căn phòng rất nhẹ, nhưng để lại một trật tự khác. Các bạn nhìn nhau, rồi nhìn vào vở, như hiểu rằng một lớp học tốt không chỉ biết nói mà còn biết dừng lại để nghĩ cùng nhau.",
                "The sentence passed through the room gently, but it left behind a different order. Students looked at one another, then back at their notebooks, as if realizing that a good class knows not only how to speak, but also how to pause and think together.",
            ),
        ])
        baihoc_vi, baihoc_en = pick([
            ("Chiều sâu của lớp học nhiều khi được tạo ra từ những phút cả lớp cùng suy nghĩ.", "A classroom's depth is often built in the moments when everyone thinks together."),
            ("Không khí học tập tốt không nằm ở chỗ ồn hay im, mà ở chỗ sự im lặng có ý nghĩa.", "A strong learning atmosphere is not about being loud or quiet, but about whether the silence has meaning."),
            ("Một lớp học trưởng thành biết tôn trọng khoảnh khắc suy nghĩ chung.", "A mature class knows how to respect moments of shared reflection."),
        ])
        eng_short = pick([
            "A good class knows when silence is doing the work.",
            "Thoughtful rooms are not empty; they are focused.",
            "Shared silence can deepen a whole lesson.",
        ])
        q1_vi, q1_en = "Lớp học của em thường im lặng theo kiểu suy nghĩ hay theo kiểu ngại nói?", "Does your class usually become quiet because people are thinking or because they are afraid to speak?"
        q2_vi, q2_en = "Em có thể làm gì để một khoảnh khắc im lặng trong lớp trở nên có ích hơn?", "What could you do to make a quiet moment in class more useful?"
    elif "lắng nghe" in q or "nghe" in q or "nói" in q or "lời" in q or "trả lời" in q:
        story_vi, story_en = pick([
            (
                "âu ấy được nói ra đúng lúc một bạn đang định chen lời bạn khác. Cả lớp chững lại; ai cũng hiểu nói hay không nằm ở nói nhiều, mà ở chỗ lời nói đã đi qua suy nghĩ và lắng nghe chưa.",
                "The sentence came just as one student was about to cut another off. The class paused, and everyone understood that speaking well is not about speaking often, but about whether your words have passed through thought and listening.",
            ),
            (
                "âu thầy nói không hề nặng, nhưng đủ để những tiếng đáp lời vội vàng chậm lại. Từ sự chậm lại đó, nhiều bạn bắt đầu nghe kỹ hơn chính mình và người đối diện.",
                "The teacher's words were not harsh, but they were enough to slow down the rushed replies. From that slowing down, many students began listening more carefully to themselves and to the person in front of them.",
            ),
            (
                "âu nói ấy khiến vài bạn đang định trả lời ngay phải dừng một nhịp. Khi lời nói không còn chạy trước suy nghĩ, cuộc trò chuyện trong lớp bỗng trở nên tử tế hơn.",
                "That sentence made a few students who were about to answer immediately pause for a moment. When speech no longer ran ahead of thought, the conversation in class became kinder.",
            ),
        ])
        baihoc_vi, baihoc_en = pick([
            ("Lắng nghe và suy nghĩ là điều làm cho lời nói có trọng lượng.", "Listening and reflection are what give words their weight."),
            ("Tôn trọng người nghe bắt đầu từ việc không để miệng chạy trước đầu óc.", "Respect for the listener begins when the mouth does not run ahead of the mind."),
            ("Một câu trả lời chậm nhưng chín thường đáng giá hơn một câu trả lời nhanh mà rỗng.", "A slow but thoughtful answer is often worth more than a fast and empty one."),
        ])
        eng_short = pick([
            "Words matter more after listening.",
            "Think first, then let the words come.",
            "Listening gives speech its weight.",
        ])
        q1_vi, q1_en = "Trong lúc tranh luận hay phát biểu, em hay vội nói hay vội nghe?", "When you discuss or respond, do you rush to speak or rush to listen?"
        q2_vi, q2_en = "Một câu trả lời của em sẽ khác đi thế nào nếu em dừng lại thêm mười giây?", "How would one of your answers change if you paused for ten more seconds?"
    elif "thời gian" in q or "không gian" in q or "khoảnh khắc" in q or "một phút" in q:
        story_vi, story_en = pick([
            (
                "âu ấy làm cả lớp chậm lại đúng một nhịp. Không ai thấy phí thời gian, vì chính khoảng dừng ngắn đó giúp mỗi người sắp xếp lại điều mình đang nghĩ.",
                "The sentence slowed the whole class down by just a beat. No one felt the time was wasted, because that brief pause helped everyone arrange their thoughts.",
            ),
            (
                "âu thầy nói xong rồi để yên vài giây, không lấp khoảng trống bằng lời khác. Nhờ vậy, sự im lặng không còn đáng ngại; nó trở thành không gian để điều quan trọng kịp xuất hiện.",
                "The teacher finished speaking and then left a few seconds untouched, without filling the gap with more words. Because of that, silence no longer felt awkward; it became the space where something important could appear.",
            ),
            (
                "âu ấy ngắn, nhưng có sức giữ cả lớp lại. Trong khoảnh khắc không ai nói, nhiều bạn nhận ra suy nghĩ cần chỗ đứng riêng chứ không thể lớn lên giữa sự vội vã.",
                "The sentence was short, but it held the class in place. In the moment when no one spoke, many students realized that thought needs room of its own and cannot grow in haste.",
            ),
        ])
        baihoc_vi, baihoc_en = pick([
            ("Tư duy sâu cần khoảng dừng, giống như hơi thở cần nhịp.", "Deep thinking needs pauses, just as breathing needs rhythm."),
            ("Không phải khoảng trống nào cũng vô ích; có khoảng trống đang làm việc cho suy nghĩ.", "Not every gap is empty; some gaps are working for thought."),
            ("Cho mình thời gian nghĩ là một cách học nghiêm túc.", "Giving yourself time to think is a serious form of learning."),
        ])
        eng_short = pick([
            "Silence gives thought room to grow.",
            "A pause is not wasted when the mind is working.",
            "Deep thought needs space and time.",
        ])
        q1_vi, q1_en = "Em thường có cho mình đủ thời gian nghĩ trước khi nói hay nộp bài không?", "Do you usually give yourself enough time to think before speaking or submitting work?"
        q2_vi, q2_en = "Một khoảng dừng ngắn có thể giúp em tốt hơn ở việc nào?", "In which task could a short pause help you do better?"
    else:
        story_vi, story_en = pick([
            (
                "âu thầy nói không dài, nhưng nó chạm đúng chỗ khiến nhiều bạn phải nhìn lại mình. Có khi bài học thật sự không đến từ việc nghe thêm, mà từ việc tự đối diện với điều mình vừa nghe.",
                "The teacher's sentence was not long, but it touched exactly the place that made many students look back at themselves. Sometimes the real lesson does not come from hearing more, but from facing what you have just heard.",
            ),
            (
                "âu ấy đi vào vở rất nhanh, nhưng ở lại trong đầu lâu hơn. Mấy bạn cuối lớp thôi viết một lát, vì nhận ra điều đáng nhớ nhất không phải là chép kịp, mà là hiểu kịp.",
                "The sentence entered notebooks quickly, but stayed in the mind longer. Even the students in the back stopped writing for a moment, realizing that what matters most is not copying fast enough, but understanding in time.",
            ),
            (
                "âu thầy nói xong không tạo ra tiếng ồ lên, chỉ tạo ra một sự lặng đi rất thật. Chính lúc ấy, mỗi người bắt đầu có cuộc đối thoại riêng với suy nghĩ của mình.",
                "What the teacher said did not produce a burst of reaction, only a very real stillness. At that moment, each student began a private conversation with their own thoughts.",
            ),
        ])
        baihoc_vi, baihoc_en = pick([
            ("Điều làm ta nhớ lâu thường không phải âm lượng lớn, mà là độ sâu của ý nghĩ.", "What stays with us is often not loudness, but depth."),
            ("Một câu nói đáng học là câu khiến người nghe phải tự nghĩ tiếp.", "A sentence worth learning from is one that makes the listener continue thinking."),
            ("Sự im lặng có ý nghĩa cho thấy bài học đã chạm vào bên trong.", "Meaningful silence shows that a lesson has reached something inside."),
        ])
        eng_short = pick([
            "The best sentences keep working after they end.",
            "A deep line keeps the mind awake.",
            "Silence often means reflection has started.",
        ])
        q1_vi, q1_en = "Điều gì trong câu này chạm đúng vào trải nghiệm học tập của em?", "What in this sentence connects most strongly with your own learning experience?"
        q2_vi, q2_en = "Nếu giữ lại một ý duy nhất từ câu này, em sẽ giữ ý nào?", "If you kept only one idea from this sentence, which idea would you keep?"

    return build_section(
        quote_vi,
        quote_en,
        story_vi,
        story_en,
        baihoc_vi,
        baihoc_en,
        eng_short,
        q1_vi,
        q1_en,
        q2_vi,
        q2_en,
    )

def section_humorous(quote_vi, quote_en_short):
    story_vi = "âu thầy nói xong, cả lớp cười — nhưng cười xong nhiều em chợt nghĩ."
    story_en = "The teacher said it; the class laughed — but after the laugh, many suddenly thought."
    baihoc_vi = "Cười xong nhớ mới là hay."
    baihoc_en = "Remembering after the laugh is what counts."
    return build_section(quote_vi, quote_en_short, story_vi, story_en, baihoc_vi, baihoc_en,
        "Laugh first, then think.", "Câu này khiến em cười vì sao?", "Why does this make you laugh?",
        "Sau khi cười em nghĩ ra điều gì?", "What do you think after laughing?")

def section_giat_minh(quote_vi, quote_en_short):
    story_vi = "âu thầy nói thẳng. Một vài em im lặng — không phải vì sợ, mà vì giật mình."
    story_en = "The teacher said it straight. Some fell silent — not from fear, but from being startled."
    baihoc_vi = "Giật mình một lần có thể đổi hướng."
    baihoc_en = "One wake-up moment can change your direction."
    return build_section(quote_vi, quote_en_short, story_vi, story_en, baihoc_vi, baihoc_en,
        "Wake up before you pay the price.", "Câu này khiến em giật mình thế nào?", "How does this startle you?",
        "Em sẽ làm gì khác đi sau khi đọc?", "What will you do differently after reading?")

def section_nan_hoc(quote_vi, quote_en_short):
    story_vi = "âu thầy nói nhẹ nhàng, không trách. Em ấy ngẩng đầu lên — như nghe được điều cần nghe."
    story_en = "The teacher said it gently, without blame. That student looked up — as if hearing what they needed."
    baihoc_vi = "Nản một lúc không sao; đứng dậy mới quan trọng."
    baihoc_en = "Feeling down for a while is okay; getting back up is what matters."
    return build_section(quote_vi, quote_en_short, story_vi, story_en, baihoc_vi, baihoc_en,
        "Support when they're down, not blame.", "Câu này giúp em đứng dậy thế nào?", "How does this help you get up?",
        "Em muốn nhớ câu này khi nào?", "When do you want to remember this?")

def section_cuoi_nam(quote_vi, quote_en_short):
    story_vi = "âu thầy nói trước khi cả lớp ra về. Nhiều em im lặng, có em rơi nước mắt."
    story_en = "The teacher said it before everyone left. Many were silent; some had tears."
    baihoc_vi = "Những lời cuối năm ở lại lâu hơn điểm số."
    baihoc_en = "Year-end words stay longer than grades."
    return build_section(quote_vi, quote_en_short, story_vi, story_en, baihoc_vi, baihoc_en,
        "Year-end words touch the heart.", "Câu này em muốn giữ lại thế nào?", "How do you want to keep this?",
        "Em sẽ nhớ thầy cô qua câu nào?", "Which sentence will remind you of your teacher?")

if __name__ == "__main__":
    # Quyển 19: 100 câu - 10 chương x 10
    q19_dir = os.path.join(BASE, "truyen-tich-cam-hung-quyen-19")
    quotes_19 = [
        "Không phải ai nói nhiều cũng là người hiểu nhiều.",
        "Im lặng đôi khi là câu trả lời hay nhất.",
        "Em đang chạy theo điểm hay đang chạy theo hiểu?",
        "Câu hỏi quan trọng hơn câu trả lời — vì nó mở đường.",
        "Người thông minh nhất trong phòng thường là người im lặng lắng nghe.",
        "Sách không thay em nghĩ; sách mời em nghĩ.",
        "Nếu em không đặt câu hỏi, em đang tin tất cả.",
        "Điều em sợ nói ra thường là điều em cần nói nhất.",
        "Học không phải để trả lời đúng — học để biết hỏi đúng.",
        "Một phút im lặng suy nghĩ đáng giá hơn mười phút nói mà không nghĩ.",
        "Tri thức làm em nổi bật; đặt câu hỏi làm em trưởng thành.",
        "Em không cần đồng ý với thầy — em cần nghĩ về điều thầy nói.",
        "Lớp học hay là lớp học biết im lặng khi cần.",
        "Đừng vội trả lời; hãy vội hiểu câu hỏi.",
        "Người giỏi không phải người trả lời nhanh nhất.",
        "Suy nghĩ trước khi nói — đó mới là tôn trọng người nghe.",
        "Không có câu hỏi ngu — chỉ có câu hỏi chưa được hỏi.",
        "Khi em im lặng, em đang cho mình thời gian nghĩ.",
        "Điều quan trọng không phải em nói gì mà em nghĩ gì trước khi nói.",
        "Cả lớp ồn có thể là cả lớp chưa nghĩ.",
        "Thầy không cần em đồng ý; thầy cần em suy nghĩ.",
        "Một câu hỏi hay có thể thay đổi cả buổi học.",
        "Im lặng không phải trống rỗng — im lặng là nơi ý tưởng ra đời.",
        "Em học được gì khi em im lặng lắng nghe?",
        "Đừng sợ im lặng; sợ nói mà không nghĩ.",
        "Người hiểu thường ít nói — vì họ biết lời có trọng lượng.",
        "Lớp học đáng nhớ là lớp học có những khoảnh khắc im lặng đầy suy nghĩ.",
        "Câu trả lời đúng có thể sai thời điểm; câu hỏi đúng luôn đúng lúc.",
        "Suy nghĩ là thứ em làm khi em không vội trả lời.",
        "Thầy nói xong; giờ đến lượt em nghĩ.",
        "Không ai có thể nghĩ hộ em — im lặng là lúc em nghĩ cho mình.",
        "Em có quyền im lặng — và quyền đó rất quý.",
        "Nói ít, nghĩ nhiều — đó là cách người lớn dùng lời.",
        "Khi cả lớp im, có thể đang có điều quan trọng được suy nghĩ.",
        "Điều em giữ trong im lặng đôi khi mạnh hơn điều em nói ra.",
        "Học cách im lặng cũng là học.",
        "Một khoảnh khắc im lặng có thể đáng giá cả trang sách.",
        "Thầy chờ không phải vì thầy không biết — thầy chờ để em có thời gian nghĩ.",
        "Câu nói khiến em im lặng là câu nói đáng nhớ.",
        "Im lặng sau câu hỏi là dấu hiệu lớp đang làm việc.",
        "Đừng lấp đầy im lặng bằng lời vô nghĩa.",
        "Suy nghĩ cần thời gian — và im lặng cho em thời gian đó.",
        "Người biết lắng nghe thường là người nói có trọng lượng sau này.",
        "Lớp học tốt không phải lớp ồn nhất hay im nhất — mà lớp biết khi nào nên im.",
        "Em không cần trả lời ngay; em cần nghĩ trước.",
        "Im lặng là ngôn ngữ của suy nghĩ sâu.",
        "Câu hỏi của thầy không phải để em trả lời nhanh — mà để em nghĩ kỹ.",
        "Khi em im lặng, em đang tôn trọng chính suy nghĩ của mình.",
        "Nói trước khi nghĩ là đánh mất cơ hội hiểu.",
        "Im lặng không phải đồng nghĩa với không biết — đôi khi là đang tìm câu trả lời đúng.",
        "Thầy thích những khoảnh khắc cả lớp im — vì đó là lúc các em đang học thật.",
        "Suy nghĩ trước khi nói là món quà em tặng cho người nghe.",
        "Không phải lúc nào cũng cần lời — có lúc chỉ cần im lặng và nghĩ.",
        "Câu nói khiến em dừng lại là câu nói đáng giữ.",
        "Im lặng cho em không gian để hỏi chính mình.",
        "Người giỏi tranh luận không phải người nói nhiều — mà người biết khi nào im.",
        "Lớp học có chiều sâu là lớp học không sợ im lặng.",
        "Em có thể không nói gì — nhưng em vẫn có thể nghĩ rất nhiều.",
        "Im lặng là một dạng câu trả lời.",
        "Thầy không cần em trả lời đúng ngay — thầy cần em nghĩ đúng.",
        "Khoảnh khắc im lặng sau câu nói quan trọng là khoảnh khắc học tập.",
        "Suy nghĩ là công việc quan trọng nhất trong lớp — và im lặng là không gian của nó.",
        "Đừng nghĩ im lặng là thất bại của giao tiếp; đôi khi đó là đỉnh cao.",
        "Câu nói khiến em phải dừng và nghĩ — đó mới là câu đáng học.",
        "Im lặng không làm em kém thông minh — nói mà không nghĩ mới làm.",
        "Lắng nghe và im lặng là hai kỹ năng của người học giỏi.",
        "Khi em im lặng, em đang cho mình quyền suy nghĩ.",
        "Thầy nói ít không phải vì thầy không có gì để nói — mà để các em có thời gian nghĩ.",
        "Lớp học đáng nhớ có những khoảnh khắc không ai nói — nhưng ai cũng nghĩ.",
        "Suy nghĩ không cần lời — nhưng cần im lặng.",
        "Em không bắt buộc phải trả lời ngay; em có quyền nghĩ trước.",
        "Im lặng là khoảng trống để ý tưởng lớn lên.",
        "Câu hỏi hay thường được theo sau bởi im lặng — vì mọi người đang nghĩ.",
        "Người biết im lặng đúng lúc thường là người nói có sức nặng.",
        "Học không chỉ là nghe và trả lời — học còn là im lặng và suy nghĩ.",
        "Im lặng không phải từ chối tham gia — mà là tham gia bằng cách nghĩ.",
        "Thầy chấp nhận im lặng — vì thầy biết suy nghĩ cần thời gian.",
        "Điều em nghĩ trong im lặng có thể quan trọng hơn điều em nói trong ồn ào.",
        "Lớp học tốt là nơi im lặng được tôn trọng.",
        "Suy nghĩ sâu thường bắt đầu từ một khoảnh khắc im lặng.",
        "Em có thể trả lời sau — nhưng em không thể nghĩ thay.",
        "Im lặng là cách em nói: tôi đang nghĩ.",
        "Câu nói khiến cả lớp im là câu nói có sức nặng.",
        "Không phải lúc nào nói nhiều cũng là đóng góp — đôi khi im lặng mới là.",
        "Người học thật là người biết dùng im lặng để suy nghĩ.",
        "Im lặng cho em cơ hội nghe chính mình.",
        "Thầy không sợ im lặng — thầy sợ các em nói mà không nghĩ.",
        "Khoảnh khắc im lặng trong lớp là khoảnh khắc vàng.",
        "Suy nghĩ không ồn ào — nhưng nó thay đổi con người.",
        "Em có quyền không trả lời ngay — và dùng quyền đó để nghĩ.",
        "Im lặng là ngôn ngữ trước khi có lời.",
        "Câu nói đáng nhớ thường được theo sau bởi im lặng đáng nhớ.",
        "Lớp học có văn hóa im lặng là lớp học có chiều sâu.",
        "Đừng vội lấp im lặng — hãy để nó làm việc.",
        "Suy nghĩ cần không gian — và im lặng tạo không gian đó.",
        "Người trưởng thành biết khi nào nên im lặng và nghĩ.",
        "Im lặng không phải thiếu ý kiến — mà đang hình thành ý kiến.",
        "Thầy tin rằng sau im lặng, các em sẽ có câu trả lời tốt hơn.",
        "Câu nói khiến em im lặng là câu nói thành công.",
        "Học từ im lặng cũng là một kỹ năng.",
        "Im lặng là món quà em tặng cho suy nghĩ của chính mình.",
        "Lớp học không chỉ là nơi nói — mà còn là nơi im lặng và nghĩ.",
        "Suy nghĩ trước khi nói — và đừng sợ im lặng khi đang nghĩ.",
        "Em không cần phải có câu trả lời ngay — em cần có thời gian nghĩ.",
        "Im lặng đúng lúc là trí tuệ.",
        "Câu nói cuối cùng trong một buổi học đôi khi là im lặng.",
        "Thầy tôn trọng im lặng của em — vì đó là lúc em đang làm việc thật sự.",
        "Lớp học tốt có những khoảnh khắc không ai nói — và ai cũng hiểu.",
        "Suy nghĩ là hành động — và im lặng là không gian cho hành động đó.",
        "Đừng đánh giá thấp sức mạnh của im lặng trong học tập.",
        "Im lặng không làm em vô hình — nó làm em có chiều sâu.",
        "Câu nói khiến em phải nghĩ mới là câu nói đáng học.",
        "Người giỏi nhất trong phòng đôi khi là người im lặng lâu nhất.",
        "Thầy để cả lớp im không phải vì quên — mà vì đang chờ các em nghĩ.",
        "Im lặng là câu trả lời đầu tiên của suy nghĩ.",
        "Lớp học đáng nhớ có đủ cả nói và im — và cả hai đều quan trọng.",
        "Suy nghĩ không cần micro — nó cần im lặng.",
        "Em có thể nói ít — nhưng nghĩ nhiều; đó mới là học.",
    ]
    # Pad to 100
    while len(quotes_19) < 100:
        quotes_19.append("Im lặng đôi khi là câu trả lời hay nhất — và suy nghĩ là công việc quan trọng nhất.")
    quotes_19 = quotes_19[:100]
    quotes_19_en = [
        "Not everyone who talks a lot understands a lot.",
        "Silence is sometimes the best answer.",
        "Are you chasing grades or understanding?",
        "A question matters more than an answer, because it opens the way.",
        "The smartest person in the room is often the one who listens in silence.",
        "Books do not think for you; they invite you to think.",
        "If you do not ask questions, you are believing everything.",
        "What you are afraid to say is often what you most need to say.",
        "Learning is not about giving the right answer; it is about asking the right question.",
        "One quiet minute of reflection is worth more than ten minutes of thoughtless talk.",
        "Knowledge makes you stand out; asking questions makes you grow up.",
        "You do not need to agree with the teacher; you need to think about what the teacher says.",
        "A good classroom is one that knows when to be quiet.",
        "Do not rush to answer; rush to understand the question.",
        "The capable student is not the one who answers fastest.",
        "Thinking before speaking is how you respect the listener.",
        "There are no stupid questions, only questions that have not been asked.",
        "When you are silent, you are giving yourself time to think.",
        "What matters is not what you say, but what you think before you speak.",
        "A noisy class may just be a class that has not started thinking.",
        "The teacher does not need your agreement; the teacher needs your thinking.",
        "One good question can change an entire lesson.",
        "Silence is not emptiness; it is where ideas are born.",
        "What do you learn when you listen in silence?",
        "Do not fear silence; fear speaking without thinking.",
        "People who understand often speak less, because they know words carry weight.",
        "A memorable class is a class with moments of thoughtful silence.",
        "A correct answer can come at the wrong time; a good question is always timely.",
        "Thinking is what you do when you do not rush to answer.",
        "The teacher has finished speaking; now it is your turn to think.",
        "No one can think on your behalf; silence is when you think for yourself.",
        "You have the right to remain silent, and that right is precious.",
        "Speak less, think more; that is how adults use words.",
        "When the whole class falls quiet, something important may be being considered.",
        "What you keep in silence is sometimes stronger than what you say aloud.",
        "Learning how to be quiet is also learning.",
        "A moment of silence can be worth a whole page of text.",
        "The teacher waits not because the teacher does not know, but because you need time to think.",
        "The sentence that makes you fall silent is the sentence you remember.",
        "Silence after a question shows that the class is at work.",
        "Do not fill silence with meaningless words.",
        "Thinking takes time, and silence gives you that time.",
        "Those who know how to listen often become the people whose words matter later.",
        "A good class is not the loudest or the quietest, but the one that knows when to be quiet.",
        "You do not need to answer at once; you need to think first.",
        "Silence is the language of deep thought.",
        "The teacher's question is not for a quick answer; it is for careful thought.",
        "When you are silent, you are respecting your own thinking.",
        "Speaking before thinking means losing the chance to understand.",
        "Silence does not mean ignorance; sometimes it means searching for the right answer.",
        "The teacher values the moments when the whole class is quiet, because that is when real learning is happening.",
        "Thinking before speaking is a gift you give the listener.",
        "Words are not always needed; sometimes silence and thought are enough.",
        "The sentence that makes you stop is the sentence worth keeping.",
        "Silence gives you room to question yourself.",
        "A good debater is not the one who talks the most, but the one who knows when to be quiet.",
        "A deep classroom is a classroom unafraid of silence.",
        "You may say nothing and still be thinking a great deal.",
        "Silence is a kind of answer.",
        "The teacher does not need an immediate correct answer; the teacher needs correct thinking.",
        "The quiet moment after an important sentence is a moment of learning.",
        "Thinking is the most important work in class, and silence is the space where it happens.",
        "Do not mistake silence for failed communication; sometimes it is its highest form.",
        "The sentence that makes you stop and think is the sentence worth learning from.",
        "Silence does not make you less intelligent; speaking without thinking does.",
        "Listening and silence are two skills of a strong learner.",
        "When you are silent, you are giving yourself the right to think.",
        "The teacher speaks little not because there is nothing to say, but to give you time to think.",
        "A memorable class has moments when no one speaks, but everyone is thinking.",
        "Thinking needs no words, but it does need silence.",
        "You are not required to answer immediately; you have the right to think first.",
        "Silence is the empty space where ideas grow.",
        "A good question is often followed by silence, because everyone is thinking.",
        "A person who knows how to be quiet at the right time often speaks with weight.",
        "Learning is not only listening and answering; it is also being quiet and thinking.",
        "Silence is not refusing to take part; it is taking part by thinking.",
        "The teacher accepts silence because thinking takes time.",
        "What you think in silence may matter more than what you say in noise.",
        "A good classroom is a place where silence is respected.",
        "Deep thinking often begins with a quiet moment.",
        "You can answer later, but no one can think in your place.",
        "Silence is how you say: I am thinking.",
        "The sentence that silences a class is a sentence with weight.",
        "Talking a lot is not always a contribution; sometimes silence is.",
        "A real learner knows how to use silence for thinking.",
        "Silence gives you a chance to hear yourself.",
        "The teacher is not afraid of silence; the teacher is afraid you will speak without thinking.",
        "A quiet moment in class is a golden moment.",
        "Thought is not noisy, but it changes people.",
        "You have the right not to answer immediately, and to use that right to think.",
        "Silence is the language before words.",
        "A memorable sentence is often followed by memorable silence.",
        "A classroom with a culture of silence is a classroom with depth.",
        "Do not rush to fill silence; let it do its work.",
        "Thought needs space, and silence creates that space.",
        "A mature person knows when to be quiet and think.",
        "Silence does not mean having no opinion; it means an opinion is taking shape.",
        "The teacher trusts that after silence, you will have a better answer.",
        "A sentence that makes you silent is a successful sentence.",
        "Learning from silence is also a skill.",
    ]

    ch_titles_19 = [
        ("Im lặng và suy nghĩ", "Silence and Thinking"),
        ("Câu hỏi và câu trả lời", "Questions and Answers"),
        ("Lắng nghe và nói", "Listening and Speaking"),
        ("Thời gian và không gian", "Time and Space"),
        ("Lớp học và chiều sâu", "Classroom and Depth"),
        ("Tôn trọng im lặng", "Respecting Silence"),
        ("Suy nghĩ trước khi nói", "Think Before You Speak"),
        ("Quyền im lặng", "The Right to Silence"),
        ("Khoảnh khắc vàng", "Golden Moments"),
        ("Học từ im lặng", "Learning from Silence"),
    ]
    for ch in range(10):
        sections = []
        for i in range(10):
            idx = ch * 10 + i
            q = quotes_19[idx]
            sections.append(q19_section(q, quotes_19_en[idx], idx))
        make_chapter(q19_dir, ch + 1, ch_titles_19[ch][0], ch_titles_19[ch][1], sections)

    print("Done Q19.")

    # Quyển 20: 50 câu hài hước sâu sắc — 5 chương x 10
    q20_dir = os.path.join(BASE, "truyen-tich-cam-hung-quyen-20")
    quotes_20 = [
        "Thầy không giận — thầy chỉ đang thử xem trần nhà có bền không.",
        "Bài này khó đến mức thầy làm cũng phải đọc lại.",
        "Em không sai — em chỉ đang sáng tạo ra đáp án mới.",
        "Lớp mình học xong chắc thành tiến sĩ… tiến sĩ ngủ gật.",
        "Thầy biết các em yêu thầy — nhưng yêu bài tập một chút nữa nhé.",
        "Điểm này không phải để buồn — mà để biết mình còn chỗ mà leo.",
        "Em quên vở à? Không sao, lần sau nhớ mang theo cái đầu.",
        "Thầy không so em với bạn — thầy chỉ mong em so với chính em hôm qua.",
        "Môn này không khó — nó chỉ không tự vào đầu mình.",
        "Các em im đi — để thầy nghe tiếng não em đang quay.",
        "Bài tập không phải kẻ thù — nó là bạn tập của em.",
        "Thầy tin em làm được — vì thầy từng tin cả lớp ồn được.",
        "Học không vui bằng chơi — nhưng chơi xong không học thì sau này khóc.",
        "Em chưa hiểu à? Không sao, thầy nói lần thứ hai vẫn miễn phí.",
        "Điểm kém không làm em kém — chỉ làm em biết mình cần ôn đâu.",
        "Lớp mình giỏi lắm — giỏi ngủ gật không ai bằng.",
        "Thầy không đòi em phải giỏi ngay — thầy chỉ đòi em đừng bỏ cuộc.",
        "Sách không cắn em — em mở ra đọc thử đi.",
        "Câu hỏi của em hay lắm — lần sau hỏi đúng lúc thầy hỏi thì hay hơn.",
        "Thầy thích em hay hỏi — vì như thế thầy mới có việc làm.",
        "Chép bài bạn cũng là học — học cách chép không để thầy thấy.",
        "Thầy biết các em mệt — nhưng mệt mà vẫn học mới là chiến binh.",
        "Không hiểu thì hỏi — đừng để trong đầu thành bãi rác.",
        "Em nói đúng rồi — chỉ sai môn thôi.",
        "Thầy không la — thầy chỉ đang nói to để em nghe rõ.",
        "Học một lần chưa đủ — học đến khi não em gật đầu.",
        "Lớp mình hôm nay im quá — thầy tưởng đi nhầm phòng.",
        "Điểm 10 không quan trọng bằng em hiểu được bài.",
        "Thầy cũng từng là học sinh — nên thầy biết em đang nghĩ gì.",
        "Bài này làm xong em sẽ thấy mình thông minh hơn — hoặc cần uống thêm sữa.",
        "Các em đừng sợ sai — sợ không thử mới đáng sợ.",
        "Thầy dạy không phải để các em nhớ thầy — mà để các em nhớ bài.",
        "Em ngủ gật à? Không sao, thầy ghi nhận em đã có mặt.",
        "Học như chơi game — level khó thì chơi nhiều lần.",
        "Thầy không so em với ai — thầy chỉ so em với đề bài.",
        "Quên bài à? Lần sau nhớ mang theo bộ nhớ.",
        "Lớp mình hôm nay học tốt — tốt đến mức thầy muốn cho thêm bài.",
        "Em không dốt — em chỉ đang tìm đường đi đúng.",
        "Thầy tin một ngày em sẽ giỏi — miễn là em đừng ngủ suốt.",
        "Bài tập là bạn — đừng bỏ bạn một mình.",
        "Các em ồn à — nhưng ồn mà vẫn làm bài thì thầy chấp nhận.",
        "Thầy không cần em nói đúng — thầy cần em nghĩ đúng.",
        "Học hôm nay để ngày mai không phải học lại.",
        "Em trả lời sai à? Cảm ơn em — nhờ em cả lớp biết đáp án đúng.",
        "Thầy biết các em có nhiều việc — nhưng việc học vẫn phải có trong list.",
        "Lớp mình sáng nay tỉnh chưa? Thầy thấy còn vài em đang mơ.",
        "Điểm số không định nghĩa em — nhưng nó cho em biết mình đang ở đâu.",
        "Thầy nói lần cuối: mở sách ra — không phải mở miệng ngáp.",
        "Học không vui — nhưng không học sau này còn không vui hơn.",
    ]
    while len(quotes_20) < 50:
        quotes_20.append("Cười xong nhớ học — đó mới là đỉnh.")
    quotes_20 = quotes_20[:50]
    ch_titles_20 = [("Cười mà nghĩ", "Laugh and Think"), ("Vui mà học", "Joy and Learn"), ("Nhẹ mà sâu", "Light but Deep"), ("Chuyện lớp học", "Classroom Tales"), ("Kết bằng cười", "End with a Smile")]
    for ch in range(5):
        sections = [section_humorous(quotes_20[ch*10+i], "Humorous but deep.") for i in range(10)]
        make_chapter(q20_dir, ch + 1, ch_titles_20[ch][0], ch_titles_20[ch][1], sections)

    # Quyển 21: 30 câu giật mình — 3 chương x 10
    q21_dir = os.path.join(BASE, "truyen-tich-cam-hung-quyen-21")
    quotes_21 = [
        "Lười hôm nay, trả giá ngày mai.",
        "Không học bây giờ, đừng hỏi sau này sao không có cơ hội.",
        "Điện thoại không trả tiền cho tương lai em.",
        "Bạn bè giỏi không làm em giỏi — chỉ khi em học thì em mới giỏi.",
        "Một ngày bỏ học là một ngày tương lai mất một viên gạch.",
        "Cha mẹ đang làm việc — em đang làm gì với giờ học?",
        "Điểm kém không giết em — nhưng thói quen lười thì có thể giết tương lai em.",
        "Em không thiếu thời gian — em thiếu quyết tâm.",
        "Sau này khi thất bại, đừng nói không ai báo trước.",
        "Lớp người ta đang chạy — em đang đứng lại vì game?",
        "Thầy không dọa — thầy chỉ nói điều sẽ xảy ra nếu em không đổi.",
        "Em có một bộ não — dùng nó trước khi nó rỉ sét.",
        "Không ai có thể học thay em — và không ai sẽ trả giá thay em.",
        "Hôm nay em chọn nghỉ — ngày mai em sẽ không có quyền chọn.",
        "Sách vở không phải kẻ thù — kẻ thù là sự lười biếng trong đầu em.",
        "Em muốn tương lai thế nào — thì hôm nay em phải làm thế ấy.",
        "Thầy đã nói — em nghe hay không là quyền em; trả giá cũng là quyền em.",
        "Trường học cho em cơ hội — em có dùng hay không?",
        "Lười một ngày dễ — lười cả đời thì tương lai trả giá.",
        "Em không cần tin thầy — em chỉ cần nhìn người không học họ đang sống thế nào.",
        "Điểm số không phạt em — cuộc đời mới phạt khi em không có kỹ năng.",
        "Hôm nay em bỏ một tiết — tương lai em có thể bỏ cả một đời.",
        "Thầy không thể kéo em đi — em phải tự bước.",
        "Em đang đầu tư thời gian vào cái gì — game hay tương lai?",
        "Người ta đang học — em đang làm gì?",
        "Sau này em sẽ hiểu — nhưng sau này thì đã muộn.",
        "Thầy nói thẳng: em lười thì không ai cứu được em.",
        "Mỗi ngày em không học là em đang vay nợ tương lai.",
        "Em có một cơ hội tên là tuổi trẻ — đừng đốt nó.",
    ]
    while len(quotes_21) < 30:
        quotes_21.append("Tỉnh ra trước khi trả giá.")
    quotes_21 = quotes_21[:30]
    ch_titles_21 = [("Trả giá", "The Price"), ("Tỉnh ra", "Wake Up"), ("Tự mình", "On Your Own")]
    for ch in range(3):
        sections = [section_giat_minh(quotes_21[ch*10+i], "Wake up.") for i in range(10)]
        make_chapter(q21_dir, ch + 1, ch_titles_21[ch][0], ch_titles_21[ch][1], sections)

    # Quyển 22: 50 câu đỉnh cao sư phạm khi nản — 5 chương x 10
    q22_dir = os.path.join(BASE, "truyen-tich-cam-hung-quyen-22")
    quotes_22 = [
        "Nản một lúc không sao — đứng dậy mới quan trọng.",
        "Thầy không đòi em phải giỏi ngay — thầy chỉ cần em đừng bỏ cuộc.",
        "Em không kém — em chỉ đang mệt; nghỉ một chút rồi đi tiếp.",
        "Mỗi người có nhịp riêng — em không cần chạy theo ai.",
        "Bài khó không có nghĩa em không làm được — chỉ cần thêm thời gian.",
        "Thầy tin em — dù em chưa tin mình.",
        "Sai hôm nay không có nghĩa sai mãi — em có thể sửa.",
        "Lớp học này có em — và thầy mong em ở lại.",
        "Điểm kém một lần không định nghĩa em.",
        "Em đã cố — thầy thấy rồi; giờ mình cố thêm chút nữa.",
        "Không ai sinh ra đã giỏi — ai cũng từng nản như em.",
        "Thầy không so em với bạn — thầy so em với chính em hôm qua.",
        "Em có thể nghỉ một nhịp — nhưng đừng bỏ cả chặng đường.",
        "Thầy ở đây không phải để phán xét — mà để cùng em đi.",
        "Mệt thì nói — đừng ôm trong lòng rồi bỏ cuộc.",
        "Em không đơn độc — cả lớp và thầy đều muốn em vượt qua.",
        "Hôm nay chưa được — ngày mai mình thử lại.",
        "Thầy biết em đang cố — và đó đã là điều đáng quý.",
        "Nản là bình thường — đứng dậy mới là điều thầy mong.",
        "Em có giá trị — không phải vì điểm, mà vì em là em.",
        "Bài này khó với nhiều người — không chỉ mình em.",
        "Thầy không bỏ em — và em cũng đừng bỏ mình.",
        "Mỗi bước nhỏ vẫn là tiến — em đừng nghĩ mình đứng yên.",
        "Thầy tin một ngày em sẽ thấy mình tiến bộ.",
        "Em được quyền mệt — nhưng cũng được quyền đứng dậy.",
        "Lớp học này cần em — không phải em giỏi hay kém, mà vì em là thành viên.",
        "Đừng nói \"em không thể\" — hãy nói \"em chưa thể\".",
        "Thầy thấy em đã thay đổi — dù chỉ một chút, đó cũng là tiến bộ.",
        "Nản rồi đứng dậy — đó mới là sức mạnh.",
        "Em không cần hoàn hảo — em cần tiếp tục.",
        "Thầy không kỳ vọng em phải đứng đầu — thầy kỳ vọng em không bỏ cuộc.",
        "Mỗi ngày em đến lớp là một ngày em đang cố — thầy trân trọng điều đó.",
        "Bài sai không làm em kém — bỏ cuộc mới làm.",
        "Thầy biết có lúc em muốn buông — nhưng thầy mong em giữ thêm một chút.",
        "Em có thể hỏi thầy bất cứ lúc nào — khi nản, khi không hiểu.",
        "Không ai đi một mạch — ai cũng có lúc dừng; quan trọng là lại đi.",
        "Thầy tin vào em — ngay cả khi em chưa tin vào mình.",
        "Em đang làm được — chỉ cần không dừng lại.",
        "Nản là tạm thời — đứng dậy là quyết định.",
        "Thầy không la em vì điểm — thầy lo khi em buông tay.",
        "Lớp này có em — và thầy muốn em biết mình được chào đón.",
        "Một bước nhỏ vẫn là bước — em đừng so với người chạy nhanh.",
        "Thầy thấy em — và thầy tin em sẽ qua được.",
        "Em không một mình — thầy và bạn cùng đi với em.",
        "Hôm nay khó — ngày mai có thể dễ hơn nếu em không bỏ.",
        "Đỉnh cao sư phạm là khi thầy đỡ em đứng dậy, không phải khi thầy đẩy em ngã.",
    ]
    while len(quotes_22) < 50:
        quotes_22.append("Thầy tin em — em hãy tin mình.")
    quotes_22 = quotes_22[:50]
    ch_titles_22 = [("Đứng dậy", "Get Up"), ("Tin vào em", "Believe in You"), ("Cùng đi", "Walk Together"), ("Không bỏ cuộc", "Don't Quit"), ("Một bước nhỏ", "One Small Step")]
    for ch in range(5):
        sections = [section_nan_hoc(quotes_22[ch*10+i], "Support when down.") for i in range(10)]
        make_chapter(q22_dir, ch + 1, ch_titles_22[ch][0], ch_titles_22[ch][1], sections)

    # Quyển 23: 50 câu cuối năm xúc động — 5 chương x 10
    q23_dir = os.path.join(BASE, "truyen-tich-cam-hung-quyen-23")
    quotes_23 = [
        "Thầy tin em — dù em đi đâu, nhớ câu đó.",
        "Cảm ơn các em đã cho thầy một năm đáng nhớ.",
        "Ra trường rồi, đừng quên mình từng là ai — và có thể trở thành ai.",
        "Thầy không cần em nhớ thầy — thầy cần em nhớ những gì mình đã học.",
        "Chúc các em đi xa — và đi đúng hướng.",
        "Lớp mình tan nhưng không tàn — các em vẫn là bạn, vẫn là đồng đội.",
        "Một ngày nào đó em sẽ hiểu — năm nay có ý nghĩa thế nào.",
        "Thầy chúc em đủ can đảm để thử — và đủ bình tĩnh để đứng dậy khi ngã.",
        "Dù em đi đâu, lớp học này vẫn là nơi em từng thuộc về.",
        "Các em đã lớn hơn — không chỉ về tuổi, mà về cách nghĩ.",
        "Thầy không dạy em để em nhớ thầy — thầy dạy để em không cần thầy nữa.",
        "Ra đời nhớ đừng đánh mất sự tử tế.",
        "Năm nay có vui có buồn — nhưng tất cả đều là quà.",
        "Thầy tin em sẽ làm được — vì thầy đã thấy em cố.",
        "Đừng quên bạn bè — họ là người cùng em đi qua năm tháng này.",
        "Thầy chúc em gặp nhiều thầy tốt hơn thầy — trên đường đời.",
        "Lớp mình hôm nay chia tay — nhưng không phải chia lìa.",
        "Em có thể không còn gặp thầy — nhưng thầy mong em vẫn gặp được điều tốt.",
        "Cảm ơn em đã là học trò của thầy — dù chỉ một năm.",
        "Ra trường rồi — nhớ học tiếp, không phải học trong sách mà học từ cuộc sống.",
        "Thầy không biết em sẽ thành ai — nhưng thầy tin em sẽ thành người đáng trân trọng.",
        "Chúc em đủ mạnh để đối mặt — và đủ mềm để yêu thương.",
        "Năm học kết thúc — nhưng việc học thì không.",
        "Các em đã cho thầy lý do để yêu nghề — cảm ơn.",
        "Dù điểm cao hay thấp — em vẫn là em, và thầy vẫn tin em.",
        "Thầy chúc em tìm được con đường của mình — và đủ dũng khí để đi.",
        "Lớp mình sẽ nhớ nhau — vì đã cùng nhau lớn lên một chút.",
        "Em có thể quên bài — nhưng đừng quên mình từng là học trò và từng được tin.",
        "Thầy mong em sống tốt — đó là món quà lớn nhất em tặng thầy.",
        "Năm nay là một chương — em viết chương tiếp theo thế nào là tùy em.",
        "Cảm ơn các em đã tin thầy — và thầy sẽ luôn tin các em.",
        "Ra đời có thể khó — nhưng em đã từng vượt khó trong lớp, em sẽ vượt được.",
        "Thầy không nói tạm biệt — thầy nói hẹn gặp lại trên đường em đi.",
        "Chúc em đủ bình an để sống — và đủ nhiệt huyết để không bỏ cuộc.",
        "Lớp học này sẽ không còn — nhưng kỷ niệm thì có.",
        "Em đã trưởng thành hơn — thầy thấy rõ; hãy giữ điều đó.",
        "Thầy chúc em gặp người tốt — và trở thành người tốt.",
        "Dù em đi đâu — nhớ rằng em từng có một nơi gọi là lớp, gọi là trường.",
        "Năm học khép lại — tương lai mở ra; em bước đi nhé.",
        "Thầy cảm ơn các em — vì đã cho thầy một năm ý nghĩa.",
        "Em có thể không còn ngồi trong lớp thầy — nhưng thầy vẫn mong em ngồi vững trên đường đời.",
        "Chúc em đủ may mắn — và đủ nỗ lực để không phụ may mắn.",
        "Lớp mình tan — nhưng tình bạn và tình thầy trò không tan.",
        "Thầy tin em — câu này thầy nói lần cuối trong năm, nhưng thầy sẽ giữ mãi.",
        "Ra trường rồi — nhớ đứng dậy mỗi khi vấp; em đã làm được ở lớp, làm được ngoài đời.",
        "Cảm ơn em đã là một phần của năm học này — thầy trân trọng điều đó.",
        "Thầy chúc em bình an và thành công — theo cách em định nghĩa.",
        "Hẹn gặp lại — trên đường đời, hoặc trong ký ức.",
    ]
    while len(quotes_23) < 50:
        quotes_23.append("Thầy tin em. Dù đi đâu, nhớ câu đó.")
    quotes_23 = quotes_23[:50]
    ch_titles_23 = [("Tin và chúc", "Believe and Wish"), ("Cảm ơn và tạm biệt", "Thanks and Goodbye"), ("Ra trường", "Graduation"), ("Nhớ và đi tiếp", "Remember and Move On"), ("Hẹn gặp lại", "See You Again")]
    for ch in range(5):
        sections = [section_cuoi_nam(quotes_23[ch*10+i], "Year-end words.") for i in range(10)]
        make_chapter(q23_dir, ch + 1, ch_titles_23[ch][0], ch_titles_23[ch][1], sections)

    print("Done Q20, Q21, Q22, Q23.")
