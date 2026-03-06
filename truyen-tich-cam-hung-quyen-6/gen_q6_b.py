#!/usr/bin/env python3
# gen_q6_b.py -- Quyển VI chương 5-8: Bản Sắc & Buông Bỏ
import os

CHAPTERS_DIR = os.path.join(os.path.dirname(__file__), "chapters")
os.makedirs(CHAPTERS_DIR, exist_ok=True)

def fix(s):
    s = s.replace('%', r'\%')
    s = s.replace('&', r'\&')
    # Convert straight double quotes to LaTeX curly quotes
    import re
    s = re.sub(r'"([^"\n]*)"', r"``\1''", s)
    return s

def make_chapter(filename, chapter_num, vn_title, en_title, stories):
    lines = []
    lines.append(r'\chapter{' + fix(vn_title) + r'}')
    lines.append(r'\markboth{' + fix(vn_title) + r'}{' + fix(en_title) + r'}')
    lines.append('')
    for idx, story in enumerate(stories, 1):
        story_vn_title = story['title_vn']
        story_en_title = story['title_en']
        pairs = story['pairs']
        lesson_vn = story['lesson_vn']
        lesson_en = story['lesson_en']
        lines.append(r'\section{' + fix(story_vn_title) + r'}')
        lines.append(r'\begin{truyen}{' + fix(story_vn_title) + r'}{' + fix(story_en_title) + r'}')
        first = True
        for (vn, en) in pairs:
            if first:
                words = fix(vn).split(' ', 1)
                if len(words[0]) > 0:
                    first_char = words[0][0]
                    rest_first = words[0][1:] + (' ' + words[1] if len(words) > 1 else '')
                    lines.append(r'\chuhoa{' + first_char + r'}{' + rest_first + r'}')
                else:
                    lines.append(fix(vn))
                first = False
            else:
                lines.append(fix(vn))
            lines.append(r'\textit{(' + fix(en) + r')}')
            lines.append('')
        lines.append(r'\end{truyen}')
        lines.append('')
        lines.append(r'\begin{baihoc}')
        lines.append(fix(lesson_vn))
        lines.append(r'\textit{(' + fix(lesson_en) + r')}')
        lines.append(r'\end{baihoc}')
        if idx < len(stories):
            lines.append(r'\ngancach')
        lines.append('')
    path = os.path.join(CHAPTERS_DIR, filename + '.tex')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f'  Đã tạo: {path}')


# ============================================================
# CHƯƠNG 5: Vai Diễn Và Con Người Thật
# ============================================================
ch05_stories = [
    {
        'title_vn': 'Diễn Viên Và Nhân Vật',
        'title_en': 'The Actor and the Character',
        'pairs': [
            ('Dustin Hoffman nổi tiếng với việc "sống trong nhân vật" — ông giả điên nhiều ngày để chuẩn bị cho vai diễn.',
             'Dustin Hoffman was famous for "living in character" — he pretended to be deranged for days to prepare for a role.'),
            ('Đồng nghiệp Laurence Olivier nhìn anh mệt mỏi rồi nói đơn giản: "Thử diễn xuất đi. Nó dễ hơn nhiều."',
             'Co-star Laurence Olivier watched him exhausted and said simply: "Try acting, dear boy. It\'s far easier."'),
            ('Câu chuyện hài hước đó ẩn chứa một sự thật sâu sắc: có sự khác biệt giữa người diễn xuất và người sống thật.',
             'That humorous anecdote hides a profound truth: there is a difference between the one who performs and the one who lives truly.'),
            ('Nhiều người trong chúng ta sống cả đời trong "nhân vật" — vai con ngoan, vai nhân viên xuất sắc, vai người thành công — đến mức quên mất mình là ai.',
             'Many of us live our entire lives in "character" — the role of obedient child, star employee, successful person — until we forget who we really are.'),
            ('Không ai hỏi bạn muốn đóng vai gì. Nhưng có một câu hỏi quan trọng hơn: Bạn thực sự là ai dưới tất cả những vai đó?',
             'No one asks what role you want to play. But there is a more important question: Who are you truly beneath all those roles?'),
        ],
        'lesson_vn': 'Bạn không phải là vai diễn của mình. Vai diễn là thứ bạn làm; bản thân bạn là thứ bạn là.',
        'lesson_en': 'You are not your role. The role is what you do; your self is who you are.',
    },
    {
        'title_vn': 'Câu Chuyện Vua Lear',
        'title_en': 'The Story of King Lear',
        'pairs': [
            ('Trong vở kịch của Shakespeare, vua Lear từ bỏ vương quốc cho hai người con gái xu nịnh và đuổi người con gái duy nhất yêu ông thật lòng.',
             'In Shakespeare\'s play, King Lear gives his kingdom to two flattering daughters and banishes the one daughter who truly loves him.'),
            ('Khi mất quyền lực — mất vai diễn "nhà vua" — ông không còn biết mình là ai nữa.',
             'When he lost power — lost the role of "king" — he no longer knew who he was.'),
            ('Lạc lõng trong bão, ông hỏi: "Ai là Lear? Mắt anh đang ở đâu?"',
             'Lost in the storm, he asks: "Who is Lear? Where are his eyes?"'),
            ('Ông đã nhầm bản sắc với quyền lực, nhầm con người thật với vương miện.',
             'He had confused identity with power, confused his real self with the crown.'),
            ('Bài học của Lear không phải là câu chuyện về vua — nó là câu chuyện về bất kỳ ai đặt bản thân mình vào một danh hiệu, một chức vụ, một vai trò.',
             'The lesson of Lear is not a story about a king — it is a story about anyone who places their identity in a title, a position, a role.'),
            ('Khi vai diễn kết thúc, ai còn lại?', 'When the role ends, who remains?'),
        ],
        'lesson_vn': 'Đừng nhầm lẫn bản sắc với vai trò. Khi vai trò kết thúc — và nó sẽ kết thúc — bạn cần biết mình còn là ai.',
        'lesson_en': 'Do not confuse identity with role. When the role ends — and it will — you need to know who you still are.',
    },
    {
        'title_vn': 'Thiền Sư Và Chiếc Mặt Nạ',
        'title_en': 'The Zen Master and the Mask',
        'pairs': [
            ('Một học trò hỏi thiền sư: "Thưa thầy, ở nhà con là người cha nghiêm khắc. Ở nơi làm việc con là sếp cứng rắn. Với bạn bè con là người vui vẻ. Vậy con người thật của con là ai?"',
             'A student asked the Zen master: "Master, at home I am a strict father. At work I am a tough boss. With friends I am cheerful. So who is my true self?"'),
            ('Thiền sư đưa cho học trò ba chiếc mặt nạ và nói: "Đeo tất cả ba vào cùng lúc."',
             'The master gave the student three masks and said: "Put all three on at once."'),
            ('Học trò cười: "Không thể được, thưa thầy."',
             'The student laughed: "That\'s impossible, Master."'),
            ('"Đúng vậy," thiền sư nói. "Và mặt nào bên dưới tất cả những mặt nạ đó — đó là con người thật của con."',
             '"Exactly," the master said. "And the face beneath all those masks — that is your true self."'),
            ('Học trò im lặng lâu rồi hỏi: "Nhưng làm sao con nhớ mặt đó khi đang đeo mặt nạ?"',
             'The student was silent a long time then asked: "But how do I remember that face when I am wearing a mask?"'),
            ('"Bằng cách thỉnh thoảng tháo mặt nạ xuống — và ngồi với chính mình."',
             '"By occasionally taking the masks off — and sitting with yourself."'),
        ],
        'lesson_vn': 'Bạn cần những vai diễn trong cuộc sống xã hội. Nhưng bạn cũng cần thời gian không vai diễn — để nhớ rằng bên dưới tất cả, bạn vẫn là bạn.',
        'lesson_en': 'You need roles in social life. But you also need time without roles — to remember that beneath everything, you are still you.',
    },
    {
        'title_vn': 'Marlon Brando Và Sự Chối Bỏ Giải Thưởng',
        'title_en': 'Marlon Brando and the Rejected Award',
        'pairs': [
            ('Năm 1973, Marlon Brando thắng giải Oscar cho phim The Godfather. Thay vì lên nhận, ông gửi một phụ nữ người da đỏ — Sacheen Littlefeather — để từ chối giải và phát biểu về quyền của người bản địa Mỹ.',
             'In 1973, Marlon Brando won the Oscar for The Godfather. Instead of accepting it, he sent a Native American woman — Sacheen Littlefeather — to decline the award and speak about indigenous rights.'),
            ('Hollywood bị sốc. Công chúng chia rẽ. Nhưng Brando không hối hận.',
             'Hollywood was shocked. The public was divided. But Brando had no regrets.'),
            ('"Tôi không thể nhận giải thưởng từ một ngành công nghiệp mà tôi tin đang phá hoại hình ảnh người bản địa," ông nói.',
             '"I cannot accept an award from an industry I believe is damaging the image of Native Americans," he said.'),
            ('Ông từ chối sự chấp nhận của đám đông thời thượng để trung thành với điều mình tin.',
             'He rejected the approval of the fashionable crowd to remain faithful to what he believed.'),
            ('Ông biết sự khác biệt giữa sự công nhận và bản sắc — rằng giải thưởng không phải là anh, và từ chối nó không lấy đi bất cứ thứ gì của anh.',
             'He knew the difference between recognition and identity — that the award was not him, and declining it took nothing away from him.'),
        ],
        'lesson_vn': 'Bản sắc không cần sự chứng nhận bên ngoài. Khi bạn biết mình là ai, bạn tự do từ chối những gì không phù hợp với điều đó.',
        'lesson_en': 'Identity needs no external validation. When you know who you are, you are free to decline what does not align with it.',
    },
    {
        'title_vn': 'Người Lính Trở Về',
        'title_en': 'The Returning Soldier',
        'pairs': [
            ('Marco trở về từ chiến trường sau ba năm. Mọi người gặp anh và hỏi: "Anh thế nào?"',
             'Marco returned from the battlefield after three years. Everyone who met him asked: "How are you?"'),
            ('Anh không biết trả lời. Người lính — vai diễn anh đã mang ba năm — không còn nữa. Nhưng "Marco" thì là ai?',
             'He did not know how to answer. The soldier — the role he had carried for three years — was gone. But who was "Marco"?'),
            ('Anh bắt đầu vẽ — điều anh làm hồi bé nhưng đã bỏ khi nhập ngũ.',
             'He began painting — something he did as a child but had abandoned when he joined the military.'),
            ('Ban đầu chỉ để giết thời gian. Rồi để xử lý ký ức. Rồi vì đó là điều duy nhất khiến anh cảm thấy là mình.',
             'At first just to fill time. Then to process memories. Then because it was the only thing that made him feel like himself.'),
            ('Năm năm sau, anh có triển lãm đầu tiên. Không phải là "anh hùng chiến tranh". Không phải là "cựu binh". Chỉ là Marco — người vẽ.',
             'Five years later, he had his first exhibition. Not as "war hero." Not as "veteran." Just Marco — the painter.'),
            ('Tìm lại con người thật của mình đôi khi đòi hỏi đi ngược lại quá khứ — về nơi bạn đã là mình trước khi thế giới quyết định bạn nên là ai.',
             'Finding your true self sometimes requires going back — to where you were yourself before the world decided who you should be.'),
        ],
        'lesson_vn': 'Khi vai diễn tạm thời kết thúc, hãy tìm về nơi con người thật của bạn đang chờ — thường là trong những điều bạn yêu từ khi còn nhỏ.',
        'lesson_en': 'When a temporary role ends, seek the place your true self is waiting — often in the things you loved since childhood.',
    },
    {
        'title_vn': 'Thái Tử Siddhartha Và Cung Điện',
        'title_en': 'Prince Siddhartha and the Palace',
        'pairs': [
            ('Siddhartha Gautama sinh ra trong cung điện, được bảo vệ khỏi mọi khổ đau bởi một người cha yêu thương.',
             'Siddhartha Gautama was born in a palace, shielded from all suffering by a loving father.'),
            ('Vai diễn của ông được vạch sẵn: thái tử, vua, chinh phục.',
             'His role was scripted: prince, king, conqueror.'),
            ('Nhưng khi ông lén rời cung điện và chứng kiến người già, người bệnh, người chết — ông biết mình không thể tiếp tục đóng vai đó.',
             'But when he secretly left the palace and witnessed old age, sickness, and death — he knew he could not continue playing that role.'),
            ('Không phải vì vai đó sai. Mà vì nó không phải là anh.',
             'Not because the role was wrong. But because it was not him.'),
            ('Ông từ bỏ tất cả — không phải để trốn tránh, mà để tìm kiếm.',
             'He gave up everything — not to escape, but to seek.'),
            ('Cuộc hành trình tìm kiếm bản thân của ông đã trở thành một trong những triết học vĩ đại nhất lịch sử nhân loại.',
             'His journey of self-seeking became one of the greatest philosophies in human history.'),
        ],
        'lesson_vn': 'Đôi khi cần bỏ lại vai diễn được trao để tìm ra vai diễn thật sự của mình — dù đó là con đường khó khăn hơn.',
        'lesson_en': 'Sometimes we must leave behind the assigned role to find our true one — even if that is the harder path.',
    },
    {
        'title_vn': 'Người Phụ Nữ Không Biết Mình Là Ai',
        'title_en': 'The Woman Who Did Not Know Who She Was',
        'pairs': [
            ('Sau mười lăm năm làm vợ, mẹ, nhân viên — tất cả cùng lúc — Linh ngã bệnh.',
             'After fifteen years of being wife, mother, and employee — all at once — Linh fell ill.'),
            ('Bác sĩ nói: "Cơ thể chị đang đình công."',
             'The doctor said: "Your body is on strike."'),
            ('Nằm trên giường, lần đầu tiên trong nhiều năm không có vai diễn nào để đóng, Linh tự hỏi: "Tôi thích gì? Tôi muốn gì? Tôi là ai ngoài những vai đó?"',
             'Lying in bed, for the first time in years with no role to play, Linh asked herself: "What do I enjoy? What do I want? Who am I beyond those roles?"'),
            ('Cô không trả lời được ngay. Nhưng câu hỏi đó mở ra một cuộc hành trình.',
             'She could not answer immediately. But the question opened a journey.'),
            ('Từ từ cô tìm lại những thứ từng là cô: cô yêu vẽ, cô yêu im lặng buổi sáng, cô yêu đọc sách mà không phải "học".',
             'Slowly she rediscovered what had once been her: she loved painting, she loved morning silence, she loved reading without "studying."'),
            ('Bệnh tật đã làm điều mà bận rộn không cho phép: buộc cô dừng lại và nhìn thấy mình.',
             'Illness did what busyness never allowed: forced her to stop and see herself.'),
        ],
        'lesson_vn': 'Đừng đợi đến khi bệnh tật hoặc khủng hoảng buộc bạn dừng lại. Hãy tự dừng lại đủ lâu để nhớ mình là ai.',
        'lesson_en': 'Do not wait until illness or crisis forces you to stop. Stop yourself long enough to remember who you are.',
    },
    {
        'title_vn': 'Nhà Thơ Và Người Biên Tập',
        'title_en': 'The Poet and the Editor',
        'pairs': [
            ('Walt Whitman gửi tập thơ "Lá Cỏ" đến nhiều nhà xuất bản và nhận về hàng chục thư từ chối.',
             'Walt Whitman sent his poetry collection "Leaves of Grass" to numerous publishers and received dozens of rejection letters.'),
            ('Một biên tập viên nói: "Thơ của ông quá trực tiếp, quá hoang dã, quá khác thường. Không ai muốn đọc."',
             'One editor said: "Your poetry is too direct, too wild, too unconventional. No one wants to read this."'),
            ('Whitman trả lời: "Tôi hiểu. Nhưng tôi không thể viết khác đi. Đây là tiếng nói của tôi."',
             'Whitman replied: "I understand. But I cannot write otherwise. This is my voice."'),
            ('Ông tự xuất bản năm 1855. Chỉ in 800 bản.',
             'He self-published in 1855. Only 800 copies were printed.'),
            ('Ngày nay, "Lá Cỏ" được coi là một trong những tập thơ vĩ đại nhất trong văn học Mỹ.',
             'Today, "Leaves of Grass" is considered one of the greatest poetry collections in American literature.'),
            ('Bản sắc sáng tạo cần được bảo vệ khỏi áp lực đám đông — vì điều khác biệt nhất thường là điều có giá trị nhất.',
             'Creative identity needs protection from crowd pressure — for what is most different is often most valuable.'),
        ],
        'lesson_vn': 'Tiếng nói riêng của bạn là tài sản quý giá nhất. Đừng để áp lực đồng nhất hóa dập tắt nó.',
        'lesson_en': 'Your own voice is your most precious asset. Do not let the pressure to conform extinguish it.',
    },
    {
        'title_vn': 'Người Diễn Hài Và Bóng Tối',
        'title_en': 'The Comedian and the Darkness',
        'pairs': [
            ('Robin Williams làm mọi người cười trong nhiều thập kỷ — nhưng ít ai biết ông đang vật lộn với trầm cảm sâu sắc trong suốt cuộc đời.',
             'Robin Williams made people laugh for decades — but few knew he was wrestling with deep depression throughout his life.'),
            ('Ông nói: "Tôi đã đeo mặt nạ cười quá lâu đến mức đôi khi tôi không nhớ nhân vật thật của mình là ai."',
             'He said: "I wore the smiling mask for so long that sometimes I forgot who my real character was."'),
            ('Câu chuyện của Williams không phải là chỉ trích ông — mà là một lời nhắc nhở về sự nguy hiểm của khoảng cách quá lớn giữa con người biểu diễn và con người thật.',
             'Williams\'s story is not a criticism of him — but a reminder of the danger of too great a distance between the performing self and the true self.'),
            ('Khi vai diễn là lớp giáp chứ không phải công cụ — khi bạn diễn để che giấu thay vì để chia sẻ — bạn mang một sức nặng không ai thấy.',
             'When the role becomes armor rather than a tool — when you perform to hide rather than to share — you carry a weight no one sees.'),
            ('Không ai hoàn toàn minh bạch. Nhưng ai cũng cần có ít nhất một không gian — một người — nơi mình không cần diễn.',
             'No one is completely transparent. But everyone needs at least one space — one person — where they need not perform.'),
        ],
        'lesson_vn': 'Hãy thường xuyên kiểm tra khoảng cách giữa con người bạn trình diễn và con người bạn thực sự là. Khi khoảng cách quá lớn, đó là lúc cần chú ý.',
        'lesson_en': 'Regularly check the gap between the self you perform and the self you truly are. When the gap grows too large, it is time to pay attention.',
    },
    {
        'title_vn': 'Người Đàn Ông Và Chiếc Áo Vest',
        'title_en': 'The Man and the Suit Jacket',
        'pairs': [
            ('Một người đàn ông trung niên đến gặp nhà trị liệu và nói: "Tôi không biết mình muốn gì. Tôi làm công việc tôi không thích, sống cuộc đời người khác kỳ vọng, và thấy trống rỗng."',
             'A middle-aged man came to a therapist and said: "I don\'t know what I want. I do work I don\'t like, live the life others expect, and feel empty."'),
            ('Nhà trị liệu hỏi: "Ông có nhớ lần cuối cùng ông làm điều gì đó chỉ vì ông muốn không — không vì ai trông đợi?"',
             'The therapist asked: "Can you remember the last time you did something simply because you wanted to — not because anyone expected it?"'),
            ('Người đàn ông nghĩ mãi không ra. Rồi cười: "Hồi mười hai tuổi tôi hay hát một mình trong nhà."',
             'The man thought for a long time. Then smiled: "When I was twelve I used to sing alone at home."'),
            ('"Tại sao dừng lại?" nhà trị liệu hỏi.',
             '"Why did you stop?" the therapist asked.'),
            ('"Cha tôi nói con trai không hát. Nên tôi bỏ."',
             '"My father said boys don\'t sing. So I quit."'),
            ('Người đàn ông bắt đầu hát lại — lúc đầu một mình trong xe. Đó không phải là giải pháp cho tất cả. Nhưng đó là sợi chỉ dẫn về nhà với chính mình.',
             'The man began singing again — at first alone in his car. That was not the solution to everything. But it was a thread leading back home to himself.'),
        ],
        'lesson_vn': 'Con người thật của bạn thường đang chờ ở những điều bạn từ bỏ vì ai đó nói bạn không nên làm. Hãy tìm lại sợi chỉ đó.',
        'lesson_en': 'Your true self is often waiting in the things you gave up because someone said you should not do them. Find that thread again.',
    },
]

# ============================================================
# CHƯƠNG 6: Áp Lực Đám Đông Và Tự Ngã
# ============================================================
ch06_stories = [
    {
        'title_vn': 'Galileo Và Đám Đông Phán Xét',
        'title_en': 'Galileo and the Judging Crowd',
        'pairs': [
            ('Năm 1633, Galileo Galilei bị Tòa Dị Giáo buộc phải từ bỏ quan điểm rằng Trái Đất quay quanh Mặt Trời.',
             'In 1633, Galileo Galilei was forced by the Inquisition to renounce his view that the Earth revolves around the Sun.'),
            ('Ông phủ nhận. Nhưng theo truyền thuyết, khi bước ra ngoài, ông thì thầm: "Dù vậy, nó vẫn chuyển động."',
             'He recanted. But according to legend, as he walked out, he murmured: "And yet it moves."'),
            ('Đám đông có thể buộc miệng bạn. Nhưng không thể thay đổi sự thật.',
             'The crowd can silence your mouth. But it cannot change the truth.'),
            ('Galileo hiểu rằng có những lúc sự tồn tại quan trọng hơn sự đúng đắn công khai. Nhưng trong tim, ông không bao giờ từ bỏ điều mình biết.',
             'Galileo understood that sometimes survival matters more than public correctness. But in his heart, he never gave up what he knew.'),
            ('Ba trăm năm sau, Giáo hoàng John Paul II chính thức xin lỗi về vụ xét xử Galileo.',
             'Three hundred years later, Pope John Paul II formally apologized for the trial of Galileo.'),
            ('Sự thật kiên nhẫn hơn áp lực đám đông — nó chỉ cần đủ thời gian.',
             'Truth is more patient than crowd pressure — it only needs enough time.'),
        ],
        'lesson_vn': 'Bạn không thể luôn chiến đấu trực tiếp với đám đông. Nhưng bạn không bao giờ cần phải từ bỏ điều mình biết là đúng trong thâm tâm.',
        'lesson_en': 'You cannot always fight the crowd directly. But you never need to give up what you know is true within yourself.',
    },
    {
        'title_vn': 'Hans Christian Andersen Và Bầy Vịt',
        'title_en': 'Hans Christian Andersen and the Ducks',
        'pairs': [
            ('Hans Christian Andersen lớn lên nghèo, xấu trai, vụng về — bạn bè chế giễu, gia đình xấu hổ về ông.',
             'Hans Christian Andersen grew up poor, unattractive, and awkward — mocked by peers, embarrassed by family.'),
            ('Ông đến Copenhagen với ước mơ trở thành diễn viên hát opera. Bị từ chối vì giọng và ngoại hình.',
             'He went to Copenhagen dreaming of becoming an opera singer. Rejected for his voice and appearance.'),
            ('Ông thử múa ba lê. Bị từ chối.',
             'He tried ballet. Rejected.'),
            ('Cuối cùng, ông viết chuyện — những câu chuyện kỳ lạ, không giống ai, xuất phát từ chính nỗi đau và sự khác biệt của mình.',
             'Finally, he wrote stories — strange stories, unlike anyone else\'s, born from his own pain and difference.'),
            ('Câu chuyện "Vịt Con Xấu Xí" là tự truyện của ông — người bị chế giễu vì khác biệt, nhưng cuối cùng tìm ra bầy của mình không phải là vịt mà là thiên nga.',
             'The story "The Ugly Duckling" was his autobiography — the one mocked for being different, who finally found his flock was not ducks but swans.'),
            ('Ngày nay ông là tác giả truyện cổ tích nổi tiếng nhất lịch sử.',
             'Today he is the most famous fairy tale author in history.'),
        ],
        'lesson_vn': 'Điều khiến bạn khác biệt với đám đông không phải là điểm yếu — đó có thể là điều duy nhất thực sự là bạn.',
        'lesson_en': 'What sets you apart from the crowd is not a weakness — it may be the one thing that is truly yours.',
    },
    {
        'title_vn': 'Thí Nghiệm Asch Về Áp Lực Xã Hội',
        'title_en': 'The Asch Conformity Experiment',
        'pairs': [
            ('Năm 1951, nhà tâm lý học Solomon Asch thực hiện một thí nghiệm nổi tiếng: ông cho một nhóm người xem hai đường thẳng và hỏi đường nào dài hơn.',
             'In 1951, psychologist Solomon Asch conducted a famous experiment: he showed a group of people two lines and asked which was longer.'),
            ('Câu trả lời rõ ràng. Nhưng các "diễn viên" trong nhóm đều cố tình trả lời sai.',
             'The answer was obvious. But the "actors" in the group all deliberately answered incorrectly.'),
            ('Kết quả: 75% người tham gia thật — dù biết câu trả lời đúng — đã ít nhất một lần đồng ý với đám đông.',
             'Result: 75% of real participants — despite knowing the correct answer — agreed with the crowd at least once.'),
            ('Khi được hỏi tại sao, họ nói: "Tôi không muốn nổi bật. Tôi không chắc chắn nữa. Mọi người đều nghĩ vậy."',
             'When asked why, they said: "I did not want to stand out. I was no longer sure. Everyone else thought so."'),
            ('Áp lực đám đông mạnh đến mức nó có thể khiến ta nghi ngờ chính mắt mình.',
             'Crowd pressure is so strong it can make us doubt our own eyes.'),
            ('Chỉ cần một người trong nhóm kiên trì trả lời đúng — tỷ lệ phục tùng giảm mạnh. Một người đứng vững có thể giải phóng người khác.',
             'Just one person in the group persisting with the correct answer — conformity dropped significantly. One person standing firm can free others.'),
        ],
        'lesson_vn': 'Đám đông không bao giờ tự động đúng. Và việc bạn đứng vững trong sự thật không chỉ bảo vệ bạn — nó có thể bảo vệ cả người khác.',
        'lesson_en': 'The crowd is never automatically right. And standing firm in truth does not only protect you — it may protect others too.',
    },
    {
        'title_vn': 'Marie Curie Và Phòng Thí Nghiệm',
        'title_en': 'Marie Curie and the Laboratory',
        'pairs': [
            ('Marie Curie là người phụ nữ đầu tiên giành giải Nobel — và người duy nhất đã giành giải Nobel ở hai lĩnh vực khác nhau.',
             'Marie Curie was the first woman to win a Nobel Prize — and the only person ever to win the Nobel in two different fields.'),
            ('Suốt sự nghiệp bà đối mặt với sự kỳ thị: phụ nữ, người nước ngoài, trong ngành khoa học do đàn ông thống trị.',
             'Throughout her career she faced discrimination: a woman, a foreigner, in a male-dominated field.'),
            ('Đồng nghiệp nghi ngờ. Báo chí chế nhạo. Viện Hàn lâm Pháp từ chối bầu bà làm thành viên.',
             'Colleagues doubted her. The press mocked her. The French Academy refused to elect her as a member.'),
            ('Bà không thay đổi hướng đi của mình để vừa lòng họ. Bà tiếp tục vào phòng thí nghiệm mỗi sáng.',
             'She did not change her direction to please them. She continued walking into the laboratory each morning.'),
            ('"Tôi không sợ hãi. Tôi được tạo ra không phải để bình yên chờ đợi, mà để khám phá."',
             '"I am not afraid; I was made to work."'),
            ('Cuối đời, bà không cần phòng thí nghiệm để chứng minh mình — bởi vì bà đã biết mình là ai từ lúc bắt đầu.',
             'At the end of her life, she did not need a laboratory to prove herself — because she had known who she was from the beginning.'),
        ],
        'lesson_vn': 'Công nhận bên ngoài là tốt — nhưng không cần thiết. Khi bạn biết mình đang làm điều đúng, hãy tiếp tục — dù đám đông chưa nhìn thấy.',
        'lesson_en': 'External recognition is good — but not necessary. When you know you are doing the right thing, continue — even if the crowd has not yet seen it.',
    },
    {
        'title_vn': 'Greta Thunberg Và Bé Gái Đình Công',
        'title_en': 'Greta Thunberg and the Striking Girl',
        'pairs': [
            ('Tháng 8 năm 2018, một em gái 15 tuổi tên Greta Thunberg ngồi một mình trước trụ sở Quốc hội Thụy Điển với tấm biển: "Đình công về khí hậu cho trường học."',
             'In August 2018, a 15-year-old girl named Greta Thunberg sat alone outside the Swedish Parliament with a sign: "School strike for climate."'),
            ('Người ta cười cô: "Cô bé điên." Người thân lo lắng. Bạn bè không hiểu.',
             'People laughed at her: "The crazy girl." Relatives worried. Friends did not understand.'),
            ('Cô tiếp tục ngồi mỗi ngày trong ba tuần.',
             'She continued sitting each day for three weeks.'),
            ('Bốn tháng sau, phong trào lan ra 125 quốc gia với 1,4 triệu học sinh đình công.',
             'Four months later, the movement spread to 125 countries with 1.4 million students striking.'),
            ('Một năm sau, đó là 7,6 triệu người trên đường phố toàn cầu.',
             'One year later, it was 7.6 million people on streets worldwide.'),
            ('Không phải vì cô hoàn hảo hay luôn đúng — mà vì cô hoàn toàn là chính mình, không xin phép ai.',
             'Not because she was perfect or always right — but because she was completely herself, asking no one\'s permission.'),
        ],
        'lesson_vn': 'Bạn không cần sự cho phép của đám đông để đứng lên vì điều bạn tin. Đôi khi chỉ cần một người ngồi xuống đúng chỗ.',
        'lesson_en': 'You do not need the crowd\'s permission to stand up for what you believe. Sometimes it only takes one person sitting down in the right place.',
    },
    {
        'title_vn': 'Người Nhạc Sĩ Và Chiếc Đàn Không Đúng Điệu',
        'title_en': 'The Musician and the Off-Key Instrument',
        'pairs': [
            ('Cô Ayasha là nhạc sĩ jazz người Mỹ gốc bản địa trong một ngành nhạc chủ yếu là người da đen và da trắng.',
             'Ayasha was a Native American jazz musician in a genre dominated by Black and white players.'),
            ('Mọi người nói: "Người da đỏ không chơi jazz." Các câu lạc bộ không thuê cô.',
             'People said: "Native Americans don\'t play jazz." Clubs would not hire her.'),
            ('Thay vì cố gắng chơi jazz như người khác, cô kết hợp âm nhạc cổ truyền của bộ tộc mình vào jazz.',
             'Instead of trying to play jazz like everyone else, she wove traditional music from her tribe into jazz.'),
            ('Tiếng nhạc cụ truyền thống kết hợp với tiếng trompet tạo ra âm thanh mà không ai từng nghe trước đó.',
             'The sound of traditional instruments blended with trumpet created sounds no one had ever heard before.'),
            ('Ba năm sau, cô biểu diễn tại Carnegie Hall và được ca ngợi là "giọng nói mới của jazz Mỹ bản địa."',
             'Three years later, she performed at Carnegie Hall and was praised as "the new voice of indigenous American jazz."'),
            ('Cô không thắng bằng cách trở thành ai đó khác — cô thắng bằng cách hoàn toàn là chính mình.',
             'She did not win by becoming someone else — she won by being completely herself.'),
        ],
        'lesson_vn': 'Sự khác biệt của bạn không phải là trở ngại — đó là lợi thế nếu bạn dám mang nó vào đầy đủ.',
        'lesson_en': 'Your difference is not an obstacle — it is an advantage if you dare to bring it fully.',
    },
    {
        'title_vn': 'Em Bé Và Đám Đông',
        'title_en': 'The Child and the Crowd',
        'pairs': [
            ('Trong câu chuyện "Hoàng Đế Cởi Truồng" của Andersen, hai tên lừa đảo thuyết phục hoàng đế rằng họ đang may cho ông bộ quần áo tuyệt vời nhất thế giới — nhưng chỉ người thông minh mới nhìn thấy.',
             'In Andersen\'s "The Emperor\'s New Clothes," two swindlers convince an emperor they are weaving him the most magnificent clothes — visible only to the intelligent.'),
            ('Quan lại nhìn thấy gì? Không có gì. Nhưng không ai dám nói sự thật.',
             'What did the courtiers see? Nothing. But no one dared speak the truth.'),
            ('Dân chúng nhìn thấy gì? Cũng không có gì. Nhưng tất cả vỗ tay và ca ngợi.',
             'What did the common people see? Also nothing. But everyone applauded and praised.'),
            ('Chỉ có một đứa bé bật miệng: "Nhưng ông ấy chẳng mặc gì cả!"',
             'Only a child blurted out: "But he isn\'t wearing anything at all!"'),
            ('Đứa bé không có gì để mất — không danh vọng, không địa vị — nên nó có thể nói sự thật.',
             'The child had nothing to lose — no reputation, no status — so it could speak the truth.'),
            ('Đôi khi sự trong sáng của người không có gì để bảo vệ mới là đôi mắt thật sự nhìn thấy thế giới.',
             'Sometimes the clarity of one who has nothing to protect is the truest pair of eyes to see the world.'),
        ],
        'lesson_vn': 'Đám đông không phải luôn đúng. Hãy dũng cảm như đứa bé — nói điều bạn thực sự thấy, dù mọi người xung quanh im lặng.',
        'lesson_en': 'The crowd is not always right. Be brave like the child — say what you truly see, even when everyone around you is silent.',
    },
    {
        'title_vn': 'Người Đồng Hành Lặng Lẽ',
        'title_en': 'The Quiet Companion',
        'pairs': [
            ('Trong một nghiên cứu, người ta đặt một người vào phòng có bốn người khác đang im lặng — không làm gì, chỉ ngồi.',
             'In a study, one person was placed in a room with four others who were silent — doing nothing, only sitting.'),
            ('Chín mươi phần trăm người mới vào, sau vài phút, cũng bắt đầu im lặng và ngồi — dù không có ai yêu cầu.',
             'Ninety percent of newcomers, after a few minutes, also began to sit in silence — though no one asked them to.'),
            ('Khi được hỏi tại sao, họ nói: "Tôi không muốn làm khác biệt" hoặc "Có lẽ đó là điều cần làm ở đây."',
             'When asked why, they said: "I did not want to be different" or "Perhaps that is what one does here."'),
            ('Chúng ta thường làm theo đám đông không phải vì ta tin đó là đúng — mà vì ta không muốn nổi bật.',
             'We often follow the crowd not because we believe it is right — but because we do not want to stand out.'),
            ('Nhận thức về cơ chế này là bước đầu tiên để thoát khỏi nó.',
             'Awareness of this mechanism is the first step to escaping it.'),
            ('Hỏi mình: "Tôi làm điều này vì tôi thực sự muốn, hay vì mọi người xung quanh đang làm?"',
             'Ask yourself: "Am I doing this because I truly want to, or because everyone around me is doing it?"'),
        ],
        'lesson_vn': 'Tự nhận thức là lá chắn trước áp lực đám đông. Hỏi bản thân "Tại sao tôi làm điều này?" trước khi làm theo.',
        'lesson_en': 'Self-awareness is the shield against crowd pressure. Ask yourself "Why am I doing this?" before following along.',
    },
    {
        'title_vn': 'Người Nghệ Sĩ Và Lời Phê Bình',
        'title_en': 'The Artist and the Criticism',
        'pairs': [
            ('Nhà phê bình Roger Ebert viết về bộ phim "2001: A Space Odyssey" khi mới ra mắt: "Phim này quá dài, quá chậm và quá khó hiểu."',
             'Critic Roger Ebert wrote of "2001: A Space Odyssey" on its release: "This film is too long, too slow, and too obscure."'),
            ('Nhiều người khác đồng ý. Phim thất bại ở tuần đầu chiếu.',
             'Many agreed. The film failed in its opening week.'),
            ('Nhưng đạo diễn Stanley Kubrick không thay đổi phim để hài lòng các nhà phê bình.',
             'But director Stanley Kubrick did not change the film to please critics.'),
            ('Năm mươi năm sau, "2001" được xếp hạng là một trong ba bộ phim vĩ đại nhất lịch sử điện ảnh.',
             'Fifty years later, "2001" is ranked among the three greatest films in cinema history.'),
            ('Ebert, cũng là nhà phê bình vĩ đại, sau này thừa nhận ông đã sai hoàn toàn.',
             'Ebert, himself a great critic, later admitted he was completely wrong.'),
            ('Lịch sử nghệ thuật là lịch sử của những tác phẩm bị từ chối bởi thế hệ mình và được tôn vinh bởi thế hệ sau.',
             'The history of art is the history of works rejected by their own generation and celebrated by the next.'),
        ],
        'lesson_vn': 'Đừng để lời phê bình của hôm nay xác định giá trị của ngày mai. Lịch sử là thẩm phán kiên nhẫn nhất.',
        'lesson_en': 'Do not let today\'s criticism define tomorrow\'s value. History is the most patient judge.',
    },
    {
        'title_vn': 'Người Bơi Không Theo Dòng Nước',
        'title_en': 'The Swimmer Who Goes Against the Current',
        'pairs': [
            ('Một con cá hỏi con cá khác: "Nước là gì?"',
             'One fish asked another: "What is water?"'),
            ('Câu hỏi này — nổi tiếng từ bài diễn văn của David Foster Wallace — ẩn dụ cho áp lực xã hội mà chúng ta bơi trong đó nhưng thường không nhận ra.',
             'This question — made famous by David Foster Wallace\'s speech — is a metaphor for the social pressure we swim in but often do not notice.'),
            ('Áp lực đám đông không phải lúc nào cũng ầm ĩ. Đôi khi nó là nước — vô hình, vô tận, bao quanh bạn.',
             'Crowd pressure is not always loud. Sometimes it is like water — invisible, endless, surrounding you.'),
            ('Nhận ra dòng chảy là bước đầu tiên. Rồi hỏi: "Con cá này có thực sự muốn bơi theo hướng này không?"',
             'Recognizing the current is the first step. Then ask: "Does this fish truly want to swim in this direction?"'),
            ('Bơi ngược không phải lúc nào cũng đúng. Nhưng bơi theo mà không biết tại sao — đó là mất tự do.',
             'Swimming against the current is not always right. But swimming with it without knowing why — that is a loss of freedom.'),
            ('Tự do thực sự không phải là làm ngược lại đám đông. Đó là biết tại sao bạn đang làm điều bạn đang làm — dù nó giống hay khác đám đông.',
             'True freedom is not doing the opposite of the crowd. It is knowing why you are doing what you are doing — whether it resembles the crowd or not.'),
        ],
        'lesson_vn': 'Hãy thỉnh thoảng nổi lên mặt nước và tự hỏi: Tôi đang bơi ở đâu? Tôi có chọn hướng này không hay chỉ đang trôi theo?',
        'lesson_en': 'Occasionally rise to the surface and ask yourself: Where am I swimming? Did I choose this direction or am I just drifting?',
    },
]

# ============================================================
# CHƯƠNG 7: Mất Của Cải, Giữ Phẩm Giá
# ============================================================
ch07_stories = [
    {
        'title_vn': 'Ông Job Và Những Gì Còn Lại',
        'title_en': 'Job and What Remained',
        'pairs': [
            ('Trong Kinh Thánh, Job là người giàu có, hạnh phúc. Rồi trong một khoảng thời gian ngắn, ông mất tất cả: tài sản, con cái, sức khỏe.',
             'In the Bible, Job was wealthy and happy. Then in a short time, he lost everything: property, children, health.'),
            ('Bạn bè đến thăm và nói: "Ắt hẳn ông phạm tội gì đó nên bị trừng phạt."',
             'Friends visited and said: "Surely you have sinned somehow to deserve this punishment."'),
            ('Job không chấp nhận lời giải thích dễ dàng. Ông không nói mình xứng đáng bị khổ. Nhưng ông cũng không mất đức tin.',
             'Job did not accept the easy explanation. He did not say he deserved to suffer. But he also did not lose his faith.'),
            ('Ông kêu than, ông nghi ngờ, ông đặt câu hỏi — nhưng ông không biến mình thành ít hơn những gì ông là.',
             'He lamented, he doubted, he questioned — but he did not make himself less than what he was.'),
            ('Phẩm giá của ông sống sót qua mọi mất mát.',
             'His dignity survived every loss.'),
            ('Câu chuyện Job không phải về phần thưởng cuối cùng — mà về sức mạnh của tinh thần khi tất cả bên ngoài đều sụp đổ.',
             'The story of Job is not about the final reward — but about the strength of spirit when everything external collapses.'),
        ],
        'lesson_vn': 'Khi mọi thứ bên ngoài mất đi, điều còn lại là con người thật của bạn. Hãy chắc chắn đó là người đáng kính.',
        'lesson_en': 'When everything external is lost, what remains is your true self. Make sure it is a person worth respecting.',
    },
    {
        'title_vn': 'Nhà Sư Shichiri Và Tên Trộm',
        'title_en': 'Monk Shichiri and the Thief',
        'pairs': [
            ('Một đêm, tên trộm đột nhập vào phòng thiền sư Shichiri Kojun.',
             'One night, a thief broke into the room of Zen monk Shichiri Kojun.'),
            ('Thiền sư thức dậy và nói bình thản: "Ai đó đó? Anh đến để lấy gì thì lấy, nhưng hãy để lại một ít cho tôi vì tôi cần sống."',
             'The monk woke and said calmly: "Who is there? Take what you came for, but please leave me a little as I need to live."'),
            ('Tên trộm, bối rối vì không bị kháng cự, lấy gần hết đồ và chạy.',
             'The thief, confused by the lack of resistance, took almost everything and fled.'),
            ('Sáng hôm sau, học trò đến thấy phòng trống và hỏi với vẻ lo lắng.',
             'The next morning, disciples came, saw the empty room, and asked with concern.'),
            ('Thiền sư nói: "Người kia còn để lại ánh trăng — anh ấy không lấy được thứ đó."',
             'The monk said: "The man left me the moonlight — he could not take that.'),
            ('Tên trộm sau này tự nộp mình ra và xin làm học trò của thiền sư.',
             'The thief later turned himself in and asked to become the monk\'s student.'),
        ],
        'lesson_vn': 'Của cải có thể bị lấy đi. Nhưng bình an, phẩm giá và tâm hồn rộng rãi — đó là những thứ không ai cướp được.',
        'lesson_en': 'Possessions can be taken. But peace, dignity, and a generous spirit — those are what no one can steal.',
    },
    {
        'title_vn': 'Aristides Và Những Mảnh Sành',
        'title_en': 'Aristides and the Pottery Shards',
        'pairs': [
            ('Aristides — được gọi là "Aristides Công Bằng" — là nhà lãnh đạo được tôn kính nhất Athens.',
             'Aristides — called "Aristides the Just" — was the most respected leader in Athens.'),
            ('Nhưng một ngày, thành phố tổ chức bỏ phiếu lưu đày ông vì một số công dân cảm thấy ông quá nổi bật.',
             'But one day, the city held a vote to exile him because some citizens felt he was too prominent.'),
            ('Một người dân mù chữ đến nhờ Aristides — không nhận ra ông — viết tên "Aristides" vào mảnh sành.',
             'An illiterate citizen came to Aristides — not recognizing him — and asked him to write "Aristides" on a shard.'),
            ('Aristides hỏi: "Aristides làm gì ông khó chịu?"',
             'Aristides asked: "What has Aristides done to offend you?"'),
            ('"Không có gì. Tôi chỉ chán nghe mọi người gọi ông là Công Bằng hoài."',
             '"Nothing. I am just tired of hearing everyone call him Just all the time."'),
            ('Aristides cầm mảnh sành, viết tên mình vào, trả lại và bước đi — không một lời than vãn, không tức giận.',
             'Aristides took the shard, wrote his own name on it, returned it, and walked away — not one word of complaint, not one moment of anger.'),
        ],
        'lesson_vn': 'Người có phẩm giá thực không cần danh tiếng để xác nhận mình. Và khi danh tiếng mất đi, họ vẫn là họ.',
        'lesson_en': 'A person of true dignity needs no reputation to confirm themselves. And when reputation is lost, they remain themselves.',
    },
    {
        'title_vn': 'Nhà Thơ Và Ngọn Lửa',
        'title_en': 'The Poet and the Flames',
        'pairs': [
            ('Năm 1922, nhà văn Ernest Hemingway để vợ mang toàn bộ bản thảo đầu tay của mình từ Paris đến Thụy Sĩ gặp ông.',
             'In 1922, writer Ernest Hemingway had his wife carry all his early manuscripts from Paris to Switzerland to meet him.'),
            ('Trên tàu, chiếc va li bị đánh cắp. Tất cả các bản thảo — nhiều năm viết lách — biến mất.',
             'On the train, the suitcase was stolen. All the manuscripts — years of writing — disappeared.'),
            ('Hemingway tan nát. Một số người khuyên ông bỏ viết.',
             'Hemingway was devastated. Some advised him to quit writing.'),
            ('Nhưng ông nhận ra: mất bản thảo không có nghĩa là mất nhà văn.',
             'But he realized: losing the manuscripts did not mean losing the writer.'),
            ('"Những gì đã xảy ra, đã xảy ra," ông viết. "Nhưng tôi vẫn biết những điều tôi biết."',
             '"What happened, happened," he wrote. "But I still know what I know."'),
            ('Ông viết lại từ đầu — và theo nhiều cách, tốt hơn trước.',
             'He rewrote from the beginning — and in many ways, better than before.'),
        ],
        'lesson_vn': 'Bạn có thể mất những gì bạn đã tạo ra. Nhưng bạn không thể mất những gì bạn đã trở thành qua quá trình tạo ra nó.',
        'lesson_en': 'You can lose what you have created. But you cannot lose who you have become through the process of creating it.',
    },
    {
        'title_vn': 'Người Lính Và Chiếc Nhẫn',
        'title_en': 'The Soldier and the Ring',
        'pairs': [
            ('Thiếu tá Cheung bị bắt làm tù binh trong chiến tranh. Quân địch tịch thu tất cả tài sản, kể cả chiếc nhẫn cưới.',
             'Major Cheung was captured as a prisoner of war. The enemy confiscated everything, including his wedding ring.'),
            ('Trong ba năm tù, ông tự chế tác một chiếc nhẫn thô từ dây kẽm nhặt được.',
             'During three years as a prisoner, he crafted a rough ring from scraps of wire he found.'),
            ('Khi được thả, vợ ông khóc vì chiếc nhẫn cưới đã mất.',
             'When released, his wife wept over the lost wedding ring.'),
            ('Ông đưa cho bà chiếc nhẫn kẽm và nói: "Tôi không thể cho em chiếc nhẫn vàng. Nhưng ba năm nay, chiếc nhẫn này nhắc tôi rằng tôi là ai và tôi thuộc về đâu."',
             'He handed her the wire ring and said: "I cannot give you the gold ring. But for three years, this ring reminded me who I am and where I belong."'),
            ('Bà giữ cả hai cho đến khi mất — chiếc vàng mua lại sau cùng và chiếc kẽm thô ráp — như bằng chứng rằng phẩm giá không cần vàng để tồn tại.',
             'She kept both until she died — the gold ring bought later and the rough wire ring — as proof that dignity needs no gold to exist.'),
        ],
        'lesson_vn': 'Phẩm giá không phụ thuộc vào vật chất. Nó là thứ bạn giữ bên trong khi mọi thứ bên ngoài bị lấy đi.',
        'lesson_en': 'Dignity does not depend on material things. It is what you keep inside when everything outside is taken away.',
    },
    {
        'title_vn': 'Người Buôn Bán Phá Sản',
        'title_en': 'The Bankrupt Merchant',
        'pairs': [
            ('Kakichi Matsumoto, thương nhân Nhật Bản thế kỷ 19, mất toàn bộ tài sản vì một trận cháy kho hàng.',
             'Kakichi Matsumoto, a 19th-century Japanese merchant, lost all his assets in a warehouse fire.'),
            ('Khi chủ nợ đến đòi tiền, ông mời họ vào nhà và phục vụ trà.',
             'When creditors came to collect, he invited them in and served tea.'),
            ('"Tôi không có tiền để trả," ông nói thẳng. "Nhưng tôi có thể cho các ông biết kế hoạch của tôi."',
             '"I have no money to repay," he said directly. "But I can tell you my plan."'),
            ('Ông trình bày kế hoạch tỉ mỉ, trung thực về tình trạng và lộ trình. Không xin lỗi thái quá. Không che giấu.',
             'He presented a detailed plan, honest about his situation and the road ahead. No excessive apology. No concealment.'),
            ('Nhiều chủ nợ cho ông thêm thời gian — không phải vì họ chắc lấy lại được tiền, mà vì cách ông đối mặt khiến họ tin tưởng.',
             'Many creditors gave him more time — not because they were sure of repayment, but because the way he faced them earned their trust.'),
            ('Năm năm sau, ông hoàn trả đủ tất cả. Và danh tiếng của ông còn vang xa hơn cả trước khi ông phá sản.',
             'Five years later, he repaid everyone in full. And his reputation spread further than even before his bankruptcy.'),
        ],
        'lesson_vn': 'Phẩm giá trong khủng hoảng không phải là không bị ngã — mà là cách bạn đứng dậy và đối mặt với những người bị ảnh hưởng bởi cú ngã đó.',
        'lesson_en': 'Dignity in crisis is not about not falling — it is about how you rise and face those affected by the fall.',
    },
    {
        'title_vn': 'Bà Lão Và Căn Nhà',
        'title_en': 'The Old Woman and the House',
        'pairs': [
            ('Bà Nguyễn Thị Tám sống một mình trong căn nhà nhỏ bà xây cả đời. Ở tuổi 75, lũ lụt cuốn trôi tất cả.',
             'Old Mrs. Nguyen Thi Tam lived alone in the small house she had built over a lifetime. At 75, floods swept everything away.'),
            ('Hàng xóm đến hỏi bà có cần giúp đỡ không. Bà đang ngồi bên đống gạch vụn, nhặt những mảnh bát sứ.',
             'Neighbors came asking if she needed help. She was sitting beside the rubble, picking up pieces of broken porcelain.'),
            ('"Những mảnh này của mẹ tôi để lại," bà giải thích. "Tôi không giữ được cái nhà, nhưng tôi giữ được mảnh bát này."',
             '"These pieces were left by my mother," she explained. "I could not keep the house, but I kept these shards."'),
            ('Bà không khóc. Không oán trời. Không trách đất.',
             'She did not cry. Did not blame heaven. Did not curse the earth.'),
            ('"Cái nhà có thể xây lại. Tôi đã xây một lần rồi, tôi xây lại được."',
             '"The house can be rebuilt. I built it once, I can build again."'),
            ('Và bà đã làm — với sự giúp đỡ của cả xóm, những người cảm phục phẩm giá của bà.',
             'And she did — with the help of the entire village, who admired her dignity.'),
        ],
        'lesson_vn': 'Của cải mất có thể xây lại. Nhưng phẩm giá mất không dễ lấy lại — vì vậy hãy giữ nó trước, dù bất cứ giá nào.',
        'lesson_en': 'Lost wealth can be rebuilt. But lost dignity is not easily recovered — so protect it first, at any cost.',
    },
    {
        'title_vn': 'Triết Gia Và Học Trò Nghèo',
        'title_en': 'The Philosopher and the Poor Student',
        'pairs': [
            ('Diogenes của Sinope chọn sống trong một cái thùng gốm — không nhà, không tài sản.',
             'Diogenes of Sinope chose to live in a large ceramic vessel — no house, no possessions.'),
            ('Một hôm Alexander Đại Đế đến thăm và hỏi: "Ngài muốn ta ban cho điều gì?"',
             'One day Alexander the Great visited and asked: "What can I grant you?"'),
            ('Diogenes trả lời: "Hãy đứng tránh chỗ, đừng che nắng của ta."',
             'Diogenes replied: "Stand aside and stop blocking my sunlight."'),
            ('Alexander cười: "Nếu ta không phải là Alexander, ta muốn là Diogenes."',
             'Alexander laughed: "If I were not Alexander, I would wish to be Diogenes."'),
            ('Con người có thể sống không cần nhiều của cải. Nhưng không thể sống thiếu phẩm giá.',
             'A person can live with few possessions. But cannot live without dignity.'),
            ('Diogenes không hề bần hàn — ông là người tự do nhất Athens.',
             'Diogenes was not impoverished — he was the freest man in Athens.'),
        ],
        'lesson_vn': 'Ít của cải không có nghĩa là thiếu phẩm giá. Thực ra, đôi khi bỏ bớt của cải mới cho thấy rõ phẩm giá thực sự.',
        'lesson_en': 'Few possessions do not mean lacking dignity. In fact, sometimes releasing possessions reveals true dignity most clearly.',
    },
    {
        'title_vn': 'Người Giàu Và Người Hành Khất',
        'title_en': 'The Wealthy Man and the Beggar',
        'pairs': [
            ('Trong một truyện ngụ ngôn Ấn Độ, một vị vua cải trang đi dạo phố và gặp người hành khất đang ngồi ca hát vui vẻ.',
             'In an Indian fable, a king in disguise walked through town and met a beggar sitting and singing cheerfully.'),
            ('Vị vua tò mò: "Ông không có gì mà sao ông vui vẻ vậy?"',
             'The king was curious: "You have nothing yet you are so cheerful. Why?"'),
            ('Người hành khất nhìn lên: "Tôi có đủ để sống hôm nay. Tôi không nặng bởi hôm qua. Tôi không lo ngại về ngày mai. Đó là không gian để hạnh phúc rất rộng đấy."',
             'The beggar looked up: "I have enough to live today. I am not burdened by yesterday. I am not anxious about tomorrow. That is a very wide space for happiness."'),
            ('Vị vua — người có tất cả — nhận ra rằng ông đang mang gánh nặng của cả quá khứ lẫn tương lai của đất nước.',
             'The king — who had everything — realized he was carrying the weight of both the past and future of an entire kingdom.'),
            ('"Ai giàu hơn ai?" ông thầm nghĩ.',
             '"Who is richer?" he thought to himself.'),
            ('Của cải đo bằng bình an nội tâm thường cho kết quả khác với của cải đo bằng tiền bạc.',
             'Wealth measured by inner peace often gives a different result than wealth measured in money.'),
        ],
        'lesson_vn': 'Giữ phẩm giá và bình an bên trong — đó là tài sản duy nhất không ai lấy được và không bao giờ mất giá trị.',
        'lesson_en': 'Keep dignity and inner peace — that is the only asset no one can take and that never loses value.',
    },
    {
        'title_vn': 'Người Nông Dân Và Bão Tố',
        'title_en': 'The Farmer and the Storm',
        'pairs': [
            ('Sau một đêm bão, người nông dân ra đồng thấy cả mùa lúa nằm rạp hết.',
             'After a night of storms, the farmer went to the field and found the entire crop flattened.'),
            ('Con trai đứng cạnh nói: "Thất thu rồi ba ơi. Chúng ta không có gì nữa."',
             'His son stood beside him and said: "Crop failure, Dad. We have nothing left."'),
            ('Người cha im lặng một lúc rồi nói: "Lúa ngã nhưng rễ vẫn còn. Nếu cắt dọn sạch, có thể có lúa tái sinh."',
             'The father was silent a moment then said: "The stalks are down but the roots remain. If we clear it properly, there may be regrowth."'),
            ('Hai cha con cúi xuống làm việc. Không than thở, không ngồi khóc.',
             'Father and son bent down and worked. No complaining, no sitting to weep.'),
            ('Sáu tuần sau, lúa tái sinh mọc lên — không bằng mùa chính, nhưng đủ qua đông.',
             'Six weeks later, regrowth appeared — not matching the main harvest, but enough for winter.'),
            ('Người cha nói: "Phẩm giá của nông dân không phải ở mùa màng. Nó ở chỗ sau bão thì cúi xuống làm việc, không cúi đầu khóc lóc."',
             'The father said: "A farmer\'s dignity is not in the harvest. It is in bending down to work after the storm, not bending down to weep."'),
        ],
        'lesson_vn': 'Mất mát không phá hủy phẩm giá. Chỉ có cách bạn phản ứng với mất mát mới có thể làm điều đó.',
        'lesson_en': 'Loss does not destroy dignity. Only the way you respond to loss can do that.',
    },
]

# ============================================================
# CHƯƠNG 8: Mất Đi, Tìm Lại Bản Thân
# ============================================================
ch08_stories = [
    {
        'title_vn': 'Đứa Con Hoang Đàng',
        'title_en': 'The Prodigal Son',
        'pairs': [
            ('Trong dụ ngôn nổi tiếng nhất của Kinh Thánh, người con thứ đòi chia gia sản, mang đi tiêu xài hết, rồi lâm vào cảnh đói khổ.',
             'In the most famous parable in the Bible, the younger son demands his inheritance, squanders it, and falls into poverty.'),
            ('Khi đang chăn lợn và đói đến mức thèm thức ăn của lợn, anh "tỉnh lại" — chữ nguyên văn tiếng Hy Lạp là "eis heauton" — "trở về với chính mình."',
             'Sitting among swine, hungry enough to eat their food, he "came to himself" — the original Greek is "eis heauton" — "returned to himself."'),
            ('Mất mát đã làm điều mà sự sung túc không thể làm: buộc anh nhìn thấy mình thật sự.',
             'Loss did what abundance could not: forced him to truly see himself.'),
            ('Anh đứng dậy và quay về nhà — không chắc mình còn được nhận là con.',
             'He rose and returned home — unsure if he would still be received as a son.'),
            ('Người cha nhìn thấy từ xa, chạy ra, ôm anh trước khi anh kịp nói lời xin lỗi.',
             'The father saw him from a distance, ran out, and embraced him before he could speak a word of apology.'),
            ('Đây không chỉ là câu chuyện về sự tha thứ — mà về hành trình mất đi để tìm lại.',
             'This is not only a story about forgiveness — but about the journey of losing to rediscover.'),
        ],
        'lesson_vn': 'Đôi khi chúng ta cần mất đi thứ gì đó quan trọng mới nhìn thấy điều thực sự quan trọng. Mất mát là con đường dẫn về nhà.',
        'lesson_en': 'Sometimes we need to lose something important before we can see what is truly important. Loss is the road that leads home.',
    },
    {
        'title_vn': 'Hermann Hesse Và Siddhartha',
        'title_en': 'Hermann Hesse and Siddhartha',
        'pairs': [
            ('Trong tiểu thuyết "Siddhartha" của Hermann Hesse, nhân vật chính từ bỏ gia đình giàu có để đi tìm giác ngộ.',
             'In Hermann Hesse\'s novel "Siddhartha," the protagonist leaves his wealthy family to seek enlightenment.'),
            ('Anh học triết học với các nhà khổ hạnh, đạt được sự thấu hiểu, nhưng vẫn cảm thấy thiếu.',
             'He studies philosophy with ascetics, attains insight, but still feels incomplete.'),
            ('Rồi anh rơi vào thế giới vật chất — tiền bạc, cờ bạc, nhục dục — và mất chính mình.',
             'Then he falls into the material world — money, gambling, sensuality — and loses himself.'),
            ('Nhưng đó là điều cần thiết. Chỉ khi thực sự mất mình, anh mới bắt đầu thật sự tìm kiếm.',
             'But that was necessary. Only when he truly lost himself did he truly begin searching.'),
            ('Điểm mấu chốt không phải là tránh né việc lạc đường — mà là khi lạc, biết rằng bạn đang lạc.',
             'The key is not avoiding getting lost — but when lost, knowing that you are lost.'),
            ('Siddhartha cuối cùng tìm thấy mình bên dòng sông — không trong kinh sách hay triết học, mà trong sự lắng nghe.',
             'Siddhartha finally finds himself beside a river — not in scriptures or philosophy, but in listening.'),
        ],
        'lesson_vn': 'Đôi khi con đường tìm lại bản thân phải đi qua sự lạc đường. Điều quan trọng là không bỏ cuộc tìm kiếm.',
        'lesson_en': 'Sometimes the path back to yourself must pass through being lost. What matters is not giving up the search.',
    },
    {
        'title_vn': 'Dante Và Khu Rừng Tối',
        'title_en': 'Dante and the Dark Forest',
        'pairs': [
            ('Dante Alighieri mở đầu Thần Khúc bằng những câu nổi tiếng nhất văn học thế giới: "Giữa đường đời, tôi thấy mình trong khu rừng tối, vì lạc đường thẳng đã mất."',
             'Dante Alighieri opens the Divine Comedy with the most famous lines in world literature: "In the middle of life\'s journey, I found myself in a dark forest, for the straight path was lost."'),
            ('Dante viết Thần Khúc sau khi bị lưu đày khỏi Florence — nhà ông, sự nghiệp ông, tất cả đã mất.',
             'Dante wrote the Divine Comedy after being exiled from Florence — his home, his career, everything lost.'),
            ('Khu rừng tối không phải là địa ngục — đó là sự mất phương hướng trong cuộc sống thực.',
             'The dark forest is not hell — it is the disorientation of real life.'),
            ('Nhưng từ khu rừng đó, Dante không chỉ tìm đường thoát — ông viết nên kiệt tác bất hủ.',
             'But from that dark forest, Dante did not merely find a way out — he wrote an immortal masterpiece.'),
            ('Nhiều tác phẩm vĩ đại nhất của nhân loại được sinh ra từ cái khu rừng tối của tác giả.',
             'Many of humanity\'s greatest works were born from the author\'s own dark forest.'),
            ('Khi bạn lạc đường, bạn không chỉ đang chịu đựng — bạn đang thu thập nguyên liệu cho chính cuộc đời của mình.',
             'When you are lost, you are not only enduring — you are gathering material for your own life.'),
        ],
        'lesson_vn': 'Khu rừng tối mà bạn đang đi qua không phải là kết thúc. Nó là nơi bắt đầu của hành trình thực sự.',
        'lesson_en': 'The dark forest you are passing through is not the end. It is where the real journey begins.',
    },
    {
        'title_vn': 'Người Phụ Nữ Bắt Đầu Lại Ở Tuổi 50',
        'title_en': 'The Woman Who Started Over at 50',
        'pairs': [
            ('Sau ly hôn ở tuổi 49, sau 25 năm làm vợ và mẹ toàn thời gian, Claudia không biết mình là ai ngoài những vai đó.',
             'After divorce at 49, after 25 years as a full-time wife and mother, Claudia did not know who she was outside those roles.'),
            ('Cô không làm việc. Không có bạn bè riêng tư. Không có sở thích cá nhân.',
             'She had no job. No personal friends. No individual hobbies.'),
            ('"Tôi đã mất chính mình trong cuộc hôn nhân đó," cô nói. "Không phải vì anh ấy lấy đi. Mà vì tôi tặng đi từng mảnh mà không giữ lại gì cho mình."',
             '"I lost myself in that marriage," she said. "Not because he took it. But because I gave away pieces of myself without keeping any for me."'),
            ('Ở tuổi 50, cô ghi danh học hội họa — điều cô thích từ nhỏ nhưng chưa bao giờ theo.',
             'At 50, she enrolled in a painting class — something she had loved since childhood but never pursued.'),
            ('Năm năm sau, cô có gallery nhỏ riêng — không giàu, nhưng sống được và sống vui.',
             'Five years later, she had her own small gallery — not wealthy, but surviving and thriving.'),
            ('"Tôi mất hai mươi lăm năm nhưng tìm lại được chính mình. Đó không phải là tệ," cô mỉm cười.',
             '"I lost twenty-five years but found myself again. That is not so bad," she smiled.'),
        ],
        'lesson_vn': 'Không bao giờ là quá muộn để tìm lại mình. Mỗi ngày bạn bắt đầu là ngày sớm nhất bạn có — và cũng đủ rồi.',
        'lesson_en': 'It is never too late to find yourself again. Every day you start is the earliest day you have — and it is enough.',
    },
    {
        'title_vn': 'Odysseus Và Hành Trình Về Nhà',
        'title_en': 'Odysseus and the Journey Home',
        'pairs': [
            ('Trong sử thi của Homer, Odysseus mất mười năm chiến tranh và mười năm lạc lối trên biển trước khi về được nhà.',
             'In Homer\'s epic, Odysseus loses ten years to war and ten years wandering at sea before reaching home.'),
            ('Trên đường về, ông gặp thần thánh, quái vật, phù thủy và mồi nhử của sự quên lãng.',
             'On the way home, he encounters gods, monsters, sorcerers, and the temptation of oblivion.'),
            ('Nhưng điều giữ ông không phải là sức mạnh — mà là ký ức về nơi ông thuộc về.',
             'But what kept him was not strength — it was memory of where he belonged.'),
            ('Người phụ nữ cho ông bất tử và sự sung sướng vĩnh cửu. Ông từ chối: "Tôi muốn về nhà."',
             'A woman offered him immortality and eternal pleasure. He refused: "I want to go home."'),
            ('"Nhà" không phải là địa điểm — đó là bản sắc, là những mối quan hệ tạo nên ý nghĩa.',
             '"Home" is not a place — it is identity, the relationships that create meaning.'),
            ('Hành trình về nhà của Odysseus là hành trình về lại với chính mình — dù có mất bao lâu.',
             'Odysseus\'s journey home is the journey back to himself — no matter how long it takes.'),
        ],
        'lesson_vn': 'Dù bạn đi lạc bao xa hay bao lâu, hành trình về lại với bản thân luôn là con đường đáng đi.',
        'lesson_en': 'No matter how far or how long you have wandered, the journey back to yourself is always the path worth taking.',
    },
    {
        'title_vn': 'Nhà Khoa Học Và Căn Bệnh',
        'title_en': 'The Scientist and the Illness',
        'pairs': [
            ('Tiến sĩ Oliver Sacks — thần kinh học nổi tiếng người Anh — được chẩn đoán ung thư năm 2015 ở tuổi 82.',
             'Dr. Oliver Sacks — the celebrated British neurologist — was diagnosed with cancer in 2015 at age 82.'),
            ('Ông viết một loạt bài trên New York Times về những gì ông nghĩ, cảm nhận và giá trị khi đối mặt với cái chết.',
             'He wrote a series of essays in the New York Times about what he thought, felt, and valued while facing death.'),
            ('"Trên tất cả, tôi đã là một sinh vật có ý thức, một con thú biết suy nghĩ trên hành tinh xinh đẹp này, và bản thân điều đó là một đặc ân và cuộc phiêu lưu lớn."',
             '"Above all, I have been a sentient being, a thinking animal on this beautiful planet, and that in itself has been an enormous privilege and adventure."'),
            ('Căn bệnh không lấy đi điều ông là — nó chắt lọc nó.',
             'The illness did not take away what he was — it distilled it.'),
            ('Những bài viết cuối đời đó được coi là một số tác phẩm quan trọng nhất của ông.',
             'Those final essays are considered some of his most important work.'),
            ('Đôi khi sự mất mát — kể cả mất sức khỏe, mất thời gian — buộc ta tập trung vào điều thực sự là ta.',
             'Sometimes losing — even losing health, losing time — forces us to focus on what is truly us.'),
        ],
        'lesson_vn': 'Khủng hoảng đôi khi là chiếc gương sắc nét nhất — nơi bạn thấy rõ nhất mình thực sự là ai và điều gì thực sự quan trọng.',
        'lesson_en': 'Crisis is sometimes the sharpest mirror — the place where you see most clearly who you truly are and what truly matters.',
    },
    {
        'title_vn': 'Người Trẻ Và Tòa Tháp',
        'title_en': 'The Young Man and the Tower',
        'pairs': [
            ('Trong một truyện ngụ ngôn Sufi, một người trẻ trèo lên tòa tháp cao nhất thành phố và nhìn xuống.',
             'In a Sufi parable, a young man climbs to the top of the tallest tower in the city and looks down.'),
            ('"Từ đây tôi thấy tất cả," anh nói với bản thân. "Nhưng tôi không thấy chính mình."',
             '"From here I can see everything," he said to himself. "But I cannot see myself."'),
            ('Anh leo xuống và hỏi một người thợ rèn đang làm việc: "Bạn có thể thấy mình trong công việc không?"',
             'He climbed down and asked a blacksmith at work: "Can you see yourself in your work?"'),
            ('Người thợ rèn nhìn lên, mồ hôi trán, bàn tay cháy, mỉm cười: "Không trong gương. Nhưng trong mỗi thanh sắt tôi đã uốn."',
             'The blacksmith looked up, sweaty brow, scorched hands, smiling: "Not in a mirror. But in every bar of iron I have bent."'),
            ('Người trẻ hiểu: bản sắc không được tìm thấy khi đứng trên cao nhìn xuống cuộc đời của mình — mà khi cúi xuống và làm việc trong lòng nó.',
             'The young man understood: identity is not found standing high looking down on life — but bending down and working within it.'),
        ],
        'lesson_vn': 'Bạn tìm lại mình không phải bằng cách thoát khỏi cuộc sống của mình — mà bằng cách đi sâu vào nó và làm việc thật sự trong đó.',
        'lesson_en': 'You do not rediscover yourself by escaping your life — but by going deeper into it and truly working within it.',
    },
    {
        'title_vn': 'Người Nhạc Sĩ Và Nốt Nhạc Bị Quên',
        'title_en': 'The Musician and the Forgotten Note',
        'pairs': [
            ('Sau một tai nạn, nghệ sĩ piano Rafael mất một phần trí nhớ vắn hạn — bao gồm nhiều đoạn nhạc ông đã thuộc lòng.',
             'After an accident, pianist Rafael lost part of his short-term memory — including many musical passages he had memorized.'),
            ('Bác sĩ nói ông có thể không bao giờ biểu diễn lại ở mức chuyên nghiệp.',
             'Doctors said he might never perform professionally again.'),
            ('Rafael bắt đầu lại từ những bài tập dành cho học sinh lớp một.',
             'Rafael began again with exercises for first-grade students.'),
            ('Lúc đầu xấu hổ. Rồi dần dần, anh nhận ra điều gì đó: lần đầu tiên trong hai mươi năm, anh đang thực sự nghe âm nhạc — không chỉ chơi nó.',
             'At first it was humiliating. Then gradually, he noticed something: for the first time in twenty years, he was truly hearing the music — not just playing it.'),
            ('Hai năm sau, ông biểu diễn trở lại. Nhưng lần này mọi người nói: anh chơi khác hơn trước — sâu hơn, chân thật hơn.',
             'Two years later, he performed again. But this time people said: he plays differently than before — deeper, more authentic.'),
            ('"Tai nạn lấy đi kỹ thuật của tôi," anh nói. "Nhưng trả lại cho tôi tình yêu âm nhạc."',
             '"The accident took my technique," he said. "But gave me back my love of music."'),
        ],
        'lesson_vn': 'Đôi khi mất đi kỹ năng hay kiến thức không phải là thất bại — mà là cơ hội bắt đầu lại với đôi mắt mới.',
        'lesson_en': 'Sometimes losing skills or knowledge is not failure — but an opportunity to begin again with new eyes.',
    },
    {
        'title_vn': 'Người Đàn Ông Và Ngọn Nến',
        'title_en': 'The Man and the Candle',
        'pairs': [
            ('Trong câu chuyện của nhà thơ Rumi, một người đàn ông đang đốt nến và bỗng nhiên ngọn lửa tắt.',
             'In a story by the poet Rumi, a man is burning a candle when suddenly the flame goes out.'),
            ('Anh ngồi trong bóng tối và than thở: "Tôi đã mất ánh sáng."',
             'He sits in the darkness and laments: "I have lost the light."'),
            ('Một giọng nói vô hình hỏi: "Hay anh đã tìm lại bóng tối?"',
             'An invisible voice asks: "Or have you regained the darkness?"'),
            ('"Đây không phải là điều tốt hơn," người đàn ông nói.',
             '"This is not something better," the man said.'),
            ('"Có thể không. Nhưng bây giờ anh biết thế nào là không có ánh sáng. Và lần tới khi có ánh sáng, anh sẽ trân trọng nó hơn bất kỳ lúc nào trước đây."',
             '"Perhaps not. But now you know what it is like without light. And the next time you have light, you will value it more than at any time before."'),
            ('Mất mát dạy chúng ta thấy giá trị của những gì bình thường bị coi là hiển nhiên.',
             'Loss teaches us to see the value of what is ordinarily taken for granted.'),
        ],
        'lesson_vn': 'Mất mát không chỉ lấy đi — nó còn dạy bạn nhìn rõ hơn những gì còn lại và những gì quan trọng.',
        'lesson_en': 'Loss does not only take away — it also teaches you to see more clearly what remains and what matters.',
    },
    {
        'title_vn': 'Người Viết Thư Cho Bản Thân',
        'title_en': 'The Person Who Wrote Letters to Herself',
        'pairs': [
            ('Sau khi qua cơn trầm cảm nặng, nhà giáo Amira bắt đầu thực hành: mỗi năm vào ngày sinh nhật, cô viết một lá thư cho "Amira của năm tới."',
             'After recovering from severe depression, teacher Amira began a practice: each year on her birthday, she wrote a letter to "next year\'s Amira."'),
            ('Trong thư, cô viết những gì cô đã mất, những gì cô đã tìm lại, và những gì cô hy vọng.',
             'In the letter, she wrote what she had lost, what she had found again, and what she hoped for.'),
            ('Mười năm sau, cô có mười lá thư — lịch sử của một người liên tục mất và tìm lại mình.',
             'Ten years later, she had ten letters — the history of a person continually losing and finding herself.'),
            ('Cô đọc lại những lá thư với học trò và nói: "Nhìn vào đây, các em thấy không — mỗi lần tôi mất mình, tôi tìm lại mình ở chỗ khác hơn, sâu hơn."',
             'She read the letters back with her students and said: "Look here — each time I lost myself, I found myself somewhere different, somewhere deeper."'),
            ('Mất mát không phải là vòng tròn — nó là đường xoáy ốc đi xuống và lên lại.',
             'Loss is not a circle — it is a spiral going down and back up again.'),
            ('Mỗi lần bạn tìm lại mình sau mất mát, bạn tìm lại một bản thân phong phú hơn lần trước.',
             'Each time you find yourself after loss, you find a self richer than before.'),
        ],
        'lesson_vn': 'Sự mất mát và tìm lại không phải là thất bại lặp đi lặp lại — đó là cách con người lớn lên và trở nên sâu sắc hơn.',
        'lesson_en': 'The pattern of losing and finding is not repeated failure — it is how people grow and become deeper.',
    },
]

print("Đang tạo chương 5-8...")

make_chapter(
    'ch05-vai-dien-va-con-nguoi-that', 5,
    'Vai Diễn Và Con Người Thật',
    'The Role and the True Self',
    ch05_stories
)

make_chapter(
    'ch06-ap-luc-dam-dong-va-tu-nga', 6,
    'Áp Lực Đám Đông Và Tự Ngã',
    'Crowd Pressure and the Self',
    ch06_stories
)

make_chapter(
    'ch07-mat-cua-cai-giu-pham-gia', 7,
    'Mất Của Cải, Giữ Phẩm Giá',
    'Losing Wealth, Keeping Dignity',
    ch07_stories
)

make_chapter(
    'ch08-mat-di-tim-lai-ban-than', 8,
    'Mất Đi, Tìm Lại Bản Thân',
    'Losing and Rediscovering Oneself',
    ch08_stories
)

print("Hoàn tất chương 5-8!")
