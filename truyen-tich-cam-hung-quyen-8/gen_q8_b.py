#!/usr/bin/env python3
# gen_q8_b.py -- Quyển VIII ch05-08: bắt nạt, mạng xã hội, tình bạn, chọn nghề
import os, re

CHAPTERS_DIR = os.path.join(os.path.dirname(__file__), "chapters")
os.makedirs(CHAPTERS_DIR, exist_ok=True)

def fix(s):
    s = s.replace('%', r'\%')
    s = s.replace('&', r'\&')
    s = re.sub(r'"([^"\n]*)"', r"``\1''", s)
    return s

def split_sentences(text):
    parts = re.split(r'(?<=[.!?])\s+', text.strip())
    return [part.strip() for part in parts if part.strip()]

def align_pairs(vn, en):
    vn_parts = split_sentences(vn)
    en_parts = split_sentences(en)
    if len(vn_parts) == len(en_parts) and len(vn_parts) > 1:
        return list(zip(vn_parts, en_parts))
    return [(vn, en)]

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
        for vn, en in pairs:
            for sub_vn, sub_en in align_pairs(vn, en):
                if first:
                    words = fix(sub_vn).split(' ', 1)
                    fc = words[0][0] if words[0] else ''
                    rest = words[0][1:] + (' ' + words[1] if len(words) > 1 else '')
                    lines.append(r'\chuhoa{' + fc + r'}{' + rest + r'}')
                    first = False
                else:
                    lines.append(fix(sub_vn))
                lines.append(r'\textit{(' + fix(sub_en) + r')}')
                lines.append('')
        lines.append(r'\end{truyen}')
        lines.append('')
        lines.append(r'\begin{baihoc}')
        lines.append(fix(lvn))
        lines.append(r'\textit{(' + fix(len_) + r')}')
        lines.append(r'\end{baihoc}')
        lines.append('')
        lines.append(r'\begin{ghinhoanh}')
        lines.append(r'\textbf{Short English to remember:}')
        lines.append('')
        for sentence in split_sentences(len_):
            lines.append(fix(sentence))
            lines.append('')
        lines.append(r'\end{ghinhoanh}')
        lines.append('')
        lines.append(r'\begin{tuhocnhanh}')
        lines.append(r'\textbf{Cau hoi tu hoc / Self-study questions}')
        lines.append('')
        lines.append(r'1. Van de chinh la gi? \textit{What is the main problem?}')
        lines.append('')
        lines.append(r'2. Cach xu ly tot hon la gi? \textit{What is a better action?}')
        lines.append('')
        lines.append(r'3. Mot cau tieng Anh em muon nho la cau nao? \textit{Which English sentence do you want to remember?}')
        lines.append(r'\end{tuhocnhanh}')
        if idx < len(stories):
            lines.append(r'\ngancach')
        lines.append('')
    path = os.path.join(CHAPTERS_DIR, filename + '.tex')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f'  Đã tạo: {path}')


ch05 = [
    {
        'title_vn': 'Bắt Nạt Không Phải Chuyện Đùa',
        'title_en': 'Bullying Is Not a Joke',
        'pairs': [
            ('Cả lớp cười khi một bạn bị gọi bằng biệt danh gắn với ngoại hình. Người nói bảo: "Đùa thôi mà."',
             'The whole class laughed when one student was called a nickname tied to appearance. The speaker said: "It is just a joke."'),
            ('Nhưng chỉ người bị gọi mới biết chữ đó bám theo mình cả ngày như thế nào.',
             'But only the person being called knew how that word clung to them all day.'),
            ('Nhiều kiểu bắt nạt sống nhờ vào một câu nguỵ trang: đùa thôi. Nó khiến người gây ra nhẹ tội trong mắt đám đông và khiến nạn nhân cảm thấy mình yếu đuối nếu phản ứng.',
             'Many forms of bullying survive behind one disguise: just kidding. It makes the aggressor look harmless to the crowd and makes the victim feel weak for reacting.'),
            ('Sự thật thô nhưng thật là thế này: nếu thứ em làm khiến người khác co rúm, xấu hổ, và sợ xuất hiện, thì đó không phải trò đùa. Đó là bạo lực.',
             'The blunt truth is this: if what you do makes another person shrink, feel ashamed, and fear showing up, it is not humor. It is violence.'),
        ],
        'lesson_vn': 'Dạy học sinh gọi đúng tên sự việc. Khi gọi đúng tên, các em mới đủ can đảm dừng nó.',
        'lesson_en': 'Teach students to name the event correctly. Only then will they have the courage to stop it.',
    },
    {
        'title_vn': 'Người Đứng Nhìn Cũng Có Phần',
        'title_en': 'The Bystander Has a Part Too',
        'pairs': [
            ('Một bạn bị xé vở. Ba mươi bạn khác nhìn thấy. Không ai trực tiếp ra tay ngoài hai đứa.',
             'One student had a notebook torn up. Thirty other students saw it. Only two acted directly.'),
            ('Nhưng sự im lặng của ba mươi người còn lại chính là thứ khiến hai đứa kia thấy mình có quyền.',
             'But the silence of the other thirty was exactly what made the two feel entitled.'),
            ('Nhiều học sinh tự an ủi: "Mình đâu làm gì." Đúng, nhưng các em cũng đã không làm gì để chặn lại.',
             'Many students comfort themselves with: "I did nothing." True, but they also did nothing to stop it.'),
            ('Không phải ai cũng đủ sức lao vào đối đầu. Nhưng tối thiểu có thể báo giáo viên, ngồi cạnh nạn nhân, hoặc từ chối cười theo.',
             'Not everyone is strong enough to intervene openly. But at minimum, one can tell a teacher, sit beside the victim, or refuse to laugh along.'),
        ],
        'lesson_vn': 'Trong bắt nạt học đường, trung lập thường vô tình đứng về phía kẻ mạnh. Học sinh cần học rằng im lặng cũng là một lựa chọn đạo đức.',
        'lesson_en': 'In school bullying, neutrality often ends up serving the stronger side. Students must learn that silence is also a moral choice.',
    },
    {
        'title_vn': 'Nạn Nhân Không Cần Lời Khuyên Rẻ Tiền',
        'title_en': 'Victims Do Not Need Cheap Advice',
        'pairs': [
            ('Khi một bạn kể mình bị bắt nạt, điều đầu tiên các bạn khác thường nói là: "Kệ đi, đừng để ý."',
             'When someone admits being bullied, the first thing others often say is: "Ignore it. Do not care."'),
            ('Nghe đơn giản, nhưng người đang bị cô lập đâu thể bật tắt cảm xúc như công tắc.',
             'It sounds simple, but a person being isolated cannot switch emotions on and off like a button.'),
            ('Có bạn cần được tin, cần được ngồi cạnh, cần một người lớn can thiệp, chứ không cần thêm một câu khuyên thể hiện rằng nỗi đau của mình quá bé để ai phải bận tâm.',
             'Some students need to be believed, need company, need an adult to intervene, not another piece of advice implying that their pain is too small to matter.'),
            ('Cách giúp tử tế nhất đôi khi rất ngắn: "Tao tin mày. Chuyện này không ổn. Tao sẽ đi cùng mày báo cô."',
             'The kindest help is sometimes very short: "I believe you. This is not okay. I will go with you to tell the teacher."'),
        ],
        'lesson_vn': 'Hỗ trợ thật không phải là ném lời khuyên cho nhanh. Hỗ trợ thật là chia bớt gánh nặng và đưa nạn nhân về phía an toàn.',
        'lesson_en': 'Real support is not tossing out quick advice. Real support shares the burden and moves the victim toward safety.',
    },
    {
        'title_vn': 'Kẻ Bắt Nạt Cũng Thường Là Một Đứa Trẻ Có Vấn Đề',
        'title_en': 'A Bully Is Often Also a Child in Trouble',
        'pairs': [
            ('Nói thế không phải để bao che. Kẻ bắt nạt phải chịu trách nhiệm.',
             'That does not excuse anything. A bully must be held responsible.'),
            ('Nhưng nếu chỉ phạt mà không hiểu gốc, nhà trường chỉ dập lửa ở ngọn.',
             'But if a school only punishes without understanding the root, it is only beating flames at the surface.'),
            ('Có đứa bị bạo lực ở nhà nên mang bạo lực đến trường. Có đứa yếu cảm giác giá trị nên phải dìm người khác để thấy mình mạnh. Có đứa chỉ học được rằng ai yếu thì đáng bị nghiền.',
             'Some children are harmed at home and bring harm to school. Some feel so little worth that they push others down to feel strong. Some simply learned that the weak deserve to be crushed.'),
            ('Xử lý bắt nạt phải vừa cứng vừa sâu: chặn hành vi ngay, bảo vệ nạn nhân ngay, nhưng cũng phải giáo dục lại kẻ gây ra trước khi nó lớn lên thành một người tàn nhẫn hơn.',
             'Handling bullying requires both firmness and depth: stop the behavior immediately, protect the victim immediately, and also re-educate the aggressor before that child grows into a crueler adult.'),
        ],
        'lesson_vn': 'Kỷ luật tốt không chỉ để phạt. Kỷ luật tốt phải bảo vệ nạn nhân và chặn quá trình một đứa trẻ đang học cách làm ác.',
        'lesson_en': 'Good discipline is not only for punishment. It must protect the victim and interrupt a child who is learning how to do harm.',
    },
]

ch06 = [
    {
        'title_vn': 'Mạng Xã Hội Là Sân Khấu, Không Phải Toàn Bộ Đời Sống',
        'title_en': 'Social Media Is a Stage, Not a Whole Life',
        'pairs': [
            ('Lên mạng, em thấy người ta luôn đẹp hơn, giỏi hơn, vui hơn, thành công hơn.',
             'Online, everyone seems prettier, smarter, happier, and more successful.'),
            ('Điều đó không lạ. Sân khấu nào chả được chọn góc đẹp nhất trước khi bật đèn.',
             'That is not strange. Every stage is arranged for its best angle before the lights go on.'),
            ('Một học sinh nhìn ảnh bạn bè đi chơi rồi thấy mình thua thiệt. Nhưng em không thấy bức ảnh đó được chụp sau ba mươi lần chọn góc, không thấy hôm trước họ vừa cãi nhau, không thấy khoản nợ mà gia đình phải gánh.',
             'A student sees friends traveling and feels deprived. But she does not see the thirty attempts behind the photo, the argument the day before, or the debt the family carries.'),
            ('Mạng xã hội không nói dối hoàn toàn. Nó chỉ kể sự thật đã được cắt gọt.',
             'Social media is not a total lie. It is a heavily edited truth.'),
        ],
        'lesson_vn': 'Dạy học sinh rằng hình ảnh đẹp không phải bằng chứng của cuộc đời đẹp. Khả năng phân biệt sân khấu với đời thật là một kỹ năng sống.',
        'lesson_en': 'Teach students that beautiful images are not proof of a beautiful life. Distinguishing stage from reality is a life skill.',
    },
    {
        'title_vn': 'Nghiện Sự Công Nhận Là Chiếc Xiềng Mềm',
        'title_en': 'Addiction to Validation Is a Soft Chain',
        'pairs': [
            ('Có học sinh đăng bài xong cứ năm phút lại mở điện thoại xem có ai thả tim chưa.',
             'Some students post something and then check every five minutes to see who liked it.'),
            ('Mỗi lượt thích là một mẩu đường nhỏ. Ngọt, nhanh, và không nuôi nổi điều gì lâu dài.',
             'Each like is a tiny piece of sugar. Sweet, fast, and unable to nourish anything lasting.'),
            ('Khi giá trị bản thân bị buộc vào phản ứng của người khác, học sinh sẽ dần đánh mất quyền tự đánh giá mình.',
             'When self-worth is tied to others’ reactions, students slowly lose the ability to evaluate themselves.'),
            ('Sự lệ thuộc này rất mềm. Nó không ồn ào như thuốc hay cờ bạc, nhưng nó bẻ cong hành vi mỗi ngày: chụp gì, nói gì, mặc gì, sống thế nào.',
             'This dependence is soft. It is not loud like drugs or gambling, but it bends daily behavior: what to photograph, what to say, what to wear, how to live.'),
        ],
        'lesson_vn': 'Học sinh cần được tập làm việc tốt ngay cả khi không ai nhìn. Tự trọng bắt đầu ở chỗ đó.',
        'lesson_en': 'Students need practice doing good work even when no one is watching. Self-respect begins there.',
    },
    {
        'title_vn': 'Tin Đồn Trên Mạng Cắn Rất Lâu',
        'title_en': 'Rumors Online Bite for a Long Time',
        'pairs': [
            ('Ngày xưa một câu nói xấu chỉ loanh quanh trong lớp. Bây giờ một ảnh chụp màn hình có thể chạy khắp trường trong một tối.',
             'In the past, a nasty comment might circle inside one classroom. Now a screenshot can spread across the whole school in one evening.'),
            ('Người tung tin thường chỉ nghĩ: gửi cho vui. Nhưng người bị nhắc tên có thể mất ngủ hàng tuần.',
             'The person sharing it often thinks: just for fun. The person named in it may lose sleep for weeks.'),
            ('Môi trường số làm cho sự tàn nhẫn trở nên dễ hơn vì người ta không phải nhìn thẳng gương mặt đau của người bị hại.',
             'Digital spaces make cruelty easier because people do not have to look directly at the hurt face of the person harmed.'),
            ('Nhà trường dạy công thức, nhưng cũng phải dạy học sinh rằng một lần bấm gửi có thể để lại hậu quả lâu hơn cả một bài kiểm tra trượt.',
             'Schools teach formulas, but they must also teach students that pressing send once can cause damage longer than failing a test.'),
        ],
        'lesson_vn': 'Đạo đức trên mạng không phải môn phụ. Với học sinh hôm nay, nó là kỹ năng an toàn cơ bản.',
        'lesson_en': 'Digital ethics is not an extra subject. For today’s students, it is a basic safety skill.',
    },
    {
        'title_vn': 'Cần Có Những Khoảng Không Màn Hình',
        'title_en': 'You Need Spaces Without Screens',
        'pairs': [
            ('Có em than mình không tập trung được nữa. Đọc vài dòng đã muốn cầm điện thoại.',
             'Some students complain that they can no longer focus. After a few lines, they want to grab the phone.'),
            ('Não quen với nội dung ngắn, nhanh, giật mạnh sẽ thấy việc học sâu như một cực hình.',
             'A brain trained by short, fast, highly stimulating content will experience deep study as torture.'),
            ('Không phải học sinh lười hơn. Nhiều khi môi trường số đã bẻ não các em theo hướng khó ngồi yên.',
             'It is not always that students have become lazier. Often the digital environment has bent their minds toward restlessness.'),
            ('Giải pháp không hào nhoáng: những khoảng không màn hình, những giờ học không điện thoại, những buổi đi bộ không tai nghe, những cuốn sách giấy đọc chậm.',
             'The solution is not glamorous: spaces without screens, study hours without phones, walks without earphones, paper books read slowly.'),
        ],
        'lesson_vn': 'Muốn lấy lại khả năng tập trung, học sinh phải chấp nhận kỷ luật với thiết bị. Không có sự tập trung nào lớn lên giữa một cơn nghiện kích thích liên tục.',
        'lesson_en': 'To regain focus, students must accept discipline with devices. No real concentration grows inside constant stimulation addiction.',
    },
]

ch07 = [
    {
        'title_vn': 'Bạn Đông Không Có Nghĩa Là Bớt Cô Đơn',
        'title_en': 'Having Many Friends Does Not Mean Feeling Less Alone',
        'pairs': [
            ('Một học sinh có thể ngồi giữa nhóm bạn rất đông mà vẫn thấy lạc lõng.',
             'A student can sit among many friends and still feel out of place.'),
            ('Bởi vì số lượng người quanh em không quyết định độ sâu của kết nối.',
             'Because the number of people around you does not determine the depth of connection.'),
            ('Có những nhóm chỉ tồn tại nhờ nói chuyện phiếm, chụp ảnh chung, và giữ nhau khỏi bị lẻ loi. Nhưng hễ ai gặp chuyện thật, cả nhóm biến mất.',
             'Some groups exist only for small talk, group photos, and avoiding loneliness. But when someone faces a real problem, the whole group disappears.'),
            ('Một người bạn thật không cần xuất hiện suốt ngày. Họ chỉ cần xuất hiện đúng lúc và không giả vờ.',
             'A real friend does not need to appear all the time. They only need to appear at the right time and not pretend.'),
        ],
        'lesson_vn': 'Dạy học sinh đừng đo tình bạn bằng số lượng tương tác. Hãy đo bằng độ thật khi có khó khăn.',
        'lesson_en': 'Teach students not to measure friendship by the number of interactions. Measure it by honesty when trouble arrives.',
    },
    {
        'title_vn': 'Bạn Tốt Không Luôn Chiều Em',
        'title_en': 'A Good Friend Does Not Always Please You',
        'pairs': [
            ('Có người gọi mình là bạn thân nhưng luôn cổ vũ mọi quyết định bốc đồng của mình. Nghe rất sướng.',
             'Some people call themselves close friends and encourage every impulsive decision you make. It feels great.'),
            ('Nhưng người dám nói: "Mày đang sai" mới là người có nguy cơ mất lòng vì muốn giữ mày.',
             'But the one who dares say: "You are wrong" risks your displeasure because they want to keep you safe.'),
            ('Tình bạn thật không chỉ là chia vui. Nó còn là can đảm kéo nhau lại khi một đứa đang trượt xuống.',
             'Real friendship is not only about sharing fun. It is also the courage to pull each other back when one starts sliding down.'),
            ('Học sinh cần hiểu sự khác nhau giữa người làm mình vui và người làm mình tốt hơn. Hai kiểu đó có khi không trùng nhau.',
             'Students need to understand the difference between someone who makes you feel good and someone who helps you become better. Those two are not always the same person.'),
        ],
        'lesson_vn': 'Một lời nhắc khó nghe đúng lúc đáng giá hơn mười câu chiều theo. Tình bạn tử tế không nuông chiều sự tự hủy.',
        'lesson_en': 'One hard truth at the right time is worth more than ten pleasing lies. Decent friendship does not indulge self-destruction.',
    },
    {
        'title_vn': 'Đừng Ở Lại Chỉ Vì Sợ Mất Nhóm',
        'title_en': 'Do Not Stay Just Because You Fear Losing the Group',
        'pairs': [
            ('Nhiều học sinh ở trong một nhóm bạn khiến mình mệt, chỉ vì sợ đi ra sẽ không còn ai.',
             'Many students stay in draining friend groups only because they fear having no one if they leave.'),
            ('Họ cười theo những câu nói ác, tham gia những trò khiến mình thấy bẩn, và gọi đó là hòa nhập.',
             'They laugh at cruel jokes, join in actions that make them feel dirty, and call it fitting in.'),
            ('Nhưng cái giá của việc thuộc về một nhóm độc hại là đánh mất sự tôn trọng chính mình.',
             'But the price of belonging to a toxic group is the loss of self-respect.'),
            ('Có những cô đơn sạch sẽ hơn rất nhiều so với một tình bạn làm em hỏng người.',
             'Some forms of loneliness are far cleaner than a friendship that corrupts you.'),
        ],
        'lesson_vn': 'Hãy dạy học sinh rằng thuộc về không đáng giá nếu cái giá là phải phản bội điều đúng. Một nhóm không đáng để đổi lấy nhân cách.',
        'lesson_en': 'Teach students that belonging is not worth it if the price is betraying what is right. No group is worth your character.',
    },
    {
        'title_vn': 'Tình Bạn Cũng Cần Ranh Giới',
        'title_en': 'Friendship Also Needs Boundaries',
        'pairs': [
            ('Có bạn thân mượn bài mãi, nhờ làm hộ mãi, trút hết cảm xúc tiêu cực lên mình mãi.',
             'Some close friends keep borrowing homework, asking for favors, and dumping endless negative emotion on you.'),
            ('Nhiều học sinh chịu đựng vì sợ nói ra sẽ mất bạn.',
             'Many students tolerate this because they fear speaking up will cost them the friendship.'),
            ('Nhưng một mối quan hệ chỉ sống được bằng sự im lặng của một phía thì nó vốn đã lệch.',
             'But a relationship that survives only because one side stays silent is already distorted.'),
            ('Nói "tao không làm hộ mày nữa" hay "hôm nay tao không đủ sức nghe thêm" không phải ích kỷ. Đó là giữ đường biên để cả hai còn tôn trọng nhau.',
             'Saying "I will not do it for you anymore" or "I do not have the energy to hear more today" is not selfish. It is drawing a line so mutual respect can survive.'),
        ],
        'lesson_vn': 'Tình bạn tốt không nuốt chửng cá nhân. Học sinh cần biết giúp người khác mà không biến mình thành chỗ bị khai thác.',
        'lesson_en': 'A good friendship does not swallow the individual. Students must learn to help others without becoming something to exploit.',
    },
]

ch08 = [
    {
        'title_vn': 'Nhiều Học Sinh Chọn Nghề Để Tránh Bị Chê',
        'title_en': 'Many Students Choose Careers to Avoid Criticism',
        'pairs': [
            ('Khi được hỏi muốn học gì, không ít học sinh trả lời bằng thứ người khác sẽ nghĩ, không phải thứ mình thực sự muốn.',
             'When asked what they want to study, many students answer with what others will approve of, not what they truly want.'),
            ('Các em sợ học ngành bị coi là thấp, sợ họ hàng hỏi thu nhập, sợ bạn bè khoe trường danh giá hơn.',
             'They fear entering a field considered low status, fear relatives asking about income, fear classmates boasting about more prestigious schools.'),
            ('Thế là các em chọn một con đường đủ an toàn để khỏi bị chê, rồi mang nỗi chán đó đi suốt nhiều năm.',
             'So they choose a path safe enough to avoid criticism, then carry that deadness for years.'),
            ('Lựa chọn nghề nghiệp mà chỉ dựa trên ánh mắt thiên hạ rất dễ biến cuộc đời thành một màn trình diễn dài.',
             'A career choice based only on public opinion easily turns life into one long performance.'),
        ],
        'lesson_vn': 'Định hướng nghề nghiệp phải bắt đầu từ năng lực, khí chất và giá trị sống, không chỉ từ danh tiếng bề ngoài.',
        'lesson_en': 'Career guidance must begin with ability, temperament, and values, not only external prestige.',
    },
    {
        'title_vn': 'Đam Mê Không Đủ, Nhưng Không Có Nó Cũng Rất Mệt',
        'title_en': 'Passion Is Not Enough, But Having None Is Exhausting',
        'pairs': [
            ('Người lớn hay nói: cứ có đam mê là được. Câu đó đẹp nhưng thiếu.',
             'Adults often say: passion is enough. It sounds nice, but it is incomplete.'),
            ('Đam mê không thay thế được năng lực, kỷ luật, và nhu cầu thị trường.',
             'Passion does not replace ability, discipline, and market reality.'),
            ('Nhưng ngược lại, học một ngành mình hoàn toàn không thấy ý nghĩa cũng là một kiểu mòn mỏi rất thật.',
             'But the opposite is also true: studying a field you find no meaning in creates a very real kind of erosion.'),
            ('Học sinh cần được dạy một phiên bản trưởng thành hơn: hãy tìm giao điểm giữa điều mình có thể làm tốt, điều mình thấy đáng làm, và điều xã hội cần.',
             'Students need a more mature version of the advice: find the overlap between what you can do well, what you find worth doing, and what society needs.'),
        ],
        'lesson_vn': 'Định hướng tốt không thần thánh hóa đam mê, nhưng cũng không chà nát nó. Nó giúp học sinh nhìn nghề bằng cả trái tim lẫn đầu óc.',
        'lesson_en': 'Good guidance does not worship passion, but it does not crush it either. It helps students view work with both heart and mind.',
    },
    {
        'title_vn': 'Không Ai Mười Bảy Tuổi Mà Hiểu Hết Mình',
        'title_en': 'No One Fully Understands Themselves at Seventeen',
        'pairs': [
            ('Nhiều học sinh lo vì mình chưa biết chắc muốn gì. Các em tưởng chỉ có mình mơ hồ.',
             'Many students panic because they are not sure what they want. They think only they are uncertain.'),
            ('Sự thật là phần lớn người lớn cũng từng mù mờ ở tuổi đó. Nhiều người ba mươi vẫn đang chỉnh lại hướng đi.',
             'The truth is that most adults were also unclear at that age. Many people are still adjusting course at thirty.'),
            ('Vấn đề không phải em chưa biết hết. Vấn đề là em có đang chịu khám phá nghiêm túc hay không.',
             'The problem is not that you do not know everything. The problem is whether you are willing to explore seriously.'),
            ('Thử việc nhỏ, đọc sâu về nghề, nói chuyện với người trong ngành, quan sát chính mình khi làm một việc cụ thể. Đó là cách biết dần, không phải ngồi chờ một tiếng gọi huyền bí.',
             'Try small tasks, read deeply about fields, talk to people doing the work, observe yourself doing something concrete. That is how clarity grows, not by waiting for a mystical calling.'),
        ],
        'lesson_vn': 'Hãy giảm áp lực phải biết ngay tất cả. Điều học sinh cần là tiến gần hơn tới câu trả lời bằng hành động thật.',
        'lesson_en': 'Reduce the pressure to know everything immediately. What students need is to move closer to answers through real action.',
    },
    {
        'title_vn': 'Đừng Giao Cả Cuộc Đời Cho Một Trào Lưu',
        'title_en': 'Do Not Hand Your Life to a Trend',
        'pairs': [
            ('Cứ vài năm lại có một nghề được tung hô như lối tắt thành công.',
             'Every few years, a profession is marketed as the shortcut to success.'),
            ('Học sinh dễ bị cuốn vào những câu như nghề hot, lương cao, tương lai sáng mà quên hỏi: mình có hợp không, có chịu được không, có muốn sống kiểu đó lâu dài không.',
             'Students are easily pulled in by phrases like hot field, high salary, bright future, and forget to ask: does it suit me, can I endure it, do I want that lifestyle long-term?'),
            ('Một nghề có thể đang được thị trường săn đón, nhưng nếu nó làm em kiệt quệ mỗi ngày, cái giá sẽ rất đắt.',
             'A job may be highly demanded by the market, but if it drains you every day, the price will be high.'),
            ('Chọn nghề theo trào lưu có thể giúp em đỡ bị lạc trong ngắn hạn, nhưng dễ làm em lạc sâu hơn về sau.',
             'Choosing by trend may reduce uncertainty in the short term, but can make you more lost later.'),
        ],
        'lesson_vn': 'Học sinh cần được dạy cách nhìn xa hơn danh sách nghề hot. Nghề đáng theo là nghề em có thể lớn lên cùng nó, không chỉ chạy theo nó.',
        'lesson_en': 'Students need to be taught to look beyond lists of trendy jobs. A worthy profession is one you can grow with, not merely chase.',
    },
]

ch05.extend([
    {
        'title_vn': 'Tên Gọi Dính Như Keo',
        'title_en': 'A Nickname That Sticks Like Glue',
        'pairs': [
            ('Ngày xưa trong lớp học làng, một cậu bé nói lắp bị gọi bằng biệt danh suốt nhiều năm.',
             'Long ago in a village classroom, a boy who stuttered was called by a mocking nickname for years.'),
            ('Đám trẻ nói cho vui. Thầy cũ nghe thấy cũng bỏ qua vì nghĩ chỉ là chuyện trẻ con.',
             'The children said it for fun. The old teacher heard it and ignored it, thinking it was only childish behavior.'),
            ('Nhưng cậu bé dần ít nói hẳn, không dám đọc bài, rồi ghét luôn cả việc đến lớp.',
             'But the boy gradually stopped speaking, no longer dared to read aloud, and eventually hated coming to class.'),
            ('Một lời chế giễu lặp lại đủ lâu sẽ thôi không còn là tiếng cười. Nó biến thành căn phòng nhốt người ta lại.',
             'A repeated mockery, carried on long enough, stops being laughter. It becomes a room that imprisons a person.'),
        ],
        'lesson_vn': 'Bắt nạt không cần đến nắm đấm mới gây thương tích. Nhiều vết thương học đường sống bằng lời nói và kéo dài rất lâu.',
        'lesson_en': 'Bullying does not require fists to injure. Many school wounds live through words and last a very long time.',
    },
    {
        'title_vn': 'Thầy Giáo Mới Và Chiếc Ghế Cuối Lớp',
        'title_en': 'The New Teacher and the Back-Row Seat',
        'pairs': [
            ('Một thầy giáo mới vào lớp và thấy có một học sinh luôn bị đẩy xuống ngồi cuối, đồ dùng hay bị giấu mất.',
             'A new teacher entered a class and noticed one student was always pushed to the back and often had belongings hidden.'),
            ('Thầy không mắng ngay giữa lớp. Thầy đổi chỗ ngồi, quan sát thêm, rồi gọi riêng từng em lên hỏi.',
             'He did not scold the class immediately. He changed the seating, observed more, and then called students in one by one.'),
            ('Hóa ra cả lớp đã quen với việc một bạn bị đùa dai đến mức không ai còn thấy đó là chuyện lạ.',
             'It turned out the whole class had become so used to one student being targeted that no one saw it as unusual anymore.'),
            ('Cái nguy của bạo lực lặp đi lặp lại là nó được bình thường hóa.',
             'The danger of repeated harm is that it becomes normalized.'),
        ],
        'lesson_vn': 'Muốn chặn bắt nạt, người lớn phải nhìn được những điều lớp học đã coi là bình thường từ lâu.',
        'lesson_en': 'To stop bullying, adults must see what the classroom has long begun treating as normal.',
    },
    {
        'title_vn': 'Kẻ Mạnh Miệng Nhưng Yếu Người',
        'title_en': 'Loud but Weak Inside',
        'pairs': [
            ('Một cậu học sinh hay chặn đường bắt nạt bạn nhỏ hơn. Trước đám đông em rất lì.',
             'A student often cornered and bullied smaller classmates. In front of crowds he seemed fearless.'),
            ('Nhưng khi cô tư vấn trò chuyện riêng, em bật ra chuyện mình thường xuyên bị chửi ở nhà và chưa bao giờ thấy mình có giá trị.',
             'But in a private counseling session, he revealed that he was often verbally abused at home and had never felt valuable.'),
            ('Điều đó không làm hành vi của em bớt sai. Nhưng nó cho thấy sự hung hăng đôi khi là chiếc áo khoác của yếu đuối.',
             'This did not make his actions less wrong. But it showed that aggression is sometimes the coat worn by weakness.'),
            ('Nếu nhà trường chỉ ghét kẻ bắt nạt mà không hiểu cơ chế tạo ra nó, vòng lặp sẽ còn tiếp tục.',
             'If a school only hates the bully and does not understand the mechanism producing him, the cycle will continue.'),
        ],
        'lesson_vn': 'Kỷ luật cần đi cùng hiểu biết. Không phải để mềm tay, mà để chặn đúng gốc của cái ác nhỏ đang lớn lên.',
        'lesson_en': 'Discipline must be paired with understanding. Not to go soft, but to interrupt the root of a small cruelty that is growing.',
    },
    {
        'title_vn': 'Tiếng Cười Trong Hành Lang',
        'title_en': 'The Laughter in the Corridor',
        'pairs': [
            ('Một bạn nữ đi ngang hành lang và nghe sau lưng mình có tiếng cười. Không ai gọi tên em, nhưng em biết họ đang cười mình.',
             'A girl walked down the corridor and heard laughter behind her. No one called her name, yet she knew they were laughing at her.'),
            ('Kiểu bắt nạt này khó nắm hơn vì nó để lại rất ít bằng chứng. Nhưng nạn nhân vẫn đau thật.',
             'This kind of bullying is harder to catch because it leaves little evidence. But the victim still hurts for real.'),
            ('Có những tổn thương học đường đến từ bầu không khí chứ không chỉ từ một hành vi cụ thể.',
             'Some school injuries come from an atmosphere, not only from one concrete act.'),
            ('Một môi trường khiến học sinh phải đoán xem tiếng cười nào là dành cho mình là một môi trường đang có vấn đề.',
             'An environment where students must guess which laugh is directed at them is an environment with a problem.'),
        ],
        'lesson_vn': 'Không phải bạo lực nào cũng rõ ràng. Người lớn cần tinh hơn với những dạng tổn thương không có dấu vết vật lý.',
        'lesson_en': 'Not every form of harm is obvious. Adults must become sharper in noticing injuries without physical marks.',
    },
    {
        'title_vn': 'Bảo Vệ Bạn Làm Em Mất Vai Trò “An Toàn”',
        'title_en': 'Protecting Someone Costs the Safe Position',
        'pairs': [
            ('Một học sinh chứng kiến bạn bị cô lập. Em biết nếu mình bênh, nhóm kia có thể quay sang loại cả mình.',
             'A student watched a classmate being isolated. She knew that if she defended him, the group might turn and exclude her too.'),
            ('Im lặng là lựa chọn an toàn nhất. Và cũng là lựa chọn khiến em khó nhìn thẳng vào mình nhất.',
             'Silence was the safest option. It was also the one that made it hardest for her to look herself in the eye.'),
            ('Cuối cùng em chỉ làm một việc nhỏ: ngồi cạnh bạn ấy trong giờ ăn trưa. Nhỏ, nhưng đủ để phá nứt bức tường cô lập.',
             'In the end she did one small thing: she sat beside him at lunch. Small, but enough to crack the wall of isolation.'),
            ('Chống bắt nạt không phải lúc nào cũng là bài diễn văn lớn. Nhiều khi nó chỉ là không bỏ một người ngồi một mình.',
             'Fighting bullying is not always a grand speech. Often it is simply refusing to leave someone alone.'),
        ],
        'lesson_vn': 'Học sinh cần những hành động can đảm vừa tầm, không phải lúc nào cũng anh hùng kiểu sân khấu.',
        'lesson_en': 'Students need forms of courage they can realistically enact, not only heroic stage-like gestures.',
    },
    {
        'title_vn': 'Kỷ Luật Để Giữ Người, Không Chỉ Để Giữ Mặt Mũi Trường',
        'title_en': 'Discipline to Protect People, Not Just the School’s Image',
        'pairs': [
            ('Có trường xử lý bắt nạt rất chậm vì sợ ồn ào, sợ phụ huynh bàn tán, sợ ảnh hưởng danh tiếng.',
             'Some schools handle bullying slowly because they fear noise, parental talk, and damage to reputation.'),
            ('Trong lúc người lớn lo giữ mặt mũi, học sinh bị hại vẫn phải bước vào lớp mỗi ngày với nỗi sợ nguyên vẹn.',
             'While adults worry about image, the harmed student still walks into class every day with intact fear.'),
            ('Một ngôi trường có danh tiếng đẹp nhưng để học sinh sống trong sợ hãi thì cái đẹp đó rất rỗng.',
             'A school with a polished reputation but fearful students holds a hollow kind of beauty.'),
            ('Kỷ luật đúng không phải để sự việc biến mất trên giấy tờ. Kỷ luật đúng là để người yếu không bị bỏ mặc.',
             'Proper discipline is not to make incidents disappear from paperwork. Proper discipline is to ensure the vulnerable are not abandoned.'),
        ],
        'lesson_vn': 'Danh tiếng nhà trường chỉ đáng giữ khi nó được xây trên sự an toàn thật của học sinh.',
        'lesson_en': 'A school’s reputation is worth preserving only when it rests on real student safety.',
    },
])

ch06.extend([
    {
        'title_vn': 'Chiếc Gương Đồng Và Bộ Lọc Ảnh',
        'title_en': 'The Bronze Mirror and the Photo Filter',
        'pairs': [
            ('Ngày xưa người ta soi mình trong gương đồng, hình đã méo sẵn. Bây giờ học sinh soi mình qua bộ lọc ảnh, hình còn méo hơn.',
             'Long ago people looked into bronze mirrors, where the image was already distorted. Today students look through photo filters, where the image is distorted even more.'),
            ('Khác thời đại nhưng giống bản chất: con người rất dễ lầm cái hình đã sửa với con người thật.',
             'Different eras, same essence: human beings easily mistake the altered image for the real person.'),
            ('Một bạn nữ chụp hàng chục ảnh mới dám đăng một. Rồi sau đó nhìn mặt mộc của mình và thấy thất vọng.',
             'One girl took dozens of photos before daring to post one. Afterwards she looked at her natural face and felt disappointed.'),
            ('Khi công nghệ làm cho chuẩn đẹp trở nên giả tạo hơn, lòng tự ti cũng có thêm nhiên liệu.',
             'When technology makes standards of beauty more artificial, insecurity gains more fuel.'),
        ],
        'lesson_vn': 'Mạng xã hội không chỉ chỉnh ảnh; nó còn chỉnh chuẩn trong đầu học sinh. Cần dạy các em nhận ra điều đó.',
        'lesson_en': 'Social media does not only edit photos; it edits standards inside students’ minds. They need to be taught to notice that.',
    },
    {
        'title_vn': 'Đứa Trẻ Sống Bằng Thông Báo',
        'title_en': 'The Child Living by Notifications',
        'pairs': [
            ('Một học sinh kể rằng em thấy bồn chồn hễ điện thoại im lặng quá lâu.',
             'A student admitted feeling restless whenever the phone stayed quiet too long.'),
            ('Thông báo đến không chỉ mang tin. Nó mang cảm giác mình vẫn được nhớ tới.',
             'A notification brings not only information. It also brings the feeling of still being remembered.'),
            ('Khi không có gì hiện lên, em thấy mình như biến mất một chút.',
             'When nothing appears, the student feels a little as if disappearing.'),
            ('Đó là lúc công cụ liên lạc đã chạm sang vùng định nghĩa giá trị bản thân.',
             'That is the moment when a communication tool has crossed into defining self-worth.'),
        ],
        'lesson_vn': 'Nếu sự im lặng của điện thoại làm em hoảng, vấn đề không còn là thiết bị nữa. Nó đã thành câu chuyện về sự lệ thuộc cảm xúc.',
        'lesson_en': 'If the silence of a phone makes you panic, the issue is no longer the device. It has become emotional dependence.',
    },
    {
        'title_vn': 'Tin Vịt Nhanh Hơn Thầy Cô',
        'title_en': 'Rumors Travel Faster Than Teachers',
        'pairs': [
            ('Một tin giả về giáo viên hay học sinh có thể chạy khắp trường trước cả giờ ra chơi kết thúc.',
             'A false rumor about a teacher or student can spread across a school before recess is over.'),
            ('Ngày xưa lời đồn đi bộ. Bây giờ nó đi bằng mạng, nên tốc độ phá hỏng danh dự cũng lớn hơn nhiều.',
             'In the past rumors walked. Now they travel by networks, so the speed of reputational harm is far greater.'),
            ('Một học sinh chuyển tiếp vì không chịu nổi áp lực từ tin đồn mà không ai chịu gỡ.',
             'One student transferred because the pressure of an uncorrected rumor became unbearable.'),
            ('Kỹ năng kiểm chứng thông tin bây giờ không chỉ là kỹ năng học tập. Nó là kỹ năng đạo đức.',
             'The skill of verifying information is no longer only an academic skill. It is an ethical one.'),
        ],
        'lesson_vn': 'Trước khi bấm chia sẻ, học sinh cần học cách dừng lại. Một lần dừng đúng lúc có thể cứu người khác khỏi rất nhiều ngày tối tăm.',
        'lesson_en': 'Before pressing share, students need to learn how to pause. One timely pause can save someone many dark days.',
    },
    {
        'title_vn': 'Bộ Não Mỏi Vì Cuộn Mãi',
        'title_en': 'The Brain Tired by Endless Scrolling',
        'pairs': [
            ('Một học sinh bảo mình không hề làm gì nặng mà vẫn rất mệt. Em chỉ nằm và lướt điện thoại hàng giờ.',
             'A student said he had done nothing strenuous yet felt very tired. He had only lain down and scrolled for hours.'),
            ('Lướt liên tục tưởng là nghỉ, nhưng thật ra não vẫn bị kéo đi bởi chuỗi kích thích ngắn không dứt.',
             'Continuous scrolling feels like rest, but the brain is still being dragged by an endless chain of short stimuli.'),
            ('Kết quả là nghỉ xong mà không hồi được, học vào cũng không sâu nổi.',
             'The result is rest that does not restore, and study that cannot go deep.'),
            ('Không phải mọi hình thức nghỉ đều phục hồi. Có kiểu nghỉ chỉ làm mình đờ hơn.',
             'Not every form of rest restores. Some forms only make us duller.'),
        ],
        'lesson_vn': 'Học sinh cần học phân biệt giữa giải trí và phục hồi. Hai thứ đó không phải lúc nào cũng trùng nhau.',
        'lesson_en': 'Students need to distinguish entertainment from recovery. The two are not always the same.',
    },
    {
        'title_vn': 'Một Ngày Không Mạng',
        'title_en': 'One Day Offline',
        'pairs': [
            ('Một lớp được giao bài tập lạ: một ngày cuối tuần không mạng xã hội rồi viết lại cảm giác của mình.',
             'One class received an unusual assignment: spend one weekend day without social media and then write about the experience.'),
            ('Nhiều em tưởng sẽ rất dễ. Đến trưa đã thấy tay ngứa ngáy vì muốn cầm máy.',
             'Many thought it would be easy. By noon their hands already twitched to pick up the phone.'),
            ('Tối đến, một số em viết rằng mình thấy thời gian dài hơn, yên hơn, nhưng cũng trống hơn.',
             'By evening, some wrote that time felt longer, quieter, but also emptier.'),
            ('Bài tập đó không nhằm tôn thờ đời sống không công nghệ. Nó chỉ giúp học sinh thấy mình đang lệ thuộc đến đâu.',
             'The exercise was not about glorifying a life without technology. It simply helped students see how dependent they had become.'),
        ],
        'lesson_vn': 'Muốn quản lý một thứ, trước hết phải thấy mức độ nó đang quản lý mình. Khoảng tách ra là cách nhìn rõ nhất.',
        'lesson_en': 'To manage something, you must first see how much it already manages you. Distance is often the clearest lens.',
    },
    {
        'title_vn': 'Học Sâu Trong Thời Đại Hời Hợt',
        'title_en': 'Deep Study in a Shallow Age',
        'pairs': [
            ('Ngày xưa người ta sợ thiếu sách. Bây giờ học sinh chìm trong quá nhiều nội dung nhưng lại thiếu chiều sâu.',
             'In the past people feared a lack of books. Now students drown in too much content while lacking depth.'),
            ('Biết rất nhiều mẩu vụn không giống với hiểu được một điều đến nơi đến chốn.',
             'Knowing many fragments is not the same as understanding one thing thoroughly.'),
            ('Một thầy giáo bảo lớp: "Nếu em không còn đọc nổi mười trang liên tiếp, đó không chỉ là vấn đề của môn Văn. Đó là vấn đề của sức bền trí tuệ."',
             'A teacher told the class, "If you can no longer read ten pages in a row, that is not only a literature problem. It is a problem of intellectual endurance."'),
            ('Trong thời đại này, khả năng ngồi lâu với một vấn đề có thể trở thành lợi thế hiếm hơn cả điểm cao.',
             'In this age, the ability to stay with one problem for a long time may become rarer, and more valuable, than high scores.'),
        ],
        'lesson_vn': 'Muốn học thật, học sinh phải bơi ngược lại thói quen tiêu thụ nhanh. Sự sâu sắc luôn tốn thời gian.',
        'lesson_en': 'To learn for real, students must swim against the habit of rapid consumption. Depth always costs time.',
    },
])

ch07.extend([
    {
        'title_vn': 'Bạn Nhậu Không Phải Lúc Nào Cũng Là Bạn Đời',
        'title_en': 'A Good-Time Companion Is Not Always a Lifelong Friend',
        'pairs': [
            ('Có những người rất vui khi đi chơi cùng, nhưng biến mất ngay khi em gặp chuyện nặng.',
             'Some people are very enjoyable to spend time with, but disappear the moment real trouble arrives.'),
            ('Điều đó không làm họ thành người xấu hoàn toàn. Chỉ là em cần gọi đúng vai trò của họ.',
             'That does not make them entirely bad people. It simply means you need to name their role correctly.'),
            ('Không phải mọi người đi cùng một đoạn đều là người nên đặt ở tầng sâu nhất của lòng tin.',
             'Not everyone who walks with you for a while belongs in the deepest level of trust.'),
            ('Học sinh hay đau vì nhầm lẫn giữa người hợp vui và người hợp đời.',
             'Students are often hurt because they confuse people who fit fun with people who fit life.'),
        ],
        'lesson_vn': 'Tình bạn bền cần được phân loại tỉnh táo. Không phải ai vui vẻ với em cũng đủ sức giữ em khi có bão.',
        'lesson_en': 'Durable friendship requires sober classification. Not everyone cheerful with you is strong enough to hold you in a storm.',
    },
    {
        'title_vn': 'Người Bạn Giữ Miệng',
        'title_en': 'The Friend Who Can Keep Their Mouth Closed',
        'pairs': [
            ('Một học sinh kể bí mật cho bạn thân. Hôm sau nửa lớp biết.',
             'A student shared a secret with a close friend. The next day half the class knew.'),
            ('Nhiều bạn trẻ tưởng thân thiết là đủ. Nhưng một tình bạn không biết giữ miệng thì rất nguy hiểm.',
             'Many young people think closeness is enough. But a friendship that cannot hold confidence is dangerous.'),
            ('Người đáng tin không chỉ là người tốt bụng. Họ còn là người biết chịu trách nhiệm với thông tin được giao.',
             'A trustworthy person is not only kind. They are also someone who takes responsibility for what is entrusted to them.'),
            ('Có những mối quan hệ tan không phải vì phản bội lớn, mà vì sự bất cẩn nhỏ lặp đi lặp lại.',
             'Some relationships collapse not through great betrayals, but through repeated small carelessness.'),
        ],
        'lesson_vn': 'Muốn xây tình bạn thật, học sinh phải học cả phẩm chất kín miệng. Tin cậy là thứ được giữ bằng hành vi nhỏ.',
        'lesson_en': 'To build real friendship, students must learn the virtue of discretion. Trust is preserved through small acts.',
    },
    {
        'title_vn': 'Chơi Cùng Không Có Nghĩa Chung Giá Trị',
        'title_en': 'Spending Time Together Does Not Mean Sharing Values',
        'pairs': [
            ('Hai bạn rất hợp tính, cười nhiều, nói chuyện hợp gu. Nhưng đến lúc có việc liên quan đến đúng sai, họ lộ ra khác nhau hoàn toàn.',
             'Two friends got along easily, laughed often, and shared the same taste. But when a question of right and wrong arose, they proved completely different.'),
            ('Một người xem quay cóp là bình thường. Người kia không làm được.',
             'One considered cheating normal. The other could not accept it.'),
            ('Từ đó họ bớt thân. Không phải vì ghét nhau, mà vì tình bạn lâu dài cần nhiều hơn sự hợp vui.',
             'After that they grew less close. Not because they hated each other, but because long-term friendship requires more than easy enjoyment.'),
            ('Giá trị sống khác biệt quá lớn sẽ sớm kéo hai người về hai phía.',
             'When values differ too greatly, life soon pulls two people in different directions.'),
        ],
        'lesson_vn': 'Học sinh cần nhìn bạn không chỉ bằng cảm giác hợp, mà còn bằng nền giá trị. Cái sau mới quyết định đường dài.',
        'lesson_en': 'Students need to see friendship not only through chemistry, but through values. The latter decides the long road.',
    },
    {
        'title_vn': 'Người Bạn Không Ghen Khi Em Sáng Lên',
        'title_en': 'The Friend Who Does Not Resent Your Growth',
        'pairs': [
            ('Có tình bạn ổn chừng nào cả hai còn ngang nhau. Hễ một người tiến lên là bắt đầu có khó chịu ngầm.',
             'Some friendships are stable only while both people remain equal. The moment one grows, quiet resentment begins.'),
            ('Một người bạn tốt thật có thể chạnh lòng, nhưng cuối cùng vẫn chúc em tiến lên.',
             'A truly good friend may feel a sting, but in the end still wants your growth.'),
            ('Người chỉ thích em khi em không vượt họ thực ra không yêu quý em. Họ chỉ thích vị trí của mình so với em.',
             'A person who likes you only when you do not surpass them does not really cherish you. They only like their position relative to you.'),
            ('Tình bạn trưởng thành phải chịu nổi sự thay đổi bậc thang của nhau.',
             'Mature friendship must be able to withstand shifts in one another’s position.'),
        ],
        'lesson_vn': 'Hãy để ý ai vui thật khi em tiến bộ. Đó là dấu hiệu rất mạnh của một tình bạn lành.',
        'lesson_en': 'Notice who is genuinely glad when you improve. That is a strong sign of healthy friendship.',
    },
    {
        'title_vn': 'Ở Bên Người Đang Xuống Dốc',
        'title_en': 'Staying Beside Someone Sliding Down',
        'pairs': [
            ('Một học sinh bắt đầu nghỉ học nhiều, cáu gắt, điểm tụt. Nhiều bạn tránh dần vì thấy phiền.',
             'A student started skipping school, becoming irritable, and falling in grades. Many friends gradually avoided him because he felt burdensome.'),
            ('Chỉ còn một đứa bạn vẫn nhắn: "Tao không cứu được mày, nhưng tao không biến mất."',
             'Only one friend kept messaging: "I may not be able to save you, but I will not disappear."'),
            ('Câu đó không giải quyết ngay mọi thứ. Nhưng nó giữ cho người đang xuống dốc biết rằng mình chưa bị bỏ hẳn.',
             'That sentence did not solve everything immediately. But it helped the struggling student know he had not been fully abandoned.'),
            ('Đôi khi tình bạn thật không phải giải pháp. Nó là sợi dây để người ta chưa rơi quá sâu.',
             'Sometimes real friendship is not the solution itself. It is the rope that keeps someone from falling too deep.'),
        ],
        'lesson_vn': 'Không phải lúc nào bạn bè cũng sửa được vấn đề của nhau. Nhưng sự hiện diện tử tế đã là một giúp đỡ lớn.',
        'lesson_en': 'Friends cannot always fix each other’s problems. But decent presence is already a major help.',
    },
    {
        'title_vn': 'Tình Bạn Không Phải Hợp Đồng Chịu Đựng',
        'title_en': 'Friendship Is Not a Contract of Endless Endurance',
        'pairs': [
            ('Có mối quan hệ kéo dài chỉ vì cả hai đều quen, chứ không còn tốt cho nhau.',
             'Some relationships continue only because both people are used to them, not because they are still good for either person.'),
            ('Một người luôn đòi hỏi, một người luôn nhịn. Rồi cả hai gọi đó là thân.',
             'One always demands, the other always endures. Then both call it closeness.'),
            ('Đến lúc người luôn nhịn kiệt sức và bước ra, người kia mới bảo là phản bội.',
             'When the one who always endured finally became exhausted and left, the other called it betrayal.'),
            ('Không phải mọi kết thúc của tình bạn đều xấu. Có kết thúc là cách bảo toàn phần tử tế cuối cùng còn sót lại.',
             'Not every ending of friendship is bad. Some endings preserve the last decent part still left.'),
        ],
        'lesson_vn': 'Học sinh cần biết có những mối quan hệ nên rời đi đàng hoàng. Không phải giữ được hết mới là tốt.',
        'lesson_en': 'Students need to know that some relationships should be left with dignity. Keeping everything is not always goodness.',
    },
])

ch08.extend([
    {
        'title_vn': 'Con Nhà Thợ Rèn Không Nhất Thiết Phải Làm Thợ Rèn',
        'title_en': 'The Blacksmith’s Child Need Not Become a Blacksmith',
        'pairs': [
            ('Ngày xưa nghề nghiệp thường đi theo dòng họ. Con nhà thợ rèn thành thợ rèn, con nhà làm mộc thành thợ mộc.',
             'Long ago professions often followed bloodlines. A blacksmith’s child became a blacksmith, a carpenter’s child became a carpenter.'),
            ('Cách đó có mặt tiện: trẻ được học nghề sớm. Nhưng nó cũng khóa luôn khả năng một đứa trẻ có thể hợp việc khác hơn.',
             'That system had an advantage: children learned skills early. But it also locked away the possibility that a child might fit another calling better.'),
            ('Một cậu bé mê chữ hơn mê búa bị coi là lệch. Sau này chính cậu trở thành người ghi chép sổ sách giúp cả làng buôn bán minh bạch hơn.',
             'A boy who loved words more than hammers was considered strange. Later he became the record-keeper who helped the village trade more honestly.'),
            ('Từ xưa đến nay, xã hội vẫn thường thích đường quen. Nhưng phát triển thật lại cần chừa chỗ cho đường hợp.',
             'Across time, society prefers familiar paths. Real development, however, requires room for fitting paths.'),
        ],
        'lesson_vn': 'Định hướng nghề nghiệp không nên chỉ dựa vào truyền thống gia đình. Hợp người quan trọng không kém hợp nghề của dòng họ.',
        'lesson_en': 'Career guidance should not rest only on family tradition. Suiting the person matters as much as continuing the family trade.',
    },
    {
        'title_vn': 'Nghề Danh Giá Và Nghề Đứng Được',
        'title_en': 'Prestigious Work and Work That Can Actually Sustain Life',
        'pairs': [
            ('Có những nghề nghe sang tai hơn nghề khác. Nhưng nghề nghe sang chưa chắc là nghề em làm nổi và sống nổi.',
             'Some professions sound more prestigious than others. But a prestigious-sounding job is not necessarily one you can do well or live by.'),
            ('Một học sinh mê ngành danh tiếng nhưng không chịu được kiểu công việc hàng ngày của nó.',
             'One student loved the status of a famous profession but could not endure its daily work style.'),
            ('Ngược lại, một nghề ít hào nhoáng hơn lại vừa với tính khí và sức bền của em, nên em có thể đi rất xa.',
             'Meanwhile, a less glamorous field matched the student’s temperament and endurance, making a long path possible.'),
            ('Danh tiếng là thứ xã hội nhìn từ ngoài. Độ hợp là thứ em phải sống với nó từ trong.',
             'Prestige is what society sees from the outside. Fit is what you must live with from the inside.'),
        ],
        'lesson_vn': 'Khi chọn nghề, đừng chỉ hỏi người khác sẽ nghĩ gì. Hãy hỏi mình có sống nổi với nhịp điệu thật của nghề đó không.',
        'lesson_en': 'When choosing work, do not ask only what others will think. Ask whether you can actually live with the true rhythm of that profession.',
    },
    {
        'title_vn': 'Người Học Việc Biết Mình Không Hợp',
        'title_en': 'The Apprentice Who Realized It Did Not Fit',
        'pairs': [
            ('Một cậu học nghề theo lời khuyên của người lớn. Sau nửa năm, em nhận ra mình không ghét vất vả, nhưng ghét đúng kiểu công việc đó.',
             'A boy apprenticed in a trade because adults advised it. After half a year, he realized he did not hate hard work, but he did hate that specific kind of work.'),
            ('Ban đầu em xấu hổ vì nghĩ bỏ là kém cỏi. Sau này ông chủ cũ nói: "Biết không hợp sớm còn hơn cố thêm mấy năm rồi hỏng luôn."',
             'At first he felt ashamed, thinking quitting meant weakness. Later his former employer said, "Knowing early that it does not fit is better than forcing yourself for years and breaking down."'),
            ('Rời một hướng không phải lúc nào cũng là thất bại. Có khi đó là một quyết định tiết kiệm cả tuổi trẻ.',
             'Leaving one direction is not always failure. Sometimes it saves an entire youth.'),
            ('Xã hội hay khen kiên trì, nhưng ít nói tới chuyện phải kiên trì đúng chỗ.',
             'Society praises perseverance, but says less about the need to persevere in the right place.'),
        ],
        'lesson_vn': 'Không phải đường nào đã bắt đầu cũng phải đi tới cùng. Học sinh cần biết phân biệt giữa kiên định và cố chấp.',
        'lesson_en': 'Not every path once begun must be finished. Students need to distinguish steadfastness from stubbornness.',
    },
    {
        'title_vn': 'Một Nghề Cần Tay, Một Nghề Cần Mặt, Một Nghề Cần Tim',
        'title_en': 'One Job Needs Hands, One Needs Presence, One Needs Heart',
        'pairs': [
            ('Có nghề chủ yếu dùng sức tay. Có nghề cần giao tiếp. Có nghề đòi hỏi ngồi rất lâu với chi tiết. Có nghề cần chịu áp lực liên tục.',
             'Some jobs rely mainly on manual skill. Some require social presence. Some demand long hours with detail. Some require constant pressure tolerance.'),
            ('Một học sinh chỉ nhìn tên nghề mà không nhìn dạng lao động thật của nghề thì rất dễ chọn sai.',
             'A student who sees only the title of a job and not the true form of labor inside it is very likely to choose badly.'),
            ('Cùng là giỏi, nhưng kiểu giỏi phù hợp với nghề nào mới là điều quyết định.',
             'Ability matters, but the type of ability that matches the job is what decides the matter.'),
            ('Định hướng tốt phải cụ thể: em thích làm việc với người hay với vật? thích chuyển động hay ngồi sâu? chịu được áp lực công khai hay chỉ hợp việc lặng lẽ?',
             'Good guidance must become concrete: do you like working with people or things? movement or deep stillness? public pressure or quiet labor?'),
        ],
        'lesson_vn': 'Tên nghề là lớp vỏ. Kiểu lao động mới là ruột. Học sinh cần được hướng vào phần ruột đó.',
        'lesson_en': 'The job title is the shell. The mode of labor is the substance. Students need guidance toward that substance.',
    },
    {
        'title_vn': 'Nghề Hot Hôm Nay, Nghề Nào Còn Lại Ngày Mai?',
        'title_en': 'What Is Hot Today, and What Remains Tomorrow?',
        'pairs': [
            ('Mỗi thời có một danh sách nghề được tung hô. Nhưng thị trường thay nhanh hơn lời quảng cáo.',
             'Every era has a list of celebrated professions. But markets change faster than advertisements.'),
            ('Một học sinh chọn ngành chỉ vì nghe nó đang hot. Ba năm sau, em phát hiện cạnh tranh đã khác và mình cũng không còn hứng thú như lúc đầu.',
             'A student chose a major only because it was fashionable. Three years later, competition had changed and the student no longer felt the original excitement.'),
            ('Đi theo xu hướng mà không có nền lực riêng giống như cưỡi sóng mà không biết bơi.',
             'Following trends without building your own strength is like riding a wave without knowing how to swim.'),
            ('Xu hướng đáng tham khảo, nhưng không thể thay việc hiểu mình và luyện kỹ năng thật.',
             'Trends are worth consulting, but they cannot replace self-knowledge and the building of real skill.'),
        ],
        'lesson_vn': 'Nghề hot chỉ cho em biết thị trường đang ồn về đâu. Nó không tự động cho em biết mình nên sống đời nào.',
        'lesson_en': 'A hot profession tells you where the market is noisy. It does not automatically tell you which life you should live.',
    },
    {
        'title_vn': 'Tấm Bản Đồ Nghề Nghiệp Đầu Tiên',
        'title_en': 'The First Career Map',
        'pairs': [
            ('Một cô giáo yêu cầu học sinh làm bản đồ nghề nghiệp cá nhân: điểm mạnh, việc mình chịu được lâu, việc mình ghét, kiểu môi trường mong muốn, mức sống mong muốn.',
             'A teacher asked students to build personal career maps: strengths, work they could sustain, work they disliked, preferred environments, and desired living standards.'),
            ('Nhiều em lần đầu thấy chọn nghề không phải chỉ là chọn một cái tên trên giấy đăng ký.',
             'For many, it was the first time realizing that choosing a career is not only choosing a title on an application form.'),
            ('Nó là chọn một kiểu ngày tháng, một kiểu mệt, một kiểu niềm vui, một kiểu đánh đổi.',
             'It is choosing a pattern of days, a pattern of fatigue, a pattern of joy, and a pattern of trade-offs.'),
            ('Người chọn nghề sớm chưa chắc giỏi hơn người chọn nghề chậm. Nhưng người nghĩ nghiêm túc chắc chắn ít mù mờ hơn.',
             'Someone who chooses early is not necessarily wiser than someone who chooses slowly. But someone who thinks seriously is certainly less blind.'),
        ],
        'lesson_vn': 'Học sinh cần công cụ để nghĩ về nghề cụ thể hơn, chứ không chỉ khẩu hiệu về đam mê và thành công.',
        'lesson_en': 'Students need tools to think about work concretely, not only slogans about passion and success.',
    },
])

print("Đang tạo chương 5-8...")

make_chapter('ch05-bat-nat-hoc-duong', 5,
    'Bắt Nạt Học Đường',
    'School Bullying', ch05)

make_chapter('ch06-mang-xa-hoi-bay-so-sanh', 6,
    'Mạng Xã Hội Và Bẫy So Sánh',
    'Social Media and the Comparison Trap', ch06)

make_chapter('ch07-tinh-ban-that-va-gia', 7,
    'Tình Bạn Thật Và Giả',
    'Real and False Friendship', ch07)

make_chapter('ch08-chon-nghe-ap-luc-dinh-huong', 8,
    'Chọn Nghề Và Áp Lực Định Hướng',
    'Career Choice and Direction Pressure', ch08)

print("Hoàn tất chương 5-8!")
