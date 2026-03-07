#!/usr/bin/env python3
# gen_q7_c.py -- Quyển VII ch09-12: Marcus Aurelius, Epicurus/Diogenes, Mặc Tử/Hàn Phi, Giao Thoa Đông Tây
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
# CHƯƠNG 9: Marcus Aurelius — Khắc Kỷ, Kiểm Soát Bản Thân
# ============================================================
ch09 = [
    {
        'title_vn': 'Chỉ Kiểm Soát Những Gì Thuộc Về Mình',
        'title_en': 'Control Only What Is Yours',
        'pairs': [
            ('Marcus Aurelius, hoàng đế La Mã quyền lực nhất thế giới, mỗi sáng thức dậy và viết vào nhật ký riêng của mình: "Sáng nay ta sẽ gặp những kẻ thô lỗ, vô ơn, kiêu ngạo, dối trá, ganh tị."',
             'Marcus Aurelius, the most powerful Roman emperor in the world, woke each morning and wrote in his private journal: "Today I shall meet rude, ungrateful, arrogant, deceitful, and envious people."'),
            ('"Nhưng ta sẽ không bực bội vì đó không phải lỗi của họ — họ không biết sự khác biệt giữa thiện và ác. Ta thì biết. Và ta sẽ chọn đối xử tử tế."',
             '"But I will not be annoyed, for it is not their fault — they do not know the difference between good and evil. I do. And I will choose to act kindly."'),
            ('Đây là nguyên lý cốt lõi của Chủ Nghĩa Khắc Kỷ: phân biệt rõ ràng giữa những gì trong tầm kiểm soát của ta và những gì không.',
             'This is the core principle of Stoicism: clearly distinguishing between what is within our control and what is not.'),
            ('Trong tầm kiểm soát: suy nghĩ, phán đoán, phản ứng, nỗ lực, giá trị của ta.',
             'Within our control: our thoughts, judgments, responses, efforts, and values.'),
            ('Ngoài tầm kiểm soát: thời tiết, ý kiến người khác, kết quả bầu cử, sức khỏe cơ thể, cái chết.',
             'Outside our control: the weather, others\' opinions, election results, physical health, death.'),
            ('Hầu hết đau khổ của con người đến từ việc cố kiểm soát những thứ ngoài tầm tay — và bỏ bê những gì thực sự thuộc về mình.',
             'Most human suffering comes from trying to control what is beyond reach — and neglecting what truly belongs to us.'),
        ],
        'lesson_vn': 'Mỗi sáng, hãy hỏi: "Điều tôi đang lo lắng này — có thực sự trong tầm kiểm soát của tôi không?" Nếu không — buông. Nếu có — hành động. Chỉ vậy thôi.',
        'lesson_en': 'Each morning, ask: "Is this thing I am worrying about truly within my control?" If not — release it. If yes — act. That is all.',
    },
    {
        'title_vn': 'Memento Mori — Hãy Nhớ Rằng Bạn Sẽ Chết',
        'title_en': 'Memento Mori — Remember That You Will Die',
        'pairs': [
            ('Trong các cuộc diễu hành khải hoàn của Đế Quốc La Mã, khi đám đông hò reo mừng chiến thắng, luôn có một người nô lệ đứng sau xe ngựa của viên tướng thắng trận, thì thầm liên tục vào tai ông ta:',
             'In the triumph parades of the Roman Empire, when crowds cheered the victory, there was always a slave standing behind the victorious general\'s chariot, continuously whispering in his ear:'),
            ('"Memento mori" — Hãy nhớ rằng ngươi sẽ chết.',
             '"Memento mori" — Remember that you will die.'),
            ('Marcus Aurelius viết: "Ngươi có thể rời khỏi cuộc đời này ngay lúc này. Hãy để điều đó quyết định những gì ngươi làm, nói, và nghĩ."',
             'Marcus Aurelius wrote: "You could leave life right now. Let that determine what you do, say, and think."'),
            ('Đây không phải tư tưởng bi quan — mà là công cụ tập trung mạnh mẽ nhất.',
             'This is not pessimism — it is the most powerful focusing tool.'),
            ('Khi biết mình hữu hạn, mỗi ngày trở nên quý giá. Khi biết mình sẽ mất tất cả, ta không còn bị trói buộc bởi sĩ diện, tiền tài, danh vọng.',
             'Knowing we are finite, each day becomes precious. Knowing we will lose everything, we are no longer bound by pride, wealth, or fame.'),
            ('Steve Jobs từng nói: "Nhớ rằng tôi sẽ sớm chết là công cụ quan trọng nhất giúp tôi đưa ra những lựa chọn lớn trong cuộc đời." Không phải tình cờ mà ông đã đọc Marcus Aurelius.',
             'Steve Jobs once said: "Remembering that I\'ll be dead soon is the most important tool I\'ve ever encountered to help me make the big choices in life." It was no coincidence that he had read Marcus Aurelius.'),
        ],
        'lesson_vn': 'Hãy để ý thức về sự hữu hạn làm bạn sống trọn vẹn hơn — không phải sợ hãi hơn. Hỏi: "Nếu đây là ngày cuối, tôi có muốn dành thời gian cho điều này không?"',
        'lesson_en': 'Let awareness of finiteness make you live more fully — not more fearfully. Ask: "If this were my last day, would I want to spend time on this?"',
    },
    {
        'title_vn': 'Volta — Trở Về Với Lý Trí',
        'title_en': 'Volta — Return to Reason',
        'pairs': [
            ('Một ngày, người ta mang tin đến cho Marcus Aurelius: kẻ thù phía Đông đang xâm lược, quân đội phản loạn ở phía Bắc, nạn dịch đang tàn phá thành phố.',
             'One day, news was brought to Marcus Aurelius: enemies were invading from the East, armies were revolting in the North, plague was devastating the city.'),
            ('Quan lại trong triều chờ xem hoàng đế sẽ hoảng loạn hay tức giận hay sụp đổ.',
             'Officials at court waited to see whether the emperor would panic, rage, or collapse.'),
            ('Marcus Aurelius ngồi xuống, viết vào sổ tay: "Không ai có thể truyền cho ta điều xấu nếu ta không chấp nhận nó là xấu. Sự kiện bên ngoài không thể chạm đến linh hồn — chỉ phán đoán của ta về chúng mới có thể."',
             'Marcus Aurelius sat down and wrote in his notebook: "No one can give me harm unless I accept it as harm. External events cannot touch the soul — only my judgment of them can."'),
            ('"Vậy thì hãy hành động. Gửi quân đội đến Đông. Đàm phán với miền Bắc. Mở kho lương thực cho dân dịch."',
             '"So then, act. Send the armies East. Negotiate with the North. Open the granaries for the plague-stricken."'),
            ('Đây là "volta" của Marcus Aurelius — khoảnh khắc quay lại với lý trí sau khi cảm xúc đầu tiên dấy lên, thay vì để cảm xúc quyết định hành động.',
             'This was Marcus Aurelius\'s "volta" — the moment of returning to reason after the first emotion arises, instead of letting emotion dictate action.'),
        ],
        'lesson_vn': 'Giữa kích thích và phản ứng, luôn có khoảng trống. Trong khoảng trống đó nằm tự do của bạn. Học cách mở rộng khoảng trống đó.',
        'lesson_en': 'Between stimulus and response, there is always a space. In that space lies your freedom. Learn to widen that space.',
    },
    {
        'title_vn': 'Sympatheia — Tất Cả Đều Liên Kết',
        'title_en': 'Sympatheia — All Is Connected',
        'pairs': [
            ('Marcus Aurelius viết: "Những gì có hại cho đàn ong thì có hại cho ta." Ông nhắc nhở bản thân mỗi ngày rằng con người là động vật xã hội — được tạo ra để sống vì lợi ích của nhau.',
             'Marcus Aurelius wrote: "What is bad for the hive is bad for me." He reminded himself daily that human beings are social animals — made to live for each other\'s benefit.'),
            ('Đây không phải chủ nghĩa xã hội hay chủ nghĩa tập thể — đây là nhận thức về sự thật sinh học và đạo đức: ta phụ thuộc vào nhau.',
             'This is not socialism or collectivism — it is recognition of a biological and moral truth: we depend on one another.'),
            ('"Cái mà dừng cản sự tiến lên lại trở thành con đường tiến lên," Marcus Aurelius viết về những trở ngại.',
             '"What stops action advances action," Marcus Aurelius wrote about obstacles.'),
            ('Một thương nhân mất hàng trong bão biển. Ông có thể than thở. Thay vào đó ông nghĩ: "Bài học nào bão này đang dạy ta về việc đa dạng hóa hàng hóa?"',
             'A merchant lost his goods in a sea storm. He could lament. Instead he thought: "What lesson is this storm teaching me about diversifying my cargo?"'),
            ('Mỗi trở ngại đều chứa trong nó thứ gì đó để học. Mỗi thất bại là huấn luyện viên cứng nhất ta sẽ gặp.',
             'Every obstacle contains within it something to learn. Every failure is the hardest coach we will ever meet.'),
        ],
        'lesson_vn': 'Hãy thay "Tại sao điều này xảy ra với TÔI?" bằng "Điều này đang dạy tôi điều gì?" Câu hỏi thứ hai mở cửa. Câu hỏi thứ nhất đóng cửa.',
        'lesson_en': 'Replace "Why is this happening to ME?" with "What is this teaching me?" The second question opens doors. The first closes them.',
    },
    {
        'title_vn': 'Premeditatio Malorum — Hình Dung Điều Xấu Nhất',
        'title_en': 'Premeditatio Malorum — Premeditate the Worst',
        'pairs': [
            ('Người Khắc Kỷ thực hành điều kỳ lạ: mỗi sáng họ hình dung điều tồi tệ nhất có thể xảy ra trong ngày.',
             'The Stoics practiced something unusual: each morning they visualized the worst things that could happen that day.'),
            ('"Hôm nay ta có thể mất việc. Hôm nay người ta yêu có thể rời bỏ ta. Hôm nay ta có thể bệnh." Rồi họ hỏi: "Nếu điều đó xảy ra, ta có thể đối mặt không? Ta còn giữ được phẩm giá không?"',
             '"Today I might lose my job. Today the one I love might leave. Today I might fall ill." Then they asked: "If that happens, can I bear it? Can I retain my dignity?"'),
            ('Câu trả lời gần như luôn là: có. Và nhận ra điều đó giải phóng họ khỏi nỗi lo âu mơ hồ.',
             'The answer was almost always: yes. And realizing this freed them from vague anxiety.'),
            ('Không phải để bi quan — mà để chuẩn bị tinh thần và nhận ra: ta mạnh hơn ta tưởng.',
             'Not to be pessimistic — but to mentally prepare and recognize: we are stronger than we think.'),
            ('Marcus Aurelius viết về những thứ ta sở hữu: "Đừng nói ta đã mất chúng — hãy nói ta đã trả chúng lại." Mọi thứ là mượn tạm, không phải sở hữu vĩnh viễn.',
             'Marcus Aurelius wrote about the things we possess: "Do not say I have lost them — say I have returned them." Everything is borrowed, not permanently owned.'),
        ],
        'lesson_vn': 'Thay vì tránh né suy nghĩ về điều tồi tệ, hãy đối mặt với nó khi còn bình yên — và nhận ra bạn sẽ ổn. Sự chuẩn bị tinh thần tốt hơn sự phủ nhận.',
        'lesson_en': 'Instead of avoiding thoughts of the worst, face them while at peace — and realize you will be fine. Mental preparation is better than denial.',
    },
    {
        'title_vn': 'Amor Fati — Yêu Mến Số Phận',
        'title_en': 'Amor Fati — Love Your Fate',
        'pairs': [
            ('Marcus Aurelius viết: "Chấp nhận những gì xảy ra với từng sự vật; vì nó đã được xếp đặt cho ngươi, và theo cách này phù hợp với ngươi."',
             'Marcus Aurelius wrote: "Accept the things to which fate binds you and love the people with whom fate brings you together, and do so with all your heart."'),
            ('Đây không phải thụ động hay bất lực — đây là sự nhận thức rằng vũ trụ vận hành theo trật tự vượt quá hiểu biết của ta.',
             'This is not passivity or helplessness — it is the recognition that the universe operates by an order beyond our understanding.'),
            ('Nhà thơ Rainer Maria Rilke viết: "Hãy yêu mến những câu hỏi của bạn." Marcus Aurelius đi xa hơn: "Hãy yêu mến cả những câu trả lời đau đớn."',
             'Poet Rainer Maria Rilke wrote: "Love your questions." Marcus Aurelius went further: "Love even the painful answers."'),
            ('Một người lính mất tay trong chiến trận hỏi Marcus Aurelius: "Làm sao tôi chấp nhận điều này?"',
             'A soldier who lost his hand in battle asked Marcus Aurelius: "How do I accept this?"'),
            ('"Không phải chấp nhận — mà là yêu mến. Bàn tay đó đã hy sinh để bảo vệ Rome. Đó là vinh dự, không phải mất mát." Người lính rời đi với ánh mắt khác.',
             '"Not merely accept — but love it. That hand was sacrificed to protect Rome. That is honor, not loss." The soldier left with different eyes.'),
        ],
        'lesson_vn': '"Amor Fati" không có nghĩa là không hành động để thay đổi hoàn cảnh. Nó có nghĩa là: trong khi thay đổi những gì có thể, hãy yêu mến những gì không thể thay đổi.',
        'lesson_en': '"Amor Fati" does not mean not acting to change circumstances. It means: while changing what can be changed, love what cannot be changed.',
    },
    {
        'title_vn': 'Thiền Định Bằng Hành Động',
        'title_en': 'Meditation Through Action',
        'pairs': [
            ('Marcus Aurelius không chỉ viết triết học — ông sống triết học trong từng giây của cuộc đời hoàng đế bận rộn nhất thế giới.',
             'Marcus Aurelius did not merely write philosophy — he lived it in every moment of his life as the world\'s busiest emperor.'),
            ('Ông cai trị 20 năm liên tiếp trong chiến tranh và dịch bệnh. Ông mất nhiều đứa con. Ông bị phản bội bởi những người thân cận nhất.',
             'He ruled for 20 consecutive years through war and plague. He lost many children. He was betrayed by those closest to him.'),
            ('Nhưng Marcus Aurelius không bao giờ ngừng thực hành: mỗi sáng viết nhật ký, mỗi đêm hỏi: "Hôm nay ta đã làm gì thiện? Đã sai ở đâu? Ngày mai sẽ làm tốt hơn thế nào?"',
             'Yet Marcus Aurelius never stopped his practice: each morning writing in his journal, each night asking: "What good did I do today? Where did I err? How will I do better tomorrow?"'),
            ('Quyển Suy Tưởng không bao giờ được viết để xuất bản — đó là nhật ký cá nhân của một người đang liên tục luyện tập làm người tốt hơn.',
             'The Meditations was never written to be published — it was the private journal of a man continuously practicing being better.'),
            ('Điều đáng kinh ngạc nhất: sau hai mươi năm quyền lực tuyệt đối, ông không hề trở nên độc tài hay tham nhũng. Triết học đã giữ ông lại.',
             'The most remarkable thing: after twenty years of absolute power, he never became tyrannical or corrupt. Philosophy had held him.'),
        ],
        'lesson_vn': 'Triết học không phải để đọc rồi đặt xuống — nó là thực hành hàng ngày. Câu hỏi mỗi đêm: "Hôm nay tôi đã sống đúng với giá trị của mình chưa?"',
        'lesson_en': 'Philosophy is not something to read and set aside — it is daily practice. The nightly question: "Did I live according to my values today?"',
    },
    {
        'title_vn': 'Cái Chết Của Một Hiền Triết Vĩ Đại',
        'title_en': 'The Death of a Great Sage',
        'pairs': [
            ('Năm 180 sau Công Nguyên, Marcus Aurelius biết mình sắp chết vì bệnh dịch trên mặt trận phía Bắc.',
             'In 180 AD, Marcus Aurelius knew he was dying of plague on the northern front.'),
            ('Các tướng lĩnh và quan lại vây quanh, lo lắng về tương lai đế quốc. Ông nhìn họ và nói: "Tại sao các ngươi khóc vì ta? Hãy nghĩ đến dịch bệnh và cái chết chung đang chờ mọi người."',
             'Generals and officials surrounded him, worried about the empire\'s future. He looked at them and said: "Why do you weep for me? Think rather of the pestilence and the common death that awaits everyone."'),
            ('Ông quay về phía người con trai Commodus và nói những lời cuối: "Con hãy là người đàn ông tốt hơn ta."',
             'He turned to his son Commodus and spoke his last words: "Be a better man than I was."'),
            ('Rồi ông quay người vào tường theo nghi thức truyền thống — thân xác đã kiệt sức, nhưng tâm hồn bình thản hoàn toàn.',
             'Then he turned to the wall in the traditional ritual — his body exhausted, but his soul entirely at peace.'),
            ('Hai mươi thế kỷ sau, người ta vẫn đọc nhật ký của ông — không phải vì ông là hoàng đế mạnh nhất thế giới, mà vì ông là người đã thực sự cố gắng sống tốt mỗi ngày.',
             'Twenty centuries later, people still read his journal — not because he was the most powerful emperor in the world, but because he genuinely tried to live well every day.'),
        ],
        'lesson_vn': 'Di sản thực sự của một người không phải những gì họ tích lũy — mà là những gì họ thực hành. Marcus Aurelius nhắc ta: sống tốt từng ngày là di sản đủ.',
        'lesson_en': 'A person\'s true legacy is not what they accumulate — but what they practice. Marcus Aurelius reminds us: living well each day is legacy enough.',
    },
]

# ============================================================
# CHƯƠNG 10: Epicurus & Diogenes — Hạnh Phúc Thật Sự Là Gì?
# ============================================================
ch10 = [
    {
        'title_vn': 'Hạnh Phúc Là Vắng Mặt Của Đau Khổ',
        'title_en': 'Happiness Is the Absence of Pain',
        'pairs': [
            ('Người ta nghĩ Epicurus dạy chủ nghĩa khoái lạc — ẩm thực cao cấp, rượu ngon, hoan lạc xác thịt. Thực ra ông sống trong một khu vườn nhỏ, ăn bánh mì và phô mai, uống nước.',
             'People think Epicurus taught hedonism — fine food, good wine, bodily pleasure. In fact he lived in a small garden, eating bread and cheese, drinking water.'),
            ('Học trò hỏi: "Thưa thầy, thầy không thích những thứ ngon sao?"',
             'A student asked: "Master, do you not enjoy fine things?"'),
            ('"Ta thích," Epicurus trả lời. "Nhưng ta đã học được điều quan trọng hơn: sự vắng mặt của đau khổ — ataraxia — là hạnh phúc cao hơn bất kỳ khoái lạc nào."',
             '"I do," Epicurus replied. "But I have learned something more important: the absence of pain — ataraxia — is a higher happiness than any pleasure."'),
            ('"Người đang đói thì chiếc bánh mì khô là bữa tiệc lớn nhất. Người đã no thì bàn tiệc thịnh soạn nhất cũng nhạt nhẽo."',
             '"For the hungry man, dry bread is the greatest feast. For the full man, the most lavish banquet tastes bland."'),
            ('Epicurus dạy: con người không tìm kiếm khoái lạc — họ tìm kiếm sự thoát khỏi đau khổ. Hiểu điều này, bạn sẽ không còn bị trói buộc bởi tham muốn vô tận.',
             'Epicurus taught: people do not seek pleasure — they seek relief from pain. Understand this, and you will no longer be bound by endless desire.'),
        ],
        'lesson_vn': 'Hãy phân biệt giữa nhu cầu thực sự và mong muốn giả tạo. Nhu cầu thực — ít hơn bạn nghĩ. Mãn nguyện với chúng là hạnh phúc đơn giản nhất và bền vững nhất.',
        'lesson_en': 'Distinguish between genuine needs and fabricated desires. True needs — fewer than you think. Contentment with them is the simplest and most durable happiness.',
    },
    {
        'title_vn': 'Ba Điều Epicurus Dạy Về Hạnh Phúc',
        'title_en': 'Three Things Epicurus Taught About Happiness',
        'pairs': [
            ('Epicurus đúc kết hạnh phúc vào ba thứ: bạn bè tốt, tự do, và thời gian suy nghĩ.',
             'Epicurus distilled happiness into three things: good friends, freedom, and time for reflection.'),
            ('Về bạn bè: "Của tất cả những thứ mà sự khôn ngoan thu thập được để giúp cho hạnh phúc trọn đời, vĩ đại nhất là việc có được tình bạn."',
             'On friendship: "Of all the things which wisdom provides to make us entirely happy, much the greatest is the possession of friendship."'),
            ('Ông lập ra "Khu Vườn" — một cộng đồng triết học bao gồm đàn ông, đàn bà, nô lệ, và tự do dân — điều phi thường trong xã hội Hy Lạp cổ đại.',
             'He founded "The Garden" — a philosophical community that included men, women, slaves, and free people — remarkable in ancient Greek society.'),
            ('Về tự do: Epicurus từ chối tham gia chính trị — không phải vì ông không quan tâm, mà vì ông nhận ra chính trị thường giam cầm con người vào những lo âu không cần thiết.',
             'On freedom: Epicurus refused to participate in politics — not because he did not care, but because he recognized that politics often imprisons people in unnecessary anxieties.'),
            ('Về thời gian suy nghĩ: mỗi ngày Epicurus và học trò dành nhiều giờ để trò chuyện, suy ngẫm, và nghi vấn. Đây không phải xa xỉ — đây là nhu cầu của tâm hồn.',
             'On time for reflection: each day Epicurus and his students spent many hours in conversation, contemplation, and questioning. This was not luxury — it was a need of the soul.'),
        ],
        'lesson_vn': 'Ba câu hỏi cần trả lời trung thực: Tôi có người bạn thực sự có thể nói chuyện về điều quan trọng không? Tôi có đủ tự do để sống theo giá trị của mình không? Tôi có thời gian để suy nghĩ mỗi ngày không?',
        'lesson_en': 'Three questions to answer honestly: Do I have true friends I can talk with about what matters? Do I have enough freedom to live by my values? Do I have time to think each day?',
    },
    {
        'title_vn': 'Diogenes Và Chiếc Thùng',
        'title_en': 'Diogenes and the Barrel',
        'pairs': [
            ('Diogenes xứ Sinope sống trong một chiếc thùng gỗ lớn ở Athens. Ông có hai tài sản: cái áo và cái bát.',
             'Diogenes of Sinope lived in a large wooden barrel in Athens. He had two possessions: a cloak and a bowl.'),
            ('Một ngày, ông thấy một đứa trẻ uống nước bằng cách chụm tay. Ông ném cái bát đi: "Đứa trẻ này đã dạy ta sự giản dị."',
             'One day, he saw a child drinking water by cupping his hands. He threw away his bowl: "This child has taught me simplicity."'),
            ('Alexander Đại Đế — người chinh phục nửa thế giới — nghe tiếng và đến gặp Diogenes. Ông hỏi: "Ta có thể làm gì cho ngươi?"',
             'Alexander the Great — conqueror of half the world — heard of him and came to visit. He asked: "Is there anything I can do for you?"'),
            ('"Có," Diogenes trả lời. "Ngươi có thể đứng tránh sang một bên — ngươi đang che mặt trời của ta."',
             '"Yes," Diogenes replied. "You can stand aside — you are blocking my sun."'),
            ('Alexander quay lại nói với các tướng lĩnh: "Nếu ta không phải là Alexander, ta muốn là Diogenes."',
             'Alexander turned back and said to his generals: "If I were not Alexander, I would wish to be Diogenes."'),
            ('Diogenes không sợ Alexander vì ông không có gì để mất. Người không có gì không thể bị đe dọa. Đây là tự do tuyệt đối.',
             'Diogenes was not afraid of Alexander because he had nothing to lose. The person who has nothing cannot be threatened. This is absolute freedom.'),
        ],
        'lesson_vn': 'Bạn sở hữu bao nhiêu thứ mà thực ra chính chúng đang sở hữu bạn? Mỗi thứ bạn sợ mất là một sợi xích. Đơn giản hóa là giải phóng.',
        'lesson_en': 'How many things do you own that actually own you? Every thing you fear losing is a chain. Simplifying is liberation.',
    },
    {
        'title_vn': 'Nỗi Sợ Hãi Cái Chết Và Triết Học',
        'title_en': 'The Fear of Death and Philosophy',
        'pairs': [
            ('Epicurus viết câu nổi tiếng nhất của ông: "Cái chết không có gì đối với ta — vì khi ta tồn tại, cái chết không có mặt; và khi cái chết có mặt, thì ta không tồn tại nữa."',
             'Epicurus wrote his most famous line: "Death is nothing to us — for when we exist, death is not present; and when death is present, we no longer exist."'),
            ('Học trò Metrodorus hỏi: "Nhưng thưa thầy, những người thân yêu của ta sẽ đau buồn khi ta chết."',
             'Student Metrodorus asked: "But Master, those dear to me will grieve when I die."'),
            ('"Và điều đó thể hiện ta đã sống như thế nào, phải không?" Epicurus đáp. "Người không ai nhớ đến khi mất — người đó mới thực sự chưa sống."',
             '"And that shows how we lived, does it not?" Epicurus replied. "One whom no one remembers when gone — that is one who has not truly lived."'),
            ('Diogenes khi sắp chết, học trò hỏi muốn được chôn ở đâu. Ông nói: "Vứt ta ra cánh đồng."',
             'When Diogenes was dying, a student asked where he wanted to be buried. He said: "Throw me in a field."'),
            ('"Nhưng thầy không sợ thú dữ ăn thầy sao?" Ông cười: "Các trò hãy đặt cây gậy của ta bên cạnh để ta xua đuổi chúng." Học trò nói xác ông không còn biết làm thế nữa. "Vậy thì ta cũng không khó chịu về điều đó."',
             '"But won\'t you fear wild animals eating you?" He laughed: "Then put my stick beside me so I can drive them off." Students said his body would not know to do that anymore. "Then I will not be troubled by it either."'),
        ],
        'lesson_vn': 'Nỗi sợ cái chết thường thực sự là nỗi sợ chưa sống trọn vẹn. Chữa thuốc cho nỗi sợ đó không phải tránh né cái chết — mà là sống đầy đủ hơn ngay hôm nay.',
        'lesson_en': 'The fear of death is often really the fear of not having lived fully. The cure for that fear is not to avoid death — but to live more fully today.',
    },
    {
        'title_vn': 'Tetrapharmakos — Bốn Vị Thuốc Của Epicurus',
        'title_en': 'Tetrapharmakos — The Fourfold Cure of Epicurus',
        'pairs': [
            ('Học trò của Epicurus truyền đi "Tứ Vị Thuốc" của thầy — bốn câu ngắn có thể chữa hầu hết nỗi khổ của con người:',
             'Epicurus\'s students transmitted their teacher\'s "Fourfold Cure" — four short sentences that can cure most human suffering:'),
            ('"Đừng sợ thần linh. Đừng sợ cái chết. Cái tốt đẹp dễ có được. Cái đáng sợ dễ chịu đựng."',
             '"Do not fear god. Do not fear death. What is good is easy to get. What is terrible is easy to endure."'),
            ('Câu đầu: các vị thần — nếu tồn tại — không quan tâm đến con người. Hãy sống đúng không phải vì sợ trừng phạt, mà vì đó là điều tốt.',
             'First: the gods — if they exist — are not concerned with us. Live rightly not from fear of punishment, but because it is good.'),
            ('Câu hai: Epicurus giải thích kỹ ở trên. Câu ba: những thứ ta thực sự cần — thức ăn đơn giản, nước, sự ấm áp, tình bạn — không khó kiếm. Câu bốn: những nỗi đau thực sự cực độ thì ngắn ngủi; những nỗi đau dai dẳng thì luôn dịu nhẹ hơn ta sợ.',
             'Second: Epicurus explained this above. Third: the things we truly need — simple food, water, warmth, friendship — are not hard to obtain. Fourth: truly extreme pain is brief; chronic pain is always more bearable than we fear.'),
            ('Bốn câu ngắn này đã giúp hàng triệu người qua hơn hai nghìn năm tìm lại sự bình yên.',
             'These four brief sentences have helped millions over more than two thousand years to find peace.'),
        ],
        'lesson_vn': 'Hãy lấy "Tứ Vị Thuốc" làm câu hỏi kiểm tra mỗi khi lo lắng: Tôi đang sợ điều gì không thực sự đáng sợ? Tôi có đang phóng đại sự khó khăn không?',
        'lesson_en': 'Use the "Fourfold Cure" as a test whenever you are anxious: Am I afraid of something not truly fearsome? Am I exaggerating the difficulty?',
    },
]

# ============================================================
# CHƯƠNG 11: Mặc Tử & Hàn Phi — Kiêm Ái, Pháp Trị
# ============================================================
ch11 = [
    {
        'title_vn': 'Kiêm Ái — Yêu Không Phân Biệt',
        'title_en': 'Jian Ai — Universal Love Without Distinction',
        'pairs': [
            ('Mặc Tử hỏi học trò: "Vì sao thiên hạ loạn?"',
             'Mozi asked his students: "Why is the world in disorder?"'),
            ('Học trò đáp: "Vì người người không yêu nhau."',
             'Students replied: "Because people do not love one another."'),
            ('"Đúng. Và tại sao người người không yêu nhau?" Mặc Tử tiếp. "Vì họ yêu người nhà mình hơn người ngoài, yêu nước mình hơn nước khác. Đây là tình yêu phân biệt — và nó tạo ra xung đột."',
             '"Correct. And why do people not love one another?" Mozi continued. "Because they love their own family more than others, their own country more than other countries. This is partial love — and it creates conflict."'),
            ('"Giải pháp là Kiêm Ái — yêu người khác như yêu người nhà mình. Coi nước người khác như nước mình."',
             '"The solution is Jian Ai — loving others as you love your own family. Regarding another\'s country as your own."'),
            ('Học trò phản đối: "Điều đó phi thực tế — người ta không thể yêu người lạ như người thân."',
             'Students objected: "That is impractical — people cannot love strangers as family."'),
            ('Mặc Tử đáp: "Hãy nhìn người lính đi chinh chiến. Ông ta muốn người bạn tốt nhất trông nom gia đình mình. Ai sẽ được chọn? Người chỉ lo gia đình mình hay người yêu thương mọi người như nhau?" Cả lớp im lặng suy nghĩ.',
             'Mozi replied: "Consider a soldier going to war. He wants the best person to look after his family. Who will he choose? The one who only cares for his own family, or the one who loves all people equally?" The class fell silent in thought.'),
        ],
        'lesson_vn': 'Kiêm Ái không đòi hỏi ta xóa bỏ sự gắn bó với gia đình — mà mở rộng vòng tròn quan tâm. Sự tiến bộ đạo đức là mở rộng "chúng ta" để bao gồm ngày càng nhiều người hơn.',
        'lesson_en': 'Universal Love does not require erasing attachment to family — but expanding the circle of concern. Moral progress is expanding "us" to include ever more people.',
    },
    {
        'title_vn': 'Mặc Tử Phản Chiến — Ý Chí Trời Không Muốn Chiến',
        'title_en': 'Mozi Against War — Heaven\'s Will Does Not Want War',
        'pairs': [
            ('Vua nước Sở chuẩn bị tấn công nước Tống. Mặc Tử nghe tin, đi bộ mười ngày mười đêm đến gặp vua.',
             'The King of Chu was preparing to attack the state of Song. When Mozi heard this, he walked for ten days and nights to see the king.'),
            ('"Đại vương," Mặc Tử nói, "nếu một người bỏ xe ngựa của mình để đi ăn trộm xe đẩy của hàng xóm — người đó là kẻ trộm hay không?"',
             '"Your Majesty," Mozi said, "if a man abandons his own carriage to steal his neighbor\'s cart — is that man a thief?"'),
            ('"Tất nhiên là thẻ," vua trả lời.',
             '"Of course," the king replied.'),
            ('"Nước Sở đất rộng dân đông, nước Tống nhỏ yếu. Đại vương muốn chiếm nước Tống — đó là điều gì nếu không phải trộm cướp?" Vua không trả lời được.',
             '"Chu is vast and populous; Song is small and weak. Your majesty wishes to take Song — what is that if not robbery?" The king could not answer.'),
            ('Mặc Tử tiếp: "Thiên hạ không có ác lớn hơn chiến tranh tấn công. Giết một người là tội ác — giết một vạn người lại được gọi là anh hùng? Logic đó sai từ gốc."',
             'Mozi continued: "There is no greater evil in the world than aggressive war. Killing one person is a crime — killing ten thousand is called heroism? That logic is wrong at its root."'),
        ],
        'lesson_vn': 'Hãy kiểm tra thang đo đạo đức của bạn để tránh thiên kiến quy mô: điều bạn lên án ở cá nhân — bạn có nhất quán lên án ở quốc gia và tổ chức không?',
        'lesson_en': 'Check your moral scale to avoid the bias of magnitude: what you condemn in individuals — do you consistently condemn in nations and organizations?',
    },
    {
        'title_vn': 'Hàn Phi — Pháp Trị Và Nghệ Thuật Cai Trị',
        'title_en': 'Han Fei — Rule of Law and the Art of Governance',
        'pairs': [
            ('Hàn Phi, học trò của Tuân Tử, đưa ra lập luận gây tranh cãi: "Đức trị thất bại vì nó phụ thuộc vào sự đức hạnh của người cai trị — điều không thể đảm bảo."',
             'Han Fei, a student of Xunzi, made a controversial argument: "Rule by virtue fails because it depends on the virtue of the ruler — something that cannot be guaranteed."'),
            ('"Nhưng luật pháp rõ ràng, có thưởng có phạt bình đẳng — không phụ thuộc vào đức hạnh cá nhân. Đó là hệ thống có thể vận hành dù người cai trị tốt hay xấu."',
             '"But clear laws, with equal rewards and punishments — these do not depend on individual virtue. That is a system that can function whether the ruler is good or bad."'),
            ('Ông đưa ra ngụ ngôn: "Cây thẳng không cần thợ mộc tài năng. Cây cong cần thợ giỏi để uốn. Xã hội phụ thuộc vào bậc thánh nhân là xã hội dễ vỡ khi thánh nhân không còn."',
             'He offered a parable: "A straight tree needs no skilled carpenter. A crooked tree needs a master to shape it. A society that depends on sages is fragile when the sage is gone."'),
            ('"Hệ thống tốt sẽ biến người bình thường thành người tốt. Hệ thống xấu sẽ biến người tốt thành kẻ xấu. Hãy xây hệ thống, đừng chờ thánh nhân."',
             '"A good system turns ordinary people into good people. A bad system turns good people into bad. Build the system; do not wait for sages."'),
            ('Tư tưởng của Hàn Phi ảnh hưởng sâu sắc đến nhà Tần thống nhất Trung Hoa — và cũng đến tư duy thể chế hiện đại: không ai là không thể thay thế, hệ thống phải tự vận hành.',
             'Han Fei\'s thought profoundly influenced the Qin dynasty that unified China — and also modern institutional thinking: no one is irreplaceable; the system must run itself.'),
        ],
        'lesson_vn': 'Đừng xây tổ chức phụ thuộc vào một cá nhân xuất sắc. Hãy xây hệ thống, quy trình, và văn hóa có thể vận hành tốt ngay cả khi người tài không còn đó.',
        'lesson_en': 'Do not build organizations that depend on one outstanding individual. Build systems, processes, and culture that function well even when the talented person is gone.',
    },
    {
        'title_vn': 'Hàn Phi Luận Về Lòng Tin Và Quyền Lực',
        'title_en': 'Han Fei on Trust and Power',
        'pairs': [
            ('Hàn Phi viết: "Người cai trị khôn ngoan không tin vào lòng tốt của thần tử — ông ta xây dựng hệ thống khiến ngay cả kẻ không tốt cũng hành động đúng."',
             'Han Fei wrote: "The wise ruler does not trust in the goodness of his ministers — he builds a system where even the not-good are compelled to act rightly."'),
            ('Ông phân tích mối quan hệ vua-tôi bằng lăng kính lợi ích: "Vua muốn tôi hiệu quả. Tôi muốn được thưởng. Khi hai lợi ích này thẳng hàng, mọi việc trôi chảy. Khi chúng mâu thuẫn, tai họa xảy ra."',
             'He analyzed the ruler-minister relationship through the lens of interest: "The ruler wants ministers to be effective. The minister wants reward. When these two interests align, things flow. When they conflict, disaster follows."'),
            ('Một vị vua hỏi bề tôi có trung thành không. Hàn Phi cố vấn: "Đó là câu hỏi sai. Câu đúng là: ta đã tạo ra hệ thống mà lòng trung thành trở nên có lợi hơn phản bội chưa?"',
             'A king asked whether his ministers were loyal. Han Fei advised: "That is the wrong question. The right one is: have I created a system where loyalty is more beneficial than betrayal?"'),
            ('Nghe có vẻ lạnh lùng — nhưng đây là nền tảng của quản trị tổ chức hiện đại: thiết kế cơ chế khuyến khích, không dựa vào lòng tốt tự phát.',
             'This sounds cold — but it is the foundation of modern organizational governance: design incentive mechanisms, do not rely on spontaneous goodwill.'),
        ],
        'lesson_vn': 'Khi xây dựng nhóm hay tổ chức, hỏi: "Hệ thống khen thưởng và trách nhiệm của tôi có đang khuyến khích hành vi đúng không — hay tôi chỉ đang hy vọng vào lòng tốt?" Cả hai đều cần, nhưng hệ thống phải đến trước.',
        'lesson_en': 'When building a team or organization, ask: "Are my reward and accountability systems encouraging the right behavior — or am I just hoping for goodwill?" Both matter, but the system must come first.',
    },
    {
        'title_vn': 'Mặc Tử Và Chiếc Cung Của Thợ Làm Tên',
        'title_en': 'Mozi and the Arrow-Maker\'s Bow',
        'pairs': [
            ('Mặc Tử đưa ra hình ảnh ấn tượng để nói về nghề nghiệp và đạo đức:',
             'Mozi offered a striking image to speak about profession and ethics:'),
            ('"Người làm áo giáp muốn người ta dễ bị thương để bán được nhiều áo. Người làm vũ khí muốn chiến tranh xảy ra để bán được dao kiếm. Người thầy thuốc muốn người ta bệnh để có việc làm." Nghe có vẻ độc ác — nhưng thực ra chỉ là logic hệ thống.',
             '"The armor-maker wants people to be vulnerable so he can sell more armor. The weapon-maker wants war to break out to sell swords. The physician wants people ill to have work." This sounds evil — but it is simply system logic.'),
            ('"Vì vậy, hãy chọn nghề nghiệp theo loại thế giới bạn muốn sống trong — không chỉ theo lợi nhuận."',
             '"Therefore, choose your profession according to the kind of world you want to live in — not merely by profit."'),
            ('Mặc Tử bản thân là thợ thủ công — một người lao động chân tay. Ông không coi triết học là nghề của tầng lớp quý tộc. Ông dạy những người thợ rèn, thợ mộc, dân thường.',
             'Mozi himself was a craftsman — a manual laborer. He did not regard philosophy as a profession for the noble class. He taught blacksmiths, carpenters, and common people.'),
            ('Trường phái Mặc Gia có tổ chức chặt chẽ nhất trong các trường phái Trung Hoa cổ đại — với người đứng đầu được gọi là "Cự Tử" và quy tắc kỷ luật nghiêm khắc.',
             'The Mohist school was the most tightly organized of all ancient Chinese schools — with a leader called "Juzi" and strict discipline.'),
        ],
        'lesson_vn': 'Hãy nhìn nghề nghiệp của bạn và hỏi: "Thế giới tốt hơn hay xấu đi khi tôi giỏi hơn trong nghề này?" Đó là câu hỏi đạo đức nghề nghiệp thực sự.',
        'lesson_en': 'Look at your profession and ask: "Is the world better or worse when I become more skilled in this work?" That is the true question of professional ethics.',
    },
    {
        'title_vn': 'Hàn Phi Và Cái Chết Của Một Nhà Tư Tưởng',
        'title_en': 'Han Fei and the Death of a Thinker',
        'pairs': [
            ('Hàn Phi là người nói lắp, không hùng biện được. Nhưng văn chương của ông sắc bén đến mức Hoàng Đế Tần Thủy Hoàng, sau khi đọc, nói: "Nếu ta được gặp người viết điều này và cùng ông ấy đi dạo, ta chết cũng không tiếc."',
             'Han Fei had a stutter and could not speak fluently. But his writing was so sharp that Emperor Qin Shi Huang, after reading it, said: "If I could meet the author of this and walk with him, I would die without regret."'),
            ('Sau đó Hàn Phi đến Tần. Nhưng Lý Tư — cũng là học trò của Tuân Tử, ganh tị với tài năng của Hàn Phi — vu cáo ông phản quốc.',
             'Han Fei then came to Qin. But Li Si — also a student of Xunzi, jealous of Han Fei\'s talent — accused him of treason.'),
            ('Hàn Phi bị bỏ tù. Trước khi Tần Thủy Hoàng kịp xét xử, Lý Tư gửi thuốc độc vào ngục. Hàn Phi chết trong tù — bởi chính người bạn học cũ của mình.',
             'Han Fei was imprisoned. Before Emperor Qin Shi Huang could hold a hearing, Li Si sent poison to the prison. Han Fei died in jail — by the hand of his own former schoolmate.'),
            ('Tư tưởng của ông về sự nguy hiểm của việc cai trị — rằng người cầm quyền luôn bị bao vây bởi những kẻ tư lợi — cuối cùng đã đúng với chính người tạo ra tư tưởng ấy.',
             'His thought about the dangers of rule — that those in power are always surrounded by self-interest — proved true for the very person who created it.'),
            ('Nhưng tư tưởng sống sót còn người. Hàn Phi Tử đến nay vẫn là một trong những tác phẩm chính trị sâu sắc nhất mọi thời đại.',
             'But thought outlives the person. Han Feizi remains to this day one of the most profound political texts of all time.'),
        ],
        'lesson_vn': 'Những người thách thức trật tự quyền lực thường trả giá cao. Nhưng tư tưởng đúng đắn có sức sống bền dai hơn bất kỳ quyền lực nào.',
        'lesson_en': 'Those who challenge power structures often pay dearly. But sound thought has a longer life than any power.',
    },
]

# ============================================================
# CHƯƠNG 12: Giao Thoa Đông Tây — Khi Các Nền Triết Học Gặp Nhau
# ============================================================
ch12 = [
    {
        'title_vn': 'Đạo Và Logos — Hai Dòng Chảy Gặp Nhau',
        'title_en': 'Tao and Logos — Two Streams Meet',
        'pairs': [
            ('Hai nghìn năm trước, ở hai đầu xa kia của lục địa Á-Âu, hai nhà tư tưởng đã nói về cùng một điều bằng hai ngôn ngữ khác nhau.',
             'Two thousand years ago, at opposite ends of the Eurasian continent, two thinkers spoke of the same thing in two different languages.'),
            ('Lão Tử viết: "Đạo khả đạo, phi thường đạo" — nguyên lý nền tảng của vũ trụ vượt quá mọi ngôn từ.',
             'Laozi wrote: "The Tao that can be told is not the eternal Tao" — the foundational principle of the universe surpasses all words.'),
            ('Heraclitus ở Hy Lạp viết: "Logos điều khiển mọi thứ, nhưng mọi người không hiểu nó." Logos — lý trí vũ trụ, nguyên lý của mọi thứ.',
             'Heraclitus in Greece wrote: "Logos governs all things, but people do not understand it." Logos — universal reason, the principle of everything.'),
            ('Cả hai nói về một thứ — một trật tự sâu hơn vượt ra ngoài ngôn ngữ và tri giác thông thường, điều khiển tất cả mà không cần cưỡng bức.',
             'Both speak of the same thing — a deeper order beyond ordinary language and perception, governing all things without compulsion.'),
            ('Không có bằng chứng Lão Tử và Heraclitus biết về nhau. Nhưng cả hai đã chạm đến cùng một chân lý — điều này nói lên rằng có những sự thật không thuộc về bất kỳ văn hóa nào.',
             'There is no evidence Laozi and Heraclitus knew of each other. Yet both touched the same truth — suggesting there are truths that belong to no single culture.'),
        ],
        'lesson_vn': 'Khi nhiều nền triết học độc lập đều chỉ đến cùng một chân lý, đó là dấu hiệu mạnh nhất rằng chân lý ấy thực sự là phổ quát.',
        'lesson_en': 'When multiple independent philosophical traditions all point to the same truth, that is the strongest sign that the truth is genuinely universal.',
    },
    {
        'title_vn': 'Tu Thân Đông Tây — Cùng Một Con Đường',
        'title_en': 'Self-Cultivation East and West — The Same Path',
        'pairs': [
            ('Khổng Tử dạy: "Muốn bình thiên hạ, trước hết phải trị quốc. Muốn trị quốc, phải tề gia. Muốn tề gia, phải tu thân. Muốn tu thân, phải chính tâm."',
             'Confucius taught: "To bring peace to the world, first govern the state. To govern the state, first order the family. To order the family, first cultivate the self. To cultivate the self, first rectify the mind."'),
            ('Marcus Aurelius viết: "Mình kiểm soát được gì? Suy nghĩ, phán đoán, hành động của mình. Đó là điểm bắt đầu và điểm kết thúc."',
             'Marcus Aurelius wrote: "What can I control? My own thoughts, judgments, actions. That is the beginning and the ending."'),
            ('Hai truyền thống — Đông Á và Địa Trung Hải — đều bắt đầu từ cùng một điểm: Thay đổi thế giới bắt đầu từ thay đổi bản thân.',
             'Two traditions — East Asian and Mediterranean — both begin from the same point: Changing the world begins with changing oneself.'),
            ('Socrates: "Hãy biết chính mình." Lão Tử: "Biết mình là sáng." Phật Thích Ca: "Hãy là ngọn đèn cho chính mình." Ba thứ tiếng, ba nền văn hóa — một thông điệp.',
             'Socrates: "Know thyself." Laozi: "Knowing yourself is enlightenment." The Buddha: "Be a lamp unto yourself." Three languages, three cultures — one message.'),
        ],
        'lesson_vn': 'Bất kể bạn theo trường phái triết học nào, điểm bắt đầu là như nhau: hiểu rõ bản thân mình. Mọi hành trình đều xuất phát từ nơi bạn đang đứng.',
        'lesson_en': 'Whatever philosophical tradition you follow, the starting point is the same: understand yourself clearly. Every journey begins from where you are standing.',
    },
    {
        'title_vn': 'Đức Hạnh Là Gì? Đông Và Tây Trả Lời',
        'title_en': 'What Is Virtue? East and West Answer',
        'pairs': [
            ('Aristotle ở Hy Lạp định nghĩa đức hạnh là trung dung giữa hai cực — dũng cảm là trung dung giữa hèn nhát và liều lĩnh, rộng lượng là trung dung giữa keo kiệt và hoang phí.',
             'Aristotle in Greece defined virtue as the mean between two extremes — courage is the mean between cowardice and rashness, generosity the mean between miserliness and extravagance.'),
            ('Khổng Tử dạy Nhân — lòng nhân — là nền tảng của tất cả đức hạnh. Từ Nhân xuất phát Lễ, Nghĩa, Trí, Tín.',
             'Confucius taught Ren — benevolence — as the foundation of all virtue. From Ren flow Ritual, Righteousness, Wisdom, and Trustworthiness.'),
            ('Mạnh Tử nói đức hạnh không cần học — nó đã có sẵn trong tâm mỗi người dưới dạng bốn mầm: trắc ẩn, tu ố, từ nhượng, thị phi.',
             'Mencius said virtue needs no teaching — it already exists in every person\'s heart as four sprouts: compassion, shame, deference, and moral discernment.'),
            ('Marcus Aurelius liệt kê bốn đức hạnh cốt lõi của người Khắc Kỷ: Sáng suốt (Wisdom), Công bằng (Justice), Can đảm (Courage), Điều độ (Temperance).',
             'Marcus Aurelius listed four core Stoic virtues: Wisdom, Justice, Courage, and Temperance.'),
            ('Kỳ lạ thay, dù khác biệt về từ ngữ và hệ thống, các nền triết học đều hội tụ về cùng một hạt nhân: biết suy nghĩ đúng, hành động công bằng, kiên nhẫn với khó khăn, và đối xử tốt với người.',
             'Remarkably, despite their different terminology and systems, all these philosophies converge on the same core: think clearly, act justly, endure hardship with grace, and treat people well.'),
        ],
        'lesson_vn': 'Danh sách đức hạnh của các nền văn hóa khác nhau trùng lặp nhau đến đáng ngạc nhiên. Đây là bằng chứng rằng có một nền đạo đức nhân loại chung — bên dưới mọi sự khác biệt văn hóa.',
        'lesson_en': 'The lists of virtues across cultures overlap to a remarkable degree. This is evidence that there is a common human ethics — beneath all cultural differences.',
    },
    {
        'title_vn': 'Khi Triết Học Gặp Thực Tế Cuộc Sống',
        'title_en': 'When Philosophy Meets Real Life',
        'pairs': [
            ('Epictetus — nô lệ trở thành triết gia Khắc Kỷ vĩ đại — bị chủ nhân bẻ gãy chân như thử nghiệm tư tưởng. Ông nhẹ nhàng nói: "Ta đã nói với ông là ông sẽ gãy nó."',
             'Epictetus — a slave who became a great Stoic philosopher — had his leg broken by his master as a test of philosophy. He said calmly: "I told you that you would break it."'),
            ('Khổng Tử bị đuổi khỏi nhiều nước, đói ăn trong nhiều năm khi chu du thiên hạ. Nhưng ông không bao giờ ngừng dạy học hay bỏ đi niềm tin vào Nhân.',
             'Confucius was expelled from many states, went hungry for years while traveling the world. But he never stopped teaching or abandoned his belief in Ren.'),
            ('Mặc Tử và học trò của ông sẵn sàng chết để bảo vệ thành bang yếu hơn khỏi kẻ xâm lăng — đưa triết học thành hành động trực tiếp.',
             'Mozi and his students were willing to die to defend weaker states from aggressors — turning philosophy into direct action.'),
            ('Điểm chung của tất cả: triết học không chỉ là tri thức đẹp đẽ trong đầu — nó phải được sống, kiểm nghiệm, và thực hành trong nghịch cảnh. Đó mới là triết học thật.',
             'The common thread of all: philosophy is not merely beautiful knowledge in the mind — it must be lived, tested, and practiced in adversity. That is real philosophy.'),
            ('Bài kiểm tra duy nhất cho một triết học là: khi mọi thứ sụp đổ, bạn có giữ được bản thân không? Tất cả các bậc thầy trong quyển sách này đều vượt qua bài kiểm tra đó.',
             'The only test for a philosophy is: when everything collapses, can you remain yourself? All the masters in this book passed that test.'),
        ],
        'lesson_vn': 'Triết học không được học trong thời bình thì chưa thực sự được học. Hãy kiểm tra tư tưởng của bạn trong những khoảnh khắc khó khăn — đó là lúc bạn tìm ra điều mình thực sự tin.',
        'lesson_en': 'Philosophy learned only in peaceful times has not been truly learned. Test your ideas in difficult moments — that is when you discover what you truly believe.',
    },
    {
        'title_vn': 'Lời Cuối — Triết Học Không Kết Thúc',
        'title_en': 'A Final Word — Philosophy Does Not End',
        'pairs': [
            ('Lão Tử rời khỏi Trung Hoa qua cửa ải Hàm Cốc, để lại năm nghìn chữ. Không ai biết ông đã đi đâu.',
             'Laozi left China through the Hangu Pass, leaving behind five thousand characters. No one knows where he went.'),
            ('Socrates chết bằng chén thuốc độc, mỉm cười, nói chuyện triết học đến phút cuối.',
             'Socrates died by a cup of poison, smiling, talking philosophy until the last moment.'),
            ('Marcus Aurelius qua đời trên chiến trường, nhật ký chưa bao giờ định xuất bản của ông vẫn còn đó.',
             'Marcus Aurelius died on the battlefield, his never-meant-to-be-published journal still there.'),
            ('Mặc Tử đi khắp thiên hạ cho đến già. Hàn Phi chết trong tù nhưng tư tưởng sống mãi.',
             'Mozi walked the world until old age. Han Fei died in prison but his ideas lived on.'),
            ('Tất cả họ đều chết. Tất cả những gì họ dạy vẫn sống.',
             'All of them died. Everything they taught still lives.'),
            ('Và đó là câu trả lời cho câu hỏi mà triết học luôn đặt ra: làm thế nào để sống một cuộc đời có ý nghĩa trong một thế giới vô thường? Bằng cách làm cho tư tưởng của bạn đủ mạnh và đủ thật để sống sót sau khi bạn đã qua đời.',
             'And that is the answer to the question philosophy always raises: how to live a meaningful life in an impermanent world? By making your thoughts strong enough and true enough to outlive you.'),
        ],
        'lesson_vn': 'Triết học không cho bạn câu trả lời — nó cho bạn những câu hỏi tốt hơn. Và câu hỏi tốt hơn chính là cuộc sống tốt hơn.',
        'lesson_en': 'Philosophy does not give you answers — it gives you better questions. And better questions are a better life.',
    },
    {
        'title_vn': 'Người Đọc Và Các Bậc Thầy',
        'title_en': 'The Reader and the Masters',
        'pairs': [
            ('Bạn đã đi cùng mười hai bậc thầy qua bảy quyển sách.',
             'You have journeyed with twelve masters across seven books.'),
            ('Họ sống ở những thế kỷ khác nhau, những vùng đất khác nhau, những ngôn ngữ khác nhau. Nhưng tất cả đều đang nói chuyện với bạn — ngay lúc này, khi bạn đọc những dòng này.',
             'They lived in different centuries, different lands, different languages. But all of them are speaking to you — right now, as you read these lines.'),
            ('Lão Tử hỏi: "Bạn có đang sống theo Đạo của mình không — hay đang cưỡng ép?" Khổng Tử hỏi: "Bạn đã tu thân hàng ngày chưa?" Mạnh Tử hỏi: "Bạn có đang nuôi dưỡng bốn mầm trong tâm không?"',
             'Laozi asks: "Are you living according to your Tao — or forcing it?" Confucius asks: "Have you cultivated yourself today?" Mencius asks: "Are you nourishing the four sprouts in your heart?"'),
            ('Trang Tử hỏi: "Bạn có đang cười cùng vũ trụ hay đang chống lại nó?" Socrates: "Bạn có đang tự hỏi liệu mình có biết những gì mình nghĩ là mình biết không?" Marcus Aurelius: "Hôm nay bạn đã phân biệt điều gì trong tầm kiểm soát và điều gì không?"',
             'Zhuangzi asks: "Are you laughing with the universe or fighting it?" Socrates: "Are you questioning whether you know what you think you know?" Marcus Aurelius: "Today, did you distinguish what is within your control and what is not?"'),
            ('Tất cả các câu hỏi quy về một: Bạn đang sống như thế nào? Không phải câu hỏi phán xét — mà câu hỏi mời gọi.',
             'All these questions reduce to one: How are you living? Not a question of judgment — but of invitation.'),
            ('Quyển sách khép lại. Con đường mở ra.',
             'The book closes. The path opens.'),
        ],
        'lesson_vn': 'Đọc sách là khởi đầu. Suy nghĩ về sách là bước tiếp theo. Sống những gì bạn đã học — mỗi ngày, trong từng lựa chọn nhỏ — đó mới là đích đến.',
        'lesson_en': 'Reading is the beginning. Thinking about what you read is the next step. Living what you have learned — each day, in every small choice — that is the destination.',
    },
]

print("Đang tạo chương 9-12...")

make_chapter('ch09-marcus-aurelius-khac-ky', 9,
    'Marcus Aurelius — Khắc Kỷ, Kiểm Soát Bản Thân Và Tình Yêu Số Phận',
    'Marcus Aurelius — Stoicism, Self-Mastery, and Amor Fati', ch09)

make_chapter('ch10-epicurus-diogenes-hanh-phuc-that', 10,
    'Epicurus & Diogenes — Hạnh Phúc Thật Sự Là Gì?',
    'Epicurus & Diogenes — What Is True Happiness?', ch10)

make_chapter('ch11-mac-tu-han-phi-kiem-ai-phap-tri', 11,
    'Mặc Tử & Hàn Phi — Kiêm Ái, Pháp Trị Và Trật Tự Xã Hội',
    'Mozi & Han Fei — Universal Love, Rule of Law, and Social Order', ch11)

make_chapter('ch12-giao-thoa-dong-tay', 12,
    'Giao Thoa Đông Tây — Khi Các Nền Triết Học Gặp Nhau',
    'East Meets West — When Philosophies Converge', ch12)

print("Hoàn tất chương 9-12!")
