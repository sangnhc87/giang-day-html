#!/usr/bin/env python3
# gen_q9_a.py -- Quyển IX chương 1-4
import os
import re

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


def make_chapter(filename, vn_title, en_title, stories):
    lines = []
    lines.append(r'\chapter{' + fix(vn_title) + r'}')
    lines.append(r'\markboth{' + fix(vn_title) + r'}{' + fix(en_title) + r'}')
    lines.append('')
    for idx, story in enumerate(stories, 1):
        lines.append(r'\section{' + fix(story['title_vn']) + r'}')
        lines.append(r'\begin{truyen}{' + fix(story['title_vn']) + r'}{' + fix(story['title_en']) + r'}')
        first = True
        for vn, en in story['pairs']:
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
        lines.append(fix(story['lesson_vn']))
        lines.append(r'\textit{(' + fix(story['lesson_en']) + r')}')
        lines.append(r'\end{baihoc}')
        lines.append('')
        lines.append(r'\begin{ghinhoanh}')
        lines.append(r'\textbf{Short English to remember:}')
        lines.append('')
        for sentence in split_sentences(story['lesson_en']):
            lines.append(fix(sentence))
            lines.append('')
        lines.append(r'\end{ghinhoanh}')
        lines.append('')
        lines.append(r'\begin{tuhocnhanh}')
        lines.append(r'\textbf{Cau hoi tu hoc / Self-study questions}')
        lines.append('')
        lines.append(r'1. Van de chinh la gi? \textit{What is the main problem?}')
        lines.append('')
        lines.append(r'2. Bai hoc thuc te la gi? \textit{What is the practical lesson?}')
        lines.append('')
        lines.append(r'3. Mot cau tieng Anh em muon nho la cau nao? \textit{Which English sentence do you want to remember?}')
        lines.append(r'\end{tuhocnhanh}')
        if idx < len(stories):
            lines.append(r'\ngancach')
        lines.append('')
    with open(os.path.join(CHAPTERS_DIR, filename + '.tex'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f'  Đã tạo: {filename}.tex')


ch01 = [
    {
        'title_vn': 'Ra Trường Xong, Không Ai Phát Đề Cương Cho Em Nữa',
        'title_en': 'After Graduation, No One Gives You an Outline',
        'pairs': [
            ('Ngày còn đi học, em luôn biết kỳ thi ở đâu, môn nào quan trọng, và mốc nào phải chạy tới.',
             'When you were in school, you always knew where the exam was, which subject mattered, and which deadline was coming.'),
            ('Ra trường rồi, nhiều người hoảng vì không còn ai vẽ sẵn đường cho mình.',
             'After graduation, many people panic because no one draws the road for them.'),
            ('Không có thời khóa biểu không có nghĩa là em tự do hơn ngay. Nhiều khi nó chỉ có nghĩa là em phải tự cầm lái.',
             'No timetable does not mean instant freedom. It often only means that you must drive yourself.'),
            ('Rất nhiều người trẻ không thua vì kém. Họ thua vì quen sống trong đường ray quá lâu.',
             'Many young people do not fail because they are weak. They fail because they lived on rails for too long.'),
        ],
        'lesson_vn': 'Bước vào đời là bước vào nơi không còn bài mẫu. Muốn đi được, em phải tập tự đặt mục tiêu và tự giữ nhịp cho mình.',
        'lesson_en': 'Entering adult life means entering a place with no model answer. To move well, you must set your own goals and keep your own rhythm.',
    },
    {
        'title_vn': 'Chiếc Đồng Phục Cởi Ra, Áp Lực Không Biến Mất',
        'title_en': 'The Uniform Is Gone, But Pressure Stays',
        'pairs': [
            ('Nhiều học sinh tưởng ra khỏi trường là thoát áp lực.',
             'Many students think leaving school means escaping pressure.'),
            ('Sự thật là áp lực chỉ đổi áo. Từ điểm số sang tiền bạc, từ kỳ thi sang công việc, từ kỳ vọng của thầy cô sang kỳ vọng của đời.',
             'The truth is that pressure only changes clothes. It moves from scores to money, from exams to work, from teachers’ expectations to life’s expectations.'),
            ('Nếu em không học cách chịu áp lực từ lúc còn trẻ, em sẽ bị đời dạy lại bằng học phí đắt hơn nhiều.',
             'If you do not learn how to carry pressure while young, life will teach it again at a much higher cost.'),
            ('Trưởng thành không làm gánh nặng biến mất. Nó chỉ yêu cầu em vững hơn khi mang nó.',
             'Growing up does not make burdens disappear. It only asks you to become steadier while carrying them.'),
        ],
        'lesson_vn': 'Đừng ảo tưởng rằng ra trường là hết mệt. Điều quan trọng là học cách mệt mà vẫn không gãy.',
        'lesson_en': 'Do not imagine that life after school is free of strain. What matters is learning how to be tired without breaking.',
    },
    {
        'title_vn': 'Không Còn Chuông Vào Lớp, Cũng Không Còn Chuông Cứu Em',
        'title_en': 'There Is No Bell to Save You Anymore',
        'pairs': [
            ('Trong trường học, mỗi tiết học đều có điểm bắt đầu và kết thúc rõ ràng.',
             'In school, every class has a clear beginning and ending.'),
            ('Ngoài đời, nhiều việc không tự dừng lại chỉ vì em đã mệt.',
             'Outside school, many things do not stop simply because you are tired.'),
            ('Một công việc dở không có tiếng chuông cứu. Một khoản nợ cũng không tự hết giờ.',
             'A bad job has no bell to rescue you. A debt does not expire because time is up.'),
            ('Vì thế người trẻ phải học kỹ năng tự chặn mình, tự nghỉ đúng lúc, và tự quay lại đúng giờ.',
             'That is why young adults must learn to stop themselves, rest at the right time, and return at the right time.'),
        ],
        'lesson_vn': 'Ra đời đòi hỏi tự quản nhiều hơn đi học. Ai không tự quản được thời gian và sức lực thì rất dễ bị cuốn trôi.',
        'lesson_en': 'Adult life demands more self-management than school. Those who cannot manage time and energy are easily swept away.',
    },
    {
        'title_vn': 'Bằng Cấp Là Vé Vào Cửa, Không Phải Ghế Ngồi Sẵn',
        'title_en': 'A Degree Opens the Door, Not the Seat',
        'pairs': [
            ('Có người cầm bằng tốt nghiệp và tưởng từ đây mình đương nhiên phải có chỗ đứng tốt.',
             'Some people hold a degree and think that from now on a good place is automatically theirs.'),
            ('Nhưng bằng cấp chỉ giúp em được nhìn thấy. Nó không tự chứng minh em làm được việc.',
             'But a degree only helps you be seen. It does not prove that you can do the work.'),
            ('Ngoài đời, chỗ đứng thường phải được dựng bằng việc làm thật, cách làm việc thật, và thái độ thật.',
             'In real life, your place is usually built by real work, real discipline, and real attitude.'),
            ('Cầm bằng mà kiêu quá sớm là một kiểu ngây thơ rất phổ biến của tuổi trẻ.',
             'Holding a degree and becoming proud too early is a very common youth mistake.'),
        ],
        'lesson_vn': 'Hãy tôn trọng bằng cấp, nhưng đừng thần thánh hóa nó. Đời còn hỏi thêm rất nhiều câu sau tấm bằng.',
        'lesson_en': 'Respect a degree, but do not worship it. Life asks many more questions after the certificate.',
    },
    {
        'title_vn': 'Ngày Đầu Không Còn Ai Gọi Em Là Học Sinh Giỏi',
        'title_en': 'On Day One, No One Calls You the Top Student',
        'pairs': [
            ('Có những người từng rất sáng trong trường học nhưng bước vào môi trường mới lại thấy mình bình thường hẳn.',
             'Some people were brilliant in school but enter a new environment and suddenly feel very ordinary.'),
            ('Điều đó đau, nhưng cần. Nó kéo cái tôi từ trên mây xuống mặt đất.',
             'That hurts, but it is necessary. It brings the ego down from the clouds to the ground.'),
            ('Ở nơi mới, em không còn sống bằng danh hiệu cũ. Em phải bắt đầu lại bằng giá trị hiện tại.',
             'In a new place, you cannot live on old titles. You must begin again with present value.'),
            ('Bắt đầu lại từ số không không hạ nhục em. Nó chỉ nói rằng sân chơi đã đổi.',
             'Starting again from zero does not humiliate you. It only means the arena has changed.'),
        ],
        'lesson_vn': 'Người trẻ cần học cách rời bỏ vinh quang cũ. Ai ôm mãi quá khứ giỏi giang thường khó lớn tiếp.',
        'lesson_en': 'Young people must learn to leave old glory behind. Those who cling to yesterday’s success often struggle to grow.',
    },
]

ch02 = [
    {
        'title_vn': 'Công Việc Đầu Tiên Thường Không Giống Trong Tưởng Tượng',
        'title_en': 'The First Job Is Usually Not What You Imagined',
        'pairs': [
            ('Nhiều người trẻ đi làm với ý nghĩ rằng mình sẽ được làm những việc quan trọng ngay.',
             'Many young people start work thinking they will handle important tasks right away.'),
            ('Nhưng việc đầu tiên thường là việc nhỏ, lặp lại, và có phần chán.',
             'But the first work is often small, repetitive, and a little boring.'),
            ('Đó không hẳn là coi thường em. Đó là cách đời kiểm tra xem em có làm tốt việc nhỏ không.',
             'That is not always disrespect. It is how life checks whether you can do small work well.'),
            ('Ai cũng muốn được tin ngay. Nhưng phần lớn niềm tin được xây từ những việc ít ai để ý.',
             'Everyone wants quick trust. But most trust is built from tasks that few people notice.'),
        ],
        'lesson_vn': 'Đừng khinh việc nhỏ ở công việc đầu tiên. Rất nhiều người mất cơ hội lớn chỉ vì làm ẩu những việc tưởng như bé.',
        'lesson_en': 'Do not despise small tasks in your first job. Many people lose big chances because they do small work carelessly.',
    },
    {
        'title_vn': 'Đi Làm Mới Biết Thông Minh Không Đủ',
        'title_en': 'Work Teaches You That Intelligence Is Not Enough',
        'pairs': [
            ('Một người có thể hiểu rất nhanh nhưng vẫn làm đồng đội mệt nếu trễ giờ, khó hợp tác, và không giữ lời.',
             'A person may understand things fast and still exhaust a team by being late, hard to work with, and careless with promises.'),
            ('Ngoài đời, người ta không chỉ nhìn em biết gì. Người ta còn nhìn em làm việc cùng người khác thế nào.',
             'In real life, people do not only see what you know. They also see how you work with others.'),
            ('Có những người rất sáng nhưng đi chậm vì kỹ năng người quá yếu.',
             'Some very bright people move slowly because their people skills are weak.'),
            ('Thông minh là lợi thế lớn. Nhưng tính ổn định và đáng tin mới giúp em đi lâu.',
             'Intelligence is a major advantage. But steadiness and trustworthiness are what help you last.'),
        ],
        'lesson_vn': 'Muốn đi xa, người trẻ phải rèn cả năng lực lẫn cách làm việc với người khác. Một mình giỏi chưa chắc đã đủ.',
        'lesson_en': 'To go far, young people must build both skill and the ability to work with others. Being clever alone is not always enough.',
    },
    {
        'title_vn': 'Làm Lại Từ Đầu Là Chuyện Bình Thường',
        'title_en': 'Doing It Again from the Start Is Normal',
        'pairs': [
            ('Ngày đi học, làm gần đúng đôi khi vẫn được điểm phần nào.',
             'In school, being almost right sometimes still earns some marks.'),
            ('Đi làm rồi, một việc gần đúng có thể vẫn là chưa dùng được.',
             'At work, something almost right may still be unusable.'),
            ('Nhiều người trẻ tự ái khi bị yêu cầu làm lại. Họ tưởng đó là phủ nhận mình.',
             'Many young people feel offended when asked to redo work. They think it is rejection.'),
            ('Thực ra nhiều lần đó chỉ là tiêu chuẩn. Việc chưa đạt thì phải sửa cho đạt.',
             'In many cases it is simply the standard. If the work is not good enough, it must be fixed.'),
        ],
        'lesson_vn': 'Bớt tự ái với phản hồi sẽ giúp em lớn nhanh hơn. Làm lại cho tốt không làm em nhỏ đi.',
        'lesson_en': 'If you become less defensive about feedback, you grow faster. Reworking something well does not make you smaller.',
    },
    {
        'title_vn': 'Sếp Không Phải Lúc Nào Cũng Là Thầy Tử Tế',
        'title_en': 'A Boss Is Not Always a Kind Teacher',
        'pairs': [
            ('Nhiều người bước vào đời và sốc vì phát hiện không phải ai hơn mình cũng có trách nhiệm nâng đỡ mình.',
             'Many people enter adult life and are shocked to learn that not everyone above them feels responsible for helping them grow.'),
            ('Có sếp chỉ quan tâm kết quả. Có người thiếu kiên nhẫn. Có người giỏi việc nhưng dở cách dẫn người.',
             'Some bosses only care about results. Some lack patience. Some are good at the job but poor at leading people.'),
            ('Điều đó không đẹp, nhưng có thật.',
             'That is not beautiful, but it is real.'),
            ('Người trẻ cần học cách tự học cả trong môi trường không lý tưởng.',
             'Young people need to learn even inside environments that are not ideal.'),
        ],
        'lesson_vn': 'Ra đời là chấp nhận rằng không phải lúc nào em cũng gặp người hướng dẫn tốt. Càng vậy, năng lực tự học càng quý.',
        'lesson_en': 'Adult life means accepting that you will not always meet good mentors. That is why self-learning becomes more valuable.',
    },
    {
        'title_vn': 'Đi Làm Mới Biết Mệt Kiểu Khác Đi Học',
        'title_en': 'Work Exhausts You in a Different Way from School',
        'pairs': [
            ('Đi học mệt vì kiểm tra, vì bài vở, vì áp lực thành tích.',
             'School is tiring because of tests, lessons, and performance pressure.'),
            ('Đi làm mệt thêm vì lặp lại, vì trách nhiệm, vì phải giữ thái độ kể cả lúc không vui.',
             'Work adds new fatigue: repetition, responsibility, and the need to stay professional even when unhappy.'),
            ('Có người không chuẩn bị tâm lý cho kiểu mệt này nên rất dễ vỡ mộng.',
             'Some people do not prepare mentally for this kind of tiredness, so they become disillusioned very quickly.'),
            ('Mỗi giai đoạn của đời có một kiểu nặng riêng. Khôn ngoan là học cách mang nó đúng, không phải ngây thơ nghĩ nó sẽ không tới.',
             'Every stage of life has its own weight. Wisdom means learning how to carry it well, not pretending it will never come.'),
        ],
        'lesson_vn': 'Đi làm không chỉ cần năng lực. Nó còn cần sức bền tâm lý cho những ngày rất bình thường nhưng rất hao người.',
        'lesson_en': 'Work requires more than ability. It also needs mental stamina for ordinary days that quietly drain you.',
    },
]

ch03 = [
    {
        'title_vn': 'Lương Đầu Không Nhiều Như Em Tưởng',
        'title_en': 'The First Salary Feels Smaller Than You Thought',
        'pairs': [
            ('Nhiều người tưởng cầm lương đầu sẽ thấy mình lớn hẳn lên.',
             'Many people think their first salary will make them feel fully grown.'),
            ('Nhưng vừa trừ tiền nhà, tiền ăn, đi lại, và vài khoản phát sinh, số còn lại rất khiêm tốn.',
             'But after rent, food, transport, and surprise expenses, what remains is often modest.'),
            ('Lúc đó nhiều người mới hiểu vì sao người lớn quanh mình luôn phải tính.',
             'At that moment many finally understand why the adults around them always had to calculate carefully.'),
            ('Tiền đầu tiên không chỉ cho em niềm vui. Nó cho em cái nhìn thật hơn về đời sống.',
             'The first salary gives not only joy. It gives a more realistic view of life.'),
        ],
        'lesson_vn': 'Kiếm được tiền là một bước lớn. Nhưng học cách giữ tiền mới là bước khiến em bớt ngây thơ.',
        'lesson_en': 'Earning money is a big step. Learning how to keep it is the step that makes you less naive.',
    },
    {
        'title_vn': 'Tiền Tự Do Và Cái Bẫy Mua Để Chứng Minh',
        'title_en': 'Freedom Money and the Trap of Buying to Prove Yourself',
        'pairs': [
            ('Khi có tiền đầu tiên, nhiều người muốn mua một thứ gì đó để thấy mình không còn là đứa trẻ đi xin nữa.',
             'When people get their first money, many want to buy something just to feel they are no longer children asking for things.'),
            ('Mong muốn đó rất dễ hiểu. Nhưng nếu không tỉnh, em sẽ tiêu để chứng minh hơn là tiêu để sống.',
             'That desire is easy to understand. But without awareness, you spend to prove something more than to live well.'),
            ('Một chiếc điện thoại đắt có thể cho em cảm giác hơn người trong vài ngày. Một khoản tiết kiệm lại cho em bình an nhiều tháng.',
             'An expensive phone may give you a sense of status for a few days. Savings can give peace for many months.'),
            ('Người trẻ hay lẫn giữa cái mình thích ngay và cái mình cần lâu dài.',
             'Young people often confuse what they want now with what they need for the long run.'),
        ],
        'lesson_vn': 'Tiền đầu tiên rất dễ bị tiêu vì cái tôi. Muốn trưởng thành tài chính, em phải học tiêu theo giá trị, không chỉ theo cảm xúc.',
        'lesson_en': 'First money is easily spent by the ego. To grow financially, you must spend by values, not only by emotion.',
    },
    {
        'title_vn': 'Một Lần Quẹt Sai, Mất Cả Tháng Thở Dài',
        'title_en': 'One Bad Swipe Can Cost You a Whole Month',
        'pairs': [
            ('Có người trẻ dùng thẻ hay vay app rất nhẹ tay vì tiền chưa phải rời khỏi ví ngay trước mắt.',
             'Some young people use cards or loan apps too easily because the money does not seem to leave their hand right away.'),
            ('Đến lúc phải trả, họ mới thấy quyết định vài giây có thể kéo dài áp lực cả tháng.',
             'When payment time arrives, they realize that a few seconds of decision can create a month of pressure.'),
            ('Tiện lợi tài chính là thứ đẹp ở mặt ngoài nhưng dễ cắn nếu dùng thiếu tỉnh táo.',
             'Financial convenience looks nice on the surface but bites hard when used without care.'),
            ('Nhiều người lớn khổ không phải vì họ không làm ra tiền. Họ khổ vì không quản được nhịp tiêu tiền.',
             'Many adults suffer not because they cannot earn money, but because they cannot manage the rhythm of spending.'),
        ],
        'lesson_vn': 'Đừng coi nợ nhỏ là vô hại. Nhiều cái vòng siết bắt đầu từ những khoản rất nhỏ nhưng rất dễ dãi.',
        'lesson_en': 'Do not treat small debt as harmless. Many traps begin with tiny amounts handled too casually.',
    },
    {
        'title_vn': 'Tiền Đầu Không Chỉ Là Tiền Của Em',
        'title_en': 'Your First Money Is Not Only About You',
        'pairs': [
            ('Nhiều người trẻ lần đầu cầm tiền mới thấy một cảm giác lạ: mình muốn mua cho bố mẹ cái gì đó.',
             'Many young people feel something strange with their first money: they want to buy something for their parents.'),
            ('Khoảnh khắc đó đánh dấu một bước tâm lý rất lớn. Em bắt đầu hiểu mình không còn chỉ là người nhận.',
             'That moment marks a major psychological step. You begin to understand that you are no longer only a receiver.'),
            ('Trưởng thành một phần là từ chỗ nghĩ mình cần gì sang chỗ nghĩ mình có thể đỡ ai được gì.',
             'Part of growing up is moving from what you need to what you can help carry for others.'),
            ('Tiền đầu tiên vì thế không chỉ có giá trị vật chất. Nó còn có giá trị đạo đức.',
             'That is why first money holds not only material value, but moral value too.'),
        ],
        'lesson_vn': 'Khi đồng tiền đầu tiên khiến em nghĩ đến người khác, đó là dấu hiệu em đang lớn lên đúng hướng.',
        'lesson_en': 'When your first money makes you think about others, it is a sign that you are growing in the right direction.',
    },
    {
        'title_vn': 'Tự Do Không Có Nghĩa Là Muốn Tiêu Sao Cũng Được',
        'title_en': 'Freedom Does Not Mean Spending Without Limits',
        'pairs': [
            ('Nhiều người trẻ lẫn giữa tự do và tùy tiện.',
             'Many young people confuse freedom with impulsiveness.'),
            ('Có tiền riêng rồi, họ nghĩ mình có quyền sống theo cảm xúc hoàn toàn.',
             'Once they earn their own money, they think they have the right to live entirely by feeling.'),
            ('Nhưng tự do thật không phá hỏng tương lai của mình chỉ để thỏa mãn hiện tại.',
             'But real freedom does not damage your future just to satisfy the present.'),
            ('Người không kiểm soát được tiêu dùng thường sớm bị mất tự do bởi chính những lựa chọn của mình.',
             'People who cannot control spending often lose freedom to their own choices very quickly.'),
        ],
        'lesson_vn': 'Tiền có thể cho em lựa chọn. Nhưng chỉ kỷ luật mới giữ cho những lựa chọn đó không quay lại bóp nghẹt em.',
        'lesson_en': 'Money can give you options. But only discipline keeps those options from turning around and choking you.',
    },
]

ch04 = [
    {
        'title_vn': 'Không Ai Nợ Em Một Chỗ Đứng',
        'title_en': 'No One Owes You a Place',
        'pairs': [
            ('Nhiều người trẻ bước vào đời với một niềm tin ngầm rằng nếu mình cố nhiều năm, đời sẽ phải sắp một chỗ xứng đáng cho mình.',
             'Many young people enter life with a hidden belief: if they worked hard for years, life must prepare a worthy place for them.'),
            ('Nhưng đời không vận hành bằng cảm giác xứng đáng. Nó vận hành bằng giá trị, thời điểm, quan hệ, và cả may rủi.',
             'But life does not operate by your feeling of deserving. It moves through value, timing, relationships, and luck as well.'),
            ('Nghe lạnh, nhưng biết sớm thì đỡ vỡ mộng hơn.',
             'It sounds cold, but knowing it early saves some disillusionment.'),
            ('Khi hiểu không ai nợ mình chỗ đứng, em sẽ bớt chờ và bắt đầu dựng chỗ đứng của mình thật hơn.',
             'Once you understand that no one owes you a place, you stop waiting and start building one more honestly.'),
        ],
        'lesson_vn': 'Cảm giác mình xứng đáng không đủ để đổi lấy cơ hội. Người trẻ phải học cách biến xứng đáng thành năng lực thấy được.',
        'lesson_en': 'Feeling deserving is not enough to earn opportunity. Young people must turn that feeling into visible ability.',
    },
    {
        'title_vn': 'Gửi Mười Hồ Sơ, Im Lặng Cả Mười',
        'title_en': 'Ten Applications, Ten Silences',
        'pairs': [
            ('Có người gửi rất nhiều hồ sơ mà không nhận nổi một phản hồi.',
             'Some people send many applications and receive almost no reply.'),
            ('Sự im lặng đó đau theo kiểu rất lạ. Không ai chê thẳng, nhưng cũng không ai chọn.',
             'That silence hurts in a strange way. No one rejects you openly, but no one chooses you either.'),
            ('Nhiều người bắt đầu nghi ngờ cả bản thân chỉ vì không được hồi âm.',
             'Many start doubting their whole self simply because no one answers.'),
            ('Nhưng im lặng nhiều khi không phải bản án cuối. Nó là tín hiệu rằng em phải sửa cách trình bày giá trị của mình.',
             'Yet silence is often not a final sentence. It is a signal that you may need to improve how you present your value.'),
        ],
        'lesson_vn': 'Bị lờ đi không có nghĩa em vô dụng. Nhưng nó buộc em phải nhìn lại cách mình xuất hiện trước cơ hội.',
        'lesson_en': 'Being ignored does not mean you are useless. But it forces you to examine how you show up before opportunity.',
    },
    {
        'title_vn': 'Đời Không Chấm Nỗ Lực Theo Cách Trường Học Chấm',
        'title_en': 'Life Does Not Grade Effort Like School Does',
        'pairs': [
            ('Đi học, cố gắng nhiều thường sẽ được ghi nhận phần nào.',
             'In school, strong effort is often recognized in some form.'),
            ('Ngoài đời, em có thể cố rất nhiều mà kết quả vẫn chưa tới.',
             'Outside school, you may try very hard and still not get the result yet.'),
            ('Điều đó không công bằng hoàn toàn, nhưng là thật.',
             'That is not fully fair, but it is real.'),
            ('Vì thế người trưởng thành phải chịu được giai đoạn làm đúng mà chưa được trả công ngay.',
             'That is why adults must endure periods of doing the right work without immediate reward.'),
        ],
        'lesson_vn': 'Nỗ lực vẫn cần, nhưng người trẻ phải học thêm một điều khó hơn: kiên nhẫn với độ trễ của kết quả.',
        'lesson_en': 'Effort still matters, but young people must learn something harder: patience with delayed results.',
    },
    {
        'title_vn': 'Một Chỗ Đứng Đẹp Mà Em Chưa Gánh Nổi',
        'title_en': 'A Good Position You Cannot Carry Yet',
        'pairs': [
            ('Không phải cơ hội nào đến sớm cũng là may.',
             'Not every early opportunity is good luck.'),
            ('Có chỗ đứng trông rất đẹp, nhưng nếu năng lực và sức bền chưa đủ, em sẽ bị nó đè ngược lại.',
             'Some positions look attractive, but if your skill and stamina are not ready, the role can crush you.'),
            ('Nhiều người trẻ chỉ thấy cái ghế. Họ không nhìn thấy cái lực cần để ngồi vững trên ghế đó.',
             'Many young people see only the seat. They do not see the strength needed to remain steady in it.'),
            ('Đòi quá sớm một chỗ cao đôi khi chỉ làm em gãy nhanh hơn.',
             'Demanding a high place too early sometimes only makes you break faster.'),
        ],
        'lesson_vn': 'Không phải chỗ đứng nào mình muốn ngay cũng là chỗ mình nên có ngay. Có khi đi chậm hơn lại giữ được mình lâu hơn.',
        'lesson_en': 'Not every position you want now is one you should have now. Moving slower can sometimes help you last longer.',
    },
    {
        'title_vn': 'Đứng Ở Mép Cửa Cũng Là Một Giai Đoạn',
        'title_en': 'Standing at the Edge of the Door Is Also a Stage',
        'pairs': [
            ('Có những năm em chưa vào hẳn được phòng lớn của cuộc đời. Em chỉ đứng ở mép cửa, quan sát, học, và gõ nhiều lần.',
             'There are years when you are not yet inside the larger room of life. You stand at the edge, watch, learn, and knock many times.'),
            ('Giai đoạn đó dễ làm người trẻ thấy mình nhỏ và chậm.',
             'That stage easily makes young people feel small and slow.'),
            ('Nhưng đứng ở mép cửa không phải là vô nghĩa. Nó là thời gian để em lớn vào phần mình còn thiếu.',
             'But standing at the edge is not meaningless. It is time for you to grow into what is still missing.'),
            ('Nhiều người vào cửa muộn hơn một chút nhưng bước vào chắc hơn rất nhiều.',
             'Many enter later, but once inside, they stand much more firmly.'),
        ],
        'lesson_vn': 'Đừng khinh giai đoạn chờ và học. Rất nhiều nền móng tốt được xây khi người khác tưởng em vẫn chưa bắt đầu.',
        'lesson_en': 'Do not despise the stage of waiting and learning. Many good foundations are built while others think you have not really begun.',
    },
]

print("Đang tạo chương 1-4...")
make_chapter('ch01-roi-ghe-nha-truong', 'Rời Ghế Nhà Trường, Đời Không Chấm Điểm Công Khai', 'Leaving School, Entering an Ungraded Life', ch01)
make_chapter('ch02-cong-viec-dau-tien', 'Công Việc Đầu Tiên Và Cú Sốc Thực Tế', 'The First Job and the Shock of Reality', ch02)
make_chapter('ch03-tien-tu-do-sai-lam', 'Tiền Đầu Tiên, Tự Do Đầu Tiên, Sai Lầm Đầu Tiên', 'First Money, First Freedom, First Mistakes', ch03)
make_chapter('ch04-khong-ai-no-em-cho-dung', 'Không Ai Nợ Em Một Chỗ Đứng', 'No One Owes You a Place', ch04)
print("Hoàn tất chương 1-4!")
