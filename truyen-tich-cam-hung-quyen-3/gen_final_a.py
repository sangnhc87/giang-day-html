# -*- coding: utf-8 -*-
import os, unicodedata

BASE = "/Users/admin/Giang-Day-html/truyen-tich-cam-hung-quyen-3/chapters"
os.makedirs(BASE, exist_ok=True)

def story(title, theme, first_letter, pairs_body, lesson_vn, lesson_en):
    """Build a \begin{truyen}...\end{truyen} + \begin{baihoc}...\end{baihoc} block."""
    rest = first_letter
    lines = []
    lines.append(f"\\section{{{title}}}")
    lines.append(f"\\begin{{truyen}}{{{title}}}{{{theme}}}")
    first_vn, first_en = pairs_body[0]
    lines.append(f"\\chuhoa{{{first_letter[0]}}}{{{first_letter[1:]}}}{first_vn}\\\\")
    lines.append(f"\\textit{{({first_en})}}")
    lines.append("")
    for vn, en in pairs_body[1:]:
        lines.append(f"{vn}\\\\")
        lines.append(f"\\textit{{({en})}}")
        lines.append("")
    lines.append("\\end{truyen}")
    lines.append("\\begin{baihoc}")
    lines.append(f"  {lesson_vn}\\\\")
    lines.append(f"  \\textit{{({lesson_en})}}")
    lines.append("\\end{baihoc}")
    lines.append("")
    return "\n".join(lines)

def chapter(chap_vn, chap_en, quote_vn, quote_en, stories):
    lines = [
        f"%============================================================",
        f"\\chapter{{Bài Học: {chap_vn} ({chap_en})}}",
        "\\begin{center}",
        f"  \\textit{{\\color{{truyenblue}}{quote_en}}}\\\\",
        f"  \\textit{{({quote_vn})}}\\\\[4pt]",
        "  \\small\\color{truyengold}--- Thiên nhiên dạy ta ---",
        "\\end{center}",
        "\\ngancach",
        "",
    ]
    for s in stories:
        lines.append(s)
    return unicodedata.normalize("NFC", "\n".join(lines))

# ================================================================
# CHƯƠNG 1: ĐOÀN KẾT
# ================================================================
ch1 = chapter(
    "Đoàn Kết Tạo Nên Sức Mạnh", "Unity Creates Strength",
    "Muôn sợi chỉ đơn mỏng manh, xoắn thành dây thừng thì bất khả xâm phạm.",
    "A single thread is fragile; twisted together they become unbreakable rope.",
    [
    story("Kiến Khiêng Hạt Gạo", "Kiến",
          "M",
          [("M ột con kiến tìm thấy hạt gạo lớn gấp chục lần thân nó.", "A small ant found a grain of rice ten times its own size."),
           ("Nó kéo một mình mãi mà không nhúc nhích được.", "It pulled alone for a long time but could not move it."),
           ("Thay vì bỏ cuộc, nó chạy về gọi thêm hai mươi bạn.", "Instead of giving up, it ran back to call twenty more friends."),
           ("Cùng nhau, chúng khiêng hạt gạo nặng về tổ dễ dàng.", "Together, they easily carried the heavy grain back to the nest."),
           ("Nhìn lại, nếu đi một mình, cả đàn đã bỏ lỡ bữa ăn no đủ hôm đó.", "Looking back, if it had gone alone, the whole colony would have missed a full meal that day.")],
          "Một cá nhân có thể bất lực trước khó khăn lớn, nhưng tập thể đoàn kết có thể làm nên điều kỳ diệu.",
          "An individual may be powerless before great challenges, but a united team can achieve miracles."),

    story("Đàn Ngựa Vằn Xếp Vòng", "Ngựa Vằn",
          "K",
          [("K hi bầy sư tử đói khát vây kín, đàn ngựa vằn không tán loạn bỏ chạy.", "When a hungry pride of lions encircled them, the zebra herd did not scatter and flee."),
           ("Chúng lập tức xếp thành vòng tròn, đầu hướng vào trong, đuôi hướng ra ngoài.", "They immediately formed a circle, heads inward, hind legs kicking outward."),
           ("Những cú đạp hậu cực mạnh quất vào mũi sư tử khiến chúng phải lùi.", "Powerful back kicks struck the lions' noses, forcing them to retreat."),
           ("Cả đàn không để mất một con nào dù đối mặt kẻ thù hung dữ nguy hiểm hơn.", "The whole herd did not lose a single member despite facing fiercer and more dangerous enemies."),
           ("Nhưng khi một con tách ra khỏi đàn vì kiêu ngạo, nó đã bị cô lập và trở thành bữa tối.", "But when one strayed from the herd out of arrogance, it was isolated and became dinner.")],
          "Kẻ thù luôn nhắm vào con mồi đơn độc; hãy ở cạnh những người cùng chí hướng để bảo vệ nhau.",
          "Enemies always target the lone prey; stay beside like-minded people to protect each other."),

    story("Bè Cá Mòi", "Cá Mòi",
          "H",
          [("H àng triệu con cá mòi nhỏ bé bơi thành một khối cầu khổng lồ trên biển.", "Millions of small sardines swim as one giant ball in the ocean."),
           ("Từ xa trông giống như một sinh vật biển khổng lồ đáng sợ.", "From afar it looks like one terrifying giant sea creature."),
           ("Cá ngừ, cá mập tiếp cận rồi hoảng sợ bơi đi vì không xác định được con mồi thật.", "Tunas and sharks approached then swam away frightened, unable to identify the real prey."),
           ("Mỗi con cá mòi một mình chỉ bằng ngón tay út, nhưng cả đàn trở thành thực thể vô địch.", "Each sardine alone is the size of a little finger, but together the school becomes an invincible entity."),
           ("Sức mạnh không đến từ kích thước mà đến từ sự gắn kết không rời.", "Strength does not come from size but from inseparable cohesion.")],
          "Dù nhỏ bé, khi đoàn kết, ta trở thành sức mạnh mà kẻ thù không dám xem thường.",
          "Though small, when united, we become a force that enemies dare not underestimate."),

    story("Rừng Tre Chống Bão", "Rừng Tre",
          "M",
          [("M ột thân tre đứng lẻ loi bẻ gãy rất dễ trong cơn gió cuồng phong dữ dội.", "A single lone bamboo stalk breaks very easily in a fierce windstorm."),
           ("Nhưng rừng tre hàng nghìn cây đan xen rễ nhau thì khác hẳn.", "But a bamboo forest of thousands with interlocking roots is entirely different."),
           ("Gió thổi đến làm cả rừng cúi rạp, nhưng không cây nào bật gốc đứt lìa.", "The wind comes bending the whole forest low, but not one stalk is uprooted."),
           ("Rễ chằng chịt dưới đất truyền tải và phân chia lực bão cho toàn bộ.", "The tangled roots underground transmit and distribute the storm's force across the whole."),
           ("Trận bão đi qua, cả rừng tre vươn thẳng trở lại xanh tươi mạnh mẽ hơn bao giờ.", "When the storm passes, the whole forest springs back greener and stronger than ever.")],
          "Chia sẻ gánh nặng trong cộng đồng sẽ giúp mọi người vượt qua những trận bão lớn nhất của cuộc đời.",
          "Sharing burdens within a community helps everyone survive the greatest life storms."),

    story("Ong Bảo Vệ Tổ", "Loài Ong",
          "K",
          [("K hi con gấu mò đến cậy phá tổ ong để lấy mật, cả đàn ong xuất kích đồng loạt.", "When a bear came to pry open the hive for honey, the entire colony launched out together."),
           ("Hàng nghìn con ong thợ bao vây con gấu khổng lồ gấp nghìn lần thân chúng.", "Thousands of worker bees surrounded the giant bear a thousand times their size."),
           ("Mỗi con ong chỉ có một nhát chích duy nhất trong đời, nhưng chúng không tiếc.", "Each bee has only one sting in its lifetime, but they did not hesitate."),
           ("Đau đớn tột cùng buộc con gấu phải bỏ chạy tháo lui bảo toàn tính mạng.", "Extreme pain forced the bear to flee and retreat to save its life."),
           ("Cả đàn hy sinh để bảo vệ mái nhà chung và thế hệ ong con trong tổ.", "The whole colony sacrificed to protect their shared home and the young bee generation inside.")],
          "Đoàn kết không chỉ là cùng nhau hưởng lợi mà còn là cùng nhau chịu khổ bảo vệ cộng đồng.",
          "Unity is not only enjoying benefits together but also enduring hardships together to protect the community."),

    story("Cây Rừng Nguyên Sinh", "Cây Rừng",
          "T",
          [("T rong rừng nguyên sinh, các cây không hề cạnh tranh ánh sáng theo kiểu hủy diệt nhau.", "In old-growth forests, trees do not compete for sunlight in a way that destroys each other."),
           ("Cây cao tạo tán che mát cho cây non bên dưới khỏi nắng thiêu gắt.", "Tall trees create canopies to shade young trees below from scorching sun."),
           ("Rễ cây chia sẻ nước và khoáng chất qua mạng lưới nấm ngầm nối liền với nhau.", "Tree roots share water and minerals through an underground fungal network connecting them."),
           ("Khi một cây bị sâu bệnh tấn công, nó phát tín hiệu hóa học để cả rừng đề phòng.", "When one tree is attacked by pests, it sends chemical signals to alert the whole forest."),
           ("Rừng không phải tập hợp cây đơn lẻ mà là một siêu sinh thể biết yêu thương.", "A forest is not a collection of individual trees but a super-organism that knows how to love.")],
          "Hãy học rừng cây: trao đi thay vì cạnh tranh, cả cộng đồng sẽ cùng nhau xanh tươi bền vững.",
          "Learn from the forest: give instead of competing, and the whole community will thrive sustainably together."),

    story("Bầy Ngỗng Trời Di Cư", "Ngỗng Trời",
          "Đ",
          [("Đ àn ngỗng trời bay hình chữ V khi di cư vượt ngàn dặm qua mùa đông.", "Flocks of wild geese fly in V-formation when migrating thousands of miles through winter."),
           ("Con đầu đàn đối mặt sức cản gió lớn nhất, tạo luồng khí nâng đỡ cho các con sau.", "The lead goose faces the greatest wind resistance, creating updrafts to lift those behind."),
           ("Khi con đầu mệt, nó lùi về sau và ngay lập tức một con khác lên thay thế vị trí.", "When the lead goose tires, it drops back and another immediately takes its place."),
           ("Những con phía sau kêu lên cỗ vũ con đầu đàn để chúng giữ được tốc độ cao.", "Those behind honk encouragingly to help the lead goose maintain high speed."),
           ("Nhờ hình chữ V đoàn kết, cả đàn bay được xa hơn 70% so với từng con bay đơn độc.", "Thanks to the united V-shape, the whole flock flies 70% farther than each flying alone.")],
          "Luân phiên gánh vác và cổ vũ nhau là bí quyết để đi thật xa trong cuộc hành trình chung.",
          "Taking turns carrying the load and cheering each other on is the secret to going very far together."),

    story("Đàn Sói Săn Mồi", "Đàn Sói",
          "M",
          [("M ột con sói đơn độc rất khó hạ được con nai lớn hơn nó rất nhiều.", "A lone wolf finds it very difficult to take down a deer much larger than itself."),
           ("Nhưng một bầy sói đã tiến hóa chiến thuật săn mồi tập thể vô cùng tinh vi.", "But a wolf pack has evolved extremely sophisticated collective hunting tactics."),
           ("Vài con xua đuổi con mồi, vài con mai phục sẵn ở hai bên sườn đón đầu.", "Some chase the prey, while others ambush on both flanks to cut it off."),
           ("Con nai dù chạy thật nhanh cũng không thể thoát khỏi vòng vây chiến thuật của cả bầy.", "No matter how fast the deer runs, it cannot escape the tactical encirclement of the whole pack."),
           ("Sau khi săn được, cả bầy chia đều phần ăn theo thứ bậc, không con nào bị bỏ đói.", "After a successful hunt, the pack shares the meal by rank, leaving no one hungry.")],
          "Chiến lược tập thể phân công rõ ràng luôn hiệu quả hơn sức mạnh cá nhân đơn độc.",
          "Clear collective strategy is always more effective than individual strength alone."),

    story("Dế Mèn Và Đàn Kiến", "Dế Và Kiến",
          "M",
          [("M ột buổi sáng mùa đông lạnh giá, dế mèn đơn độc gõ cửa tổ kiến xin thức ăn.", "On a cold winter morning, a lonely cricket knocked on the ant colony's door begging for food."),
           ("Dế đã hát nhảy suốt mùa hè trong khi kiến làm việc gom góp lương thực.", "The cricket had sung and danced all summer while ants worked hard storing food."),
           ("Kiến chúa nhìn dế tội nghiệp và quyết định không đóng cửa từ chối.", "The queen ant looked at the pitiful cricket and decided not to close the door in refusal."),
           ("Bà bảo: Chúng ta chia sẻ một ít, nhưng mùa xuân tới, dế phải cùng làm việc với đàn.", "She said: We share a little, but when spring comes, the cricket must work together with the colony."),
           ("Dế hiểu ra bài học và mùa sau trở thành thành viên chăm chỉ nhất của cả đàn kiến.", "The cricket learned the lesson and the next season became the hardest working member of the ant colony.")],
          "Giúp đỡ người khác không phải yếu đuối; đó là cách xây dựng cộng đồng gắn bó bền vững lâu dài.",
          "Helping others is not weakness; it is the way to build a lasting and cohesive community."),

    story("Rùa Biển Cùng Bơi Về Bờ", "Rùa Biển",
          "H",
          [("H àng trăm con rùa biển con mới nở phải vượt bãi cát dài về phía sóng biển.", "Hundreds of newly hatched sea turtles must cross a long beach to reach the waves."),
           ("Chim hải âu, cua đỏ rình rập săn bắt chúng xung quanh tứ phía.", "Seagulls and red crabs lurk to hunt them from all four directions."),
           ("Rùa con chạy thành từng nhóm nhỏ đông như vũ bão, khiến kẻ thù bối rối không kịp phản ứng.", "The baby turtles ran in large stormy groups, leaving enemies confused and unable to react in time."),
           ("Con nằm bên cạnh con, con này ngã thì con kia dùng thân mình che chắn, đỡ dậy.", "One beside another, if one fell the next used its body to shield and help it up."),
           ("Tỷ lệ sống sót của nhóm cao gấp nhiều lần so với những con rùa lạc lõng đi một mình.", "The survival rate of the group was many times higher than that of lone stray turtles going alone.")],
          "Trong những hành trình nguy hiểm nhất của cuộc đời, hãy tìm kiếm người đồng hành cùng chí hướng.",
          "In life's most dangerous journeys, seek out companions who share your direction."),
    ])

with open(os.path.join(BASE, "ch01-doan-ket.tex"), "w", encoding="utf-8") as f:
    f.write(ch1)
print("ch01 done")

# ================================================================
# CHƯƠNG 2: KIÊN TRÌ
# ================================================================
ch2 = chapter(
    "Kiên Trì Vượt Qua Thử Thách", "Perseverance Overcomes All",
    "A river cuts through rock not because of its power, but because of its persistence.",
    "Dòng sông khoét thủng đá không phải vì sức mạnh mà vì sự kiên trì.",
    [
    story("Cá Hồi Ngược Dòng", "Cá Hồi",
          "H",
          [("H àng trăm con cá hồi đối mặt với dòng thác trắng xóa hung hãn ngàn lực xô đẩy.", "Hundreds of salmon face raging white waterfalls with a thousand forces pushing back."),
           ("Chúng lao thân ngược nước, bị đẩy ngã xuống, rồi lại leo lên từ đầu.", "They thrust upstream, get pushed back down, then climb up again from the start."),
           ("Mỗi lần vượt được một thác, cơ thể chúng thêm mạnh mẽ hơn, màu đỏ rực sáng hơn.", "Each time they pass a waterfall, their bodies grow stronger, their color glowing redder."),
           ("Không có con cá hồi nào về được nguồn mà không vượt qua ít nhất chục thác dữ.", "No salmon ever returns to its source without crossing at least a dozen fierce waterfalls."),
           ("Kết thúc hành trình, chúng đẻ trứng rồi chết, nhưng để lại thế hệ kế tiếp dũng mãnh.", "The journey ends: they spawn then die, but leave behind a courageous next generation.")],
          "Mục tiêu đích thực đáng giá phải luôn đặt ở phía đầu nguồn của dòng chảy khắc nghiệt.",
          "A truly worthy goal must always be placed at the headwaters of the fiercest current."),

    story("Sâu Phá Kén", "Loài Bướm",
          "M",
          [("M ột con sâu cuốn mình vào cái kén hẹp hòi tối tăm chật chội không còn chỗ cựa quậy.", "A caterpillar wraps itself into a narrow, dark, cramped cocoon with no room to move."),
           ("Nó vật lộn từng phút từng giờ để chui ra qua cái khe hở bé như đầu kim.", "It struggles minute by minute, hour by hour to squeeze out through a tiny needle-eye gap."),
           ("Ai đó nhân từ cắt rộng khe hở giúp nó, nhưng nó trượt ra với đôi cánh nhăn nhúm lả tả.", "Someone kindly widened the gap to help, but it slipped out with crumpled, limp wings."),
           ("Chính sự vật lộn bơm máu lên cánh mới tạo ra đôi cánh đủ cứng để bay lượn.", "The very struggle pumps blood into the wings, creating wings strong enough to fly."),
           ("Không có kén chật, không có bướm đẹp; không có vật lộn, không có đôi cánh thật sự.", "No tight cocoon, no beautiful butterfly; no struggle, no real wings.")],
          "Những khó khăn trong cuộc đời không phải để giết chết ta; chúng ở đó để cường hóa ta.",
          "Difficulties in life are not there to kill us; they are there to strengthen us."),

    story("Nhện Giă Tơ Bruce", "Nhện",
          "V",
          [("V ua Robert Bruce thất trận bảy lần liên tiếp và trốn trong hang động tuyệt vọng.", "King Robert Bruce lost seven consecutive battles and hid in a cave in despair."),
           ("Ông nhìn thấy một con nhện cố gắng giăng tơ từ vách này sang vách kia.", "He watched a spider trying to spin its web from one wall to the other."),
           ("Sáu lần sợi tơ đứt rụng, sáu lần nhện nhẫn nại ném lại từ đầu không nản lòng.", "Six times the thread broke and fell, six times the spider patiently tried again without discouragement."),
           ("Lần thứ bảy sợi tơ móc vào đúng điểm, cả tấm lưới được dệt hoàn chỉnh.", "The seventh time the thread hooked at exactly the right point and the whole web was woven complete."),
           ("Vua đứng dậy, tập hợp quân đội và lần thứ tám giành lại giang sơn Scotland.", "The king stood up, assembled his army, and on the eighth attempt reclaimed Scotland.")],
          "Nếu con nhện biết thử lần thứ bảy thì con người cũng có thể đứng dậy thêm một lần nữa.",
          "If the spider knows to try a seventh time, then a person can also stand up one more time."),

    story("Rùa Và Thỏ", "Rùa Và Thỏ",
          "C",
          [("C on rùa chậm chạp thách thức con thỏ nhanh nhẹn trong một cuộc đua dài.", "The slow turtle challenged the fast rabbit in a long race."),
           ("Thỏ bứt tốc bỏ xa ngay từ đầu, rồi ngủ nghỉ giữa đường vì quá tự tin.", "The rabbit sped far ahead at the start, then napped midway out of overconfidence."),
           ("Rùa bước từng bước đều đặn, không nghỉ, không ngoảnh đầu nhìn lại.", "The turtle walked each step steadily, never stopping, never turning to look back."),
           ("Khi thỏ tỉnh dậy chạy tốc lực đến đích thì rùa đã về trước từ lâu rồi.", "When the rabbit woke up and sprinted to the finish, the turtle had already been there long before."),
           ("Bài học không phải rùa nhanh hơn thỏ mà là sự kiên trì bền bỉ đánh bại tài năng thiếu nỗ lực.", "The lesson is not that turtles are faster than rabbits, but that steady persistence defeats ungrown talent.")],
          "Tốc độ tức thời không bằng sự đều đặn kiên định; người đi chậm mà chắc luôn về đích.",
          "Instant speed is no match for steady consistency; those who move slowly but surely always reach the goal."),

    story("Kiến Leo Núi", "Kiến",
          "M",
          [("M ột con kiến nhỏ bé cứ leo lên phiến đá rồi lăn xuống, leo lên rồi lăn xuống.", "A tiny ant kept climbing up the rock slab, then rolling down, up then down again."),
           ("Người quan sát đếm được con kiến đó ngã xuống và leo lại đúng năm mươi bảy lần.", "An observer counted that ant falling down and climbing back up exactly fifty-seven times."),
           ("Không một lần con kiến bỏ đi tìm đường khác hay từ chối tiếp tục cố gắng.", "Not once did the ant leave to find another route or refuse to keep trying."),
           ("Đến lần thứ năm mươi tám, nó cuối cùng ôm miếng mồi vượt qua đỉnh phiến đá.", "On the fifty-eighth try, it finally hugged its food and crossed over the top of the slab."),
           ("Quan sát con kiến, vị tu sĩ hiểu ra rằng không có gì thất bại trừ khi ta tự bỏ cuộc.", "Watching the ant, the monk understood that nothing fails except when we ourselves give up.")],
          "Số lần ngã không quyết định thất bại; chỉ có quyết định KHÔNG ĐỨNG DẬY nữa mới là thất bại thật sự.",
          "The number of falls does not decide failure; only the decision to NEVER GET UP AGAIN is true failure."),

    story("Cây Tre Bốn Năm Im Lặng", "Cây Tre",
          "B",
          [("B ốn năm liên tiếp nông dân tưới nước, bón phân cho hạt tre đã gieo mà không thấy gì.", "Four consecutive years a farmer watered and fertilized the planted bamboo seed seeing nothing."),
           ("Hàng xóm cười chế giễu rằng đất đó chết, hạt giống đó thối không mọc được.", "Neighbors laughed and mocked that the soil was dead, the seed rotten and unable to grow."),
           ("Người nông dân vẫn kiên trì mỗi sáng ra tưới, tin tưởng vào sự sống tiềm ẩn bên dưới.", "The farmer still patiently watered every morning, trusting in the hidden life beneath."),
           ("Năm thứ năm, một mầm nhỏ chọc thủng mặt đất và trong sáu tuần mọc cao ba mươi mét.", "In the fifth year, a small shoot pierced through the ground and in six weeks grew thirty meters tall."),
           ("Bốn năm đó không phải vô ích; rễ tre đã ngầm tỏa rộng mười mét đề phòng bão tố.", "Those four years were not wasted; bamboo roots had spread silently ten meters to guard against storms.")],
          "Khi công sức của bạn chưa hiển thị, đừng đổ lỗi cho mảnh đất; hãy tin rằng rễ đang lớn mạnh trong bóng tối.",
          "When your efforts are not yet visible, do not blame the soil; trust that the roots are growing mightily in darkness."),

    story("Nhím Leo Núi Everest", "Nhím",
          "H",
          [("H ai con nhím được mang đến chân núi và thả ra, ai leo được cao hơn sẽ thắng.", "Two hedgehogs were brought to the mountain base and released; whoever climbed higher would win."),
           ("Con thứ nhất bước vài bước, bị gai đá cào chảy máu chân và ngồi xuống khóc.", "The first one took a few steps, got its paws cut on sharp rocks and sat down crying."),
           ("Con thứ hai cũng bị cào, cũng đau, nhưng cứ tiếp tục bước từng bước nhỏ lên cao.", "The second was also cut, also in pain, but kept taking each small step upward."),
           ("Cả đám đông vây quanh cổ vũ con thứ nhất, không ai nhìn con thứ hai đơn độc leo lên.", "The whole crowd surrounded cheering on the first one; no one watched the second quietly climbing."),
           ("Ba giờ sau, con nhím thứ hai đứng trên đỉnh, trong khi con thứ nhất vẫn còn ở dưới chân núi.", "Three hours later, the second hedgehog stood at the summit while the first was still at the base.")],
          "Đau đớn là không thể tránh khỏi, nhưng để nỗi đau hủy hoại bước tiếp theo mới chính là thất bại.",
          "Pain is unavoidable, but letting pain destroy the next step is the real failure."),

    story("Cáo Leo Vào Vườn Nho", "Con Cáo",
          "C",
          [("C on cáo đói bụng nhìn thấy chùm nho chín mọng đỏ lẻ trên cao khó với tới được.", "The hungry fox saw ripe red grape clusters hanging high and hard to reach."),
           ("Nó nhảy lên, thiếu nửa mét, ngã xuống, nhảy lại, lại ngã, liên tục nhiều lần.", "It jumped up, missing by half a meter, fell down, jumped again, fell again, repeatedly many times."),
           ("Lần thứ mười lăm nó cuối cùng vươn tới nhánh thấp nhất và kéo xuống được.", "On the fifteenth try it finally reached the lowest branch and pulled it down."),
           ("Nếu dừng lại ở lần thứ mười bốn và tự nhủ rằng nho chắc chua thì nó đã mãi không biết vị ngọt.", "Had it stopped at the fourteenth try telling itself the grapes were surely sour, it would have never known the sweet taste."),
           ("Bài học: Đừng hợp lý hóa sự từ bỏ; hãy cố thêm một lần nữa trước khi quyết định.", "Lesson: Do not rationalize giving up; try one more time before deciding.")],
          "Nho chỉ thật sự chua khi con cáo đã cố hết sức mà thật sự không thể với tới.",
          "The grapes are truly sour only when the fox has truly tried its hardest and genuinely cannot reach them."),

    story("Ngựa Hoang Luyện Thuần", "Ngựa Hoang",
          "N",
          [("N gựa hoang rừng bị bắt lần đầu sợ hãi điên cuồng đạp phá cả đêm đến kiệt sức.", "The wild horse caught for the first time fought madly all night kicking until exhausted."),
           ("Người nài ngựa không đánh roi, không trói chặt, chỉ giữ cương kiên nhẫn thì thôi.", "The trainer did not whip or tie tight, only held the reins patiently nothing more."),
           ("Mỗi ngày ngựa chống cự ít hơn, bắt đầu chú ý lắng nghe tín hiệu tay cương.", "Each day the horse resisted less, beginning to notice and listen to the rein hand signals."),
           ("Sau sáu tháng kiên trì, con ngựa hoang trở thành người bạn đồng hành tin cậy trên đường dài.", "After six months of patience, the wild horse became a trustworthy companion on long journeys."),
           ("Điều không thể chinh phục bằng vũ lực trong một ngày có thể được chinh phục bằng sự kiên nhẫn trong sáu tháng.", "What cannot be conquered by force in one day can be conquered by patience in six months.")],
          "Sự kiên nhẫn là loại sức mạnh tinh tế nhất mà coercive force thô bạo không bao giờ có thể thay thế được.",
          "Patience is the most refined form of strength that brute coercive force can never replace."),

    story("Hoa Xương Rồng Sa Mạc", "Hoa Xương Rồng",
          "G",
          [("G iữa sa mạc khô cằn nắng gắt không một giọt mưa trong suốt chín tháng liền.", "In the middle of a scorching arid desert without a drop of rain for nine straight months."),
           ("Cây xương rồng gai nhọn đứng im toả rễ sâu xuống bắt từng hạt ẩm còn sót lại.", "The thorny cactus stands still spreading deep roots to catch every remaining moisture particle."),
           ("Nó tích nước trong thân dày, không phung phí một vi lượng nào không cần thiết.", "It stores water in its thick trunk, not wasting a single unnecessary microgram."),
           ("Sau cơn mưa đầu mùa hiếm hoi, cây ngay lập tức bung hàng trăm bông hoa đỏ rực rỡ ánh sáng.", "After the rare first rain of the season, the plant immediately bursts into hundreds of brilliantly bright red flowers."),
           ("Vẻ đẹp rực rỡ đó không đến từ may mắn mà từ chín tháng nhẫn nhịn giữ gìn tích lũy im lặng.", "That brilliant beauty comes not from luck but from nine months of patient silent accumulation.")],
          "Vẻ đẹp vĩ đại nhất luôn nở rộ sau thời gian dài nhất của sự chờ đợi và chuẩn bị trong im lặng.",
          "The greatest beauty always blooms after the longest period of silent waiting and preparation."),
    ])

with open(os.path.join(BASE, "ch02-kien-tri.tex"), "w", encoding="utf-8") as f:
    f.write(ch2)
print("ch02 done")
