#!/usr/bin/env python3
# gen_q7_a.py -- Quyển VII ch01-04: Lão Tử, Khổng Tử, Mạnh Tử, Trang Tử
import os, re

CHAPTERS_DIR = os.path.join(os.path.dirname(__file__), "chapters")
os.makedirs(CHAPTERS_DIR, exist_ok=True)

def fix(s):
    s = s.replace('%', r'\%')
    s = s.replace('&', r'\&')
    s = re.sub(r'"([^"\n]*)"', r"``\1''", s)
    return s

def make_chapter(filename, chapter_num, vn_title, en_title, stories):
    lines = []
    lines.append(r'\chapter{' + fix(vn_title) + r'}')
    lines.append(r'\markboth{' + fix(vn_title) + r'}{' + fix(en_title) + r'}')
    lines.append('')
    for idx, story in enumerate(stories, 1):
        svn = story['title_vn']
        sen = story['title_en']
        pairs = story['pairs']
        lvn = story['lesson_vn']
        len_ = story['lesson_en']
        lines.append(r'\section{' + fix(svn) + r'}')
        lines.append(r'\begin{truyen}{' + fix(svn) + r'}{' + fix(sen) + r'}')
        first = True
        for (vn, en) in pairs:
            if first:
                words = fix(vn).split(' ', 1)
                fc = words[0][0] if words[0] else ''
                rest = words[0][1:] + (' ' + words[1] if len(words) > 1 else '')
                lines.append(r'\chuhoa{' + fc + r'}{' + rest + r'}')
                first = False
            else:
                lines.append(fix(vn))
            lines.append(r'\textit{(' + fix(en) + r')}')
            lines.append('')
        lines.append(r'\end{truyen}')
        lines.append('')
        lines.append(r'\begin{baihoc}')
        lines.append(fix(lvn))
        lines.append(r'\textit{(' + fix(len_) + r')}')
        lines.append(r'\end{baihoc}')
        if idx < len(stories):
            lines.append(r'\ngancach')
        lines.append('')
    path = os.path.join(CHAPTERS_DIR, filename + '.tex')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f'  Đã tạo: {path}')


# ============================================================
# CHƯƠNG 1: Lão Tử — Đạo, Vô Vi, Nước Chảy, Biết Đủ
# ============================================================
ch01 = [
    {
        'title_vn': 'Đạo Mà Nói Được Không Phải Đạo Thường',
        'title_en': 'The Tao That Can Be Told Is Not the Eternal Tao',
        'pairs': [
            ('Một học trò đến gặp Lão Tử và hỏi: "Thưa thầy, Đạo là gì? Xin thầy giải thích để con hiểu."',
             'A student came to Laozi and asked: "Master, what is the Tao? Please explain it so I can understand."'),
            ('Lão Tử im lặng một lúc, rồi hỏi ngược lại: "Con có thể nắm nước trong tay không?"',
             'Laozi was silent a moment, then asked in return: "Can you hold water in your hand?"'),
            ('"Được, thưa thầy, nhưng nó chảy ra ngoài nếu con nắm chặt."',
             '"Yes, Master, but it flows out when I grip tightly."'),
            ('"Đúng vậy. Đạo cũng như nước — nó tồn tại, có thể cảm nhận, nhưng không thể nắm chặt hay định nghĩa bằng lời."',
             '"Exactly. The Tao is like water — it exists, can be felt, but cannot be gripped tight or defined in words."'),
            ('Lão Tử mở đầu Đạo Đức Kinh bằng câu: "Đạo khả đạo, phi thường đạo" — Đạo có thể nói ra được thì không phải Đạo vĩnh hằng.',
             'Laozi opens the Tao Te Ching with: "The Tao that can be told is not the eternal Tao."'),
            ('Không phải vì Đạo huyền bí, mà vì thực tại vốn sâu hơn bất kỳ ngôn từ nào có thể chứa đựng.',
             'Not because the Tao is mysterious, but because reality is always deeper than any words can contain.'),
        ],
        'lesson_vn': 'Đừng nhầm bản đồ với lãnh thổ. Ngôn ngữ chỉ trỏ — nó không phải chính thứ nó trỏ. Sự thật sâu nhất luôn nằm ngoài lời.',
        'lesson_en': 'Do not confuse the map with the territory. Language only points — it is not the thing it points to. The deepest truth always lies beyond words.',
    },
    {
        'title_vn': 'Vô Vi — Hành Động Không Gượng Ép',
        'title_en': 'Wu Wei — Action Without Force',
        'pairs': [
            ('Vua Hui của nước Lương hỏi một người đầu bếp tại sao ông mổ trâu trông dễ dàng đến vậy.',
             'King Hui of Liang asked a cook why he butchered an ox with such apparent ease.'),
            ('Người đầu bếp nói: "Tâu bệ hạ, thần không dùng mắt nữa — thần dùng tâm. Thần thuận theo tự nhiên của con vật, đưa dao vào những khoảng trống đã có sẵn."',
             'The cook replied: "Your Majesty, I no longer use my eyes — I use my mind. I follow the natural structure of the ox, guiding my blade through spaces already there."'),
            ('"Tay thần, vai thần, chân thần, đầu gối thần — tất cả chuyển động như nghi lễ, như vũ điệu theo nhạc trời."',
             '"My hand, shoulder, foot, and knee — all move like a ritual, like a dance to heavenly music."'),
            ('Đây là "Vô Vi" — không phải không làm gì, mà là hành động thuận theo tự nhiên, không gượng ép, không cưỡng cầu.',
             'This is "Wu Wei" — not doing nothing, but acting in harmony with nature, without force, without striving.'),
            ('Con sông không cố chảy xuống biển — nó chỉ thuận theo địa hình và tự nhiên đến nơi.',
             'The river does not try to reach the sea — it simply follows the landscape and naturally arrives.'),
        ],
        'lesson_vn': 'Khi bạn cưỡng ép, mọi thứ kháng cự. Khi bạn thuận theo tự nhiên của việc, nó trở nên dễ dàng. Vô Vi không phải lười biếng — đó là trí tuệ cao nhất.',
        'lesson_en': 'When you force, everything resists. When you follow the nature of the work, it becomes easy. Wu Wei is not laziness — it is the highest wisdom.',
    },
    {
        'title_vn': 'Thượng Thiện Nhược Thủy — Thiện Cao Nhất Như Nước',
        'title_en': 'The Highest Good Is Like Water',
        'pairs': [
            ('Học trò hỏi Lão Tử: "Thưa thầy, thầy dạy chúng con phải như thế nào để sống tốt?"',
             'A student asked Laozi: "Master, what do you teach us to be like in order to live well?"'),
            ('Lão Tử dẫn học trò ra suối, ngồi xuống và hỏi: "Con thấy gì?"',
             'Laozi led the student to a stream, sat down, and asked: "What do you see?"'),
            ('"Nước chảy, thưa thầy."',
             '"Water flowing, Master."'),
            ('"Nước chảy xuống chỗ thấp — không ai muốn ở đó, nước lại chọn. Nước nuôi dưỡng vạn vật mà không tranh giành. Nước mềm mại nhưng xuyên qua đá cứng nhất. Hãy sống như nước."',
             '"Water flows to low places — where no one wants to be, water chooses. Water nourishes all things without competing. Water is soft yet pierces the hardest stone. Live like water."'),
            ('Chương 8 Đạo Đức Kinh dạy: thiện cao nhất giống như nước — lợi vạn vật mà không tranh, ở chỗ người người chê mà không phàn nàn.',
             'Chapter 8 of the Tao Te Ching teaches: the highest good is like water — it benefits all things without competing, dwells in places people disdain without complaint.'),
            ('Khiêm tốn, linh hoạt, bền bỉ — ba đức tính của nước là ba chỉ dẫn sống trọn vẹn nhất.',
             'Humility, flexibility, persistence — the three virtues of water are the three best guides for a full life.'),
        ],
        'lesson_vn': 'Đừng tranh chỗ cao. Hãy chảy về chỗ thấp — nơi bạn thực sự nuôi dưỡng được người khác. Sức mạnh thật không cần phô trương.',
        'lesson_en': 'Do not seek the high place. Flow to the low place — where you truly nourish others. True strength needs no display.',
    },
    {
        'title_vn': 'Tri Túc Giả Phú — Biết Đủ Là Giàu',
        'title_en': 'Those Who Know Enough Are Rich',
        'pairs': [
            ('Một thương nhân giàu có đến thăm Lão Tử và khoe: "Thưa ngài, tôi có một trăm con ngựa, năm kho lúa, ba tòa nhà lớn. Vậy mà lúc nào tôi cũng thấy thiếu."',
             'A wealthy merchant visited Laozi and boasted: "Sir, I have a hundred horses, five granaries, three great houses. Yet I always feel lacking."'),
            ('Lão Tử hỏi: "Ông có bao nhiêu miệng?"',
             'Laozi asked: "How many mouths do you have?"'),
            ('"Một, thưa ngài."',
             '"One, sir."'),
            ('"Một dạ dày?"',
             '"One stomach?"'),
            ('"Vâng."',
             '"Yes."'),
            ('"Thế thì ông đang giàu hơn mức một miệng và một dạ dày cần. Vấn đề không phải là ông có bao nhiêu — mà là ông chưa bao giờ dừng lại để nhận ra mình đã có đủ."',
             '"Then you are richer than one mouth and one stomach needs. The problem is not how much you have — it is that you have never stopped to realize you already have enough."'),
            ('Đạo Đức Kinh chương 33: "Tri túc giả phú" — người biết đủ mới thực sự giàu.',
             'Tao Te Ching chapter 33: "Those who know enough are rich" — one who knows sufficiency is truly wealthy.'),
        ],
        'lesson_vn': 'Lòng tham không có đáy. Sự giàu có thực sự không đến từ việc có thêm — mà từ việc nhận ra bạn đã có đủ để sống trọn vẹn hôm nay.',
        'lesson_en': 'Greed has no bottom. True wealth does not come from having more — but from recognizing you already have enough to live fully today.',
    },
    {
        'title_vn': 'Cứng Mạnh Thuộc Về Chết — Mềm Yếu Thuộc Về Sống',
        'title_en': 'The Hard and Strong Belong to Death — The Soft and Weak to Life',
        'pairs': [
            ('Lão Tử chỉ vào cây sồi lớn và cây sậy nhỏ bên bờ suối và hỏi học trò: "Cây nào sẽ sống qua cơn bão?"',
             'Laozi pointed to a large oak and a small reed by the stream and asked his student: "Which will survive the storm?"'),
            ('Học trò tự tin: "Cây sồi to lớn, thưa thầy."',
             'The student said confidently: "The great oak, Master."'),
            ('Cơn bão đến. Cây sồi gãy. Cây sậy oằn xuống rồi đứng thẳng lại.',
             'A storm came. The oak broke. The reed bent low, then stood straight again.'),
            ('"Cứng cỏi là đặc tính của chết," Lão Tử nói. "Mềm mại là đặc tính của sống. Đá cứng rồi vỡ. Nước mềm luôn tìm được đường."',
             '"Rigidity is the nature of death," Laozi said. "Softness is the nature of life. Hard stone eventually shatters. Soft water always finds its way."'),
            ('Đạo Đức Kinh chương 76 dạy: con người lúc sinh thì mềm mại, lúc chết thì cứng đờ. Cây cỏ lúc sống thì mềm, lúc chết thì khô cứng.',
             'Tao Te Ching chapter 76 teaches: at birth people are soft and supple; at death, stiff and rigid. Plants when living are supple; when dead, dry and brittle.'),
            ('Khả năng thích nghi không phải yếu đuối — đó là trí tuệ sống còn.',
             'The ability to adapt is not weakness — it is the wisdom of survival.'),
        ],
        'lesson_vn': 'Hãy học cây sậy — biết khi nào cúi đầu, biết khi nào đứng thẳng. Sự linh hoạt không mâu thuẫn với sức mạnh; nó chính là sức mạnh.',
        'lesson_en': 'Learn from the reed — knowing when to bow, knowing when to stand straight. Flexibility does not contradict strength; it is strength.',
    },
    {
        'title_vn': 'Thánh Nhân Không Tích Trữ',
        'title_en': 'The Sage Does Not Hoard',
        'pairs': [
            ('Một học trò trẻ hỏi: "Thưa thầy, con nên giữ lại tri thức cho mình hay chia sẻ hết với người khác?"',
             'A young student asked: "Master, should I keep my knowledge for myself or share it all with others?"'),
            ('Lão Tử trả lời bằng một hình ảnh: "Đốt lửa cho người khác — ngọn lửa của con có bị tắt không?"',
             'Laozi answered with an image: "If you light a fire for someone else — does your own flame go out?"'),
            ('"Không, thưa thầy. Ngược lại còn sáng hơn."',
             '"No, Master. If anything it burns brighter."'),
            ('"Đó là Đạo của cho đi. Càng cho đi, càng không thiếu. Thánh nhân không tích trữ — càng làm cho người, mình càng có nhiều; càng cho người, mình càng giàu thêm."',
             '"That is the Tao of giving. The more you give, the less you lack. The sage does not hoard — the more he does for others, the more he has; the more he gives, the richer he becomes."'),
            ('Đây là chương 81, câu kết của Đạo Đức Kinh — bài học cuối cùng và cũng là bài học đơn giản nhất.',
             'This is chapter 81, the closing verse of the Tao Te Ching — the last lesson and also the simplest.'),
        ],
        'lesson_vn': 'Tri thức, tình yêu, lòng tốt — càng chia sẻ càng không cạn. Người sợ mất nhiều nhất thường mất nhiều nhất. Người cho đi dễ nhất thường nhận lại nhiều nhất.',
        'lesson_en': 'Knowledge, love, kindness — the more you share, the less they run dry. Those who fear losing most usually lose most. Those who give most freely usually receive most.',
    },
    {
        'title_vn': 'Cái Hữu Ích Của Cái Không',
        'title_en': 'The Usefulness of Emptiness',
        'pairs': [
            ('Lão Tử dạy: "Ba mươi nan hoa hội tụ vào một trục bánh xe — chính cái trống ở giữa làm cho bánh xe hữu dụng."',
             'Laozi taught: "Thirty spokes converge on a wheel hub — it is the empty space in the center that makes the wheel useful."'),
            ('"Nhào đất sét thành bình — chính cái trống ở trong làm cho bình chứa được."',
             '"Clay is shaped into a vessel — it is the empty space inside that makes the vessel useful."'),
            ('"Đục cửa và cửa sổ — chính khoảng trống làm cho phòng ở được."',
             '"Doors and windows are cut — it is the empty spaces that make the room livable."'),
            ('Học trò suy nghĩ: thứ có hình có ích; thứ không có hình mới tạo ra công dụng.',
             'The student reflected: what has form is useful; what has no form creates the function.'),
            ('Một nhà giáo hiện đại áp dụng bài học này: "Lớp học tốt nhất không phải là lớp thầy nói nhiều nhất — mà là lớp có đủ khoảng im lặng cho học trò tự suy nghĩ."',
             'A modern teacher applied this lesson: "The best classroom is not where the teacher speaks most — but where there is enough silence for students to think for themselves."'),
            ('Cái trống, cái im lặng, cái khoảng nghỉ — đó không phải thiếu hụt, đó là điều kiện cho mọi thứ tồn tại.',
             'Emptiness, silence, the pause — these are not absences; they are the conditions for everything else to exist.'),
        ],
        'lesson_vn': 'Đừng sợ khoảng trống trong cuộc sống. Khoảng trống không phải thiếu sót — nó là không gian cho điều mới sinh ra.',
        'lesson_en': 'Do not fear emptiness in life. Emptiness is not deficiency — it is the space where new things are born.',
    },
    {
        'title_vn': 'Biết Người Là Khôn, Biết Mình Là Sáng',
        'title_en': 'Knowing Others Is Wisdom; Knowing Yourself Is Enlightenment',
        'pairs': [
            ('Một vị tướng đến gặp Lão Tử và khoe: "Tôi biết điểm mạnh và điểm yếu của tất cả tướng địch."',
             'A general came to Laozi and boasted: "I know the strengths and weaknesses of every enemy commander."'),
            ('Lão Tử hỏi: "Thế ông có biết điểm mạnh và điểm yếu của chính mình không?"',
             'Laozi asked: "Do you know your own strengths and weaknesses?"'),
            ('Viên tướng im lặng.',
             'The general fell silent.'),
            ('Lão Tử tiếp: "Người biết người khác là khôn. Người biết mình mới là sáng suốt. Người thắng người khác là có sức. Người thắng chính mình mới là thực sự mạnh."',
             'Laozi continued: "Knowing others is wisdom. Knowing yourself is enlightenment. Overcoming others takes strength. Overcoming yourself is true power."'),
            ('Viên tướng đó sau này kể lại: câu hỏi của Lão Tử đã thay đổi toàn bộ cách ông nhìn chiến lược — từ tập trung vào kẻ thù bên ngoài sang hiểu rõ bản thân mình trước.',
             'The general later recounted: Laozi\'s question changed his entire approach to strategy — from focusing on outside enemies to first understanding himself.'),
        ],
        'lesson_vn': 'Kẻ thù nguy hiểm nhất của bạn thường sống bên trong — sự kiêu ngạo, sợ hãi, thiên kiến. Hãy chiến thắng bản thân trước khi chinh phục thế giới.',
        'lesson_en': 'Your most dangerous enemy often lives within — pride, fear, bias. Conquer yourself before conquering the world.',
    },
    {
        'title_vn': 'Phục Mệnh Viết Thường — Trở Về Là Lẽ Thường',
        'title_en': 'Returning to the Root Is Called Stillness',
        'pairs': [
            ('Một người đàn ông mất hết sau khi kinh doanh thất bại, đến gặp Lão Tử trong trạng thái tuyệt vọng.',
             'A man who lost everything after a failed business came to Laozi in despair.'),
            ('"Tôi không còn gì nữa," anh nói. "Tất cả đã mất."',
             '"I have nothing left," he said. "Everything is gone."'),
            ('Lão Tử dẫn ông ra vườn: "Hãy nhìn cây táo này. Mùa đông nó mất hết lá. Có vẻ chết. Nhưng rễ nó vẫn đó."',
             'Laozi led him to the garden: "Look at this apple tree. In winter it loses all its leaves. It appears dead. But its roots remain."'),
            ('"Mùa xuân đến, nó ra hoa và quả lại. Không phải vì nó không mất lá — mà vì nó trở về với rễ."',
             '"When spring comes, it flowers and fruits again. Not because it did not lose its leaves — but because it returned to its roots."'),
            ('Lão Tử dạy: tất cả mọi thứ đều trở về với gốc của nó. Đó là sự tĩnh lặng. Trở về với gốc là sự sống mới.',
             'Laozi taught: all things return to their root. That is stillness. Returning to the root is renewal.'),
            ('Người đàn ông hiểu ra: mất hết của cải không có nghĩa là mất hết bản thân.',
             'The man understood: losing all wealth does not mean losing oneself.'),
        ],
        'lesson_vn': 'Trong những mất mát lớn nhất, hãy tìm về "gốc rễ" của mình — những điều cốt lõi không thể mất đi. Từ đó, mọi thứ có thể bắt đầu lại.',
        'lesson_en': 'In the greatest losses, return to your "roots" — the core things that cannot be lost. From there, everything can begin again.',
    },
    {
        'title_vn': 'Thánh Nhân Xử Vô Vi — Hành Bất Ngôn Chi Giáo',
        'title_en': 'The Sage Acts Without Striving, Teaches Without Words',
        'pairs': [
            ('Một vị quan đến hỏi Lão Tử: "Làm thế nào để cai trị đất nước tốt?"',
             'An official came to ask Laozi: "How does one govern a country well?"'),
            ('"Như nấu cá nhỏ," Lão Tử trả lời.',
             '"Like cooking a small fish," Laozi replied.'),
            ('Vị quan bối rối: "Nghĩa là sao?"',
             'The official was puzzled: "What does that mean?"'),
            ('"Nấu cá nhỏ càng khuấy nhiều càng nát. Cai trị dân càng can thiệp nhiều càng rối. Thánh nhân cai trị bằng cách ít can thiệp nhất — để người dân tự sắp xếp theo Đạo của họ."',
             '"The more you stir a small fish while cooking, the more it falls apart. The more you intervene in governing people, the more disorder arises. The sage governs by intervening least — letting people arrange themselves according to their own Tao."'),
            ('Chương 17 dạy: nhà lãnh đạo giỏi nhất là người mà dân chúng hầu như không biết ông ta tồn tại. Khi việc hoàn thành, dân nói: "Chúng tôi tự làm được thôi."',
             'Chapter 17 teaches: the best leader is one the people barely know exists. When the work is done, the people say: "We did it ourselves."'),
        ],
        'lesson_vn': 'Lãnh đạo giỏi nhất tạo ra điều kiện để người khác phát huy — không phải kiểm soát từng bước. Bài học này đúng cho cả cha mẹ, thầy giáo, và người quản lý.',
        'lesson_en': 'The best leaders create conditions for others to flourish — not control every step. This lesson applies equally to parents, teachers, and managers.',
    },
]

# ============================================================
# CHƯƠNG 2: Khổng Tử — Nhân, Lễ, Chính Danh, Tu Thân
# ============================================================
ch02 = [
    {
        'title_vn': 'Nhân — Yêu Người Là Nền Tảng Của Tất Cả',
        'title_en': 'Ren — Loving People Is the Foundation of All',
        'pairs': [
            ('Học trò Phàn Trì hỏi Khổng Tử: "Thưa thầy, Nhân là gì?"',
             'Student Fan Chi asked Confucius: "Master, what is Ren?"'),
            ('Khổng Tử trả lời ngắn gọn: "Yêu người."',
             'Confucius answered simply: "Loving people."'),
            ('Phàn Trì hỏi tiếp: "Vậy Trí là gì?"',
             'Fan Chi asked further: "Then what is Wisdom?"'),
            ('"Biết người."',
             '"Knowing people."'),
            ('Phàn Trì ra về chưa hiểu hết. Khổng Tử giải thích thêm với các học trò khác: "Nâng đỡ người ngay thẳng, đặt sang một bên người cong queo — dân sẽ thuần phục. Đặt người cong queo lên trên người ngay thẳng — dân sẽ không phục."',
             'Fan Chi left not fully understanding. Confucius explained further to other students: "Raise the upright above the crooked, and the people will submit. Raise the crooked above the upright, and the people will not submit."'),
            ('Nhân không phải cảm xúc mơ hồ — nó là nguyên tắc tổ chức xã hội: khi người tốt được tôn trọng, xã hội vận hành tốt.',
             'Ren is not a vague emotion — it is a principle of social organization: when good people are honored, society functions well.'),
        ],
        'lesson_vn': 'Mọi thứ bắt đầu từ khả năng yêu thương và hiểu biết con người. Kỹ thuật có thể học được; nhân cách phải tu dưỡng.',
        'lesson_en': 'Everything begins with the ability to love and understand people. Skills can be learned; character must be cultivated.',
    },
    {
        'title_vn': 'Học Mà Không Nghĩ Là Uổng',
        'title_en': 'Learning Without Thinking Is Wasted Effort',
        'pairs': [
            ('Học trò Tử Lộ hỏi về một bài thơ trong Kinh Thi: "Thưa thầy, bài thơ này hay ở chỗ nào?"',
             'Student Zilu asked about a poem in the Book of Odes: "Master, what is fine about this poem?"'),
            ('Khổng Tử hỏi ngược: "Con nghĩ sao?"',
             'Confucius asked in return: "What do you think?"'),
            ('Tử Lộ đọc lại bài thơ rồi đưa ra ý kiến của mình.',
             'Zilu reread the poem and offered his own interpretation.'),
            ('Khổng Tử gật đầu: "Tốt hơn ta nói cho con nghe rất nhiều."',
             'Confucius nodded: "That is far better than if I had simply told you."'),
            ('Ông dạy trong Luận Ngữ: "Học mà không nghĩ là uổng. Nghĩ mà không học là nguy."',
             'He taught in the Analects: "Learning without thinking is wasted effort. Thinking without learning is dangerous."'),
            ('Hai thần kinh biệt — ghi nhớ và suy luận — phải làm việc cùng nhau. Người chỉ ghi nhớ là thư viện sống. Người chỉ suy luận mà thiếu tri thức là người xây nhà không có nền.',
             'Two faculties — memory and reasoning — must work together. One who only memorizes is a living library. One who only reasons without knowledge builds a house without a foundation.'),
        ],
        'lesson_vn': 'Hãy đọc để nạp thông tin, nhưng đừng bao giờ đọc thụ động. Hỏi "Điều này có đúng không? Áp dụng vào cuộc sống mình như thế nào?" — đó mới là học thực sự.',
        'lesson_en': 'Read to absorb information, but never read passively. Ask "Is this true? How does this apply to my life?" — that is real learning.',
    },
    {
        'title_vn': 'Chính Danh — Gọi Đúng Tên Là Nền Tảng Trật Tự',
        'title_en': 'Rectification of Names — Calling Things Correctly Is the Foundation of Order',
        'pairs': [
            ('Tể Lộ hỏi Khổng Tử: "Nếu nước Vệ nhờ thầy cai trị, thầy sẽ làm gì trước tiên?"',
             'Zilu asked Confucius: "If the state of Wei asked you to govern, what would you do first?"'),
            ('Khổng Tử trả lời: "Trước tiên ta sẽ chỉnh danh."',
             'Confucius replied: "First I would rectify the names."'),
            ('Tể Lộ hoài nghi: "Thầy xa rời thực tế! Chỉnh tên để làm gì?"',
             'Zilu was skeptical: "That is so impractical! What is the use of rectifying names?"'),
            ('Khổng Tử giải thích: "Nếu tên không chỉnh, lời nói không thuận. Lời nói không thuận, việc không xong. Việc không xong, lễ nhạc không hưng. Lễ nhạc không hưng, hình phạt không đúng. Hình phạt không đúng, dân không biết đặt tay chân vào đâu."',
             'Confucius explained: "If names are not correct, speech does not accord with truth. When speech does not accord with truth, affairs cannot be accomplished. When affairs cannot be accomplished, ritual and music will not flourish. When ritual and music do not flourish, punishments will not be just. When punishments are not just, the people will not know where to put their hands and feet."'),
            ('Bài học này vẫn còn nguyên giá trị: khi "hòa bình" bị gọi là "chiến tranh", khi "tham nhũng" bị gọi là "phúc lợi" — trật tự xã hội sụp đổ.',
             'This lesson remains fully relevant: when "peace" is called "war," when "corruption" is called "welfare" — social order collapses.'),
        ],
        'lesson_vn': 'Ngôn từ tạo ra thực tại. Khi chúng ta gọi sai tên, chúng ta không thể suy nghĩ đúng về chúng. Hãy gọi sự vật đúng tên — đó là hành động đạo đức đầu tiên.',
        'lesson_en': 'Language creates reality. When we name things wrongly, we cannot think rightly about them. Call things by their right names — that is the first moral act.',
    },
    {
        'title_vn': 'Tu Thân Tề Gia Trị Quốc Bình Thiên Hạ',
        'title_en': 'Cultivate the Self, Regulate the Family, Govern the State, Bring Peace Under Heaven',
        'pairs': [
            ('Một học trò hỏi: "Thưa thầy, muốn trị vì thiên hạ thì bắt đầu từ đâu?"',
             'A student asked: "Master, if one wishes to bring order to the world under heaven, where does one begin?"'),
            ('Khổng Tử trả lời bằng chuỗi nhân quả trong Đại Học: "Muốn bình thiên hạ trước phải trị quốc. Muốn trị quốc trước phải tề gia. Muốn tề gia trước phải tu thân. Muốn tu thân trước phải chính tâm. Muốn chính tâm trước phải thành ý. Muốn thành ý phải có tri thức."',
             'Confucius replied with the chain of causation in the Great Learning: "To bring peace under heaven, first govern the state. To govern the state, first regulate the family. To regulate the family, first cultivate the self. To cultivate the self, first rectify the mind. To rectify the mind, first make the will sincere. To make the will sincere, one must have knowledge."'),
            ('Học trò hỏi: "Nhưng con chỉ là người thường — điều này có relevante với con không?"',
             'The student asked: "But I am just an ordinary person — is this relevant to me?"'),
            ('Khổng Tử mỉm cười: "Mỗi người đều có thiên hạ của mình — gia đình, cộng đồng, công việc. Muốn thay đổi thế giới của con, hãy bắt đầu từ chính con."',
             'Confucius smiled: "Every person has their own world under heaven — family, community, work. If you wish to change your world, begin with yourself."'),
        ],
        'lesson_vn': 'Mọi thay đổi lớn bắt đầu từ bên trong. Bạn không thể đòi hỏi trật tự từ thế giới nếu bạn chưa tạo được trật tự trong bản thân mình.',
        'lesson_en': 'All great change begins within. You cannot demand order from the world if you have not yet created order within yourself.',
    },
    {
        'title_vn': 'Kỷ Sở Bất Dục, Vật Thi Ư Nhân — Điều Mình Không Muốn, Đừng Làm Cho Người',
        'title_en': 'Do Not Impose on Others What You Do Not Desire for Yourself',
        'pairs': [
            ('Học trò Tử Cống hỏi: "Có một chữ nào có thể làm kim chỉ nam cho cả đời sống không, thưa thầy?"',
             'Student Zigong asked: "Is there one word that can serve as a guide for one\'s entire life, Master?"'),
            ('Khổng Tử suy nghĩ rồi nói: "Có lẽ đó là chữ Thứ — lòng khoan dung. Điều mình không muốn, đừng làm cho người khác."',
             'Confucius reflected and said: "Perhaps it is the word Shu — reciprocity. What you do not desire for yourself, do not impose on others."'),
            ('Câu này gần như giống với Quy tắc Vàng xuất hiện trong mọi nền văn hóa lớn: Kinh Thánh dạy "Yêu người lân cận như mình", Phật giáo dạy không hại chúng sinh, đạo Hồi dạy yêu cho người những gì mình yêu cho mình.',
             'This is nearly identical to the Golden Rule appearing in every great culture: the Bible teaches "Love your neighbor as yourself," Buddhism teaches not harming beings, Islam teaches loving for others what you love for yourself.'),
            ('Khổng Tử đã nói câu này 500 năm trước Chúa Jesus — bằng chứng rằng một số chân lý không thuộc về thời đại hay văn hóa nào.',
             'Confucius spoke this 500 years before Jesus — evidence that some truths belong to no single era or culture.'),
        ],
        'lesson_vn': 'Trước khi phán xét, hãy tự hỏi: nếu người này làm với mình điều mình chuẩn bị làm với họ, mình có chấp nhận không? Đó là thước đo đơn giản và đủ tin cậy nhất.',
        'lesson_en': 'Before judging, ask yourself: if this person did to me what I am about to do to them, would I accept it? That is the simplest and most reliable measure.',
    },
    {
        'title_vn': 'Ba Lần Hỏi Tên Phụ Thân',
        'title_en': 'Three Times He Asked His Father\'s Name',
        'pairs': [
            ('Khổng Tử mồ côi cha từ khi còn nhỏ và ít biết về cha mình. Ông lớn lên trong nghèo khó nhưng học hành không ngừng.',
             'Confucius lost his father as a young child and knew little about him. He grew up in poverty but studied ceaselessly.'),
            ('Khi làm quan nhỏ ở nước Lỗ, ông nghe kể rằng cha ông từng được tiếng là người dũng cảm và nhân hậu.',
             'While serving as a minor official in the state of Lu, he heard that his father had been known for courage and benevolence.'),
            ('Ông tìm đến ba người đã biết cha ông và hỏi kỹ về những hành động cụ thể — không phải để khoe, mà để học.',
             'He sought out three people who had known his father and asked carefully about specific actions — not to boast, but to learn.'),
            ('Học trò hỏi tại sao ông làm vậy, Khổng Tử trả lời: "Con người học từ thầy giáo, sách vở — nhưng cũng học từ hành động của những người đã sống trước mình. Cha ta là bài học ta chưa đọc xong."',
             'Students asked why he did this; Confucius replied: "People learn from teachers, from books — but also from the actions of those who lived before them. My father is a lesson I have not yet finished reading."'),
            ('Điều đó phản chiếu một trong những giá trị cốt lõi của ông: học không có điểm dừng, và mọi người đều có thể dạy ta điều gì đó.',
             'This reflected one of his core values: learning has no stopping point, and every person can teach us something.'),
        ],
        'lesson_vn': 'Học là thái độ sống — không phải giai đoạn. Người thực sự học không phân biệt nguồn gốc kiến thức, dù từ sách vở, người già, hay cuộc sống hàng ngày.',
        'lesson_en': 'Learning is a way of life — not a phase. One who truly learns does not discriminate among sources of knowledge, whether from books, elders, or daily life.',
    },
    {
        'title_vn': 'Quân Tử Hòa Nhi Bất Đồng',
        'title_en': 'The Exemplary Person Harmonizes But Does Not Merely Agree',
        'pairs': [
            ('Khổng Tử phân biệt rõ giữa hai loại người: "Quân tử hòa mà không đồng; tiểu nhân đồng mà không hòa."',
             'Confucius drew a clear distinction between two kinds of people: "The exemplary person harmonizes but does not merely agree; the petty person agrees but does not harmonize."'),
            ('Một học trò hỏi sự khác biệt là gì.', 'A student asked what the difference was.'),
            ('Khổng Tử giải thích: "Người đầu bếp giỏi không cho tất cả nguyên liệu vào nồi với lượng bằng nhau — ông ta cân bằng vị chua, mặn, ngọt, cay để tạo ra hương vị hài hòa. Đó là hòa. Kẻ chỉ đồng ý giống như người nếm cháo nhạt và thêm vào chỉ nước — không thay đổi gì cả."',
             'Confucius explained: "A good cook does not put all ingredients in equal amounts — he balances sour, salty, sweet, and spicy to create harmony. That is harmonizing. One who merely agrees is like tasting bland soup and adding only water — nothing changes."'),
            ('Sự hòa hợp thực sự cần có sự khác biệt và bổ sung cho nhau.',
             'True harmony requires difference and complementarity.'),
            ('Người bạn tốt nhất không phải là người luôn đồng ý với bạn — mà là người đủ kính trọng để nói thật.',
             'The best friend is not one who always agrees with you — but one who respects you enough to tell the truth.'),
        ],
        'lesson_vn': 'Đừng nhầm sự phục tùng với hòa thuận. Người bạn thực sự, đồng nghiệp tốt, và lãnh đạo xuất sắc không sợ bất đồng — họ biết bất đồng là điều kiện của sự hoàn thiện.',
        'lesson_en': 'Do not confuse compliance with harmony. True friends, good colleagues, and excellent leaders do not fear disagreement — they know disagreement is a condition for improvement.',
    },
    {
        'title_vn': 'Khổng Tử Khóc Người Học Trò',
        'title_en': 'Confucius Weeps for His Student',
        'pairs': [
            ('Khi học trò Nhan Hồi — người ông yêu quý nhất — chết trẻ, Khổng Tử khóc thảm thiết.',
             'When his student Yan Hui — the one he loved most — died young, Confucius wept bitterly.'),
            ('Các học trò khác ngạc nhiên: "Thưa thầy, thầy dạy chúng con tiết chế cảm xúc — sao thầy lại khóc như vậy?"',
             'Other students were surprised: "Master, you teach us to moderate our emotions — why do you weep like this?"'),
            ('Khổng Tử trả lời: "Nếu không khóc cho người này thì khóc cho ai?"',
             'Confucius replied: "If I do not weep for this person, for whom should I weep?"'),
            ('Nhan Hồi nghèo, ăn cơm đựng trong giỏ, uống nước bằng gáo dừa, sống trong ngõ hẻm chật chội — nhưng học không biết mệt và không bao giờ mất đi niềm vui.',
             'Yan Hui was poor, ate from a basket, drank from a gourd, lived in a narrow alley — yet studied tirelessly and never lost his joy.'),
            ('Khổng Tử từng nói về ông: "Thật tuyệt vời là Nhan Hồi! Một giỏ cơm, một gáo nước, ở ngõ nghèo — người khác không chịu được sự khổ đó, nhưng Hồi không để nó thay đổi niềm vui của mình."',
             'Confucius had said of him: "Admirable indeed, Yan Hui! A basket of rice, a gourd of water, living in a poor lane — others could not endure such hardship, yet Hui would not let it change his joy."'),
        ],
        'lesson_vn': 'Niềm vui học hỏi và sống đúng với giá trị của mình không phụ thuộc vào hoàn cảnh vật chất. Đó là di sản lớn nhất Nhan Hồi để lại — sống vui dù nghèo.',
        'lesson_en': 'The joy of learning and living true to your values does not depend on material circumstances. That is the greatest legacy Yan Hui left — living joyfully despite poverty.',
    },
    {
        'title_vn': 'Ngô Nhật Tam Tỉnh Ngô Thân',
        'title_en': 'Each Day I Examine Myself on Three Points',
        'pairs': [
            ('Học trò Tăng Tử — một trong những đệ tử quan trọng nhất của Khổng Tử — có thói quen tự xét mỗi ngày.',
             'Student Zengzi — one of Confucius\'s most important disciples — had the habit of daily self-examination.'),
            ('Ông nói: "Mỗi ngày ta tự xét bản thân trên ba điều: làm việc cho người khác có hết lòng không? Giao tiếp với bạn bè có thành thật không? Điều thầy dạy có ôn luyện không?"',
             'He said: "Each day I examine myself on three points: Was I faithful in doing things for others? Was I sincere in my dealings with friends? Have I mastered and practiced what I was taught?"'),
            ('Không phải ba điều khổng lồ — chỉ là ba câu hỏi đơn giản mỗi buổi tối trước khi ngủ.',
             'Not three enormous things — just three simple questions each evening before sleep.'),
            ('Hàng nghìn năm sau, nhà tâm lý học Benjamin Franklin áp dụng cách tương tự: mỗi tối ông tự hỏi "Hôm nay ta đã làm gì tốt?"',
             'Thousands of years later, Benjamin Franklin applied an identical practice: each evening he asked himself "What good have I done today?"'),
            ('Tự xét không phải tự ngược đãi — nó là hệ thống phản hồi giúp bạn liên tục cải thiện mà không cần ai chỉ trích bạn.',
             'Self-examination is not self-punishment — it is a feedback system that helps you continuously improve without needing anyone else to criticize you.'),
        ],
        'lesson_vn': 'Xây dựng thói quen tự xét hàng ngày — không phán xét khắt khe, chỉ hỏi thật lòng: "Hôm nay mình đã sống đúng với điều mình tin chưa?" Câu trả lời là thầy giáo tốt nhất.',
        'lesson_en': 'Build a habit of daily self-examination — not harsh judgment, just honest asking: "Did I live in accordance with my values today?" That answer is your best teacher.',
    },
    {
        'title_vn': 'Người Không Nghĩ Xa, Tất Lo Gần',
        'title_en': 'One Who Does Not Think Far Ahead Will Find Trouble Near at Hand',
        'pairs': [
            ('Một phú hộ trẻ đến hỏi Khổng Tử về cách làm giàu bền vững.',
             'A young wealthy man came to ask Confucius about sustainable prosperity.'),
            ('Khổng Tử hỏi: "Anh có con không?"',
             'Confucius asked: "Do you have children?"'),
            ('"Có, thưa thầy, ba đứa nhỏ."',
             '"Yes, Master, three young ones."'),
            ('"Anh đang dạy chúng điều gì?"',
             '"What are you teaching them?"'),
            ('Phú hộ lúng túng: "Con chưa nghĩ đến chuyện đó."',
             'The young man was at a loss: "I have not thought about that yet."'),
            ('Khổng Tử nói: "Anh đang xây nhà mà không xây nền. Của cải có thể tích lũy trong một đời — nhưng đức hạnh của con người phải được trồng từ khi còn nhỏ. Người không nghĩ xa, tất có lo gần."',
             'Confucius said: "You are building a house without laying the foundation. Wealth can be accumulated in one lifetime — but human virtue must be cultivated from childhood. One who does not think far ahead will certainly find trouble near at hand."'),
        ],
        'lesson_vn': 'Tầm nhìn dài hạn không chỉ là chiến lược kinh doanh — nó là trách nhiệm với những người bạn yêu. Đầu tư vào nhân cách con cái quan trọng hơn của cải để lại cho chúng.',
        'lesson_en': 'Long-term vision is not only business strategy — it is responsibility to those you love. Investing in your children\'s character matters more than the wealth you leave them.',
    },
]

# ============================================================
# CHƯƠNG 3: Mạnh Tử — Tính Thiện, Lòng Trắc Ẩn, Dân Vi Quý
# ============================================================
ch03 = [
    {
        'title_vn': 'Tính Người Vốn Thiện Như Nước Chảy Xuống',
        'title_en': 'Human Nature Is Originally Good Like Water Flowing Downward',
        'pairs': [
            ('Cáo Tử tranh luận với Mạnh Tử: "Tính người không thiện không ác, như nước — đổ về đông thì chảy đông, đổ về tây thì chảy tây."',
             'Gaozi argued with Mencius: "Human nature is neither good nor bad, like water — direct it east and it flows east, direct it west and it flows west."'),
            ('Mạnh Tử đáp: "Nước thì không phân đông tây, nhưng có phân trên dưới. Tính thiện của người cũng như nước chảy xuống — không ai không thiện, như không có nước nào không chảy xuống."',
             'Mencius replied: "Water does not distinguish east from west, but it does distinguish up from down. Human goodness is like water flowing downward — there is no person who is not good, just as there is no water that does not flow downward."'),
            ('"Nhưng có thể đập nước bắn lên trán người — đó có phải tính của nước không? Bắt nước chảy ngược lên núi được — nhưng đó không phải tính của nước. Người làm ác cũng vậy — là vì hoàn cảnh cưỡng bức, không phải vì tính gốc."',
             '"But you can splash water up to a man\'s forehead — is that the nature of water? You can make water flow up a mountain — but that is not the nature of water. When people do evil, it is likewise because of circumstances forcing it, not because of their original nature."'),
            ('Mẹ Mạnh Tử chuyển nhà ba lần để chọn môi trường tốt cho con — bởi vì bà hiểu: tính thiện cần môi trường để phát triển.',
             'Mencius\'s mother moved their home three times to choose a good environment for her son — because she understood: goodness of nature needs the right environment to develop.'),
        ],
        'lesson_vn': 'Con người sinh ra với mầm thiện. Nhưng mầm thiện cần được vun xới bởi giáo dục và môi trường đúng. Đây là lý do giáo dục không bao giờ là xa xỉ phẩm.',
        'lesson_en': 'People are born with seeds of goodness. But those seeds need to be nurtured by proper education and environment. This is why education is never a luxury.',
    },
    {
        'title_vn': 'Tứ Đoan — Bốn Mầm Đức Hạnh',
        'title_en': 'The Four Sprouts of Virtue',
        'pairs': [
            ('Mạnh Tử dạy: người ta ai cũng có bốn mầm đức hạnh bẩm sinh, như bốn chi trên thân thể.',
             'Mencius taught: everyone has four innate sprouts of virtue, like the four limbs of the body.'),
            ('"Thấy đứa trẻ sắp ngã xuống giếng, ai cũng có lòng kinh hãi thương xót — đó là mầm của Nhân."',
             '"Seeing a child about to fall into a well, everyone feels alarm and compassion — that is the sprout of Benevolence."'),
            ('"Biết xấu hổ về điều xấu mình làm — đó là mầm của Nghĩa."',
             '"Feeling shame about the wrong things one does — that is the sprout of Righteousness."'),
            ('"Biết nhường nhịn — đó là mầm của Lễ."',
             '"Knowing to defer and yield — that is the sprout of Ritual Propriety."'),
            ('"Phân biệt đúng sai — đó là mầm của Trí."',
             '"Distinguishing right from wrong — that is the sprout of Wisdom."'),
            ('"Ai có bốn mầm này mà nói mình không thể thiện là tự hại mình. Ai nói vua mình không thể thiện là tự hại vua mình."',
             '"Whoever has these four sprouts and says they cannot be good is injuring themselves. Whoever says their ruler cannot be good is injuring their ruler."'),
        ],
        'lesson_vn': 'Bạn không cần học đạo đức từ đầu — bạn chỉ cần nhận ra và nuôi dưỡng những mầm đức hạnh đã sẵn có trong mình từ khi sinh ra.',
        'lesson_en': 'You do not need to learn ethics from scratch — you only need to recognize and nurture the sprouts of virtue already present in you from birth.',
    },
    {
        'title_vn': 'Dân Vi Quý, Xã Tắc Thứ Chi, Quân Vi Khinh',
        'title_en': 'The People Are Most Important; the State Comes Next; the Ruler Least',
        'pairs': [
            ('Đây là câu nói táo bạo nhất của Mạnh Tử — và nguy hiểm nhất với các bạo vương thời ông.',
             'This is Mencius\'s boldest statement — and the most dangerous for the tyrants of his time.'),
            ('"Dân vi quý, xã tắc thứ chi, quân vi khinh" — Dân quan trọng nhất, đất nước đứng thứ, vua là nhẹ nhất.',
             '"The people are most important; the altars of land and grain come next; the ruler is least important."'),
            ('Một vua hỏi: "Vậy vua có quyền gì?"',
             'A king asked: "Then what authority does the ruler have?"'),
            ('Mạnh Tử đáp: "Thiên tử mất lòng dân thì mất thiên hạ. Chư hầu mất lòng thiên tử thì mất nước. Đại phu mất lòng chư hầu thì mất ấp. Dân là nền tảng của quốc gia — nền bền thì nước yên."',
             'Mencius replied: "When the Son of Heaven loses the favor of the people, he loses the realm. When the feudal lords lose the favor of the Son of Heaven, they lose their states. When the ministers lose the favor of the feudal lords, they lose their domains. The people are the foundation of the nation — when the foundation is solid, the nation is at peace."'),
            ('Tư tưởng này xuất hiện hơn 2000 năm trước khi các triết gia châu Âu phát triển khái niệm chủ quyền nhân dân.',
             'This idea appeared more than 2000 years before European philosophers developed the concept of popular sovereignty.'),
        ],
        'lesson_vn': 'Quyền lực chỉ hợp pháp khi phục vụ người dân. Mọi tổ chức — nhà nước, công ty hay gia đình — vận hành tốt nhất khi đặt lợi ích của những người phụ thuộc vào nó lên trước.',
        'lesson_en': 'Power is only legitimate when it serves the people. Every organization — state, company, or family — functions best when it places the interests of those who depend on it first.',
    },
    {
        'title_vn': 'Mẹ Mạnh Tử Chuyển Nhà Ba Lần',
        'title_en': 'Mencius\'s Mother Moved Three Times',
        'pairs': [
            ('Thuở nhỏ, Mạnh Tử và mẹ sống gần nghĩa địa. Mạnh Tử thường chơi trò giả vờ chôn cất người chết.',
             'In his youth, Mencius and his mother lived near a cemetery. Mencius would play at imitating burial rites.'),
            ('Mẹ ông lo lắng và chuyển nhà đến gần chợ. Mạnh Tử bắt đầu chơi trò bán hàng và mặc cả.',
             'His mother was concerned and moved near a market. Mencius began playing at buying and selling.'),
            ('Bà chuyển nhà lần thứ ba, đến gần trường học. Mạnh Tử bắt đầu chơi trò học lễ nghi và tranh luận.',
             'She moved a third time, to near a school. Mencius began playing at learning rites and debating.'),
            ('"Đây là chỗ xứng đáng cho con ta," bà nói và ở lại.',
             '"This is a proper place for my son," she said and stayed.'),
            ('Câu chuyện này là nền tảng của triết lý giáo dục Mạnh Tử: môi trường định hình tính cách. Đứa trẻ không chọn được môi trường — người lớn có trách nhiệm chọn thay.',
             'This story is the foundation of Mencius\'s educational philosophy: environment shapes character. Children cannot choose their environment — adults bear the responsibility to choose for them.'),
        ],
        'lesson_vn': 'Chúng ta đều là sản phẩm một phần của môi trường mình lớn lên. Hãy có ý thức về môi trường bạn tạo ra cho con trẻ — hoặc cho chính bạn.',
        'lesson_en': 'We are all partly products of the environment we grew up in. Be intentional about the environment you create for children — or for yourself.',
    },
    {
        'title_vn': 'Kẻ Cùng Đường Không Thụ Diều Rẻo',
        'title_en': 'The Proud Poor Man',
        'pairs': [
            ('Mạnh Tử kể câu chuyện một người đàn ông nghèo, vợ và thiếp đều kính trọng, tưởng ông là người đáng trọng.',
             'Mencius told the story of a poor man whose wife and concubine both respected him, thinking he was worthy of regard.'),
            ('Nhưng bí mật là: mỗi ngày ông lẻn ra nghĩa địa xin đồ ăn thừa từ người đến cúng tế, rồi về nhà phô trương như đã ăn với người giàu có.',
             'But the secret was: each day he would sneak to the cemetery to beg leftover food from those who came to make offerings, then return home bragging about dining with the wealthy.'),
            ('Vợ và thiếp phát hiện ra sự thật, hai người ôm nhau khóc.',
             'When his wife and concubine discovered the truth, they wept together.'),
            ('Mạnh Tử kết luận: "Nếu quan sát cách người đời tìm kiếm giàu sang danh vọng, ít người không làm khiến vợ thiếp phải xấu hổ và khóc."',
             'Mencius concluded: "If we observe how people in the world seek wealth and honor, there are few whose wives and concubines would not be ashamed and weep."'),
            ('Câu chuyện không phê phán người nghèo — nó phê phán sự giả tạo và cái giá của danh dự lừa dối.',
             'The story does not criticize poverty — it criticizes pretense and the price of false honor.'),
        ],
        'lesson_vn': 'Danh dự xây trên sự lừa dối không phải danh dự — đó là gánh nặng. Sự thật, dù khiêm nhường, nhẹ hơn mọi lời nói dối hào nhoáng.',
        'lesson_en': 'Honor built on deception is not honor — it is a burden. Truth, however humble, is lighter than any glamorous lie.',
    },
    {
        'title_vn': 'Thiên Tướng Đại Nhiệm Tất Tiên Khổ Kỳ Tâm Chí',
        'title_en': 'Heaven Prepares Great Tasks Through Suffering',
        'pairs': [
            ('Mạnh Tử dạy: "Khi trời muốn giao trọng trách lớn cho người nào, ắt trước làm khổ tâm chí người ấy, làm mỏi mệt gân cốt, làm đói thân thể, làm thiếu thốn thân người, làm rối loạn mọi việc người làm."',
             'Mencius taught: "When heaven is about to confer a great responsibility on someone, it first afflicts their mind with suffering, tires their sinews and bones, starves their body, subjects them to poverty, and confounds their undertakings."'),
            ('"Tất cả để thúc đẩy tâm họ kiên nhẫn, và tăng thêm năng lực mà trước đây họ không có."',
             '"All of this is to stimulate their mind to endurance, and to develop capabilities they did not previously possess."'),
            ('Ông liệt kê những thánh nhân vĩ đại đều qua gian khổ trước khi trở thành vĩ đại: Shun từ ruộng đồng, Phó Duyệt từ công trường xây dựng, Giao Cách từ cá muối, Quản Trọng từ lao ngục.',
             'He listed the great sages who all passed through hardship before becoming great: Shun from the fields, Fu Yue from construction sites, Jiao Ge from salt fish selling, Guan Zhong from prison.'),
            ('Đây không phải triết học của sự đau khổ — mà là quan sát rằng khó khăn cưỡng bức sự tăng trưởng mà thoải mái không thể tạo ra.',
             'This is not a philosophy of suffering — but an observation that hardship forces growth that comfort cannot produce.'),
        ],
        'lesson_vn': 'Đừng cầu xin cuộc đời dễ dàng hơn. Hãy cầu mình đủ mạnh hơn. Khó khăn không phải dấu hiệu bạn thất bại — nó có thể là dấu hiệu trời đang chuẩn bị bạn.'  ,
        'lesson_en': 'Do not pray for an easier life. Pray to be stronger. Hardship is not a sign you are failing — it may be a sign that heaven is preparing you.',
    },
    {
        'title_vn': 'Sinh Ư Ưu Hoạn, Tử Ư An Lạc',
        'title_en': 'Life Springs from Sorrow; Death Comes from Ease',
        'pairs': [
            ('Một học trò hỏi Mạnh Tử: "Tại sao những người sống khổ lại thường mạnh và sống lâu hơn người sống sung sướng?"',
             'A student asked Mencius: "Why do people who live hard lives often seem stronger and live longer than those who live comfortably?"'),
            ('Mạnh Tử trả lời bằng quan sát: "Sinh ở lo âu, chết ở an nhàn."',
             'Mencius responded with an observation: "Life springs from sorrow and calamity; death comes from ease and pleasure."'),
            ('"Quốc gia không có kẻ thù bên ngoài và mối lo bên trong thường diệt vong. Cá nhân không có sự kháng cự và thử thách trong cuộc đời thường yếu đi."',
             '"A state that has no outside enemies and internal troubles will usually perish. An individual who has no resistance and challenges in life usually weakens."'),
            ('Cơ thể tập thể dục trở nên mạnh vì phải vượt qua kháng cự. Trí tuệ phát triển khi đối mặt với vấn đề. Tính cách rèn trong gian khổ.',
             'The body strengthened by exercise becomes strong by overcoming resistance. The mind grows when facing problems. Character is forged in hardship.'),
            ('Sự thoải mái hoàn toàn là kẻ thù của sự tăng trưởng.',
             'Complete comfort is the enemy of growth.'),
        ],
        'lesson_vn': 'Hãy cảm ơn những thách thức — chúng giữ cho tâm trí và tính cách bạn sắc nét. Cuộc sống không có ma sát là cuộc sống không phát triển.',
        'lesson_en': 'Be grateful for challenges — they keep your mind and character sharp. A life without friction is a life without growth.',
    },
    {
        'title_vn': 'Mạnh Tử Và Vua Lương Huệ Vương',
        'title_en': 'Mencius and King Hui of Liang',
        'pairs': [
            ('Vua Huệ của nước Lương gặp Mạnh Tử và hỏi: "Ngài đến từ xa — có điều gì lợi cho nước ta không?"',
             'King Hui of Liang met Mencius and asked: "You have come from afar — is there anything that will profit my kingdom?"'),
            ('Mạnh Tử đáp thẳng: "Vua sao lại hỏi về lợi? Chỉ cần có Nhân Nghĩa là đủ."',
             'Mencius replied directly: "Why must Your Majesty speak of profit? There need only be benevolence and righteousness."'),
            ('"Nếu vua hỏi điều gì lợi cho nước, đại thần hỏi điều gì lợi cho nhà, sĩ thứ hỏi điều gì lợi cho thân — trên dưới tranh lợi, nước sẽ nguy."',
             '"If the king asks what profits the state, ministers ask what profits their households, scholars and commoners ask what profits themselves — when all levels compete for profit, the state will be in danger."'),
            ('Mạnh Tử không phủ nhận tầm quan trọng của lợi ích — ông cảnh báo về nguy hiểm khi lợi ích trở thành giá trị duy nhất.',
             'Mencius did not deny the importance of benefit — he warned of the danger when profit becomes the only value.'),
            ('Một xã hội chỉ nói về lợi nhuận sẽ xói mòn sự tin tưởng, lòng trung thành và phẩm giá con người.',
             'A society that speaks only of profit will erode trust, loyalty, and human dignity.'),
        ],
        'lesson_vn': 'Hỏi "điều này có lợi gì không?" là câu hỏi hợp lý. Nhưng khi đó là câu hỏi duy nhất bạn đặt ra, bạn đã bắt đầu mất đi điều quan trọng hơn lợi nhuận.',
        'lesson_en': 'Asking "what is the profit in this?" is a reasonable question. But when it is the only question you ask, you have begun losing something more important than profit.',
    },
    {
        'title_vn': 'Ngư Dữ Hùng Chưởng — Cá Và Chân Gấu',
        'title_en': 'Fish and Bear\'s Paw — On Choosing Between Two Goods',
        'pairs': [
            ('Mạnh Tử nói: "Cá là điều ta muốn. Chân gấu cũng là điều ta muốn. Nếu không thể có cả hai, ta bỏ cá lấy chân gấu."',
             'Mencius said: "Fish is something I desire. Bear\'s paw is also something I desire. If I cannot have both, I will give up fish and take bear\'s paw."'),
            ('"Sống là điều ta muốn. Nghĩa cũng là điều ta muốn. Nếu không thể có cả hai, ta bỏ sống giữ nghĩa."',
             '"Life is something I desire. Righteousness is also something I desire. If I cannot have both, I will give up life and hold onto righteousness."'),
            ('Học trò ngạc nhiên: "Thưa thầy, thầy coi nghĩa quan trọng hơn mạng sao?"',
             'Students were surprised: "Master, do you consider righteousness more important than life?"'),
            ('"Không phải ta không ham sống — ta ham sống nhiều lắm. Nhưng có thứ ta ham hơn sống, nên không làm bất cứ điều gì để sống còn. Cũng không phải ta không sợ chết — nhưng có thứ ta sợ hơn chết, nên không tránh được nguy hiểm."',
             '"It is not that I do not desire life — I desire it greatly. But there is something I desire more than life, so I will not do anything to preserve it at any cost. It is not that I do not fear death — but there is something I fear more than death, so I do not always avoid danger."'),
            ('Điều đó, Mạnh Tử nói, là không thể mất — lương tâm và phẩm giá.',
             'That thing, Mencius said, must not be lost — conscience and dignity.'),
        ],
        'lesson_vn': 'Mỗi người có một "chân gấu" — điều họ sẽ không đánh đổi dù giá nào. Biết điều đó là gì với bạn nghĩa là bạn đã biết mình là ai.',
        'lesson_en': 'Every person has their "bear\'s paw" — something they will not trade at any price. Knowing what that is for you means you know who you are.',
    },
    {
        'title_vn': 'Bất Nhẫn Nhân Chi Tâm — Lòng Không Thể Chịu Được Khi Người Khác Khổ',
        'title_en': 'The Heart That Cannot Bear to See Others Suffer',
        'pairs': [
            ('Mạnh Tử mô tả khoảnh khắc mà ông tin rằng chứng minh bản chất thiện của con người.',
             'Mencius described a moment he believed proves the innate goodness of human nature.'),
            ('"Bất kỳ ai thấy đứa trẻ sắp ngã xuống giếng đều sẽ có lòng kinh hãi và thương xót — không phải vì muốn kết thân với cha mẹ đứa trẻ, không phải vì muốn tiếng khen của làng xóm, không phải vì sợ tai tiếng nếu không cứu."',
             '"Anyone who sees a child about to fall into a well will feel alarm and compassion — not because they want to befriend the child\'s parents, not because they want praise from the village, not because they fear blame if they do not act."'),
            ('"Cảm xúc đó là tự nhiên, tức thì, không tính toán — đó chính là bằng chứng của Nhân trong tâm người."',
             '"That feeling is natural, immediate, uncalculated — that is the evidence of Benevolence in the human heart."'),
            ('Thực nghiệm tâm lý học hiện đại xác nhận: mọi người ở khắp nơi trên thế giới đều có phản ứng cảm xúc tức thì với nỗi đau của người khác — bất kể văn hóa hay giáo dục.',
             'Modern psychological experiments confirm: people everywhere in the world have an immediate emotional response to others\' pain — regardless of culture or education.'),
            ('Mạnh Tử đúng: tính thiện không phải học được — nó được phát hiện.',
             'Mencius was right: goodness is not something learned — it is something discovered.'),
        ],
        'lesson_vn': 'Lòng trắc ẩn không phải yếu đuối — đó là bằng chứng bạn còn người. Đừng để xã hội dạy bạn tắt đi thứ thiên nhiên đặt vào bạn.',
        'lesson_en': 'Compassion is not weakness — it is evidence of your humanity. Do not let society teach you to extinguish what nature placed within you.',
    },
]

# ============================================================
# CHƯƠNG 4: Trang Tử — Tự Do Tâm Thức, Tương Đối, Bướm Mơ
# ============================================================
ch04 = [
    {
        'title_vn': 'Trang Châu Mộng Hồ Điệp — Bướm Hay Người?',
        'title_en': 'Zhuangzi Dreamed He Was a Butterfly',
        'pairs': [
            ('Trang Tử kể: "Một lần ta mơ thấy ta là con bướm, vui bay lượn, hoàn toàn là bướm. Khi tỉnh dậy, ta là Trang Châu rõ ràng."',
             'Zhuangzi said: "Once I dreamed I was a butterfly, fluttering freely, completely a butterfly. When I woke, I was clearly Zhuang Zhou."'),
            ('"Nhưng ta không biết — ta là Trang Châu mơ thấy mình là bướm, hay ta là con bướm đang mơ thấy mình là Trang Châu?"',
             '"But I do not know — am I Zhuang Zhou who dreamed of being a butterfly, or am I a butterfly now dreaming of being Zhuang Zhou?"'),
            ('Câu hỏi này không phải triết học vô ích — nó thách thức điều mà tất cả chúng ta coi là hiển nhiên: sự phân biệt cứng nhắc giữa "tôi" và "không phải tôi", giữa "thực" và "không thực".',
             'This is not idle philosophy — it challenges what we all take for granted: the rigid distinction between "I" and "not I," between "real" and "not real."'),
            ('Trang Tử không đưa ra câu trả lời. Ông đặt câu hỏi để mở ra không gian suy nghĩ.',
             'Zhuangzi does not give an answer. He poses the question to open up space for thinking.'),
            ('Người ngủ không biết mình đang ngủ — người thức cũng có thể không biết mình đang ở trong một loại giấc mộng khác.',
             'The sleeping person does not know they are sleeping — the waking person may also not know they are in a different kind of dream.'),
        ],
        'lesson_vn': 'Đừng quá chắc chắn rằng bạn biết đâu là thực, đâu là ảo. Sự khiêm tốn nhận thức — hiểu rằng hiểu biết của mình có giới hạn — là nền tảng của tâm minh triết.',
        'lesson_en': 'Do not be too certain you know what is real and what is illusion. Epistemic humility — understanding that your knowledge has limits — is the foundation of a wise mind.',
    },
    {
        'title_vn': 'Tể Ngưu — Người Đầu Bếp Và Đạo',
        'title_en': 'Cook Ding and the Tao',
        'pairs': [
            ('Trang Tử kể câu chuyện người đầu bếp Tể Ngưu mổ trâu cho Vương Lương Tuệ Vương.',
             'Zhuangzi tells the story of Cook Ding butchering an ox for Prince Hui of Liang.'),
            ('Dao chạm vào xương và thịt, vai nhịp nhàng, chân giậm cuộn, tiếng dao xèo xèo — tất cả như vũ điệu, như nhạc.',
             'The knife touched bones and flesh, shoulders moved rhythmically, feet stamped in cadence, the knife swooshing — all like a dance, like music.'),
            ('Vương hỏi: "Kỹ thuật của ngươi thật diệu kỳ!"',
             'The prince said: "Your skill is truly wonderful!"'),
            ('Tể Ngưu đặt dao xuống: "Thần thực hành Đạo, không phải kỹ thuật thông thường. Thần không dùng mắt — thần dùng tâm. Thần theo cấu trúc tự nhiên của con trâu, đưa dao vào khoảng trống đã có sẵn, không bao giờ cắt vào khớp xương lớn."',
             'Cook Ding set down his knife: "What I practice is the Tao, which goes beyond mere skill. I no longer see with my eyes — I work with my mind. I follow the natural structure of the ox, guiding my knife through spaces already there, never hacking at joints or bones."'),
            ('"Con dao của thần đã dùng mười chín năm, cắt hàng nghìn con trâu, nhưng lưỡi vẫn như mới mài vì thần không cắt nơi nào không nên cắt."',
             '"My knife has been used for nineteen years, cutting thousands of oxen, yet its blade is still as sharp as when freshly ground, because I never cut where I should not cut."'),
        ],
        'lesson_vn': 'Kỹ năng cao nhất là khi bạn không còn phải nghĩ đến kỹ thuật — bạn thuận theo tự nhiên của công việc. Đó là khi công việc trở thành nghệ thuật.',
        'lesson_en': 'The highest skill is when you no longer have to think about technique — you flow according to the nature of the work. That is when work becomes art.',
    },
    {
        'title_vn': 'Tương Đối — Không Có Chuẩn Tuyệt Đối',
        'title_en': 'Relativity — There Is No Absolute Standard',
        'pairs': [
            ('Trang Tử hỏi: "Con người ngủ nơi ẩm ướt sẽ đau lưng và tê liệt — con lươn có vậy không? Người leo cây cao sẽ sợ — con vượn có vậy không? Ba sinh vật — ai ở đúng chỗ nhất?"',
             'Zhuangzi asked: "If a man sleeps in damp places, his back will ache and he will be half paralyzed — does that happen to eels? If a man climbs a tree, he will be frightened — does that happen to monkeys? Of these three, who knows the proper place to live?"'),
            ('"Con người ăn thịt và cá. Con hươu ăn cỏ. Con rết ăn rắn nhỏ. Con cú ăn chuột. Bốn loài — ai biết thức ăn đúng là gì?"',
             '"People eat meat and fish. Deer eat grass. Centipedes eat small snakes. Owls eat mice. Of these four, which knows what the proper food is?"'),
            ('Trang Tử không nói không có thực tại — ông nói thực tại phụ thuộc vào góc nhìn của người quan sát.',
             'Zhuangzi is not saying there is no reality — he is saying reality depends on the perspective of the observer.'),
            ('Điều này không dẫn đến hư vô — nó dẫn đến sự khiêm tốn và cởi mở với những quan điểm khác.',
             'This does not lead to nihilism — it leads to humility and openness to other perspectives.'),
            ('Ai đó nhìn thế giới rất khác bạn — họ có thể không sai, họ chỉ nhìn từ chỗ khác.',
             'Someone who sees the world very differently from you may not be wrong — they are simply looking from a different place.'),
        ],
        'lesson_vn': 'Trước khi kết luận ai đúng ai sai, hãy hỏi: "Họ đang nhìn từ góc độ nào?" Sự thật thường lớn hơn bất kỳ góc nhìn đơn lẻ nào.',
        'lesson_en': 'Before concluding who is right or wrong, ask: "From what perspective are they seeing?" Truth is usually larger than any single viewpoint.',
    },
    {
        'title_vn': 'Trang Tử Hát Bên Mộ Vợ',
        'title_en': 'Zhuangzi Singing Beside His Wife\'s Coffin',
        'pairs': [
            ('Khi vợ Trang Tử mất, Huệ Tử đến thăm và thấy ông đang ngồi, gõ vào bát và hát.',
             'When Zhuangzi\'s wife died, Huizi came to offer condolences and found him sitting, beating on a bowl and singing.'),
            ('Huệ Tử trách: "Bạn đã sống với bà ấy, bà lớn tuổi đã nuôi dạy con cái. Không khóc khi bà chết là đã đủ tệ, nhưng còn đang ca hát!"',
             'Huizi reproached: "You lived with her, she raised your children in old age. Not to weep at her death is already bad enough, but to be singing!"'),
            ('Trang Tử trả lời: "Không phải vậy. Khi bà mới mất, ta hoàn toàn đau buồn như bất kỳ ai. Nhưng ta nhìn lại nguồn gốc — trước khi có sự sống, trước khi có hình thể, trước khi có khí. Rồi khí biến thành hình, hình biến thành sự sống, giờ thì biến đổi lại thành cái chết — như bốn mùa luân chuyển."',
             'Zhuangzi replied: "Not so. When she first died, I was in grief like anyone. But I looked back to her beginning — before she lived there was no life; not only no life, but no form; not only no form, but no vital energy. Then the vital energy transformed and she had form; the form transformed and she had life; now it transforms again and she is dead — like the progression of the four seasons."'),
            ('"Bà đang ngủ yên trong ngôi nhà vĩ đại của tự nhiên. Nếu ta khóc lóc ầm ĩ, ta sẽ tự chứng tỏ mình không hiểu số mệnh."',
             '"She is now resting peacefully in the great mansion of nature. If I were to howl and weep, it would show that I do not understand destiny."'),
        ],
        'lesson_vn': 'Đây không phải bài học về sự lạnh lùng — mà về một loại chấp nhận sâu sắc hơn, nhìn cái chết như phần tự nhiên của chu kỳ chứ không phải thảm kịch tuyệt đối.',
        'lesson_en': 'This is not a lesson in coldness — but in a deeper kind of acceptance, seeing death as a natural part of the cycle rather than an absolute tragedy.',
    },
    {
        'title_vn': 'Sơn Mộc Vô Dụng Mà Thọ — Cây Vô Dụng Mà Sống Lâu',
        'title_en': 'The Useless Tree Lives Long',
        'pairs': [
            ('Một người thợ mộc đang đi cùng học trò thì thấy một cây sồi khổng lồ được thờ ở một miếu thờ. Học trò trầm trồ về sự hùng vĩ của cây.',
             'A carpenter was traveling with his apprentice and saw a huge oak tree worshipped at a shrine. The apprentice admired the magnificent tree.'),
            ('Người thợ mộc phẩy tay: "Vô dụng! Gỗ cứng quá cưa không vào, đốt không cháy. Đó là lý do nó sống lâu như vậy."',
             'The carpenter waved his hand: "Useless! The wood is too hard to saw, too resinous to burn. That is why it has grown so old."'),
            ('Đêm đó, cây sồi hiện trong mơ người thợ mộc và nói: "Ngươi so sánh ta với cây hữu ích ư? Lê, cam, táo — chúng hữu ích nên bị hái trụi, bị chặt khi còn sớm. Cái hữu ích của ta là cái vô dụng."',
             'That night, the oak appeared in the carpenter\'s dream and said: "You compare me to useful trees? Pear, orange, apple trees — because they are useful they are stripped bare, cut down before their time. My uselessness is my use."'),
            ('Trang Tử dùng hình ảnh này để nói về người quân tử trong loạn thế: đôi khi không hữu ích theo nghĩa thông thường là điều bảo vệ bạn và cho phép bạn phát triển.',
             'Zhuangzi uses this image to speak about the wise person in turbulent times: sometimes being "useless" in the ordinary sense is what protects you and allows you to develop.'),
        ],
        'lesson_vn': 'Trong thế giới đánh giá con người theo năng suất và lợi ích, hãy nhớ: không phải mọi giá trị đều đo bằng công cụ được. Đôi khi "không hữu ích" là loại tự do cao nhất.',
        'lesson_en': 'In a world that measures people by productivity and utility, remember: not all value is measurable by usefulness. Sometimes "being useless" is the highest form of freedom.',
    },
    {
        'title_vn': 'Phước Họa Tương Sinh — Trong Họa Có Phúc',
        'title_en': 'Fortune and Misfortune Give Birth to Each Other',
        'pairs': [
            ('Trang Tử kể câu chuyện người lão nông mất con ngựa. Hàng xóm đến an ủi.',
             'Zhuangzi tells the story of an old farmer who lost his horse. Neighbors came to console him.'),
            ('"Biết đâu là họa?" ông nói.', '"Who knows if this is misfortune?" he said.'),
            ('Con ngựa trở về và dẫn theo một đàn ngựa hoang. Hàng xóm chúc mừng.',
             'The horse returned, bringing a herd of wild horses with it. Neighbors congratulated him.'),
            ('"Biết đâu là phúc?" ông nói.', '"Who knows if this is fortune?" he said.'),
            ('Con trai ông cưỡi ngựa hoang và gãy chân. Hàng xóm đến thương.',
             'His son rode one of the wild horses and broke his leg. Neighbors came to commiserate.'),
            ('"Biết đâu là họa?" ông nói lại.', '"Who knows if this is misfortune?" he said again.'),
            ('Năm sau, chiến tranh nổ ra. Tất cả trai tráng trong làng đều bị bắt lính và chết trận — chỉ có con ông vì chân tàn được ở nhà.',
             'The following year, war broke out. All the able-bodied young men in the village were conscripted and died in battle — only his son, disabled from the broken leg, remained home.'),
            ('Trang Tử kết luận: cuộc sống quá phức tạp để phán xét bất cứ sự kiện đơn lẻ nào là tốt hay xấu hoàn toàn.',
             'Zhuangzi concludes: life is too complex to judge any single event as wholly good or wholly bad.'),
        ],
        'lesson_vn': 'Khi điều xấu xảy ra, đừng vội kết luận. Khi điều tốt xảy ra, cũng đừng quá phấn khởi. Thực tại sâu hơn bất kỳ nhãn dán "tốt" hay "xấu" nào.',
        'lesson_en': 'When something bad happens, do not rush to conclusions. When something good happens, do not celebrate prematurely. Reality is deeper than any label of "good" or "bad."',
    },
    {
        'title_vn': 'Trang Tử Từ Chối Làm Quan',
        'title_en': 'Zhuangzi Refuses Official Position',
        'pairs': [
            ('Vua Sở phái sứ giả đến mời Trang Tử làm Tướng Quốc với bổng lộc lớn.',
             'The King of Chu sent messengers to invite Zhuangzi to serve as Prime Minister with great reward.'),
            ('Trang Tử đang câu cá bên sông, nghe xong và không nhìn lên: "Ta nghe rằng ở Sở có con rùa thần, đã chết ba nghìn năm, vua Sở giữ xương nó trong hộp lụa để trong miếu thờ."',
             'Zhuangzi was fishing by the river; hearing this, he did not look up: "I have heard that in Chu there is a sacred tortoise that died three thousand years ago; the king of Chu keeps its bones in a box wrapped in silk in the ancestral temple."'),
            ('"Vậy bây giờ hỏi con rùa — nó thích để xương được thờ phụng danh giá, hay thích sống và kéo đuôi trong bùn?"',
             '"Now tell me — would that tortoise prefer to have its bones honored and preserved, or would it prefer to be alive, dragging its tail in the mud?"'),
            ('Sứ giả đáp: "Thưa ngài, tất nhiên nó thích sống trong bùn."',
             'The messengers replied: "It would prefer to be alive in the mud, of course."'),
            ('Trang Tử cầm cần câu lên: "Hãy về đi. Ta cũng thích kéo đuôi trong bùn."',
             'Zhuangzi picked up his fishing rod: "Begone then. I too prefer to drag my tail in the mud."'),
        ],
        'lesson_vn': 'Tự do của tinh thần có giá trị ngang với — thậm chí hơn — quyền lực và địa vị. Đừng để người khác định nghĩa thành công cho bạn nếu nó đòi hỏi bạn phải từ bỏ bản thân mình.',
        'lesson_en': 'Freedom of spirit is worth as much as — even more than — power and status. Do not let others define success for you if it requires giving up yourself.',
    },
    {
        'title_vn': 'Tri Ngư Chi Lạc — Trang Tử Biết Niềm Vui Của Cá',
        'title_en': 'How Do You Know the Joy of Fish?',
        'pairs': [
            ('Trang Tử và Huệ Tử đang đi trên cầu bắc qua sông Hào.',
             'Zhuangzi and Huizi were walking on a bridge over the Hao River.'),
            ('Trang Tử nói: "Cá bơi thong thả thế — đó là niềm vui của cá."',
             'Zhuangzi said: "Look at those fish swimming so leisurely — that is the joy of fish."'),
            ('Huệ Tử phản bác theo kiểu tranh luận logic: "Bạn không phải là cá — làm sao bạn biết niềm vui của cá?"',
             'Huizi retorted in his logical way: "You are not a fish — how do you know the joy of fish?"'),
            ('Trang Tử đáp: "Bạn không phải là tôi — làm sao bạn biết tôi không biết niềm vui của cá?"',
             'Zhuangzi replied: "You are not me — how do you know I do not know the joy of fish?"'),
            ('Cuộc tranh luận này không có người thắng theo nghĩa logic — nhưng Trang Tử đang chỉ ra một điều sâu hơn: cảm nhận đồng cảm và nhận thức suy luận là hai loại tri thức khác nhau.',
             'This argument has no logical winner — but Zhuangzi is pointing to something deeper: empathic feeling and rational inference are two different kinds of knowledge.'),
            ('Đôi khi ta biết theo cách mà ta không thể giải thích bằng logic.',
             'Sometimes we know in ways we cannot explain through logic.'),
        ],
        'lesson_vn': 'Không phải mọi tri thức đều đi qua logic và bằng chứng. Có những thứ chỉ biết được qua cảm nhận, đồng cảm, và sự chú ý sâu sắc.',
        'lesson_en': 'Not all knowledge passes through logic and evidence. There are things only knowable through feeling, empathy, and deep attention.',
    },
    {
        'title_vn': 'Bếp Của Thiên Nhiên — Biến Hóa Không Ngừng',
        'title_en': 'The Crucible of Nature — Endless Transformation',
        'pairs': [
            ('Tứ đang lâm bệnh nặng, người bạn Tử Lê đến thăm và hỏi có giận vì bệnh không.',
             'Ziyu was gravely ill; his friend Zili came to ask if he was resentful about being sick.'),
            ('Tứ trả lời: "Không. Ta đang tự hỏi thiên nhiên sẽ biến ta thành gì tiếp theo. Có lẽ cánh tay trái ta sẽ biến thành con gà — ta sẽ dùng nó để gáy sáng. Cánh tay phải ta thành cung tên — ta sẽ bắn chim cú nướng ăn."',
             'Ziyu replied: "No. I wonder what nature will transform me into next. Perhaps my left arm will become a rooster — I will use it to herald the dawn. My right arm might become a crossbow pellet — I will use it to shoot down an owl for roasting."'),
            ('"Vạn vật đang trong quá trình biến hóa không ngừng. Tôi coi thân xác chẳng qua là chỗ tạm trú. Cuộc sống và cái chết, hiện hữu và hư vô — đều là phần của vòng quay vĩ đại."',
             '"All things are in ceaseless transformation. I regard my body as merely a temporary lodging. Life and death, existence and nonexistence — all are part of the great cycle."'),
            ('Trang Tử không dạy ta không sợ chết — ông dạy ta nhìn mình như một phần của cái gì đó lớn hơn, đang chuyển hóa chứ không chỉ đơn giản là kết thúc.',
             'Zhuangzi is not teaching us not to fear death — he is teaching us to see ourselves as part of something larger, something transforming rather than simply ending.'),
        ],
        'lesson_vn': 'Cái tôi không phải thứ bất biến. Bạn đang thay đổi mỗi ngày — tế bào, suy nghĩ, giá trị. Hãy ôm lấy sự thay đổi như bản chất chứ không phải mối đe dọa.',
        'lesson_en': 'The self is not a fixed thing. You are changing every day — cells, thoughts, values. Embrace change as your nature rather than a threat.',
    },
    {
        'title_vn': 'Đại Chí Nhàn Nhàn — Tâm Hồn Lớn Thong Thả',
        'title_en': 'The Great Soul Moves Unhurriedly',
        'pairs': [
            ('Trang Tử mở đầu sách bằng hình ảnh con chim Bằng — loài chim thần thoại khổng lồ bay chín vạn dặm lên trời.',
             'Zhuangzi opens his book with the image of the Peng bird — a mythical enormous bird that flies ninety thousand li up into the sky.'),
            ('Con ve nhỏ cười nhạo: "Tôi bay từ cây này sang cây kia, nhiều lắm là lên cao vài chục trượng — cần gì bay chín vạn dặm?"',
             'A small cicada laughs at it: "I fly from tree to tree, at most a few dozen feet high — what is the use of flying ninety thousand li?"'),
            ('Trang Tử chú thích: "Tri thức nhỏ không đủ hiểu tri thức lớn. Năm ngắn không đủ hiểu năm dài." Con nấm sáng chết không biết ngày đêm là gì. Con nhộng không biết xuân thu ra sao.',
             'Zhuangzi notes: "Small knowledge cannot encompass great knowledge. A short year cannot take in a long year." The morning mushroom knows nothing of alternating day and night. The chrysalis knows nothing of spring and autumn.'),
            ('Đây không phải bài học về sự kiêu ngạo của người biết nhiều — mà về sự khác biệt của góc nhìn: cái đúng với con ve không nhất thiết đúng với con chim Bằng.',
             'This is not a lesson about the arrogance of the knowledgeable — but about the difference in perspective: what works for the cicada does not necessarily work for the Peng bird.'),
            ('Mỗi người có định mệnh và quy mô của mình. Không nên phán xét cuộc đời người khác bằng thước đo của mình.',
             'Each person has their own destiny and scale. One should not judge others\' lives by one\'s own measure.'),
        ],
        'lesson_vn': 'Đừng để những tiếng cười nhạo của "con ve" xung quanh ngăn bạn nhắm đến tầm bay lớn hơn. Và cũng đừng cười nhạo ai có tầm nhìn khác bạn — họ có thể đang nhìn thấy điều bạn chưa thấy.',
        'lesson_en': 'Do not let the mockery of the "cicadas" around you stop you from aiming for a greater flight. And do not mock others who have a different vision — they may be seeing something you have not yet seen.',
    },
]

print("Đang tạo chương 1-4...")

make_chapter('ch01-lao-tu-dao-vo-vi', 1,
    'Lão Tử — Đạo, Vô Vi, Nước Chảy, Biết Đủ',
    'Laozi — Tao, Wu Wei, Flowing Water, Knowing Enough', ch01)

make_chapter('ch02-khong-tu-nhan-le-nghia', 2,
    'Khổng Tử — Nhân, Lễ, Nghĩa, Tu Thân',
    'Confucius — Benevolence, Ritual, Righteousness, Self-Cultivation', ch02)

make_chapter('ch03-manh-tu-tinh-thien', 3,
    'Mạnh Tử — Tính Thiện, Lòng Trắc Ẩn, Dân Vi Quý',
    'Mencius — Original Goodness, Compassion, People First', ch03)

make_chapter('ch04-trang-tu-tu-do-tam-thuc', 4,
    'Trang Tử — Tự Do Tâm Thức Và Tương Đối',
    'Zhuangzi — Freedom of Mind and Relativity', ch04)

print("Hoàn tất chương 1-4!")
