#!/usr/bin/env python3
# gen_q9_c.py -- Quyển IX chương 9-12
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


ch09 = [
    {
        'title_vn': 'Tử Tế Không Có Nghĩa Là Cho Ai Cũng Bước Qua Em',
        'title_en': 'Kindness Does Not Mean Letting Everyone Walk Over You',
        'pairs': [
            ('Nhiều người trẻ rất sợ bị coi là khó nên gật đầu với mọi yêu cầu.',
             'Many young people fear being seen as difficult, so they say yes to every request.'),
            ('Họ tưởng đó là tử tế.',
             'They think that is kindness.'),
            ('Nhưng khi người khác quen dùng em như một chỗ tiện lợi, đó không còn là giúp đỡ lành mạnh nữa.',
             'But when others grow used to using you as a convenient tool, that is no longer healthy help.'),
            ('Người tử tế thật biết giúp đúng chỗ và biết dừng đúng lúc.',
             'A truly kind person knows how to help at the right place and stop at the right time.'),
        ],
        'lesson_vn': 'Tử tế mà không có ranh giới rất dễ thành mềm yếu. Ranh giới giữ lòng tốt khỏi bị biến thành chỗ khai thác.',
        'lesson_en': 'Kindness without boundaries easily becomes weakness. Boundaries protect goodness from turning into something others exploit.',
    },
    {
        'title_vn': 'Làm Hộ Mãi Không Phải Là Nghĩa Khí',
        'title_en': 'Doing Everything for Others Is Not Loyalty',
        'pairs': [
            ('Có người trẻ luôn làm hộ phần việc của bạn, của đồng nghiệp, của người yêu, vì sợ bị chê là không tình nghĩa.',
             'Some young people keep doing the work of friends, coworkers, or partners because they fear being called disloyal.'),
            ('Lâu dần, họ mệt nhưng vẫn cắn răng chịu.',
             'Over time they become exhausted but still endure silently.'),
            ('Giúp người khác lớn không giống với việc thay họ sống phần trách nhiệm của họ.',
             'Helping someone grow is not the same as living their responsibility for them.'),
            ('Nhiều mối quan hệ hỏng vì một bên cứ cho quá mức, còn bên kia quen nhận quá mức.',
             'Many relationships decay because one side keeps giving too much while the other gets used to taking too much.'),
        ],
        'lesson_vn': 'Người trẻ cần học cách phân biệt giữa hỗ trợ và gánh thay. Nhầm hai thứ đó rất hao đời.',
        'lesson_en': 'Young people must learn the difference between supporting and carrying someone. Confusing the two drains life badly.',
    },
    {
        'title_vn': 'Mềm Mỏng Không Có Nghĩa Là Mờ Ranh Giới',
        'title_en': 'Gentle Does Not Mean Blurry',
        'pairs': [
            ('Nhiều người nghĩ phải thật cứng mới giữ được mình.',
             'Many people think they must be hard to protect themselves.'),
            ('Thực ra em có thể nói rất nhẹ mà vẫn rất rõ.',
             'In fact, you can speak very softly and still be very clear.'),
            ('Một câu như "Mình không làm việc đó" thường mạnh hơn cả bài giải thích dài dòng.',
             'A sentence like "I am not doing that" is often stronger than a long explanation.'),
            ('Ranh giới tốt không cần nhiều kịch tính. Nó chỉ cần nhất quán.',
             'A good boundary does not need drama. It only needs consistency.'),
        ],
        'lesson_vn': 'Người trẻ càng hiền càng nên học nói rõ. Giọng nói nhỏ không có nghĩa là quyền từ chối nhỏ.',
        'lesson_en': 'The gentler a young person is, the more they need to learn clear speech. A quiet voice does not mean a small right to refuse.',
    },
    {
        'title_vn': 'Người Hay Thấy Có Lỗi Thường Dễ Bị Dùng',
        'title_en': 'People Who Feel Guilty Easily Are Easy to Use',
        'pairs': [
            ('Có kiểu người chỉ cần từ chối ai một lần là thấy day dứt rất lâu.',
             'Some people feel guilty for a long time after refusing someone just once.'),
            ('Những người thao túng rất nhạy với kiểu người đó.',
             'Manipulative people are quick to notice that kind of person.'),
            ('Họ không cần ép mạnh. Họ chỉ cần gợi cảm giác em đang tệ, đang ích kỷ, hay đang vô tình.',
             'They do not need to force hard. They only need to suggest that you are selfish, cold, or unkind.'),
            ('Nếu không tỉnh, em sẽ cho đi vì tội lỗi chứ không còn vì tự nguyện.',
             'Without awareness, you begin giving out of guilt instead of choice.'),
        ],
        'lesson_vn': 'Lòng tốt cần đi cùng sự tỉnh táo. Nếu không, cảm giác có lỗi sẽ bị người khác dùng như một cái dây kéo em đi.',
        'lesson_en': 'Kindness must be paired with awareness. Otherwise guilt becomes a rope other people use to pull you around.',
    },
    {
        'title_vn': 'Giúp Người Mà Không Bỏ Mình',
        'title_en': 'Help Others Without Abandoning Yourself',
        'pairs': [
            ('Có những người trẻ sau một thời gian cho đi quá nhiều bỗng thấy mình cạn sạch.',
             'Some young people give too much for too long and suddenly find themselves empty.'),
            ('Lúc đó họ cay đắng và bắt đầu ghét cả sự tử tế của chính mình.',
             'Then they become bitter and start resenting their own kindness.'),
            ('Vấn đề không phải lòng tốt sai. Vấn đề là nó đã được dùng mà không có giới hạn.',
             'The problem is not that goodness is wrong. The problem is that it was used without limits.'),
            ('Một lòng tốt bền là lòng tốt không đòi em phải biến mất để nó tồn tại.',
             'Sustainable kindness is kindness that does not require you to disappear in order to exist.'),
        ],
        'lesson_vn': 'Giúp người khác là điều đẹp. Nhưng đừng làm điều đẹp theo cách phá hỏng chính mình.',
        'lesson_en': 'Helping others is beautiful. But do not do a beautiful thing in a way that destroys you.',
    },
]

ch10 = [
    {
        'title_vn': 'Giỏi Trên Giấy Chưa Chắc Giỏi Trong Phòng Phỏng Vấn',
        'title_en': 'Good on Paper Does Not Mean Good in the Interview Room',
        'pairs': [
            ('Có người bảng điểm rất đẹp nhưng vào phỏng vấn nói lan man, thiếu rõ, và không cho thấy mình hiểu công việc.',
             'Some people have excellent transcripts but speak vaguely in interviews and do not show that they understand the work.'),
            ('Nhà tuyển dụng không chỉ nhìn thành tích. Họ nhìn xem em có thể biến kiến thức thành hành động hay không.',
             'Employers do not only look at achievements. They look at whether you can turn knowledge into action.'),
            ('Người trẻ hay tưởng học giỏi là đủ. Nhưng đời cần thêm cách trình bày, cách ứng xử, và cách chứng minh.',
             'Young people often think being academically strong is enough. But life also needs communication, conduct, and proof.'),
            ('Một năng lực không biết cách xuất hiện thì rất dễ bị bỏ qua.',
             'An ability that does not know how to show up is easy to overlook.'),
        ],
        'lesson_vn': 'Học giỏi rất quý. Nhưng muốn có việc, em còn phải học cách nói rõ mình làm được gì và vì sao mình hợp.',
        'lesson_en': 'Studying well is valuable. But to get work, you must also learn how to explain what you can do and why you fit.',
    },
    {
        'title_vn': 'Kiến Thức Không Ứng Dụng Được Sẽ Bị Nghi Ngờ',
        'title_en': 'Knowledge Without Use Will Be Questioned',
        'pairs': [
            ('Nhiều bạn trẻ học được rất nhiều nhưng không làm ra sản phẩm nào, không có ví dụ nào, không có việc gì chỉ rõ mình từng làm được.',
             'Many young people learn a lot but produce nothing, show no examples, and cannot point to work they have actually done.'),
            ('Khi đó nhà tuyển dụng phải tin vào lời em nói nhiều hơn tin vào dấu vết công việc.',
             'Then an employer must trust your words more than any evidence of work.'),
            ('Điều đó làm em yếu đi trong cạnh tranh.',
             'That weakens you in competition.'),
            ('Kiến thức mạnh hơn khi nó để lại dấu vết: bài viết, dự án, sản phẩm, kỹ năng dùng được.',
             'Knowledge becomes stronger when it leaves traces: writing, projects, products, and usable skill.'),
        ],
        'lesson_vn': 'Muốn người khác tin mình có năng lực, hãy tạo ra bằng chứng nhỏ nhưng thật. Đừng chỉ nói em biết.',
        'lesson_en': 'If you want others to believe in your ability, create small but real evidence. Do not only say that you know.',
    },
    {
        'title_vn': 'Biết Nhiều Không Bằng Làm Xong',
        'title_en': 'Knowing More Is Not Better Than Finishing',
        'pairs': [
            ('Có người học rất rộng nhưng việc nào cũng để dở.',
             'Some people study widely but leave every task unfinished.'),
            ('Ngoài đời, người hoàn thành ổn định thường được tin hơn người biết rất nhiều nhưng hay bỏ lửng.',
             'In real life, people who finish reliably are often trusted more than people who know a lot but leave things hanging.'),
            ('Hoàn thành là một đức tính ít hào nhoáng nhưng rất mạnh.',
             'Finishing is a quiet virtue, but a powerful one.'),
            ('Người trẻ muốn có việc phải học cách đi tới cuối, không chỉ hứng khởi ở đầu.',
             'Young people who want work must learn to go to the end, not only feel excited at the start.'),
        ],
        'lesson_vn': 'Thị trường thường thưởng cho người làm xong và làm được, không chỉ cho người nói hay hay biết nhiều.',
        'lesson_en': 'The market often rewards people who finish and deliver, not only those who speak well or know a lot.',
    },
    {
        'title_vn': 'Giỏi Nhưng Khó Làm Việc Cùng Là Một Điểm Trừ Lớn',
        'title_en': 'Skilled but Hard to Work With Is a Major Problem',
        'pairs': [
            ('Có người rất thông minh nhưng phản ứng gay gắt khi bị góp ý, coi thường người khác, và làm không khí chung nặng nề.',
             'Some people are very smart but react harshly to feedback, look down on others, and make the team atmosphere heavy.'),
            ('Ban đầu họ vẫn được giữ vì năng lực.',
             'At first they may still be kept because of ability.'),
            ('Nhưng về lâu dài, nhiều nơi không muốn trả giá quá lớn cho một người giỏi mà gây hao tổn tập thể.',
             'But in the long run, many workplaces do not want to pay too high a price for one skilled person who drains the whole group.'),
            ('Cách làm việc cùng người khác là một phần của năng lực, không phải chuyện phụ.',
             'The way you work with others is part of competence, not a side issue.'),
        ],
        'lesson_vn': 'Muốn có chỗ đứng bền, người trẻ phải rèn cả tài và nết làm việc. Chỉ có một vế thì rất dễ chông chênh.',
        'lesson_en': 'To keep a stable place, young people must develop both skill and work character. Having only one side is shaky.',
    },
    {
        'title_vn': 'Đi Xin Việc Cũng Là Một Kỹ Năng',
        'title_en': 'Job Seeking Is Also a Skill',
        'pairs': [
            ('Nhiều người nghĩ chỉ cần giỏi là người ta sẽ tự tìm tới.',
             'Many people think that if they are good enough, others will automatically find them.'),
            ('Điều đó hiếm khi đúng lúc mới bắt đầu.',
             'That is rarely true at the beginning.'),
            ('Viết CV, gửi hồ sơ, viết thư ngắn gọn, trả lời email, phỏng vấn, và theo dõi sau buổi gặp đều là kỹ năng phải học.',
             'Writing a CV, sending applications, writing short emails, interviewing, and following up are all skills that must be learned.'),
            ('Người trẻ càng sớm hiểu đi xin việc cũng là một nghề phụ tạm thời, họ càng bớt bị động.',
             'The sooner young people understand that job seeking is a temporary craft of its own, the less passive they become.'),
        ],
        'lesson_vn': 'Đừng chỉ học để làm việc. Hãy học cả cách bước vào một công việc. Cánh cửa cũng có kỹ năng riêng của nó.',
        'lesson_en': 'Do not only learn how to do the job. Learn how to enter the job. The door has its own skill too.',
    },
]

ch11 = [
    {
        'title_vn': 'Hết Động Lực Rồi Thì Còn Gì?',
        'title_en': 'What Remains When Motivation Is Gone?',
        'pairs': [
            ('Nhiều người trẻ bắt đầu rất mạnh khi còn hứng.',
             'Many young people start strongly while they still feel inspired.'),
            ('Nhưng hứng không phải nguồn nhiên liệu bền.',
             'But inspiration is not durable fuel.'),
            ('Đến ngày chán, mệt, bị từ chối, hay thấy chẳng có kết quả nào, người ta mới biết mình sống bằng gì.',
             'On days of boredom, exhaustion, rejection, or no visible results, people discover what truly keeps them moving.'),
            ('Ai chỉ sống bằng cảm xúc rất dễ bỏ dở đời mình.',
             'People who live only by emotion are very likely to abandon their own path.'),
        ],
        'lesson_vn': 'Động lực giúp em bắt đầu. Kỷ luật giúp em đi tiếp khi cảm xúc không còn muốn giúp nữa.',
        'lesson_en': 'Motivation helps you begin. Discipline helps you continue when emotion no longer wants to help.',
    },
    {
        'title_vn': 'Những Ngày Bình Thường Mới Quyết Định Đường Dài',
        'title_en': 'Ordinary Days Decide the Long Road',
        'pairs': [
            ('Đời người không được tạo chủ yếu từ những ngày bùng nổ.',
             'A life is not built mainly from explosive days.'),
            ('Nó được dựng lên từ những ngày bình thường, khi không ai nhìn, không ai khen, và em vẫn làm phần việc của mình.',
             'It is built from ordinary days, when no one watches, no one praises, and you still do your part.'),
            ('Kỷ luật vì thế trông chán nhưng rất đáng sợ theo nghĩa tốt.',
             'That is why discipline looks boring but is powerful in the best sense.'),
            ('Nó lấy những ngày không có gì đặc biệt và biến chúng thành nền móng.',
             'It takes days that feel unremarkable and turns them into foundation.'),
        ],
        'lesson_vn': 'Ai coi thường ngày bình thường thì thường không có đường dài mạnh. Chính những ngày đó đang âm thầm quyết định em là ai.',
        'lesson_en': 'Those who underestimate ordinary days rarely build a strong long road. Those days quietly decide who you become.',
    },
    {
        'title_vn': 'Kỷ Luật Không Cần Oai, Chỉ Cần Đều',
        'title_en': 'Discipline Does Not Need Drama, Only Consistency',
        'pairs': [
            ('Nhiều người hình dung kỷ luật là dậy từ rất sớm, làm rất nhiều, và sống rất căng.',
             'Many people imagine discipline as waking very early, doing a lot, and living under constant strain.'),
            ('Thực ra kỷ luật tốt thường ít ồn hơn thế.',
             'In reality, good discipline is usually quieter than that.'),
            ('Nó có thể chỉ là ngủ đúng giờ hơn, làm việc đúng khung hơn, bớt trì hoãn hơn, và quay lại nhanh hơn sau khi lệch nhịp.',
             'It may be sleeping on time, working in a stable schedule, delaying less, and returning faster after losing rhythm.'),
            ('Không cần hào hùng. Chỉ cần đều.',
             'It does not need heroics. It needs consistency.'),
        ],
        'lesson_vn': 'Người trẻ hay thua vì đòi kỷ luật thật đẹp rồi bỏ luôn. Hãy xây một kiểu kỷ luật sống được trước đã.',
        'lesson_en': 'Young people often fail because they demand a perfect form of discipline and then quit. Build a livable discipline first.',
    },
    {
        'title_vn': 'Khi Em Lệch Nhịp, Điều Quan Trọng Là Quay Lại Nhanh',
        'title_en': 'When You Lose Rhythm, Return Quickly',
        'pairs': [
            ('Không ai giữ được nhịp hoàn hảo mãi.',
             'No one keeps a perfect rhythm forever.'),
            ('Sẽ có ngày em lười, em trễ, em trượt lịch, em mất tập trung.',
             'There will be days when you are lazy, late, off schedule, or distracted.'),
            ('Người đi xa không phải người chưa từng lệch. Họ là người quay lại nhanh hơn sau khi lệch.',
             'People who go far are not those who never slip. They are those who return faster after slipping.'),
            ('Tự tha thứ vừa đủ và quay lại sớm tốt hơn nhiều so với tự ghét mình rồi bỏ luôn.',
             'A measured self-forgiveness followed by a quick return is much better than self-hatred followed by quitting.'),
        ],
        'lesson_vn': 'Kỷ luật bền không phải không sai. Nó là biết sai, sửa, và quay lại mà không diễn quá nhiều.',
        'lesson_en': 'Sustainable discipline is not the absence of mistakes. It is knowing, fixing, and returning without excessive drama.',
    },
    {
        'title_vn': 'Cứu Mình Bằng Nề Nếp Nhỏ',
        'title_en': 'Save Yourself with Small Routines',
        'pairs': [
            ('Có giai đoạn người trẻ không cần những tuyên ngôn lớn. Họ cần vài nề nếp nhỏ để không trượt thêm.',
             'There are periods when young people do not need grand slogans. They need a few small routines to stop sliding further.'),
            ('Ăn đúng bữa hơn, ngủ đúng hơn, tập nhẹ, đọc vài trang, làm một việc quan trọng trước khi mở mạng.',
             'Eat on time more often, sleep better, exercise lightly, read a few pages, do one important task before opening social media.'),
            ('Nghe rất nhỏ, nhưng nhiều lần chính những thứ nhỏ này giữ người ta khỏi đổ sập.',
             'These things sound small, but often they are what keep a person from collapse.'),
            ('Đời dài không chỉ được cứu bằng quyết tâm lớn. Nó còn được cứu bằng nề nếp nhỏ giữ mỗi ngày.',
             'A long life is not saved only by big determination. It is also saved by small routines that hold each day together.'),
        ],
        'lesson_vn': 'Khi đời rối, đừng coi thường những nề nếp nhỏ. Nhiều khi chúng là tay vịn đầu tiên để em bám lại.',
        'lesson_en': 'When life is messy, do not underestimate small routines. They are often the first railing you can hold onto.',
    },
]

ch12 = [
    {
        'title_vn': 'Trưởng Thành Là Bớt Đổ Lỗi',
        'title_en': 'Growing Up Means Blaming Less',
        'pairs': [
            ('Người trẻ có rất nhiều lý do thật để khó khăn: gia cảnh, nền tảng, môi trường, và cả bất công.',
             'Young people have many real reasons for difficulty: family background, limited support, environment, and unfairness.'),
            ('Nhưng nếu mọi chuyện trong đời đều được giải thích chỉ bằng lỗi của người khác, em sẽ mất dần quyền thay đổi phần của mình.',
             'But if everything in life is explained only by other people’s fault, you slowly lose the power to change your own part.'),
            ('Trưởng thành không phải phủ nhận khó khăn thật.',
             'Growing up does not mean denying real hardship.'),
            ('Nó là biết trong hoàn cảnh đó, phần nào là phần mình vẫn phải chịu trách nhiệm.',
             'It means knowing what part remains your responsibility within that hardship.'),
        ],
        'lesson_vn': 'Đổ lỗi đôi khi giúp em đỡ đau trong chốc lát. Chịu trách nhiệm mới giúp em đổi đời về lâu dài.',
        'lesson_en': 'Blame may reduce pain for a moment. Responsibility is what changes life over the long run.',
    },
    {
        'title_vn': 'Xin Lỗi Và Sửa Lỗi Là Hai Việc Khác Nhau',
        'title_en': 'Apologizing and Repairing Are Two Different Things',
        'pairs': [
            ('Có người xin lỗi rất hay nhưng vẫn lặp lại cùng một lỗi mãi.',
             'Some people apologize well but keep repeating the same mistake.'),
            ('Lời xin lỗi khi đó dần mất giá.',
             'Then the apology slowly loses value.'),
            ('Người trưởng thành không chỉ biết nhận sai bằng miệng. Họ sửa sai bằng cách đổi hành vi.',
             'A mature person does not only admit fault with words. They repair it by changing behavior.'),
            ('Nói đúng mà sống không đổi thì vẫn chưa đủ.',
             'Speaking correctly without changing life is still not enough.'),
        ],
        'lesson_vn': 'Muốn lớn thật, đừng chỉ học nói câu xin lỗi. Hãy học cả cách làm người khác thấy mình đã khác đi.',
        'lesson_en': 'To truly mature, do not only learn the words “I am sorry.” Learn how to let people see that you have changed.',
    },
    {
        'title_vn': 'Dọn Phần Bừa Bộn Mình Tạo Ra',
        'title_en': 'Clean Up the Mess You Create',
        'pairs': [
            ('Một dấu hiệu của trưởng thành là không bỏ lại hậu quả của mình cho người khác dọn mãi.',
             'One sign of maturity is not leaving your consequences for other people to clean forever.'),
            ('Đi trễ thì xin lỗi và sửa lịch. Làm hỏng việc thì nhận phần mình. Tiêu quá tay thì tự siết lại.',
             'If you are late, apologize and fix your schedule. If you damage work, own your part. If you overspend, tighten your own budget.'),
            ('Người lớn không được định nghĩa bằng tuổi. Họ được định nghĩa bằng khả năng dọn phần bừa bộn mình gây ra.',
             'Adults are not defined by age. They are defined by their ability to clean up the mess they create.'),
            ('Ai cứ muốn hưởng quyền mà né phần dọn dẹp thì mới chỉ lớn cái xác.',
             'Those who want rights but avoid cleanup have grown only in body.'),
        ],
        'lesson_vn': 'Chịu trách nhiệm không hào nhoáng, nhưng nó làm con người có trọng lượng hơn rất nhiều.',
        'lesson_en': 'Responsibility is not glamorous, but it gives a person much more weight and substance.',
    },
    {
        'title_vn': 'Không Còn Tuổi Để Chờ Ai Nhắc Mãi',
        'title_en': 'There Comes an Age When No One Should Keep Reminding You',
        'pairs': [
            ('Lớn lên rồi, có những việc em không thể chờ người khác nhắc mãi mới làm.',
             'As you grow older, there are tasks you cannot keep waiting to be reminded about.'),
            ('Đúng giờ, giữ lời, trả tiền, phản hồi, và chuẩn bị là những thứ dần phải thành phản xạ.',
             'Punctuality, keeping promises, paying what you owe, replying, and preparing must gradually become reflexes.'),
            ('Nếu cái gì cũng cần ai đó nhắc, em vẫn đang sống như người khác cầm tay mình đi.',
             'If everything still requires reminders, you are living as if someone else must hold your hand.'),
            ('Một phần trưởng thành là biến điều đúng thành thói quen, không phải biến nó thành bài giảng người khác phải lặp đi lặp lại.',
             'Part of maturity is turning what is right into habit, not into a lecture others must repeat forever.'),
        ],
        'lesson_vn': 'Tự nhắc được mình là bước rất quan trọng của trưởng thành. Người nào cũng chờ bị nhắc thì rất khó lớn thật.',
        'lesson_en': 'Being able to remind yourself is a major step in growing up. People who always wait to be reminded rarely mature deeply.',
    },
    {
        'title_vn': 'Sống Làm Sao Để Sau Này Khỏi Xấu Hổ Với Mình',
        'title_en': 'Live So That Future You Will Not Be Ashamed',
        'pairs': [
            ('Cuối cùng, trưởng thành không chỉ là kiếm được tiền hay sống riêng được.',
             'In the end, maturity is not only about earning money or living on your own.'),
            ('Nó còn là chuyện mỗi ngày em đang thành loại người nào.',
             'It is also about what kind of person you are becoming each day.'),
            ('Có người lớn lên về tuổi nhưng nhỏ đi về nhân cách.',
             'Some people grow older in age while shrinking in character.'),
            ('Có người đi chậm, còn vụng, còn nghèo, nhưng mỗi năm lại đáng tin hơn và đàng hoàng hơn.',
             'Some move slowly, remain clumsy, remain poor, yet each year become more trustworthy and decent.'),
        ],
        'lesson_vn': 'Đích của trưởng thành không phải chỉ là sống sót. Nó là sống sao để không phải cúi mặt trước chính mình.',
        'lesson_en': 'The goal of adulthood is not only survival. It is living in a way that does not make you lower your eyes before yourself.',
    },
]

print("Đang tạo chương 9-12...")
make_chapter('ch09-tu-te-nhung-dung-de-bi-dung', 'Tử Tế Nhưng Đừng Dễ Bị Dùng', 'Be Kind, But Do Not Be Easily Used', ch09)
make_chapter('ch10-gioi-khong-dong-nghia-co-viec', 'Giỏi Không Đồng Nghĩa Với Kiếm Được Việc', 'Being Good Does Not Automatically Get You a Job', ch10)
make_chapter('ch11-ky-luat-cuu-nguoi', 'Kỷ Luật Cứu Người Khi Hết Động Lực', 'Discipline Saves You When Motivation Is Gone', ch11)
make_chapter('ch12-truong-thanh-la-chiu-trach-nhiem', 'Trưởng Thành Là Bớt Đổ Lỗi, Tăng Chịu Trách Nhiệm', 'Maturity Means Less Blame and More Responsibility', ch12)
print("Hoàn tất chương 9-12!")
