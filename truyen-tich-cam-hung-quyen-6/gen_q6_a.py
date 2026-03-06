#!/usr/bin/env python3
# gen_q6_a.py -- Quyển VI chương 1-4: Nhân Quả & Bản Sắc
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
        lines.append(r'\begin{truyen}{' + fix(story_vn_title) + r'}{' + fix(story_en_title) + r'}')
        first = True
        for (vn, en) in pairs:
            if first:
                # Split first word for drop cap
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
# CHƯƠNG 1: Gieo Điều Tốt, Gặp Điều Tốt
# ============================================================
ch01_stories = [
    {
        'title_vn': 'Churchill Và Fleming',
        'title_en': 'Churchill and Fleming',
        'pairs': [
            ('Năm 1914, một cậu bé nhà nghèo tên Alexander Fleming đang chơi gần đầm lầy khi nghe tiếng kêu cứu.',
             'In 1914, a poor boy named Alexander Fleming was playing near a swamp when he heard a cry for help.'),
            ('Không do dự, cậu lao xuống kéo một đứa trẻ khác lên bờ — đứa trẻ đó là Winston Churchill.',
             'Without hesitation, he jumped in and pulled another child to safety — that child was Winston Churchill.'),
            ('Cha của Churchill, Lord Randolph, cảm kích sâu sắc trước hành động dũng cảm đó.',
             "Churchill's father, Lord Randolph, was deeply moved by the act of bravery."),
            ('Ông quyết định tài trợ cho Fleming học y khoa — ngành mà Fleming hằng mơ ước nhưng không có tiền theo.',
             'He decided to sponsor Fleming\'s medical education — a dream Fleming had long held but could not afford.'),
            ('Hai mươi năm sau, trong Thế chiến Thứ hai, Churchill bị viêm phổi nặng gần như chết.',
             'Twenty years later, during World War II, Churchill contracted severe pneumonia and nearly died.'),
            ('Vị bác sĩ dùng loại thuốc mới chữa lành ông chính là Alexander Fleming — người vừa phát minh ra penicillin.',
             'The doctor who saved him with a new medicine was Alexander Fleming — the very man who had just invented penicillin.'),
            ('Hạt giống tốt gieo xuống năm nào đã nảy mầm và cứu sống người gieo nó.',
             'The good seed sown long ago had sprouted and saved the very one who planted it.'),
        ],
        'lesson_vn': 'Điều tốt bạn làm hôm nay có thể trở lại cứu bạn vào ngày mai, theo những cách bạn không thể ngờ tới.',
        'lesson_en': 'The good you do today may return to save you tomorrow in ways you could never imagine.',
    },
    {
        'title_vn': 'Người Nông Dân Và Hạt Lúa Vàng',
        'title_en': 'The Farmer and the Golden Grain',
        'pairs': [
            ('Có hai người nông dân sống cạnh nhau: một người chăm chỉ bón phân, gieo hạt đúng mùa; người kia lười biếng, gieo hạt qua loa.',
             'Two farmers lived side by side: one diligently fertilized and sowed at the right season; the other was lazy, seeding carelessly.'),
            ('Mùa gặt, người chăm chỉ thu được lúa vàng đầy bồ; người lười chỉ nhận được gié lép và cỏ dại.',
             'At harvest time, the diligent one reaped golden grain filling his barn; the lazy one got only hollow husks and weeds.'),
            ('Người lười than thở: "Sao trời bất công với tôi vậy?"',
             'The lazy farmer complained: "Why is heaven so unfair to me?"'),
            ('Người láng giềng trả lời: "Trời không bất công. Đồng ruộng chỉ trả lại những gì chúng ta cho nó."',
             'His neighbor replied: "Heaven is not unfair. The field simply returns what we give it."'),
            ('Cuộc sống cũng là một cánh đồng như thế — nó không phán xét, nó chỉ phản chiếu.',
             'Life is such a field — it does not judge, it only reflects.'),
        ],
        'lesson_vn': 'Cuộc sống trả lại đúng những gì chúng ta gieo vào nó — chăm chỉ hay lười biếng, tử tế hay ích kỷ.',
        'lesson_en': 'Life returns exactly what we sow into it — diligence or laziness, kindness or selfishness.',
    },
    {
        'title_vn': 'Câu Chuyện Của Trẻ Em Tibet',
        'title_en': 'The Story of the Tibetan Children',
        'pairs': [
            ('Một vị sư già dạy học trò: "Mỗi buổi sáng, hãy làm một điều tốt nhỏ mà không ai biết."',
             'An old monk taught his students: "Each morning, do one small good deed that no one knows about."'),
            ('Một cậu bé hỏi: "Thưa thầy, nếu không ai biết thì có ích gì?"',
             'A boy asked: "Master, if no one knows, what is the use?"'),
            ('Vị sư cầm một hạt giống bỏ vào đất, rồi nói: "Hạt này có cần ai biết không, để mọc thành cây?"',
             'The monk took a seed, placed it in the soil, and said: "Does this seed need anyone to know it, to grow into a tree?"'),
            ('Cậu bé hiểu ra: điều thiện không cần khán giả để sinh hoa trái.',
             'The boy understood: goodness needs no audience to bear fruit.'),
            ('Mười năm sau, cậu bé ấy trở thành người được cả làng yêu quý — không vì danh tiếng, mà vì thói quen âm thầm làm tốt đã thấm vào tính cách.',
             'Ten years later, that boy became the most beloved person in the village — not for fame, but because the habit of quietly doing good had permeated his character.'),
        ],
        'lesson_vn': 'Điều tốt không cần khán giả. Nó tự âm thầm xây dựng bạn từ bên trong.',
        'lesson_en': 'Goodness needs no audience. It quietly builds you from within.',
    },
    {
        'title_vn': 'Người Đưa Thư Và Mảnh Vườn',
        'title_en': 'The Postman and the Garden',
        'pairs': [
            ('Mỗi ngày đi làm, người đưa thư Joseph Alphonse thường nhặt rác trên con đường mình đi qua.',
             'Every day on his route, postman Joseph Alphonse would pick up trash along the path he walked.'),
            ('Không ai nhờ anh làm. Không ai trả công anh. Đó chỉ là thói quen anh tự đặt ra cho mình.',
             'No one asked him to. No one paid him. It was simply a habit he set for himself.'),
            ('Sau mười năm, con đường đó trở thành con đường xanh nhất, sạch nhất trong vùng.',
             'After ten years, that road became the greenest, cleanest in the area.'),
            ('Chính quyền địa phương tìm ra người đứng sau và trao cho anh giải thưởng công dân tiêu biểu.',
             'Local authorities found the person behind it and awarded him the outstanding citizen prize.'),
            ('Anh chỉ cười: "Tôi chỉ muốn con đường sạch để đi làm cho vui. Không ngờ lại được như vậy."',
             'He just smiled: "I only wanted a clean road to walk to work. I never expected this."'),
            ('Nhân quả không bao giờ thất bại — nó chỉ đến theo thời điểm của nó.',
             'Karma never fails — it only arrives on its own schedule.'),
        ],
        'lesson_vn': 'Hãy làm điều tốt không vì phần thưởng. Phần thưởng sẽ tìm đến bạn theo cách riêng của nó.',
        'lesson_en': 'Do good not for reward. Reward will find you in its own way.',
    },
    {
        'title_vn': 'Người Thợ Mộc Và Ngôi Nhà Cuối Cùng',
        'title_en': 'The Carpenter and the Last House',
        'pairs': [
            ('Một người thợ mộc lão làng sắp về hưu. Chủ nhà máy yêu cầu anh xây một ngôi nhà cuối cùng.',
             'An experienced carpenter was about to retire. His employer asked him to build one last house.'),
            ('Người thợ, biết mình sắp nghỉ, không còn dồn tâm huyết như trước. Anh dùng vật liệu kém, làm qua loa.',
             'The carpenter, knowing he would soon retire, no longer put in his best effort. He used inferior materials and worked carelessly.'),
            ('Khi hoàn thành, chủ nhà máy trao cho anh chìa khóa và nói: "Đây là ngôi nhà của anh. Quà tặng về hưu của tôi."',
             'When done, the employer handed him the keys and said: "This is your house. My retirement gift to you."'),
            ('Người thợ mộc đứng lặng, tim như thắt lại.',
             'The carpenter stood silent, his heart sinking.'),
            ('Nếu anh biết mình đang xây nhà cho mình, anh đã xây nó bằng tất cả những gì tốt nhất.',
             'Had he known he was building it for himself, he would have built it with everything he had.'),
            ('Cuộc sống cũng vậy — ta đang xây ngôi nhà mà rốt cuộc chính ta sẽ ở trong đó.',
             'Life is the same — we are building the house we ourselves will ultimately live in.'),
        ],
        'lesson_vn': 'Hãy sống và làm việc như thể bạn đang xây chính ngôi nhà mà bạn sẽ ở — vì thực ra đó là sự thật.',
        'lesson_en': 'Live and work as if you are building the very house you will live in — because that is the truth.',
    },
    {
        'title_vn': 'Người Phụ Nữ Và Chiếc Bánh Mì',
        'title_en': 'The Woman and the Bread',
        'pairs': [
            ('Emiliana là người phụ nữ nghèo làm công nhật ở một cửa hàng bánh mì nhỏ tại São Paulo.',
             'Emiliana was a poor day laborer at a small bakery in São Paulo.'),
            ('Mỗi ngày tan ca, bà thường nhặt những mảnh bánh vỡ còn lại mang về cho những đứa trẻ đường phố gần nhà.',
             'Each day after her shift, she would collect leftover broken bread to bring back to street children near her home.'),
            ('Hai mươi năm trôi qua, một trong những đứa trẻ ấy trở thành kỹ sư và tìm lại bà để cảm ơn.',
             'Twenty years passed, and one of those children became an engineer and searched for her to say thank you.'),
            ('"Bà không nhớ tôi đâu," anh nói, "nhưng bánh mì của bà là thứ duy nhất tôi có trong những ngày bụng trống."',
             '"You would not remember me," he said, "but your bread was the only thing I had on those empty days."'),
            ('"Bây giờ công ty tôi tài trợ bữa ăn cho 200 trẻ em mỗi ngày. Tất cả là vì mảnh bánh nhỏ của bà."',
             '"Now my company sponsors meals for 200 children each day. It all started from your small piece of bread."'),
            ('Từ một mảnh bánh vỡ, tình người đã nhân lên hai trăm lần.',
             'From one broken piece of bread, human kindness multiplied two hundred times.'),
        ],
        'lesson_vn': 'Bạn không thể biết một hành động nhỏ sẽ lan rộng đến đâu. Hãy cứ làm điều tốt — và để nhân quả lo phần còn lại.',
        'lesson_en': 'You cannot know how far a small act will spread. Just do good — and let karma take care of the rest.',
    },
    {
        'title_vn': 'Đứa Bé Và Người Già Ở Bến Tàu',
        'title_en': 'The Child and the Old Man at the Dock',
        'pairs': [
            ('Tại một bến tàu ở Nhật Bản, một cụ già đang loay hoay với túi hành lý nặng.',
             'At a dock in Japan, an old man was struggling with heavy luggage.'),
            ('Không ai dừng lại giúp — trừ một cậu bé tám tuổi đang đi cùng mẹ.',
             'No one stopped to help — except an eight-year-old boy walking with his mother.'),
            ('Cậu bé không đủ sức nâng túi lên, nhưng cậu dùng cả hai tay giữ túi không bị đổ cho đến khi cụ ổn định chỗ ngồi.',
             'The boy was not strong enough to lift the bag, but he used both hands to keep it from falling until the old man was settled.'),
            ('Cụ nhìn cậu bé và nói: "Cảm ơn con. Con có trái tim của người lớn."',
             'The old man looked at the boy and said: "Thank you, child. You have the heart of a grown man."'),
            ('Cậu bé không nghĩ gì nhiều — chỉ thấy người cần giúp thì giúp.',
             'The boy did not think much of it — he simply saw someone who needed help and helped.'),
            ('Nhưng người mẹ, quan sát tất cả, kể lại câu chuyện này mãi cho con nghe sau này, như bài học về điều tốt không cần tính toán.',
             'But the mother, watching everything, retold this story to her son for years, as a lesson about goodness that needs no calculation.'),
        ],
        'lesson_vn': 'Điều tốt đẹp nhất thường đến từ sự tự nhiên — không tính toán, không chờ cơ hội, chỉ đơn giản là thấy và làm.',
        'lesson_en': 'The finest good often comes naturally — no calculation, no waiting for the right moment, simply seeing and doing.',
    },
    {
        'title_vn': 'Vườn Hoa Của Người Tù',
        'title_en': 'The Prisoner\'s Flower Garden',
        'pairs': [
            ('Nelson Mandela bị giam 27 năm trên đảo Robben. Trong suốt thời gian đó, ông chăm sóc một vườn rau nhỏ trong sân tù.',
             'Nelson Mandela was imprisoned for 27 years on Robben Island. Throughout that time, he tended a small vegetable garden in the prison yard.'),
            ('Ông chia sẻ rau quả với các tù nhân khác — kể cả những người từng đối xử tàn nhẫn với ông.',
             'He shared the produce with other prisoners — including those who had treated him harshly.'),
            ('Một lính gác hỏi: "Sao ông cho cả kẻ ghét ông?"',
             'A guard asked: "Why do you give even to those who hate you?"'),
            ('Mandela trả lời: "Bởi vì khi tôi ra khỏi đây, tôi muốn mang theo người dẫn đường — không phải người tù."',
             'Mandela replied: "Because when I leave here, I want to carry a guide within me — not a prisoner."'),
            ('Khi ông trở thành tổng thống, ông mời một trong những cai tù cũ dự lễ nhậm chức.',
             'When he became president, he invited one of his former guards to the inauguration.'),
            ('Điều ông gieo trong vườn rau nhỏ bé ở Robben Island đã trổ bông thành tha thứ và hòa giải cho cả một dân tộc.',
             'What he sowed in that small garden on Robben Island blossomed into forgiveness and reconciliation for an entire nation.'),
        ],
        'lesson_vn': 'Gieo điều tốt ngay cả trong hoàn cảnh xấu nhất. Đất tốt hay xấu không quan trọng bằng hạt giống bạn chọn gieo.',
        'lesson_en': 'Sow good even in the worst circumstances. Whether the soil is good or bad matters less than the seed you choose to plant.',
    },
    {
        'title_vn': 'Bác Sĩ Và Người Bệnh Không Tiền',
        'title_en': 'The Doctor and the Penniless Patient',
        'pairs': [
            ('Bác sĩ Albert gặp một người bệnh nặng không có tiền đóng viện phí. Ông điều trị miễn phí.',
             'Dr. Albert encountered a seriously ill patient who could not afford hospital fees. He treated him for free.'),
            ('Người đồng nghiệp hỏi: "Anh làm vậy để được gì?"',
             'A colleague asked: "What do you gain by doing this?"'),
            ('Albert trả lời: "Tôi không biết. Nhưng tôi biết nếu không làm thì tôi sẽ mất điều gì đó quan trọng hơn tiền."',
             'Albert replied: "I don\'t know. But I know that if I don\'t, I will lose something more important than money."'),
            ('Năm năm sau, người bệnh ấy trở lại — lần này không phải để điều trị, mà để giới thiệu một tổ chức từ thiện tài trợ cho phòng khám của Albert.',
             'Five years later, the patient returned — not for treatment, but to introduce a charitable organization that would fund Albert\'s clinic.'),
            ('"Tôi không quên ơn anh. Và tôi muốn điều anh đã làm cho tôi được làm cho nhiều người hơn."',
             '"I have not forgotten your kindness. And I want what you did for me to reach more people."'),
            ('Một trái tim rộng mở không bao giờ trống rỗng lâu.',
             'An open heart is never empty for long.'),
        ],
        'lesson_vn': 'Khi bạn cho đi chân thành, cuộc sống tìm cách hoàn trả — đôi khi theo những đường vòng bạn không ngờ tới.',
        'lesson_en': 'When you give sincerely, life finds a way to repay — sometimes through paths you never expected.',
    },
    {
        'title_vn': 'Người Thầy Và Học Sinh Khó Tính',
        'title_en': 'The Teacher and the Difficult Student',
        'pairs': [
            ('Thầy Kane có một học sinh liên tục gây rối, chống đối, không chịu học. Nhưng thầy không bỏ cuộc.',
             'Teacher Kane had a student who constantly caused trouble, resisted authority, and refused to study. But the teacher did not give up.'),
            ('Mỗi ngày thầy tìm thấy một điều tốt nhỏ trong cậu bé và khen ngợi thật lòng.',
             'Each day the teacher found one small good thing in the boy and praised it sincerely.'),
            ('Tháng đầu, cậu bé tỏ ra không quan tâm. Tháng thứ hai, cậu bắt đầu hỏi bài. Tháng thứ ba, cậu ở lại sau giờ học để nói chuyện với thầy.',
             'The first month, the boy seemed indifferent. The second month, he began asking questions. The third month, he stayed after class to talk.'),
            ('"Thầy là người đầu tiên không bỏ em," cậu bé nói.',
             '"You are the first person who did not give up on me," the boy said.'),
            ('Hai mươi năm sau, ông trở thành hiệu trưởng một trường học và dành cả đời dạy những học sinh khó tính nhất.',
             'Twenty years later, he became a school principal and devoted his life to teaching the most difficult students.'),
            ('Vì năm đó, một người đã không bỏ cuộc với ông.',
             'Because that year, one person did not give up on him.'),
        ],
        'lesson_vn': 'Kiên nhẫn và thiện chí không bao giờ lãng phí. Chúng gieo mầm ở những nơi tưởng như khô cằn nhất.',
        'lesson_en': 'Patience and goodwill are never wasted. They plant seeds even in the most barren-seeming places.',
    },
]

# ============================================================
# CHƯƠNG 2: Hành Động Nhỏ, Hệ Quả Lớn
# ============================================================
ch02_stories = [
    {
        'title_vn': 'Cái Đinh Và Vương Quốc',
        'title_en': 'The Nail and the Kingdom',
        'pairs': [
            ('Có một câu tục ngữ cổ kể rằng: vì mất một cái đinh, móng ngựa bị tuột; vì mất móng ngựa, con ngựa bị ngã;',
             'An old proverb tells: for want of a nail, the horseshoe was lost; for want of a horseshoe, the horse was lost;'),
            ('vì mất con ngựa, người kỵ sĩ bị thương; vì mất người kỵ sĩ, trận chiến thua; vì thua trận, vương quốc sụp đổ.',
             'for want of a horse, the rider was injured; for want of a rider, the battle was lost; for want of a battle, the kingdom fell.'),
            ('Tất cả chỉ vì một cái đinh nhỏ không được đóng đúng chỗ.',
             'All for the want of a small nail not properly driven.'),
            ('Lịch sử đầy những bước ngoặt xuất phát từ chi tiết tưởng như vô nghĩa.',
             'History is full of turning points born from seemingly insignificant details.'),
            ('Một hành động nhỏ — đúng lúc, đúng chỗ — có thể viết lại tất cả.',
             'A small action — at the right moment, in the right place — can rewrite everything.'),
        ],
        'lesson_vn': 'Đừng xem thường điều nhỏ. Một chi tiết bỏ qua có thể là mắt xích mà tất cả phụ thuộc vào.',
        'lesson_en': 'Never underestimate the small. One overlooked detail may be the link everything else depends on.',
    },
    {
        'title_vn': 'Rosa Parks Và Chiếc Ghế Xe Buýt',
        'title_en': 'Rosa Parks and the Bus Seat',
        'pairs': [
            ('Ngày 1 tháng 12 năm 1955, Rosa Parks — một phụ nữ da đen mệt mỏi sau một ngày làm việc dài — từ chối nhường ghế trên xe buýt cho người da trắng.',
             'On December 1, 1955, Rosa Parks — a tired Black woman after a long workday — refused to give up her bus seat to a white passenger.'),
            ('Đó là một hành động nhỏ, thầm lặng. Không có bài diễn văn. Không có đám đông. Chỉ là một người phụ nữ quyết định không đứng dậy.',
             'It was a small, quiet action. No speech. No crowd. Just one woman deciding not to stand up.'),
            ('Nhưng hành động đó châm ngòi cho Phong trào Dân quyền, dẫn đến việc Martin Luther King Jr. nổi lên, và cuối cùng thay đổi bộ mặt nước Mỹ.',
             'But that action ignited the Civil Rights Movement, led to the rise of Martin Luther King Jr., and ultimately changed the face of America.'),
            ('Rosa Parks sau này nói: "Tôi không lên kế hoạch gì cả. Tôi chỉ mệt quá rồi."',
             'Rosa Parks later said: "I had not planned anything. I was just too tired."'),
            ('Sự mệt mỏi chân thật của một người bình thường đã viết nên lịch sử.',
             'The honest exhaustion of an ordinary person wrote history.'),
        ],
        'lesson_vn': 'Những hành động thay đổi thế giới thường không xuất phát từ anh hùng đặc biệt — mà từ người bình thường đứng vào đúng khoảnh khắc.',
        'lesson_en': 'World-changing actions rarely come from special heroes — but from ordinary people standing in the right moment.',
    },
    {
        'title_vn': 'Đứa Bé Ném Sao Biển',
        'title_en': 'The Child Throwing Starfish',
        'pairs': [
            ('Sau cơn bão, hàng nghìn con sao biển bị dạt vào bờ, chờ chết dưới ánh mặt trời.',
             'After a storm, thousands of starfish were washed ashore, dying under the sun.'),
            ('Một người đi bộ trên bãi thấy một cậu bé đang nhặt từng con ném trở lại biển.',
             'A man walking the beach saw a boy picking up starfish one by one and throwing them back into the sea.'),
            ('"Cháu làm gì vậy? Có cả nghìn con — cháu không thể cứu hết được đâu."',
             '"What are you doing? There are thousands of them — you cannot save them all."'),
            ('Cậu bé nhặt thêm một con, ném ra biển, rồi quay lại: "Nhưng cháu vừa cứu được con này."',
             'The boy picked up another, threw it into the sea, and turned back: "But I just saved this one."'),
            ('Người đi bộ lặng im. Rồi ông cúi xuống và bắt đầu nhặt cùng.',
             'The man fell silent. Then he bent down and began picking up starfish too.'),
            ('Một hành động nhỏ không chỉ cứu được một con sao biển — nó còn thức tỉnh được một người lớn.',
             'One small action not only saved one starfish — it also awakened one grown man.'),
        ],
        'lesson_vn': 'Bạn không thể giải quyết tất cả. Nhưng với người bạn giúp được hôm nay, điều đó có nghĩa là tất cả.',
        'lesson_en': 'You cannot solve everything. But for the one you help today, it means everything.',
    },
    {
        'title_vn': 'Bức Thư Chưa Gửi',
        'title_en': 'The Unsent Letter',
        'pairs': [
            ('Năm 1940, một nhà khoa học trẻ chuẩn bị bỏ cuộc vì liên tục thất bại trong nghiên cứu.',
             'In 1940, a young scientist was about to give up after repeated failures in his research.'),
            ('Tối hôm đó, ông nhận được một phong bì không tên người gửi, bên trong chỉ có một dòng chữ: "Đừng dừng lại. Bạn đang gần đến nơi rồi."',
             'That evening, he received an unmarked envelope containing only one line: "Do not stop. You are almost there."'),
            ('Không biết ai gửi, nhưng ông tiếp tục. Hai năm sau, ông công bố công trình thay đổi lĩnh vực của mình.',
             'Not knowing who sent it, he continued. Two years later, he published work that changed his field.'),
            ('Mười năm sau, ông gặp một người bạn cũ và đề cập bức thư.',
             'Ten years later, he met an old friend and mentioned the letter.'),
            ('Người bạn ngờ ngợ: "Bức thư... tôi gửi đó. Tôi chỉ nghĩ anh cần một lời khích lệ thôi."',
             'The friend hesitated: "That letter... I sent it. I just thought you needed some encouragement."'),
            ('Một hành động bốc đồng mất năm phút đã thay đổi cả một cuộc đời khoa học.',
             'An impulsive act taking five minutes changed an entire scientific career.'),
        ],
        'lesson_vn': 'Một lời động viên đúng lúc có thể là tất cả sự khác biệt giữa ai đó bỏ cuộc và tiếp tục.',
        'lesson_en': 'One word of encouragement at the right moment can be all the difference between someone giving up and carrying on.',
    },
    {
        'title_vn': 'Hạt Cà Phê Ở Ethiopia',
        'title_en': 'The Coffee Bean in Ethiopia',
        'pairs': [
            ('Truyền thuyết kể rằng vào thế kỷ thứ 9, một người chăn dê tên Kaldi nhận thấy dê của mình trở nên vô cùng năng động sau khi ăn quả đỏ của một cây lạ.',
             'Legend tells that in the 9th century, a goat herder named Kaldi noticed his goats became extraordinarily energetic after eating red berries from an unknown tree.'),
            ('Kaldi mang quả đó đến một tu viện gần đó.',
             'Kaldi brought the berries to a nearby monastery.'),
            ('Các tu sĩ thử nấu chúng thành thức uống — và cà phê ra đời.',
             'The monks brewed them into a drink — and coffee was born.'),
            ('Từ một quan sát nhỏ của người chăn dê, một đồ uống đã lan ra toàn thế giới và ngày nay nuôi sống hàng trăm triệu người.',
             'From one small observation by a goat herder, a drink spread across the world and today sustains hundreds of millions of people.'),
            ('Hành động nhỏ nhất — chú ý, tò mò, chia sẻ — có thể mở ra những cánh cửa không tưởng.',
             'The smallest action — noticing, being curious, sharing — can open unimaginable doors.'),
        ],
        'lesson_vn': 'Mỗi phát minh vĩ đại đều bắt đầu từ sự chú ý đến một điều nhỏ mà người khác bỏ qua.',
        'lesson_en': 'Every great invention begins with paying attention to something small that others overlook.',
    },
    {
        'title_vn': 'Người Trồng Cây Trên Sa Mạc',
        'title_en': 'The Man Who Planted Trees in the Desert',
        'pairs': [
            ('Wangari Maathai bắt đầu bằng việc trồng bảy cây trong vườn nhà mình ở Kenya vào năm 1977.',
             'Wangari Maathai began by planting seven trees in her own backyard in Kenya in 1977.'),
            ('Hàng xóm hỏi: "Chị làm vậy để làm gì?"',
             'Neighbors asked: "Why are you doing this?"'),
            ('"Để bóng mát," bà trả lời đơn giản.',
             '"For shade," she answered simply.'),
            ('Nhưng hành động đó truyền cảm hứng cho phụ nữ khác. Rồi cả cộng đồng. Rồi cả nước.',
             'But that action inspired other women. Then the whole community. Then the entire country.'),
            ('Đến năm 2004, Phong trào Vành đai Xanh của bà đã trồng hơn 30 triệu cây trên khắp châu Phi.',
             'By 2004, her Green Belt Movement had planted over 30 million trees across Africa.'),
            ('Wangari Maathai giành giải Nobel Hòa bình. Tất cả bắt đầu từ bảy cây trong vườn nhà.',
             'Wangari Maathai won the Nobel Peace Prize. It all began with seven trees in a backyard.'),
        ],
        'lesson_vn': 'Đừng chờ đủ lực để làm điều lớn. Hãy làm điều nhỏ ngay bây giờ — và để nó lớn lên.',
        'lesson_en': 'Do not wait until you are strong enough to do something big. Do something small now — and let it grow.',
    },
    {
        'title_vn': 'Bước Chân Đầu Tiên Lên Mặt Trăng',
        'title_en': 'The First Step on the Moon',
        'pairs': [
            ('Ngày 20 tháng 7 năm 1969, Neil Armstrong đặt chân lên Mặt Trăng và nói: "Đây là một bước chân nhỏ của con người, nhưng là một bước tiến vĩ đại của nhân loại."',
             'On July 20, 1969, Neil Armstrong stepped onto the Moon and said: "That\'s one small step for man, one giant leap for mankind."'),
            ('Nhưng bước chân đó không phát sinh từ không khí.',
             'But that step did not arise from thin air.'),
            ('Nó đòi hỏi 400.000 kỹ sư, nhà khoa học, làm việc suốt một thập kỷ, mỗi người hoàn thành phần việc nhỏ của mình.',
             'It required 400,000 engineers and scientists working for a decade, each completing their small part.'),
            ('Một kỹ sư kể lại: "Tôi chỉ chịu trách nhiệm cho một con bulong. Nhưng tôi biết con bulong đó giữ cho phi hành gia sống."',
             'One engineer recalled: "I was only responsible for one bolt. But I knew that bolt kept the astronaut alive."'),
            ('Mỗi người làm tốt phần nhỏ của mình — đó là cách thế giới đặt chân lên Mặt Trăng.',
             'Each person doing their small part well — that is how the world set foot on the Moon.'),
        ],
        'lesson_vn': 'Bạn không cần là người duy nhất làm tất cả. Chỉ cần làm tốt phần nhỏ của bạn — và nó sẽ là một phần của điều vĩ đại.',
        'lesson_en': 'You do not need to do everything alone. Just do your small part well — and it will be part of something great.',
    },
    {
        'title_vn': 'Cô Giáo Và Bức Vẽ',
        'title_en': 'The Teacher and the Drawing',
        'pairs': [
            ('Tại một lớp học nghèo ở Ấn Độ, cô giáo Sunita nhận thấy một học sinh luôn ngồi cuối lớp và vẽ lên sách vở.',
             'In a poor school in India, teacher Sunita noticed a student who always sat at the back, drawing in his notebooks.'),
            ('Thay vì phạt, cô hỏi: "Em có thể vẽ một bức lên bảng không?"',
             'Instead of punishing him, she asked: "Can you draw something on the board?"'),
            ('Cậu bé ngạc nhiên, run run đi lên và vẽ một cảnh làng quê tuyệt đẹp.',
             'The boy, surprised, walked up trembling and drew a breathtaking village scene.'),
            ('Cả lớp trầm trồ. Lần đầu tiên trong đời, cậu bé được vỗ tay.',
             'The class was awestruck. For the first time in his life, the boy was applauded.'),
            ('Cô giáo chỉ làm một điều nhỏ: chú ý và hỏi.',
             'The teacher did one small thing: notice and ask.'),
            ('Cậu bé đó sau này trở thành một trong những họa sĩ nổi tiếng nhất vùng, và luôn kể câu chuyện ấy cho các học trò của mình.',
             'That boy later became one of the most famous artists in the region, and always told that story to his own students.'),
        ],
        'lesson_vn': 'Đôi khi một câu hỏi đúng lúc có sức mạnh thay đổi một cuộc đời hơn cả nghìn bài giảng.',
        'lesson_en': 'Sometimes one timely question holds more power to change a life than a thousand lectures.',
    },
    {
        'title_vn': 'Hòn Đá Và Con Suối',
        'title_en': 'The Stone and the Stream',
        'pairs': [
            ('Nước không thể xuyên qua đá bằng sức mạnh. Nhưng nước có thể làm mòn đá bằng sự kiên trì.',
             'Water cannot break through stone by force. But water can wear away stone through persistence.'),
            ('Một nhà nghiên cứu đặt một viên đá dưới dòng chảy nhỏ và đo sự thay đổi sau mỗi năm.',
             'A researcher placed a stone under a small stream and measured the change after each year.'),
            ('Năm đầu, không thể thấy sự khác biệt bằng mắt thường.',
             'The first year, no difference was visible to the naked eye.'),
            ('Năm thứ mười, viên đá đã bị mòn một phần ba.',
             'By the tenth year, the stone had worn away by one third.'),
            ('Năm thứ ba mươi, viên đá không còn nhận ra được nữa.',
             'By the thirtieth year, the stone was unrecognizable.'),
            ('Mỗi giọt nước chỉ là một giọt — nhưng sự lặp đi lặp lại của nó tạo ra thứ mà không có sức lực nào phá được.',
             'Each drop of water is just a drop — but its repetition creates what no force can break.'),
        ],
        'lesson_vn': 'Không cần sức mạnh lớn. Chỉ cần hành động nhỏ, lặp đi lặp lại đúng hướng, đủ lâu.',
        'lesson_en': 'No great force is needed. Only small actions, repeated in the right direction, for long enough.',
    },
    {
        'title_vn': 'Nụ Cười Của Người Xa Lạ',
        'title_en': 'The Stranger\'s Smile',
        'pairs': [
            ('Mark Howden kể lại: ngày anh bước ra cầu để kết thúc cuộc đời, một người phụ nữ xa lạ đan vai đi ngang nhìn anh và nở nụ cười.',
             'Mark Howden recounted: the day he walked onto a bridge to end his life, a stranger walking by glanced at him and offered a smile.'),
            ('Không ai biết anh đang đứng ở đầu vực. Người phụ nữ chỉ mỉm cười như người ta thường làm.',
             'No one knew he was standing at the edge. The woman simply smiled as people sometimes do.'),
            ('Nhưng anh nói: "Nụ cười đó nhắc tôi rằng có người thấy tôi. Tôi không vô hình."',
             'But he said: "That smile reminded me that someone saw me. I was not invisible."'),
            ('Anh bước xuống và gọi điện thoại cho đường dây khủng hoảng.',
             'He stepped down and called a crisis line.'),
            ('Ngày hôm nay anh là nhà hoạt động vận động sức khỏe tâm thần.',
             'Today he is a mental health advocate.'),
            ('Người phụ nữ kia không bao giờ biết nụ cười của mình đã làm được điều gì.',
             'That woman never knew what her smile had done.'),
        ],
        'lesson_vn': 'Bạn không bao giờ biết hành động nhỏ của mình đang tiếp chạm ai và đang thay đổi gì. Vì vậy hãy cứ tử tế.',
        'lesson_en': 'You never know whose life your small act is touching and what it is changing. So just be kind.',
    },
]

# ============================================================
# CHƯƠNG 3: Thói Quen Tạo Nên Số Phận
# ============================================================
ch03_stories = [
    {
        'title_vn': 'Aristotle Và Người Thanh Niên',
        'title_en': 'Aristotle and the Young Man',
        'pairs': [
            ('Một thanh niên đến gặp Aristotle và hỏi: "Làm thế nào để trở nên xuất sắc?"',
             'A young man came to Aristotle and asked: "How does one become excellent?"'),
            ('Aristotle trả lời: "Chúng ta là những gì chúng ta liên tục làm. Sự xuất sắc không phải là một hành động, mà là một thói quen."',
             'Aristotle replied: "We are what we repeatedly do. Excellence is not an act, but a habit."'),
            ('Thanh niên bối rối: "Vậy tôi nên bắt đầu từ đâu?"',
             'The young man was puzzled: "Then where do I begin?"'),
            ('"Bắt đầu từ hành động nhỏ nhất mà nếu lặp lại mỗi ngày sẽ tạo ra người bạn muốn trở thành."',
             '"Begin with the smallest action that, repeated daily, will create the person you wish to become."'),
            ('Thanh niên đó trở về và bắt đầu đọc mười trang sách mỗi ngày — một thói quen nhỏ.',
             'The young man returned home and began reading ten pages a day — one small habit.'),
            ('Mười năm sau, ông trở thành học giả uyên bác nhất vùng.',
             'Ten years later, he became the most learned scholar in the region.'),
        ],
        'lesson_vn': 'Bạn không cần thay đổi bản thân ngay lập tức. Chỉ cần thay đổi một thói quen nhỏ mỗi ngày — và năm tháng sẽ thay đổi còn lại.',
        'lesson_en': 'You do not need to change yourself immediately. Just change one small habit each day — and time will change the rest.',
    },
    {
        'title_vn': 'Benjamin Franklin Và Cuốn Sổ Nhỏ',
        'title_en': 'Benjamin Franklin and the Little Notebook',
        'pairs': [
            ('Năm hai mươi tuổi, Benjamin Franklin tự đặt ra mục tiêu trở thành người hoàn hảo về đạo đức.',
             'At the age of twenty, Benjamin Franklin set himself the goal of becoming morally perfect.'),
            ('Ông liệt kê 13 đức tính và mỗi tuần tập trung rèn luyện một đức tính.',
             'He listed 13 virtues and focused on practicing one each week.'),
            ('Trong cuốn sổ nhỏ, mỗi đêm ông đánh dấu những lần mình vi phạm đức tính đó.',
             'In a small notebook, each night he marked the times he had violated that virtue.'),
            ('Ông không bao giờ đạt được sự hoàn hảo. Nhưng vì cố gắng, ông trở thành nhà khoa học, nhà ngoại giao, và nhà tư tưởng lớn nhất của nước Mỹ thế kỷ 18.',
             'He never achieved perfection. But in striving, he became the greatest scientist, diplomat, and thinker of 18th-century America.'),
            ('Ông viết: "Tôi có thể chưa đạt được sự hoàn hảo, nhưng tôi đã trở nên tốt hơn và hạnh phúc hơn nhờ nỗ lực đó."',
             'He wrote: "I may not have achieved perfection, but I became better and happier through the effort."'),
        ],
        'lesson_vn': 'Không cần hoàn hảo. Chỉ cần hệ thống. Thói quen đơn giản, duy trì nhất quán, tạo ra người vĩ đại.',
        'lesson_en': 'Perfection is not required. Only a system. Simple habits, consistently maintained, create great people.',
    },
    {
        'title_vn': 'Edith Hamilton Và Tiếng Hy Lạp',
        'title_en': 'Edith Hamilton and Greek',
        'pairs': [
            ('Edith Hamilton bắt đầu học tiếng Hy Lạp cổ đại khi đã 63 tuổi — sau khi nghỉ hưu khỏi nghề giáo.',
             'Edith Hamilton began learning ancient Greek at age 63 — after retiring from teaching.'),
            ('Bạn bè ngạc nhiên: "Ở tuổi này học làm gì?"',
             'Friends were surprised: "Why learn at this age?"'),
            ('"Bởi vì tôi muốn đọc Homer theo nguyên bản trước khi chết."',
             '"Because I want to read Homer in the original before I die."'),
            ('Bà dành mỗi buổi sáng học một tiếng. Mỗi chiều đọc một đoạn.',
             'She spent each morning studying for one hour. Each afternoon reading a passage.'),
            ('Năm năm sau, bà xuất bản cuốn sách về văn minh Hy Lạp — trở thành kinh điển được dạy ở hàng nghìn trường đại học.',
             'Five years later, she published a book on Greek civilization — which became a classic taught at thousands of universities.'),
            ('Không bao giờ là quá muộn để xây dựng thói quen và viết trang tiếp theo của cuộc đời mình.',
             'It is never too late to build a habit and write the next chapter of your life.'),
        ],
        'lesson_vn': 'Tuổi tác không quyết định bạn có thể học gì hay trở thành ai. Thói quen kiên trì có thể thay đổi mọi thứ — ở bất kỳ tuổi nào.',
        'lesson_en': 'Age does not decide what you can learn or become. Persistent habits can change everything — at any age.',
    },
    {
        'title_vn': 'Người Thợ Rèn Và Thanh Sắt',
        'title_en': 'The Blacksmith and the Iron Bar',
        'pairs': [
            ('Một người thợ rèn già dạy học trò: "Sắt nguội không thể uốn được. Sắt nóng dễ uốn — nhưng nếu bạn không giữ hình ngay, nó sẽ nguội lại thành dạng cũ."',
             'An old blacksmith taught his apprentice: "Cold iron cannot be bent. Hot iron bends easily — but if you do not hold its shape at once, it will cool back to its old form."'),
            ('"Thói quen cũng vậy," ông nói. "Não người là như sắt — nóng, dễ thay đổi; nguội, rất cứng đầu."',
             '"Habits are the same," he said. "The human brain is like iron — hot, easy to change; cold, very stubborn."'),
            ('"Khi bạn quyết định thay đổi, đó là lúc sắt đang nóng. Hãy hành động ngay lập tức, không chờ đợi."',
             '"When you decide to change, that is when the iron is hot. Act immediately, do not wait."'),
            ('Học trò hỏi: "Bao lâu thì thói quen thành hình?"',
             'The apprentice asked: "How long before a habit takes shape?"'),
            ('"Đủ lâu để không còn phải nghĩ đến nó nữa. Lúc đó nó đã là bạn."',
             '"Long enough that you no longer have to think about it. Then it has become you."'),
        ],
        'lesson_vn': 'Khi bạn cảm thấy có động lực để thay đổi — hãy hành động ngay. Đó là lúc sắt đang nóng nhất.',
        'lesson_en': 'When you feel motivated to change — act immediately. That is when the iron is hottest.',
    },
    {
        'title_vn': 'Hiro Và Nghệ Thuật Gấp Giấy',
        'title_en': 'Hiro and the Art of Origami',
        'pairs': [
            ('Hiro Yamagata là người tị nạn Việt Nam đến Nhật Bản năm 1979 không biết tiếng Nhật, không quen biết ai.',
             'Hiro Yamagata was a Vietnamese refugee who arrived in Japan in 1979 knowing no Japanese, with no connections.'),
            ('Ông bắt đầu gấp origami mỗi buổi tối — một thứ duy nhất ông có thể làm mà không cần ngôn ngữ.',
             'He began folding origami each evening — the one thing he could do without language.'),
            ('Mỗi đêm một con. Sau một năm, ông có 365 con hạc.',
             'One piece each night. After one year, he had 365 cranes.'),
            ('Ông xếp chúng vào hộp và tặng cho bệnh viện nơi ông làm tình nguyện.',
             'He arranged them in a box and donated them to the hospital where he volunteered.'),
            ('Một nhà báo viết bài về ông. Câu chuyện lan rộng. Ông nhận được học bổng học nghệ thuật.',
             'A journalist wrote about him. The story spread. He received an art scholarship.'),
            ('Thói quen gấp giấy mỗi đêm đã gấp lại cả cuộc đời của ông.',
             'The habit of folding paper each night had folded his entire life into a new shape.'),
        ],
        'lesson_vn': 'Thói quen nhỏ không chỉ xây dựng kỹ năng — nó xây dựng bản sắc, mở ra cơ hội, và đôi khi thay đổi hoàn toàn quỹ đạo cuộc đời.',
        'lesson_en': 'Small habits do not only build skills — they build identity, open opportunities, and sometimes completely change the trajectory of a life.',
    },
    {
        'title_vn': 'Người Chạy Bộ Lúc 5 Giờ Sáng',
        'title_en': 'The 5 AM Runner',
        'pairs': [
            ('David Goggins từng nặng 130kg, trầm cảm, và không có tương lai rõ ràng.',
             'David Goggins once weighed 130kg, was depressed, and had no clear future.'),
            ('Ông bắt đầu bằng việc chạy bộ mỗi sáng lúc 5 giờ — dù chỉ 10 phút.',
             'He began by running each morning at 5 AM — even if only for 10 minutes.'),
            ('"Tôi không thể chạy xa. Nhưng tôi có thể ra khỏi giường," ông nói.',
             '"I could not run far. But I could get out of bed," he said.'),
            ('Dần dần 10 phút thành 30, rồi một tiếng, rồi mỗi ngày.',
             'Gradually 10 minutes became 30, then an hour, then a daily practice.'),
            ('Sau nhiều năm, ông trở thành một trong những vận động viên sức bền khắc nghiệt nhất thế giới — hoàn thành nhiều cuộc đua siêu marathon.',
             'Years later, he became one of the world\'s most extreme endurance athletes — completing multiple ultramarathons.'),
            ('"Mọi thứ tôi có ngày hôm nay bắt đầu từ 10 phút chạy bộ lúc 5 giờ sáng với đôi chân đau và trái tim không muốn," ông nói.',
             '"Everything I have today started with 10 minutes of running at 5 AM with aching legs and an unwilling heart," he said.'),
        ],
        'lesson_vn': 'Không cần bắt đầu bằng cái gì lớn. Bắt đầu bằng điều nhỏ nhất bạn thực sự có thể làm hôm nay — và giữ nó.',
        'lesson_en': 'No need to start with something big. Begin with the smallest thing you can truly do today — and keep it.',
    },
    {
        'title_vn': 'Ngọc Trai Và Con Trai',
        'title_en': 'The Pearl and the Oyster',
        'pairs': [
            ('Ngọc trai không được tạo ra từ vàng bạc hay ánh sáng. Nó được tạo ra từ một hạt cát nhỏ lọt vào con trai.',
             'A pearl is not made from gold or light. It is created from a grain of sand that enters an oyster.'),
            ('Con trai không trục xuất hạt cát — nó bao bọc nó, lớp này qua lớp khác, cho đến khi hạt cát trở thành ngọc.',
             'The oyster does not expel the grain — it wraps it, layer by layer, until the grain becomes a pearl.'),
            ('Một nhà tâm lý học dùng hình ảnh này để dạy bệnh nhân của mình: "Thói quen tốt cũng được tạo ra từ sự khó chịu nhỏ bạn lặp lại đến khi nó trở thành bạn."',
             'A psychologist used this image to teach patients: "Good habits are also created from small discomforts you repeat until they become you."'),
            ('Phòng tập gym khó chịu — nhưng sau 90 ngày, nó là nơi bạn muốn đến.',
             'The gym is uncomfortable — but after 90 days, it becomes a place you want to go.'),
            ('Thiền định buồn chán — nhưng sau 30 ngày, không có nó bạn thấy thiếu.',
             'Meditation is boring — but after 30 days, you feel its absence.'),
            ('Thói quen không hỏi bạn có muốn hay không — nó chỉ cần bạn lặp lại đủ lâu.',
             'A habit does not ask whether you want it — it only needs you to repeat it long enough.'),
        ],
        'lesson_vn': 'Người bạn muốn trở thành đang chờ ở phía bên kia của sự khó chịu bạn lặp lại đủ lần.',
        'lesson_en': 'The person you want to become is waiting on the other side of the discomfort you repeat enough times.',
    },
    {
        'title_vn': 'Người Không Ngủ Quá 6 Tiếng',
        'title_en': 'The Person Who Never Sleeps More Than 6 Hours',
        'pairs': [
            ('Leonardo da Vinci nổi tiếng với thói quen ngủ theo kiểu đa pha: ngủ bốn lần mỗi ngày, mỗi lần 90 phút.',
             'Leonardo da Vinci was famous for polyphasic sleeping: sleeping four times each day, 90 minutes each time.'),
            ('Điều này giải phóng thêm giờ để ông vẽ, giải phẫu, viết, nghiên cứu.',
             'This freed up extra hours for him to paint, study anatomy, write, and research.'),
            ('Không phải ai cũng cần ngủ như da Vinci. Nhưng điều quan trọng là ông có hệ thống.',
             'Not everyone needs to sleep like da Vinci. But the key is that he had a system.'),
            ('Ông không để ngày trôi qua ngẫu nhiên — ông thiết kế từng giờ.',
             'He did not let days pass randomly — he designed each hour.'),
            ('Nhật ký của ông ghi chép từng ý tưởng, từng quan sát, từng câu hỏi chưa trả lời — thói quen ghi chép giúp ông không quên bất cứ điều gì.',
             'His journals recorded every idea, every observation, every unanswered question — the habit of writing helped him forget nothing.'),
            ('Thiên tài của da Vinci không chỉ là tài năng bẩm sinh — nó là hệ thống thói quen cẩn thận ông xây dựng mỗi ngày.',
             'Da Vinci\'s genius was not only innate talent — it was the careful system of habits he built each day.'),
        ],
        'lesson_vn': 'Thiên tài không sống ngẫu nhiên. Họ thiết kế ngày của mình. Thói quen không phải xiềng xích — nó là bộ khung để tự do.',
        'lesson_en': 'Geniuses do not live randomly. They design their days. Habits are not chains — they are the framework for freedom.',
    },
    {
        'title_vn': 'Người Làm Vườn Bonsai',
        'title_en': 'The Bonsai Gardener',
        'pairs': [
            ('Nghệ thuật bonsai đòi hỏi sự kiên nhẫn tuyệt vời: một cây bonsai đẹp cần 20-50 năm chăm sóc.',
             'The art of bonsai demands extraordinary patience: a beautiful bonsai takes 20-50 years of care.'),
            ('Mỗi ngày người trồng bonsai chỉ làm một việc nhỏ: tưới nước, tỉa lá, quan sát.',
             'Each day the bonsai grower does one small thing: water, prune, observe.'),
            ('Không ngày nào tạo ra sự khác biệt rõ ràng. Nhưng sau mười năm, cây trở thành tác phẩm nghệ thuật sống.',
             'No single day makes a visible difference. But after ten years, the tree becomes a living work of art.'),
            ('Một người học bonsai hỏi thầy: "Bao giờ thì cây mới đẹp?"',
             'A bonsai student asked his master: "When will the tree be beautiful?"'),
            ('Thầy trả lời: "Khi bạn ngừng hỏi câu đó."',
             'The master replied: "When you stop asking that question."'),
            ('Thói quen đòi hỏi niềm tin rằng ngày hôm nay có ý nghĩa — dù bạn chưa thấy kết quả.',
             'Habits require the faith that today matters — even when you cannot yet see the result.'),
        ],
        'lesson_vn': 'Hãy tin vào quá trình. Kết quả không đến mỗi ngày — nhưng nó đến cho những người mỗi ngày đều làm phần việc của mình.',
        'lesson_en': 'Trust the process. Results do not come every day — but they come to those who do their part every day.',
    },
    {
        'title_vn': 'Thói Quen Của Một Bà Mẹ',
        'title_en': 'A Mother\'s Habit',
        'pairs': [
            ('Bà Maya Angelou, nhà thơ lớn của nước Mỹ, có thói quen viết mỗi buổi sáng từ 6 giờ đến 12 giờ — trong một căn phòng khách sạn rẻ tiền bà thuê riêng để viết.',
             'Maya Angelou, the great American poet, had a habit of writing each morning from 6 to 12 — in a cheap hotel room she rented just for writing.'),
            ('Bà không viết khi "cảm hứng đến". Bà viết khi đến giờ — dù có cảm hứng hay không.',
             'She did not write when "inspiration came." She wrote when it was time — whether inspired or not.'),
            ('"Nếu bạn chờ cảm hứng, bạn sẽ không bao giờ có đủ," bà nói.',
             '"If you wait for inspiration, you will never have enough," she said.'),
            ('Bà có sáu cuốn tự truyện, hàng chục tập thơ, và là người đọc thơ duy nhất được mời tại lễ nhậm chức của hai tổng thống Mỹ.',
             'She had six autobiographies, dozens of poetry collections, and was the only poet invited to read at two US presidential inaugurations.'),
            ('Tất cả được xây dựng từ thói quen viết sáu tiếng mỗi ngày — không phải chờ cảm hứng.',
             'All of it built from the habit of writing six hours each day — not waiting for inspiration.'),
        ],
        'lesson_vn': 'Cảm hứng đến khi bạn đang làm việc — không phải trước khi bạn bắt đầu. Thói quen tạo ra cảm hứng, không phải ngược lại.',
        'lesson_en': 'Inspiration comes while you are working — not before you begin. Habits create inspiration, not the other way around.',
    },
]

# ============================================================
# CHƯƠNG 4: Tôi Là Con Người Tôi Chọn
# ============================================================
ch04_stories = [
    {
        'title_vn': 'Viktor Frankl Trong Trại Tập Trung',
        'title_en': 'Viktor Frankl in the Concentration Camp',
        'pairs': [
            ('Viktor Frankl — nhà tâm lý học người Áo — bị giam trong các trại tập trung Đức Quốc Xã, trong đó có Auschwitz.',
             'Viktor Frankl — the Austrian psychiatrist — was imprisoned in Nazi concentration camps, including Auschwitz.'),
            ('Họ lấy đi tất cả: gia đình, tài sản, tự do, thậm chí quần áo và tên tuổi.',
             'They took everything from him: family, possessions, freedom, even his clothes and name.'),
            ('Nhưng có một thứ họ không thể lấy đi.',
             'But there was one thing they could not take.'),
            ('Ông viết: "Khi chúng ta không thể thay đổi hoàn cảnh, chúng ta bị thách thức để thay đổi bản thân."',
             'He wrote: "When we are no longer able to change a situation, we are challenged to change ourselves."'),
            ('"Giữa kích thích và phản ứng có một khoảng trống. Trong khoảng trống đó là quyền tự do và sức mạnh của chúng ta để chọn phản ứng của mình."',
             '"Between stimulus and response there is a space. In that space is our power and freedom to choose our response."'),
            ('Ngay cả trong cái địa ngục đó, ông chọn giúp đỡ những người tù khác, giữ phẩm giá, và giữ hy vọng.',
             'Even in that hell, he chose to help fellow prisoners, maintain dignity, and hold on to hope.'),
            ('Ông sống sót và viết cuốn sách "Đi Tìm Lẽ Sống" — một trong những tác phẩm có ảnh hưởng nhất thế kỷ 20.',
             'He survived and wrote "Man\'s Search for Meaning" — one of the most influential works of the 20th century.'),
        ],
        'lesson_vn': 'Hoàn cảnh có thể lấy đi tất cả — trừ quyền chọn thái độ của bạn. Đó là tự do cuối cùng và không ai có thể cướp đi.',
        'lesson_en': 'Circumstances can take everything — except your right to choose your attitude. That is the last freedom and no one can take it away.',
    },
    {
        'title_vn': 'Nelson Mandela Chọn Tha Thứ',
        'title_en': 'Nelson Mandela Chooses Forgiveness',
        'pairs': [
            ('Sau 27 năm tù, Nelson Mandela bước ra khỏi nhà tù Víctor Verster.',
             'After 27 years in prison, Nelson Mandela walked out of Victor Verster Prison.'),
            ('Đám đông chờ đợi ông với kỳ vọng về sự trả thù và cách mạng bạo lực.',
             'The crowd awaited him expecting revenge and violent revolution.'),
            ('Nhưng Mandela nói: "Khi tôi bước qua cánh cổng đó tôi biết rằng nếu tôi không để lại sự đắng cay và căm thù ở lại bên trong thì tôi vẫn còn là tù nhân."',
             'But Mandela said: "As I walked out the door toward the gate that would lead to my freedom, I knew if I didn\'t leave my bitterness and hatred behind, I\'d still be in prison."'),
            ('Đó không phải là sự yếu đuối. Đó là lựa chọn có ý thức của người hiểu rằng hận thù phá hủy người mang nó nhiều hơn người bị ghét.',
             'That was not weakness. It was the conscious choice of a man who understood that hatred destroys the one who carries it more than the one it targets.'),
            ('Ông trở thành tổng thống và xây dựng chính sách hòa giải thay vì trả thù.',
             'He became president and built a policy of reconciliation instead of revenge.'),
            ('Nam Phi thoát khỏi nội chiến phần lớn nhờ lựa chọn của một người.',
             'South Africa escaped civil war largely because of one man\'s choice.'),
        ],
        'lesson_vn': 'Tha thứ là hành động dũng cảm nhất — không phải vì người kia xứng đáng, mà vì bạn xứng đáng được tự do.',
        'lesson_en': 'Forgiveness is the bravest act — not because the other deserves it, but because you deserve freedom.',
    },
    {
        'title_vn': 'Epictetus — Người Nô Lệ Tự Do',
        'title_en': 'Epictetus — The Free Slave',
        'pairs': [
            ('Epictetus sinh ra là nô lệ ở La Mã. Chủ của ông tra tấn ông, gãy chân ông.',
             'Epictetus was born a slave in Rome. His master tortured him, breaking his leg.'),
            ('Khi chủ nhà vặn chân ông, Epictetus điềm tĩnh nói: "Anh sắp gãy nó rồi."',
             'As his master twisted his leg, Epictetus calmly said: "You are about to break it."'),
            ('Xương gãy. Ông nói: "Tôi đã nói với anh rồi."',
             'The bone broke. He said: "I told you so."'),
            ('Không la hét. Không cầu xin. Không tuyệt vọng.',
             'No screaming. No begging. No despair.'),
            ('Sau này, ông trở thành triết gia vĩ đại nhất về Khắc Kỷ và dạy: "Đừng yêu cầu điều xảy ra theo ý muốn của bạn; hãy muốn điều xảy ra theo cách nó xảy ra, và bạn sẽ bình an."',
             'Later, he became the greatest Stoic philosopher and taught: "Seek not that the things which happen should happen as you wish; but wish the things which happen to be as they are, and you will have a tranquil flow of life."'),
            ('Một người nô lệ về thân xác đã trở thành người tự do nhất về tâm hồn.',
             'A slave in body became the most free in spirit.'),
        ],
        'lesson_vn': 'Tự do thực sự không phải là hoàn cảnh bên ngoài — mà là quyền năng bên trong bạn để chọn cách bạn đáp lại thế giới.',
        'lesson_en': 'True freedom is not external circumstances — it is the inner power within you to choose how you respond to the world.',
    },
    {
        'title_vn': 'Helen Keller Chọn Ánh Sáng',
        'title_en': 'Helen Keller Chooses Light',
        'pairs': [
            ('Helen Keller mất cả thị giác lẫn thính giác khi 19 tháng tuổi do bệnh tật.',
             'Helen Keller lost both her sight and hearing at 19 months old due to illness.'),
            ('Cô lớn lên trong thế giới tối và câm lặng hoàn toàn, không thể giao tiếp và thường xuyên nổi cơn thịnh nộ.',
             'She grew up in a world of complete darkness and silence, unable to communicate, and frequently in rage.'),
            ('Khi cô giáo Anne Sullivan đến, mọi thứ thay đổi — không phải vì hoàn cảnh thay đổi, mà vì Helen chọn học.',
             'When teacher Anne Sullivan arrived, everything changed — not because circumstances changed, but because Helen chose to learn.'),
            ('Cái khoảnh khắc Helen hiểu rằng "w-a-t-e-r" là nước chảy trên tay cô — cô cảm thấy như được tái sinh.',
             'The moment Helen understood that "w-a-t-e-r" was the water flowing over her hand — she felt reborn.'),
            ('Cô nói: "Tôi cảm ơn Chúa vì những chướng ngại vật của tôi, vì nhờ chúng tôi đã tìm thấy chính mình, công việc của mình và Chúa của mình."',
             'She said: "I thank God for my handicaps, for through them I have found myself, my work, and my God."'),
            ('Helen Keller tốt nghiệp đại học, viết sách, diễn thuyết toàn cầu và trở thành biểu tượng của ý chí con người.',
             'Helen Keller graduated from university, wrote books, spoke globally, and became a symbol of human will.'),
        ],
        'lesson_vn': 'Không ai chọn được hoàn cảnh họ sinh ra. Nhưng mọi người đều có thể chọn ai họ trở thành trong hoàn cảnh đó.',
        'lesson_en': 'No one chooses the circumstances of their birth. But everyone can choose who they become within those circumstances.',
    },
    {
        'title_vn': 'Người Cai Tù Và Người Tù',
        'title_en': 'The Prison Guard and the Prisoner',
        'pairs': [
            ('Trong truyện ngắn của Tolstoy, một tên cướp bị tống vào tù và thề sẽ trả thù tên cai tù đã bắt anh.',
             'In Tolstoy\'s short story, a thief is thrown into prison and vows to take revenge on the guard who captured him.'),
            ('Mỗi ngày anh nuôi dưỡng hận thù, mài sắc nó.', 'Each day he nurtured his hatred, sharpening it.'),
            ('Nhưng mười năm trôi qua. Anh được thả. Tên cai tù đã già yếu và không còn nhớ anh.',
             'But ten years passed. He was released. The guard was old and frail and no longer remembered him.'),
            ('Người tù nhận ra: ông ta đã ngồi tù thật sự trong suốt mười năm đó — không phải trong tường đá, mà trong hận thù của mình.',
             'The prisoner realized: he had truly been imprisoned for those ten years — not by stone walls, but by his own hatred.'),
            ('"Ông ta không biết tôi tồn tại. Chỉ có tôi là tù nhân của chính mình."',
             '"He did not know I existed. Only I was my own prisoner."'),
            ('Anh bước đi, để hận thù lại, và lần đầu tiên trong mười năm — thở tự do.',
             'He walked away, leaving hatred behind, and for the first time in ten years — breathed freely.'),
        ],
        'lesson_vn': 'Bạn không thể thay đổi những gì người khác làm với bạn. Nhưng bạn có thể chọn không để nó giam cầm bạn.',
        'lesson_en': 'You cannot change what others do to you. But you can choose not to let it imprison you.',
    },
    {
        'title_vn': 'Malala Và Tiếng Súng',
        'title_en': 'Malala and the Gunshot',
        'pairs': [
            ('Năm 2012, Malala Yousafzai — 15 tuổi — bị Taliban bắn vào đầu vì dám đòi quyền giáo dục cho trẻ em gái Pakistan.',
             'In 2012, Malala Yousafzai — age 15 — was shot in the head by the Taliban for daring to demand education rights for Pakistani girls.'),
            ('Cô sống sót. Và khi tỉnh lại, câu đầu tiên cô hỏi là: "Bây giờ tôi có thể tiếp tục đi học không?"',
             'She survived. And when she woke up, the first thing she asked was: "Can I go back to school now?"'),
            ('Taliban muốn im lặng hóa một giọng nói. Thay vào đó, họ tạo ra một biểu tượng toàn cầu.',
             'The Taliban wanted to silence one voice. Instead, they created a global symbol.'),
            ('Malala nói: "Họ tưởng rằng viên đạn sẽ im lặng chúng tôi. Nhưng họ đã thất bại. Bởi vì từ sự im lặng, hàng nghìn giọng nói đã cất lên."',
             'Malala said: "They thought that the bullets would silence us. But they failed. And out of that silence came thousands of voices."'),
            ('Năm 17 tuổi, cô trở thành người trẻ nhất nhận giải Nobel Hòa bình.',
             'At 17, she became the youngest person to receive the Nobel Peace Prize.'),
            ('Kẻ thù có thể chọn cách họ đối xử với bạn. Nhưng chỉ có bạn mới chọn được người bạn trở thành sau đó.',
             'Enemies can choose how they treat you. But only you can choose who you become afterward.'),
        ],
        'lesson_vn': 'Những gì xảy ra với bạn không định nghĩa bạn. Cách bạn đáp lại mới là nơi bản sắc thực sự của bạn được tạo ra.',
        'lesson_en': 'What happens to you does not define you. How you respond is where your true identity is forged.',
    },
    {
        'title_vn': 'Triết Nhân Và Học Trò Bất Hạnh',
        'title_en': 'The Philosopher and the Unlucky Student',
        'pairs': [
            ('Một học trò đến gặp triết nhân và than vãn: "Thầy ơi, cuộc đời con thật bất hạnh. Cha mất sớm, nhà nghèo, không ai giúp đỡ."',
             'A student came to the philosopher and lamented: "Master, my life is so unfortunate. Father died young, family is poor, no one helps me."'),
            ('Triết nhân nghe xong rồi hỏi: "Con kể cho thầy nghe về những điều con đã chọn trong cuộc đời mình."',
             'The philosopher listened then asked: "Tell me about the things you have chosen in your life."'),
            ('Học trò ngạc nhiên: "Con đâu có được chọn!"',
             'The student was surprised: "I had no choices!"'),
            ('"Con chọn đến đây hôm nay không? Con chọn hỏi thầy không? Con chọn cảm thấy bất hạnh không?"',
             '"Did you choose to come here today? Did you choose to ask me? Did you choose to feel unfortunate?"'),
            ('Học trò im lặng. Lần đầu tiên anh nhận ra: anh luôn có lựa chọn — chỉ là anh không chú ý đến nó.',
             'The student fell silent. For the first time he realized: he always had choices — he just had not noticed them.'),
            ('"Cuộc đời là tổng hợp của những lựa chọn mà ta thường bỏ qua," triết nhân nói, "vì ta quá bận mơ về hoàn cảnh tốt hơn để nhìn thấy cánh cửa đang mở trước mắt."',
             '"Life is the sum of choices we usually overlook," the philosopher said, "because we are too busy dreaming of better circumstances to see the door opening before us."'),
        ],
        'lesson_vn': 'Bạn có nhiều lựa chọn hơn bạn nghĩ — nhưng chỉ khi bạn ngừng tập trung vào những gì bạn không có và bắt đầu chú ý đến những gì bạn có thể làm.',
        'lesson_en': 'You have more choices than you think — but only when you stop focusing on what you lack and start noticing what you can do.',
    },
    {
        'title_vn': 'Người Lính Bại Trận',
        'title_en': 'The Defeated Soldier',
        'pairs': [
            ('Sau thất bại thảm hại tại trận đánh Shiloh năm 1862, tướng Ulysses S. Grant được khuyên nên rút lui.',
             'After the disastrous defeat at the Battle of Shiloh in 1862, General Ulysses S. Grant was advised to retreat.'),
            ('Ông từ chối: "Tôi không thể rút lui. Tôi không bao giờ nghĩ đến thất bại."',
             'He refused: "I cannot retreat. I never think of defeat."'),
            ('Buổi tối hôm đó, tướng Sherman đến và nói: "Grant, chúng ta đã thua nặng hôm nay."',
             'That evening, General Sherman came and said: "Grant, we have had the devil\'s own day, haven\'t we?"'),
            ('Grant trả lời: "Ừ, đánh thật. Nhưng triển lại vào ngày mai." Và ông làm đúng như vậy.',
             'Grant replied: "Yes. Lick \'em tomorrow, though." And he did exactly that.'),
            ('Grant về sau trở thành tổng tư lệnh quân đội miền Bắc, dẫn đến chiến thắng trong Nội chiến, rồi trở thành tổng thống thứ 18 của nước Mỹ.',
             'Grant later became commander of the Union Army, led to victory in the Civil War, then became the 18th president of the United States.'),
            ('Không phải không thất bại — mà không để thất bại là từ cuối cùng.',
             'Not never failing — but never letting failure be the last word.'),
        ],
        'lesson_vn': 'Bạn không chọn được kết quả mọi trận chiến. Nhưng bạn chọn được liệu bạn có đứng dậy vào ngày mai không.',
        'lesson_en': 'You cannot choose the outcome of every battle. But you can choose whether you rise the next day.',
    },
    {
        'title_vn': 'Người Đàn Bà Và Chiếc Gương',
        'title_en': 'The Woman and the Mirror',
        'pairs': [
            ('Cô Amara lớn lên bị bạn bè chế giễu vì ngoại hình. Cô dành nhiều năm ghét bản thân, tránh gương soi.',
             'Amara grew up mocked by peers for her appearance. She spent years hating herself, avoiding mirrors.'),
            ('Một ngày, cô quyết định làm một thí nghiệm: mỗi buổi sáng, nhìn vào gương và nói ba điều tốt về bản thân.',
             'One day she decided to do an experiment: each morning, look in the mirror and say three good things about herself.'),
            ('Ngày đầu: không tìm được gì. Ngày thứ hai: "Tôi còn sống." Ngày thứ ba: "Tôi có đôi mắt nhìn thấy."',
             'Day one: she found nothing. Day two: "I am alive." Day three: "I have eyes that can see."'),
            ('Tháng đầu: khó. Tháng thứ ba: quen. Năm đầu: thay đổi.',
             'First month: difficult. Third month: natural. First year: transformed.'),
            ('Cô bắt đầu để ý đến người khác cũng đang tự ghét bản thân — và bắt đầu giúp đỡ họ.',
             'She began to notice others also hating themselves — and started helping them.'),
            ('Mười năm sau, cô điều hành trung tâm hỗ trợ lòng tự trọng cho phụ nữ trẻ — tất cả bắt đầu từ quyết định thay đổi cách cô nhìn chính mình.',
             'Ten years later, she ran a self-esteem support center for young women — it all started with her decision to change how she looked at herself.'),
        ],
        'lesson_vn': 'Mối quan hệ quan trọng nhất trong đời bạn là mối quan hệ với chính bạn. Chọn nhìn mình bằng ánh mắt từ bi — và mọi thứ khác sẽ thay đổi theo.',
        'lesson_en': 'The most important relationship in your life is with yourself. Choose to see yourself with compassion — and everything else will change.',
    },
    {
        'title_vn': 'Mẹ Teresa Và Sự Chọn Lựa Mỗi Ngày',
        'title_en': 'Mother Teresa and the Daily Choice',
        'pairs': [
            ('Mẹ Teresa được hỏi: "Làm sao sơ có thể chịu đựng được cảnh khổ đau như vậy mỗi ngày mà không sụp đổ?"',
             'Mother Teresa was asked: "How can you endure such suffering every day without breaking down?"'),
            ('Bà trả lời: "Tôi không chăm sóc cả thế giới. Mỗi ngày tôi chỉ chăm sóc người trước mặt tôi."',
             'She replied: "I do not care for the whole world. Each day I only care for the person in front of me."'),
            ('"Tôi không chọn làm điều vĩ đại. Tôi chọn làm những việc nhỏ với tình yêu vĩ đại."',
             '"I do not choose to do great things. I choose to do small things with great love."'),
            ('Bà sống 87 năm — không hề nghỉ phép một ngày nào từ khi bắt đầu sứ mệnh.',
             'She lived 87 years — not taking a single holiday from the day she began her mission.'),
            ('Không phải vì bà không biết mệt. Mà vì mỗi sáng bà chọn lại quyết định đó.',
             'Not because she did not know exhaustion. But because each morning she renewed that choice.'),
            ('Bản sắc không được tạo ra trong một quyết định anh hùng — nó được tạo ra trong hàng nghìn quyết định nhỏ hàng ngày.',
             'Identity is not forged in one heroic decision — it is forged in thousands of small daily decisions.'),
        ],
        'lesson_vn': 'Bạn trở thành người bạn chọn mỗi ngày — không phải trong một khoảnh khắc vĩ đại, mà trong từng lựa chọn nhỏ tưởng là vô nghĩa.',
        'lesson_en': 'You become the person you choose each day — not in one grand moment, but in each small choice that seems insignificant.',
    },
]

print("Đang tạo chương 1-4...")

make_chapter(
    'ch01-giao-dieu-tot-gap-dieu-tot', 1,
    'Gieo Điều Tốt, Gặp Điều Tốt',
    'Sow Good, Harvest Good',
    ch01_stories
)

make_chapter(
    'ch02-hanh-dong-nho-hau-qua-lon', 2,
    'Hành Động Nhỏ, Hệ Quả Lớn',
    'Small Actions, Big Consequences',
    ch02_stories
)

make_chapter(
    'ch03-thoi-quen-tao-so-phan', 3,
    'Thói Quen Tạo Nên Số Phận',
    'Habits Shape Destiny',
    ch03_stories
)

make_chapter(
    'ch04-toi-la-con-nguoi-toi-chon', 4,
    'Tôi Là Con Người Tôi Chọn',
    'I Am the Person I Choose to Be',
    ch04_stories
)

print("Hoàn tất chương 1-4!")
