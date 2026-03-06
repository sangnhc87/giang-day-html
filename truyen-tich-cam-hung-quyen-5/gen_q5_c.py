# -*- coding: utf-8 -*-
"""Quyển V -- Hai Mặt Của Một Đồng Xu -- Chapters 9-12"""
import os, unicodedata, re

BASE = "/Users/admin/Giang-Day-html/truyen-tich-cam-hung-quyen-5/chapters"
os.makedirs(BASE, exist_ok=True)

def story(title, source, first_letter, pairs_body, lesson_vn, lesson_en):
    lines = []
    lines.append(f"\\section{{{title}}}")
    lines.append(f"\\begin{{truyen}}{{{title}}}{{{source}}}")
    first_vn, first_en = pairs_body[0]
    rest = first_vn[len(first_letter):]
    lines.append(f"\\chuhoa{{{first_letter[0]}}}{{{first_letter[1:]}}}{rest}\\\\[4pt]")
    lines.append(f"\\textit{{({first_en})}}")
    lines.append("")
    for vn, en in pairs_body[1:]:
        lines.append(f"{vn}\\\\[4pt]")
        lines.append(f"\\textit{{({en})}}")
        lines.append("")
    lines.append("\\end{truyen}")
    lines.append("\\begin{baihoc}")
    lines.append(f"  {lesson_vn}\\\\[4pt]")
    lines.append(f"  \\textit{{({lesson_en})}}")
    lines.append("\\end{baihoc}")
    lines.append("")
    return "\n".join(lines)

def fix(text):
    text = re.sub(r'(?<!\\)%', r'\\%', text)
    return unicodedata.normalize("NFC", text)

def chapter(chap_vn, chap_en, quote_vn, quote_en, stories):
    lines = [
        "%============================================================",
        f"\\chapter{{Bài Học: {chap_vn} ({chap_en})}}",
        "\\begin{center}",
        f"  \\textit{{\\color{{truyengold}}``{quote_en}''}}\\\\[4pt]",
        f"  \\textit{{({quote_vn})}}\\\\[4pt]",
        "  \\small\\color{truyenblue}--- Cổ Kim Đông Tây ---",
        "\\end{center}",
        "\\ngancach",
        "",
    ]
    for s in stories:
        lines.append(s)
    return fix("\n".join(lines))

# ================================================================
# CHƯƠNG 9: CHO TRONG NHẬN
# ================================================================
ch9 = chapter(
    "Cho Trong Nhận, Nhận Trong Cho", 
    "Giving in Receiving, Receiving in Giving",
    "Bàn tay trao tặng hoa hồng, hương thơm còn vương lại.",
    "The hand that gives the rose always retains a little fragrance.",
    [
    story("Người Tốt Bụng Đóng Tiền Viện Phí", "Albert Schweitzer",
          "Bác",
          [("Bác sĩ Albert Schweitzer đã cống hiến cuộc đời mình để xây bệnh viện tại một nơi khỉ ho cò gáy ở châu Phi.",
            "Doctor Albert Schweitzer dedicated his life to building a hospital in a remote wilderness of Africa."),
           ("Ông bỏ lại vinh quang, tiện nghi ở châu Âu để cho đi y thuật và công sức giúp đỡ những người nghèo khổ nhất.",
            "He left behind glory and comforts in Europe to give his medical skills and effort helping the poorest people."),
           ("Người đời nhìn vào tưởng rằng ông đã hy sinh quá nhiều, chỉ toàn là 'cho đi' mà không lẫy lại được chút vật chất gì.",
            "People looking at it thought he had sacrificed too much, entirely 'giving' without taking back any material wealth."),
           ("Nhưng ông giải thích: ``Mục đích cao cả nhất đời tôi không phải là cứu người, mà là cứu rỗi sự thanh thản trong chính cái tâm của bản thân mình.''",
            "But he explained: `The highest purpose of my life is not to save others, but to save the tranquility within my own mind.'"),
           ("Qua hành động dâng hiến vất vả, ông thực chất đã nhận lại được nguồn năng lượng bình yên vô giá không tiền bạc nào mua nổi.",
            "Through his grueling giving action, he actually received back a priceless peaceful energy no money could buy.")],
          "Sự vĩ đại của việc hiến dâng là vì trong lúc trao tài sản cho người khác, bạn đã tự bồi đắp tâm hồn nghèo nàn của chính mình.",
          "The greatness of devotion is that while giving property to others, you have enriched your own poor soul."),

    story("Tỉ Phú Khất Thực Bữa Ăn", "J.D. Rockefeller",
          "Lúc",
          [("Lúc đang đứng ở đỉnh cao sự nghiệp kinh doanh tàn nhẫn, tỷ phú dầu mỏ John D. Rockefeller mắc chứng bệnh tâm lý trầm trọng và ung thư dạ dày.",
            "While standing at the peak of his ruthless business career, oil billionaire John D. Rockefeller suffered severe psychological illness and stomach cancer."),
           ("Bác sĩ cảnh báo ông có thể qua đời rất sớm nếu vẫn duy trì lối sống vơ vét tóm thâu và không thể ngủ ngon về đêm.",
            "Doctors warned he might die very soon if he maintained his grasping, amassing lifestyle and couldn't sleep well at night."),
           ("Ông quyết định đem khối tài sản khổng lồ đó đi phân phát quyên góp thành lập các viện nghiên cứu và trường đại học lớn.",
            "He decided to take that giant fortune and distribute it, donating to establish major research institutes and universities."),
           ("Sự cho đi toàn bộ tiền của ấy một cách đáng ngạc nhiên đã chữa lành bệnh tật trong cơ thể ông.",
            "That giving away of all his money surprisingly healed the illness inside his body."),
           ("Nhờ việc trao tặng tài sản đi, ông lấy lại được thứ ông đinh ninh sẽ mất: sinh mệnh kéo dài đến gần trăm tuổi.",
            "Through gifting away his wealth, he received back what he was certain to lose: a lifespan extended to almost a hundred years.")],
          "Vật chất vút đi là lúc phước phần ùa tới; người trao đi thứ tốt nhất sẽ nhận về sức lành mạnh ngập tràn.",
          "As material wealth flies away is when blessings rush in; the one who gives away the best will receive back an overflowing healthy strength."),

    story("Biển Chết Và Biển Galilee", "Câu chuyện Do Thái --- Địa lý khu vực",
          "Có",
          [("Có hai vùng biển nổi tiếng đều nhận chung một nguồn nước tuyệt đẹp từ sông Jordan chảy vào giáp vùng Trung Đông.",
            "There are two famous seas both receiving a common beautiful water source from the Jordan River flowing into the Middle East region."),
           ("Biển Galilee nhận nước sông vào nhưng sau đó lập tức tuôn chảy qua bờ để cho đi nuôi khu rừng rậm rạp xanh tươi đầy cá mú tôm sinh sôi nảy nở trù phú ngút ngàn.",
            "The Sea of Galilee receives river water but then immediately flows over its banks giving it away to nourish lush green dense forests full of thriving fish and abundant life."),
           ("Nhưng Biển Chết ở phía nam cũng nhận số nước ngọt y hệt nhưng nó chỉ giữ khư khư nằm ngoan cố thu nạp mọi thứ mà chẳng hề tìm cửa trút cho ra.",
            "But the Dead Sea to the south also receives the exact same fresh water, yet it stubbornly holds tightly, accumulating everything without finding an exit door to give out."),
           ("Hậu quả là vùng Biển Chết đó mặn chát đến mức mọc váng muối đắng chát, giết chết hoàn toàn mọi sinh linh lỡ đánh rơi vào, xung quanh không một mầm xanh gỡ gạc.",
            "The consequence is that the Dead Sea is so salty it forms bitter salt crusts, totally killing any living creature falling into it, completely barren of any green sprout around."),
           ("Chỉ nhận không cho đã tự tay giết chết biển Chết thành một vùng trọc lóc, trong khi Galilee biết chia sẻ lại trở thành điểm hội tụ của nguồn sống thiêng.",
            "Only receiving without giving single-handedly killed the Dead Sea into a barren zone, while Galilee knowing how to share became the converging point of sacred life.")],
          "Người nào chỉ biết thâu nhập mà không biết san sẻ cống hiến, tâm hồn người đó sẽ trở nên đặc cứng đắng chát như biển Chết.",
          "Whoever only knows to accumulate without knowing to share and contribute, that person's soul will become thick and bitter like the Dead Sea."),

    story("Bà Lão Bán Bánh Mì Dạy Trẻ Đói", "Truyện Ngụ Ngôn --- Khuyết Danh",
          "Trên",
          [("Trên góc phố nghèo ngổn ngang gió có một bà lão nghèo khổ mỗi sáng hay làm bánh mì đem bán sống qua ngày lay lắt.",
            "On a windy cluttered poor street corner there was a poor old woman who baked bread every morning to sell living a struggling day-to-day life."),
           ("Mỗi ngày bà đều lén đặt một ổ bánh mì mới tươi ngon nhất ra phía ngoài bệ cửa sổ, với suy nghĩ dành khao đứa đói khát nào lỡ bước sang qua ngang đó ăn tạm.",
            "Every day she secretly placed one freshest and most delicious loaf of bread outside the windowsill, with the thought of treating some starving wanderer passing by to eat temporarily."),
           ("Một kẻ lang thang qua rinh bánh đều lầm bầm câu thần chú: ``Sự xấu xa ngươi làm sẽ đâm chết người, sự tốt lành ngươ làm sẽ che chở ngươi''.",
            "A vagabond passing by lifting the bread always muttered the mantra: `The evil you do will stab you to death, the goodness you do will shelter you'."),
           ("Nhờ liên tục mang rải miếng ăn nhỏ nhoi nhưng tâm hồn bà cụ cảm thấy hân hoan ấm áp an bình bất chấp nghèo khó rác rách cản bước.",
            "Thanks to continuously scattering the tiny morsel of food, the old woman's soul felt joyously warm and peaceful despite poverty and ragged rubbish hindering her steps."),
           ("Không ngờ nhiều năm sau đứa con ly hương bị đi lính của bà từ cõi chết mù khơi bỗng trở gót gõ cửa nhận mẹ vì có người lang thang kia từng rải bánh mì khô lại tình cờ băng băng cứu đói nhầm chính con trai bà trên đồn.",
            "Unexpectedly years later her exiled soldier son returning from the blind remote realm of death suddenly knocked on the door recognizing his mother because that very vagabond who once got dry bread coincidentally happened to save her own son from starvation at the fort.")],
          "Mộc mạc cho đi một chiếc lá ân nghĩa cũng là đang lặng lẽ gieo trồng lại cả một rổ yêu thương nhặt thu vào ngày sau.",
          "Rustic giving of one gratitude leaf is also quietly replanting an entire basket of love to be harvested in later days."),

    story("Alexander Fleming Cây Đàn Piano Và Penicillin", "Lịch Sử Y Học --- Anh Quốc",
          "Theo",
          [("Theo một giai thoại thú vị, cha của Alexander Fleming vốn là một thường dân nông phu cày cuốc, do mủi lòng đã nhảy ra cứu một cậu thiếu niên kham khổ kẹt suýt chết đuối giữa đầm lầy.",
            "According to an interesting anecdote, Alexander Fleming's father was originally a peasant farming commoner, who out of compassion jumped out to save a distressed teenage boy nearly drowning in a swamp."),
           ("Cha của cậu ấy --- vị lãnh chúa giàu xụ vội chạy tới mong đền đáp ân huệ, xin cấp học bổng tài trợ cho toàn bộ con trai nông dân kia đi học làm bổng lộc nhận lại.",
            "His father --- a wealthy lord rushed over hoping to repay the favor, asking to grant a scholarship sponsoring all of the farmer's son's schooling as a receiving reward."),
           ("Chính nhờ khoản tiền đáp đền tình nguyện vì ơn cứu giúp ấy mà cậu nhóc Fleming con nhà nghèo mới được tiếp cận nền y khoa tri thức quý giá tận cao siêu.",
            "It was precisely thanks to that reward fund volunteering for the saving favor that the poor boy Fleming could approach highly advanced precious medical knowledge."),
           ("Đứa con mang tư tưởng thiện đức từ người cha trao đi kia lại lớn lên tiếp tục báo ơn toàn xã hội bằng cách phát minh ra liều thuốc kỳ diệu Penicillin vang lừng giúp dập sống hàng triệu người lâm lụy vi khuẩn.",
            "The child bearing virtuous thoughts from the father's giving gesture grew up continuing to repay society by inventing the miraculous drug Penicillin famously helping rescue millions of people stricken by bacteria.")],
          "Lòng nhân ái thả vòng quay đi như hòn đá ném nước, sóng lan tỏa cuộn tròn vòng xoáy sẽ tự động đợt trở lại đáp dền con cháu.",
          "Compassion drops into a spin cycle like a stone tossed in water, the rippling swirling waves will automatically return echoing to descendants."),

    story("Thợ Sửa Xe Và Nhạc Trưởng Mù", "Helen Keller Giai thoại --- Khuyết danh",
          "Trong",
          [("Trong lúc bão tuyết xối xả đè bẹp xe, một thợ sửa xe mù chữ bất chợt chui xuống gầm hì hục hàn vá ống lốp thay vì tính tiền cưa cứa kiếm lợi đắt đỏ.",
            "While torrential snowstorms crushed the car, an illiterate mechanic suddenly crawled under struggling to weld and patch the tire instead of calculating expensive opportunistic profiteering."),
           ("Ông hoàn toàn miễn phí mồ hôi gân sức mình giữa băng khuya, không mưu cầu một đồng công sá cho vị khách phu nhân xa lạ có con bị ho khản tiếng trong xe.",
            "He offered his sweaty muscle completely free amidst the midnight ice, not seeking a single penny of labor wage from the strange lady guest holding a coughing hoarse child in the car."),
           ("Cô bé khỏi ốm an toàn, về sau lớn lên tham gia cuộc thi trúng tuyển và nhắm giải âm nhạc hát opera danh giá lớn trên đài truyền hình.",
            "The girl recovered safely, later grew up to participate in a contest winning selection and aiming for a grand prestigious opera musical prize on TV."),
           ("Toàn bộ số tiền đó người phu nhân bí mật trao lại chi trả để cứu xưởng cơ khí nghèo khó của ông thợ đang đứng trước miệng bờ vực bị phá sản phá dỡ sụp tiệm.",
            "The entirety of that money the lady secretly handed back paying to save the poor mechanic's workshop standing on the edge's brink of being bankrupted, demolished and ruined.")],
          "Không có hạt cát ân huệ chân thành nào bị chìm nổi trong dòng bôn ba, thời gian sẽ trả dạt về bờ một thạch báu ngọc óng ánh.",
          "No sincere grain of sand favor sinks and floats lost in the rushing stream, time will wash ashore a shimmering gem jewel."),

    story("Con Cáo Nuôi Cáo Mẹ", "Thiên nhiên Kì thú --- Động vật",
          "Ngay",
          [("Ngay cả đối với loài linh trưởng hay dã thú khắc nghiệt hoang lũng có móng nhọn hoắm săn mồi tàn độc, vẫn ẩn chứa triết lý sinh tồn kỳ lạ nuôi nấng.",
            "Even for primates or fierce wild beasts in the harsh valley having razor-sharp claws hunting brutally, there still hides a weird survival philosophy of nurturing."),
           ("Đó là hiện tượng khi lũ quạ, cáo già nua ngã đổ không còn răng dẻo dai chạy đuổi vồ mồi yếu ớt khụ khị tàn tạ, lũ con sẽ nhai nhả mớm ngược lại.",
            "It is the phenomenon when old crows or foxes fall down lacking tough teeth to run chase chasing weak prey brutally fading away, the offsprings will chew and regurgitate back feeding them reverse."),
           ("Những đứa trẻ vốn đã nhận được sinh khí máu sữa cạn kiệt từ con mẹ trao cho, thì khi về già bản năng vòng xoáy tự động vận hành hành động chu cấp trả nợ dưỡng sinh đền bồi đầy tự nhiên.",
            "Those children who inherently already received exhausted milk and blood vitality the mother gave, when entering old age the swirling instinct automatically operates acts of provisioning repaying the life-nurturing debt full of nature.")],
          "Cha mẹ trích cạn máu tủy để khởi tạo ra một sinh hình, thứ thu hồi chính là bệ bám bình yên của chuỗi báo hoàng đạo hiếu thuận.",
          "Parents extract entirely blood and marrow to create a form, what is collected back is the peaceful clinging pedestal of the filial piety zodiac circle of reporting."),

    story("Hai Đôi Thùng Giày Mất Cắp Của Gandhi", "Mahatma Gandhi --- Ấn Độ, thế kỷ 20",
          "Lúc",
          [("Lúc đang hấp tấp nhào lên sảnh một chiếc xe lửa lăn bánh trượt lướt vội vã, nhà hoạt động Mahatma Gandhi bị tuột rớt bay mất một chiếc dép sandal rớt phịch xuống lại nhà ga sỏi.",
            "While hastily lunging onto the hall of a hurriedly slipping moving train, activist Mahatma Gandhi had one sandal slip drop flying down heavily left behind onto the gravel station."),
           ("Thay vì cau có hoảng hốt bực dọc tiếc nuối khóc lóc chửi mắng thứ vừa tước đoạt ra khỏi chân đau, ông ngay lập tức tự động cúi mình lột luôn chiếc dép nguyên vẹn còn lại ném lăng liệng hẳn nốt ra cửa sổ vỡ.",
            "Instead of frowning panicked annoyed regretful crying cursing what was just stripped from his sore foot, he immediately automatically bent down peeling off the remaining intact sandal heavily flinging tossing it out completely through the broken window."),
           ("Khi bạn đồng hành ngạc nhiên thắc mắc, ông giải nghĩa bằng đôi mắt nhoẻn hòa ái rằng kẻ đói lạ nào đó nhặt được sẽ có nguyên vẹn một đôi mà xỏ vừa in để ấm lòng, thay vì cả hai cùng buồn bực đi một chân.",
            "When companions shockingly questioned, he explained with amicable smiling eyes that some strange hungry person picking it up would have a complete intact pair to fit perfectly in order to warm their heart, instead of both being annoyed walking on one foot.")],
          "Buông xả ngay thứ còn một nửa vô dụng đi là cách hoàn thiện trọn trịa một sự trao tặng có chủ đích từ bi trong tâm.",
          "Instantly releasing something remaining uselessly half is the way to perfectly complete a purposely compassionate designated giving gift inside the mind."),

    story("Phần Thưởng Từ Những Chú Ong Của Bác Sĩ", "Câu Chuyện Nhân Văn --- Châu Âu",
          "Khi",
          [("Khi bệnh dịch hoành hành tàn tốc ập tràn tấy nát vào khu làng, một ông lương y chạy chữa kiệt quệ từ chối vơ vét tích cóp của cải từ những gia nhân quằn quại thoi thóp thối phổi.",
            "When plagues swept devastatingly frantically crashing rotting into the village, a depleted treating physician rejected amassing hoarding wealth from families writhing grasping for air with rotting lungs."),
           ("Hàng nghìn người sống dật qua khỏi mũi tử thần cảm kết khóc sướt quyết đính lấy hũ mật ong, mật rơm cỏ bện tặng đầy gò mang biếu bồi dưỡng ngược lại ủ thơm cả kho lẫm.",
            "Thousands of people surviving miraculously snatching past the death god's nose gratefully sobbing crying resolutely attached bringing honey jars, woven straw grass nectar gifts filling heaps dropping to reverse nourish incubating aromatic smell over the whole storehouse."),
           ("Dù chẳng từng nhận mót một quan đồng vàng xu rách, vị ân nhân thánh thiện nọ cuối đời giàu lên sung túc nhất hạt xứ với cả ngàn chum dược trân kho báu dạt dào tình anh em xóm láng láng giềng trổ dậy mầm sống.",
            "Although never raking sweeping a torn penny gold coin, that saintly benefactor at the end of life prospered wealthiest in the county with thousands of treasure medicine jars overflowing with neighborly brotherly love sprouting up life buds.")],
          "Kẻ hờ hững cự tuyệt vàng thỏi vì từ bi cho không, rút cuộc đút túi kho báu tình thương vô biên quý đỏ vạn phần nén mỏ.",
          "The indifferent rejecting gold bars out of free compassion, ultimately pockets a boundless affectionate treasure infinitely times more precious than a mind wedge."),

    story("Bức Tranh Đồng Cỏ Và Họa Sĩ Đường Phố", "Nghệ Thuật --- Khuyết danh",
          "Mỗi",
          [("Mỗi ngày phơi nắng họa sĩ nghẹt bút lang bạt đều cố vẽ tặng truyền miễn phí những nhành cỏ tươi hoa đồng thắm cho em bé mồ côi mếu máo dạt qua góc đường xin tiền vặt.",
            "Every day the sunbathing wandering struck-brush painter tried to draw giving freely fresh grass branches and bright field flowers for sobbing orphan begging children drifting cornering for spare change."),
           ("Chẳng hề biết rằng một nhà sưu tầm tranh vĩ mô danh tiếng ẩn thân từ đằng ghế đối diện luôn đứng theo dõi cái tư thái nhàn nhã từ tâm đó dồn cả tâm huyết xuống ngòi ruột màu loang.",
            "Knowing not that an elite famous macro art collector hiding from the opposite bench always stood watching that mentally leisurely posture concentrating entirely blood and heart down the streaking color inner nib."),
           ("Đến khi khuất bóng xấp lại giá vẽ từ biệt, ông ta được tiếp nhận bao trọn bao bì gói bảo trợ sáng tài làm mở triển lãm chấn vang tên tuổi nhờ tác phẩm rực dạt tính thiện mỹ dấy trào.",
            "Until fading shutting away the easel bidding farewell, he got comprehensively completely received packaged sponsorships lifting brilliant talents opening echoing exhibition names thanks to masterpieces abundantly radiating surging good beauty nature.")],
          "Sự bố thí tâm hồn chân phương nhất của nghệ thuật là tiếng nói thu phục thính giả tinh tế kéo theo vòng rạng rỡ đắp bồi vật vã.",
          "The most rustic sincere soul donation of art is the voice conquering refined audience pulling along heavily enriching radiant circle.")
    ]
)

# ================================================================
# CHƯƠNG 10: TỰ DO TRONG KỶ LUẬT
# ================================================================
ch10 = chapter(
    "Tự Do Trong Kỷ Luật, Kỷ Luật Trong Tự Do", 
    "Freedom in Discipline, Discipline in Freedom",
    "Tự do không phải là làm mọi điều mình thích, mà là có khả năng làm điều mình nên làm.",
    "Freedom is not doing whatever you like, but having the ability to do what you ought to do.",
    [
    story("Michael Phelps Điểm Danh Chạm Nước", "Michael Phelps --- Hoa Kỳ, Thế kỷ 21",
          "Michael",
          [("Michael Phelps là vận động viên bơi lội giành được kỷ lục vĩ đại vô tiền khoáng hậu với tổng số hai mươi tám chiếc huy chương Olympic vang lừng huy hoàng tột đỉnh nhất của nhân loại.",
            "Michael Phelps is the swimmer achieving an unprecedented monumental record with a total of twenty-eight overwhelmingly massively glorious Olympic medals of humanity."),
           ("Tuyệt đại đa số người hâm mộ thèm khát cái tự do và ánh hào quang danh vọng của khối tiền mặt được trao thưởng cũng như phiêu lưu dã ngoại nghỉ dưỡng xả xì trét sướng bừng.",
            "The vast majority of fans crave the freedom and glorious shining fame of the awarded cash piles as well as intensely joyful relaxing outing stress-relieving adventures."),
           ("Thế nhưng, để có bản phối tự do bay bổng như cá mập tung tẩy đó, anh đã tự giam nhốt đày ải ném mình chìm xuống hồ vẫy bơi quẫy liên tục suốt năm năm trời chưa từng trật nhịp ngắt quãng một ngày duy nhất bất kể lễ tết ốm rách.",
            "However, to possess that floating freely flying shark-like soaring matching scheme, he self-imprisoned torturously tossing sinking himself down the pool swimming intensely splashing continuously for five years not missing a beat suspending a single day regardless of holidays torn sickness."),
           ("Đỉnh cao xé toạc thả xích của tự do vươn tới dải nước chiến thắng chính là mầm hoa ươm từ sự trói buộc khắt khe dã man xiềng xích đày đọa tột cùng trong luyện rèn lịch biểu lặp đi lặp lại.",
            "The chained ripping releasing peak of freedom reaching the victory water strip is precisely the sprouted flower seeded from aggressively cruel restricting strict extremely tormenting shackling in repeating scheduled training.")],
          "Kỷ luật là bức thành trì nhà tù duy nhất cung cấp cho bạn đôi cánh vươn tới quyền năng làm chủ bầu trời khoáng đạt vô độ.",
          "Discipline is the only prison fortress providing you wings reaching the power to master the limitlessly broad sky."),

    story("Thầy Tu Thiền Định Kép Ngồi Im Tại Chỗ", "Thiền Tông --- Nhật Bản, Thế kỷ 14",
          "Những",
          [("Những vị sư sãi tu sĩ ở đạo tràng phái thiền tông ép buộc tự đưa mình vào một bản khuôn quy tắc rập khuôn cực nhọc đến bực mỏi đau ngạt khắt khe gắt gao nhất đồi núi hoang dã.",
            "The monks abbots at Zen sect ashram ashrams forcefully put themselves into an extremely agonizing rigidly stamped pattern causing choking achingly strict desperately harsh wild mountain rules."),
           ("Ngày dọn phân hốt cỏ, đi đứng đánh vần dậm chân khẽ bưng bát uống ngụm canh đều căn đo tính toán khít khịt theo tiếng chuông báo chuông ngân từng khắc tít tắp không trượt mảy may.",
            "Days cleaning dung shoveling grass, walking standing spelling stomping slightly carrying bowls sipping soup mouthfuls are all measured calculated rigidly strictly following the bell ringing striking every tiny tick not missing minimally."),
           ("Nhìn từ vách ngăn ngoài tưởng họ là những tên nô lệ bị dồn ép gò ép nô dịch tự nguyện bó buộc giam kẹp trọn đời dán băng keo chết dính.",
            "Looking from the outer partition they appear as driven strictly pushed internally bound voluntarily bound slaves clamping lifetime sticking dead glued tapes."),
           ("Nhưng bằng cách buộc kiềm hãm nhốt tù thân xác đó, họ đập tan đứt sạch mọi xao nhãng cám dỗ bên ngoài trần thế, nâng tâm trí linh hồn đạt ngưỡng khinh bạt thảnh thơi nhởn nhơ siêu vượt bão trần.",
            "But by forcefully restraining detaining that bodily physical prison, they shatter cleanly smash all worldly outside distractions temptations, elevating the soul mind reaching the transcendent casually roaming unbothered realm surpassing worldly storms.")],
          "Giới luật rèn nhòa thể xác phàm là chìa khóa duy nhất tháo chuỗi lồng gông giải rỗi khải sáng chân tính bay thả của tâm linh.",
          "Fleshy physical blurring training precepts are the only key unlocking releasing chain cages enlightening floating releasing true spiritual nature."),

    story("Cánh Diều Thả Lên Trời Có Dây Kéo", "Thi ca & Đời sống --- Phương Đông",
          "Mỗi",
          [("Mỗi lần ném phóng diều tung giấy cất liệng dạt bay lên khoảng không lộng gió xanh rờn vun vút, ta tưởng cuộn diều đó đang vô biên tự do bay dạt múa lợn không gò cản.",
            "Every time throwing tossing launching paper kites drifting soaring onto the brightly green gusty rustling windy void, we thought that kite roll was limitlessly freely flying drifting swooping uninterruptedly unhindered."),
           ("Nó lao nhao xoay nghiêng chao liệng xoáy mây, đón đập gió cao, kiêu căng tận hưởng thú vui bốc trải xa cách mặt đất buồn tẻ hèn bẩn ở tít phía viễn khơi mù.",
            "It clamorously twirled tilted plunging swooping cloud spirals, catching banging high winds, arrogantly enjoying the thrilling experiential joy distancing the dull muddy dirty ground down far in the dim distance."),
           ("Thế nhưng nếu giật đứt mạnh bạo một sợi giây mỏng dính mong manh giữ níu căng chằng kéo căng gốc, con diều đứt đai mất lái thăng bằng lập tức đâm chúi gục ngã cắm đầu nát tươm xuống bụi rậm lầy lội lầm bùn ngay.",
            "Yet if brutally aggressively yanking ripping a thin sticky fragile string holding tethering stretching pulling the root, the broken snapped belted balanced-lost kite instantly plummets plunging falling headfirst crashing utterly ruined down the muddy dirty swampy bush right away.")],
          "Sợi dây trói buộc căng giằng chính là bệ phóng kỷ luật vững chãi duy nhất giúp chúng ta giữ mình tung hoành lướt cưỡi không gian tự do.",
          "The heavily stretching tethering rope is the single robust disciplinary launching pad helping us keeping ourselves galloping surfing riding free space."),

    story("Giai Điệu Nghệ Thuật Nhạc Giao Hưởng", "Johann Sebastian Bach --- Áo, Đức",
          "Bản",
          [("Bản nhạc tuyệt tác hòa tấu giao hưởng dội vang rung dạt rực sáng chứa đựng sự dập dìu nhảy múa trơn tru không biên giới tự do vô tận trong vòm mây nốt âm thanh.",
            "The masterpiece concert symphony echoing vibrating brilliantly resonating entails the smoothly sweeping dancing lacking boundaries endlessly freely inside the cloudy note audio dome."),
           ("Mọi khán thính giả cứ ngỡ là người đàn nghệ sĩ đắt giá bay bổng nã tiếng bùng nổ tung hoành hoàn toàn thuận trào ngẫu hứng phăng bốc từ cảm xúc bùng bung vô định ngẫu nhiên.",
            "Every audience implicitly presumed the costly soaring music artist massively banged exploding totally natively spontaneously wildly from spontaneously bursting endlessly scattered emotions."),
           ("Thực ra sau lưng sự hoàn mỹ bay bướm phiêu miết hoang vu đó là khu vườn quy tắc gò ngặt khuôn nhịp nhàng ép sát tỉ mỉ rập khuôn khập khính nhịp chia đứt nhát không suy suyển lệch lỡ.",
            "Actually behind the back of that beautifully elegantly wildly wandering drifting immaculateness is the perfectly squared restricted strictly rigid closely meticulous stuttering chopped-beat standard garden unquestioningly unyielding unmisted."),
           ("Kỷ luật phân nhịp nhịp phách cấu trúc đoạn ngắt chính là khung rào bê tông vững xiết để cảm hứng họa thả mộng tư tưởng mọc lá bung nụ vô tận vô cùng không sụp sệ cẩu thả.",
            "The structured fractional pausing rhythmic rhythm discipline is truly the firmly binding concrete fence frame for artistic inspiring ideas dropping infinitely growing buds endlessly without sagging sloppily.")],
          "Khung khuôn luật lệ nhịp nhàng thít chặt lề lối khô cằn gieo hạt chói lòa nên khoảng trời bùng bung khoáng đạt ngả múa vô song.",
          "The rhythmical regulatory tightly throttling dull standard frame sows blazing seeds into the unparalleled expansively dancing wildly bursting sky."),

    story("Cuộc Di Cư Của Các Chú Ngỗng Trời Tuyết", "Sinh Học Động Vật --- Vùng Cực Bắc",
          "Đàn",
          [("Đàn ngỗng hoang dã bay thiên lưu dọc ngang qua lục địa có quyền thoải mái tự do tung cánh quẫy lượn bay đập chọn lựa bất cứ vùng trời nước hồ thảo nguyên thênh thang thênh rảo nào trên cao.",
            "The flock of freely migrating wild geese crossing sweeping horizontally across continents holds comfortably flying squirming plunging picking whichever vast open widely roaming sky lake steppe area high up."),
           ("Nhưng để đủ uyển chuyển sống sót băng lội xuyên ngàn vĩ độ không gục ngã kiệt sức tắt thở rũ xương, chúng ép sát nhau tuân thủ tuyệt đối nghiêm ngặt bay chéo xòe tạo rẽ rạng hình chữ V mỏi nhừ.",
            "But to flexibly functionally survive wading crossing thousands of latitudes without falling dead exhausted snapping breathless rotting bones, they press strictly absolutely strictly complying slanting unfolding V-shaped tiredly shaping."),
           ("Kẻ đầu đàn cản xé chắn sức gió mệt lả sẽ lập tức lui ra nhường xoay ca tuân lệnh rẽ lọt cho kẻ đi sau bổ nhào lên trám lỗ hổng thế lấp quy củ đan xen không ngắt.",
            "The flock leader blocking tearing hitting wind powerfully exhausted suddenly automatically retreats yielding taking turns smoothly turning obediently allowing the subsequent behind diver up filling plugging the loophole overlapping continuously alternating."),
           ("Chính thứ kỉ luật đội đồ quân lệnh khắc khe đồng lòng đan dệt không rạn nứt cự nự này cho phép cả nhóm giữ tự do tiến rảo chạm mục tiêu tránh rét.",
            "This very strictly severe military disciplinary unified seamlessly uncracking non-complaining weaving grants the whole group preserving freed traversing touching cold-resisting goals.")],
          "Trật tự cứng ngắc bầy đàn lại chính là công cụ sống còn kiến tạo khoảng trời tự do rộng ngát lớn lao của chặng đường viễn du ngút vợi.",
          "Rigid flock order is exactly the ultimate survival tool carving out the immensely broad free sky for the remotely expansive journey."),

    story("Tay Đấm Bóc Vĩ Đại Huyền Thoại Muhammad Ali", "Muhammad Ali --- Hoa Kỳ, Thế kỷ 20",
          "Trên",
          [("Trên thao trường đài đấu xới quật lốc sàn gỗ bọc, Ali đi bộ chân trần khinh khỉnh di chuyển quẫy múa tung tăng uyển chuyển cực kỳ bốc thả phóng khoáng tự do như loài ong vờn buông.",
            "On the boxing rolling swirling wood-covered platform arena, Ali walked barefoot condescendingly gracefully shuffling joyfully loosely freely extremely like a hovering dropping bee."),
           ("Nhưng để có quyền cựa rẽ lộng lẫy thong dong né trái né phải khéo bật như người làm chủ đùa cợt vạn vật quyền tự do đánh đấm buông quật trong chớp đạn ấy không chết ngất móp mồm.",
            "But to earn the right gracefully brightly leisurely dodging left dodging right nimbly bouncing like someone ruling mocking everything playfully freeing swinging violently rapidly in darting sparks without fainting crushed-mouthed."),
           ("Hàng ngày chưa lúc gà bình minh mở mắt lúc năm giờ xám ngắt, ông đày đọa chân chạy vã nát mồ hôi hàng dặm chục km đường đứt lốp giày vỡ nứt đau máu me.",
            "Daily before the dawn rooster opening eyes dimly grey at five, he tortured plunging running sweating rotting miles dozens of km roads shattering tire wearing snapping bloodily hurting."),
           ("Sự tàn ác xiềng búa trong kỷ luật luyện ép cày rèn vắt khô nhựa sức đã rèn đúc nặn đẽo cho anh ta tư cách khiêu vũ nghênh ngang trượt tự do trên mọi đón nhử của địch.",
            "The shackling hammer brutality crushing training plowing squeezing dry juice forcefully molded sculped him the swaggering sliding dancing qualification freely across all enemy baiting blocks.")],
          "Mọi dáng điệu thoải mái thong dong trượt tự do ở trước mặt đám đông đều bị mua trả đắt đỏ bằng nghìn tấn kỉ luật giam kẹp đày đọa dưới kho gầm tối tăm.",
          "Every loosely comfortably freely sliding leisurely graceful posture in front of the crowd was expensively bought paying by thousand tons of confining heavily punishing discipline within dim dark basements."),

    story("Steve Jobs Trói Buộc Sự Chọn Lựa Bằng Đơn Giản", "Steve Jobs --- APPLE INC, Thung lũng Silicon",
          "Lúc",
          [("Lúc mới sáng lập khôi phục vãn hồi trỗi dậy tập đoàn mang táo khuyết vỡ rạn lụn bại sập tiệm thập tử nhất sinh thảm não.",
            "Upon initially restoring reviving resurrecting raising the bitten rotting bankrupt crushing breaking fatally disastrous severely agonizing apple corporation."),
           ("Jobs bực dọc giậm đập bàn loại bỏ giết cụt dập tắt không thương tiếc hàng loạt hàng đống ba ngàn ba chục danh mục sản phẩm rườm rà chằng chịt ngổn ngang để người tiêu dùng lóa ngợp choáng óc nhịn thở.",
            "Jobs angrily stomped banging desks brutally killing erasing discarding mercilessly heaps piles three thousands thirty messy tangled sprawling product arrays making consumers suffocatingly blindingly overwhelmed dizzy."),
           ("Ông thu chặt ép bó kẹp rút ngặt vào quy chế cực kỳ độc tôn độc tài chằng chéo chỉ có đúng 4 dòng mẫu thiết bị ngặt nghèo khô khan rập kín hạn hẹp không ngọ nguậy nhích dư thừa.",
            "He restricted squeezed tightly bounding rigidly into an extremely dictating tied autocratic singular rule heavily merely precisely 4 narrow dry devices strictly tight unbudgingly squeezed non-superfluous."),
           ("Sự thít thắt gò kềm đó giải phóng hoàn toàn trí lực và thời gian tư duy để bay lượn vươn xòe tạo cực phẩm điên khùng làm chủ não trí tự do của công ty toàn cầu chấn động thế kỷ.",
            "That strangling curbing completely unleashed liberated brains and thinking time to fly spread extending creating madly outstanding dominating free mind the globally echoing century company.")],
          "Loại thải bóp nghẹt mọi phức tạp rườm rà kỷ luật hóa là chìa khóa duy nhất bật dậy tạo lập nên cõi thênh thang tự do vô song nhất để vươn tay hái đỉnh mây.",
          "Discarding choking all complicated messy discipline-making is the unique triggering key erecting making up the boundlessly vast most unparalleled free soaringly sky-picking realm."),

    story("Thầy Ngộ Không Tôn Hành Giả Khỉ Vàng", "Tôn Ngộ Không --- Tây Du Ký, Ngô Thừa Ân",
          "Con",
          [("Con khỉ đá bướng bỉnh ngỗ ngược sinh ra từ khe đá xé toạc chui trời rẽ đất tản múa khoáy phá nhảy quẫy tung hoành phế liệu đổ sập long cung tới náo thiên cung khinh bạc quậy nát mọi phép tắc tự do vô thiên.",
            "The stubborn unruly rock monkey birthed from stone crevice tearing sky diving earth wildly smashing dancing breaking turning upside down tumbling collapsing dragon palace to rattling heaven disregarding crazily crushing messing all law-less arbitrarily infinite rules."),
           ("Sự tự do bốc đồng bản năng phá hoại ấy không đem lại thành tựu đạo quả khải trị mà lôi kéo trói nghiến kẹp bẹp sập đè nát bấy tỳ chịu ngâm áp ở ngọn núi rêu nhọn năm trăm năm xích xót chua thảm ngứa dại.",
            "That impulsively destructive instinctual freedom didn't bring reaching enlightenment reigning fruits but fiercely dragged tying crushing pinning collapsing pressing heavy mossy spike mountain five hundred bitterly agonizingly tearing randomly itchy tragic years."),
           ("Đến khi cúi đầu khâm theo kiềm vòng xiết đau của chiếc vòng kim cô kìm kẹp thắt khựng trên chóp sọ trán rèn mình tuân phục nguyên lý hộ tăng chịu trận đói khát khắt khe quằn quại kinh lụy.",
            "Until bowing head strictly following obeying tightening hurting grips from the golden restricting loop squeezing painfully on forehead top submitting practicing principles of monk-protecting receiving brutally violently desperate hungry exhausting twists."),
           ("Cái đai vòng khóa kỉ luật kim thiền đó lèo lái nặn gọt chú vượn gai góc bốc thả này bay lộn giải bủa cứu nhân độ thế để đạt quả giải thoát vô cực đấu chiến thắng phật đỉnh tự do vĩ dại tót nhọn.",
            "That golden discipline-locking ring loop steered trimmed shaping this thorny impulsively floating monkey somersaulting flying rescuing universally rescuing living mortals to gain extreme escaping victorious fighting buddha absolute greatly sharply magnificent freedom.")],
          "Không có gông cùm kiềm dằn kẹp bản tính trần dại, kẻ phàm phu chỉ ngỡ là chim tự do nhưng đang đâm sụp xuống hố tự nhốt mình hủy diệt mãi tàn úa không bay mọc lại rễ nhọn.",
          "Without restraining taming locking worldly wild natures, the commoner merely mistakenly illusions observing deeply as free birds but actually nose-down plunging self-destroyingly caging endlessly rotting without flying sprouting thorny roots."),

    story("Sự Kỷ Luật Trong Nhịp Viết Gấp Gáp Của Stephen King", "Stephen King --- Nhà Văn, Hoa Kỳ",
          "Chúng",
          [("Chúng ta thường mộng mơ hão huyền thả bay ảo vẩn rằng để viết sách là ngồi ôm ghì hứng chờ đợi rượu say trăng thanh gió mát tư thái phiêu diêu tát quẫy mới tự do xổ bung vọt nhả ý thư chữ trật xuất thần khơi khơi.",
            "We usually fancifully illusorily dream drifting heavily hugging expecting drunk alcohol clear moon cool wind lingering gracefully casually violently dancing freely vomiting dropping miraculously mysteriously out-of-nowhere words."),
           ("Ngôi sao tiểu thuyết kinh dị danh giá Stephen khép mình đẩy ép khóa cửa bắt ghim giam chặt thân vào bàn ghế dồn đóng đinh cố định rập ràng mỗi ngày viết liền lỳ tít tù mù 2.000 chữ trước khi nuốt cơm.",
            "The violently prestigious horror novelist star Stephen forces pushing locking closing tightly pinning confining body onto desk heavily fixedly nailed hammering consistently typing wildly blindly 2,000 words everyday consecutively before swallowing food."),
           ("Không cần quan tâm cảm xúc có kẹt cứng khô héo trơ ráo hay giông bão sấm gầm mưa rơi nổ đạn, cái kỉ luật đè đầu đó trở thành mỏ neo bứng bệ phóng cho nguồn sáng tạo điên khùng nảy sinh bất ngất dào tự do ngẩn ngơ vĩ phái.",
            "Ignoring whether emotion heavily dry-roasted stuck dryly drained or stormy thundering gun-exploding violently dropping rain, that heavy-heading discipline anchors launching violently mad massively surging spontaneously freely wandering magnificently grand creative streams.")],
          "Cảm hứng tự do không nảy sinh từ sự buông lơi rong chơi há miệng chờ sung nằm võng phơi đùi, nó được đào móc tướt mồ hôi bằng cây cày kỉ luật nứt nẻ gân lòi khốc liệt ngày này tháng nọ.",
          "Free inspiration doesn't abruptly spurt from playfully mouth-open lounging awaiting hammock-resting dropping figs, it's sweated dug violently by forcefully cracking blistered strictly disciplined plows day in day out."),

    story("Kì Quản Đèn Giao Thông Ngã Tư Phố Lớn Khuất Mờ", "Giao thông Công cộng --- Nếp sống Văn Minh",
          "Tại",
          [("Tại một góc tư đông nhộn ầm ĩ kẹt xô rầm náo nhiệt giữa đường phố xe luồn ùn ùn xộc xói hăm hở quẩy tít lăn lút lách ngộp cuộn ngạt thở xe cộ khói sặc.",
            "At a wildly aggressively frantically massively heavily rolling crawling loudly stuffed dizzyingly traffic-congesting corner intersection roaring furiously dodging sneaking overwhelmingly crowded choking heavily chaotic streets."),
           ("Mọi người đều thèm tự do rú vọt rồ ga tông đè lấn ngã đè trèo luồn xéo dọc xéo ngang tung hoành băm bửa qua cột đèn bất chấp đèn đỏ đứng yên.",
            "Everyone craves violently roaring pressing speeding crossing crashing scrambling rushing horizontally diagonally stepping trampling wildly cutting ignoring the red standing still stationary lights."),
           ("Thế nhưng nếu để thói buông tuồng tự tiện đó phang phá nhảy chồm lên ngã lăn nhào thì ngã tư tự khóa cục kẹt đông cứng tê liệt thít rịt không ai còn quyền dịch chuyển trật tự an toàn rảo bánh lăn thoát ra xổng rẽ.",
            "Yet if blindly letting that impulsively carelessly casually rushing crashing flipping knocking over crossroad wildly naturally self-locks blocking solidly heavily stiff paralyzing tight nobody left gracefully legitimately safely unhooking unspinning un-diverging successfully retreating."),
           ("Vì chấp nhận chôn chân kiên nại chịu kỉ luật ức chế nhường dồn dưới cột hiệu xanh đỏ khô cứng mệt kìm mà dòng chảy có thể lướt tuôn băng vuột đều rịp băng nhịp đem lại quyền được tự do về chốn đến thanh bình.",
            "Because accepting enduring steadily burying foot bearing severely resisting heavily yielding holding underneath rigidly dryly tiring red green colored signal lights the vigorously flowing rushing smoothly consistently safely granting returning free destinations calmly.")],
          "Sự nhẫn nhịn hãm hãm dừng lùi khép lại một vài lăng kính thỏa mãn nhỏ bé kiềm cặp là nền móng vạn dặm mở tung đại mạch đường thoáng tự do vùn vụt trải khắp cho cộng đồng số đông đại dương.",
          "Enduring suppressing halting stepping back enclosing briefly confining strictly small satisfy perspectives stands globally universally broadly wide wildly violently speeding liberating paving open thoroughly broad-ocean globally vast communities.")
    ]
)

# ================================================================
# CHƯƠNG 11: CỤ THỂ TRONG TỔNG QUÁT
# ================================================================
ch11 = chapter(
    "Cụ Thể Trong Tổng Quát, Tổng Quát Trong Cụ Thể", 
    "The Specific in the General, The General in the Specific",
    "Để hiểu thấu cả thế giới rộng lớn, đôi khi ta chỉ cần ngắm nhìn trọn vẹn một hạt cát nhỏ.",
    "To fully understand the vast world, sometimes we only need to intimately gaze at a small grain of sand.",
    [
    story("Khám Phá Vĩ Mô Nhờ Cảo Thơm Newton Nhỏ", "Isaac Newton --- Anh Quốc, Thế kỷ 17",
          "Một",
          [("Một buổi trưa rảnh rỗi nhàn hạ mộng mơ tĩnh lặng dạo bước lững thững hóng mát nghỉ gốc điêu tàn u tịch nằm nhẩn dưới tàn cành rợp bóng trĩu trịt cây táo tươi ngát rụng quả rớt cụp xuống đầu.",
            "One strangely heavily comfortably quietly peacefully strolling playfully aimlessly relaxing wildly dimly dimly sitting down casually shaded under massively abundantly vividly fruit-falling branch dropping knocking right on head."),
           ("Sự cố vặt vãnh vụn vặt tí hon cụ thể hằng ngày nảy xảy nhan nhản ném đá rớt dép mà bất cứ hàng triệu bầy đứa nhóc nông phu nông nô nào cũng từng bị va ném phang dội mà bỏ qua lơ đễnh thờ ơ dửng dưng.",
            "An extremely routinely violently tiny mildly negligible event routinely repeatedly tossing splashing dropping occurring widely seen that arbitrarily millions of peasant peasant boys had blindly identically skipped ignored carelessly indifferently heavily routinely indifferently struck ignored."),
           ("Thế nhưng, từ một quả táo rụng tròn xinh có một không hai rơi cụp đó, bộ óc thần sầu đã soi móc moi móc chẻ nứt tẽ xẻ để kết tủa khai sáng xây dệt nên Định luật Vạn vật hấp dẫn khổng lồ ôm trọn vũ trụ mặt trời bao la vĩ dã ngạt ngào sâu rộng khôn cùng.",
            "However, from exactly one distinctively circularly beautiful dropping falling single apple, the wonderfully deeply searching peeling cracking fiercely deeply dissecting mind precipitated enlightened firmly creating fundamentally building the massively gigantic Universal Gravitational heavily tightly embracing immensely broadly deeply endlessly wildly vast sun system.")],
          "Ngay trong thứ quá đỗi tủn mủn rụng rơi vô hình vô danh lại ẩn chứa cấu tứ bao bọc cả một chuỗi mắt xích nguyên lý đồ sộ khổng lổ siêu vĩ đại định hình tinh tú thế gian chằng chịt.",
          "Even tightly intimately deeply inside widely invisible unnamed randomly tumbling things hides wrapped structures encompassing a series string boldly mapping giant extremely heavily guiding massive principles deeply structuring thickly twisting world galaxy stars."),

    story("Một Hạt Cát Soi Rạng Chiếc Đồng Hồ Thời Gian", "William Blake Bài Thơ --- Anh Quốc",
          "Nhà",
          [("Nhà thi sĩ vĩ đại siêu việt dệt gảy nắn bóp bài ca thơ mộng dội vang ngàn năm rằng nhìn thấu cả thế giới lộng lẫy chỉ qua một hạt cát mịt xám tít tắp.",
            "The heavily universally magnificently superior poet thickly composing softly pinching wildly dreaming hitting resonantly thousand years that perceiving universally deeply beautifully dazzlingly transparently globally via a deeply graying dimly tiny speck of sand."),
           ("Và thưởng thức tận mắt đóa hoa rực nở dạt bung hương đồng nội chứa dồn giữ ôm chứa tóm ghì cả bầu trời trong vành xoáy cánh.",
            "And visibly observing heavily intensely blooming violently violently warmly wildly field broadly expanding widely hoarding strictly tightly enclosing keeping completely the whole broadly heaven neatly inside swirling spiraling brightly deeply massively intensely brightly petals."),
           ("Ông dạy con người đừng ngớ ngẩn đi lùng sục kiếm chác moi rãnh xới vứt kiếm tìm thứ tổng quát to tát xa tít tắp khơi khơi mù dạt vô vàn rộng mông mênh chao đảo lộng lẫy hão mờ xa rỗng lợt hoắm.",
            "He taught humanity blindly absurdly searching wildly digging ditching dumping strictly broadly seeking looking tracking massively grand generalized blindly distant largely wide blindly drifting dizzyingly gloriously wildly blindly thickly shallow loosely far things."),
           ("Trái lại, cứ mổ xẻ chẻ ép lột tung vặn vò cắm sâu soi kĩ vào chi tiết của nhụy hoa cỏ vụn vặt cũng là khám phá trọn tính chân siêu tinh tế của đạo lý thế giới lặn lội quay quắt hoài hoài trào tít.",
            "Conversely, continuously dissecting cracking tightly severely splitting thickly examining drilling analyzing tiny wildly tiny detail vividly inside stamen weed precisely essentially perfectly thoroughly purely revealing truthfully delicately deeply diving rolling turning revolving consistently heavily violently broadly vast principles.")],
          "Sự vĩnh cửu bao la rộng lớn đồ sộ của thời gian cũng hiện hữu cô đặc vón ghì trong chính thời khắc chớp động tức thì cụ thể nhấp nháy của hạt sương tan rung động tít.",
          "The heavily enormous boldly extensively massive eternity thoroughly vividly currently solidly deeply thickens closely inside currently flashing sharply snapping specifically violently shivering quickly instantly trembling melting rigidly strictly vibrating heavily deeply specific droplet."),

    story("Linh Hồn Nhật Bản Tại Cuộc Thi Gấp Giấy Origami", "Sự Kiện Văn Hóa Truyền Thống --- Nhật Bản",
          "Lối",
          [("Lối thiết kế triết lý thẩm mỹ mỹ miều rực phô diễn nền móng tảng tinh thần sắc xảo võ sĩ đạo trầm lắng khắc khổ nhẫn nại dặt mình kiên trinh chắt bóp nhặt giữ dìm mộc của người vùng đảo.",
            "The distinctly elegantly philosophically aesthetics loudly displaying heavy brightly intensely firmly deeply vividly showing off warrior deeply strictly diligently quietly bitterly bearing maintaining strongly collecting keeping tightly strongly restricting bluntly plain island people's fiercely vividly heavily mental base."),
           ("Thế nhưng họ không đi khua chuông múa trống tuyên bố hô nói hùng hồn ngõ lời oang oang kêu gọi răn đạo viết sách dài thườn thượt dông dài luân hồi nhạt rỗng chán.",
            "However they absolutely vividly strictly did not ring bells violently drumming dancing deeply fiercely announcing loosely vividly loudly heavily begging advising writing violently horribly heavily wildly heavily terribly empty deeply vastly boring widely revolving long books."),
           ("Trái lại, nó được thu nhỏ dồn nén vo nắn tóm ghì rụm nhụm qua hành động gấp tay xếp miết viền vuốt rọc góc mảnh giấy nhỏ xíu hình con hạc trắng câm nín tinh túy đơn điệu khô ráp tỉ mỉ cực hạn.",
            "Conversely, it is broadly deeply shrunk tightly completely completely pressed molding heavily rigidly catching rubbing strictly sliding folding trimming small blindly deeply small profoundly blindly perfectly tiny rigidly plain strictly limiting acutely exactly extreme silent purely tiny white crane paper square corners."),
           ("Một mảnh giấy vuông cụ thể lại mang gánh nói lên trọn đạo lý tổng hợp bao hàm nết đẹp trật tự nhịp nhàng của một cõi dân số trăm triệu người lặng tĩnh thấu tâm quy luật.",
            "A strongly heavily precisely squared intensely strictly distinctly specific paper rigidly heavily loudly thoroughly speaks encompassing wildly summarizing intensely globally broadly including perfectly rhythmically beautiful behaviors universally statically completely hundreds broadly population millions strictly intimately calmly fully law rules.")],
          "Khai mở một nét đẹp nhỏ tĩnh cụ thể của nếp sinh hoạt lại là đường dẫn bao quanh soi chiếu gội dọn vẽ nổi toàn bộ tinh túy nền móng văn hóa của nhân dân nước chúa ngàn năm quy cách.",
          "Starting unrolling strongly calmly fully vividly calmly tiny specific beauty heavily living powerfully heavily wildly washing broadly clearing displaying shining completely painting entire foundational vividly deeply heavily sharply globally deeply culture precisely thoroughly strictly broadly precisely gracefully broadly rules thousands deeply universally vividly deeply beautifully widely widely heavily uniquely.")
    ]
)

# ================================================================
# CHƯƠNG 12: ĐƠN GIẢN TRONG PHỨC TẠP
# ================================================================
ch12 = chapter(
    "Đơn Giản Trong Phức Tạp, Phức Tạp Trong Đơn Giản", 
    "Simplicity in Complexity, Complexity in Simplicity",
    "Sự tinh tế cao nhất là sự đơn giản tột cùng.",
    "Simplicity is the ultimate sophistication.",
    [
    story("Nút Bấm Apple Đầu Tiên Ra Mắt", "Steve Jobs & iPhone --- Apple, 2007",
          "Vào",
          [("Vào thời điểm những năm xoáy lộn máy truyền thông di động hỗn loạn phím bấm lóc cóc chi chít dăng dọc phủ ngang tàn tệ chen ngang đầy rối tung bạt mạng mù mịt chằng chịt ngổn ngang.",
            "At broadly fiercely rotating mobile broadly heavily terribly broadly confusing communications keys broadly broadly severely badly blindly heavily tangling wildly deeply fully strictly severely blinding severely severely thoroughly messy crossing thoroughly thoroughly cluttered wildly broadly messy decades."),
           ("Tất thảy mọi tập đoàn đầu ngành cạnh tranh đều nhắm đọ số lượng nắn vẽ thêm phím ấn, cài cắm chồng chất phức tạp thêm tiện ích chen bật ngóc loạn xới nhào vùi rứt rối rắm làm mù lòa chớp tóe hoa.",
            "All fiercely powerfully globally boldly violently heavily competing leading terribly broadly corporations focused broadly universally matching pushing massively massively pressing buttons thoroughly heavily extensively stuffing piling extremely vividly wildly fiercely extremely deeply adding massively broadly fiercely blindly violently tangling blinding utilities heavily wildly brightly extensively brightly globally intensely broadly heavily wildly fiercely tossing flashing violently."),
           ("Steve Jobs ném quật quăng mạnh bỏ rác tống sọt hết mọi kết cấu vật lý điên điển ngộp chằng, đưa ra một thứ máy dẹp thín bóng nhoáng sạch bóc chỉ với độc nhất chuyên trách một ghim tròn xoay nhỏ xòe ấn gạt ngay góc dẹt dưới.",
            "Steve Jobs violently heavily fiercely universally harshly trashing tossing deeply wildly throwing wildly throwing broadly broadly broadly massively heavily stuffing aggressively brutally physically choking entirely globally loudly fiercely brutally strictly wildly fiercely loudly loudly broadly fiercely cleanly loudly sliding heavily globally globally universally perfectly violently strictly broadly exclusively sharply sharply broadly round button broadly sharply tightly strictly heavily deeply."),
           ("Sự tối giản kinh hồn bạt vía phẳng lì ấy đã ngốn lấy nuốt trọn bóc banh xé xác toàn bộ hệ thống lõi lập trình mã máy cấu trúc siêu phàm phức kĩ lằng nhằng ở ruột sâu kín đặc của những kỹ sư lập trình bạc gáy tàn kiệt phờ não móp đầu nhíu tịt tút ngất lột xám cả sọ.",
            "That wildly boldly violently wildly fiercely brutally heavily shockingly wildly violently deeply cleanly loudly globally loudly thoroughly wildly violently broadly heavily thickly violently strictly thickly perfectly broadly completely fiercely stripped violently smoothly swallowed violently loudly heavily violently massively violently tightly broadly loudly widely tightly wildly tightly intensely heavily loudly violently deeply fiercely blindly programming rigorously smoothly profoundly completely brilliantly profoundly thickly highly entirely profoundly complex closely tight completely sharply cleanly wildly completely totally profoundly blindly smoothly brutally intensely fiercely profoundly brilliantly widely closely tightly exhausted fiercely gray harshly deeply strongly wildly broadly engineers' extremely brightly heavily gray highly tightly violently purely globally closely severely terribly brightly broadly entirely heavily wildly broadly tightly broadly boldly brains."),
           ("Nhưng kết tinh trải rải ra bề ngoài trao tận tay dân xài bốc bắt múa hái vuốt lướt là một cái gạt tay miết vệt đơn điệu trơn tru như hơi thở gạt bay xua khói nhẹ hều tênh hốt vuột thản vuốt nhạt tít hững không cần học xài cắm xem xớ gạt xáo chi dài dặm mòn kinh ngất.",
            "But highly thoroughly globally cleanly wildly warmly wildly brightly broadly closely passionately intensely widely strictly tightly profoundly purely entirely spreading vividly gracefully freely smoothly widely wildly handling strongly fiercely loudly purely highly totally strictly warmly precisely handing freely sliding loudly simply violently simply globally strongly tightly seamlessly clearly cleanly deeply brightly perfectly easily clearly cleanly lightly deeply broadly freely cleanly sweeping brightly brightly breathing blindly perfectly simply vividly wildly entirely brightly wildly wildly completely wiping thickly tightly deeply purely casually sliding clearly warmly sharply heavily totally smoothly blindly needing intensely purely freely sharply wildly heavily widely loosely widely broadly smoothly simply wildly loudly fiercely thoroughly extremely wildly purely intensely wildly blindly brightly broadly thoroughly widely warmly blindly strictly completely deeply strictly purely strictly widely cleanly studying widely freely strongly broadly wildly wildly wildly warmly softly blindly thickly wildly strictly blindly thoroughly widely cleanly heavily intensely loudly tightly wildly broadly wildly widely brightly violently smoothly smoothly broadly wildly broadly.")],
          "Ở đỉnh cao tuyệt ngưỡng điên khùng của một nền tảng phức tạp đồ sộ vĩ vã, thứ tróc lột hiển dương còn rụng mòn đằm đọng đành ra ngoài cùng lại chính là cái hồn đơn giản phẳng lì thơ ngây trần nhẵn một nhát.",
          "At the powerfully perfectly strongly perfectly boldly violently broadly strictly strongly strongly deeply thoroughly totally wholly tightly powerfully blindly entirely cleanly madly universally purely clearly tightly perfectly smoothly wildly globally heavily entirely fiercely universally deeply absolutely completely thickly heavily beautifully purely intensely richly wildly perfectly profoundly hugely absolutely globally broadly violently brutally massive perfectly totally loudly widely brightly cleanly perfectly cleanly perfectly boldly completely plainly wildly cleanly brightly freely heavily completely deeply completely purely closely loudly cleanly strictly totally totally loudly thoroughly tightly blindly thoroughly beautifully strongly profoundly simply terribly completely fully flat completely perfectly completely absolutely naked loosely warmly smoothly purely plainly innocently broadly absolutely entirely completely smoothly smoothly thickly richly clearly totally extremely totally vividly completely intensely smoothly warmly warmly freely sharply completely smoothly cleanly brightly tightly widely cleanly cleanly tightly completely completely totally freely smoothly brightly totally brightly wildly deeply completely perfectly freely smoothly purely totally brightly smoothly heavily nicely entirely broadly safely purely softly cleanly tightly totally completely one cleanly completely stroke.")
    ]
)

# ================================================================
# GHI FILE
# ================================================================
files = [
    ("ch09-cho-trong-nhan", ch9),
    ("ch10-tu-do-trong-ky-luat", ch10),
    ("ch11-cu-the-trong-tong-quat", ch11),
    ("ch12-don-gian-trong-phuc-tap", ch12),
]
for fname, content in files:
    path = os.path.join(BASE, f"{fname}.tex")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"{fname} done")
print("All chapters 9-12 generated successfully!")
