#!/usr/bin/env python3
# gen_q8_c.py -- Quyển VIII ch09-12: sức khỏe tâm thần, cô đơn, ranh giới, đứng dậy
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


ch09 = [
    {
        'title_vn': 'Không Phải Cứ Cười Là Ổn',
        'title_en': 'Smiling Does Not Always Mean Fine',
        'pairs': [
            ('Có những học sinh đi học đủ, nói chuyện bình thường, thậm chí còn pha trò. Nhưng bên trong các em đang kiệt quệ.',
             'Some students attend school, talk normally, and even joke around. Inside, however, they are exhausted.'),
            ('Người lớn hay bỏ sót tín hiệu vì họ chỉ tìm dấu hiệu sụp đổ rõ ràng. Trong khi nhiều đứa trẻ rất giỏi che giấu.',
             'Adults often miss the signs because they look only for dramatic collapse. Many children are very good at hiding.'),
            ('Một học sinh có thể vẫn nộp bài đúng hạn và đồng thời mỗi tối đều nghĩ mình vô dụng.',
             'A student may still submit assignments on time while thinking every night that they are worthless.'),
            ('Sức khỏe tâm thần không phải thứ chỉ được chú ý khi có khủng hoảng. Nó cần được chăm trước khi vỡ.',
             'Mental health is not something to notice only when crisis comes. It must be cared for before it breaks.'),
        ],
        'lesson_vn': 'Dạy học sinh và người lớn bỏ thói quen đánh giá ổn hay không chỉ bằng vẻ ngoài. Nhiều vết nứt nguy hiểm nhất nằm dưới gương mặt vẫn đang cười.',
        'lesson_en': 'Teach both students and adults to stop judging wellbeing by appearance alone. Many of the most dangerous cracks sit beneath a smiling face.',
    },
    {
        'title_vn': 'Kiệt Sức Không Phải Lười',
        'title_en': 'Burnout Is Not Laziness',
        'pairs': [
            ('Một học sinh từng chăm chỉ bỗng không còn muốn mở sách. Người lớn lập tức kết luận: lười.',
             'A once-hardworking student suddenly no longer wants to open a book. Adults immediately conclude: lazy.'),
            ('Nhưng có khi em đã đi quá lâu trong áp lực mà không được nghỉ thật. Não và thân đã cạn.',
             'But sometimes the student has been running under pressure too long without real rest. Mind and body are depleted.'),
            ('Kiệt sức nhìn bên ngoài rất giống lười: chậm, nản, trì hoãn, né tránh. Nhưng gốc của nó khác. Một bên là không muốn cố. Một bên là không còn lực để cố.',
             'Burnout looks from the outside a lot like laziness: slow, discouraged, delaying, avoiding. But the root is different. One is not wanting to try. The other is not having enough strength left to try.'),
            ('Nếu nhầm hai thứ này, người lớn sẽ tiếp tục đánh vào chỗ đã nứt. Và học sinh càng tệ hơn.',
             'If these two are confused, adults keep striking the place that is already cracked. Then the student gets worse.'),
        ],
        'lesson_vn': 'Muốn giúp đúng, phải chẩn đoán đúng. Không phải đứa trẻ dừng lại nào cũng thiếu ý chí; có em chỉ đang cạn pin.',
        'lesson_en': 'To help correctly, you must diagnose correctly. Not every child who slows down lacks willpower; some are simply out of charge.',
    },
    {
        'title_vn': 'Xin Giúp Đỡ Không Làm Em Yếu Đi',
        'title_en': 'Asking for Help Does Not Make You Weak',
        'pairs': [
            ('Nhiều học sinh chịu đựng rất lâu vì sợ bị gắn mác yếu đuối, làm màu, hay có vấn đề.',
             'Many students endure for a long time because they fear being labeled weak, dramatic, or problematic.'),
            ('Các em chỉ đi tìm giúp đỡ khi mọi thứ đã quá nặng. Lúc đó việc hồi phục khó hơn nhiều.',
             'They seek help only when everything has become too heavy. By then recovery is much harder.'),
            ('Nếu đau bụng kéo dài, em đi khám. Nếu tâm trí em tối dần, em cũng cần sự giúp đỡ chuyên môn. Không có gì đáng xấu hổ ở đó.',
             'If stomach pain continues, you seek treatment. If your mind grows darker, you also need professional help. There is nothing shameful in that.'),
            ('Một nền giáo dục tốt phải cho học sinh biết rằng cầu cứu đúng lúc là hành vi trưởng thành, không phải thất bại.',
             'A good educational culture must teach students that asking for help at the right time is maturity, not failure.'),
        ],
        'lesson_vn': 'Hãy bình thường hóa việc tìm hỗ trợ tâm lý. Cái tôi im lặng nhiều khi nguy hiểm hơn chính vấn đề ban đầu.',
        'lesson_en': 'Normalize seeking mental-health support. A silent ego is often more dangerous than the initial problem itself.',
    },
    {
        'title_vn': 'Nghỉ Ngơi Không Phải Tội Lỗi',
        'title_en': 'Rest Is Not a Sin',
        'pairs': [
            ('Có những học sinh cứ nghỉ là thấy cắn rứt. Không học một tối cũng thấy mình tụt lại.',
             'Some students feel guilty whenever they rest. Missing one evening of study already feels like falling behind.'),
            ('Đó không còn là chăm chỉ nữa. Đó là mối quan hệ bệnh lý với năng suất.',
             'That is no longer diligence. It is an unhealthy relationship with productivity.'),
            ('Não người không vận hành như máy. Nó cần khoảng dừng để hợp nhất kiến thức, để hồi phục cảm xúc, để không cháy rụi.',
             'The human mind does not operate like a machine. It needs pauses to consolidate knowledge, recover emotionally, and avoid burning out.'),
            ('Học sinh cần được dạy rằng nghỉ đúng cách không cản trở thành công. Nó là điều kiện để thành công không giết mình.',
             'Students need to be taught that proper rest does not obstruct success. It is what keeps success from destroying you.'),
        ],
        'lesson_vn': 'Nghỉ ngơi có kỷ luật là một phần của học tập có kỷ luật. Đừng dạy trẻ em tự hào vì kiệt sức.',
        'lesson_en': 'Disciplined rest is part of disciplined study. Do not teach children to feel proud of exhaustion.',
    },
]

ch10 = [
    {
        'title_vn': 'Có Thể Em Đang Một Mình Dù Quanh Em Rất Đông',
        'title_en': 'You May Be Alone Even When Surrounded by People',
        'pairs': [
            ('Một học sinh đi học, đi thêm, đi sinh hoạt câu lạc bộ, nhắn tin liên tục, nhưng vẫn thấy trống rỗng.',
             'A student attends school, extra classes, clubs, and messages people constantly, yet still feels empty.'),
            ('Cô đơn không chỉ là không có ai bên cạnh. Cô đơn còn là không có ai thực sự chạm được vào phần thật của mình.',
             'Loneliness is not only having no one around. It is also having no one who reaches the real part of you.'),
            ('Nhiều học sinh học cách biểu diễn phiên bản dễ chấp nhận của mình để khỏi bị loại ra. Cái giá là dần dần không ai biết mình thật nữa.',
             'Many students learn to perform an acceptable version of themselves to avoid exclusion. The price is that gradually nobody knows who they really are.'),
            ('Một đám đông có thể che cô đơn rất tốt. Nhưng nó không chữa cô đơn.',
             'A crowd can hide loneliness very well. But it cannot cure it.'),
        ],
        'lesson_vn': 'Giải pháp cho cô đơn không luôn là thêm người. Nhiều khi là thêm sự thật trong những kết nối đang có.',
        'lesson_en': 'The solution to loneliness is not always more people. Often it is more truth inside the connections that already exist.',
    },
    {
        'title_vn': 'Cô Đơn Có Lúc Là Tín Hiệu Tốt',
        'title_en': 'Sometimes Loneliness Is a Useful Signal',
        'pairs': [
            ('Không phải mọi cô đơn đều xấu. Có lúc nó là tín hiệu rằng môi trường quanh em không còn phù hợp.',
             'Not all loneliness is bad. Sometimes it is a signal that the environment around you no longer fits.'),
            ('Một học sinh rời khỏi nhóm bạn độc hại sẽ rất cô đơn một thời gian. Nhưng đó là nỗi cô đơn sạch.',
             'A student who leaves a toxic friend group will feel lonely for a while. But that is a clean loneliness.'),
            ('Một người dám ngừng giả vờ trước tập thể cũng sẽ cô đơn hơn lúc đầu. Nhưng đó là khoảng trống cần thiết để một bản thân thật xuất hiện.',
             'A person who stops pretending before the group will also feel lonelier at first. But that is the necessary space for a real self to emerge.'),
            ('Điều nguy hiểm không phải là có những giai đoạn cô đơn. Điều nguy hiểm là chấp nhận mọi sự sai lệch chỉ để không phải ở một mình.',
             'The danger is not going through lonely phases. The danger is accepting every distortion just to avoid being alone.'),
        ],
        'lesson_vn': 'Học sinh cần biết phân biệt cô đơn độc hại với cô đơn trưởng thành. Có những quãng một mình là cái giá để sống thật.',
        'lesson_en': 'Students need to distinguish toxic loneliness from maturing loneliness. Some seasons of aloneness are the price of living truthfully.',
    },
    {
        'title_vn': 'Biết Ở Một Mình Là Một Năng Lực',
        'title_en': 'Knowing How to Be Alone Is a Skill',
        'pairs': [
            ('Nhiều bạn không chịu nổi một bữa trưa ngồi một mình hay một buổi chiều không ai nhắn tin.',
             'Many students cannot bear eating lunch alone or spending an afternoon without messages.'),
            ('Sự khó chịu đó cho thấy các em chưa quen ở với chính mình.',
             'That discomfort shows they are not used to being with themselves.'),
            ('Người không ở một mình được rất dễ phụ thuộc vào đám đông để xác nhận giá trị. Từ đó họ dễ bị dẫn dắt, dễ chiều theo, dễ đánh mất hướng.',
             'A person who cannot be alone is easily dependent on the crowd for validation. From there, they are easily led, easily bent, easily lost.'),
            ('Ở một mình không phải tự cô lập. Nó là khả năng yên được với bản thân mà không phải mở tiếng ồn lên để chạy trốn.',
             'Being alone is not self-isolation. It is the ability to stay at peace with yourself without turning on noise to escape.'),
        ],
        'lesson_vn': 'Một phần trưởng thành là tập cho học sinh chịu được sự im lặng, suy nghĩ riêng, và những khoảng không không được lấp ngay bằng người khác.',
        'lesson_en': 'Part of maturity is training students to tolerate silence, private thought, and empty spaces that are not instantly filled by others.',
    },
    {
        'title_vn': 'Có Một Người Hiểu Em Đã Là Rất Nhiều',
        'title_en': 'Having One Person Who Understands You Is Already a Lot',
        'pairs': [
            ('Nhiều học sinh đau vì nghĩ mình phải có rất nhiều bạn thân, phải được nhiều người quý thì mới không cô đơn.',
             'Many students suffer because they think they need many close friends and broad approval in order not to feel alone.'),
            ('Nhưng đôi khi một người hiểu mình thật sự đã là một tài sản lớn.',
             'But sometimes one person who truly understands you is already a great treasure.'),
            ('Một cô giáo chủ nhiệm, một người anh, một đứa bạn ít nói nhưng đáng tin, hay chính mẹ mình nếu mẹ biết nghe. Chỉ một kết nối sâu cũng có thể giữ một học sinh khỏi trượt quá xa.',
             'A homeroom teacher, an older brother, a quiet but trustworthy friend, or one’s own mother if she knows how to listen. A single deep bond can keep a student from sliding too far.'),
            ('Vấn đề không phải mạng lưới rộng đến đâu. Vấn đề là có nơi nào em không phải diễn không.',
             'The issue is not how wide the network is. The issue is whether there exists any place where you do not have to perform.'),
        ],
        'lesson_vn': 'Đừng dạy học sinh chạy theo độ nổi tiếng của quan hệ. Hãy giúp các em xây ít nhưng thật.',
        'lesson_en': 'Do not teach students to chase the popularity of relationships. Help them build fewer but truer ones.',
    },
]

ch11 = [
    {
        'title_vn': 'Biết Nói Không Là Một Dấu Hiệu Trưởng Thành',
        'title_en': 'Knowing How to Say No Is a Sign of Maturity',
        'pairs': [
            ('Nhiều học sinh nghĩ từ chối là hỗn, là ích kỷ, là làm mất lòng.',
             'Many students think refusal is rude, selfish, or hurtful.'),
            ('Vì vậy các em gật đầu với việc chép bài hộ, đi chơi khi không muốn, tham gia trò ngu khi thấy sai, và nhận thêm gánh khi đã quá sức.',
             'So they say yes to doing others’ homework, going out when they do not want to, joining stupid acts they know are wrong, and taking on burdens when already overloaded.'),
            ('Một chữ không nói ra đúng lúc thường dẫn tới hàng chục hậu quả phải trả sau đó.',
             'One no withheld at the right time often leads to dozens of consequences paid later.'),
            ('Từ chối không làm em thành người xấu. Từ chối đúng lúc giúp em giữ thời gian, nhân cách, và sự an toàn của mình.',
             'Refusing does not make you a bad person. Refusing at the right time protects your time, your character, and your safety.'),
        ],
        'lesson_vn': 'Giáo dục tốt không chỉ dạy học sinh vâng lời. Nó còn phải dạy các em từ chối điều sai và điều quá sức.',
        'lesson_en': 'Good education does not only teach students to obey. It must also teach them to refuse what is wrong and what is too much.',
    },
    {
        'title_vn': 'Ai Cũng Muốn Em Dễ Sai Khi Em Không Có Ranh Giới',
        'title_en': 'Everyone Can Push You Around If You Have No Boundaries',
        'pairs': [
            ('Một học sinh không có ranh giới rõ thường trở thành người bị nhờ nhiều nhất, lợi dụng nhiều nhất, và mệt mỏi nhiều nhất.',
             'A student without clear boundaries often becomes the one most asked, most used, and most exhausted.'),
            ('Không phải vì em xấu số. Mà vì những người khác sớm nhận ra em khó từ chối.',
             'This is not bad luck. It is because others quickly notice that you are hard to refuse.'),
            ('Ranh giới không cần hung hăng. Nó chỉ cần rõ ràng: em không cho phép gì, em sẵn sàng gì, và em dừng ở đâu.',
             'Boundaries do not need aggression. They only need clarity: what you do not allow, what you are willing to give, and where you stop.'),
            ('Người quen lợi dụng em sẽ khó chịu khi em bắt đầu có ranh giới. Điều đó không chứng minh em sai. Nó chỉ chứng minh trước đây họ được lợi từ việc em quá mềm.',
             'People who benefit from using you will dislike your boundaries. That does not prove you are wrong. It only proves they previously benefited from your softness.'),
        ],
        'lesson_vn': 'Ranh giới là kỹ năng tự bảo vệ, không phải thái độ thù địch. Học sinh càng tử tế càng cần được học điều này.',
        'lesson_en': 'Boundaries are a self-protection skill, not hostility. The kinder the student, the more necessary this lesson becomes.',
    },
    {
        'title_vn': 'Từ Chối Bạn Xấu Khó Hơn Từ Chối Người Lạ',
        'title_en': 'It Is Harder to Refuse Bad Friends Than Strangers',
        'pairs': [
            ('Nhiều học sinh không sa vào rắc rối vì người lạ ép. Các em sa vào vì bạn thân rủ.',
             'Many students do not get into trouble because strangers pressure them. They get into trouble because close friends invite them.'),
            ('Một điếu thuốc đầu tiên, một lần quay cóp, một trò làm nhục người khác, một cú trốn học. Những bước lệch lớn rất hay bắt đầu bằng câu: "Có gì đâu, đi một lần thôi."',
             'A first cigarette, one act of cheating, humiliating someone else, skipping school. Major deviations often begin with the line: "It is nothing, just once."'),
            ('Từ chối người mình quý rất khó vì em sợ mất nhóm, sợ bị chê là nhát, sợ trở thành kẻ khác biệt.',
             'Refusing people you like is hard because you fear losing the group, being mocked as weak, or becoming the odd one out.'),
            ('Nhưng nhiều cuộc đời hỏng không phải vì một quyết định lớn. Nó hỏng vì quá nhiều lần không dám nói không với cái sai nhỏ.',
             'But many lives are not ruined by one huge decision. They are ruined by too many small moments of failing to say no to what is wrong.'),
        ],
        'lesson_vn': 'Hãy tập cho học sinh những câu từ chối cụ thể. Bản lĩnh không tự xuất hiện trong khoảnh khắc áp lực nếu trước đó chưa từng luyện.',
        'lesson_en': 'Train students with concrete refusal sentences. Strength does not appear magically under pressure if it has never been practiced before.',
    },
    {
        'title_vn': 'Nói Không Với Chính Mình Còn Khó Hơn',
        'title_en': 'Saying No to Yourself Is Even Harder',
        'pairs': [
            ('Không phải mọi cám dỗ đều đến từ người khác. Rất nhiều lần, chính mình dụ mình.',
             'Not every temptation comes from other people. Very often, we tempt ourselves.'),
            ('Thêm mười phút điện thoại, thêm một lần trì hoãn, thêm một lời cay nghiệt cho đã miệng, thêm một lý do để không làm điều nên làm.',
             'Ten more minutes on the phone, one more delay, one more cruel remark for satisfaction, one more excuse not to do what should be done.'),
            ('Tự chủ bắt đầu từ những khoảnh khắc rất nhỏ đó. Người nói không được với chính mình thì sớm muộn cũng khó đứng vững trước sức ép bên ngoài.',
             'Self-control begins in those tiny moments. A person who cannot refuse themselves will eventually struggle to stand against outside pressure too.'),
            ('Trưởng thành không chỉ là tự do làm điều mình muốn. Trưởng thành là đủ nội lực để không làm những điều mình sẽ hối hận.',
             'Maturity is not only the freedom to do what you want. It is the inner strength not to do what you will regret.'),
        ],
        'lesson_vn': 'Ranh giới quan trọng nhất không phải ranh giới với người khác, mà là ranh giới với phần yếu đuối và bốc đồng trong chính mình.',
        'lesson_en': 'The most important boundary is not with others, but with the impulsive and weaker part inside yourself.',
    },
]

ch12 = [
    {
        'title_vn': 'Ngã Không Đáng Xấu Hổ, Nằm Luôn Mới Đáng Lo',
        'title_en': 'Falling Is Not Shameful, Staying Down Is the Real Danger',
        'pairs': [
            ('Một học sinh thi trượt, bị chê cười, rồi tự kết luận đời mình kém cỏi.',
             'A student fails an exam, gets mocked, and concludes that life itself is inferior.'),
            ('Nhưng cuộc đời không đo con người bằng số lần ngã. Nó đo bằng chuyện sau đó em làm gì.',
             'But life does not measure a person by the number of falls. It measures what happens next.'),
            ('Có người vấp rồi học được cách đi chắc hơn. Có người chỉ mải xấu hổ nên không đứng dậy nữa.',
             'Some people stumble and learn to walk more firmly. Others stay busy feeling ashamed and never rise again.'),
            ('Vấp ngã là chuyện thường. Bỏ mặc bản thân sau cú ngã mới là điều đáng sợ.',
             'Falling is ordinary. Abandoning yourself after the fall is what is frightening.'),
        ],
        'lesson_vn': 'Điều cần dạy học sinh không phải là làm sao không bao giờ ngã. Điều cần dạy là cách tự kéo mình dậy sau khi ngã.',
        'lesson_en': 'What students need is not a way never to fall. They need a way to lift themselves after falling.',
    },
    {
        'title_vn': 'Bắt Đầu Lại Luôn Nhỏ Và Xấu',
        'title_en': 'Starting Again Is Always Small and Ugly',
        'pairs': [
            ('Nhiều em tưởng đứng dậy phải thật hoành tráng: lập kế hoạch lớn, thay đổi triệt để, hứa với bản thân từ nay khác hẳn.',
             'Many students imagine recovery must be dramatic: a huge plan, total transformation, promises of becoming completely different from now on.'),
            ('Sự thật là bắt đầu lại thường rất nhỏ và khá xấu. Một buổi ngồi vào bàn học lại. Một bài tập làm cho xong. Một cuộc nói chuyện trung thực. Một giấc ngủ đúng giờ.',
             'The truth is that starting again is usually very small and rather ugly. One evening sitting at the desk again. One assignment completed. One honest conversation. One proper night of sleep.'),
            ('Những thứ nhỏ ấy không gây xúc động mạnh, nhưng chúng mới thật sự dựng lại cuộc đời.',
             'Those small things do not create dramatic emotion, but they are what actually rebuild a life.'),
            ('Người thích chờ động lực lớn thường chờ rất lâu. Người chấp nhận bước nhỏ thì đi được.',
             'People who wait for grand motivation often wait a very long time. Those who accept small steps actually move.'),
        ],
        'lesson_vn': 'Dạy học sinh yêu bước nhỏ. Hồi phục bền gần như luôn bắt đầu bằng thứ rất bình thường.',
        'lesson_en': 'Teach students to respect small steps. Durable recovery almost always begins with something ordinary.',
    },
    {
        'title_vn': 'Đời Không Công Bằng, Nhưng Em Vẫn Có Thể Chơi Đẹp',
        'title_en': 'Life Is Not Fair, But You Can Still Play Clean',
        'pairs': [
            ('Có người sinh ra đã có điều kiện hơn, nền tốt hơn, đỡ áp lực hơn. Điều đó là thật.',
             'Some people are born with better conditions, stronger support, and less pressure. That is real.'),
            ('Học sinh cần được nói sự thật này, thay vì nghe những lời màu hồng rằng ai cố cũng như ai.',
             'Students need to hear this truth rather than soft slogans claiming that everyone’s effort starts equally.'),
            ('Nhưng từ bất công đó không suy ra rằng em được quyền buông xuôi, làm bậy, hay dối trá.',
             'But that unfairness does not imply that you have the right to give up, act wrongly, or become dishonest.'),
            ('Đời không công bằng là lý do để em tỉnh táo hơn, không phải bẩn hơn.',
             'Life being unfair is a reason to become clearer, not dirtier.'),
        ],
        'lesson_vn': 'Giáo dục trung thực phải nhìn nhận chênh lệch thật của đời sống, nhưng vẫn giữ cho học sinh một nguyên tắc cứng: khó không cho phép mình trở nên xấu.',
        'lesson_en': 'Honest education must acknowledge real inequality in life, while preserving one hard principle: difficulty does not permit becoming corrupt.',
    },
    {
        'title_vn': 'Cuối Cùng, Điều Giữ Em Đi Tiếp Không Phải Là Lời Khen',
        'title_en': 'In the End, Praise Is Not What Keeps You Going',
        'pairs': [
            ('Có thời gian học sinh sống bằng lời khen. Được công nhận là có năng lượng. Bị chê là rơi xuống ngay.',
             'For a time, students may live on praise. Recognition gives energy; criticism drops them instantly.'),
            ('Nhưng càng lớn, em càng phải đi bằng thứ bền hơn: giá trị bên trong, thói quen lao động, và khả năng tự nhắc mình lý do phải tiếp tục.',
             'But as you grow, you must move by something more durable: inner values, habits of work, and the ability to remind yourself why to continue.'),
            ('Không ai được vỗ tay cho em mọi ngày. Có những giai đoạn rất dài em phải bước trong im lặng.',
             'No one will applaud you every day. There are long phases when you must walk in silence.'),
            ('Người đi đường dài là người không chết đói vì thiếu lời khen.',
             'The person who lasts is the one who does not starve in the absence of praise.'),
        ],
        'lesson_vn': 'Hãy giúp học sinh xây nội lực thay vì chỉ bơm cảm xúc. Người trưởng thành phải đi được cả khi không ai cổ vũ.',
        'lesson_en': 'Help students build inner strength rather than only emotional boosts. A mature person must be able to continue even when no one cheers.',
    },
]

ch09.extend([
    {
        'title_vn': 'Người Học Trò Vẫn Đi Học Đều Nhưng Đã Rỗng Dần',
        'title_en': 'The Student Who Still Attended but Was Slowly Emptying Out',
        'pairs': [
            ('Có học sinh vẫn đến lớp đầy đủ, làm bài đủ, cười khi cần, nhưng bên trong đã rỗng đi từng ngày.',
             'Some students still attend class, finish assignments, and smile when needed, while inside they are emptying out day by day.'),
            ('Người lớn dễ bị đánh lừa bởi sự đúng giờ và bề ngoài gọn gàng.',
             'Adults are easily misled by punctuality and neat appearance.'),
            ('Nhưng một tâm trí kiệt quệ vẫn có thể vận hành thêm một thời gian bằng quán tính.',
             'Yet an exhausted mind can keep functioning for a while through inertia.'),
            ('Nếu chỉ chờ đến lúc một học sinh gục hẳn mới gọi đó là vấn đề, ta đã chậm rất lâu rồi.',
             'If we wait until a student completely collapses before calling it a problem, we are already very late.'),
        ],
        'lesson_vn': 'Sức khỏe tâm thần cần được quan sát ở giai đoạn nứt, không phải đợi đến giai đoạn vỡ.',
        'lesson_en': 'Mental health must be noticed at the cracking stage, not only at the breaking stage.',
    },
    {
        'title_vn': 'Ông Đồ Già Và Cơn U Uất Mùa Thi',
        'title_en': 'The Old Tutor and the Exam-Season Melancholy',
        'pairs': [
            ('Ngày xưa mỗi mùa khoa cử đến, không ít sĩ tử mất ăn mất ngủ, dễ cáu bẳn, chán nản, và sợ hãi quá mức.',
             'In the old examination seasons, many candidates lost sleep and appetite, became irritable, despondent, and excessively fearful.'),
            ('Người đời khi đó chưa gọi tên là kiệt quệ tâm lý. Nhưng triệu chứng thì vẫn là những gì học sinh hôm nay đang trải qua.',
             'People then did not name it psychological burnout. Yet the symptoms were much like what students experience today.'),
            ('Một ông đồ già thường bắt học trò nghỉ hẳn một buổi chiều trước kỳ thi để đi bộ quanh đồng và nói chuyện trời đất.',
             'An old tutor would make his students take one full afternoon off before the exam to walk through the fields and talk about ordinary things.'),
            ('Ông bảo: "Đầu óc căng quá thì chữ nghĩa dính vào nhau thành bùn. Phải để nó có chỗ thở."',
             'He said, "When the mind is too tight, words stick together like mud. It must be given space to breathe."'),
        ],
        'lesson_vn': 'Vấn đề tâm lý trong học tập không phải chuyện mới của thời hiện đại. Nó chỉ có tên gọi mới hơn mà thôi.',
        'lesson_en': 'Psychological struggle in study is not a new modern problem. It simply has newer names now.',
    },
    {
        'title_vn': 'Cái Mệt Không Nói Thành Lời',
        'title_en': 'The Fatigue Without Words',
        'pairs': [
            ('Nhiều học sinh không biết mô tả mình đang bị gì. Các em chỉ nói: "Em mệt."',
             'Many students do not know how to describe what is happening inside them. They simply say, "I am tired."'),
            ('Mệt có thể là thiếu ngủ. Cũng có thể là lo âu, là quá tải, là mất hứng sống, là áp lực kéo dài.',
             'Tired may mean lack of sleep. It may also mean anxiety, overload, loss of joy, or prolonged pressure.'),
            ('Khi từ vựng cảm xúc quá nghèo, học sinh rất khó cầu cứu đúng thứ mình cần.',
             'When emotional vocabulary is too poor, students struggle to ask for the help they actually need.'),
            ('Dạy một đứa trẻ gọi tên được trạng thái của mình là đang cho nó thêm một công cụ sống sót.',
             'Teaching a child to name their inner state gives them one more survival tool.'),
        ],
        'lesson_vn': 'Giáo dục cảm xúc không phải thứ phụ. Nó giúp học sinh phân biệt mệt, buồn, kiệt sức, hoảng loạn, và biết khi nào cần nói ra.',
        'lesson_en': 'Emotional education is not an extra. It helps students distinguish tiredness, sadness, burnout, panic, and know when to speak.',
    },
    {
        'title_vn': 'Người Đứng Đầu Lớp Cũng Có Thể Muốn Biến Mất',
        'title_en': 'The Top Student Can Also Want to Disappear',
        'pairs': [
            ('Thành tích tốt không miễn trừ ai khỏi đau tinh thần.',
             'Good performance does not immunize anyone against mental pain.'),
            ('Một học sinh đứng đầu lớp vẫn có thể về nhà và cảm thấy trống rỗng, vô nghĩa, hoặc muốn biến mất khỏi mọi kỳ vọng.',
             'A top student can still go home and feel empty, meaningless, or wish to disappear from every expectation.'),
            ('Chính vì người đó học tốt nên xung quanh càng dễ chủ quan: nó vẫn ổn mà.',
             'Precisely because the student performs well, people around are more likely to be careless: he seems fine.'),
            ('Đó là một sai lầm đắt. Năng lực không phải áo giáp trước tổn thương tâm lý.',
             'That is a costly mistake. Competence is not armor against psychological harm.'),
        ],
        'lesson_vn': 'Đừng đánh giá sức khỏe tâm thần bằng kết quả học tập. Một bảng điểm đẹp có thể che rất nhiều nứt gãy.',
        'lesson_en': 'Do not judge mental health by academic results. A beautiful report card can hide many fractures.',
    },
    {
        'title_vn': 'Khi Cơ Thể Kêu Thay Tâm Trí',
        'title_en': 'When the Body Speaks for the Mind',
        'pairs': [
            ('Có học sinh đau bụng trước giờ kiểm tra, tim đập mạnh, run tay, toát mồ hôi, nhưng không hề nghĩ đó là chuyện tâm lý.',
             'Some students get stomach pain before tests, racing hearts, shaking hands, and sweating, yet do not realize it may be psychological.'),
            ('Các em tưởng mình yếu người. Thực ra có khi cơ thể đang nói thay cho một đầu óc quá căng.',
             'They think their body is weak. In fact, the body may be speaking on behalf of an overloaded mind.'),
            ('Nếu chỉ chữa phần ngọn mà không nhìn phần gốc, nỗi khổ sẽ đổi hình chứ không biến mất.',
             'If only the surface is treated while the root is ignored, the suffering changes shape but does not disappear.'),
            ('Học sinh cần biết tâm trí và cơ thể không tách nhau sạch như trong sách vở.',
             'Students need to know that mind and body are not separated as neatly as textbooks suggest.'),
        ],
        'lesson_vn': 'Một số tín hiệu cơ thể là lời nhắc rằng tâm trí đang quá tải. Biết đọc những dấu hiệu đó là kỹ năng tự bảo vệ.',
        'lesson_en': 'Some bodily symptoms are reminders that the mind is overloaded. Learning to read them is a self-protection skill.',
    },
    {
        'title_vn': 'Người Lớn Lắng Nghe Một Lần Đúng Cách',
        'title_en': 'One Adult Who Listens Properly',
        'pairs': [
            ('Có học sinh đã nhiều lần định nói mình không ổn, nhưng mỗi lần mở lời đều bị chặn bằng câu: "Nghĩ ít thôi là hết."',
             'A student tried many times to say they were not okay, but every attempt was cut off with, "Just think less and it will pass."'),
            ('Đến khi gặp một cô giáo chỉ hỏi: "Em muốn cô ngồi nghe hay muốn cô tìm người giúp?" em mới bật khóc.',
             'Only when a teacher asked, "Do you want me to listen, or do you want me to help find support?" did the student finally break down in tears.'),
            ('Được lắng nghe tử tế không phải phép màu. Nhưng nó thường là cánh cửa đầu tiên để một người chịu bước ra khỏi bóng tối.',
             'Being listened to properly is not magic. But it is often the first door through which someone steps out of darkness.'),
            ('Không phải người lớn nào cũng cần giải quyết ngay. Nhiều khi việc đầu tiên là đừng làm học sinh thấy mình bị coi nhẹ.',
             'Not every adult needs to solve things immediately. Often the first task is simply not to make the student feel minimized.'),
        ],
        'lesson_vn': 'Trong hỗ trợ tâm lý, cách nghe quan trọng không kém cách nói. Một câu đúng lúc có thể giữ người ở lại với đời.',
        'lesson_en': 'In mental-health support, the way you listen matters as much as the way you speak. One timely sentence can help keep someone in life.',
    },
])

ch10.extend([
    {
        'title_vn': 'Ngồi Giữa Hội Làng Mà Vẫn Lạc',
        'title_en': 'Lost Even in the Village Festival',
        'pairs': [
            ('Ngày xưa giữa hội làng đông người vẫn có những đứa trẻ đứng bên lề, thấy mình không thuộc về đâu.',
             'Long ago, even amid crowded village festivals, some children stood at the edge feeling that they belonged nowhere.'),
            ('Cô đơn không phải phát minh của mạng xã hội. Nó chỉ đổi cảnh nền theo thời đại.',
             'Loneliness was not invented by social media. It merely changes backdrop across eras.'),
            ('Một đứa trẻ có thể ở giữa tiếng trống, tiếng cười, và vẫn thấy mình như đang ở ngoài cửa.',
             'A child can stand amid drums and laughter, yet feel as if standing outside the door.'),
            ('Cảm giác bị lệch khỏi đám đông là rất cổ. Điều mới là ngày nay người ta giấu nó bằng kết nối liên tục.',
             'The feeling of being out of step with the crowd is ancient. What is new is how we now hide it with constant connection.'),
        ],
        'lesson_vn': 'Cô đơn là vấn đề của con người, không phải chỉ của thời đại số. Vì thế cách đối diện nó cũng cần sâu hơn mẹo dùng mạng.',
        'lesson_en': 'Loneliness is a human problem, not merely a digital-age problem. That is why facing it requires more than social-media advice.',
    },
    {
        'title_vn': 'Người Có Nhiều Nhóm Chat Nhất Lại Không Có Ai Để Gọi',
        'title_en': 'The Person With Many Group Chats but No One to Call',
        'pairs': [
            ('Có học sinh điện thoại luôn sáng vì tin nhắn nhóm, nhưng đến lúc buồn thật lại không biết gọi cho ai.',
             'Some students have phones constantly lit by group messages, yet when real sadness comes, they do not know whom to call.'),
            ('Đó là kiểu cô đơn mới nhưng rất quen: rất nhiều tiếp xúc, rất ít chỗ nương.',
             'This is a newer-looking loneliness but a very familiar one: much contact, very little shelter.'),
            ('Sự hiện diện kỹ thuật số đông đúc không tự động tạo nên thân mật.',
             'Crowded digital presence does not automatically create intimacy.'),
            ('Một danh bạ dài không có nghĩa em đang được giữ bởi những mối quan hệ sâu.',
             'A long contact list does not mean you are held by deep relationships.'),
        ],
        'lesson_vn': 'Học sinh cần phân biệt giữa liên lạc và gắn bó. Một cái cho cảm giác bớt vắng, cái còn lại mới thực sự chống cô đơn.',
        'lesson_en': 'Students need to distinguish contact from connection. One reduces the feeling of emptiness; the other truly counters loneliness.',
    },
    {
        'title_vn': 'Cô Đơn Vì Không Dám Nói Sự Thật',
        'title_en': 'Lonely Because You Dare Not Tell the Truth',
        'pairs': [
            ('Có những học sinh quanh mình không thiếu người, nhưng không ai biết em đang sợ gì, thích gì, ghét gì, hay thật sự mệt thế nào.',
             'Some students are surrounded by people, yet no one knows what they fear, like, hate, or how tired they really are.'),
            ('Càng diễn phiên bản an toàn của mình lâu, các em càng khó được chạm tới thật.',
             'The longer they perform a safer version of themselves, the harder it becomes for anyone to reach them truly.'),
            ('Nhiều cô đơn không đến từ việc thiếu người. Nó đến từ việc thiếu sự thật.',
             'Many forms of loneliness do not come from a lack of people. They come from a lack of truth.'),
            ('Muốn bớt cô đơn, có lúc em phải mạo hiểm nói thật hơn một chút với người đáng tin.',
             'To become less lonely, sometimes you must risk being a little more truthful with someone trustworthy.'),
        ],
        'lesson_vn': 'Sự thật có thể khiến em dễ bị tổn thương hơn lúc đầu, nhưng cũng chính nó mở cửa cho kết nối thật.',
        'lesson_en': 'Truth may make you more vulnerable at first, but it is also what opens the door to genuine connection.',
    },
    {
        'title_vn': 'Buổi Trưa Một Mình',
        'title_en': 'Eating Lunch Alone',
        'pairs': [
            ('Ở trường, có những nỗi cô đơn rất cụ thể: không biết ngồi với ai lúc ăn trưa, không biết chen vào nhóm nào giữa giờ ra chơi.',
             'In school, some forms of loneliness are very concrete: not knowing whom to sit with at lunch, not knowing which group to join at recess.'),
            ('Những khoảnh khắc nhỏ đó lặp lại đủ nhiều sẽ làm học sinh thấy mình như người thừa.',
             'Repeated often enough, those small moments make students feel like excess persons.'),
            ('Một cô giáo chỉ cần chú ý chuyện tưởng nhỏ này đã cứu được một bạn khỏi nhiều tuần thu mình.',
             'A teacher who noticed this seemingly small matter was able to save one student from weeks of withdrawal.'),
            ('Cô đơn học đường đôi khi bắt đầu từ những chi tiết rất bình thường mà người lớn hay bỏ qua.',
             'School loneliness sometimes begins with very ordinary details adults often overlook.'),
        ],
        'lesson_vn': 'Nếu muốn xây môi trường học đường lành, phải để ý cả những khoảnh khắc nhỏ nơi học sinh bị tách ra khỏi đám đông.',
        'lesson_en': 'If we want a healthy school environment, we must notice the small moments in which students are separated from the crowd.',
    },
    {
        'title_vn': 'Học Cách Ngồi Với Mình',
        'title_en': 'Learning to Sit With Yourself',
        'pairs': [
            ('Một học sinh từng rất sợ ở một mình. Hễ không có người bên cạnh là em phải bật nhạc, mở video, hay nhắn cho ai đó.',
             'A student was once afraid of being alone. Whenever no one was around, she had to turn on music, videos, or message someone.'),
            ('Cô tư vấn giao cho em bài tập lạ: mỗi ngày ngồi yên mười phút không màn hình và chỉ ghi lại xem đầu mình đang nghĩ gì.',
             'The counselor gave her an unusual exercise: sit quietly ten minutes a day without screens and write down what the mind is thinking.'),
            ('Ban đầu em rất khó chịu. Nhưng dần dần, em bớt sợ khoảng trống trong chính mình.',
             'At first she found it unbearable. Gradually, though, she became less afraid of the empty space inside herself.'),
            ('Ai không chịu được chính mình thì rất dễ bám lấy người khác quá mức.',
             'Whoever cannot bear their own company is easily driven to cling to others too much.'),
        ],
        'lesson_vn': 'Khả năng ở một mình không chống lại tình thân. Nó giúp em bước vào tình thân mà không tuyệt vọng bấu víu.',
        'lesson_en': 'The ability to be alone does not oppose intimacy. It helps you enter intimacy without desperate clinging.',
    },
    {
        'title_vn': 'Một Lá Thư Không Gửi',
        'title_en': 'An Unsent Letter',
        'pairs': [
            ('Một học sinh viết thư cho chính mình về cảm giác bị lạc lõng trong lớp, nhưng không gửi cho ai cả.',
             'A student wrote a letter to herself about feeling out of place in class, but sent it to no one.'),
            ('Viết xong, em nhận ra điều mình cần nhất lúc đó không phải lời khuyên, mà là cảm giác mình đã thành thật với nỗi buồn của mình.',
             'When she finished, she realized that what she needed most in that moment was not advice, but the sense that she had been honest about her sadness.'),
            ('Không phải mọi cô đơn đều hết bằng cách thêm người. Có cô đơn cần được gọi tên trước.',
             'Not every loneliness is healed by adding more people. Some loneliness first needs to be named.'),
            ('Từ chỗ gọi đúng tên, em mới biết mình cần người, cần nghỉ, hay cần đổi môi trường.',
             'Once named correctly, she could see whether she needed people, rest, or a change of environment.'),
        ],
        'lesson_vn': 'Đôi khi bước đầu chống cô đơn là trung thực với chính mình. Không nhận ra nỗi trống thì rất khó chữa nó.',
        'lesson_en': 'Sometimes the first step against loneliness is honesty with oneself. If the emptiness is not recognized, it is hard to heal.',
    },
])

ch11.extend([
    {
        'title_vn': 'Một Chữ “Không” Cứu Cả Đời',
        'title_en': 'One No Can Save a Life',
        'pairs': [
            ('Có những tai họa lớn bắt đầu từ việc một học sinh không dám nói không với chuyện rất nhỏ.',
             'Some major disasters begin with a student’s inability to say no to something seemingly small.'),
            ('Một lần chép bài hộ, một lần đi theo nhóm làm chuyện dại, một lần lên xe với người lái ẩu. Rất nhiều tai nạn bắt đầu kiểu đó.',
             'One act of copying homework for someone, one outing to do something reckless, one ride with an unsafe driver. Many accidents begin that way.'),
            ('Bản lĩnh không chỉ nằm ở những tình huống to tát. Nó nằm ở khoảnh khắc em ngắt được dòng cuốn của đám đông.',
             'Strength is not found only in dramatic situations. It lives in the moment when you interrupt the momentum of the crowd.'),
            ('Một chữ không nói ra đúng lúc nhiều khi đắt hơn một bài học nói ra sau khi đã hỏng.',
             'A no not spoken at the right time is often costlier than a lesson learned after damage has been done.'),
        ],
        'lesson_vn': 'Dạy học sinh nói không không phải dạy cứng đầu. Đó là dạy năng lực tự bảo vệ trước sức ép xã hội.',
        'lesson_en': 'Teaching students to say no is not teaching stubbornness. It is teaching self-protection against social pressure.',
    },
    {
        'title_vn': 'Người Thợ Giữ Giới Hạn Của Mình',
        'title_en': 'The Craftsman Who Kept His Limits',
        'pairs': [
            ('Một người thợ nổi tiếng vì làm việc chắc tay, nhưng ông luôn từ chối nhận quá số việc mình có thể làm tử tế.',
             'A craftsman became known for reliable work, yet always refused to take on more jobs than he could do well.'),
            ('Người ta chê ông bỏ tiền. Ông đáp: "Nhận quá sức là hại khách, hại nghề, và hại chính mình."',
             'People said he was turning money away. He replied, "Taking on more than I can handle harms the client, the craft, and myself."'),
            ('Học sinh cũng vậy. Gật đầu với mọi yêu cầu không làm em rộng lượng hơn nếu cuối cùng em làm đâu cũng dở và người cũng nát.',
             'Students are the same. Saying yes to every demand does not make you more generous if in the end everything is done poorly and you yourself are wrecked.'),
            ('Ranh giới là thứ giữ chất lượng sống, không phải chỉ để làm khó người khác.',
             'Boundaries protect the quality of life; they are not merely obstacles placed before others.'),
        ],
        'lesson_vn': 'Biết giới hạn của mình là trí khôn, không phải ích kỷ. Người không giữ giới hạn thường trả giá bằng sức khỏe và uy tín.',
        'lesson_en': 'Knowing your limits is wisdom, not selfishness. Those who fail to keep boundaries often pay with health and credibility.',
    },
    {
        'title_vn': 'Câu Từ Chối Không Cần Gắt',
        'title_en': 'A Refusal Does Not Need to Be Harsh',
        'pairs': [
            ('Nhiều học sinh ngại từ chối vì nghĩ đã nói không là phải căng thẳng và làm mất lòng.',
             'Many students avoid refusing because they think saying no must create tension and offense.'),
            ('Thực ra có những câu rất đơn giản: "Tao không làm chuyện đó," "Tao không đi đâu," "Tao đang quá tải rồi."',
             'In fact, there are simple sentences: "I am not doing that," "I am not going," "I am already overloaded."'),
            ('Ranh giới rõ mà bình tĩnh thường có sức nặng hơn kiểu giải thích dài dòng xin phép được tồn tại.',
             'Clear and calm boundaries often carry more weight than lengthy justifications begging permission to exist.'),
            ('Học sinh cần luyện câu từ chối như luyện bài tập. Đến lúc áp lực đến, thứ đã luyện mới bật ra được.',
             'Students need to practice refusal as they practice exercises. When pressure comes, only what has been practiced will come out.'),
        ],
        'lesson_vn': 'Dám nói không không đồng nghĩa với dữ dằn. Nhiều ranh giới vững nhất được nói bằng giọng rất bình thường.',
        'lesson_en': 'Having the courage to say no does not mean being aggressive. Many of the strongest boundaries are spoken in an ordinary tone.',
    },
    {
        'title_vn': 'Không Thích Không Có Nghĩa Phải Cố Hợp',
        'title_en': 'Disliking Something Does Not Mean You Must Force Yourself to Fit',
        'pairs': [
            ('Có học sinh nhận mọi lời mời, mọi vai trò, mọi hoạt động chỉ vì sợ mình khó gần.',
             'Some students accept every invitation, role, and activity because they fear seeming difficult.'),
            ('Nhưng con người không lớn lên bằng cách luôn ép mình hợp với mọi chỗ.',
             'But people do not mature by constantly forcing themselves to fit everywhere.'),
            ('Có việc em không thích đơn giản vì nó không hợp em. Không cần biến điều đó thành lỗi đạo đức.',
             'Some things you dislike simply do not suit you. There is no need to turn that fact into a moral defect.'),
            ('Biết nói không với cái không hợp cũng là cách giữ năng lượng cho cái đáng.',
             'Knowing how to refuse what does not fit is also a way of preserving energy for what matters.'),
        ],
        'lesson_vn': 'Học sinh không cần vừa lòng tất cả để trở thành người tử tế. Biết chọn cũng là một phần của trưởng thành.',
        'lesson_en': 'Students do not need to please everyone in order to be decent. Selection is part of maturity too.',
    },
    {
        'title_vn': 'Từ Chối Một Người Lớn',
        'title_en': 'Refusing an Adult',
        'pairs': [
            ('Khó nhất không phải lúc từ chối bạn bè. Khó nhất là khi người ép em là một người lớn có quyền hơn.',
             'The hardest refusals are not always to peers. Sometimes the hardest moment comes when the pressure is from an adult with more power.'),
            ('Một học sinh bị bắt làm thêm việc tập thể vô lý trong lúc đã quá tải học hành. Em rất sợ nói không vì sợ bị ghét.',
             'A student was forced into unreasonable extra duties while already overloaded with study. He feared saying no because he feared being disliked.'),
            ('Cuối cùng em học cách nói: "Em muốn giúp, nhưng hiện tại em không đảm bảo làm tốt được."',
             'Eventually he learned to say, "I want to help, but at present I cannot guarantee I will do it well."'),
            ('Từ chối người có quyền cần nhiều khôn ngoan hơn, nhưng vẫn là kỹ năng cần có.',
             'Refusing someone with authority requires more tact, but it is still a necessary skill.'),
        ],
        'lesson_vn': 'Học sinh cần được dạy cách bảo vệ ranh giới cả trước người trên, không chỉ với bạn bè ngang hàng.',
        'lesson_en': 'Students need to learn how to protect boundaries not only with peers, but also with authority figures.',
    },
    {
        'title_vn': 'Khi Em Nói Không Với Phiên Bản Tệ Của Mình',
        'title_en': 'When You Say No to the Worse Version of Yourself',
        'pairs': [
            ('Có lúc ranh giới lớn nhất không nằm bên ngoài. Nó nằm trong đầu khi em muốn buông xuôi, muốn trả đũa, muốn nói dối cho xong.',
             'At times the biggest boundary is not outside. It lies in the mind when you want to give up, retaliate, or lie to escape.'),
            ('Không ai nhìn thấy những lần nói không với bản thân đó, nhưng nó tạo nên phần cứng nhất của nhân cách.',
             'No one sees those refusals inside the self, yet they build the hardest part of character.'),
            ('Người giữ được mình trong lúc không ai nhìn thường là người đứng được lâu nhất khi ai cũng nhìn.',
             'The person who can govern themselves when no one watches is often the one who stands longest when everyone watches.'),
            ('Tự chủ không hào nhoáng, nhưng nó là xương sống của tự do.',
             'Self-control is not glamorous, but it is the backbone of freedom.'),
        ],
        'lesson_vn': 'Cuối cùng, chữ không quan trọng nhất là chữ em nói với phần thấp của chính mình. Từ đó mọi ranh giới khác mới có gốc.',
        'lesson_en': 'In the end, the most important no is the one you say to the lower part of yourself. From there all other boundaries gain roots.',
    },
])

ch12.extend([
    {
        'title_vn': 'Đứng Dậy Không Có Nhạc Nền',
        'title_en': 'Rising Without Background Music',
        'pairs': [
            ('Nhiều câu chuyện truyền cảm hứng kể việc đứng dậy như một khoảnh khắc rất đẹp. Đời thật thường không vậy.',
             'Many inspirational stories portray rising again as a beautiful moment. Real life usually does not.'),
            ('Đứng dậy ngoài đời thường diễn ra trong căn phòng lộn xộn, tâm trạng nặng, và một gương mặt chưa hề thấy khá hơn.',
             'Rising in real life often happens in a messy room, with a heavy mood, and a face that does not yet look better.'),
            ('Em vẫn buồn, vẫn ngại, vẫn chưa tin mình ổn lên được, nhưng em làm việc cần làm trước đã.',
             'You may still feel sad, embarrassed, and unconvinced that things will improve, but you do the necessary work first.'),
            ('Hồi phục thật thường không kịch tính. Nó bền vì nó không phụ thuộc cảm hứng.',
             'Real recovery is often not dramatic. It lasts because it does not depend on inspiration.'),
        ],
        'lesson_vn': 'Đừng chờ cảm giác sẵn sàng mới đứng dậy. Nhiều lần, hành động đi trước rồi tinh thần mới theo sau.',
        'lesson_en': 'Do not wait to feel ready before rising. Many times action comes first, and the spirit follows later.',
    },
    {
        'title_vn': 'Người Thợ Học Lại Từ Mũi Đục Đầu Tiên',
        'title_en': 'The Craftsman Who Started Again With the First Chisel Stroke',
        'pairs': [
            ('Có người thợ làm hỏng một món lớn, mất uy tín, phải bắt đầu lại từ những việc nhỏ nhất.',
             'A craftsman ruined an important commission, lost credibility, and had to start again from the smallest jobs.'),
            ('Ông không lấy lại tên tuổi bằng một cú bứt phá. Ông lấy lại nó bằng hàng trăm lần làm đúng những việc bé mà không ai vỗ tay.',
             'He did not regain his name through one dramatic comeback. He regained it through hundreds of correct small acts that no one applauded.'),
            ('Học sinh sau cú ngã cũng vậy. Danh dự và niềm tin thường được xây lại bằng việc nhỏ lặp đi lặp lại.',
             'Students after a fall are the same. Dignity and trust are often rebuilt through repeated small actions.'),
            ('Không có đường tắt tử tế cho việc dựng lại một con người.',
             'There is no decent shortcut for rebuilding a person.'),
        ],
        'lesson_vn': 'Muốn đứng dậy bền, hãy chấp nhận làm lại từ những viên gạch nhỏ. Sự nóng vội thường chỉ làm căn nền mới nứt tiếp.',
        'lesson_en': 'To rise in a lasting way, accept rebuilding with small bricks. Impatience often only cracks the new foundation again.',
    },
    {
        'title_vn': 'Bài Học Không Có Trong Bằng Khen',
        'title_en': 'The Lesson Not Found in Certificates',
        'pairs': [
            ('Bằng khen ghi lại lúc em đang sáng. Nhưng phần trưởng thành lớn nhất nhiều khi được viết ở những đoạn tối hơn.',
             'Certificates record moments when you shine. But the greatest part of maturity is often written in darker passages.'),
            ('Một người học cách ngồi dậy sau trượt ngã sẽ mang kỹ năng đó suốt đời, trong công việc, hôn nhân, bệnh tật, và mất mát.',
             'A person who learns to rise after falling carries that skill for life, into work, marriage, illness, and loss.'),
            ('Không có tấm giấy đẹp nào ghi: em đã không bỏ mình lại sau khi thất bại. Nhưng đó là một thành tựu rất lớn.',
             'There is no elegant certificate that says: you did not abandon yourself after failure. Yet that is a great achievement.'),
            ('Trường học nếu chỉ khen thành tích mà không dạy hồi phục thì đang bỏ quên một nửa đời người.',
             'A school that praises achievement but does not teach recovery is neglecting half of life.'),
        ],
        'lesson_vn': 'Giáo dục cần tôn trọng những kỹ năng không treo trên tường: hồi phục, bền bỉ, và tự kéo mình qua giai đoạn tệ.',
        'lesson_en': 'Education needs to honor skills that are never hung on walls: recovery, endurance, and self-restoration through hard periods.',
    },
    {
        'title_vn': 'Không Cần Trả Thù Thất Bại',
        'title_en': 'You Do Not Need to Take Revenge on Failure',
        'pairs': [
            ('Sau khi thua, nhiều học sinh lao vào học như để trả thù cú ngã vừa rồi.',
             'After losing, many students throw themselves into study as if taking revenge on the fall.'),
            ('Năng lượng đó có thể mạnh trong ngắn hạn, nhưng thường mang theo rất nhiều cay cú và tự ép.',
             'That energy may be powerful in the short term, but it often carries bitterness and self-violence.'),
            ('Đứng dậy không nhất thiết phải dựa vào thù hằn. Em có thể đi tiếp bằng sự điềm tĩnh hơn: mình sai đâu sửa đó, chưa đủ đâu bồi đó.',
             'Rising again does not have to rely on resentment. You can continue more calmly: fix where you were wrong, strengthen where you were not enough.'),
            ('Người phục hồi lành mạnh thường đi xa hơn người chỉ cháy bùng lên vì tức.',
             'Those who recover healthily often go farther than those who burn briefly from anger.'),
        ],
        'lesson_vn': 'Đừng biến thất bại thành cuộc chiến với chính mình. Sửa lại bản thân hiệu quả hơn trừng phạt bản thân.',
        'lesson_en': 'Do not turn failure into war against yourself. Correcting yourself works better than punishing yourself.',
    },
    {
        'title_vn': 'Đường Dài Ưa Người Bền Hơn Người Bốc',
        'title_en': 'The Long Road Favors the Steady Over the Explosive',
        'pairs': [
            ('Có học sinh sau một cú vấp bùng lên rất mạnh vài tuần rồi tắt. Có học sinh khác hồi lại chậm hơn nhưng đều.',
             'Some students erupt with effort for a few weeks after a fall and then burn out. Others recover more slowly but steadily.'),
            ('Đường dài hiếm khi thưởng cho người bốc nhất. Nó thường thưởng cho người giữ nhịp được lâu.',
             'The long road rarely rewards the most explosive person. It usually rewards the one who can keep rhythm.'),
            ('Đời sống học tập cũng như tập luyện cơ thể: quá đà rồi đứt quãng thường kém hơn vừa sức mà bền.',
             'Study is like training the body: going too hard and breaking off is often worse than a moderate pace sustained well.'),
            ('Sau vấp ngã, việc cần nhất không phải là hứa thật lớn. Nó là tìm lại nhịp có thể giữ được.',
             'After a stumble, the most necessary thing is not a grand promise. It is recovering a rhythm you can sustain.'),
        ],
        'lesson_vn': 'Muốn đứng dậy và đi xa, học sinh phải học yêu sự bền hơn sự bốc đồng. Nhịp đúng quan trọng hơn hào quang ngắn.',
        'lesson_en': 'To rise and travel far, students must learn to value steadiness over sudden intensity. The right rhythm matters more than brief glory.',
    },
    {
        'title_vn': 'Một Ngày Nhìn Lại, Em Sẽ Biết Mình Đã Qua',
        'title_en': 'One Day You Will Look Back and Know You Passed Through',
        'pairs': [
            ('Khi đang ở giữa giai đoạn tệ, học sinh rất khó tin rằng rồi nó sẽ lùi lại phía sau.',
             'When in the middle of a bad period, students find it very hard to believe it will eventually move behind them.'),
            ('Nhưng nhiều người trưởng thành nhìn lại đều có một đoạn từng tưởng không qua nổi, cuối cùng vẫn qua.',
             'Yet many adults look back and find a period they once thought unsurvivable, and still they passed through it.'),
            ('Không phải vì lúc đó họ mạnh sẵn. Nhiều khi chỉ vì họ chịu sống thêm từng ngày một, rồi từng bước một.',
             'Not because they were already strong then. Often simply because they kept living one day at a time, and then one step at a time.'),
            ('Hồi phục lớn đôi khi chỉ là tổng cộng của rất nhiều ngày không bỏ cuộc.',
             'Great recovery is sometimes nothing more than the sum of many days of not quitting.'),
        ],
        'lesson_vn': 'Khi học sinh đang ở đáy, đừng bắt các em nhìn quá xa. Nhiều lúc mục tiêu đủ tốt chỉ là qua được hôm nay cho tử tế.',
        'lesson_en': 'When students are at the bottom, do not force them to look too far ahead. Sometimes the goal that is good enough is simply to get through today with dignity.',
    },
])

print("Đang tạo chương 9-12...")

make_chapter('ch09-suc-khoe-tam-than', 9,
    'Sức Khỏe Tâm Thần',
    'Mental Health', ch09)

make_chapter('ch10-co-don-trong-dam-dong', 10,
    'Cô Đơn Trong Đám Đông',
    'Loneliness in a Crowd', ch10)

make_chapter('ch11-dam-noi-khong', 11,
    'Dám Nói Không',
    'The Courage to Say No', ch11)

make_chapter('ch12-dung-day-sau-vap-nga', 12,
    'Đứng Dậy Sau Vấp Ngã',
    'Rising After a Fall', ch12)

print("Hoàn tất chương 9-12!")
