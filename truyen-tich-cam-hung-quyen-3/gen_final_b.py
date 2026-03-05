# -*- coding: utf-8 -*-
import os, unicodedata

BASE = "/Users/admin/Giang-Day-html/truyen-tich-cam-hung-quyen-3/chapters"
os.makedirs(BASE, exist_ok=True)

def story(title, theme, first_letter, pairs_body, lesson_vn, lesson_en):
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
# CHƯƠNG 3: HY SINH
# ================================================================
ch3 = chapter(
    "Yêu Thương Và Hy Sinh", "Love and Sacrifice",
    "Tình yêu đích thực không đòi hỏi gì lại; nó cho đi và như vậy là đủ.",
    "True love asks nothing in return; it gives and that is enough.",
    [
    story("Cá Mẹ Bảo Vệ Trứng", "Cá Cichlid",
          "L",
          [("L oài cá cichlid mẹ ngậm chặt hàng trăm quả trứng trong miệng suốt ba tuần liền.", "The mother cichlid holds hundreds of eggs tightly in her mouth for three straight weeks."),
           ("Trong suốt thời gian đó bà không ăn gì, chỉ hít thở, chỉ canh giữ.", "Throughout that time she eats nothing, only breathes, only watches over."),
           ("Khi kẻ thù đến bà sẵn sàng nuốt xuống tạm thời để bảo vệ trứng khỏi bị săn.", "When enemies come she is ready to swallow them temporarily to protect the eggs from predators."),
           ("Sau ba tuần, tất cả trứng nở, cá con bơi lội tự do và bà lần đầu tiên được ăn.", "After three weeks all eggs hatch, the young swim free and she eats for the first time."),
           ("Không ai ép buộc bà hy sinh; đó là tình yêu thuần túy không tính toán lợi hại.", "No one forced her to sacrifice; it is pure love that does not calculate gain or loss.")],
          "Sự hi sinh của người mẹ không cần được chứng kiến hay khen thưởng; nó tự nhiên như hơi thở.",
          "A mother's sacrifice needs no witness or reward; it is as natural as breathing."),

    story("Cá Hồi Sau Đẻ Trứng", "Cá Hồi",
          "S",
          [("S au chuyến hành trình ngược dòng dài hàng trăm cây số, cá hồi đẻ trứng trong suối nguồn.", "After the upstream journey of hundreds of kilometers, salmon lay their eggs in the source stream."),
           ("Và rồi cơ thể chúng bắt đầu phân hủy, từng tế bào tan ra trong nước trong lành.", "And then their bodies begin to decompose, each cell dissolving into the clear water."),
           ("Xác cá trở thành dinh dưỡng nuôi tảo, tôm, côn trùng nước là thức ăn cho cá con sau này.", "Their bodies become nutrients feeding algae, shrimp, and water insects that will feed the young salmon."),
           ("Cả cuộc đời cá hồi chỉ hướng đến một mục đích: về nguồn, đẻ trứng, hiến thân nuôi con.", "A salmon's entire life aims at one purpose: return to the source, lay eggs, offer its body to feed the young."),
           ("Sự hy sinh hoàn toàn nhất là khi ta cho đi chính sự tồn tại của mình vì thế hệ tương lai.", "The most complete sacrifice is when we give away our very existence for the future generation.")],
          "Thế hệ hiện tại được no đủ vì thế hệ trước đã sẵn sàng tiêu tan hoàn toàn vì tình yêu.",
          "The current generation thrives because the previous one was willing to dissolve completely out of love."),

    story("Ong Thợ Chích Xong Chết", "Ong Thợ",
          "M",
          [("M ỗi con ong thợ chỉ có một cái kim chích duy nhất dính liền với nội tạng.", "Every worker bee has only one stinger permanently attached to its organs."),
           ("Khi ong chích kẻ địch xâm phạm, cái kim bị giật đứt và ong sẽ chết sau đó.", "When a bee stings an invader, the stinger is torn out and the bee dies shortly after."),
           ("Dù biết điều đó, ong vẫn không chần chừ lao vào bảo vệ tổ không một giây do dự.", "Knowing this, the bee still does not hesitate to charge in defense of the hive without a second's doubt."),
           ("Mỗi con ong chết đi đều đổi lấy sự an toàn cho hàng nghìn con ong khác còn sống.", "Each bee that dies exchanges its life for the safety of thousands of others still living."),
           ("Không có anh hùng nào cao cả hơn người biết hi sinh cả mạng sống vì điều lớn hơn bản thân.", "There is no greater hero than one who willingly sacrifices their whole life for something greater than themselves.")],
          "Sự dũng cảm hy sinh lớn nhất không đến từ kẻ không biết sợ mà từ người biết sợ nhưng vẫn tiến lên.",
          "The greatest courageous sacrifice comes not from those who know no fear but from those who know fear yet still advance."),

    story("Mẹ Voi Đỡ Con Qua Sông", "Voi",
          "K",
          [("K hi bầy voi di chuyển qua con sông lớn đang chảy mạnh do lũ về.", "When the elephant herd moves through a large river running strong from floods."),
           ("Voi mẹ đứng đối mặt dòng chảy, dùng thân mình làm bức tường ngăn dòng nước xiết.", "The mother elephant stands facing the current, using her body as a wall blocking the rushing flood."),
           ("Voi con bơi bên cạnh được che chắn hoàn toàn khỏi lực cuốn nguy hiểm.", "The calf swims beside her completely shielded from the dangerous drag."),
           ("Voi mẹ mệt lả người vì phải chống đỡ lực nước trong suốt thời gian voi con qua.", "The mother elephant is utterly exhausted from resisting the water force the whole time her calf crosses."),
           ("Tình yêu của người mẹ luôn đứng giữa sóng gió và con cái, bất kể cái giá phải trả.", "A mother's love always stands between the storm and her children, regardless of the cost.")],
          "Hãy nhớ ơn những người đã từng đứng im làm bức tường chắn gió che sóng cho ta.",
          "Remember and be grateful for those who once stood still as a wall shielding us from wind and waves."),

    story("Cây Mẹ Nhường Nhựa", "Cây Mẹ",
          "T",
          [("T rong rừng, cây mẹ lớn truyền nhựa đường mạng lưới rễ ngầm tới cây con yếu ớt.", "In the forest, a large mother tree transmits sugar through underground root networks to weak young trees."),
           ("Khi cây con thiếu ánh sáng dưới tán rừng, cây mẹ bù đắp bằng cách gửi thêm đường.", "When young trees lack light under the forest canopy, the mother tree compensates by sending extra sugar."),
           ("Các nhà khoa học đo lường và phát hiện cây mẹ giữ cho mình ít hơn mức cần thiết.", "Scientists measured and found the mother tree keeps less for herself than the minimum needed."),
           ("Khi cây mẹ bị chặt hạ, hàng chục cây con trong mạng lưới từ từ suy sụp mà chết.", "When the mother tree is felled, dozens of young trees in the network slowly weaken and die."),
           ("Tình yêu thương không chỉ là cảm xúc; nó là dòng nhựa nuôi dưỡng sự sống thực sự.", "Love is not just an emotion; it is the sap flow that actually nourishes life.")],
          "Người thầy người cha người mẹ vĩ đại luôn cho đi nhiều hơn mức họ cần để con cái mình lớn mạnh.",
          "Great teachers, fathers, and mothers always give more than they need so their children can grow strong."),

    story("Hải Cẩu Mẹ Nhịn Đói", "Hải Cẩu",
          "H",
          [("H ải cẩu mẹ sinh con trên tảng băng rồi không rời con đi săn trong nhiều ngày đầu.", "The mother seal gives birth on the ice floe then does not leave her pup to hunt for many early days."),
           ("Bà tập cho con nhận ra mùi riêng của mình để không bị thất lạc giữa hàng nghìn con.", "She trains the pup to recognize her unique scent so it is not lost among thousands."),
           ("Mỗi ngày bà mẹ gầy đi trong khi con ngày càng tròn trịa khỏe mạnh hơn.", "Each day the mother grows thinner while the pup grows rounder and healthier."),
           ("Khi hải cẩu con đủ lông dày đã sẵn sàng, bà mới ra biển tìm ăn bù lại phần đã mất.", "When the pup has thick enough fur and is ready, only then does she go to sea to eat and recover what she lost."),
           ("Bà đã hy sinh cơ thể bản thân để đổi lấy một mạng sống sung túc đầy đủ cho con.", "She sacrificed her own body to exchange it for a prosperous full life for her young.")],
          "Tình yêu không nói bằng lời mà thể hiện qua từng hy sinh âm thầm ngày qua ngày.",
          "Love is not spoken in words but shown through each silent sacrifice day after day."),

    story("Ong Chúa Và Vương Quốc", "Ong Chúa",
          "K",
          [("K hi tổ ong trở nên quá đông, ong chúa cũ thực hiện hành động phi thường: bà ra đi.", "When the hive becomes too crowded, the old queen does something extraordinary—she leaves."),
           ("Bà dẫn theo một nửa đàn tìm nơi ở mới, để lại tất cả mật và kho dự trữ cho đàn trẻ.", "She leads half the colony to find a new home, leaving all honey and reserves for the young colony."),
           ("Bà đã xây dựng tổ này từ không có gì và bây giờ bà trao nó lại cho thế hệ tiếp theo.", "She built this hive from nothing and now she hands it over to the next generation."),
           ("Hành động này đảm bảo cả hai đàn đều sống sót và phát triển mạnh mẽ hơn.", "This action ensures both colonies survive and thrive more strongly."),
           ("Người lãnh đạo vĩ đại nhất là người biết khi nào nên nhường lại vị trí để người khác phát triển.", "The greatest leader is one who knows when to step aside so others can grow.")],
          "Trao lại điều tốt nhất ta đã xây dựng cho thế hệ sau là hình thức hy sinh cao quý nhất.",
          "Passing on the best of what we built to the next generation is the noblest form of sacrifice."),

    story("Nhện Mẹ Để Con Ăn Mình", "Nhện Mẹ",
          "L",
          [("L oài nhện Stegodyphus mẹ khi sinh con xong không rời đi mà ở lại bên cạnh.", "The mother Stegodyphus spider after giving birth does not leave but stays beside the young."),
           ("Bà tự tiêu hóa các cơ quan nội tạng của mình thành thức ăn dạng lỏng cho con.", "She self-digests her own internal organs into liquid food for her young."),
           ("Con nhện con hút chất dinh dưỡng từ cơ thể mẹ cho đến khi đủ lớn để tự săn mồi.", "The young spiders draw nutrients from their mother's body until they are large enough to hunt."),
           ("Khi không còn gì để cho, bà nằm xuống nhẹ nhàng và để con hoàn thành phần còn lại.", "When there is nothing left to give, she lies down gently and lets her young complete the rest."),
           ("Tôi không biết cách diễn đạt tình yêu nào triệt để và tuyệt đối hơn thế này nữa.", "I know no way to describe a love more radical and absolute than this.")],
          "Yêu thương đích thực không có giới hạn; nó cho đến khi không còn gì để cho nữa.",
          "True love has no limits; it gives until there is nothing left to give."),

    story("Bướm Để Lại Hạt Phấn", "Bướm",
          "T",
          [("T rong lúc hút mật trên cành hoa rừng, bướm vô tình mang theo phấn hoa trên cánh mình.", "While sipping nectar on forest flowers, the butterfly unknowingly carries pollen on its wings."),
           ("Bay sang cây hoa khác bướm gieo phấn lên nhụy, kết hợp hai cây thành một sinh linh mới.", "Flying to another flower the butterfly deposits pollen on the pistil, joining two plants into a new life."),
           ("Bướm không biết mình đang làm công việc duy trì sự sống của cả khu rừng.", "The butterfly does not know it is maintaining the life of the entire forest."),
           ("Mỗi chuyến bay của nó là một món quà âm thầm trao cho thiên nhiên mà nó không hề hay biết.", "Each of its flights is a silent gift to nature that it is completely unaware of."),
           ("Đôi khi hy sinh lớn nhất không phải đau đớn mà chỉ đơn giản là chia sẻ sự có mặt của mình.", "Sometimes the greatest sacrifice is not pain but simply sharing one's presence.")],
          "Sự hiện diện của bạn, dù bạn không ý thức, có thể là món quà quý giá nhất cho cuộc sống xung quanh.",
          "Your presence, even without your awareness, may be the most precious gift to the life around you."),

    story("Gấu Mẹ Nhịn Ngủ Đông", "Gấu Mẹ",
          "T",
          [("T rong mùa đông dưới tuyết, gấu mẹ ngủ đông nhưng vẫn nuôi con sinh ra trong hang lạnh.", "In winter under snow, the mother bear hibernates yet nurses cubs born in the cold den."),
           ("Bà không ăn trong suốt sáu tháng nhưng vẫn sản xuất đủ sữa giàu chất béo nuôi con.", "She does not eat for six months yet still produces enough rich fat milk to feed her cubs."),
           ("Cơ thể bà tiêu hao chính lớp mỡ tích trữ để chuyển đổi thành sự sống cho những đứa con nhỏ.", "Her body consumes its own stored fat, converting it into life for her little ones."),
           ("Khi mùa xuân đến bà dìu từng đứa con bước ra ánh nắng đầu tiên trong đời.", "When spring comes she guides each cub out into the first sunlight of their lives."),
           ("Mỗi đứa con lành lặn bước đi trong nắng xuân là đền đáp xứng đáng cho sáu tháng hy sinh ấy.", "Each healthy cub walking in spring sunshine is worthy compensation for those six months of sacrifice.")],
          "Yêu con đích thực là chịu đựng cái lạnh và cái đói trong tối tăm để con được bước ra ánh sáng.",
          "Truly loving your child is enduring cold and hunger in darkness so the child can step into light."),
    ])

with open(os.path.join(BASE, "ch03-hy-sinh.tex"), "w", encoding="utf-8") as f:
    f.write(ch3)
print("ch03 done")

# ================================================================
# CHƯƠNG 4: DŨNG CẢM
# ================================================================
ch4 = chapter(
    "Dũng Cảm Đối Mặt Nỗi Sợ", "Courage to Face Fear",
    "Bravery is not the absence of fear—it is taking action despite the fear.",
    "Dũng cảm không phải không có sợ hãi mà là hành động dù đang sợ.",
    [
    story("Cú Điên Săn Đêm", "Cú Điên",
          "C",
          [("C ú điên bay ra khỏi cành cây an toàn vào bóng đêm không thể nhìn thấy gì.", "The great owl launches from its safe branch into the pitch-dark night seeing nothing."),
           ("Nó định vị con mồi bằng thính giác trong bóng đêm tuyệt đối không có ánh sáng.", "It locates prey by hearing alone in absolute darkness without any light."),
           ("Mỗi cú nhào xuống là đặt cược cả tính mạng vào một giọng chân chuột giữa đêm đen.", "Each dive is betting its life on a single mouse sound in the black night."),
           ("Nó không chờ đến khi trăng lên hay rạng sáng; bóng tối là địa bàn hoạt động của nó.", "It does not wait for moonrise or dawn; darkness is its operating territory."),
           ("Người dũng cảm không đợi điều kiện hoàn hảo mà hành động ngay trong bóng tối bất định.", "The courageous person does not wait for perfect conditions but acts right in the uncertain darkness.")],
          "Dũng cảm không phải là không sợ bóng tối mà là học cách lấy bóng tối làm lợi thế của mình.",
          "Courage is not fearing darkness but learning to use darkness as your advantage."),

    story("Ngựa Nhảy Rào Lửa", "Ngựa",
          "N",
          [("N gựa có bản năng bẩm sinh sợ lửa từ thời tổ tiên chạy trốn cháy rừng.", "Horses have an innate fear of fire inherited from ancestors fleeing forest fires."),
           ("Người huấn luyện phải kiên nhẫn dạy ngựa đứng gần lửa nhỏ dần dần từng tháng.", "The trainer must patiently teach the horse to stand near small fires gradually month by month."),
           ("Ngày thi đấu con ngựa đứng trước rào lửa bừng bừng, tim đập mạnh, thở hổn hển.", "On competition day the horse stands before the blazing fire barrier, heart pounding, breathing hard."),
           ("Nhưng nó tin tưởng vào người cưỡi, lấy hơi, và nhảy vọt qua rào lửa rực rỡ.", "But it trusts its rider, takes a breath, and leaps over the brilliant fire barrier."),
           ("Dũng cảm không phải không cảm thấy sợ; đó là chọn tin tưởng và tiến lên dù tim đang run.", "Courage is not the absence of feeling fear; it is choosing to trust and advance even as the heart trembles.")],
          "Hãy tìm người đáng tin cậy để cùng đối mặt nỗi sợ của bạn; chúng ta dũng cảm hơn khi không đơn độc.",
          "Find a trustworthy person to face your fears with you; we are braver when we are not alone."),

    story("Rái Cá Chống Lại Rắn", "Rái Cá",
          "M",
          [("M ột con rái cá nhỏ gặp trăn khổng lồ đang cuộn thân vào quanh bộng cây nó sống.", "A small otter found a giant python coiling around the hollow tree where it lived."),
           ("Thay vì chạy trốn bỏ nhà, nó cắn vào đuôi trăn và kéo mạnh không thả ra.", "Instead of fleeing and leaving its home, it bit the python's tail and pulled hard without releasing."),
           ("Trăn giương đầu dậy nhưng đuôi đang bị cắn làm nó mất thế cân bằng.", "The python raised its head but its pinned tail disrupted its balance."),
           ("Rái cá lợi dụng khoảnh khắc đó xoay mình kéo trăn ra khỏi bộng cây và ném xuống nước.", "The otter used that moment to spin, drag the python out of the hollow, and throw it into the water."),
           ("Kẻ yếu hơn có thể thắng kẻ mạnh hơn nếu chọn đúng điểm tấn công với đủ dũng khí.", "The weaker can beat the stronger if they choose the right attack point with sufficient courage.")],
          "Dũng cảm thông minh không phải nhắm vào chỗ kẻ địch mạnh nhất mà vào chỗ chúng dễ tổn thương.",
          "Intelligent courage does not aim at the enemy's strongest point but their most vulnerable spot."),

    story("Hổ Mẹ Chống Đàn Chó Sói", "Hổ Mẹ",
          "H",
          [("H ổ mẹ một mình đối mặt với mười hai con sói xám đang vây chặt hổ con.", "The mother tiger alone confronts twelve grey wolves tightly encircling her cub."),
           ("Bà gầm lên một tiếng khủng khiếp đủ mạnh để làm rừng vang dội chấn động.", "She lets out one terrifying roar powerful enough to make the forest echo and shake."),
           ("Hai con sói nhỏ phía sau hoảng sợ tháo chạy, phá vỡ đội hình vây đang khép kín.", "Two smaller wolves at the back fled in fear, breaking the closing encirclement formation."),
           ("Bà lao vào khoảng trống đó, cắp hổ con lên và biến vào rừng sậu trước khi đàn sói kịp phản ứng.", "She charged into that gap, grabbed her cub, and disappeared into dense forest before the wolves could react."),
           ("Không phải sức mạnh mà là ý chí sắt đá bảo vệ con đã quyết định trận đấu đó.", "Not strength but iron will to protect her young decided that battle.")],
          "Tình yêu thương có thể tạo ra dũng khí phi thường vượt quá giới hạn thể chất thông thường của ta.",
          "Love can create extraordinary courage that transcends our ordinary physical limits."),

    story("Cú Đấu Với Đại Bàng", "Cú Nhỏ",
          "M",
          [("M ột con cú nhỏ dám tấn công con đại bàng lớn gấp ba lần đang xâm phạm lãnh địa.", "A small owl dares to attack a golden eagle three times its size invading its territory."),
           ("Cú lao từ sau vào gáy đại bàng và dùng móng sắc quét liên hồi không cho đại bàng phục hồi.", "The owl dives from behind onto the eagle's neck, using sharp talons to slash repeatedly not letting the eagle recover."),
           ("Đại bàng vùng vẫy nhưng không thể tập trung bay và chiến đấu cùng một lúc.", "The eagle struggles but cannot focus on both flying and fighting simultaneously."),
           ("Cuối cùng con chim lớn hơn bỏ đi, nhường vùng trời cho kẻ dũng cảm kiên trì hơn.", "Finally the larger bird leaves, ceding the sky to the more courageous and persistent one."),
           ("Kích thước không quyết định ai giữ được lãnh thổ; sự quyết tâm bảo vệ mới quyết định.", "Size doesn't decide who keeps the territory; the determination to protect does.")],
          "Đừng đánh giá đối thủ qua kích thước; hãy xem sự quyết tâm của họ vì đó mới là thứ đáng sợ.",
          "Don't judge an opponent by size; judge their determination, for that is what's truly fearsome."),

    story("Bạch Tuộc Đổi Màu Đối Mặt", "Bạch Tuộc",
          "K",
          [("K hi cá mập tiếp cận, bạch tuộc không bơi trốn mà bất ngờ đổi màu thành màu cảnh báo.", "When a shark approaches, the octopus doesn't swim away but suddenly changes to vivid warning colors."),
           ("Nó phình to thân mình, giang tám cánh tay tạo dáng đứng to gấp đôi kích thước thật.", "It puffs itself up, spreading eight arms to create a stance twice its real size."),
           ("Màu sắc rực rỡ lạ lẫm làm cá mập không chắc chắn liệu con mồi có độc hay không.", "The vivid unusual colors make the shark uncertain whether this prey is poisonous."),
           ("Sau vài giây do dự, cá mập đổi hướng bơi đi tìm con mồi an toàn hơn.", "After a few seconds of hesitation, the shark changes direction to find safer prey."),
           ("Đôi khi dũng cảm không phải chiến đấu mà là biết cách khiến kẻ địch không dám bắt đầu.", "Sometimes courage is not fighting but knowing how to make the enemy afraid to start.")],
          "Vẻ ngoài tự tin đôi khi là vũ khí mạnh hơn cả sức mạnh thật sự; hãy đứng thẳng trước mọi thử thách.",
          "Confident appearance is sometimes a stronger weapon than real strength; stand tall before every challenge."),

    story("Chó Sói Tách Bầy Chiến Đấu", "Chó Sói",
          "M",
          [("M ột con sói già bị đẩy ra khỏi bầy vì xung đột với con sói đực trẻ mạnh hơn.", "An old wolf was driven from the pack due to conflict with a stronger younger male."),
           ("Một mình trong tuyết lạnh, không bầy đàn, không ai bảo vệ, nó vẫn đứng vững.", "Alone in the cold snow, no pack, no protection, it still stood firm."),
           ("Nó học cách săn thỏ nhỏ và chim rừng, chuyển đổi chiến thuật hoàn toàn để sống sót.", "It learned to hunt small rabbits and forest birds, completely shifting tactics to survive."),
           ("Khi năm sau bầy gặp nguy hiểm, con sói già quay lại chiến đấu cho bầy cũ không tính toán.", "When the following year the pack faced danger, the old wolf returned to fight for its former pack without calculation."),
           ("Dũng cảm không phải chiến đấu khi mạnh; đó là chiến đấu cả khi bị từ bỏ cô đơn.", "Courage is not fighting when strong; it is fighting even when abandoned and alone.")],
          "Kẻ thật sự dũng cảm không phải người chưa bao giờ bị đánh ngã mà là người đứng dậy mỗi lần.",
          "The truly courageous person is not one who was never knocked down but one who stands up each time."),

    story("Kiến Đỏ Xây Lại Tổ Sau Lụt", "Kiến Đỏ",
          "S",
          [("S au trận lũ quét, toàn bộ tổ kiến đỏ bị cuốn sạch không còn gì sót lại.", "After a flash flood, the entire red ant mound was swept away with nothing remaining."),
           ("Đàn kiến không có một ngày đau buồn; chúng bắt đầu lại ngay sáng hôm sau.", "The ant colony did not take one day to grieve; they started over the very next morning."),
           ("Từng hạt đất nhỏ được khiêng về, từng hành lang được đào lại từ đầu.", "Each small grain of earth was carried back, each corridor re-dug from scratch."),
           ("Trong bảy ngày tổ mới hình thành, không hoàn hảo nhưng đủ an toàn cho cả đàn.", "In seven days a new mound formed, not perfect but safe enough for the whole colony."),
           ("Dũng cảm không chỉ là đối mặt nguy hiểm mà còn là dũng khí bắt đầu lại sau thất bại.", "Courage is not only facing danger but also the courage to start over after disaster.")],
          "Thảm họa không phải dấu chấm hết; đó chỉ là dấu phẩy trong câu chuyện của những người không bỏ cuộc.",
          "Disaster is not the end; it is only a comma in the story of those who do not give up."),

    story("Gấu Bắc Cực Bơi Xuyên Băng", "Gấu Bắc Cực",
          "G",
          [("G ấu bắc cực phải bơi hàng chục cây số trong nước biển đóng băng lạnh âm độ để tìm mồi.", "Polar bears must swim dozens of kilometers in sub-zero freezing seawater to find food."),
           ("Nhiều con bơi đến kiệt sức, lên được một tảng băng trôi, nằm lại nghỉ rồi tiếp tục.", "Many swim to exhaustion, climb onto a drifting ice floe, rest, then continue on."),
           ("Không có đảm bảo phía trước có gì, nhưng chúng vẫn bơi vì bản năng sống sót thôi thúc.", "There is no guarantee of what lies ahead, but they swim because the survival instinct drives them."),
           ("Con gấu dừng bơi ở giữa biển thì chết đuối; con người dừng lại giữa thử thách cũng chìm.", "A bear that stops swimming mid-ocean drowns; a person who stops mid-challenge also sinks."),
           ("Thứ duy nhất giữ ta nổi là tiếp tục đạp chân tiếp tục cử động tiếp tục tiến lên.", "The only thing keeping us afloat is continuing to kick, continuing to move, continuing to advance.")],
          "Cuộc sống dũng cảm không đòi hỏi ta không bao giờ kiệt sức; nó chỉ đòi ta nghỉ rồi tiếp tục.",
          "A courageous life does not require that we never tire; it only requires that we rest and then continue."),

    story("Cáo Thoát Bẫy Thợ Săn", "Cáo",
          "M",
          [("M ột con cáo bị kẹt chân vào bẫy thép sáng sớm trong rừng lạnh giá.", "A fox caught its leg in a steel trap in the cold early forest morning."),
           ("Nó la thét đau đớn trong một lúc rồi dừng lại, quan sát bẫy một cách bình tĩnh.", "It cried out in pain for a while then stopped, observing the trap calmly."),
           ("Bằng răng sắc nó cắn đứt dây gân chân mình để giải thoát trước khi thợ săn đến.", "With sharp teeth it bit through its own leg tendon to free itself before the hunter arrived."),
           ("Nó chạy đi với ba chân, đau đớn, nhưng tự do, không chờ ai giải cứu mình.", "It ran on three legs, in pain, but free, not waiting for anyone to rescue it."),
           ("Khi không thể thoát khỏi hoàn cảnh theo cách cũ, đôi khi dũng cảm nhất là quyết định đau đớn nhất.", "When unable to escape circumstances the old way, sometimes the most courageous act is the most painful decision.")],
          "Dũng cảm thật sự đôi khi là sẵn sàng cắt bỏ điều đang giam cầm ta dù đó là điều ta yêu thích.",
          "True courage is sometimes being willing to cut away what imprisons us even if it is something we love."),
    ])

with open(os.path.join(BASE, "ch04-dung-cam.tex"), "w", encoding="utf-8") as f:
    f.write(ch4)
print("ch04 done")
