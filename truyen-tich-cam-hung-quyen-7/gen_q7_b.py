#!/usr/bin/env python3
# gen_q7_b.py -- Quyển VII ch05-08: Tuân Tử, Socrates, Plato, Aristotle
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
# CHƯƠNG 5: Tuân Tử — Giáo Dục Cải Hóa, Tu Thân, Môi Trường
# ============================================================
ch05 = [
    {
        'title_vn': 'Tính Người Vốn Ác — Nhưng Có Thể Cải Hóa',
        'title_en': 'Human Nature Is Originally Bad — But Can Be Transformed',
        'pairs': [
            ('Tuân Tử tranh luận trực tiếp với Mạnh Tử: "Tính người vốn ác — những gì tốt đẹp ở người là do học và rèn giũa."',
             'Xunzi directly debated Mencius: "Human nature is originally bad — what is good in people comes from learning and cultivation."'),
            ('"Trẻ con sinh ra đã muốn lợi, đã biết ghen tuông, đã có ham muốn giác quan. Nếu cứ thuận theo mà không sửa đổi, tranh giành và bạo lực sẽ nảy sinh."',
             '"Children are born desiring gain, knowing envy, having sensory desires. If these are followed without correction, contention and violence will arise."'),
            ('Học trò hỏi: "Vậy con người vô vọng sao?"',
             'A student asked: "Then is humanity hopeless?"'),
            ('Tuân Tử trả lời: "Không! Đó là lý do tại sao thánh nhân đặt ra Lễ và Nghĩa — để cải hóa bản chất xấu của người, hướng dẫn họ đi con đường ngay thẳng. Mọi người đều có thể trở thành Vũ vương — bằng học tập và rèn luyện."',
             'Xunzi replied: "No! That is why the sages established ritual and righteousness — to transform people\'s bad nature, to guide them on the straight path. Everyone can become King Yu — through learning and discipline."'),
            ('Khác với Mạnh Tử lạc quan về tự nhiên con người, Tuân Tử thực tế hơn: ông tin vào sức mạnh của giáo dục như công cụ biến đổi.',
             'Unlike Mencius\'s optimism about human nature, Xunzi was more pragmatic: he believed in the power of education as a transformative tool.'),
        ],
        'lesson_vn': 'Dù bạn tin tính người thiện hay ác, điều quan trọng không thay đổi: giáo dục và rèn luyện là nền tảng của mọi con người tốt. Không ai tự dưng trở nên tốt mà không có nỗ lực.',
        'lesson_en': 'Whether you believe human nature is good or bad, the important thing does not change: education and practice are the foundation of every good person. No one becomes good without effort.',
    },
    {
        'title_vn': 'Học Không Có Đỉnh — Người Quân Tử Học Mãi',
        'title_en': 'Learning Has No Summit — The Exemplary Person Never Stops Learning',
        'pairs': [
            ('Tuân Tử mở đầu thiên "Khuyến học" bằng câu: "Học không thể dừng được."',
             'Xunzi opens his chapter "Encouraging Learning" with: "Learning must not stop."'),
            ('"Xanh lấy từ chàm mà xanh hơn chàm. Băng từ nước mà lạnh hơn nước." Học trò có thể vượt qua thầy khi học đúng cách.',
             '"Blue comes from the indigo plant yet is bluer than the plant. Ice comes from water yet is colder than water." Students can surpass teachers when they learn properly.'),
            ('"Tôi suy nghĩ cả ngày không bằng học một lúc. Tôi đứng kiễng chân nhìn xa không bằng leo lên chỗ cao."',
             '"I spent all day in thought — it does not compare to a moment of study. I stood on tiptoe to see far — it does not compare to climbing to a high place."'),
            ('"Người không có bước chân của ngựa giỏi nhưng cứ tiến từng bước không dừng sẽ đến đích trước ngựa giỏi bỏ cuộc nửa đường."',
             '"One who lacks a fine horse\'s stride but keeps advancing step by step without stopping will arrive before the fine horse that gives up halfway."'),
            ('Tuân Tử tin giáo dục không chỉ truyền đạt kiến thức — nó biến đổi bản chất con người, như lửa biến đổi quặng thành kim loại.',
             'Xunzi believed education does not merely transmit knowledge — it transforms human nature, like fire transforms ore into metal.'),
        ],
        'lesson_vn': 'Người học liên tục — dù chậm — sẽ vượt qua người tài nhưng không cố gắng. Kiên trì trong học tập là đặc điểm của tâm hồn vĩ đại.',
        'lesson_en': 'The person who learns continuously — however slowly — will surpass the talented person who does not persist. Persistence in learning is the mark of a great soul.',
    },
    {
        'title_vn': 'Ngựa Địa Điền Dư Cân — Tích Lũy Từng Bước',
        'title_en': 'The Thousand-Mile Journey Comes From Single Steps',
        'pairs': [
            ('Tuân Tử dạy bằng hàng loạt hình ảnh về sức mạnh của tích lũy:',
             'Xunzi taught through a series of images about the power of accumulation:'),
            ('"Đất chồng lên đất thành núi, gió mưa từ đó sinh ra. Nước gom vào thành biển, rồng thuồng luồng từ đó sinh ra. Việc thiện tích lũy thành đức, thánh tâm tự nhiên có được."',
             '"Earth piled upon earth becomes a mountain, and wind and rain arise from it. Water gathered becomes the sea, and dragons emerge from it. Good deeds accumulated form virtue, and the sagely mind naturally takes shape."'),
            ('"Không có bước đi nhỏ, không thể đến ngàn dặm. Không dòng suối nhỏ, không thành sông biển."',
             '"Without small steps, one cannot reach a thousand miles. Without small streams, rivers and seas cannot form."'),
            ('Một học trò than thở: "Con không đủ tài năng thiên bẩm để vĩ đại."',
             'A student lamented: "I do not have enough innate talent to be great."'),
            ('Tuân Tử đáp: "Con giun đất không có móng vuốt sắc, không có gân cốt mạnh, nhưng ăn đất trên ăn ngầm dưới, uống nước vàng. Nó làm được tất cả vì chuyên nhất. Con cua có tám chân và hai càng nhưng không có hang của loài khác để ở. Nó không chuyên nhất. Tài năng thiên bẩm ít giúp ích bằng sự chuyên nhất."',
             'Xunzi replied: "An earthworm has no sharp claws, no strong bones, yet it eats from the yellow soil above and drinks from the yellow springs below. It accomplishes this through single-mindedness. A crab has eight legs and two claws but has no burrow of its own to live in. It lacks single-mindedness. Innate talent matters far less than focused effort."'),
        ],
        'lesson_vn': 'Thiên tài không phải điểm khởi đầu — nó là kết quả của tích lũy lâu dài. Hãy bắt đầu từ đâu bạn đang đứng và tiến từng bước một.',
        'lesson_en': 'Genius is not a starting point — it is the result of long accumulation. Begin from where you stand and advance one step at a time.',
    },
    {
        'title_vn': 'Chọn Bạn Mà Chơi — Môi Trường Quan Trọng Hơn Ý Chí',
        'title_en': 'Choose Your Companions — Environment Matters More Than Willpower',
        'pairs': [
            ('Tuân Tử viết: "Cỏ bồng dựa vào lúa đen mà thành thẳng, không cần nắn. Cát trắng nằm trong bùn đen thì đen cùng."',
             'Xunzi wrote: "The mugwort plant, growing among hemp, becomes straight without being trained. White sand in black mud turns black together."'),
            ('"Vì vậy người quân tử phải chọn chỗ ở cẩn thận, chọn người học cùng cẩn thận."',
             '"Therefore the exemplary person must choose their dwelling carefully, choose their learning companions carefully."'),
            ('Một thanh niên than với Tuân Tử về việc bạn bè xấu kéo anh xuống.',
             'A young man complained to Xunzi about bad friends pulling him down.'),
            ('Tuân Tử hỏi: "Vậy tại sao anh không chọn bạn khác?"',
             'Xunzi asked: "Then why do you not choose different friends?"'),
            ('"Nhưng những người tốt không muốn chơi với con." "Vậy thì con hãy tự làm cho mình đáng được làm bạn với người tốt."',
             '"But good people do not want to associate with me." "Then make yourself worthy of the friendship of good people."'),
            ('Câu trả lời đó tóm tắt toàn bộ triết lý giáo dục của Tuân Tử: thay đổi bản thân để xứng đáng với môi trường tốt — và môi trường tốt sẽ duy trì sự thay đổi đó.',
             'That answer summarizes Xunzi\'s entire educational philosophy: change yourself to deserve a good environment — and a good environment will sustain that change.'),
        ],
        'lesson_vn': 'Bạn là trung bình cộng của năm người bạn gần gũi nhất. Chọn môi trường xã hội của bạn như chọn đất trồng cây — loại đất quyết định loại cây bạn trở thành.',
        'lesson_en': 'You are the average of the five people you associate with most. Choose your social environment as you would choose soil for a plant — the soil type determines what kind of plant you become.',
    },
    {
        'title_vn': 'Lễ — Nền Tảng Của Mọi Văn Minh',
        'title_en': 'Ritual Propriety — The Foundation of All Civilization',
        'pairs': [
            ('Tuân Tử giải thích tại sao cần Lễ: "Người ta từ khi sinh ra đã có ham muốn. Ham muốn mà không được thoả mãn thì phải tìm cách thoả mãn. Không có giới hạn và phân chia thì tranh giành. Tranh giành thì loạn. Loạn thì nghèo."',
             'Xunzi explained why ritual is necessary: "From birth, people have desires. When desires are not satisfied, they must seek satisfaction. Without limits and distinctions, there is contention. Contention causes disorder. Disorder leads to poverty."'),
            ('"Thánh vương xưa ghét loạn nên chế lễ nghĩa để phân chia — để nuôi ham muốn của người, cung cấp cho sự tìm kiếm của người. Đảm bảo ham muốn không thiếu vật, vật không thiếu trước ham muốn — hai thứ cùng lớn và nương tựa nhau."',
             '"The ancient sage kings hated disorder, so they established ritual and righteousness to create distinctions — to nourish people\'s desires, to supply what they seek. Ensuring desires are not hampered by things and things are not depleted by desires — both growing and sustaining each other."'),
            ('Lễ không phải quy tắc tùy tiện — đó là hệ thống giải quyết xung đột mà không cần bạo lực.',
             'Ritual propriety is not arbitrary rules — it is a system for resolving conflicts without violence.'),
            ('Khi xã hội mất đi các quy ước chung, người mạnh nhất sẽ thắng — không phải người tốt nhất.',
             'When society loses shared conventions, the strongest will prevail — not the best.'),
        ],
        'lesson_vn': 'Quy ước xã hội, luật pháp và nghi thức không phải xích trói tự do — chúng là điều kiện để tự do tồn tại được. Không có chúng, chỉ có quyền của kẻ mạnh.',
        'lesson_en': 'Social conventions, laws, and ritual are not chains on freedom — they are the conditions under which freedom can exist. Without them, only the power of the strongest prevails.',
    },
    {
        'title_vn': 'Người Quân Tử Và Kẻ Tiểu Nhân Trước Lợi Và Nghĩa',
        'title_en': 'The Exemplary Person and the Petty Person Before Profit and Righteousness',
        'pairs': [
            ('Tuân Tử phân biệt rõ: "Người quân tử: tin vào đạo lý hơn lợi ích. Người tiểu nhân: tin vào lợi ích hơn đạo lý."',
             'Xunzi drew a clear distinction: "The exemplary person: believes in principle over profit. The petty person: believes in profit over principle."'),
            ('"Người quân tử trước tiên suy nghĩ điều gì là đúng, rồi mới làm. Người tiểu nhân trước tiên suy nghĩ điều gì có lợi, rồi mới làm."',
             '"The exemplary person first thinks about what is right, then acts. The petty person first thinks about what is profitable, then acts."'),
            ('Học trò hỏi: "Nhưng thưa thầy, nếu làm điều đúng mà bị thiệt thòi thì sao?"',
             'A student asked: "But Master, what if doing the right thing puts us at a disadvantage?"'),
            ('Tuân Tử đáp: "Hãy nhìn dài hạn. Người có danh tiếng tốt sẽ được tin tưởng và hợp tác với nhiều người hơn. Về lâu dài, làm điều đúng thường cũng là điều có lợi nhất — nhưng ta không làm điều đúng vì nó có lợi, mà vì nó đúng."',
             'Xunzi replied: "Look long-term. The person with a good reputation will be trusted and will cooperate with more people. In the long run, doing the right thing is also usually most profitable — but we do not do the right thing because it is profitable; we do it because it is right."'),
        ],
        'lesson_vn': 'Hành động đúng vì nó đúng, không phải vì nó có lợi. Nghịch lý là người hành động theo nguyên tắc đó thường cũng đạt được kết quả tốt hơn về lâu dài.',
        'lesson_en': 'Act rightly because it is right, not because it is profitable. The paradox is that people who act on that principle usually achieve better results over the long term.',
    },
    {
        'title_vn': 'Trị Quốc Lấy Lễ Làm Gốc',
        'title_en': 'Governing a State Requires Ritual as Its Root',
        'pairs': [
            ('Tuân Tử làm quan ở nước Triệu và bị hỏi về bí quyết cai trị tốt.',
             'Xunzi served as an official in the state of Zhao and was asked about the secret of good governance.'),
            ('"Lễ là nền tảng. Nhân tài là công cụ. Luật pháp là điều kiện bổ sung."',
             '"Ritual propriety is the foundation. Talented people are the tools. Laws are supplementary conditions."'),
            ('"Vua không lễ thì không tôn trọng thần dân. Thần dân không lễ thì không vâng lời vua. Quan không lễ thì không quản lý được thuộc cấp. Quốc gia không lễ thì mọi mệnh lệnh đều không ổn định."',
             '"A king without ritual will not respect his ministers. Ministers without ritual will not obey their king. Officials without ritual cannot manage subordinates. A state without ritual has unstable commands."'),
            ('Hỏi thêm về luật pháp, Tuân Tử nói: "Có người cầm luật mà không cần người giải thích và áp dụng tinh tế thì luật cũng vô nghĩa."',
             'Asked further about laws, Xunzi said: "Having the law without people of judgment to apply it wisely renders it meaningless."'),
            ('Có pháp luật nhưng thiếu con người có đức hạnh vận hành nó là bộ máy không có năng lượng.',
             'Having laws but lacking virtuous people to operate them is a machine without energy.'),
        ],
        'lesson_vn': 'Thể chế tốt cần con người tốt để vận hành. Và con người tốt cần thể chế tốt để duy trì sự tốt đó. Hai yếu tố không thể tách rời.',
        'lesson_en': 'Good institutions need good people to operate them. And good people need good institutions to sustain their goodness. The two cannot be separated.',
    },
    {
        'title_vn': 'Học Rộng Rồi Về Tóm Lại',
        'title_en': 'Learn Broadly Then Distill to the Essential',
        'pairs': [
            ('Tuân Tử dạy phương pháp học: "Học không nên quá phân tán mà cũng không nên quá hẹp. Học rộng — tích lũy nhiều loại kiến thức. Rồi về tóm lại — tìm ra nguyên lý cốt lõi."',
             'Xunzi taught a method of learning: "Learning should be neither too scattered nor too narrow. Learn broadly — accumulate diverse knowledge. Then distill — find the core principles."'),
            ('"Người chỉ học rộng mà không tóm lại là người có nhiều gỗ nhưng không xây được nhà. Người chỉ tóm lại mà không học rộng là người xây nhà không có đủ vật liệu."',
             '"One who learns broadly without distilling is like a person with much wood who cannot build a house. One who distills without learning broadly has insufficient building materials."'),
            ('Học trò hỏi: "Làm thế nào để biết mình đã học đủ rộng chưa?"',
             'A student asked: "How do I know when I have learned broadly enough?"'),
            ('Tuân Tử: "Khi bạn có thể nhìn một vấn đề từ nhiều góc độ khác nhau mà không bị kẹt ở một góc duy nhất — đó là bạn đã học đủ rộng."',
             'Xunzi: "When you can see a problem from many different perspectives without being stuck in a single one — that is when you have learned broadly enough."'),
        ],
        'lesson_vn': 'Hãy học rộng nhưng đừng bị chìm đắm. Mục tiêu cuối cùng là tổng hợp — hiểu nguyên lý sâu bên dưới tất cả những chi tiết bề mặt.',
        'lesson_en': 'Learn broadly but do not drown in details. The final goal is synthesis — understanding the deep principles beneath all the surface details.',
    },
    {
        'title_vn': 'Tự Tri Chi Minh — Sáng Suốt Là Biết Mình',
        'title_en': 'Clarity of Self-Knowledge',
        'pairs': [
            ('Tuân Tử gặp một người tự hào về trí tuệ của mình và hỏi anh ta: "Bạn có biết điểm yếu lớn nhất của bạn không?"',
             'Xunzi met a man proud of his intelligence and asked him: "Do you know your greatest weakness?"'),
            ('Người đàn ông nghĩ một lúc rồi liệt kê một số điểm yếu nhỏ.',
             'The man thought a while and listed several minor weaknesses.'),
            ('Tuân Tử nói: "Điểm yếu lớn nhất của bạn là bạn không biết điểm yếu lớn nhất của mình."',
             'Xunzi said: "Your greatest weakness is not knowing your greatest weakness."'),
            ('"Người thực sự thông tuệ không ngừng tự xét bản thân. Người hão huyền tin mình đã hoàn hảo. Sự khác biệt đó quyết định ai thực sự học được từ cuộc sống."',
             '"The truly wise person never stops examining themselves. The self-deluded person believes they are already perfect. That difference determines who truly learns from life."'),
            ('Tuân Tử tin giáo dục không chỉ là học thêm — nó là liên tục sửa những hiểu biết sai về bản thân và thế giới.',
             'Xunzi believed education is not just adding more knowledge — it is continuously correcting mistaken beliefs about oneself and the world.'),
        ],
        'lesson_vn': 'Người khiêm tốn nhận ra giới hạn của mình sẽ liên tục lớn lên. Người tưởng mình biết hết đã đặt ra giới hạn cho chính việc học của mình.',
        'lesson_en': 'The humble person who recognizes their limits will continuously grow. The person who thinks they know everything has placed a limit on their own learning.',
    },
    {
        'title_vn': 'Không Phân Biệt Nguồn Gốc Trong Giáo Dục',
        'title_en': 'No Discrimination in Education',
        'pairs': [
            ('Tuân Tử nhận học trò từ mọi tầng lớp xã hội — kể cả những người xuất thân thấp kém.',
             'Xunzi accepted students from all social classes — including those of humble origin.'),
            ('Khi bị hỏi tại sao, ông trả lời theo tinh thần của Khổng Tử nhưng thêm vào lý do của riêng mình: "Vì tính người có thể thay đổi được qua giáo dục. Ai cũng có khả năng trở thành quân tử."',
             'When asked why, he replied in the spirit of Confucius but added his own reason: "Because human nature can be changed through education. Anyone has the potential to become an exemplary person."'),
            ('"Người xuất thân thấp kém nhưng học và rèn luyện có thể vượt qua người xuất thân cao quý mà lười biếng."',
             '"A person of humble birth who studies and cultivates can surpass a person of noble birth who is lazy."'),
            ('Học trò Hàn Phi sau này triển khai tư tưởng Tuân Tử theo hướng pháp trị — nhưng học trò khác là Lý Tư và Hàn Phi đều thừa nhận họ học được từ Tuân Tử nhiều nhất.',
             'His student Han Fei later developed Xunzi\'s thought in the direction of legalism — but both Li Si and Han Fei acknowledged they learned most from Xunzi.'),
            ('Nghịch lý: người thầy tin vào tính người có thể cải hóa đã đào tạo hai học trò theo đường pháp trị cứng nhắc nhất.',
             'The paradox: the teacher who believed in transformable human nature trained two students who became the most rigid legalists.'),
        ],
        'lesson_vn': 'Giáo dục là quyền của tất cả mọi người — không phải đặc quyền của người giàu hay người có xuất thân tốt. Ai cũng có thể học và cải thiện bản thân.',
        'lesson_en': 'Education is the right of all people — not the privilege of the wealthy or the well-born. Anyone can learn and improve themselves.',
    },
]

# ============================================================
# CHƯƠNG 6: Socrates — Biết Mình Không Biết, Đối Thoại, Đức Hạnh
# ============================================================
ch06 = [
    {
        'title_vn': 'Ta Chỉ Biết Rằng Ta Không Biết Gì',
        'title_en': 'I Know Only That I Know Nothing',
        'pairs': [
            ('Khi nhà tiên tri Apollo tại Delphi tuyên bố Socrates là người khôn ngoan nhất Athens, Socrates bối rối.',
             'When the Oracle of Apollo at Delphi declared Socrates the wisest man in Athens, Socrates was puzzled.'),
            ('"Ta không biết mình khôn ngoan điều gì. Hãy để ta đi tìm người khôn ngoan hơn để chứng minh nhà tiên tri sai."',
             '"I do not know what wisdom I have. Let me go find someone wiser to prove the oracle wrong."'),
            ('Ông đến gặp các chính trị gia, nhà thơ, thợ thủ công nổi tiếng — những người được tiếng là khôn ngoan.',
             'He visited famous politicians, poets, craftsmen — those with reputations for wisdom.'),
            ('Sau mỗi cuộc trò chuyện, ông kết luận: "Người này nghĩ họ biết điều họ không biết. Tôi không biết điều đó — nhưng tôi cũng không nghĩ mình biết nó. Vì vậy tôi có phần khôn hơn một chút."',
             'After each conversation he concluded: "This person thinks they know what they do not know. I do not know that thing — but I also do not think I know it. So I am slightly wiser."'),
            ('Đây là nền tảng của triết học Socrates: sự khiêm tốn nhận thức — biết giới hạn của tri thức mình là bước đầu tiên của sự khôn ngoan.',
             'This is the foundation of Socratic philosophy: epistemic humility — knowing the limits of one\'s knowledge is the first step of wisdom.'),
        ],
        'lesson_vn': 'Người thực sự học được là người biết mình chưa biết đủ. Sự chắc chắn quá mức là kẻ thù của sự hiểu biết. Hãy giữ câu hỏi mở lâu hơn bạn muốn.',
        'lesson_en': 'The person who truly learns is one who knows they do not yet know enough. Excessive certainty is the enemy of understanding. Keep questions open longer than you want to.',
    },
    {
        'title_vn': 'Phép Đỡ Đẻ — Socrates Giúp Người Khác Tự Tìm Ra Sự Thật',
        'title_en': 'Midwifery — Socrates Helps Others Give Birth to Truth',
        'pairs': [
            ('Socrates thường nói: mẹ ta là bà mụ đỡ đẻ, còn ta cũng là bà mụ đỡ đẻ — nhưng đỡ đẻ ý tưởng.',
             'Socrates often said: "My mother was a midwife, and I too am a midwife — but I deliver ideas."'),
            ('Ông gặp Meno và hỏi: "Đức hạnh là gì?"',
             'He met Meno and asked: "What is virtue?"'),
            ('Meno đưa ra nhiều định nghĩa — đức hạnh của đàn ông, của phụ nữ, của trẻ em, của người già.',
             'Meno offered many definitions — virtue of men, of women, of children, of the elderly.'),
            ('Socrates hỏi: "Nhưng điều gì là chung cho tất cả? Như ong — có nhiều loài ong, nhưng điều gì làm cho tất cả đều là ong?"',
             'Socrates asked: "But what is common to all? Like bees — there are many kinds of bees, but what makes them all bees?"'),
            ('Qua hàng loạt câu hỏi, Meno dần dần tự phát hiện ra sự mâu thuẫn trong định nghĩa của mình và tự xây dựng lại.',
             'Through a series of questions, Meno gradually discovered the contradictions in his own definitions and rebuilt them himself.'),
            ('"Ta không dạy bất cứ điều gì," Socrates nói. "Ta chỉ hỏi. Sự thật đã ở trong anh — ta chỉ giúp anh sinh nó ra."',
             '"I teach nothing," Socrates said. "I only ask. The truth was already within you — I only helped you give birth to it."'),
        ],
        'lesson_vn': 'Câu hỏi tốt thường hữu ích hơn câu trả lời tốt. Khi bạn giúp người khác tự tìm ra sự thật, họ sẽ nhớ và tin tưởng nó hơn gấp nhiều lần so với khi bạn nói cho họ.',
        'lesson_en': 'A good question is often more useful than a good answer. When you help others discover truth for themselves, they will remember and trust it far more than when you simply tell them.',
    },
    {
        'title_vn': 'Sống Không Được Xem Xét Không Đáng Sống',
        'title_en': 'The Unexamined Life Is Not Worth Living',
        'pairs': [
            ('Trước tòa án Athens sau khi bị kết tội, Socrates có cơ hội đề xuất hình phạt nhẹ hơn.',
             'Before the court of Athens after being convicted, Socrates had the opportunity to propose a lighter sentence.'),
            ('Thay vì xin tha hoặc đề xuất lưu đày, ông nói những điều khiến tòa án tức giận hơn.',
             'Instead of pleading for mercy or proposing exile, he said things that angered the court further.'),
            ('"Tôi sẽ không bao giờ ngừng triết học. Nếu tôi bị lưu đày và bảo đừng triết học, tôi sẽ từ chối. Vì cuộc sống không được xem xét không đáng sống."',
             '"I will never stop philosophizing. If I were exiled and told not to philosophize, I would refuse. For the unexamined life is not worth living."'),
            ('"Tôi là con ruồi trâu của Athens — tôi chích vào con ngựa lười biếng này để nó không ngủ quên."',
             '"I am the gadfly of Athens — I sting this sluggish horse to keep it from falling asleep."'),
            ('Tòa án bỏ phiếu tử hình ông. Ông từ chối trốn thoát và uống thuốc độc.',
             'The court voted for his execution. He refused escape and drank the poison.'),
            ('Ông chết vì trung thành với điều ông tin — rằng triết học, đặt câu hỏi, và sống có ý thức quan trọng hơn sự sống vật lý.',
             'He died faithful to what he believed — that philosophy, questioning, and conscious living matter more than physical survival.'),
        ],
        'lesson_vn': 'Hãy liên tục đặt câu hỏi về cuộc sống của mình: Tôi đang sống vì điều gì? Các lựa chọn của tôi có phản ánh điều tôi thực sự tin không? Đó là hành động dũng cảm nhất.',
        'lesson_en': 'Continuously question your life: What am I living for? Do my choices reflect what I truly believe? That is the most courageous act.',
    },
    {
        'title_vn': 'Chỉ Có Một Điều Tốt — Tri Thức. Chỉ Có Một Điều Xấu — Ngu Dốt',
        'title_en': 'There Is Only One Good — Knowledge. Only One Evil — Ignorance.',
        'pairs': [
            ('Socrates dạy học trò Plato về nguồn gốc của hành vi xấu.',
             'Socrates taught his student Plato about the origin of bad behavior.'),
            ('"Khi người ta làm điều xấu, họ có thực sự muốn điều xấu không?"',
             '"When people do wrong, do they truly want to do wrong?"'),
            ('Plato ngạc nhiên: "Thưa thầy, ý thầy là sao? Kẻ trộm biết ăn trộm là xấu."',
             'Plato was surprised: "Master, what do you mean? A thief knows stealing is wrong."'),
            ('"Kẻ trộm ăn trộm vì anh ta nghĩ nó sẽ đem lại điều tốt cho anh ta — tiền bạc, sự sống còn. Anh ta sai về điều đó, nhưng anh ta đang cố đạt điều tốt theo cách anh ta hiểu. Không ai cố ý cố làm điều mà họ biết là xấu cho bản thân."',
             '"The thief steals because he thinks it will bring him good — money, survival. He is wrong about this, but he is trying to achieve good as he understands it. No one deliberately tries to do what they know is bad for themselves."'),
            ('"Vì vậy, điều duy nhất là xấu thực sự là sự hiểu sai — ngu dốt về điều gì thực sự tốt. Và điều duy nhất là tốt thực sự là tri thức về điều gì thực sự tốt."',
             '"Therefore, the only real evil is misunderstanding — ignorance of what is truly good. And the only real good is knowledge of what is truly good."'),
        ],
        'lesson_vn': 'Trước khi phán xét ai đó là ác, hãy hỏi: họ có thực sự biết điều tốt không? Dạy người tốt hơn là trừng phạt họ — bởi vì ác hành thường bắt nguồn từ sự thiếu hiểu biết.',
        'lesson_en': 'Before judging someone as evil, ask: do they truly know the good? Teaching people is better than punishing them — because wrongdoing often originates in lack of understanding.',
    },
    {
        'title_vn': 'Phép Biện Luận — Socrates Và Sophist',
        'title_en': 'The Art of Argument — Socrates and the Sophists',
        'pairs': [
            ('Sophist là những người dạy nghệ thuật thuyết phục — thu tiền để dạy cách thắng trong tranh luận, không quan tâm điều gì đúng.',
             'Sophists were those who taught the art of persuasion — charging money to teach how to win arguments, regardless of what was true.'),
            ('Socrates phân biệt rõ: "Ta không phải Sophist. Ta không dạy người ta thắng tranh luận. Ta dạy người ta tìm sự thật."',
             'Socrates drew a clear distinction: "I am not a Sophist. I do not teach people to win arguments. I teach people to find truth."'),
            ('Khi gặp một Sophist nổi tiếng, Socrates hỏi đơn giản: "Bạn dạy đức hạnh là gì?"',
             'Meeting a famous Sophist, Socrates simply asked: "What is the virtue you teach?"'),
            ('Sophist dài dòng giải thích. Socrates đặt câu hỏi từng điểm. Sophist mâu thuẫn chính mình. Đám đông cười.',
             'The Sophist gave a lengthy explanation. Socrates questioned each point. The Sophist contradicted himself. The crowd laughed.'),
            ('"Tôi không cố làm bạn trông ngốc," Socrates nói nhẹ nhàng. "Tôi chỉ muốn chúng ta cùng nhau tìm ra điều thực sự là đơn giản."',
             '"I am not trying to make you look foolish," Socrates said gently. "I only want us together to find what is truly simple."'),
        ],
        'lesson_vn': 'Biết thắng cuộc tranh luận và biết sự thật là hai kỹ năng khác nhau — và thường chống lại nhau. Hãy chọn theo đúng hướng.',
        'lesson_en': 'Knowing how to win an argument and knowing the truth are two different skills — and often opposed. Choose your direction wisely.',
    },
    {
        'title_vn': 'Người Tốt Không Thể Bị Tổn Hại',
        'title_en': 'No Harm Can Come to a Good Person',
        'pairs': [
            ('Trong những giờ cuối trước khi uống thuốc độc, bạn bè cầu xin Socrates chạy trốn.',
             'In the final hours before drinking the poison, friends begged Socrates to escape.'),
            ('"Giám ngục sẵn sàng nhắm mắt. Chúng tôi đã bố trí quần áo và xe ngựa. Hãy đi!"',
             '"The jailer is ready to look away. We have arranged clothes and a horse. Go!"'),
            ('Socrates trả lời: "Thân thể ta có thể chết. Nhưng linh hồn ta — những gì ta thực sự là — không thể chết bởi bất cứ điều gì người Athens làm. Họ có thể giết ta, nhưng họ không thể làm ta trở nên tồi tệ hơn."',
             'Socrates replied: "My body may die. But my soul — what I truly am — cannot be killed by anything the Athenians do. They can kill me, but they cannot make me worse."'),
            ('"Người tốt không thể bị tổn hại thực sự — vì điều tệ nhất họ có thể làm với người tốt là giết thân xác. Còn linh hồn người tốt vẫn nguyên vẹn."',
             '"No true harm can come to a good person — for the worst that can be done to a good person is killing the body. But the soul of a good person remains intact."'),
            ('Ông uống thuốc độc bình thản, nói chuyện triết học cho đến khi thuốc ngấm.',
             'He drank the poison calmly, discussing philosophy until it took effect.'),
        ],
        'lesson_vn': 'Điều người khác có thể làm với bạn là hữu hạn. Điều bạn tự làm với tâm hồn và đức hạnh của mình — đó là điều thực sự quan trọng và không ai khác kiểm soát được ngoài bạn.',
        'lesson_en': 'What others can do to you is limited. What you do with your own soul and virtue — that is what truly matters and no one else controls it but you.',
    },
    {
        'title_vn': 'Hỏi Những Câu Đúng Về Tình Yêu',
        'title_en': 'Asking the Right Questions About Love',
        'pairs': [
            ('Tại một bữa tiệc, Socrates được hỏi về tình yêu và dẫn lại câu chuyện người phụ nữ trí tuệ Diotima dạy ông.',
             'At a banquet, Socrates was asked about love and recounted what the wise woman Diotima had taught him.'),
            ('"Tình yêu không phải thần — nó là tinh linh trung gian giữa người và thần, giữa dốt nát và khôn ngoan."',
             '"Love is not a god — it is a spirit intermediary between mortals and gods, between ignorance and wisdom."'),
            ('"Yêu cái đẹp là bước đầu. Nhưng cái đẹp toàn nhất không phải vẻ đẹp thân xác của một người — mà là cái Đẹp thuần túy, vĩnh cửu, không biến đổi."',
             '"To love beauty is the first step. But the greatest beauty is not the physical beauty of one person — it is pure, eternal, unchanging Beauty itself."'),
            ('"Người được dẫn dắt đúng cách trong tình yêu sẽ đi từ yêu một thân xác đẹp, đến yêu vẻ đẹp của nhiều thân xác, đến yêu vẻ đẹp trong tâm hồn, đến yêu vẻ đẹp trong kiến thức và hành động tốt đẹp, cho đến khi đến được tình yêu thuần túy nhất — tình yêu Cái Đẹp tuyệt đối."',
             '"One properly guided in love will move from loving one beautiful body, to loving the beauty in many bodies, to loving beauty of soul, to loving beauty in knowledge and fine actions, until arriving at the purest love — love of absolute Beauty itself."'),
        ],
        'lesson_vn': 'Tình yêu lãng mạn chỉ là một hình thức của điều gì đó sâu hơn: khao khát cái tốt đẹp và vĩnh cửu. Khi hiểu điều này, mọi hình thức yêu thương đều có thể trở thành con đường dẫn đến trí tuệ.',
        'lesson_en': 'Romantic love is only one form of something deeper: the longing for what is good and eternal. When you understand this, every form of love can become a path to wisdom.',
    },
    {
        'title_vn': 'Hỏi Chính Mình Trước Khi Hỏi Người Khác',
        'title_en': 'Question Yourself Before Questioning Others',
        'pairs': [
            ('Một thanh niên giàu đến gặp Socrates và nói anh muốn học triết học để nói chuyện trong các buổi tiệc sang trọng.',
             'A wealthy young man came to Socrates saying he wanted to learn philosophy to converse at elegant banquets.'),
            ('Socrates bắt đầu hỏi: "Điều gì làm cho cuộc sống tốt?"',
             'Socrates began asking: "What makes a life good?"'),
            ('"Của cải." "Bạn có bao giờ thấy người giàu mà không hạnh phúc không?" "Vâng." "Vậy của cải đủ chưa?"',
             '"Wealth." "Have you ever seen a rich person who was unhappy?" "Yes." "Then is wealth enough?"'),
            ('"Sức khỏe." "Bạn có biết người khỏe mạnh nhưng sống vô nghĩa không?" "Vâng." "Vậy sức khỏe đủ chưa?"',
             '"Health." "Do you know healthy people who live meaninglessly?" "Yes." "Then is health enough?"'),
            ('Sau hai giờ, thanh niên bắt đầu khóc: "Thưa ngài, tôi không biết gì mà tôi cứ tưởng tôi biết."',
             'After two hours, the young man began to weep: "Sir, I know nothing although I thought I knew."'),
            ('Socrates nhẹ nhàng: "Đây là buổi học triết học quan trọng nhất của bạn. Bây giờ chúng ta có thể bắt đầu thực sự."',
             'Socrates gently said: "This is your most important philosophical lesson. Now we can truly begin."'),
        ],
        'lesson_vn': 'Nhận ra mình không biết là khởi đầu của mọi sự học. Trước khi tìm câu trả lời từ bên ngoài, hãy để câu hỏi bên trong làm tan vỡ những giả định sai của mình.',
        'lesson_en': 'Realizing you do not know is the beginning of all learning. Before seeking answers from outside, let inner questions shatter your false assumptions.',
    },
    {
        'title_vn': 'Cái Ác Đến Từ Không Biết Điều Gì Tốt',
        'title_en': 'Evil Comes from Not Knowing What Is Good',
        'pairs': [
            ('Socrates gặp người tướng quân Laches và hỏi: "Lòng can đảm là gì?"',
             'Socrates met the general Laches and asked: "What is courage?"'),
            ('"Đứng vững không chạy trốn trong trận chiến."',
             '"Standing firm in battle without fleeing."'),
            ('"Nhưng người lính bơi vào bão để cứu đồng đội có dũng cảm không?" "Có." "Ông ta không đứng vững trong trận chiến — vậy thì định nghĩa của anh thiếu gì?"',
             '"But is a soldier who swims into a storm to rescue comrades courageous?" "Yes." "He is not standing firm in battle — so what does your definition miss?"'),
            ('Sau nhiều vòng, họ đến kết luận: dũng cảm là biết điều gì đáng sợ và điều gì không. Nó đòi hỏi tri thức.',
             'After many rounds, they concluded: courage is knowing what is worth fearing and what is not. It requires knowledge.'),
            ('"Vì vậy kẻ hèn nhát không phải người thiếu bản năng chiến đấu — họ là người không hiểu đúng điều gì thực sự đáng sợ và điều gì không. Và kẻ liều lĩnh không phải dũng cảm — họ cũng không hiểu điều gì đáng sợ và điều gì không."',
             '"Therefore the coward is not simply one who lacks fighting instinct — they are one who misunderstands what is truly worth fearing and what is not. And the reckless person is not courageous — they too misunderstand what is worth fearing and what is not."'),
        ],
        'lesson_vn': 'Đức hạnh không phải cảm xúc hay bản năng — nó là một loại tri thức. Người tốt là người hiểu đúng điều gì thực sự có giá trị và điều gì không.',
        'lesson_en': 'Virtue is not emotion or instinct — it is a form of knowledge. The good person is one who correctly understands what is truly valuable and what is not.',
    },
    {
        'title_vn': 'Con Ruồi Trâu Của Athens',
        'title_en': 'The Gadfly of Athens',
        'pairs': [
            ('Socrates mô tả vai trò của mình trong Apologia: "Thần đặt ta vào Athens như một con ruồi trâu trên con ngựa quý nhưng lười biếng — để chích và đánh thức nó."',
             'Socrates described his role in the Apology: "The god has placed me in Athens like a gadfly on a noble but sluggish horse — to sting and awaken it."'),
            ('"Ta đi khắp nơi không ngừng thúc đẩy, thuyết phục, khiển trách các bạn — mỗi cá nhân trong các bạn, cả ngày, cả đời."',
             '"I go everywhere unceasingly urging, persuading, reproaching you — every one of you, all day, all my life."'),
            ('"Nếu các bạn giết ta, các bạn sẽ không dễ tìm được người khác như ta — mặc dù điều đó nghe có vẻ buồn cười. Ta thực sự là quà tặng của thần cho thành phố."',
             '"If you kill me, you will not easily find someone like me — though that may sound absurd. I am truly the god\'s gift to the city."'),
            ('Athens giết con ruồi trâu của mình. Nhưng ý tưởng của Socrates đã sống hơn hai nghìn năm.',
             'Athens killed its gadfly. But Socrates\'s ideas have lived for more than two thousand years.'),
            ('Ông đã đúng về một điều: không dễ tìm được người sẵn sàng nói thật với quyền lực.',
             'He was right about one thing: it is not easy to find people willing to speak truth to power.'),
        ],
        'lesson_vn': 'Đôi khi vai trò cao quý nhất là người đặt câu hỏi khó chịu — không phải để tranh luận, mà để thức tỉnh. Xã hội cần những "ruồi trâu" như vậy để không ngủ quên.',
        'lesson_en': 'Sometimes the noblest role is the one who asks uncomfortable questions — not to argue, but to awaken. Society needs such "gadflies" to keep from falling asleep.',
    },
]

# ============================================================
# CHƯƠNG 7: Plato — Hang Động, Linh Hồn, Tình Yêu Đích Thực
# ============================================================
ch07 = [
    {
        'title_vn': 'Hang Động Của Plato — Ta Có Đang Nhìn Bóng Không?',
        'title_en': 'Plato\'s Cave — Are We Seeing Only Shadows?',
        'pairs': [
            ('Plato mô tả những tù nhân bị xích trong hang từ khi sinh ra, chỉ có thể nhìn về phía trước.',
             'Plato described prisoners chained in a cave from birth, able only to look forward.'),
            ('Phía sau họ là lửa và những hình nộm di chuyển — ánh sáng chiếu bóng lên tường động. Với tù nhân, những bóng đó là toàn bộ thực tại.',
             'Behind them was fire and moving puppet figures — the light casting shadows on the cave wall. For the prisoners, those shadows were all of reality.'),
            ('Một người được thả ra, chịu đựng đau mắt, dần thích nghi với ánh sáng thật, thấy cây cối, người, cuối cùng thấy mặt trời.',
             'One prisoner is freed, endures the pain of his eyes, gradually adapts to real light, sees trees, people, finally sees the sun.'),
            ('Khi trở lại hang để dẫn những người khác ra, anh bị mù trước bóng tối và bị những người còn lại chế giễu, thậm chí muốn giết.',
             'When he returns to the cave to lead others out, he is blinded in the darkness and mocked by those remaining, who even want to kill him.'),
            ('Plato hỏi: "Chúng ta có đang nhìn vào bóng và tưởng đó là thực không? Và người cố chỉ cho ta thấy thực tại — ta có đang giết họ không?"',
             'Plato asks: "Are we looking at shadows and thinking that is reality? And the person trying to show us reality — are we killing them?"'),
        ],
        'lesson_vn': 'Hầu hết điều chúng ta tin là "thực" chỉ là bóng của thực tại sâu hơn. Hành trình hướng đến sự thật đòi hỏi đau đớn, kiên nhẫn, và sẵn sàng từ bỏ những gì quen thuộc.',
        'lesson_en': 'Most of what we believe is "real" is only a shadow of a deeper reality. The journey toward truth requires pain, patience, and willingness to give up the familiar.',
    },
    {
        'title_vn': 'Hai Loại Nhận Thức — Ý Kiến Và Tri Thức',
        'title_en': 'Two Kinds of Knowing — Opinion and Knowledge',
        'pairs': [
            ('Plato phân biệt rõ giữa "doxa" — ý kiến, và "episteme" — tri thức thực sự.',
             'Plato drew a clear distinction between "doxa" — opinion, and "episteme" — genuine knowledge.'),
            ('"Ý kiến có thể đúng hoặc sai, thay đổi tùy hoàn cảnh. Tri thức thực sự là về những thực thể vĩnh hằng không thay đổi — Hình thái của Tốt, Đẹp, Công bằng."',
             '"Opinion can be right or wrong, changing with circumstances. Genuine knowledge is of eternal unchanging entities — the Forms of the Good, the Beautiful, the Just."'),
            ('Học trò hỏi: "Tại sao điều đó quan trọng?"',
             'A student asked: "Why does that matter?"'),
            ('"Vì khi ta ra quyết định dựa trên ý kiến — cảm xúc, thành kiến, thông tin không đầy đủ — ta thường sai. Nhà lãnh đạo tốt phải tìm kiếm tri thức thực sự, không phải ý kiến đám đông."',
             '"Because when we make decisions based on opinion — emotions, prejudice, incomplete information — we are often wrong. A good leader must seek genuine knowledge, not the opinion of the crowd."'),
            ('Đây là lý do Plato tranh luận rằng triết gia — người yêu tri thức — nên lãnh đạo.',
             'This is why Plato argued that the philosopher — the lover of knowledge — should lead.'),
        ],
        'lesson_vn': 'Hãy phân biệt giữa điều bạn thực sự biết và điều bạn chỉ nghĩ là đúng. Quyết định quan trọng đòi hỏi tri thức thực sự — không chỉ cảm giác hoặc ý kiến.',
        'lesson_en': 'Distinguish between what you truly know and what you merely think is true. Important decisions require genuine knowledge — not just feeling or opinion.',
    },
    {
        'title_vn': 'Linh Hồn Ba Phần — Lý Trí, Khí Chất Và Ham Muốn',
        'title_en': 'The Three-Part Soul — Reason, Spirit, and Appetite',
        'pairs': [
            ('Plato dùng hình ảnh người đánh xe với hai con ngựa để mô tả linh hồn con người.',
             'Plato used the image of a charioteer with two horses to describe the human soul.'),
            ('"Người đánh xe là Lý Trí — phần hiểu biết và ra quyết định đúng. Một con ngựa thuần chủng đẹp là Khí Chất — danh dự, dũng cảm, tự trọng. Con ngựa xấu xí và bướng bỉnh là Ham Muốn — đói, khát, dục vọng."',
             '"The charioteer is Reason — the part that understands and makes right decisions. One noble horse is Spirit — honor, courage, self-respect. The ugly, unruly horse is Appetite — hunger, thirst, desire."'),
            ('"Linh hồn khỏe mạnh là linh hồn trong đó Lý Trí điều khiển, được Khí Chất hỗ trợ, giữ Ham Muốn trong vòng kiểm soát."',
             '"A healthy soul is one in which Reason is in control, supported by Spirit, keeping Appetite within bounds."'),
            ('Học trò hỏi: "Nhưng Ham Muốn có hoàn toàn xấu không?"',
             'A student asked: "But is Appetite entirely bad?"'),
            ('"Không — nó cần thiết cho sự sống. Nhưng khi nó nắm quyền lãnh đạo linh hồn, người đó mất tự do thực sự — họ bị nô lệ bởi ham muốn của mình."',
             '"No — it is necessary for life. But when it seizes leadership of the soul, the person loses true freedom — they are enslaved by their own desires."'),
        ],
        'lesson_vn': 'Sự tự do thực sự không phải làm bất cứ điều gì bạn muốn làm — mà là khả năng lý trí điều khiển cuộc sống của bạn thay vì ham muốn bốc đồng.',
        'lesson_en': 'True freedom is not doing whatever you want to do — it is the capacity of reason to direct your life rather than impulsive desires.',
    },
    {
        'title_vn': 'Triết Gia Vương — Người Biết Cái Tốt Nên Lãnh Đạo',
        'title_en': 'The Philosopher King — One Who Knows the Good Should Lead',
        'pairs': [
            ('Plato tranh luận trong "Nước Cộng Hòa": xã hội tốt nhất là xã hội do các triết gia lãnh đạo — người đã có tri thức về Cái Tốt.',
             'Plato argued in "The Republic": the best society is one led by philosophers — those who have knowledge of the Good.'),
            ('"Nếu người mù dẫn đường, cả đoàn sẽ rơi xuống hố. Nếu người chỉ quan tâm đến lợi ích riêng cai trị, dân sẽ bị bóc lột. Chỉ người hiểu rõ cái Tốt mới có thể cai trị vì lợi ích của tất cả."',
             '"If the blind lead the way, the whole group falls into a ditch. If those who care only for their own benefit rule, the people will be exploited. Only those who understand the Good can rule for the benefit of all."'),
            ('Glaucon phản bác: "Nhưng người triết gia không muốn cai trị — họ muốn ở lại trong tri thức."',
             'Glaucon objected: "But philosophers do not want to rule — they want to remain in knowledge."'),
            ('Plato đồng ý: "Đúng vậy — và đó là lý do họ phù hợp để lãnh đạo hơn những người khao khát quyền lực."',
             'Plato agreed: "Exactly — and that is why they are more suited to lead than those who crave power."'),
            ('Lịch sử thường xác nhận: những người khao khát quyền lực ít phù hợp nhất để nắm giữ nó.',
             'History often confirms: those who crave power are the least suited to hold it.'),
        ],
        'lesson_vn': 'Hãy hoài nghi với người quá khao khát quyền lực. Lãnh đạo tốt nhất thường là người nắm giữ quyền lực như một trách nhiệm, không phải như phần thưởng.',
        'lesson_en': 'Be wary of those who crave power too intensely. The best leaders often hold power as a responsibility, not as a reward.',
    },
    {
        'title_vn': 'Hình Thái Của Cái Đẹp — Tình Yêu Dẫn Đến Trí Tuệ',
        'title_en': 'The Form of Beauty — Love Leads to Wisdom',
        'pairs': [
            ('Trong Symposium, Plato kể lại Socrates thuật lại lời dạy của bà Diotima về tình yêu.',
             'In the Symposium, Plato recounts Socrates recounting Diotima\'s teaching on love.'),
            ('"Người được dẫn dắt đúng trong tình yêu bắt đầu bằng yêu một thân thể đẹp. Rồi nhận ra: vẻ đẹp trong thân xác này giống với vẻ đẹp trong thân xác khác — nên yêu vẻ đẹp trong tất cả thân thể đẹp."',
             '"The one properly guided in love begins by loving one beautiful body. Then realizes: the beauty in this body is akin to the beauty in another — so he loves the beauty in all beautiful bodies."'),
            ('"Rồi nhận ra vẻ đẹp tâm hồn cao quý hơn vẻ đẹp thân xác. Rồi yêu vẻ đẹp trong hành động và tri thức. Cuối cùng nhìn thấy cái Đẹp thuần túy — vĩnh hằng, không thay đổi, không pha trộn."',
             '"Then recognizes beauty of soul as nobler than physical beauty. Then loves beauty in actions and knowledge. Finally beholds pure Beauty — eternal, unchanging, unmixed."'),
            ('"Đây là cuộc đời đáng sống — khi người ta chiêm ngưỡng Cái Đẹp thuần túy."',
             '"This is the life worth living — when a person contemplates pure Beauty."'),
        ],
        'lesson_vn': 'Tình yêu ở dạng thấp nhất là ham muốn thể xác. Ở dạng cao nhất, nó là sự khám phá và yêu mến Cái Đẹp, Cái Tốt, và Cái Thực — những nguyên lý không thay đổi của thực tại.',
        'lesson_en': 'Love in its lowest form is physical desire. In its highest form, it is the discovery and love of Beauty, Goodness, and Truth — the unchanging principles of reality.',
    },
    {
        'title_vn': 'Công Bằng Là Khi Mỗi Phần Làm Đúng Việc Của Mình',
        'title_en': 'Justice Is When Each Part Does Its Proper Work',
        'pairs': [
            ('Plato định nghĩa công lý không phải về hình phạt hay phần thưởng — mà là về trật tự và chức năng.',
             'Plato defined justice not as punishment or reward — but as order and function.'),
            ('"Trong thành phố tốt: các triết gia cai trị, chiến binh bảo vệ, thợ thủ công sản xuất — mỗi người làm điều mình giỏi nhất. Đó là công bằng."',
             '"In a just city: philosophers rule, warriors protect, craftsmen produce — each doing what they do best. That is justice."'),
            ('"Trong linh hồn tốt: Lý Trí lãnh đạo, Khí Chất hỗ trợ, Ham Muốn phục tùng. Đó là cũng là công bằng."',
             '"In a just soul: Reason leads, Spirit supports, Appetite obeys. That too is justice."'),
            ('Bất công là khi thứ thấp hơn cai trị thứ cao hơn — khi Ham Muốn chiến thắng Lý Trí, khi mị dân chiến thắng triết nhân.',
             'Injustice is when the lower rules the higher — when Appetite defeats Reason, when the demagogue defeats the philosopher.'),
            ('Học trò hỏi: "Vậy người hoàn toàn bất công — người bạo chúa — sống hạnh phúc không?" Plato trả lời: "Không bao giờ. Người bạo chúa là nô lệ của ham muốn tồi tệ nhất của mình."',
             'A student asked: "Then does the completely unjust person — the tyrant — live happily?" Plato replied: "Never. The tyrant is a slave to his own worst desires."'),
        ],
        'lesson_vn': 'Khi bạn để phần thấp nhất của mình lãnh đạo — ham muốn tức thời, cảm xúc bốc đồng — bạn đang sống theo kiểu bạo chúa bên trong. Lý Trí phải điều khiển để bạn trải nghiệm tự do thực sự.',
        'lesson_en': 'When you let your lowest part lead — immediate desire, impulsive emotion — you are living as an inner tyrant. Reason must be in command for you to experience true freedom.',
    },
    {
        'title_vn': 'Học Nhớ Lại — Tri Thức Là Ký Ức Của Linh Hồn',
        'title_en': 'Learning as Recollection — Knowledge Is the Soul\'s Memory',
        'pairs': [
            ('Plato đề xuất lý thuyết độc đáo: "Linh hồn đã tồn tại trước khi sinh ra. Trong cõi trời, nó nhìn thấy Hình Thái vĩnh hằng — Tốt, Đẹp, Công bằng. Khi sinh vào thân xác, nó quên đi."',
             'Plato proposed a unique theory: "The soul existed before birth. In the realm above, it beheld the eternal Forms — Goodness, Beauty, Justice. When born into a body, it forgets."'),
            ('"Học là nhớ lại điều mình đã biết — không phải tiếp nhận điều hoàn toàn mới."',
             '"Learning is recollecting what you already knew — not receiving what is entirely new."'),
            ('Ông chứng minh điều này bằng cách dạy một đứa trẻ nô lệ không được học — và thông qua câu hỏi thuần túy, trẻ "tự mình tìm ra" định lý hình học.',
             'He demonstrated this by questioning an uneducated slave boy — and through pure questioning, the boy "found for himself" a geometric theorem.'),
            ('Dù lý thuyết linh hồn có vẻ lạ, ý tưởng cốt lõi vẫn có giá trị: mỗi người có tiềm năng tri thức lớn hơn họ nhận ra — và giáo dục giỏi là đánh thức tiềm năng đó, không phải nhồi nhét từ bên ngoài vào.',
             'Though the soul theory seems unusual, the core idea remains valuable: each person has more intellectual potential than they realize — and good education awakens that potential, rather than stuffing it in from the outside.'),
        ],
        'lesson_vn': 'Giáo dục tốt nhất không phải truyền thêm thông tin — mà là khơi dậy trí tuệ tiềm ẩn đã có sẵn trong người học.',
        'lesson_en': 'The best education does not transmit more information — it awakens the latent intelligence already present in the learner.',
    },
    {
        'title_vn': 'Plato Thất Bại Với Dionysius — Triết Gia Gặp Thực Tế Quyền Lực',
        'title_en': 'Plato\'s Failure with Dionysius — The Philosopher Meets the Reality of Power',
        'pairs': [
            ('Plato hai lần đến Syracuse để thuyết phục bạo chúa Dionysius trở thành triết gia-vương.',
             'Plato traveled to Syracuse twice to persuade the tyrant Dionysius to become a philosopher-king.'),
            ('Lần đầu, ông bị bán làm nô lệ bởi Dionysius nổi giận. Bạn bè phải mua chuộc để ông được thả.',
             'The first time, he was sold into slavery by an angered Dionysius. Friends had to ransom his freedom.'),
            ('Lần thứ hai, Dionysius hứa thực hành triết học nhưng thực ra chỉ muốn học thuật như trang sức quyền lực.',
             'The second time, Dionysius promised to practice philosophy but really only wanted learning as an ornament of power.'),
            ('Plato về Athens thất vọng. Học trò Aristotle sau này nhận xét: "Thầy Plato ơi, lý tưởng là cần thiết. Nhưng để thay đổi trật tự hiện hữu, ta phải bắt đầu từ trật tự hiện hữu."',
             'Plato returned to Athens disappointed. His student Aristotle would later observe: "Dear Plato, ideals are necessary. But to change the existing order, we must begin from the existing order."'),
            ('Câu chuyện này là bài học về khoảng cách giữa triết học và chính trị thực tế.',
             'This story is a lesson on the gap between philosophy and real politics.'),
        ],
        'lesson_vn': 'Lý tưởng quan trọng — nhưng lý tưởng không tiếp đất không thay đổi được gì. Người muốn cải tạo thế giới phải hiểu thế giới như nó đang là, không chỉ như ta muốn nó là.',
        'lesson_en': 'Ideals matter — but ideals that do not touch ground change nothing. Those who want to transform the world must understand the world as it is, not only as we wish it to be.',
    },
    {
        'title_vn': 'Nước Công Hòa Lý Tưởng — Và Người Sẽ Không Bao Giờ Đọc Nó',
        'title_en': 'The Ideal Republic — And the People Who Will Never Read It',
        'pairs': [
            ('Plato viết "Nước Cộng Hòa" — một trong những tác phẩm triết học vĩ đại nhất lịch sử nhân loại.',
             'Plato wrote "The Republic" — one of the greatest philosophical works in human history.'),
            ('Nhưng ông biết rõ: những người cần đọc nó nhất — những kẻ bạo quyền, tham lam, ích kỷ — sẽ không bao giờ đọc một dòng.',
             'But he knew clearly: those who most need to read it — the tyrannical, the greedy, the selfish — will never read a line.'),
            ('Ông hỏi học trò: "Vậy tại sao ta viết?" Sau đó trả lời chính mình: "Không phải để thuyết phục kẻ xấu. Mà để chỉ đường cho người tốt. Và để mỗi người đọc có thể xây dựng nước cộng hòa lý tưởng trong chính tâm hồn mình."',
             'He asked his students: "Then why do I write?" Then answered himself: "Not to persuade the bad. But to show the way to the good. And so each reader can build the ideal republic within their own soul."'),
            ('"Nước cộng hòa quan trọng nhất không phải nước nào trên bản đồ — mà là trật tự trong tâm hồn người đọc sau khi gấp sách lại."',
             '"The most important republic is not one on any map — it is the order within the reader\'s soul after closing the book."'),
        ],
        'lesson_vn': 'Ý tưởng vĩ đại không thay đổi thế giới ngay lập tức — nhưng chúng thay đổi từng cá nhân đọc và suy nghĩ về chúng. Và qua từng cá nhân, chúng thay đổi thế giới.',
        'lesson_en': 'Great ideas do not change the world immediately — but they change each individual who reads and thinks about them. And through each individual, they change the world.',
    },
    {
        'title_vn': 'Học Viện Athens — Vườn Ươm Của Văn Minh Phương Tây',
        'title_en': 'The Academy of Athens — Nursery of Western Civilization',
        'pairs': [
            ('Sau khi trở về từ Syracuse, Plato thành lập Học Viện — trường đại học đầu tiên trong lịch sử phương Tây, hoạt động suốt 900 năm cho đến khi bị đóng cửa vào năm 529 sau Công nguyên.',
             'After returning from Syracuse, Plato founded the Academy — the first university in Western history, operating for 900 years until it was closed in 529 CE.'),
            ('Ở đó, ông dạy không phải bằng bài giảng mà bằng đối thoại và tranh luận — theo tinh thần của Socrates.',
             'There, he taught not through lectures but through dialogue and debate — in the spirit of Socrates.'),
            ('Học trò nổi tiếng nhất: Aristotle, đến từ Macedonia và học ở Học Viện 20 năm.',
             'His most famous student: Aristotle, who came from Macedonia and studied at the Academy for 20 years.'),
            ('"Ta yêu thầy Plato," Aristotle sau này nói, "nhưng ta yêu sự thật hơn." Rồi ông rời Học Viện để xây dựng triết học của riêng mình.',
             '"I love Plato," Aristotle would later say, "but I love truth more." He then left the Academy to build his own philosophy.'),
            ('Đây là hình mẫu đẹp nhất của giáo dục: học trò được dạy để tự suy nghĩ và cuối cùng vượt qua thầy.',
             'This is the finest model of education: students are taught to think for themselves and ultimately to surpass their teacher.'),
        ],
        'lesson_vn': 'Thầy giáo vĩ đại nhất không phải người học trò luôn đồng ý — mà là người học trò tìm thấy đủ nền tảng để xây dựng tư tưởng riêng vượt qua thầy.',
        'lesson_en': 'The greatest teacher is not one whose students always agree — but one whose students find enough foundation to build their own thought that surpasses the teacher\'s.',
    },
]

# ============================================================
# CHƯƠNG 8: Aristotle — Trung Dung, Hạnh Phúc Thực, Bạn Bè
# ============================================================
ch08 = [
    {
        'title_vn': 'Eudaimonia — Hạnh Phúc Thực Không Phải Cảm Giác',
        'title_en': 'Eudaimonia — True Happiness Is Not a Feeling',
        'pairs': [
            ('Aristotle bắt đầu Đạo Đức Học Nicomachean bằng quan sát: "Mọi nghệ thuật, điều tra, hành động và theo đuổi đều nhắm đến một điều tốt nào đó." Câu hỏi là: điều tốt tối cao là gì?',
             'Aristotle began the Nicomachean Ethics with the observation: "Every art, inquiry, action and pursuit aims at some good." The question is: what is the highest good?'),
            ('"Mọi người đều đồng ý tên của nó: Eudaimonia — thịnh vượng của tâm hồn, hay sống tốt và làm tốt. Nhưng người ta bất đồng về nội dung của nó."',
             '"Everyone agrees on its name: Eudaimonia — flourishing of the soul, or living well and doing well. But people disagree about its content."'),
            ('"Người nghèo nói nó là giàu có. Người bệnh nói nó là sức khỏe. Người giàu nói nó là danh tiếng."',
             '"The poor say it is wealth. The sick say it is health. The wealthy say it is honor."'),
            ('"Nhưng những thứ đó chỉ là điều kiện cho eudaimonia — không phải chính nó. Eudaimonia là hoạt động của linh hồn phù hợp với đức hạnh — sống theo bản chất tốt nhất của mình."',
             '"But those are only conditions for eudaimonia — not eudaimonia itself. Eudaimonia is the activity of the soul in accordance with virtue — living according to one\'s best nature."'),
        ],
        'lesson_vn': 'Hạnh phúc không phải trạng thái cảm xúc — mà là chất lượng của cuộc sống bạn đang sống. Sống đúng với phiên bản tốt nhất của bản thân mình: đó là hạnh phúc thực.',
        'lesson_en': 'Happiness is not an emotional state — it is the quality of the life you are living. Living true to the best version of yourself: that is true happiness.',
    },
    {
        'title_vn': 'Đức Hạnh Là Thói Quen — Không Phải Hành Động Đơn Lẻ',
        'title_en': 'Virtue Is Habit — Not a Single Act',
        'pairs': [
            ('Aristotle phân biệt rõ: "Chúng ta không vì biết điều tốt mà trở nên tốt — chúng ta trở nên tốt bằng cách thực hành điều tốt."',
             'Aristotle drew a clear distinction: "We do not become good by knowing the good — we become good by practicing the good."'),
            ('"Con người trở thành người công bằng bằng cách làm việc công bằng, trở thành người tự kiềm chế bằng cách tự kiềm chế, trở thành người dũng cảm bằng cách làm những việc dũng cảm."',
             '"A man becomes just by doing just acts, temperate by doing temperate acts, courageous by performing courageous acts."'),
            ('Học trò hỏi: "Nhưng nếu con chưa có đức hạnh, làm sao con thực hành nó được?"',
             'A student asked: "But if I do not yet have the virtue, how can I practice it?"'),
            ('"Bắt đầu bằng cách hành động như thể bạn đã có đức hạnh đó. Lúc đầu khó, nhưng dần dần thành thói quen. Và thói quen trở thành bản chất. Đó là cách đức hạnh được sinh ra."',
             '"Begin by acting as if you already had that virtue. At first it is difficult, but gradually it becomes habit. And habit becomes character. That is how virtue is born."'),
            ('Chúng ta là những gì chúng ta liên tục làm. Sự xuất sắc không phải hành động — mà là thói quen.',
             'We are what we repeatedly do. Excellence is not an act — it is a habit.'),
        ],
        'lesson_vn': 'Đừng chờ đến khi bạn "cảm thấy" dũng cảm để hành động dũng cảm. Hãy hành động dũng cảm — cảm giác sẽ theo sau. Đức hạnh là thứ bạn tập luyện, không phải thứ bạn đột nhiên có.',
        'lesson_en': 'Do not wait until you "feel" courageous to act courageously. Act courageously — the feeling will follow. Virtue is something you practice, not something you suddenly have.',
    },
    {
        'title_vn': 'Trung Dung — Đức Hạnh Nằm Giữa Hai Thái Cực',
        'title_en': 'The Golden Mean — Virtue Lies Between Two Extremes',
        'pairs': [
            ('Aristotle quan sát rằng mỗi đức hạnh nằm giữa hai thái cực — thái quá và thiếu hụt.',
             'Aristotle observed that every virtue lies between two extremes — excess and deficiency.'),
            ('"Lòng dũng cảm nằm giữa hèn nhát (thiếu) và liều lĩnh (thái quá). Hào phóng nằm giữa keo kiệt và hoang phí. Tự trọng nằm giữa hèn hạ và kiêu ngạo."',
             '"Courage lies between cowardice (deficiency) and recklessness (excess). Generosity lies between miserliness and prodigality. Dignity lies between servility and arrogance."'),
            ('"Trung dung không phải điểm giữa toán học — nó là điểm đúng theo hoàn cảnh và theo người. Lượng thức ăn vừa đủ cho Milo lực sĩ không phải lượng vừa đủ cho người mới bắt đầu tập."',
             '"The mean is not a mathematical midpoint — it is the right point relative to the situation and the person. The proper amount of food for Milo the athlete is not the proper amount for someone beginning training."'),
            ('Đây là tại sao không có quy tắc đạo đức đơn giản nào phù hợp mọi hoàn cảnh — cần có sự khôn ngoan thực tế để biết trung dung là bao nhiêu trong từng tình huống cụ thể.',
             'This is why no simple moral rule fits all circumstances — practical wisdom is needed to know where the mean lies in each specific situation.'),
        ],
        'lesson_vn': 'Đừng hỏi "tôi có thể dũng cảm đến mức nào?" — hãy hỏi "dũng cảm đúng mức trong hoàn cảnh này là như thế nào?" Đức hạnh đòi hỏi sự phán đoán, không chỉ tuân theo quy tắc.',
        'lesson_en': 'Do not ask "how brave can I be?" — ask "what is the right degree of bravery in this situation?" Virtue requires judgment, not merely following rules.',
    },
    {
        'title_vn': 'Ba Loại Tình Bạn — Và Chỉ Một Loại Giữ Lâu',
        'title_en': 'Three Kinds of Friendship — And Only One Endures',
        'pairs': [
            ('Aristotle phân tích tình bạn sâu sắc hơn bất kỳ triết gia nào trước ông.',
             'Aristotle analyzed friendship more deeply than any philosopher before him.'),
            ('"Có ba loại tình bạn: tình bạn vì lợi ích, tình bạn vì vui vẻ, và tình bạn vì đức hạnh."',
             '"There are three kinds of friendship: friendship of utility, friendship of pleasure, and friendship of virtue."'),
            ('"Tình bạn vì lợi ích chấm dứt khi lợi ích chấm dứt. Tình bạn vì vui vẻ chấm dứt khi vui vẻ chấm dứt. Tình bạn vì đức hạnh là tình bạn hoàn hảo — vì nó vì chính người kia, không vì điều người kia mang lại cho ta."',
             '"Friendship of utility ends when the utility ends. Friendship of pleasure ends when the pleasure ends. Friendship of virtue is perfect friendship — because it is for the sake of the other person themselves, not for what they bring us."'),
            ('"Người yêu bạn vì đức hạnh của bạn cũng yêu bạn vì lợi ích và vui vẻ — nhưng ngược lại không đúng."',
             '"One who loves you for your virtue also loves you for utility and pleasure — but the reverse is not true."'),
            ('Tình bạn đức hạnh đòi hỏi thời gian, gần gũi, và cùng sống qua thử thách — không thể có nhiều người bạn như vậy.',
             'Virtue friendship requires time, proximity, and living through challenges together — one cannot have many such friends.'),
        ],
        'lesson_vn': 'Nhìn vào bạn bè của bạn và hỏi: họ đang ở đây vì điều bạn mang lại cho họ, hay vì họ thực sự quan tâm đến bạn — và bạn thực sự quan tâm đến họ? Loại sau là hiếm và đáng quý nhất.',
        'lesson_en': 'Look at your friends and ask: are they here because of what you bring them, or because they genuinely care about you — and you genuinely care about them? The latter kind is rarest and most precious.',
    },
    {
        'title_vn': 'Con Người Là Động Vật Chính Trị',
        'title_en': 'Man Is a Political Animal',
        'pairs': [
            ('Aristotle tuyên bố: "Con người tự bản chất là động vật chính trị — sống trong thành phố." Người sống bên ngoài cộng đồng hoặc là thần hoặc là thú vật.',
             'Aristotle declared: "Man is by nature a political animal — meant to live in a polis." One living outside community is either a god or a beast.'),
            ('"Người không thể sống một mình và vẫn là người hoàn toàn. Ta cần người khác không chỉ vì sự sống còn — mà vì sự phát triển."',
             '"A person cannot live alone and still be fully human. We need others not only for survival — but for flourishing."'),
            ('Học trò hỏi: "Thưa thầy, nhưng sống với người khác thường đau khổ lắm."',
             'A student said: "Master, but living with others is often very painful."'),
            ('"Đúng vậy," Aristotle đồng ý. "Nhưng phát triển thực sự chỉ xảy ra trong ma sát với thực tại — và thực tại quan trọng nhất là những người xung quanh ta. Cô đơn hoàn toàn không phải tự do — đó là sự thiếu hụt."',
             '"That is true," Aristotle agreed. "But genuine flourishing only happens in friction with reality — and the most important reality is the people around us. Complete solitude is not freedom — it is deficiency."'),
        ],
        'lesson_vn': 'Bạn không thể phát triển đầy đủ trong cô đơn. Những mối quan hệ khó khăn — gia đình, bạn bè, đồng nghiệp — là chất liệu mà từ đó đức hạnh và trí tuệ được rèn giũa.',
        'lesson_en': 'You cannot fully flourish in solitude. Difficult relationships — family, friends, colleagues — are the material from which virtue and wisdom are forged.',
    },
    {
        'title_vn': 'Phronesis — Trí Tuệ Thực Hành',
        'title_en': 'Phronesis — Practical Wisdom',
        'pairs': [
            ('Aristotle mô tả một loại trí tuệ mà không cuốn sách nào dạy được: phronesis — khôn ngoan thực hành.',
             'Aristotle described a kind of intelligence no book can teach: phronesis — practical wisdom.'),
            ('"Nó là khả năng nhìn rõ điều gì tốt trong từng hoàn cảnh cụ thể và hành động phù hợp."',
             '"It is the ability to clearly see what is good in each specific circumstance and to act accordingly."'),
            ('"Không phải mọi quy tắc đạo đức đều áp dụng được trong mọi tình huống. Người có phronesis biết quy tắc nào áp dụng như thế nào trong từng hoàn cảnh."',
             '"Not every moral rule applies in every situation. The person with phronesis knows which rule applies how in each circumstance."'),
            ('Học trò hỏi: "Làm sao ta có được phronesis?" "Bằng kinh nghiệm suy ngẫm — không chỉ sống qua kinh nghiệm, mà còn suy nghĩ sâu về những gì đã xảy ra."',
             'A student asked: "How do we acquire phronesis?" "Through reflective experience — not just living through experience, but also thinking deeply about what happened."'),
            ('Sự khác biệt giữa người già khôn ngoan và người già không rút ra bài học: cả hai đều có nhiều kinh nghiệm, nhưng chỉ một người liên tục suy ngẫm về chúng.',
             'The difference between a wise elder and one who draws no lessons: both have much experience, but only one continuously reflects on it.'),
        ],
        'lesson_vn': 'Kinh nghiệm không tự động tạo ra sự khôn ngoan — sự suy ngẫm có hệ thống về kinh nghiệm mới làm điều đó. Hãy dành thời gian không chỉ để trải nghiệm mà còn để suy nghĩ về những gì đã xảy ra.',
        'lesson_en': 'Experience does not automatically create wisdom — systematic reflection on experience does. Take time not just to have experiences but to think about what happened.',
    },
    {
        'title_vn': 'Mọi Thứ Có Mục Đích — Teleology',
        'title_en': 'Everything Has a Purpose — Teleology',
        'pairs': [
            ('Aristotle quan sát: "Hạt sồi có mục đích trở thành cây sồi. Cây sồi đang thực hiện đầy đủ bản chất hạt sồi."',
             'Aristotle observed: "An acorn has the purpose of becoming an oak tree. An oak tree is the full actualization of the acorn\'s nature."'),
            ('"Con người cũng có bản chất — và hạnh phúc là khi ta trở thành người hoàn toàn theo bản chất đó."',
             '"People also have a nature — and happiness is fully becoming that person according to that nature."'),
            ('"Khả năng phân biệt lý trí là khả năng của người — không phải con vật hay thần. Vì vậy sống theo lý trí là sống hoàn toàn như người."',
             '"The capacity for rational discernment is uniquely human — not of animals or gods. Therefore, living according to reason is living fully as a human."'),
            ('Học trò hỏi: "Nhưng nếu bản chất ta không tốt thì sao?" Aristotle trả lời: "Bản chất của con người là tốt — vấn đề là ta đã phát triển đúng không. Cây sồi trồng trong điều kiện xấu không đạt được bản chất đầy đủ của nó — nhưng điều đó không nghĩa là hạt sồi vốn xấu."',
             'A student asked: "But what if our nature is not good?" Aristotle replied: "Human nature is good — the issue is whether we have developed properly. An oak tree grown in poor conditions does not achieve its full nature — but that does not mean the acorn was inherently bad."'),
        ],
        'lesson_vn': 'Hãy hỏi: bản chất tốt nhất của mình là gì? Phiên bản đầy đủ nhất của mình trông như thế nào? Rồi hãy sống theo hướng đó — đó là cái Aristotle gọi là eudaimonia.',
        'lesson_en': 'Ask: what is the best nature within me? What does the fullest version of myself look like? Then live in that direction — that is what Aristotle called eudaimonia.',
    },
    {
        'title_vn': 'Aristotle Dạy Alexander Đại Đế',
        'title_en': 'Aristotle Teaches Alexander the Great',
        'pairs': [
            ('Năm 343 trước Công nguyên, Aristotle nhận lời làm gia sư cho cậu bé 13 tuổi Alexander — người sau này trở thành Alexander Đại Đế.',
             'In 343 BCE, Aristotle accepted the position of tutor to the 13-year-old Alexander — who would become Alexander the Great.'),
            ('Aristotle dạy Alexander logic, khoa học, y học, văn học và triết học — mở ra cho cậu một thế giới tri thức mà không vua nào trước đó được tiếp cận.',
             'Aristotle taught Alexander logic, science, medicine, literature and philosophy — opening for him a world of knowledge no previous king had accessed.'),
            ('Alexander sau này nói: "Ta tôn trọng cha ta Philip vì ta được sống từ ông. Nhưng ta tôn trọng Aristotle vì ta được sống tốt từ ông."',
             'Alexander later said: "I honor my father Philip because I live through him. But I honor Aristotle because I live well through him."'),
            ('Trên mọi chiến dịch, Alexander mang theo bản sao chép tác phẩm Homer do Aristotle chú thích.',
             'On every campaign, Alexander carried a copy of Homer annotated by Aristotle.'),
            ('Tuy nhiên, khi trở thành đại đế, Alexander không luôn làm theo lời thầy — minh chứng rằng tri thức không tự động chuyển hóa thành đức hạnh.',
             'However, as he became a great conqueror, Alexander did not always follow his teacher\'s advice — demonstrating that knowledge does not automatically transform into virtue.'),
        ],
        'lesson_vn': 'Giáo dục tốt cho người ta khả năng chọn đúng — nhưng không đảm bảo họ sẽ chọn đúng. Cuối cùng, đức hạnh vẫn là lựa chọn cá nhân của từng người.',
        'lesson_en': 'Good education gives a person the capacity to choose rightly — but does not guarantee they will choose rightly. In the end, virtue remains each person\'s individual choice.',
    },
    {
        'title_vn': 'Siêu Hình Học — Nguyên Nhân Đầu Tiên Của Mọi Thứ',
        'title_en': 'Metaphysics — The First Cause of Everything',
        'pairs': [
            ('Aristotle đặt câu hỏi mà ít người dám đặt: "Tại sao có cái gì đó chứ không phải không có gì?"',
             'Aristotle asked a question few dare to ask: "Why is there something rather than nothing?"'),
            ('Lý thuyết của ông về bốn nguyên nhân: Nguyên nhân chất liệu (làm từ gì), Hình thức (thiết kế là gì), Hiệu quả (ai làm), và Mục đích (để làm gì).',
             'His theory of four causes: Material cause (what it is made of), Formal (what the design is), Efficient (who made it), and Final cause (what it is for).'),
            ('"Không thể có chuỗi nguyên nhân vô tận. Phải có một nguyên nhân đầu tiên không bị gây ra bởi bất cứ điều gì khác."',
             '"There cannot be an infinite chain of causes. There must be a first cause that is not caused by anything else."'),
            ('Aristotle gọi nguyên nhân đầu tiên này là "Động lực không bị chuyển động" — nguyên lý vĩnh hằng mà qua đó mọi thứ vận động và tồn tại.',
             'Aristotle called this first cause the "Unmoved Mover" — the eternal principle through which all things move and exist.'),
            ('Thánh Thomas Aquinas sau này dùng lập luận này để chứng minh sự tồn tại của Thiên Chúa — minh chứng ảnh hưởng của triết học Hy Lạp lên thần học Kitô giáo.',
             'Saint Thomas Aquinas later used this argument to prove the existence of God — demonstrating the influence of Greek philosophy on Christian theology.'),
        ],
        'lesson_vn': 'Hỏi "tại sao" không bao giờ là vô ích — kể cả khi câu hỏi đó đưa bạn đến những giới hạn của điều con người có thể biết. Đó là ranh giới giữa triết học và sự khiêm tốn của tâm linh.',
        'lesson_en': 'Asking "why" is never useless — even when the question leads you to the limits of what humans can know. That is the boundary between philosophy and spiritual humility.',
    },
    {
        'title_vn': 'Nghệ Thuật Và Bi Kịch — Catharsis',
        'title_en': 'Art and Tragedy — Catharsis',
        'pairs': [
            ('Aristotle bất đồng với thầy Plato về nghệ thuật: Plato muốn đuổi các nhà thơ khỏi nước cộng hòa vì họ kêu gọi cảm xúc hơn lý trí.',
             'Aristotle disagreed with his teacher Plato about art: Plato wanted to expel poets from the republic because they appealed to emotion over reason.'),
            ('"Nhưng bi kịch," Aristotle viết trong Poetics, "thanh tẩy sợ hãi và thương xót thông qua sợ hãi và thương xót."',
             '"But tragedy," Aristotle wrote in the Poetics, "effects the purgation of such emotions, namely fear and pity, through fear and pity."'),
            ('"Khi xem Oedipus đào mù mình, khán giả trải qua sự thương xót và sợ hãi an toàn — và ra về với tâm hồn được thanh tẩy."',
             '"When watching Oedipus blind himself, the audience experiences pity and fear safely — and leaves with the soul purified."'),
            ('Nghệ thuật không làm hỏng con người — nó giúp họ xử lý những cảm xúc sâu nhất theo cách an toàn và có ý nghĩa.',
             'Art does not corrupt people — it helps them process their deepest emotions in a safe and meaningful way.'),
            ('Đây là tại sao văn học và nghệ thuật không phải xa xỉ phẩm — chúng là cần thiết cho sức khỏe tinh thần của con người.',
             'This is why literature and art are not luxuries — they are necessary for human psychological health.'),
        ],
        'lesson_vn': 'Đọc tiểu thuyết, xem kịch, nghe nhạc — những hoạt động này không chỉ giải trí. Chúng giúp bạn xử lý những cảm xúc và kinh nghiệm phức tạp nhất mà cuộc sống mang đến.',
        'lesson_en': 'Reading novels, watching plays, listening to music — these activities do not merely entertain. They help you process the most complex emotions and experiences that life brings.',
    },
]

print("Đang tạo chương 5-8...")

make_chapter('ch05-tuan-tu-giao-duc-cai-hoa', 5,
    'Tuân Tử — Giáo Dục Cải Hóa Và Tu Thân',
    'Xunzi — Education as Transformation and Self-Cultivation', ch05)

make_chapter('ch06-socrates-biet-minh-khong-biet', 6,
    'Socrates — Biết Mình Không Biết Và Đức Hạnh',
    'Socrates — Knowing That You Do Not Know and Virtue', ch06)

make_chapter('ch07-plato-the-gioi-ly-tuong', 7,
    'Plato — Thế Giới Lý Tưởng Và Hang Động',
    'Plato — The World of Ideas and the Cave', ch07)

make_chapter('ch08-aristotle-trung-dung-hanh-phuc', 8,
    'Aristotle — Trung Dung, Hạnh Phúc Thực Và Bạn Bè',
    'Aristotle — The Golden Mean, True Happiness, and Friendship', ch08)

print("Hoàn tất chương 5-8!")
