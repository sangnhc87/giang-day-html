#!/usr/bin/env python3
# gen_q9_b.py -- Quyển IX chương 5-8
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


ch05 = [
    {
        'title_vn': 'Không Được Chọn Là Chuyện Rất Bình Thường',
        'title_en': 'Not Being Chosen Is Very Normal',
        'pairs': [
            ('Nhiều người trẻ sốc mạnh trong lần đầu bị từ chối xin việc, xin học bổng, hay xin một cơ hội tốt.',
             'Many young people are deeply shocked the first time they are rejected for a job, a scholarship, or a good chance.'),
            ('Họ tưởng mình làm chưa đủ. Đôi khi đúng. Nhưng cũng nhiều khi chỉ là hôm đó người ta chọn người khác hợp hơn.',
             'They think they did not do enough. Sometimes that is true. But often someone else simply fit better that day.'),
            ('Không được chọn đau vì nó chạm vào cái tôi.',
             'Not being chosen hurts because it touches the ego.'),
            ('Nhưng nếu học được cách chịu đựng nó, em sẽ bớt gãy hơn rất nhiều trong đời.',
             'But if you learn how to bear it, life will break you much less.'),
        ],
        'lesson_vn': 'Bị từ chối không nói hết giá trị của em. Nó chỉ nói rằng cơ hội đó không thuộc về em vào lúc đó.',
        'lesson_en': 'Rejection does not tell the whole truth about your worth. It only says that this chance was not yours at that time.',
    },
    {
        'title_vn': 'Bị Chê Không Luôn Là Bị Xúc Phạm',
        'title_en': 'Criticism Is Not Always an Insult',
        'pairs': [
            ('Đi học lâu làm nhiều người quen với việc lỗi sai vẫn được nương.',
             'Long years in school make many people used to having mistakes softened.'),
            ('Ra đời rồi, lời góp ý có thể ngắn, thẳng, và khó nghe hơn.',
             'In adult life, feedback can be shorter, sharper, and harder to hear.'),
            ('Nếu cái tôi quá lớn, em sẽ thấy mọi lời chê đều là đòn đánh vào mình.',
             'If the ego is too large, every criticism feels like a personal attack.'),
            ('Nhưng bớt tự ái một chút, em sẽ thấy nhiều lời khó nghe chính là thứ giúp mình lớn lên nhanh nhất.',
             'But if you become a little less defensive, you will see that many hard comments are what help you grow fastest.'),
        ],
        'lesson_vn': 'Không phải lời chê nào cũng đúng. Nhưng người trưởng thành biết lọc phần có ích thay vì chỉ nổi nóng.',
        'lesson_en': 'Not every criticism is correct. But a mature person knows how to keep the useful part instead of only getting angry.',
    },
    {
        'title_vn': 'Bị Thay Thế Là Một Bài Học Tỉnh Người',
        'title_en': 'Being Replaced Is a Waking Lesson',
        'pairs': [
            ('Có người trẻ tưởng chỉ cần mình từng làm tốt là vị trí sẽ luôn là của mình.',
             'Some young people think that if they once did well, the position will always remain theirs.'),
            ('Nhưng đời thay người rất nhanh khi em ngừng học, ngừng giữ chất lượng, hay ngừng tiến lên.',
             'But life replaces people quickly when they stop learning, stop keeping quality, or stop moving forward.'),
            ('Bị thay thế nghe đau, nhưng nó nhắc em rằng không có chỗ đứng nào nên được ngủ quên trên đó.',
             'Being replaced sounds painful, but it reminds you that no position should become a sleeping place.'),
            ('Ai cũng có thể bị thay. Câu hỏi là em học gì trước sự thật đó.',
             'Anyone can be replaced. The question is what you learn from that fact.'),
        ],
        'lesson_vn': 'Đừng sống như thể vị trí hôm nay là vĩnh viễn. Giữ mình sắc là cách duy nhất để không bị cũ quá nhanh.',
        'lesson_en': 'Do not live as if today’s place is permanent. Staying sharp is the only way not to become outdated too fast.',
    },
    {
        'title_vn': 'Có Những Cánh Cửa Đóng Vì Em Chưa Đủ, Không Phải Vì Em Hỏng',
        'title_en': 'Some Doors Close Because You Are Not Ready Yet',
        'pairs': [
            ('Một người trẻ bị từ chối vài lần rất dễ đi đến kết luận rằng mình không có tương lai.',
             'A young person rejected several times can easily conclude that they have no future.'),
            ('Đó là kết luận quá lớn từ dữ liệu còn quá ít.',
             'That is too large a conclusion from too little data.'),
            ('Nhiều cánh cửa đóng không phải để sỉ nhục em. Nó chỉ phản ánh khoảng cách giữa em hiện tại và tiêu chuẩn của cơ hội đó.',
             'Many closed doors are not meant to humiliate you. They only reflect the gap between your current self and that opportunity’s standard.'),
            ('Thấy đúng khoảng cách thì còn học được. Chỉ thấy mình hỏng thì thường chỉ muốn bỏ.',
             'If you see the gap clearly, you can still learn. If you see only yourself as broken, you will usually just want to quit.'),
        ],
        'lesson_vn': 'Đừng biến “chưa đủ” thành “không xứng”. Hai câu đó khác nhau rất xa.',
        'lesson_en': 'Do not turn “not ready yet” into “not worthy.” Those are very different sentences.',
    },
    {
        'title_vn': 'Không Ai Nhớ Mãi Một Lần Em Trượt',
        'title_en': 'No One Remembers Your Failure Forever',
        'pairs': [
            ('Người trẻ thường nghĩ lần thất bại của mình sẽ bám theo rất lâu trong mắt người khác.',
             'Young people often think their failure will stay in other people’s eyes for a very long time.'),
            ('Sự thật là ai cũng bận với cuộc đời của họ hơn em tưởng.',
             'The truth is that most people are more busy with their own lives than you imagine.'),
            ('Điều bám lâu nhất không phải ký ức của người khác. Nó là cách em tự kể lại chuyện đó với chính mình.',
             'What lasts longest is not other people’s memory. It is the story you keep telling yourself.'),
            ('Nếu em không biến một cú trượt thành danh tính, nó sẽ sớm chỉ còn là một sự kiện.',
             'If you do not turn one failure into an identity, it soon becomes only an event.'),
        ],
        'lesson_vn': 'Sau khi ngã, việc khó nhất không phải chịu mắt người đời. Nhiều khi là ngừng tự đóng đinh mình vào cú ngã đó.',
        'lesson_en': 'After a fall, the hardest task is often not facing the world. It is stopping yourself from nailing your whole identity to that fall.',
    },
]

ch06 = [
    {
        'title_vn': 'Sống Xa Nhà Là Một Cú Lớn Lên Rất Thật',
        'title_en': 'Living Away from Home Is a Very Real Shock of Growth',
        'pairs': [
            ('Khi còn ở nhà, nhiều việc nhỏ được ai đó âm thầm gánh hộ em.',
             'When you live at home, many small burdens are quietly carried for you.'),
            ('Ra ở riêng rồi, em mới thấy bữa ăn, tiền điện, ga gối, bệnh vặt, và cả sự im lặng cũng đều có trọng lượng.',
             'Once you live alone, meals, utility bills, laundry, small illness, and even silence all gain weight.'),
            ('Sống xa nhà không chỉ là đổi địa chỉ. Nó là đổi vai trò.',
             'Living away from home is not only changing address. It is changing roles.'),
            ('Từ người được chăm, em dần thành người tự chăm mình.',
             'From being cared for, you slowly become the one who cares for yourself.'),
        ],
        'lesson_vn': 'Xa nhà làm người ta mệt hơn, nhưng cũng thật hơn. Nó ép em chạm vào phần đời sống mà trước đó em chỉ đi qua.',
        'lesson_en': 'Living away from home is harder, but also more real. It forces you to touch parts of life you once only passed by.',
    },
    {
        'title_vn': 'Bệnh Một Mình Mới Hiểu Nhớ Nhà Là Gì',
        'title_en': 'You Understand Homesickness When You Get Sick Alone',
        'pairs': [
            ('Có những ngày em sốt, nằm trong phòng trọ, và không có ai hỏi đã ăn chưa.',
             'There are days when you have a fever in a rented room and no one asks whether you have eaten.'),
            ('Lúc đó nỗi nhớ nhà không còn là cảm xúc mơ hồ. Nó thành một cảm giác rất cụ thể trong cổ họng.',
             'Then homesickness is no longer vague. It becomes something very physical in your throat.'),
            ('Người trẻ hay nghĩ mình mạnh cho đến khi phải tự lo lúc cơ thể yếu nhất.',
             'Young people often think they are strong until they must care for themselves at their weakest.'),
            ('Những ngày như vậy dạy em giá trị của gia đình theo cách không cuốn sách nào dạy hết được.',
             'Days like that teach the value of family in a way no book can fully teach.'),
        ],
        'lesson_vn': 'Sống xa nhà khiến em hiểu tình thương không phải điều hiển nhiên. Nó là một thứ rất cụ thể khi em thiếu nó.',
        'lesson_en': 'Living away from home teaches that care is not abstract. You feel exactly what it is when you do not have it.',
    },
    {
        'title_vn': 'Thành Phố Không Ác, Nhưng Không Rảnh Dịu Dàng Với Em',
        'title_en': 'The City Is Not Cruel, But It Is Not Gentle for Free',
        'pairs': [
            ('Thành phố lớn không ghét em. Nó chỉ rất bận.',
             'A big city does not hate you. It is simply very busy.'),
            ('Nếu em chậm, thiếu tỉnh, hay thiếu tiền, thành phố sẽ cho em thấy giá của những điều đó rất nhanh.',
             'If you are slow, careless, or short of money, the city shows the price of those things very quickly.'),
            ('Điều đó làm nhiều người trẻ tưởng mình bị cuộc đời nhắm vào.',
             'That makes many young people feel personally attacked by life.'),
            ('Thực ra không phải. Đô thị chỉ vận hành nhanh và lạnh hơn làng quê hay mái nhà cũ của em.',
             'In truth, no. Urban life simply moves faster and colder than your old home.'),
        ],
        'lesson_vn': 'Muốn sống được ở thành phố, người trẻ cần tỉnh táo, tự lập, và biết giữ nhịp. Sự ngây thơ ở đây rất đắt.',
        'lesson_en': 'To live well in the city, young people need alertness, self-reliance, and rhythm. Naivety becomes expensive there.',
    },
    {
        'title_vn': 'Một Căn Phòng Nhỏ Cũng Có Thể Dạy Em Rất Nhiều',
        'title_en': 'A Small Room Can Teach You a Lot',
        'pairs': [
            ('Nhiều người trẻ bắt đầu đời sống trưởng thành trong một căn phòng rất nhỏ.',
             'Many young adults begin adult life in a very small room.'),
            ('Nhỏ nhưng trong đó có đủ bài học: cách giữ sạch, cách tiết kiệm, cách sống gọn, và cách chịu một mình.',
             'It is small, but it holds many lessons: how to keep things clean, save money, live simply, and endure solitude.'),
            ('Không gian chật đôi khi lại ép con người học những điều rất căn bản.',
             'A tight space can force a person to learn very basic truths.'),
            ('Có những người sau này có nhà rộng hơn, nhưng trưởng thành nhất lại bắt đầu từ căn phòng bé nhất.',
             'Some later live in bigger homes, yet their real growth began in the smallest room.'),
        ],
        'lesson_vn': 'Đừng khinh giai đoạn sống chật. Nhiều nền nếp tốt của người lớn bắt đầu từ những điều rất chật nhưng rất thật.',
        'lesson_en': 'Do not despise the cramped phase of life. Many strong adult habits begin in conditions that are small but very real.',
    },
    {
        'title_vn': 'Gọi Về Nhà Không Phải Là Yếu',
        'title_en': 'Calling Home Is Not Weakness',
        'pairs': [
            ('Có người trẻ sống xa nhà và cố tỏ ra cứng đến mức ngay cả khi mệt cũng không muốn gọi về.',
             'Some young people live far from home and act so tough that they refuse to call even when exhausted.'),
            ('Họ sợ mình sẽ yếu đi nếu thừa nhận rằng mình nhớ nhà hoặc cần một lời hỏi han.',
             'They fear becoming weak if they admit that they miss home or need a kind voice.'),
            ('Nhưng trưởng thành không có nghĩa là cắt hết nhu cầu được yêu thương.',
             'But growing up does not mean cutting away the need to be loved.'),
            ('Biết tự lập và vẫn giữ được sợi dây với gia đình là một kiểu trưởng thành lành mạnh hơn nhiều.',
             'Being self-reliant while still keeping a bond with family is a far healthier form of adulthood.'),
        ],
        'lesson_vn': 'Tự lập không đồng nghĩa với cô lập. Người mạnh không phải người không cần ai, mà là người biết cần ai cho đúng.',
        'lesson_en': 'Self-reliance is not self-isolation. A strong person is not one who needs no one, but one who knows whom to lean on wisely.',
    },
]

ch07 = [
    {
        'title_vn': 'Ra Đời Rồi, Bạn Bè Không Còn Đi Cùng Một Tốc Độ',
        'title_en': 'After School, Friends No Longer Move at the Same Speed',
        'pairs': [
            ('Khi còn đi học, lịch sống của mọi người khá giống nhau.',
             'When people are in school, their schedules are still fairly similar.'),
            ('Ra đời rồi, có người đi làm sớm, có người học tiếp, có người lấy chồng lấy vợ, có người còn đang loay hoay.',
             'After that, some start work early, some continue studying, some get married, and some are still searching.'),
            ('Bạn bè vì thế không còn đi cùng một nhịp như trước.',
             'So friends no longer move in the same rhythm as before.'),
            ('Nếu không hiểu điều đó, người trẻ rất dễ buồn vì nghĩ rằng tình bạn đang chết đi.',
             'If you do not understand this, it is easy to think friendship is dying.'),
        ],
        'lesson_vn': 'Nhiều tình bạn không hỏng. Nó chỉ đổi nhịp. Người trưởng thành phải học chấp nhận nhịp khác nhau mà vẫn giữ lòng tử tế.',
        'lesson_en': 'Many friendships are not broken. They only change pace. Adults must learn to accept different rhythms while keeping kindness.',
    },
    {
        'title_vn': 'Có Người Chỉ Hợp Đi Cùng Em Một Đoạn',
        'title_en': 'Some People Fit Only One Part of the Road',
        'pairs': [
            ('Có những người rất hợp với em ở tuổi mười bảy nhưng không còn hợp ở tuổi hai mươi ba.',
             'Some people fit you well at seventeen but no longer fit at twenty-three.'),
            ('Điều đó không nhất thiết ai phản bội ai.',
             'That does not always mean betrayal.'),
            ('Con người đổi giá trị, đổi môi trường, đổi nhịp sống, nên tình bạn cũng đổi theo.',
             'People change values, environments, and pace, so friendship changes too.'),
            ('Cố giữ một mối quan hệ chỉ vì quá khứ đẹp đôi khi làm hiện tại mệt thêm.',
             'Trying to keep a relationship only because the past was beautiful can make the present heavier.'),
        ],
        'lesson_vn': 'Không phải ai từng thân cũng phải ở lại mãi. Có người đến để đi cùng em một quãng, vậy là đủ.',
        'lesson_en': 'Not everyone who was once close must stay forever. Some people come to walk with you for one part, and that is enough.',
    },
    {
        'title_vn': 'Thành Công Của Bạn Có Thể Làm Em Chạnh Lòng',
        'title_en': 'A Friend’s Success May Sting You',
        'pairs': [
            ('Ra đời rồi, chênh lệch giữa bạn bè hiện ra rất nhanh.',
             'After school, the gap between friends can appear very quickly.'),
            ('Người này có việc tốt, người kia thất nghiệp. Người này mua xe, người kia còn nợ trọ.',
             'One person gets a good job, another is unemployed. One buys a motorbike, another still owes rent.'),
            ('Chạnh lòng trước thành công của bạn là rất người.',
             'Feeling a sting before a friend’s success is very human.'),
            ('Điều quan trọng là đừng để cơn chạnh lòng đó làm em ghét điều tốt của người khác.',
             'What matters is not letting that sting turn into hatred for someone else’s good fortune.'),
        ],
        'lesson_vn': 'So sánh là điều khó tránh. Nhưng nếu giữ được lòng sạch trước thành công của bạn, em sẽ đỡ cay độc và đỡ khổ hơn.',
        'lesson_en': 'Comparison is hard to avoid. But if you keep your heart clean before a friend’s success, you will become less bitter and less miserable.',
    },
    {
        'title_vn': 'Tin Nhắn Thưa Dần Không Luôn Là Hết Thân',
        'title_en': 'Fewer Messages Do Not Always Mean Less Love',
        'pairs': [
            ('Lớn lên rồi, có những người thương nhau thật nhưng nói chuyện ít đi.',
             'As people grow older, some truly care for each other yet speak less often.'),
            ('Không phải vì họ hết quý nhau. Mà vì đời sống bắt đầu đầy trách nhiệm khác.',
             'It is not always because they care less. It is because life fills with other responsibilities.'),
            ('Người trẻ nếu quá bám vào tần suất liên lạc sẽ dễ hiểu lầm nhiều mối quan hệ tốt.',
             'If young people cling too much to message frequency, they may misread many good relationships.'),
            ('Có những tình bạn trưởng thành hơn khi nó bớt ồn mà vẫn còn thật.',
             'Some friendships become more mature when they grow less noisy but remain true.'),
        ],
        'lesson_vn': 'Tình bạn lớn lên không phải lúc nào cũng ồn ào. Có khi nó chỉ trở nên lặng hơn nhưng chắc hơn.',
        'lesson_en': 'Friendship does not always grow louder as it matures. Sometimes it grows quieter but stronger.',
    },
    {
        'title_vn': 'Cũng Có Lúc Phải Chia Tay Một Tình Bạn',
        'title_en': 'Sometimes You Must End a Friendship',
        'pairs': [
            ('Có những người bạn chỉ hợp khi cả hai còn vô tư.',
             'Some friendships work only while both people remain carefree.'),
            ('Khi đời bắt đầu khó hơn, những lệch giá trị, lệch cách sống, và lệch đạo đức hiện ra rõ hơn.',
             'When life becomes harder, differences in values, lifestyle, and ethics become clearer.'),
            ('Không phải mối quan hệ nào cũng cần cứu bằng mọi giá.',
             'Not every relationship should be saved at all costs.'),
            ('Có những cuộc chia tay tử tế giúp cả hai bớt làm hỏng nhau hơn.',
             'Some decent endings keep both people from damaging each other further.'),
        ],
        'lesson_vn': 'Người trưởng thành phải biết có những tình bạn nên được buông xuống đàng hoàng, không phải kéo lê mãi trong khó chịu.',
        'lesson_en': 'A mature person must know that some friendships should be laid down with dignity, not dragged on in resentment.',
    },
]

ch08 = [
    {
        'title_vn': 'Yêu Không Tự Động Cứu Được Ai',
        'title_en': 'Love Does Not Automatically Save Anyone',
        'pairs': [
            ('Nhiều người trẻ bước vào tình yêu với ảo tưởng rằng chỉ cần thương đủ thì mọi vết thương của nhau sẽ lành.',
             'Many young people enter love with the illusion that deep love alone can heal each other’s wounds.'),
            ('Nhưng tình yêu không thay thế được trị liệu, kỷ luật, hay trách nhiệm cá nhân.',
             'But love cannot replace therapy, discipline, or personal responsibility.'),
            ('Thương một người đang vỡ là chuyện đẹp. Nghĩ rằng mình có thể cứu họ chỉ bằng thương là chuyện nguy hiểm.',
             'Loving someone who is broken can be beautiful. Thinking you can save them with love alone is dangerous.'),
            ('Không ai nên bắt tình yêu làm công việc mà chính bản thân họ không chịu làm.',
             'No one should ask love to do work they themselves refuse to do.'),
        ],
        'lesson_vn': 'Tình yêu có thể nâng đỡ, nhưng không thể làm thay việc trưởng thành của một con người.',
        'lesson_en': 'Love can support someone, but it cannot do the work of growing up for them.',
    },
    {
        'title_vn': 'Ngọt Không Đồng Nghĩa Bền',
        'title_en': 'Sweet Does Not Mean Stable',
        'pairs': [
            ('Có những mối quan hệ rất ngọt ở đầu: nhắn tin nhiều, hứa nhiều, nhớ nhiều, dính nhiều.',
             'Some relationships are very sweet at the start: many messages, many promises, much longing, much closeness.'),
            ('Nhưng độ ngọt đầu kỳ không nói hết được sức bền lâu dài.',
             'But early sweetness says little about long-term stability.'),
            ('Một mối quan hệ bền cần nhiều thứ ít lãng mạn hơn: trách nhiệm, đúng giờ, giữ lời, cách xử lý mâu thuẫn.',
             'A stable relationship needs things less romantic: responsibility, punctuality, keeping promises, and handling conflict well.'),
            ('Người trẻ hay yêu bằng cảm giác rồi khổ vì quên nhìn cấu trúc của mối quan hệ.',
             'Young people often love through feeling and suffer because they forget to examine the structure of the relationship.'),
        ],
        'lesson_vn': 'Đừng chỉ nhìn người ta làm em rung động thế nào. Hãy nhìn họ sống có đáng tin không.',
        'lesson_en': 'Do not only watch how someone makes you feel. Watch whether that person lives in a trustworthy way.',
    },
    {
        'title_vn': 'Yêu Không Giữ Được Người Không Muốn Ở Lại',
        'title_en': 'Love Cannot Keep Someone Who Does Not Want to Stay',
        'pairs': [
            ('Một trong những bài học đau nhất của tuổi trẻ là biết rằng mình rất thương vẫn có thể không giữ được một người.',
             'One of youth’s most painful lessons is learning that deep love may still fail to keep someone.'),
            ('Nhiều người cố cứu một mối quan hệ đã chết bằng nỗ lực một phía.',
             'Many people try to save a dead relationship through one-sided effort.'),
            ('Nhưng tình yêu thật không thể được giữ bằng van xin mãi mãi.',
             'Real love cannot be preserved forever by begging.'),
            ('Có lúc buông một người không phải vì hết thương, mà vì ở lại chỉ làm cả hai hỏng thêm.',
             'Sometimes letting go is not a sign of less love, but a sign that staying would damage both people further.'),
        ],
        'lesson_vn': 'Tuổi trẻ cần học rằng yêu không đồng nghĩa sở hữu. Không phải ai mình thương cũng sẽ ở lại.',
        'lesson_en': 'Youth must learn that love is not ownership. Not everyone we love will stay.',
    },
    {
        'title_vn': 'Tình Yêu Và Sĩ Diện',
        'title_en': 'Love and Pride',
        'pairs': [
            ('Có những cuộc cãi nhau kéo dài không phải vì vấn đề quá lớn, mà vì hai cái tôi đều không chịu lùi.',
             'Some arguments last not because the issue is huge, but because two egos refuse to step back.'),
            ('Người trẻ nhiều khi thương nhau thật nhưng vẫn phá nhau vì sĩ diện.',
             'Young people may truly love each other and still destroy the relationship through pride.'),
            ('Xin lỗi đúng lúc, nói thật đúng lúc, và chịu nghe đúng lúc là những kỹ năng ít lãng mạn nhưng rất cứu mối quan hệ.',
             'Apologizing in time, speaking honestly in time, and listening in time are not romantic skills, but they save relationships.'),
            ('Nhiều tình yêu không chết vì hết cảm xúc. Nó chết vì cái tôi lớn hơn tình nghĩa.',
             'Many relationships do not die from lack of feeling. They die because the ego grows larger than the bond.'),
        ],
        'lesson_vn': 'Yêu ai đó lâu dài đòi hỏi bớt thắng thua. Lúc nào cũng muốn thắng thì thường sẽ mất.',
        'lesson_en': 'To love someone for a long time, you must care less about winning. Those who always need to win often end up losing.',
    },
    {
        'title_vn': 'Một Mối Tình Tốt Không Làm Em Mất Mình',
        'title_en': 'A Good Relationship Does Not Erase You',
        'pairs': [
            ('Có người yêu xong bỏ hết bạn bè, thói quen tốt, mục tiêu riêng, và cuộc sống của chính mình.',
             'Some people enter love and then abandon friends, good habits, personal goals, and their own lives.'),
            ('Họ tưởng đó là hết lòng.',
             'They think that means wholehearted love.'),
            ('Nhưng một mối quan hệ lành không nuốt mất bản thân của em.',
             'But a healthy relationship does not swallow your identity.'),
            ('Yêu đúng là khi em vẫn là mình, chỉ là rộng hơn, chín hơn, và tử tế hơn khi có người bên cạnh.',
             'Loving well means still being yourself, only wider, more mature, and kinder with someone beside you.'),
        ],
        'lesson_vn': 'Đừng gọi việc đánh mất mình là yêu sâu. Một tình yêu tốt phải giữ được cả tình cảm lẫn nhân cách.',
        'lesson_en': 'Do not call losing yourself deep love. A good relationship should preserve both feeling and character.',
    },
]

print("Đang tạo chương 5-8...")
make_chapter('ch05-bi-tu-choi-bi-thay-the', 'Bị Từ Chối, Bị Chê, Bị Thay Thế', 'Rejected, Criticized, Replaced', ch05)
make_chapter('ch06-song-xa-nha', 'Lên Thành Phố, Sống Xa Nhà, Tự Lo Mọi Thứ', 'Moving Away and Taking Care of Everything', ch06)
make_chapter('ch07-ban-be-ra-re', 'Bạn Bè Ra Rẽ, Đường Ai Nấy Đi', 'Friends Drift, Each Person Has a Road', ch07)
make_chapter('ch08-tinh-yeu-tuoi-tre', 'Tình Yêu Tuổi Trẻ Và Những Ảo Tưởng Ngọt', 'Young Love and Its Sweet Illusions', ch08)
print("Hoàn tất chương 5-8!")
