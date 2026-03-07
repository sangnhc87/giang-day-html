#!/usr/bin/env python3
# gen_q8_a.py -- Quyển VIII ch01-04: Điểm số, áp lực gia đình, so sánh, thất bại
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


ch01 = [
    {
        'title_vn': 'Điểm Cao Không Tự Động Biến Em Thành Người Giỏi',
        'title_en': 'High Scores Do Not Automatically Make You Capable',
        'pairs': [
            ('Minh luôn đứng nhất lớp. Bảng điểm của em gần như không có số nào dưới chín.',
             'Minh was always first in class. His report card almost never showed a score below nine.'),
            ('Nhưng mỗi khi thầy hỏi thêm một câu ngoài sách giáo khoa, Minh đứng im. Em biết đáp án mẫu, nhưng không biết nghĩ tiếp.',
             'But whenever the teacher asked one extra question beyond the textbook, Minh froze. He knew the model answer, but did not know how to think beyond it.'),
            ('Đến khi thi học sinh giỏi, đề không hỏi học thuộc. Đề bắt phải hiểu. Minh làm bài như người đi trên chiếc cầu đã mất bản đồ.',
             'When the gifted-student exam came, the questions did not reward memorization. They demanded understanding. Minh wrote like someone walking on a bridge after losing the map.'),
            ('Điểm số từng giúp em được khen. Nhưng chính điểm số cũng che giấu lỗ hổng lớn nhất: em học để đúng, không học để hiểu.',
             'Scores once brought him praise. But they also hid the largest gap: he studied to be correct, not to understand.'),
            ('Thầy giáo nói thẳng với cả lớp: "Điểm cao là tín hiệu tốt, nhưng không phải bằng chứng cuối cùng của năng lực. Năng lực lộ ra khi em gặp câu chưa từng thấy."',
             'The teacher told the class plainly: "High scores are a good signal, but not the final proof of competence. Competence shows when you face a question you have never seen before."'),
        ],
        'lesson_vn': 'Đừng dùng điểm số để ru ngủ mình. Hãy tự hỏi: ngoài bài kiểm tra, mình giải thích lại được không, ứng dụng được không, và tự học tiếp được không?',
        'lesson_en': 'Do not let scores lull you to sleep. Ask instead: beyond the test, can I explain it, apply it, and continue learning on my own?',
    },
    {
        'title_vn': 'Điểm Thấp Không Có Nghĩa Em Vô Dụng',
        'title_en': 'Low Scores Do Not Mean You Are Worthless',
        'pairs': [
            ('Lan bị điểm bốn môn Toán. Em giấu bài kiểm tra xuống đáy cặp như giấu một vết thương.',
             'Lan got a four in mathematics. She hid the test at the bottom of her bag as if hiding a wound.'),
            ('Tối đó em nói: "Con ngu thật." Mẹ em không mắng, chỉ hỏi: "Bài nào con sai vì không biết, bài nào con sai vì cẩu thả?"',
             'That evening she said: "I am stupid." Her mother did not scold her, but asked: "Which mistakes came from not knowing, and which came from carelessness?"'),
            ('Hai mẹ con ngồi tách từng lỗi ra. Hóa ra ba câu sai vì quên đổi đơn vị, hai câu sai vì đọc thiếu dữ kiện, chỉ một câu là thực sự không hiểu.',
             'Together they separated each mistake. It turned out three errors came from forgetting units, two from misreading the problem, and only one from truly not understanding.'),
            ('Điểm bốn vẫn là điểm bốn. Nhưng từ chỗ thấy mình kém cỏi toàn bộ, Lan bắt đầu nhìn ra một sự thật công bằng hơn: mình sai ở đâu thì sửa ở đó.',
             'A four was still a four. But instead of seeing herself as entirely inadequate, Lan began to see a fairer truth: fix the specific place where you are wrong.'),
            ('Một tháng sau, Lan được bảy điểm. Không phải phép màu. Chỉ là em thôi chửi bản thân và bắt đầu sửa lỗi thật.',
             'A month later, Lan scored seven. It was not magic. She had simply stopped insulting herself and started correcting real errors.'),
        ],
        'lesson_vn': 'Điểm thấp là dữ liệu, không phải bản án. Người tiến bộ không phải người chưa từng sai, mà là người chịu nhìn thẳng lỗi sai mà không tự hủy mình.',
        'lesson_en': 'A low score is data, not a verdict. The person who improves is not the one who never errs, but the one who can face mistakes without destroying self-respect.',
    },
    {
        'title_vn': 'Có Những Đứa Trẻ Giỏi Vì Sợ',
        'title_en': 'Some Children Perform Well Because They Are Afraid',
        'pairs': [
            ('Vy học ngày học đêm. Ai nhìn vào cũng nghĩ em có ý chí thép.',
             'Vy studied day and night. Anyone watching thought she had iron discipline.'),
            ('Chỉ có em biết thứ kéo mình chạy không phải đam mê, mà là sợ hãi. Em sợ thua bạn, sợ bố thất vọng, sợ mình không còn giá trị nếu không đứng đầu.',
             'Only she knew that what drove her was not passion, but fear. She feared losing to classmates, feared disappointing her father, feared becoming worthless if she was not first.'),
            ('Thành tích của em tăng, nhưng giấc ngủ của em giảm. Nét mặt em căng như dây đàn. Một đứa trẻ được gọi là giỏi, nhưng sống như đang chạy trốn.',
             'Her achievements rose, but her sleep shrank. Her face stayed tight like a string. She was called gifted, yet lived as if fleeing something.'),
            ('Cô chủ nhiệm nói riêng với em: "Nếu thứ giữ em học là nỗi sợ, rồi sẽ đến lúc em ghét luôn cả việc học. Không ai chạy mãi bằng hoảng loạn được."',
             'Her homeroom teacher told her privately: "If fear is what keeps you studying, one day you will hate learning itself. No one can run forever on panic."'),
            ('Vy bắt đầu nghỉ đúng giờ hơn, chừa một buổi tối không học thêm, và tập trả lời câu hỏi khó nhất: nếu không đứng nhất, mình còn là ai?',
             'Vy began ending study at a fixed hour, keeping one evening free from extra classes, and practicing the hardest question: if I am not first, who am I still?'),
        ],
        'lesson_vn': 'Kết quả tốt đạt được bằng hoảng loạn không bền. Hãy xây động lực từ ý nghĩa, sự tò mò và lòng tự trọng, không phải từ nỗi sợ bị bỏ rơi hay bị so sánh.',
        'lesson_en': 'Results achieved through panic do not last. Build motivation from meaning, curiosity, and self-respect, not from fear of abandonment or comparison.',
    },
    {
        'title_vn': 'Câu Hỏi Quan Trọng Hơn Điểm Số',
        'title_en': 'The Questions Matter More Than the Score',
        'pairs': [
            ('Một thầy giáo mới vào lớp và viết lên bảng: "Em muốn trở thành kiểu người như thế nào?"',
             'A new teacher entered the class and wrote on the board: "What kind of person do you want to become?"'),
            ('Cả lớp ngơ ngác. Họ quen với những câu hỏi như công thức nào, định lý nào, tác giả nào. Không ai quen bị hỏi về chính mình.',
             'The class stared blankly. They were used to questions like which formula, which theorem, which author. No one was used to being asked about themselves.'),
            ('Thầy nói: "Nếu em chỉ hỏi làm sao được chín, mười, em sẽ trở thành cỗ máy săn điểm. Nếu em hỏi làm sao hiểu sâu hơn, sống tử tế hơn, làm việc chắc hơn, em mới đang học thật."',
             'The teacher said: "If you only ask how to get nines and tens, you will become a score-hunting machine. If you ask how to understand more deeply, live more decently, and work more solidly, then you are truly learning."'),
            ('Buổi học hôm đó không có nhiều bài tập. Nhưng nhiều học sinh về nhà với một cảm giác lạ: lần đầu tiên việc học được nối với cuộc đời thật.',
             'There were not many exercises that day. But many students went home with a strange feeling: for the first time, study had been connected to real life.'),
        ],
        'lesson_vn': 'Điểm số quan trọng, nhưng câu hỏi em mang theo suốt đời còn quan trọng hơn. Học để thành người, rồi mới học để thắng bài kiểm tra.',
        'lesson_en': 'Scores matter, but the questions you carry for life matter more. Study first to become a person, then to beat a test.',
    },
]

ch02 = [
    {
        'title_vn': 'Áp Lực Mang Tên Yêu Thương',
        'title_en': 'Pressure That Arrives in the Name of Love',
        'pairs': [
            ('Nam nghe câu này suốt ba năm cấp ba: "Bố mẹ làm tất cả cũng vì con."',
             'Nam heard this sentence throughout high school: "We do everything for you."'),
            ('Câu đó đúng một nửa. Nửa còn lại là mọi kỳ vọng, mọi lịch học kín đặc, mọi so sánh ngầm cũng được gói trong chữ yêu.',
             'That sentence was half true. The other half was that every expectation, every overloaded schedule, every quiet comparison was also wrapped inside the language of love.'),
            ('Nam không dám than mệt vì sợ bị gọi là vô ơn. Em không dám nói không thích ngành bố chọn vì sợ làm mẹ buồn.',
             'Nam did not dare complain of exhaustion because he feared being called ungrateful. He did not dare say he disliked the major his father chose because he feared hurting his mother.'),
            ('Một tối, em bật khóc và nói: "Con biết bố mẹ thương con. Nhưng nếu con chỉ được quyền làm người bố mẹ tự hào, còn con người thật của con thì sao?"',
             'One night he cried and said: "I know you love me. But if I only get to be the child you are proud of, what happens to the real me?"'),
            ('Căn phòng im lặng rất lâu. Đó là im lặng khó chịu, nhưng cần thiết. Có những gia đình chỉ bắt đầu chữa lành từ lúc một đứa trẻ dám nói thật.',
             'The room stayed silent for a long time. It was an uncomfortable silence, but a necessary one. Some families only begin healing when a child dares to tell the truth.'),
        ],
        'lesson_vn': 'Tình thương không nên biến thành chiếc lồng mạ vàng. Cha mẹ cần định hướng, nhưng cũng phải chừa chỗ cho tiếng nói thật của con.',
        'lesson_en': 'Love should not become a golden cage. Parents should guide, but must leave room for the child’s real voice.',
    },
    {
        'title_vn': 'So Với Con Nhà Người Ta Là Cách Giết Tự Tin Nhanh Nhất',
        'title_en': 'Comparing You to Other People’s Children Destroys Confidence Fastest',
        'pairs': [
            ('Mỗi lần Huy được tám điểm, bố hỏi: "Sao không được mười như bạn An?"',
             'Every time Huy scored an eight, his father asked: "Why not ten like An?"'),
            ('Mỗi lần Huy đá bóng giỏi, mẹ bảo: "Giỏi cái đó để làm gì? Con nhìn con người ta học đi."',
             'Whenever Huy played football well, his mother said: "What is the use of that? Look at how other people’s children study."'),
            ('Lâu dần, Huy không còn nghe lời góp ý. Em chỉ nghe thấy một thông điệp duy nhất: mình không bao giờ đủ.',
             'Over time, Huy no longer heard advice. He heard only one message: I am never enough.'),
            ('Người lớn thường tưởng so sánh sẽ tạo động lực. Thực tế, so sánh kéo học sinh vào một cuộc đua mà đích đến luôn nằm ở người khác.',
             'Adults often think comparison creates motivation. In reality, comparison drags students into a race whose finish line is always inside someone else.'),
            ('Khi một đứa trẻ mất cảm giác mình có giá trị riêng, nó hoặc lì ra, hoặc phát điên vì chứng minh, hoặc âm thầm ghét chính gia đình mình.',
             'When a child loses the sense of having unique worth, that child either goes numb, goes obsessive, or quietly grows to resent the family.'),
        ],
        'lesson_vn': 'So sánh có thể tạo áp lực ngắn hạn, nhưng làm hỏng gốc rễ lâu dài. Hãy đo sự tiến bộ của một học sinh bằng chính đường đi của em ấy, không phải bằng con nhà người ta.',
        'lesson_en': 'Comparison may create short-term pressure, but it damages the roots long-term. Measure a student’s growth against that student’s own path, not somebody else’s child.',
    },
    {
        'title_vn': 'Đứa Con Ngoan Không Phải Lúc Nào Cũng Ổn',
        'title_en': 'The Good Child Is Not Always Fine',
        'pairs': [
            ('Có những đứa trẻ không cãi, không phá, không gây rắc rối. Người lớn rất thích kiểu con như vậy.',
             'There are children who do not argue, do not rebel, and do not cause trouble. Adults love that kind of child.'),
            ('Nhưng đôi khi sự ngoan đó không phải trưởng thành. Nó là kết quả của việc sợ làm ai đó thất vọng.',
             'But sometimes that obedience is not maturity. It is the result of being terrified of disappointing someone.'),
            ('Thu luôn nói: "Dạ, sao cũng được." Em hiếm khi xin thứ mình muốn, hiếm khi phản đối điều mình không thích.',
             'Thu always said: "Yes, whatever you think." She rarely asked for what she wanted, and rarely objected to what she disliked.'),
            ('Đến khi vào đại học, không ai quản lịch nữa, em sụp hoàn toàn. Em không biết mình thích gì, giỏi gì, chọn gì, vì cả tuổi học sinh chỉ quen làm theo.',
             'When she entered university and no one managed her schedule anymore, she collapsed. She did not know what she liked, what she was good at, or what to choose, because her student years had trained her only to obey.'),
            ('Một đứa trẻ quá ngoan đôi khi không cần thêm lời khen. Nó cần được hỏi: "Con thực sự nghĩ gì?"',
             'An overly obedient child sometimes does not need more praise. That child needs to be asked: "What do you really think?"'),
        ],
        'lesson_vn': 'Giáo dục không phải đào tạo ra người chỉ biết nghe lời. Giáo dục tốt phải giúp học sinh biết suy nghĩ, biết phản biện, và biết chịu trách nhiệm cho lựa chọn của mình.',
        'lesson_en': 'Education is not the training of compliant people. Good education should help students think, disagree respectfully, and own their choices.',
    },
    {
        'title_vn': 'Nói Chuyện Thật Với Cha Mẹ Là Một Kỹ Năng',
        'title_en': 'Speaking Honestly With Parents Is a Skill',
        'pairs': [
            ('Không phải học sinh nào cũng có cha mẹ dễ nói chuyện. Có nhà vừa mở lời đã thành cãi nhau.',
             'Not every student has parents who are easy to talk to. In some homes, every conversation turns into conflict.'),
            ('Nhưng im lặng mãi cũng không giải quyết được. Có những điều chỉ thay đổi khi con cái học cách nói rõ, bình tĩnh, và có dẫn chứng.',
             'But silence solves nothing either. Some things change only when children learn to speak clearly, calmly, and with evidence.'),
            ('Mai viết ra giấy ba điều: con đang mệt vì lịch học thêm nào, con muốn giảm gì, và con sẽ bù bằng cách nào.',
             'Mai wrote down three things: which extra classes were exhausting her, what she wanted reduced, and how she would make up for it.'),
            ('Khi nói với mẹ, em không dùng câu trách móc như "Mẹ ép con". Em nói: "Con đang quá tải. Nếu giữ lịch này, con học tệ hơn chứ không tốt hơn."',
             'When she spoke to her mother, she did not use accusing lines like "You force me." She said: "I am overloaded. If this schedule stays, I will study worse, not better."'),
            ('Cuộc nói chuyện không hoàn hảo, nhưng đủ để mẹ em lùi một bước. Người lớn không phải lúc nào cũng thay đổi vì cảm xúc. Nhiều khi họ thay đổi vì cuối cùng cũng nghe được sự thật rõ ràng.',
             'The conversation was not perfect, but enough for her mother to step back. Adults do not always change because of emotion. Often they change because they finally hear the truth stated clearly.'),
        ],
        'lesson_vn': 'Muốn được lắng nghe, học sinh cũng phải học cách nói có cấu trúc, không chỉ bùng nổ. Sự thật nói đúng cách có sức nặng hơn tiếng cãi vã.',
        'lesson_en': 'If you want to be heard, you must learn to speak with structure, not only with explosion. Truth said properly carries more weight than shouting.',
    },
]

ch03 = [
    {
        'title_vn': 'Người Ta Chỉ Cho Em Thấy Thành Tích, Không Cho Em Thấy Cái Giá',
        'title_en': 'People Show You the Achievement, Not the Price',
        'pairs': [
            ('Trên mạng, An thấy bạn bè khoe giấy khen, huy chương, ảnh học bổng, ảnh trường top.',
             'Online, An saw friends posting certificates, medals, scholarships, and top-school photos.'),
            ('Không ai đăng ảnh những đêm mất ngủ, những lần khóc trong nhà vệ sinh, hay những cơn hoảng loạn trước kỳ thi.',
             'No one posted the sleepless nights, the crying in the bathroom, or the panic attacks before exams.'),
            ('Khi chỉ nhìn thấy phần sáng, An tưởng ai cũng đang tiến lên còn mình thì tụt lại.',
             'Seeing only the bright part, An believed everyone else was moving forward while she alone was falling behind.'),
            ('Cô tư vấn học đường nói: "Con đang so hậu trường của mình với sân khấu của người khác. Cuộc so đó chắc chắn khiến con thua."',
             'The school counselor said: "You are comparing your backstage to everyone else’s stage. That comparison guarantees defeat."'),
        ],
        'lesson_vn': 'Khi ganh tị, hãy nhớ: em gần như không bao giờ nhìn thấy toàn bộ câu chuyện của người khác. So sánh từ dữ liệu méo thì kết luận cũng méo.',
        'lesson_en': 'When envy rises, remember: you almost never see the whole story of other people. If the data is distorted, the conclusion will be distorted too.',
    },
    {
        'title_vn': 'Ghen Tị Không Làm Em Xấu, Nhưng Che Nó Đi Thì Nguy',
        'title_en': 'Envy Does Not Make You Evil, But Hiding It Is Dangerous',
        'pairs': [
            ('Khi bạn cùng lớp đỗ đội tuyển, Phúc cười chúc mừng nhưng trong lòng nóng ran.',
             'When his classmate got into the elite team, Phuc smiled and congratulated him, but burned inside.'),
            ('Em ghét cảm giác đó nên cố giả như mình không quan tâm. Nhưng càng giả, em càng cay cú hơn.',
             'He hated the feeling, so he pretended not to care. The more he pretended, the more bitter he became.'),
            ('Một người thầy nói với em: "Ghen tị chỉ là tín hiệu cho thấy con đang muốn một thứ mình chưa có. Vấn đề không phải cảm xúc đó. Vấn đề là con làm gì sau đó."',
             'A teacher told him: "Envy is only a signal that you want something you do not yet have. The problem is not the emotion. The problem is what you do after it."'),
            ('Phúc bắt đầu đổi câu hỏi từ "Sao nó có mà mình không có?" sang "Nó làm được gì mà mình chưa làm?"',
             'Phuc began changing the question from "Why does he have it and I do not?" to "What did he do that I have not yet done?"'),
        ],
        'lesson_vn': 'Ghen tị được soi sáng sẽ thành động lực. Ghen tị bị giấu đi sẽ thành độc. Đừng tô hồng cảm xúc của mình; hãy đọc đúng nó.',
        'lesson_en': 'Envy examined becomes motivation. Envy hidden becomes poison. Do not beautify your emotions; read them accurately.',
    },
    {
        'title_vn': 'Tự Ti Không Phải Khiêm Tốn',
        'title_en': 'Low Self-Worth Is Not Humility',
        'pairs': [
            ('Nhiều học sinh nói câu này như một thói quen: "Em dốt lắm, em không làm được đâu."',
             'Many students say this habitually: "I am dumb. I cannot do it."'),
            ('Các em tưởng đó là khiêm tốn. Thực ra đó là cách đầu hàng trước khi thử thật.',
             'They think it is humility. In reality it is surrender before trying seriously.'),
            ('Khi một người tự gắn nhãn thấp cho mình, não sẽ bớt nỗ lực vì nó tin thất bại là điều đã định sẵn.',
             'When someone attaches a low label to the self, the brain reduces effort because failure seems already predetermined.'),
            ('Khiêm tốn thật không phải nói mình tệ. Khiêm tốn thật là biết mình chưa đủ và vẫn chịu học tiếp.',
             'Real humility is not saying you are bad. Real humility is knowing you are not enough yet and still being willing to continue learning.'),
        ],
        'lesson_vn': 'Bỏ kiểu nói hạ nhục bản thân để tỏ ra an toàn. Hãy thay bằng câu trung thực hơn: "Em chưa làm được, nhưng em có thể học."',
        'lesson_en': 'Drop the self-insulting language used as a shield. Replace it with a more truthful sentence: "I cannot do it yet, but I can learn."',
    },
    {
        'title_vn': 'Đường Của Em Không Cần Giống Đường Của Bạn',
        'title_en': 'Your Path Does Not Need to Match Your Friend’s Path',
        'pairs': [
            ('Hai người bạn thân học chung từ nhỏ. Một người rất mạnh về Toán, người còn lại mạnh về Văn và giao tiếp.',
             'Two close friends studied together from childhood. One was strong in mathematics, the other in literature and communication.'),
            ('Đến lớp mười hai, cả hai đều cố chen vào cùng một lối vì sợ đi khác sẽ bị coi là kém hơn.',
             'By twelfth grade, both tried to squeeze into the same path because they feared that different meant inferior.'),
            ('Kết quả là cả hai đều khổ. Người giỏi Văn học Toán trong lo âu. Người giỏi Toán đi thi hùng biện như bị phạt.',
             'The result was that both suffered. The literature student studied math anxiously. The math student competed in speaking as if under punishment.'),
            ('Chỉ khi dám thừa nhận sở trường khác nhau, họ mới ngừng đánh nhau với chính thiết kế của mình.',
             'Only when they dared admit different strengths did they stop fighting their own design.'),
        ],
        'lesson_vn': 'So sánh khiến học sinh coi khác biệt là thua kém. Nhưng khác biệt nhiều khi chỉ là dấu hiệu em nên đi con đường khác, không phải thấp hơn.',
        'lesson_en': 'Comparison makes students treat difference as inferiority. But often difference is only a sign that you should take a different path, not a lower one.',
    },
]

ch04 = [
    {
        'title_vn': 'Rớt Một Kỳ Thi Không Có Nghĩa Cuộc Đời Em Rớt Theo',
        'title_en': 'Failing One Exam Does Not Mean Failing Your Life',
        'pairs': [
            ('Khi trượt nguyện vọng đầu, Quân đóng cửa phòng suốt hai ngày.',
             'When he missed his first-choice admission, Quan shut himself in his room for two days.'),
            ('Em nghĩ mọi thứ kết thúc rồi. Bao nhiêu năm học như đổ xuống sông.',
             'He thought everything was over. Years of study seemed thrown away.'),
            ('Người lớn quanh em cũng nói kiểu như tận thế: "Thế là hỏng." Chính những câu đó làm nỗi đau của học sinh phình to hơn sự thật.',
             'The adults around him spoke as if it were the apocalypse: "It is ruined." Those sentences made the student’s pain swell larger than reality.'),
            ('Một cậu anh họ kéo Quân đi uống nước và nói thẳng: "Em vừa rớt một cánh cửa, không phải rớt cả cuộc đời. Đừng thần thánh hóa một kỳ thi đến mức để nó quyết định giá trị của em."',
             'An older cousin took Quan out for a drink and said plainly: "You missed one door, not your entire life. Do not worship a single exam so much that it gets to define your worth."'),
        ],
        'lesson_vn': 'Thi cử quan trọng, nhưng không đủ quyền để định nghĩa một con người. Sau thất bại, việc đầu tiên là kéo sự việc về đúng kích cỡ thật của nó.',
        'lesson_en': 'Exams matter, but they do not have the authority to define a human being. After failure, the first job is to resize the event back to its true scale.',
    },
    {
        'title_vn': 'Xấu Hổ Là Một Nỗi Đau Thật, Nhưng Không Phải La Bàn',
        'title_en': 'Shame Is Real Pain, But Not a Compass',
        'pairs': [
            ('Nhiều học sinh không sợ điểm thấp bằng sợ bị nhìn thấy điểm thấp.',
             'Many students fear being seen with a low score more than the score itself.'),
            ('Họ sợ ánh mắt bạn bè, giọng họ hàng, câu hỏi hàng xóm, và cả sự im lặng thất vọng trong bữa cơm.',
             'They fear classmates’ eyes, relatives’ voices, neighbors’ questions, and the disappointed silence at dinner.'),
            ('Xấu hổ làm người ta muốn trốn. Nhưng trốn thì không sửa được gì. La bàn của em phải là sự thật và kế hoạch, không phải ánh mắt thiên hạ.',
             'Shame makes people want to hide. But hiding repairs nothing. Your compass must be truth and planning, not the eyes of the crowd.'),
            ('Một học sinh can đảm nhất không phải người không biết xấu hổ. Đó là người dám ngồi lại với sự xấu hổ và vẫn tiếp tục làm việc cần làm.',
             'The bravest student is not the one who feels no shame. It is the one who can sit with shame and still do the work that must be done.'),
        ],
        'lesson_vn': 'Đừng để xấu hổ lái đời em. Cảm xúc đó cần được thừa nhận, nhưng không được giao tay lái.',
        'lesson_en': 'Do not let shame drive your life. That emotion should be acknowledged, but never handed the steering wheel.',
    },
    {
        'title_vn': 'Sau Vấp Ngã, Việc Đầu Tiên Không Phải Là Cố Tỏ Ra Mạnh',
        'title_en': 'After a Fall, the First Task Is Not to Pretend to Be Strong',
        'pairs': [
            ('Có những học sinh vừa thi trượt xong đã đăng trạng thái kiểu: "Không sao cả."',
             'Some students fail an exam and instantly post: "It is fine."'),
            ('Có thể họ thật sự ổn. Nhưng nhiều trường hợp chỉ là đang cố diễn mạnh mẽ để khỏi bị thương hại.',
             'Maybe they truly are fine. But often it is only a performance of strength to avoid pity.'),
            ('Sự thật là có những thất bại đau. Và đau thì phải thừa nhận là đau. Bỏ qua bước đó, em chỉ đang chôn cảm xúc xuống đất chứ không vượt qua nó.',
             'The truth is that some failures hurt. And pain should be admitted as pain. If you skip that step, you are burying emotion, not overcoming it.'),
            ('Khóc một trận, nghỉ một ngày, nói chuyện với người tin được, rồi quay lại bàn học. Đó không phải yếu đuối. Đó là phục hồi đúng cách.',
             'Cry once, rest a day, speak to someone trustworthy, then return to the desk. That is not weakness. That is recovery done properly.'),
        ],
        'lesson_vn': 'Muốn đứng dậy thật, trước hết phải cho phép mình bị đau thật. Chỉ những thứ được nhìn nhận mới được chữa lành.',
        'lesson_en': 'To stand up for real, you must first permit yourself to hurt for real. Only what is acknowledged can be healed.',
    },
    {
        'title_vn': 'Người Bản Lĩnh Không Phải Người Không Thất Bại',
        'title_en': 'A Strong Person Is Not One Who Never Fails',
        'pairs': [
            ('Trường học thường khen người thắng. Nhưng đời thật cuối cùng lại tôn trọng người biết trở lại sau khi thua.',
             'Schools often praise winners. Real life, however, ultimately respects those who know how to return after losing.'),
            ('Một học sinh từng trượt đại học năm đầu, đi làm thêm, học lại, rồi năm sau đỗ vào trường phù hợp hơn.',
             'One student failed university admission the first year, worked part-time, studied again, and the next year entered a school that suited him better.'),
            ('Nếu chỉ nhìn một lát cắt, ai cũng bảo em đó thất bại. Nhưng nếu nhìn dài hơn, người ta sẽ thấy em đang học một kỹ năng đắt giá hơn điểm số: khả năng hồi phục.',
             'If you look at one slice of time, everyone calls that student a failure. If you look longer, you see a far more valuable skill than a score: recovery.'),
            ('Đời người dài. Một cú ngã đau không đáng sợ bằng thói quen ngã xong nằm luôn.',
             'Life is long. One painful fall is less dangerous than the habit of staying down forever.'),
        ],
        'lesson_vn': 'Hãy dạy học sinh không chỉ cách thắng, mà còn cách thua cho đàng hoàng và đứng dậy cho tử tế. Đó mới là bản lĩnh đi đường dài.',
        'lesson_en': 'Teach students not only how to win, but how to lose with dignity and rise with discipline. That is long-distance strength.',
    },
]

ch01.extend([
    {
        'title_vn': 'Sĩ Tử Đèn Dầu Và Cái Đầu Rỗng',
        'title_en': 'The Lamp-Lit Candidate With an Empty Head',
        'pairs': [
            ('Ngày xưa có một sĩ tử nổi tiếng chăm chỉ. Đêm nào trong làng người ta cũng thấy ánh đèn dầu nhà cậu sáng tới khuya.',
             'Long ago there was a candidate famous for diligence. Every night the villagers saw his oil lamp burning late.'),
            ('Ai cũng tin cậu sẽ đỗ cao. Nhưng vào trường thi, đề hỏi một ý lạ hơn sách cũ một chút là cậu lúng túng ngay.',
             'Everyone believed he would rank highly. But in the examination hall, the moment the question moved slightly beyond the standard text, he was lost.'),
            ('Thầy đồ già nói: "Con đốt nhiều dầu thật, nhưng chưa chắc đã soi sáng đầu mình. Học mà chỉ nhét chữ thì đầu nặng chứ não chưa mở."',
             'The old teacher said, "You have burned much oil, but not necessarily lit up your mind. If study is only stuffing words in, the head becomes heavy while the mind stays shut."'),
            ('Từ đó cậu đổi cách học: bớt chép, tăng hỏi, tăng giải thích lại bằng lời của mình. Năm sau cậu mới thi đỗ thật.',
             'From then on he changed his method: less copying, more questioning, more explaining in his own words. Only the next year did he truly pass.'),
        ],
        'lesson_vn': 'Thời nào cũng vậy, học nhiều giờ không đồng nghĩa học sâu. Đừng nhầm số giờ với chất lượng tư duy.',
        'lesson_en': 'In every era, studying for many hours does not equal studying deeply. Do not confuse the number of hours with the quality of thought.',
    },
    {
        'title_vn': 'Học Tủ Là Một Canh Bạc',
        'title_en': 'Selective Studying Is a Gamble',
        'pairs': [
            ('Tùng nghe anh khóa trên mách rằng đề năm nào cũng quanh quẩn vài dạng. Em bỏ hẳn mấy phần khó và chỉ học đúng những gì mình tin sẽ ra.',
             'Tung heard older students say that the exam always repeated a few patterns. He dropped the hard parts and studied only what he believed would appear.'),
            ('Tuần trước khi thi, em còn rất tự tin vì làm đề đoán khá trúng.',
             'A week before the exam, he was confident because the predicted papers fit him well.'),
            ('Đến hôm thi thật, đề đổi hướng. Tùng ngồi nhìn giấy như nhìn một người lạ.',
             'On the real exam day, the paper shifted direction. Tung stared at it as if at a stranger.'),
            ('Em không trượt vì kém thông minh. Em trượt vì đã biến việc học thành trò đặt cược.',
             'He did not fail because he lacked intelligence. He failed because he had turned learning into a betting game.'),
        ],
        'lesson_vn': 'Học tủ có thể thắng một lần, nhưng rất khó nuôi năng lực thật. Điều em cần là nền rộng đủ để không sập khi đề đổi.',
        'lesson_en': 'Selective studying may win once, but it rarely builds real ability. What you need is a foundation wide enough not to collapse when the exam changes.',
    },
    {
        'title_vn': 'Cô Bé Bán Hàng Tính Nhanh Hơn Học Sinh Giỏi',
        'title_en': 'The Shop Girl Who Calculated Faster Than the Top Student',
        'pairs': [
            ('Ở chợ, một cô bé phụ mẹ bán rau tính tiền rất nhanh. Khách vừa gọi ba món là em đã nhẩm ra số tiền và tiền thối gần như ngay lập tức.',
             'At the market, a girl helping her mother sell vegetables calculated very quickly. The moment customers named three items, she almost instantly knew the total and the change.'),
            ('Một học sinh giỏi Toán đi ngang qua ngạc nhiên. Em ấy giải phương trình tốt hơn nhiều, nhưng gặp tình huống thật lại chậm hơn cô bé bán hàng.',
             'A top mathematics student passing by was surprised. He could solve equations far better, but in real situations he was slower than the girl at the stall.'),
            ('Người mẹ cười: "Mỗi người giỏi một kiểu. Học trong trường là một chuyện, dùng được ngoài đời là chuyện khác nữa."',
             'The mother laughed: "People are good in different ways. Learning in school is one thing; using it in life is another."'),
            ('Cậu học sinh nghe xong thấy xấu hổ theo nghĩa tốt. Lần đầu tiên em hiểu rằng kiến thức không đi ra được đời thì vẫn còn thiếu một đoạn đường.',
             'The boy felt a useful kind of embarrassment. For the first time he understood that knowledge which cannot step into life is still incomplete.'),
        ],
        'lesson_vn': 'Trường học không phải toàn bộ năng lực con người. Điểm cao đáng quý, nhưng khả năng làm được việc thật cũng đáng quý không kém.',
        'lesson_en': 'School is not the whole of human ability. High scores are valuable, but the ability to do real things is equally valuable.',
    },
    {
        'title_vn': 'Bài Kiểm Tra Mở Sách',
        'title_en': 'The Open-Book Test',
        'pairs': [
            ('Một cô giáo bất ngờ cho lớp làm bài kiểm tra mở sách. Cả lớp mừng vì tưởng sẽ dễ.',
             'A teacher surprised the class with an open-book test. Everyone was happy because they thought it would be easy.'),
            ('Nhưng khi nhận đề, nhiều em hoảng hơn bình thường. Sách ở đó, nhưng câu hỏi buộc phải biết nối ý, so sánh, và tự kết luận.',
             'But when they received the paper, many were more panicked than usual. The book was there, but the questions required connecting ideas, comparing, and drawing conclusions.'),
            ('Cô giáo nói: "Thi đóng sách kiểm tra trí nhớ. Thi mở sách kiểm tra đầu óc các em dùng trí nhớ vào việc gì."',
             'The teacher said, "A closed-book test checks memory. An open-book test checks what your mind does with memory."'),
            ('Buổi đó nhiều học sinh hiểu ra thứ mình còn yếu nhất không phải nhớ ít, mà là nghĩ ít.',
             'That day many students realized their greatest weakness was not remembering too little, but thinking too little.'),
        ],
        'lesson_vn': 'Đừng chỉ luyện nhớ. Hãy luyện kết nối, lập luận và giải thích. Đó mới là phần khó bị thay thế nhất.',
        'lesson_en': 'Do not train memory alone. Train connection, reasoning, and explanation. Those are the parts hardest to replace.',
    },
    {
        'title_vn': 'Khi Điểm Mười Là Mục Tiêu Duy Nhất',
        'title_en': 'When a Perfect Score Becomes the Only Goal',
        'pairs': [
            ('Có học sinh làm bài được chín rưỡi nhưng chỉ chăm chăm hỏi: "Sao em mất nửa điểm?"',
             'Some students score nine and a half yet ask only, "Why did I lose half a point?"'),
            ('Câu hỏi đó không sai, nhưng nếu nó là câu duy nhất, việc học sẽ bị thu nhỏ thành săn lỗi để đủ điểm tối đa.',
             'That question is not wrong, but if it is the only question, learning shrinks into a hunt for lost marks.'),
            ('Một thầy giáo trả bài rồi hỏi ngược: "Ngoài nửa điểm đó, em đã hiểu sâu thêm điều gì?" Học sinh đứng im vì chưa từng nghĩ tới.',
             'A teacher handed back the paper and asked in return, "Besides that half point, what did you understand more deeply?" The student stood silent, never having considered it.'),
            ('Nhiều em không thiếu năng lực. Các em chỉ bị hệ thống phần thưởng làm cho quên mất mục đích thật của việc học.',
             'Many students do not lack ability. They have simply been shaped by reward systems that make them forget the real purpose of study.'),
        ],
        'lesson_vn': 'Điểm tối đa không xấu. Nhưng nếu nó là mục tiêu duy nhất, em rất dễ trở thành người học hẹp.',
        'lesson_en': 'A perfect score is not bad. But if it becomes the only goal, you easily become a narrow learner.',
    },
    {
        'title_vn': 'Học Để Làm Việc Hay Học Để Diễn?',
        'title_en': 'Are You Studying to Work or to Perform?',
        'pairs': [
            ('Một nhóm học sinh chuẩn bị thuyết trình. Có bạn chăm sửa slide cho thật đẹp, có bạn lo tập nói, có bạn đọc thêm tài liệu để hiểu vấn đề.',
             'A group of students prepared a presentation. One polished the slides, one practiced delivery, one read further to truly understand the topic.'),
            ('Hôm trình bày, hình thức của nhóm rất ổn. Nhưng chỉ cần giáo viên hỏi sâu hơn một chút, cả nhóm lộ ra chỗ rỗng ngay.',
             'On presentation day, the group looked polished. But as soon as the teacher asked a slightly deeper question, the emptiness showed.'),
            ('Có nhiều thứ trong trường học cho phép em diễn được khá lâu. Nhưng đời thật sẽ sớm hỏi tới phần ruột.',
             'Many things in school allow you to perform convincingly for quite a while. Real life, however, quickly asks about substance.'),
            ('Sau buổi đó, cả nhóm mới hiểu: học không chỉ để qua mặt một bài chấm. Học là để đứng được khi bị hỏi thật.',
             'After that session, the group finally understood: studying is not only to get past a grade. It is to remain standing when real questions come.'),
        ],
        'lesson_vn': 'Nếu em chỉ trau vỏ ngoài, em sẽ sống trong nỗi sợ bị hỏi thật. Năng lực thật là thứ làm em bớt sợ.',
        'lesson_en': 'If you polish only the surface, you will live in fear of real questions. Real competence is what makes that fear smaller.',
    },
])

ch02.extend([
    {
        'title_vn': 'Cha Muốn Con Nối Nghiệp',
        'title_en': 'The Father Wants the Son to Continue the Line',
        'pairs': [
            ('Ngày xưa trong một gia đình có nghề thuốc, người cha nhất quyết muốn con trai lớn nối nghiệp.',
             'Long ago in a family of physicians, the father insisted that his eldest son continue the profession.'),
            ('Nhưng cậu con lại thích đo đạc, dựng mô hình, và mê nghề xây dựng cầu đường.',
             'But the son loved measuring, making models, and was drawn to building bridges and roads.'),
            ('Người cha giận dữ: "Nhà ta bao đời cứu người, con bỏ đi là bất hiếu."',
             'The father grew angry: "Our family has healed people for generations. If you leave, you are unfilial."'),
            ('Bà nội chỉ nói một câu: "Cứu người bằng thuốc là cứu. Làm cây cầu để người ta qua sông an toàn cũng là cứu." Người cha im đi rất lâu.',
             'The grandmother said only one thing: "Healing with medicine saves people. Building a bridge so people cross safely also saves people." The father fell silent for a long time.'),
        ],
        'lesson_vn': 'Nhiều áp lực nghề nghiệp từ xưa đến nay đều đội lốt chữ hiếu. Nhưng hiếu không có nghĩa là sao chép nguyên xi cuộc đời cha mẹ.',
        'lesson_en': 'Across time, career pressure often wears the mask of filial duty. But duty does not mean copying a parent’s life exactly.',
    },
    {
        'title_vn': 'Gánh Kỳ Vọng Của Con Cả',
        'title_en': 'The Weight on the Eldest Child',
        'pairs': [
            ('Trong nhiều gia đình, đứa con đầu không chỉ là con. Nó còn bị coi như người phải mở đường cho cả nhà.',
             'In many families, the eldest child is not treated only as a child. That child is also treated as the one who must open the road for the whole family.'),
            ('Hải học giỏi, nên mọi người đặt hết niềm tin vào em. Tin nhiều đến mức biến thành gánh.',
             'Hai studied well, so the family placed all their hope on him. So much hope that it became a burden.'),
            ('Mỗi lần em mệt, người lớn lại nhắc chuyện em là anh cả, phải làm gương, phải gánh.',
             'Whenever he tired, adults reminded him that he was the eldest, had to set an example, had to carry the load.'),
            ('Không ai hỏi một đứa trẻ gánh lâu như vậy có đau vai không.',
             'No one asked whether a child carrying that weight for so long had aching shoulders.'),
        ],
        'lesson_vn': 'Kỳ vọng có thể nâng người ta lên, nhưng quá tải thì nó nghiền người ta xuống. Con cả cũng là một đứa trẻ trước khi là biểu tượng.',
        'lesson_en': 'Expectation can lift someone up, but overload crushes them down. An eldest child is still a child before becoming a symbol.',
    },
    {
        'title_vn': 'Mẹ Bán Rau Và Bảng Điểm',
        'title_en': 'The Vegetable Seller Mother and the Report Card',
        'pairs': [
            ('Một người mẹ bán rau ngoài chợ gửi hết hy vọng vào con gái. Bà tin chỉ có học thật giỏi mới thoát nghèo.',
             'A mother selling vegetables in the market placed all her hope in her daughter. She believed only excellent academic success could lift them from poverty.'),
            ('Niềm tin đó không sai. Nhưng dần dần nó biến thành một câu vô hình treo trên đầu đứa bé: mày không được phép trượt.',
             'That belief was not wrong. But gradually it became an invisible sentence hanging over the girl’s head: you are not allowed to fail.'),
            ('Mỗi lần con được điểm thấp, người mẹ không đánh. Bà chỉ ngồi im và thở dài. Có những tiếng thở dài còn nặng hơn roi.',
             'Whenever her daughter scored low, the mother did not hit her. She simply sat quietly and sighed. Some sighs weigh heavier than a cane.'),
            ('Đến khi cô giáo mời mẹ lên trường và nói: "Chị đang làm con sợ học chứ không còn muốn học nữa," bà mới khóc.',
             'When the teacher invited the mother to school and said, "You are making her fear study, not love it anymore," the mother finally cried.'),
        ],
        'lesson_vn': 'Khát vọng cho con đổi đời là điều đáng trọng. Nhưng nếu không tỉnh táo, hy vọng của người lớn sẽ biến thành nỗi sợ của trẻ nhỏ.',
        'lesson_en': 'A parent’s hope for a better life is honorable. But without awareness, adult hope turns into a child’s fear.',
    },
    {
        'title_vn': 'Nhật Ký Không Dám Đưa Cho Mẹ',
        'title_en': 'The Diary She Dared Not Show Her Mother',
        'pairs': [
            ('Một học sinh viết trong nhật ký: "Con không sợ học khó. Con sợ làm mẹ buồn."',
             'A student wrote in her diary: "I am not afraid of difficult study. I am afraid of making my mother sad."'),
            ('Dòng đó ngắn, nhưng nói hết tình cảnh của rất nhiều đứa trẻ học giỏi mà mệt mỏi.',
             'The line was short, but it captured the condition of many high-performing yet exhausted children.'),
            ('Các em không chỉ đối mặt kiến thức. Các em còn phải gánh trạng thái cảm xúc của người lớn.',
             'They are not facing knowledge alone. They are also carrying adult emotional states.'),
            ('Khi con cái học để giữ hòa khí gia đình hơn là học cho tương lai của chính mình, việc học rất dễ hóa thành gông.',
             'When children study more to preserve family peace than for their own future, study easily becomes a yoke.'),
        ],
        'lesson_vn': 'Học sinh không nên phải làm nhiệm vụ giữ cân bằng cảm xúc cho cha mẹ. Đó là gánh quá lớn với một người còn đang lớn.',
        'lesson_en': 'Students should not have to stabilize their parents’ emotions. That burden is too large for someone still growing up.',
    },
    {
        'title_vn': 'Cuộc Nói Chuyện Sau Bữa Cơm',
        'title_en': 'The Conversation After Dinner',
        'pairs': [
            ('Sau nhiều tháng im lặng, một cậu con trai đặt bảng điểm xuống bàn và nói: "Con cần bố nghe hết trước khi đánh giá."',
             'After months of silence, a son placed his report card on the table and said, "I need you to hear me through before judging."'),
            ('Cậu kể mình đang học vì sợ, ngủ không ngon, và không còn thấy vui với bất kỳ môn nào nữa.',
             'He explained that he was studying out of fear, sleeping badly, and no longer feeling joy in any subject.'),
            ('Người bố ban đầu khó chịu. Nhưng khi nghe đến câu: "Con không dám kể gì với bố vì lúc nào bố cũng chỉ hỏi điểm," ông khựng lại.',
             'The father was irritated at first. But when he heard, "I do not dare tell you anything because you only ever ask about scores," he stopped.'),
            ('Không phải gia đình nào cũng đổi ngay. Nhưng nhiều thay đổi bắt đầu từ một bữa cơm có người chịu nói thật.',
             'Not every family changes immediately. But many changes begin with one dinner where someone dares to tell the truth.'),
        ],
        'lesson_vn': 'Nhiều áp lực tồn tại dai vì trong nhà không ai nói thật. Giao tiếp vụng vẫn tốt hơn im lặng kéo dài.',
        'lesson_en': 'Many pressures survive because no one in the family speaks honestly. Awkward communication is still better than prolonged silence.',
    },
    {
        'title_vn': 'Người Lớn Cũng Cần Học Cách Xin Lỗi',
        'title_en': 'Adults Also Need to Learn to Apologize',
        'pairs': [
            ('Một ông bố từng ép con trai học thêm kín tuần. Đến khi thấy con hoảng loạn trước mỗi bài kiểm tra, ông mới nhận ra mình đã đi quá.',
             'A father once forced his son into a week packed with extra classes. Only when he saw the boy panic before every test did he realize he had gone too far.'),
            ('Tối đó ông nói một câu hiếm: "Bố xin lỗi. Bố tưởng thúc con là giúp con."',
             'That night he said something rare: "I am sorry. I thought pushing you was helping you."'),
            ('Đứa con ngồi im rồi khóc. Không phải vì câu xin lỗi xóa hết mọi thứ, mà vì lần đầu tiên em thấy người lớn chịu nhận phần sai của mình.',
             'The child sat silently and cried. Not because the apology erased everything, but because for the first time he saw an adult admit fault.'),
            ('Nhiều gia đình không thiếu tình thương. Họ chỉ thiếu khả năng sửa sai sau khi đã thương sai cách.',
             'Many families do not lack love. They lack the ability to correct themselves after loving in the wrong way.'),
        ],
        'lesson_vn': 'Muốn giáo dục con cái tốt, người lớn cũng phải học. Một lời xin lỗi đúng lúc có thể mở ra không khí mới cho cả nhà.',
        'lesson_en': 'To educate children well, adults must also learn. A timely apology can open a new atmosphere for the whole family.',
    },
])

ch03.extend([
    {
        'title_vn': 'Bảng Vàng Và Cái Bóng Dưới Chân',
        'title_en': 'The Honor Board and the Shadow Under It',
        'pairs': [
            ('Ngày xưa ở làng có một bảng vàng ghi tên những người đỗ đạt. Bọn trẻ lớn lên dưới cái bảng ấy, đứa nào cũng ngước nhìn.',
             'Long ago in a village there was an honor board listing successful scholars. Children grew up under it, all of them looking upward.'),
            ('Có đứa lấy đó làm động lực. Có đứa nhìn mãi rồi chỉ thấy mình thấp bé.',
             'Some used it as motivation. Others stared so long that they felt only small.'),
            ('Một ông đồ già nói: "Ngẩng đầu nhìn lên để biết đường là tốt. Nhưng nếu cứ vừa đi vừa ngước mãi, con sẽ vấp chân mình."',
             'An old tutor said, "Looking up to know the road is good. But if you keep walking while staring upward, you will trip over your own feet."'),
            ('So sánh chỉ hữu ích khi nó cho em phương hướng. Từ lúc nó làm em ghét chính mình, nó đã hỏng.',
             'Comparison helps only when it gives direction. The moment it makes you hate yourself, it is broken.'),
        ],
        'lesson_vn': 'Ngước nhìn người giỏi hơn để học là tốt. Dùng họ làm thước đo để tự chà đạp mình là dại.',
        'lesson_en': 'Looking at those ahead to learn is wise. Using them as a whip to beat yourself is foolish.',
    },
    {
        'title_vn': 'Hai Anh Em Trong Một Nhà',
        'title_en': 'Two Siblings Under One Roof',
        'pairs': [
            ('Trong một nhà có hai anh em. Anh học nhanh, em chậm hơn nhưng bền.',
             'In one house lived two siblings. The older learned quickly; the younger more slowly but with endurance.'),
            ('Người lớn khen anh trước mặt em quá nhiều. Lâu dần, em không còn nghe thấy lời khen dành cho anh nữa, chỉ nghe thấy bản án dành cho mình.',
             'Adults praised the older sibling in front of the younger too often. In time, the younger no longer heard praise for the older one, only a verdict on himself.'),
            ('Hai đứa trẻ vốn thương nhau bắt đầu khó gần nhau hơn vì mỗi lần thành công của một đứa lại thành vết xước của đứa kia.',
             'Two children who loved each other began drifting apart because each success of one became a scratch on the other.'),
            ('So sánh trong gia đình không chỉ làm một đứa đau. Nó làm hỏng luôn cả tình thân.',
             'Comparison in a family does not wound only one child. It damages the bond itself.'),
        ],
        'lesson_vn': 'Đừng dùng một đứa trẻ để kích một đứa trẻ khác. Cách đó có thể đẩy thành tích lên chút ít nhưng làm rách mối quan hệ rất lâu.',
        'lesson_en': 'Do not use one child to provoke another. That method may raise performance slightly, but it tears relationships for a long time.',
    },
    {
        'title_vn': 'Thợ Học Việc Và Người Tay Nhanh',
        'title_en': 'The Apprentice and the Quick-Handed Boy',
        'pairs': [
            ('Trong một xưởng mộc, một cậu học việc rất chán nản vì bạn cùng lứa cưa nhanh hơn, đục đẹp hơn.',
             'In a carpentry workshop, one apprentice was discouraged because another boy his age sawed faster and carved more neatly.'),
            ('Ông thợ cả không an ủi kiểu dễ dãi. Ông chỉ bảo: "Nó nhanh ở tay. Còn con chắc ở mắt. Mỗi lần đo đạc của con ít lỗi hơn nó."',
             'The master carpenter did not offer cheap comfort. He simply said, "He is quick with the hands. You are steadier with the eyes. Your measurements make fewer mistakes than his."'),
            ('Cậu bé lần đầu hiểu mình không phải bản sao lỗi của người kia. Mình là một kiểu năng lực khác chưa được gọi đúng tên.',
             'For the first time the boy understood that he was not a failed copy of the other. He was a different kind of ability not yet named correctly.'),
            ('So sánh làm mờ đi lợi thế riêng. Người hướng dẫn giỏi giúp học trò nhìn lại chỗ mạnh của mình.',
             'Comparison blurs personal strengths. A good mentor helps the learner see where their own strength already lies.'),
        ],
        'lesson_vn': 'Không phải ai chậm hơn ở một mặt cũng kém hơn toàn bộ. Học sinh cần được chỉ ra năng lực theo cách chính xác hơn.',
        'lesson_en': 'Being slower in one area does not mean being worse overall. Students need their abilities named with greater precision.',
    },
    {
        'title_vn': 'Người Bạn Đỗ Trước',
        'title_en': 'The Friend Who Succeeded First',
        'pairs': [
            ('Hai người bạn cùng ôn thi. Một người đỗ sớm, một người trượt.',
             'Two friends prepared for the same exam. One passed early; the other failed.'),
            ('Người trượt vừa mừng cho bạn vừa đau cho mình. Cảm xúc đó làm em thấy tội lỗi vì nghĩ mình nhỏ nhen.',
             'The one who failed felt happy for the friend and hurt for himself at the same time. That feeling made him guilty, as if he were petty.'),
            ('Người bạn đỗ nói: "Mày không xấu khi thấy đau. Miễn là mày không để cơn đau đó biến thành việc ghét tao."',
             'The friend who passed said, "You are not bad for hurting. As long as you do not let the pain turn into hatred toward me."'),
            ('Nhờ câu đó, họ giữ được tình bạn và người trượt cũng giữ được lòng tự trọng của mình.',
             'Because of that sentence, they kept the friendship, and the one who failed also kept his self-respect.'),
        ],
        'lesson_vn': 'Cảm giác chạnh lòng trước thành công của bạn là rất người. Điều quan trọng là xử lý nó tử tế.',
        'lesson_en': 'Feeling a sting at a friend’s success is deeply human. What matters is handling it with decency.',
    },
    {
        'title_vn': 'Cái Giếng Làng Và Bầu Trời',
        'title_en': 'The Village Well and the Sky',
        'pairs': [
            ('Có người chỉ quanh quẩn ở cái giếng làng nên tưởng bầu trời nhỏ lắm. Có người ra khỏi làng mới biết trời rộng hơn rất nhiều.',
             'Some people stay around the village well and think the sky is small. Those who leave discover that it is far wider.'),
            ('Nhiều học sinh so mình với vài bạn trong lớp rồi hoặc ảo tưởng, hoặc tuyệt vọng quá sớm.',
             'Many students compare themselves to a few classmates and become either arrogant or hopeless far too early.'),
            ('Thế giới lớn hơn một lớp, một trường, một kỳ thi. Nhưng cũng vì lớn nên cuộc đua trong đầu em không nên quá chật hẹp.',
             'The world is larger than one class, one school, one exam. And because it is larger, the race inside your head should not be so cramped.'),
            ('Biết mở rộng tầm nhìn giúp em bớt ganh hơn và cũng bớt tự mãn hơn.',
             'Broadening your view helps you become less envious and also less smug.'),
        ],
        'lesson_vn': 'So sánh trong phạm vi quá hẹp dễ làm méo bản thân. Hãy mở rộng góc nhìn để thấy mình rõ hơn.',
        'lesson_en': 'Comparison inside a space that is too narrow easily distorts the self. Widen the view to see yourself more clearly.',
    },
    {
        'title_vn': 'Người Thầy Không Xếp Hạng Tâm Hồn',
        'title_en': 'The Teacher Who Refused to Rank Souls',
        'pairs': [
            ('Một thầy giáo từng nói với lớp: "Tôi phải xếp hạng bài làm của các em, nhưng tôi từ chối xếp hạng giá trị của từng đứa."',
             'A teacher once told the class, "I may have to rank your papers, but I refuse to rank the worth of your souls."'),
            ('Câu nói đó làm nhiều học sinh sững lại, vì lần đầu họ nghe một người lớn tách thành tích khỏi phẩm giá.',
             'The sentence startled many students, because for the first time they heard an adult separate achievement from dignity.'),
            ('Từ hôm ấy, lớp vẫn cạnh tranh nhưng bớt độc hơn. Các em hiểu rằng thắng bài kiểm tra không cho mình quyền khinh người khác.',
             'From that day, the class still competed, but with less poison. They understood that winning a test did not grant the right to despise others.'),
            ('Một môi trường học lành mạnh không cần xóa cạnh tranh. Nó chỉ cần chặn việc biến cạnh tranh thành tàn nhẫn.',
             'A healthy learning environment does not need to erase competition. It only needs to stop competition from turning cruel.'),
        ],
        'lesson_vn': 'Học sinh cần được nhắc rằng điểm số có thứ bậc, nhưng con người thì không nên bị đối xử như bảng xếp hạng.',
        'lesson_en': 'Students need to be reminded that scores have rank, but human beings should not be treated like a leaderboard.',
    },
])

ch04.extend([
    {
        'title_vn': 'Sĩ Tử Trượt Khoa Thi Đầu',
        'title_en': 'The Scholar Who Failed His First Exam',
        'pairs': [
            ('Ngày xưa có người trẻ lên kinh ứng thí, chuẩn bị nhiều năm, nhưng trượt ngay kỳ đầu.',
             'Long ago a young scholar traveled to the capital after years of preparation, only to fail at the first examination.'),
            ('Cậu xé hết nháp, định bỏ học về quê làm ruộng.',
             'He tore up his drafts and planned to abandon study and return home to farm.'),
            ('Ông chủ quán trọ giữ cậu lại và bảo: "Trượt một khoa không chứng minh con dốt. Nó chỉ chứng minh lần này con chưa đủ."',
             'The innkeeper stopped him and said, "Failing one exam does not prove you are stupid. It proves only that this time you were not enough yet."'),
            ('Câu nói đó cứu cậu khỏi quyết định nóng. Ba năm sau cậu thi lại và đỗ.',
             'That sentence saved him from a hot-blooded decision. Three years later he retook the exam and passed.'),
        ],
        'lesson_vn': 'Thất bại đầu tiên rất dễ bị ta phóng to thành chân lý cuối cùng. Đó là một ảo giác nguy hiểm.',
        'lesson_en': 'The first failure is easily exaggerated into a final truth. That is a dangerous illusion.',
    },
    {
        'title_vn': 'Bài Văn Bị Gạch Đỏ Chi Chít',
        'title_en': 'The Essay Covered in Red Marks',
        'pairs': [
            ('Một học sinh nhận lại bài Văn với vô số nét đỏ. Em nhìn bài như nhìn bằng chứng cho việc mình vô vọng.',
             'A student got back an essay covered in red marks. She looked at it as if it were proof that she was hopeless.'),
            ('Cô giáo gọi em ở lại và nói: "Cô chữa nhiều vì bài này có thể khá lên. Những bài cô bỏ mặc mới đáng lo."',
             'The teacher asked her to stay and said, "I corrected this so much because it can become good. The papers I leave untouched worry me more."'),
            ('Em sững người. Cùng một tờ giấy, nhưng ý nghĩa đổi hẳn khi được nhìn bằng một lăng kính khác.',
             'She froze. It was the same paper, but its meaning changed entirely when seen through a different lens.'),
            ('Không phải mọi lời chê đều là phủ định. Có lời chê thực ra là đầu tư.',
             'Not every criticism is a rejection. Some criticism is really an investment.'),
        ],
        'lesson_vn': 'Sau thất bại, học sinh cần học cách đọc phản hồi. Không phải chỗ nào đau cũng là chỗ phải bỏ cuộc.',
        'lesson_en': 'After failure, students need to learn how to read feedback. Not every painful place is a place to quit.',
    },
    {
        'title_vn': 'Năm Gap Không Đáng Xấu Hổ',
        'title_en': 'A Gap Year Is Not Shameful',
        'pairs': [
            ('Một cậu học sinh thi xong không đỗ và quyết định nghỉ một năm để học lại, làm thêm, và nghĩ kỹ hơn về đường mình đi.',
             'A student failed an entrance exam and decided to take a year to study again, work part-time, and think more carefully about his path.'),
            ('Người quanh cậu nói nhiều câu khiến cậu nhục: chậm một năm, thua bạn bè, tụt hậu.',
             'People around him said things meant to humiliate him: one year behind, defeated by friends, falling behind.'),
            ('Nhưng trong năm đó, cậu lớn lên nhiều hơn ba năm ngồi học chỉ để khỏi bị chê.',
             'Yet in that year he grew more than in three years of studying only to avoid criticism.'),
            ('Có những đường vòng không phải lạc đường. Nó là khoảng cần thiết để người ta đi lại cho đúng.',
             'Some detours are not getting lost. They are necessary intervals for someone to get back on the right road.'),
        ],
        'lesson_vn': 'Không phải lúc nào đi nhanh hơn cũng tốt hơn. Với một số người, chậm lại một năm là cái giá hợp lý để không lạc cả chục năm.',
        'lesson_en': 'Moving faster is not always moving better. For some people, slowing down for a year is a fair price to avoid being lost for ten.',
    },
    {
        'title_vn': 'Khi Cả Lớp Biết Em Trượt',
        'title_en': 'When the Whole Class Knows You Failed',
        'pairs': [
            ('Điều đau nhất đôi khi không phải trượt. Điều đau nhất là sáng hôm sau phải bước vào lớp với cảm giác ai cũng biết.',
             'Sometimes the worst pain is not failing itself. It is walking into class the next morning feeling that everyone knows.'),
            ('Một học sinh đã định nghỉ học mấy hôm chỉ để tránh ánh mắt người khác.',
             'One student planned to skip school for several days just to avoid other people’s eyes.'),
            ('Cô giáo nói với em: "Em càng trốn, chuyện này càng lớn. Em đi học lại đi, để não em thấy rằng em vẫn sống tiếp được."',
             'The teacher told him, "The more you hide, the larger this becomes. Go back to school, so your mind sees that life continues."'),
            ('Ngày đầu rất khó, nhưng qua được ngày đầu, cái xấu hổ mất bớt quyền lực.',
             'The first day was very hard, but once it was crossed, shame lost some of its power.'),
        ],
        'lesson_vn': 'Một phần phục hồi là quay lại nơi mình muốn trốn. Nếu cứ lẩn mãi, nỗi sợ sẽ lớn hơn sự thật.',
        'lesson_en': 'Part of recovery is returning to the place you want to avoid. If you keep hiding, fear grows larger than reality.',
    },
    {
        'title_vn': 'Thua Một Keo, Học Một Nếp',
        'title_en': 'Lose One Round, Learn One Discipline',
        'pairs': [
            ('Một học sinh trượt đội tuyển và sau đó nhìn lại mới thấy mình thua không chỉ vì kiến thức.',
             'A student failed to enter the elite team and later realized the loss was not about knowledge alone.'),
            ('Em ngủ muộn, làm việc theo hứng, và chỉ tăng tốc sát ngày. Thất bại lần này bóc ra thói quen mà lời nhắc nhở trước đó chưa bóc được.',
             'He slept late, worked by mood, and accelerated only near deadlines. This failure exposed habits that previous advice had never truly exposed.'),
            ('Có những cú thua dạy bài học mà lúc còn thắng người ta không chịu học.',
             'Some defeats teach lessons that people refuse to learn while winning.'),
            ('Năm sau em chưa chắc thắng ngay, nhưng em bước vào với một nếp sống nghiêm túc hơn hẳn.',
             'The next year he did not necessarily win immediately, but he entered with a far more disciplined way of living.'),
        ],
        'lesson_vn': 'Thất bại đáng giá nhất là thất bại lộ ra được thói quen xấu. Nó đau, nhưng nó mở cửa sửa từ gốc.',
        'lesson_en': 'The most valuable failure is the one that exposes bad habits. It hurts, but it opens the door to root-level change.',
    },
    {
        'title_vn': 'Không Ai Cười Em Lâu Đến Thế',
        'title_en': 'No One Laughs at You for That Long',
        'pairs': [
            ('Sau một lần vấp, nhiều học sinh nghĩ cả thế giới đang nhớ và nhắc đến mình.',
             'After one stumble, many students think the whole world remembers and keeps talking about them.'),
            ('Sự thật phũ hơn nhưng cũng dễ thở hơn: phần lớn người khác bận lo chuyện của chính họ.',
             'The truth is harsher but also easier to breathe with: most people are busy with their own lives.'),
            ('Một cậu từng bị xấu hổ vì thuyết trình hỏng. Một tuần sau em phát hiện gần như không ai còn nhắc nữa.',
             'A boy once felt humiliated after a bad presentation. One week later he found that almost nobody mentioned it anymore.'),
            ('Chính em là người giữ sự cố đó sống lâu nhất trong đầu mình.',
             'He himself was the one keeping the incident alive longest in his own mind.'),
        ],
        'lesson_vn': 'Nhiều cú ngã kéo dài không phải vì thiên hạ bám lấy em, mà vì em bám lấy nó. Buông dần đi là một phần của đứng dậy.',
        'lesson_en': 'Many falls last not because the world clings to them, but because you do. Letting go is part of standing up.',
    },
])

print("Đang tạo chương 1-4...")

make_chapter('ch01-diem-so-khong-phai-tat-ca', 1,
    'Điểm Số Không Phải Tất Cả',
    'Scores Are Not Everything', ch01)

make_chapter('ch02-ap-luc-tu-cha-me', 2,
    'Áp Lực Từ Cha Mẹ',
    'Pressure from Parents', ch02)

make_chapter('ch03-so-sanh-va-ganh-ti', 3,
    'So Sánh Và Ganh Tị',
    'Comparison and Envy', ch03)

make_chapter('ch04-that-bai-hoc-duong', 4,
    'Thất Bại Học Đường',
    'Academic Failure', ch04)

print("Hoàn tất chương 1-4!")
