# -*- coding: utf-8 -*-
"""Gen chapters 4-7 for Quyen IV: Triet Ly Nhan Sinh"""
import os, unicodedata, re

BASE = "/Users/admin/Giang-Day-html/truyen-tich-cam-hung-quyen-4/chapters"
os.makedirs(BASE, exist_ok=True)

def story(title, source, first_letter, pairs_body, lesson_vn, lesson_en):
    lines = []
    lines.append(f"\\section{{{title}}}")
    lines.append(f"\\begin{{truyen}}{{{title}}}{{{source}}}")
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

def fix(text):
    text = re.sub(r'(?<!\\)%', r'\\%', text)
    return unicodedata.normalize("NFC", text)

def chapter(chap_vn, chap_en, quote_vn, quote_en, stories):
    lines = [
        "%============================================================",
        f"\\chapter{{Bai Hoc: {chap_vn} ({chap_en})}}",
        "\\begin{center}",
        f"  \\textit{{\\color{{truyengold}}``{quote_en}''}}\\\\[4pt]",
        f"  \\textit{{({quote_vn})}}\\\\[4pt]",
        "  \\small\\color{truyenblue}--- Co Kim Dong Tay ---",
        "\\end{center}",
        "\\ngancach",
        "",
    ]
    for s in stories:
        lines.append(s)
    return fix("\n".join(lines))

# ================================================================
# CHUONG 4: BAN BE TRI KY
# ================================================================
ch4 = chapter(
    "Ban Be Tri Ky --- Nguoi Hieu Ta La Vo Gia", "True Friendship --- A Priceless Understanding",
    "A friend is someone who knows all about you and still loves you.",
    "Ban be la nguoi biet tat ca ve ban va van yeu quy ban.",
    [
    story("Ba Ya Va Tu Ky --- Am Nhac Tri Am", "Truyen Co Trung Hoa --- TK 5 TCN",
          "B",
          [("B a Ya la mot nghe sy dan tranh bac thay thoi Xuan Thu; ong co the bieu hien moi cam xuc qua tieng dan.", "Boya was a master zither player of the Spring and Autumn period; he could express every emotion through his music."),
           ("Nhung chi mot nguoi hieu duoc am nhac cua ong --- Tu Ky, mot tieu phu theo doi ong tu rung ve.", "But only one person truly understood his music --- Ziqi, a woodcutter who followed him back from the forest."),
           ("Khi Ba Ya dan ve nui cao, Tu Ky noi: 'Tiet tau nhu Nui Thai Son vut len troi.' Khi dan nguoc, Tu Ky noi: 'Nuoc cuon cua Truong Giang.'", "When Boya played of high mountains, Ziqi said: 'The rhythm soars like Mount Tai.' When he played rivers, Ziqi said: 'The flow of the Yangtze.'"),
           ("Ba Ya kinh ngac: giua hai nguoi khac biet xa hoi hoan toan, trai tim ngu am nhu mot.", "Boya was astonished: between two people of completely different social standing, their musical hearts beat as one."),
           ("Khi Tu Ky mat, Ba Ya dap vo dan tranh: 'Tri am da mat, con ai nua de ta dan cho?'", "When Ziqi died, Boya smashed his zither: 'My soul-friend is gone; who remains for whom I should play?'")],
          "Tri am --- nguoi hieu trai tim ban --- quy hon van vang; thieu tri am, tat ca tai nang tro nen co don va vo nghia.",
          "A soul-friend --- someone who understands your heart --- is worth more than ten thousand gold; without one, all talent becomes lonely and meaningless."),

    story("Orville Va Wilbur Wright --- Anh Em Cung Uoc Mo", "Wright Brothers --- Hoa Ky 1903",
          "O",
          [("O rville va Wilbur Wright khong co bang dai hoc, khong co tai tro chinh phu, khong co ekip ky su.", "Orville and Wilbur Wright had no university degrees, no government funding, no team of engineers."),
           ("Ho chi co nhau --- va cung mot giac mo dien ro rang ngay la: nguoi co the bay.", "They only had each other --- and one dream that seemed insane at the time: that people could fly."),
           ("Khi Wilbur thu kheo, Orville ghi chep ky luong; khi Orville nan long, Wilbur la nguoi dong vien.", "When Wilbur experimented, Orville took detailed notes; when Orville lost heart, Wilbur was there to encourage."),
           ("Ngay 17/12/1903, may bay mot dong co dau tien cat canh duoc 12 giay tai Kitty Hawk, Bac Carolina.", "On December 17, 1903, the first powered aircraft flew for 12 seconds at Kitty Hawk, North Carolina."),
           ("Ho khong tranh nhau ai la nguoi bay truoc --- ho quay phiem khi nao; nguoi ban thang duoc bay truoc.", "They didn't argue over who would fly first --- they flipped a coin; the winner flew first.")],
          "Ban be that su khong tranh gianh cong trang --- ho chia se no; va chinh su chia se do nhan doi suc manh cho ca hai.",
          "True friends don't compete for credit --- they share it; and that sharing doubles the strength of both."),

    story("Marie Curie Va Nguoi Ban Gay Dung Su Nghiep", "Marie Curie --- Ba Lan/Phap 1891",
          "K",
          [("K hi Marie Sklodowska roi Ba Lan den Paris hoc, ba gan nhu khong co tien --- chi co sach va mot ban la Bronya chi em.", "When Marie Sklodowska left Poland for Paris to study, she had almost no money --- only books and the friend Bronya, her own sister."),
           ("Theo ke hoach cua hai chi em: Bronya hoc y truoc, Marie lam viec gui tien ho tro; xong Bronya lan luot giup Marie.", "By arrangement between the two sisters: Bronya studied medicine first while Marie worked and sent money; then Bronya would help Marie in turn."),
           ("Ke hoach nay keo dai nam nam --- cu bo cuoc thi muon; nhung ca hai giu loi hua.", "The plan stretched five years --- either could have abandoned it anytime; but both kept their promise."),
           ("Marie tro thanh nguoi phu nu dau tien nhan giai Nobel --- va lam dieu do hai lan, voi hai linh vuc khoa hoc khac nhau.", "Marie became the first woman to win a Nobel Prize --- and did so twice, in two different fields of science."),
           ("Bronya luon duoc nhac den trong nhung bai phat bieu cua Marie --- vi khong co su ban be trung thanh ay, khong co Marie Curie.", "Bronya was always mentioned in Marie's speeches --- because without that loyal friendship, there would be no Marie Curie.")],
          "Ban be that su dau tu vao nhau --- du khong biet bao gio se thu hoi duoc --- va chinh su dau tu do tao nen vi dai.",
          "True friends invest in each other --- not knowing when or whether there will be a return --- and that investment creates greatness."),

    story("Luu Binh Va Duong Le --- Hung Co Biet Chia Sot Kho", "Truyen Co Viet Nam --- TK 17",
          "L",
          [("L u Binh va Duong Le la ban than tu thuon, cung nhau an hoc ngheo kho trong nhieu nam.", "Luu Binh and Duong Le were close friends since youth, studying together through years of poverty."),
           ("Duong Le thi dau len lam quan; Luu Binh thi mai that bai, phai song ban ray lam muon.", "Duong Le passed the exam and became an official; Luu Binh kept failing and had to live hand to mouth."),
           ("Luu Binh thi den nha ban xin giup do, nghi rang ban se mo long; nhung Duong Le tiep don lanh nhat, co tinh to ra khinh khi.", "Luu Binh traveled to his friend's home hoping for help, expecting a warm welcome; but Duong Le received him coldly, deliberately showing contempt."),
           ("Bi ton thuong va tuc gian, Luu Binh quyet tam lai sach, cuoi cung thi dau dung truoc mat thien ha.", "Hurt and furious, Luu Binh resolved to study hard, and finally passed the exam with honors before everyone."),
           ("Chi luc nay Duong Le moi tiet lo: ong da gia vo lanh lung vi biet chi su tuyet vong moi khai hoa su quyet tam cua ban.", "Only then did Duong Le reveal: he had pretended coldness knowing that only the pain of rejection could unlock his friend's resolve.")],
          "Co nhung ban be hy sinh su de chiu cua ban than de thuc day ban tien --- chinh ho moi la ban tre long nhat.",
          "Some friends sacrifice their own comfort to push you forward --- they are the truest friends of all."),

    story("Alexander Dai De Va Hephaestion", "Alexander --- Hy Lap TK 4 TCN",
          "A",
          [("A lexander Dai De --- nguoi chinh phuc ba chau luc khi moi 32 tuoi --- co mot nguoi ban thiet than suot cuoc doi la Hephaestion.", "Alexander the Great --- who conquered three continents by age 32 --- had one lifelong friend: Hephaestion."),
           ("Ho lon len cung nhau, hoc cung Aristotle, chien dau sai nhau trong moi tran ma.", "They grew up together, studied under Aristotle, fought side by side in every battle."),
           ("Khi mot phai vien Ba Tu nham lam Ho la Alexander va cui dau, Alexander noi: 'Khong sao --- Ho cung la Alexander.'", "When a Persian envoy mistakenly bowed to Hephaestion thinking him Alexander, Alexander said: 'No matter --- he is also Alexander.'"),
           ("Khi Hephaestion chet dot ngot o Ecbatana, Alexander khoc long rong --- roi ra lenh quoc tang trong ba ngay.", "When Hephaestion died suddenly at Ecbatana, Alexander wept publicly --- then ordered three days of state mourning."),
           ("Nguoi ta noi Alexander sau do chang con vui the nua --- chien thang mat vi sac, boi vi thieu nguoi de chia se no.", "People say Alexander was never the same again --- victories lost their flavor, because there was no one left to share them with.")],
          "Chua du suc manh de co ban be tri ky --- khi co roi, dung de mat --- vi chien thang khong co ai chia se chi la su co don co doi.",
          "Having the strength to find a true friend is one thing --- once found, don't lose them --- for victory shared with no one is only gilded loneliness."),

    story("Abraham Lincoln Va Joshua Speed", "Lincoln --- Hoa Ky 1837",
          "K",
          [("K hi Abraham Lincoln den Springfield hoc luat vao nam 1837, ong gan nhu khong co gi --- khong tien, khong noi o.", "When Abraham Lincoln arrived in Springfield to study law in 1837, he had almost nothing --- no money, no place to stay."),
           ("Joshua Speed, len noi, nghe chuyen, roi don gian noi: 'Toi co mot giuong kep --- neu ong muon, moi o cung.'", "Joshua Speed, the storekeeper, listened, then simply said: 'I have a large double bed --- if you'd like, you're welcome to share it.'"),
           ("Lincoln leo len gac, dat tui sach xuong va noi: '--- Toi o day roi.'", "Lincoln climbed upstairs, set down his bag, and said: 'Well --- I live here now.'"),
           ("Ho o cung bay nam; Speed la nguoi Lincoln viet thu khi bi con troi u am nhat; Speed bay den ben khi co can.", "They lived together for seven years; Speed was the one Lincoln wrote to in his darkest moods; Speed came whenever needed."),
           ("Lincoln ke: 'Speed la nguoi duy nhat toi ke ra ma lo au cua minh va nghe ro loi khuyen tra lai.'", "Lincoln said: 'Speed was the only one to whom I told my anxieties clearly and whose advice I could actually hear.'")],
          "Ban be that su khong bo di luc ban o tay trang --- ho den --- va o lai; chinh dieu do tao nen su khac biet.",
          "True friends don't leave when you're empty-handed --- they arrive --- and stay; that is precisely what makes all the difference."),

    story("Nguyen Du Va Tinh Tri Am Qua He Thong Chuyen", "Nguyen Du --- Viet Nam TK 18-19",
          "N",
          [("N guyen Du song trong thoi ky chuyen tiep day bao dong giua nha Le suy tan va trieu Nguyen moi noi.", "Nguyen Du lived in a tumultuous transitional era between the declining Le dynasty and the rising Nguyen."),
           ("Ong viet Truyen Kieu --- khong chi la tac pham van hoc ma con la tho dan to am thanh cua trai tim co don.", "He wrote the Tale of Kieu --- not just a literary work but a love poem to the sound of a lonely heart."),
           ("'Tran the bach nien cuong ban le, De thuong nhung luong nguai biet nhau' --- cau tho noi len noi khat khao tri am.", "'In a hundred years of this world, how many people do we truly meet who understand us?' --- this line voices the craving for a soul-friend."),
           ("Nguyen Du tin rang su hieu nhau that su qua chuyen --- qua van chuong --- con lau ben hon tat ca cac rang buoc xa hoi.", "Nguyen Du believed that true understanding through story --- through literature --- outlasts all social bonds."),
           ("Truyen Kieu ngay nay duoc doc va kien giai boi hang trieu nguoi --- la minh chung rang tri am co the vuot thoi gian.", "The Tale of Kieu is today read and interpreted by millions --- proof that a soul connection can transcend time.")],
          "Van chuong lon la mot loai ban be --- no hieu ban ma khong can ban giai thich; no o lai khi tat ca nguoi khac di.",
          "Great literature is a kind of friendship --- it understands you without needing explanation; it stays when everyone else has gone."),

    story("David Va Jonatan --- Tinh Ban Vuot Quyen Loi", "Kinh Thanh --- Israel TK 10 TCN",
          "J",
          [("J onatan --- con trai vua Sau-lol --- le ra se la nguoi ke vi --- nhung ong yeu quy David hon ca ngai bau.", "Jonathan --- son of King Saul --- was the crown prince --- but he cherished David more than the throne itself."),
           ("Khi vua cha dat ke hoach giet David, Jonatan tiet lo bi mat va giup David tron thoat.", "When his royal father planned to kill David, Jonathan revealed the secret and helped David escape."),
           ("Ong tra ve chiu de bat dua cua cha --- trong khi biet rang viec lam cua minh co the bi coi la phan boi.", "He returned to endure his father's rage --- knowing his action could be considered treason."),
           ("Ong noi voi David: 'Di di --- van menh may se lon lao; chic ta khong the o ben may. Nhung ta se luon la ban may.'", "He said to David: 'Go --- your destiny will be great; I cannot be by your side. But I will always be your friend.'"),
           ("Tien su ke: 'Tinh ban cua Jonatan voi David vuot qua tinh yeu cua phu nu' --- vi no khong mang dieu kin nao ngoai su hi sinh.", "Scripture records: 'Jonathan's love for David surpassed the love of women' --- because it carried no condition except self-sacrifice.")],
          "Ban be that su khong ganh ghet thanh cong cua ban --- ho vui mung cung ban, dan du no lam mo nhat chan troi cua chinh ho.",
          "True friends don't envy your success --- they rejoice with you, even if it dims their own horizon."),

    story("Goethe Va Schiller --- Doi Ban Biet Nhau Qua Trang Giay", "Goethe & Schiller --- Duc 1794",
          "G",
          [("G oethe va Schiller gap nhau o Weimar nam 1794 --- hai nha tho, hai nha tu tuong, luc dau cung khong qua thich nhau.", "Goethe and Schiller met in Weimar in 1794 --- two poets, two thinkers who at first didn't particularly like each other."),
           ("Nhung qua trao doi thu tu --- hang tram buc thu trong muoi nam --- ho xay dung nen su hieu biet sau sac.", "But through an exchange of letters --- hundreds of letters over ten years --- they built a profound mutual understanding."),
           ("Goethe viet ve khoa hoc va triet hoc; Schiller viet ve my hoc va lich su; ca hai cham chua nhau.", "Goethe wrote about science and philosophy; Schiller wrote about aesthetics and history; each critiqued and enriched the other."),
           ("Nhung tac pham lon nhat cua ca hai --- Faust, Don Carlos, Wilhelm Tell --- duoc viet trong giai doan ho quen biet nhau.", "The greatest works of both --- Faust, Don Carlos, William Tell --- were written during the years they knew each other."),
           ("Khi Schiller mat som o tuoi 45, Goethe noi: 'Toi mat mot nua ban than minh.'", "When Schiller died young at 45, Goethe said: 'I have lost half of myself.'")],
          "Ban tri ky khong chi la nguoi chia vui se buon --- ho la nguoi giup ban tro nen nguoi tot hon qua su phan bien va khich le.",
          "A soul-friend is not just someone who shares joys and sorrows --- they help you become better through critique and encouragement."),

    story("Franklin Roosevelt Va Louis Howe", "FDR & Louis Howe --- Hoa Ky 1910",
          "K",
          [("K hi Franklin Roosevelt moi vao chinh truong, Louis Howe --- phong vien gia, hom hoi --- quyet dinh ong nay se la Tong Thong.", "When Franklin Roosevelt first entered politics, Louis Howe --- an aging, sickly reporter --- decided this man would be President."),
           ("Howe chiu trach nhiem moi viec --- tu viet dien van toi ky hop dong --- moi thu de Roosevelt toa sang.", "Howe took charge of everything --- from writing speeches to signing contracts --- everything so Roosevelt could shine."),
           ("Khi Roosevelt bi liet hai chan vi benh bai liet, Howe la nguoi duy nhat noi: 'Ong van co the thanh Tong Thong.'", "When Roosevelt was paralyzed by polio, Howe was the only one who said: 'You can still be President.'"),
           ("Howe khong bao gio tu nhan minh la nguoi quan trong --- ong tu goi minh la 'nguoi hau can' cua Roosevelt.", "Howe never claimed importance for himself --- he called himself Roosevelt's 'errand boy.'"),
           ("FDR tro thanh Tong Thong duy nhat trong lich su My giu 4 nhiem ky --- Louis Howe la nguoi o sau hau truong giup dieu do.", "FDR became the only President in American history to serve 4 terms --- Louis Howe was the man behind the curtain who made that possible.")],
          "Ban be that su doi khi hi sinh ca su nghiep ca nhan de giup ban thanh cong --- do khong phai su hy sinh ma la tinh yeu.",
          "True friends sometimes sacrifice their own career to help you succeed --- that is not sacrifice, that is love."),
    ])

with open(os.path.join(BASE, "ch04-ban-be-tri-ky.tex"), "w", encoding="utf-8") as f:
    f.write(ch4)
print("ch04 done")

# ================================================================
# CHUONG 5: NHAN QUA
# ================================================================
ch5 = chapter(
    "Nhan Qua --- Nhung Gi Ban Gieo, Ban Se Gat", "Karma --- What You Sow, You Reap",
    "As you sow, so shall you reap.",
    "Ban gieo gi, ban gat nay.",
    [
    story("Nguoi Nong Dan Cuu Fleming Cuu Churchill", "Truyen Thuc Te --- Scotland 1886",
          "M",
          [("M ot ngay o Scotland, mot cau be quy ngheo bi sa xuong dam lay va keu cuu tuyet vong.", "One day in Scotland, a poor farm boy fell into a boggy swamp and cried out desperately for help."),
           ("Mot nong dan nghe tieng keu, bo viec lai cuu cau be len --- khong nghi ngoi, khong doi biet on.", "A farmer heard the cries, dropped his work and pulled the boy out --- without hesitation, without expecting thanks."),
           ("Hom sau, mot quy ong do xe ngua den nha nguoi nong dan nay, noi: 'Con trai toi muon cam on ong.'", "The next day, a well-dressed gentleman drove a carriage to the farmer's home, saying: 'My son wants to thank you.'"),
           ("Ong quy ong de nghi tra on bang cach cho con trai nguoi nong dan di hoc y khoa tai Luong Y --- nguoi nong dan khiem ton nhan loi.", "The gentleman offered to repay by sending the farmer's son to study medicine in London --- the humble farmer accepted."),
           ("Con trai nguoi nong dan tro thanh Alexander Fleming, nguoi phat minh ra Penicillin; va cau be duoc cuu nam xua chinh la Winston Churchill.", "The farmer's son became Alexander Fleming, who discovered Penicillin; and the boy saved long ago was Winston Churchill himself.")],
          "Mot hanh dong tot tu nguyen den roi co the cuu song ca the gioi --- vi chung ta khong biet dieu gi se xay ra tu long nhan ai.",
          "One spontaneous act of kindness can save the whole world --- for we never know what ripples flow from simple human compassion."),

    story("Nguoi Trong Cay Bong Mat Cho Doi Sau", "Triet Ly Co --- Trung Dong co dai",
          "M",
          [("M ot cu ong gia bo co the dang trong cay cho nho.", "An old man was seen planting date palm saplings."),
           ("Nguoi di duong hoi: 'Ong tuoi dau roi ma trong cay cho nho --- ong co the song de an khong?'", "A passerby asked: 'You are so old and planting date palms --- will you live long enough to eat them?'"),
           ("Cu ong tra loi: 'Khi toi sinh ra, da co cho san khi toi an --- nguoi xua trong ma khong biet toi la ai.'", "The old man replied: 'When I was born, there were already dates waiting for me --- someone had planted without knowing me.'"),
           ("'Toi trong hom nay de nhung nguoi sinh ra sau toi se co cho an --- du ho khong biet toi la ai.'", "'I plant today so those born after me will have dates to eat --- though they will never know my name.'"),
           ("Nguoi di duong ngoi xuong, im lang suy nghi --- roi cung cam lay mot cay con trong xuong dat.", "The passerby sat down, fell silent in thought --- then also picked up a small sapling and planted it in the earth.")],
          "Hanh dong dep nhat khong phai la hanh dong de nguoi ta nho on ban --- ma la hanh dong ban lam cho nguoi ban khong bao gio gap.",
          "The most beautiful action is not one done to be remembered --- it is the one you do for someone you will never meet."),

    story("Andrew Carnegie Va Nguon Goc Cua Long Tu Thien", "Andrew Carnegie --- Hoa Ky 1900",
          "A",
          [("A ndrew Carnegie bat dau cuoc doi tu mot co be lam viec trong nha may khi moi 13 tuoi, luong mot do la mot tuan.", "Andrew Carnegie began life as a 13-year-old factory worker earning one dollar a week."),
           ("Mot ong chu nha may tung cho cau be nghe nho thu vien cua ong --- dieu do thay doi cuoc doi Carnegie.", "A factory owner once allowed the young boy to use his private library --- that changed Carnegie's life."),
           ("Khi tro nen giau co, Carnegie nho lai dieu do: 'Ong ay cho toi dieu gi? Kien thuc. Kien thuc lam thay doi tat ca.'", "When Carnegie became wealthy, he remembered: 'What did he give me? Knowledge. Knowledge changes everything.'"),
           ("Carnegie sau do xay dung 2.509 thu vien cong cong tren khap nuoc My --- tu tien cua chinh minh.", "Carnegie then built 2,509 public libraries across America --- from his own funds."),
           ("Ong noi: 'Nguoi chet giau la nguoi chet nho.' Ong tang het tai san truoc khi mat --- va ten ong song mai.", "He said: 'The man who dies rich dies disgraced.' He gave away his fortune before death --- and his name lives forever.")],
          "Nhung gi nguoi khac gieo vao doi ban --- du la mot co hoi nho --- tao ra mot nghi vu tham lang chuyen di luon trao xuong cho doi sau.",
          "What others sow into your life --- even a small opportunity --- creates a silent obligation that flows on to the next generation."),

    story("Khong Tu Va Vu Khi Vo Hinh", "Khong Tu --- Trung Hoa TK 5 TCN",
          "M",
          [("M ot hoc tro hoi Khong Tu: 'Thay co su that rang lam dieu tot se duoc bao dap va lam dieu ac se bi trung phat?'", "A student asked Confucius: 'Is it truly the case that doing good brings reward and doing evil brings punishment?'"),
           ("Khong Tu tra loi: 'It nhan bi at nhan phat hien ngay; nhung nhung van de sau nhieu nam sau moi hien ro.'", "Confucius replied: 'Immediate revenge is visible; but consequences often take years to become clear.'"),
           ("'Con nguoi khong phai la nguoi thi hanh, nhung su that chinh là nhan cach cua ho truoc canh nhan bao.'", "'People are not the enforcers, but the truth is in their character --- as its own judge.'"),
           ("Ong ke chuyen mot nguoi trong boa tren duong di --- nhieu nam sau con chau ong duoc bong mat tren chinh con duong do.", "He told of a man who planted a tree along a road --- years later his descendants enjoyed shade on that very road."),
           ("'Nhan qua khong phai la phan thuong hay hinh phat --- no la su tiep noi tu nhien cua moi hanh dong lam on doi.'", "'Karma is not reward or punishment --- it is the natural continuation of every action rippling through the world.'")],
          "Hanh dong tot khong can chung nhan --- no tac dong nhu song tu tren mat nuoc, lan rong bang nhung cach ban khong nhin thay.",
          "Good actions need no witnesses --- they ripple like waves on water, spreading in ways you cannot see."),

    story("Thien Si Nhat Ban Ci Matsutaro Shoriki", "Matsutaro Shoriki --- Nhat Ban 1924",
          "K",
          [("K hi Nhật Báo Yomiuri Shimbun sap pha san vao nam 1924, Matsutaro Shoriki mua lai to bao nay bang ca tai san cuoi cung cua minh.", "When the Yomiuri Shimbun was about to go bankrupt in 1924, Matsutaro Shoriki bought the paper with his last personal fortune."),
           ("Nhieu nguoi cho rang ong dien khi dau tu vao mot to bao tat nghiep; nhung ong tin rang bao chi can thiet cho xa hoi.", "Many thought him foolish for investing in a failing paper; but he believed journalism was necessary for society."),
           ("Ong giu to bao song --- nhung con lam hon: dua bong chay ve Nhat va phat trien cong nghiep truyen hinh.", "He kept the paper alive --- and did much more: he brought baseball to Japan and developed the television industry."),
           ("Khi nguoi ta hoi sao ong dam mao hiem, ong noi: 'Toi khong mao hiem --- toi dang gieo hat vao mot dat ma chinh toi cung se song tren do.'", "When asked why he dared to risk, he said: 'I wasn't taking a risk --- I was sowing seeds in a land I myself would also live in.'"),
           ("Yomiuri Shimbun tro thanh to bao phat hanh lon nhat the gioi voi hon 14 trieu ban moi ngay.", "Yomiuri Shimbun became the world's highest-circulation newspaper with over 14 million copies daily.")],
          "Khi ban gieo hat vao xa hoi that su ban dang song trong do --- ban khong dau tu, ban dang cham soc chinh ngoi nha cua ban.",
          "When you sow seeds into the society you actually live in --- you're not investing, you're tending your own home."),

    story("Nguoi Tho Ren Va Ke Trom", "Truyen Co La Ma --- TK 2",
          "M",
          [("M ot nguoi tho ren La Ma noi tieng voi su cong bang trong viec giao thuong --- khong bao gio can thi gian khi tre lai.", "A Roman blacksmith was famous for his fair dealings --- never shortchanging time or quality in return."),
           ("Mot ngay, mot ten trom vao xin viec va an cap mot con dao quy cua ong, roi bien mat.", "One day, a thief came asking for work and stole a valuable knife from him, then disappeared."),
           ("Muoi nam sau, ten trom ay --- bay gio da thanh nguoi luong thien --- tim ve tra lai con dao va tien chuoc loi.", "Ten years later, the thief --- now an honest man --- returned to give back the knife and money to make amends."),
           ("Nguoi tho ren hoi: 'Sao nguoi lai quay lai?' Ten trom tra loi: 'Vi suot muoi nam, con dao do nang trai tim toi.'", "The blacksmith asked: 'Why did you come back?' The thief replied: 'Because for ten years, that knife weighed on my heart.'"),
           ("Nguoi tho ren mim cuoi: 'Tinh luong thien trong nguoi khong det mat; no chi ngu yen doi khi.'", "The blacksmith smiled: 'The goodness in a person never dies; it only sleeps for a while.'")],
          "Long luong thien trong moi con nguoi la mot hat giong --- co the bi chon vui nhung khong bao gio chet het; chi can dieu kien dung la no moc len.",
          "The goodness in every person is a seed --- it may be buried but never fully dies; given the right conditions, it will always grow."),

    story("Martin Luther King Va Nhan Qua Bat Bao Luc", "Martin Luther King Jr. --- Hoa Ky 1963",
          "K",
          [("K ing thuong xuyen bi de doa, bi danh bom nha, bi tu, bi dieu tra boi FBI --- nhung ong kien tri con duong bat bao luc.", "King was constantly threatened, had his home bombed, was jailed, monitored by the FBI --- but remained committed to nonviolence."),
           ("Ong tin rang neu phong trao dat quyen binh dang bang bao luc, ho se de lai mot xa hoi chua viet thuong day bao luc.", "He believed that if the movement achieved equality through violence, it would leave a society with fresh wounds full of new violence."),
           ("Ong noi: 'Bao luc tu vu thuong chi tao them bao luc --- ong si nhan va nguoc lai moi dut diem chuoi truyen.'' ", "He said: 'Violence from violence only creates more violence --- patience and love alone can end the chain.'"),
           ("Cuoc hanh trinh tu Washington nam 1963 --- voi 250.000 nguoi dung yeu lang truoc Lincoln Memorial --- thay doi lich su that su.", "The March on Washington in 1963 --- with 250,000 standing quietly before the Lincoln Memorial --- truly changed history."),
           ("Nhan qua cua su kien nhan bat bao luc do: Dao Luat Dan Quyen 1964 va Dao Luat Quyen Bau Cu 1965.", "The karma of that patient nonviolence: the Civil Rights Act of 1964 and the Voting Rights Act of 1965.")],
          "Hanh dong bat bao luc gieo nhan qua lau dai hon that bai vi no thay doi tam tri nguoi con lai, khong chi co the ho.",
          "Nonviolent action sows longer-lasting karma than victory by force because it changes the minds of those who remain, not just their bodies."),

    story("Nguoi Dan Ba Trung Quoc Va Bao Gio Cung Tra On", "Truyen Co Trung Hoa --- TK 2",
          "M",
          [("M ot nguoi dan ong ngheo trong lang lan dau mua ruong, nhung vu mua that bat --- ong sap dan vo tre don vao o.", "A poor village man had his first harvest fail badly --- he was about to take wife and children to live elsewhere."),
           ("Ba hang xom trong lang quyen gop thuc an va tien de giup gia dinh ong qua mua dong.", "Three neighbors in the village pooled food and money to help his family survive the winter."),
           ("Hai muoi nam sau, nguoi dan ong do tro nen giau co --- ong tim ve lan luot den nha ba nguoi hang xom cu.", "Twenty years later, the man became prosperous --- he traveled back and visited each of the three former neighbors."),
           ("Ong tra on ho --- khong phai vi luat le yeu cau, ma vi long biet on that su khong the dung yen trong long.", "He repaid them --- not because any law required it, but because genuine gratitude cannot sit still in the heart."),
           ("Mot trong so ho da mat; ong tim den con cai va tra on the he sau cua nguoi da giup ong.", "One of them had died; he found the children and repaid the next generation of the one who had helped him.")],
          "Long biet on that su khong doi thoi han --- no tim rac cach tra on du qua nhieu the he; do la nhan qua cua long nhan ai.",
          "Genuine gratitude knows no statute of limitations --- it finds ways to repay even across generations; that is the karma of human kindness."),

    story("Hanh Dong Vo Tu Cua Nguoi Xay Gieng", "Truyen Co Trung Dong --- Co dai",
          "M",
          [("M ot nguoi xay gieng o giua sa mac chiu dong thanh tien rieng tuy, khong duoc ai y kien tra.", "A man built a well in the middle of a desert at his own expense, without anyone asking or offering reward."),
           ("Nguoi qua duong hoi: 'Ong co biet ten cua nhung nguoi se uong nuoc o day khong?' Ong luc dau.", "A passerby asked: 'Do you know the names of the people who will drink from this well?' He shook his head."),
           ("'Ong co biet ho se nho on ong khong?' Ong lai luc dau.", "'Do you know if they will be grateful to you?' He shook his head again."),
           ("'Vay tai sao ong lam?' Ong tra loi: 'Vi ai do da xay gieng cho toi uong khi toi can --- va toi khong bao gio biet ten ho.'", "'Then why do you do it?' He replied: 'Because someone built a well for me to drink when I needed it --- and I never knew their name.'"),
           ("'Toi chi lam tiep dieu da lam cho toi --- that vay la du'.", "'I am only continuing what was done for me --- that is enough.'")],
          "Vo tu la hinh thuc cao dep nhat cua nhan qua --- lam dieu tot vi no dung, khong phai vi ban mong doi duoc biet den.",
          "Selflessness is the highest form of karma --- doing good because it is right, not because you hope to be known for it."),

    story("Nguoi Dau Bep Va Cach Tra On Cuoc Song", "Truyen Co Nhat Ban --- TK 12",
          "M",
          [("M ot nguoi dau bep tre trong mot nha hang lon Nhat Ban noi tieng vi nau an tot lam.", "A young chef in a famous large Japanese restaurant was known for cooking unusually well."),
           ("Khi hoi ong bí mat la gi, ong tra loi mot cau bat ngo: 'Toi nau mon an nhu the toi dang tra on thuc pham.'", "Asked about his secret, he gave an unexpected answer: 'I cook as if I am thanking the ingredients.'"),
           ("'Con ga chet de nuoi toi --- toi co trach nhiem che bien no sao cho xung voi su hi sinh do.'", "'The chicken died to nourish me --- I have a responsibility to prepare it in a way worthy of that sacrifice.'"),
           ("'Con ca, hat gao, cu hanh --- moi thu deu den tu dat va bien va mat moi nguoi lao dong.'", "'The fish, the rice, the onion --- everything comes from the earth and sea and the labor of many hands.'"),
           ("Hanh dong nau an vo cung can than cua ong la mot hinh thuc tran trong nhan qua --- noi biet on qua tung mon an.", "His extraordinarily careful cooking was a form of honoring karma --- expressing gratitude through each dish.")],
          "Bat ky viec gi ban lam voi long tran trong --- du la nau an, trong cay hay viet code --- deu la cach tra on cuoc song da trao cho ban.",
          "Whatever you do with deep respect --- whether cooking, planting trees, or writing code --- is a way of giving thanks for the life given to you."),
    ])

with open(os.path.join(BASE, "ch05-nhan-qua.tex"), "w", encoding="utf-8") as f:
    f.write(ch5)
print("ch05 done")

# ================================================================
# CHUONG 6: VUOT QUA NGHICH CANH
# ================================================================
ch6 = chapter(
    "Vuot Qua Nghich Canh --- Su Gap Kho La Giao Vien Tot Nhat", "Overcoming Adversity --- Hardship Is the Greatest Teacher",
    "The gem cannot be polished without friction, nor man perfected without trials.",
    "Da quy khong mai giua kho khan, va con nguoi khong nen duoc ma khong co thu thach.",
    [
    story("Helen Keller --- Dem Toi Khong The Dap Tat Anh Sang", "Helen Keller --- Hoa Ky 1887",
          "H",
          [("H elen Keller bi mat ca thi giac lan thinh giac vao nam 19 thang tuoi vi benh tat.", "Helen Keller lost both her sight and hearing at 19 months of age due to illness."),
           ("Trong nam thu bay cua cuoc doi minh, ba song trong mot the gioi hoan toan toi va im lang --- khong ngon ngu, khong hinh anh.", "For the first six years of her life she lived in a world of complete darkness and silence --- no language, no images."),
           ("Ro roi Anne Sullivan den --- va trong mot buoi chieu tai gieng nuoc, Helen dat tay duoi voi nuoc chay, con Anne viet 'n-u-o-c' len long ban tay kia.", "Then Anne Sullivan arrived --- and one afternoon at the water pump, Helen held one hand under flowing water as Anne spelled 'w-a-t-e-r' into her other palm."),
           ("Helen nho lai: 'Dieu ki dieu da xay ra --- mot cai gi do sat luong sinh dan sang trong toi --- toi biet ray van vat deu co ten.'", "Helen later wrote: 'A miracle happened --- something alive and illuminated woke within me --- I knew that everything had a name.'"),
           ("Ba tot nghiep dai hoc, viet 12 quyen sach, du lich 39 quoc gia va tro thanh bieu tuong cua tinh than con nguoi.", "She graduated from college, wrote 12 books, visited 39 countries, and became a symbol of the human spirit.")],
          "Bot mot giac quan, con nguoi thuong phat trien nhung nang luc ma nguoi binh thuong khong bao gio can phai kham pha.",
          "Deprived of one sense, people often develop capacities that the ordinary person never needs to discover."),

    story("Beethoven Diec Ma Van Sang Tac", "Ludwig van Beethoven --- Duc 1801",
          "K",
          [("K hoan 27 tuoi, Beethoven bat dau nhan ra minh dang dan bi diec --- mot thoa ma chua chac the nao trai qua.", "Around age 27, Beethoven began realizing he was gradually going deaf --- a fate no composer should have to face."),
           ("Ong viet trong thu: 'Mo cua re ti toi den gap roi di --- roi moi nguoi di ca --- toi bi bo lai mot minh.'", "He wrote in a letter: 'People open and close doors near me --- they all went away --- I was left alone.'"),
           ("Ong can nhac viec tu tu --- nhung quyet dinh tiep tuc vi con qua nhieu am nhac van con trong tam tri ong.", "He considered suicide --- but decided to continue because there was still too much music left in his mind."),
           ("Bản giao huong so 9 --- tac pham vi dai nhat cua ong --- duoc sang tac khi ong diec hoan toan.", "Symphony No. 9 --- his greatest work --- was composed when he was completely deaf."),
           ("Khi bieu dien buoi ra mat, ong ngoi tren san khau nhung khong nghe gi ca --- ca khan gia vo tay, ong chi biet khi nguoi ban quay mat ong lai.", "At its premiere he sat on stage but heard nothing --- the audience applauded, he only knew when someone turned him around to face them.")],
          "Nhung gi ban mat khong bao gio bang nhung gi ban van con --- Beethoven mat thinh giac nhung khong mat am nhac.",
          "What you lose is never equal to what you still have --- Beethoven lost his hearing but never lost his music."),

    story("J.K. Rowling --- 12 Lan Bi Tu Choi", "J.K. Rowling --- Anh 1995",
          "N",
          [("N am 1995, J.K. Rowling la nguoi me don than, song nho tro cap xa hoi, nuoi con mot minh sau cuoc hon nhan vo.", "In 1995, J.K. Rowling was a single mother on welfare, raising her daughter alone after a failed marriage."),
           ("Trong hoan canh do, ba viet xong ban thao cuon sach dau tien ve mot cau be phap thuat ten Harry Potter.", "In those circumstances, she finished the first manuscript about a young wizard named Harry Potter."),
           ("Ba gui ban thao den 12 nha xuat ban --- ca 12 tu choi; mot trong so ho con gop y la khong nen viet cho tre em nua.", "She sent the manuscript to 12 publishers --- all 12 rejected it; one even advised her to stop writing for children."),
           ("Cuoi cung, nha xuat ban thu 13 --- Bloomsbury --- chap nhan, tuy nguoi chu bien khong cu ki vong cao vao tu be.", "Finally, the 13th publisher --- Bloomsbury --- accepted it, though the editor did not have high commercial hopes."),
           ("Sach ban duoc hon 500 trieu ban tren toan the gioi, dich ra 80 ngon ngu, va J.K. Rowling tro thanh ti phu.","The books sold over 500 million copies worldwide, translated into 80 languages, and J.K. Rowling became a billionaire.")],
          "Tu choi khong phai la hanh trinh ket thuc --- no la mot trong nhung phan can thiet cua trieu ly thanh cong.",
          "Rejection is not the end of the journey --- it is one of the necessary checkpoints on the road to success."),

    story("Abraham Lincoln --- Dong Thoi Gian Lon Nhat Ve That Bai", "Abraham Lincoln --- Hoa Ky 1860",
          "N",
          [("N am 1816, gia dinh Lincoln bi mat nha. Nam 1818, me ong mat. Nam 1831, ong kinh doanh phat san.", "In 1816 Lincoln's family lost their home. In 1818 his mother died. In 1831 he failed in business."),
           ("Nam 1832, ong that cu chuc nhat dinh vien. Nam 1833, kinh doanh phat san lan hai. Nam 1835, hon the chet.", "In 1832 he was defeated for the state legislature. In 1833 his business failed again. In 1835 his fiancée died."),
           ("Nam 1836, sup do than kinh. Nam 1838, that cu chuc chinh. Nam 1843, that cu vao Quoc Hoi. Nam 1848, mat ghe Quoc Hoi.", "In 1836 he had a nervous breakdown. In 1838 defeated for speaker. In 1843 defeated for Congress. In 1848 lost re-election."),
           ("Nam 1849, bi tu choi bo nhiem. Nam 1854, that cu vao Thu'ong Vien. Nam 1856, that cu Pho Tong Thong.", "In 1849 he was rejected for a land officer position. In 1854 defeated for Senate. In 1856 defeated for Vice President."),
           ("Nam 1858, one lan nua that cu vao Thuong Vien --- nam 1860, ong tro thanh Tong Thong My.", "In 1858 defeated for Senate once more --- in 1860 he became President of the United States.")],
          "That bai khong tich luy thanh nguoi that bai --- chi tich luy thanh kinh nghiem, neu ban khong buong tay.",
          "Failures do not accumulate into a failed person --- they accumulate only into experience, if you do not let go."),

    story("Nick Vujicic --- Khong Tay Khong Chan Nhung Co Hi Vong", "Nick Vujicic --- Australia 1982",
          "N",
          [("N ick Vujicic sinh ra khong co tay va chan --- mot benh tam co roi rac chua biet nguyen nhan.", "Nick Vujicic was born without arms and legs --- a rare disorder of unknown cause."),
           ("O tuoi len 8, ong tu hoi tai sao ong phai song --- o tuoi 10, ong da co ke hoach tu tu.", "At age 8 he asked why he should live --- at age 10 he had planned to end his life."),
           ("Me ong cho ong xem bai bao ve mot nguoi khuyet tat song day du y nghia --- lan dau tien ong thay tu lai minh trong nguoi khac.", "His mother showed him a newspaper article about a disabled person living a full life --- for the first time he saw his reflection in someone else."),
           ("Ong hoc boi, hoc danh golf, hoc gianh bong, hoc lap trinh may tinh --- tat ca chi bang hai ngon chan nho.", "He learned to swim, play golf, catch a ball, use a computer --- all using only his two small toes."),
           ("Ong tro thanh dien gia truyen cam hung duoc moi den hon 50 quoc gia, la chong va la cha cua bon con.", "He became a motivational speaker invited to over 50 countries, a husband and father of four children.")],
          "Dieu gi ban khong co --- neu dat truoc sau mat minh --- co the tro thanh nguon suc manh lon nhat rather than ra nhung gi ban co.",
          "What you lack --- if placed before you as purpose --- can become the greatest source of strength, even greater than what you have."),

    story("Stephen Hawking --- Vat Ly Hoc Tu Xe Lan", "Stephen Hawking --- Anh 1963",
          "O",
          [("O tuoi 21, Stephen Hawking bien dang xu phong than kinh ben --- bac si du doan ong chi song them 2 den 3 nam.", "At age 21, Stephen Hawking was diagnosed with ALS --- doctors predicted he would live only 2 to 3 more years."),
           ("Ong khong chet sau 3 nam --- ong song them 55 nam nua, viet 15 quyen sach va cach mang trong vat ly hoc.", "He did not die after 3 years --- he lived 55 more years, wrote 15 books, and revolutionized physics."),
           ("Ong mat dan kha nang van dong, roi kha nang noi --- nhung khong mat kha nang suy nghi.", "He gradually lost his ability to move, then to speak --- but never lost the ability to think."),
           ("Cuoi cung ong giao tiep chi qua cai dung ma ong co the kiem soat --- mot co bang mat --- voi phan mem doc suy nghi.", "In the end he communicated only through the single muscle he could control --- a cheek muscle --- with software reading his thoughts."),
           ("Ong noi: 'Dieu duy nhat toi su'ng sot hon ca cai mo'i bán' --- su kien ngac nhien la minh van so'ng va lam viec duoc.'", "He said: 'The one thing that surprised me more than my diagnosis --- was the surprise that I could still live and work.'")],
          "Chang co dieu kien nao tu dong cua het cuoc song --- chi la ban tu dong cua no; hay de tat ca cac cua khac con mo.",
          "No condition automatically closes off life --- only you can do that; keep all the other doors open."),

    story("Malala Yousafzai --- Tien Vao Truong Hoc Bat Chap Dan", "Malala Yousafzai --- Pakistan 2012",
          "N",
          [("N am 2012, khi Malala Yousafzai 15 tuoi, mot ten ban vao xe buyt hoc sinh va ban thang vao dau ba.", "In 2012, when Malala Yousafzai was 15, a gunman boarded her school bus and shot her directly in the head."),
           ("Ba song sot --- sau ca thang phau thuat phuc hoi tai Pakistan va Anh.", "She survived --- after months of surgery and rehabilitation in Pakistan and England."),
           ("Khi tinh day trong benh vien, cau hoi dau tien cua ba la: 'Chung ban toi vi gi?' Nguoi cha tra loi: 'Vi di hoc.'", "When she awoke in the hospital, her first question was: 'Why did they shoot me?' Her father answered: 'For going to school.'"),
           ("Ba tra loi: 'Vay thi toi se tiep tuc di hoc --- vi chinh dieu ho so hai moi la thu quan trong nhat.'", "She replied: 'Then I will keep going to school --- because the very thing they fear is what matters most.'"),
           ("Nam 2014, o tuoi 17, ba nhan Giai Nobel Hoa Binh --- nguoi tre nhat trong lich su duoc ghi nhan.", "In 2014, at age 17, she received the Nobel Peace Prize --- the youngest ever to be recognized.")],
          "Doi khi chinh vien dan nhung ke co quyen tru ban la luat chung minh rang viec ban dang lam la thu gi do rat quan trong.",
          "Sometimes the very bullets those in power aim at you are proof that what you are doing truly matters."),

    story("Thomas Edison --- 10.000 Thu Nghiem Truoc Den Dien", "Thomas Edison --- Hoa Ky 1878",
          "T",
          [("T homas Edison khong tot nghiep trung hoc --- thay giao noi ong 'qua do' de hoc.", "Thomas Edison never finished high school --- his teacher said he was 'too stupid' to learn."),
           ("Ong mat viec lam hai lan trong thap nien dau --- nhung moi lan bi sa thai, ong chi nghi: 'Bay gio toi co them thoi gian de thuc nghiem.'", "He lost two jobs in his early years --- but every time he was fired, he thought only: 'Now I have more time to experiment.'"),
           ("O tuoi 97, nguoi ta hoi Edison co khi nao tiếc dieu gi khong --- ong tra loi khong bao gio.", "At 97, someone asked Edison if he ever had regrets --- he said never."),
           ("'Co ai do tinh cho toi la toi da that bai 10.000 lan. Toi khong bao gio 'that bai' 10.000 lan --- toi hoc 10.000 bai.'", "'Someone calculated that I had failed 10,000 times. I never 'failed' 10,000 times --- I learned 10,000 lessons.'"),
           ("Cac phat minh cua Edison --- den dien, may hat, may dien hinh --- tao nen nen tang cua nen van minh hien dai.", "Edison's inventions --- the light bulb, the phonograph, the movie camera --- formed the foundation of modern civilization.")],
          "Chinh nghich canh la thu luyen kien nhan --- va chinh kien nhan la thu thuoc duy nhat chua duoc su tu bo.",
          "Adversity itself is the training of patience --- and patience is the only remedy for the disease of giving up."),

    story("Nguyen Ngoc Ky --- Viet Bang Chan", "Nguyen Ngoc Ky --- Viet Nam 1956",
          "N",
          [("N guyen Ngoc Ky bi liet co tay tu nho --- luc dau tuong rang cuoc doi ong se la mot bi kich.", "Nguyen Ngoc Ky was paralyzed in both arms from childhood --- at first it seemed his life would be a tragedy."),
           ("Nhung ong quyet dinh di hoc --- va hoc bang each dung chan viet chu.", "But he decided to go to school --- and to write using his feet."),
           ("Ban dau chu ong ngoay ngoac khong doc duoc; nhung qua hang gio luyen viet moi ngay, dan dan chu cai hinh thanh ro rang.", "At first his letters were illegible; but through hours of daily practice, gradually clear characters formed."),
           ("Ong khong chi hoc xong pho thong ma con vao dai hoc su pham, tro thanh giao vien nhan dang cua mot the he.", "He not only finished school but attended teacher's college, becoming an icon of a generation."),
           ("Ong noi: 'Toi khong co doi ban tay --- nhung toi co doi ban chan va mot cai dau. Vay la du de song va cong hien.'", "He said: 'I don't have two hands --- but I have two feet and a mind. That is enough to live and contribute.'")],
          "Ban khong can day du de tro nen phi thuong --- ban chi can su dung het nhung gi ban co.",
          "You don't need to be complete to become extraordinary --- you only need to fully use what you have."),

    story("Florence Nightingale Chong Lai He Thong Y Te", "Florence Nightingale --- Anh 1854",
          "T",
          [("T rong chien tranh Crimea, Florence Nightingale den benh vien quan su tai Scutari va bi sock boi su ban thiu va vo to chuc.", "During the Crimean War, Florence Nightingale arrived at the military hospital in Scutari and was shocked by filth and disorganization."),
           ("Cac bac si quan su chong doi ba --- mot phu nu khong the noi chuyen ve y khoa trong quan doi.", "Military doctors opposed her --- a woman could not speak about medicine in the army."),
           ("Ba khong tranh luan bang loi noi --- ba lam viec bang so lieu: thu thap du lieu, ve bieu do, chung minh rang su ban thiu giet chet nguoi.", "She didn't argue with words --- she worked with numbers: collecting data, drawing charts, proving that filth was killing people."),
           ("Voi du lieu trong tay, ba thuyet phuc Quoc Hoi Anh cai to toan bo he thong y te quan su.", "With data in hand she persuaded the British Parliament to reform the entire military medical system."),
           ("Ba khong thua truoc nghich canh --- ba bien nghich canh thanh ti le phan tram va bieu do de thay doi the gioi.", "She did not yield to adversity --- she transformed adversity into percentages and charts to change the world.")],
          "Doi khi nghich canh khong can duoc vuot qua bang y chi --- ma bang tri tue va du lieu duoc su dung dung cach.",
          "Sometimes adversity need not be overcome by willpower --- but by intelligence and data used skillfully."),
    ])

with open(os.path.join(BASE, "ch06-vuot-nghich-canh.tex"), "w", encoding="utf-8") as f:
    f.write(ch6)
print("ch06 done")

# ================================================================
# CHUONG 7: TU BIET MINH
# ================================================================
ch7 = chapter(
    "Tu Biet Minh --- Tri Tue Bat Dau Tu Su Khiem Ton", "Self-Knowledge --- Wisdom Begins with Humility",
    "Knowing yourself is the beginning of all wisdom.",
    "Tu biet minh la khoi dau cua moi tri tue.",
    [
    story("Socrates --- Ta Biet Ta Khong Biet Gi", "Socrates --- Hy Lap TK 5 TCN",
          "N",
          [("N am no, than truyen dat Delphi tuyen bo Socrates la nguoi khon ngoan nhat Athens.", "One year, the Oracle at Delphi proclaimed Socrates to be the wisest man in Athens."),
           ("Socrates boi roi --- ong tu nhan minh la khong co tri tue gi dac biet.", "Socrates was puzzled --- he considered himself to have no special wisdom."),
           ("Ong quyet dinh kiem tra: ong gap tung nguoi bi cho la khon ngoan va dat cau hoi.", "He decided to verify this: he visited each person reputed to be wise and questioned them."),
           ("Ket qua: moi nguoi deu nghĩ ho biet nhung thuc ra ho khong biet; con Socrates --- ong biet ong khong biet.", "The result: each person thought they knew things but actually did not; while Socrates --- he knew that he did not know."),
           ("Do chinh la tri khon cua ong: biet rat ro ranh gioi kien thuc cua minh --- dieu ma nhung nguoi bi goi la khon ngoan khac khong lam duoc.", "That was precisely his wisdom: knowing clearly the limits of his own knowledge --- the very thing others called 'wise' could not do.")],
          "Khoi diem cua moi tri tue la biet ro nhung gi minh khong biet --- dieu nay kho hon nhieu so viec biet nhung gi minh biet.",
          "The starting point of all wisdom is knowing clearly what you do not know --- this is far harder than knowing what you do know."),

    story("Benjamin Franklin Va Nhat Ky Tu Hoan Thien", "Benjamin Franklin --- Hoa Ky 1726",
          "O",
          [("O tuoi 20, Benjamin Franklin lap ra mot he thong tu kiem soat ban than chinh minh --- ong gui 13 duc tinh vao mot cuon so tay.", "At age 20, Benjamin Franklin created a system of self-monitoring --- he placed 13 virtues into a small notebook."),
           ("Moi tuan, ong tap trung chiu nguong luyen mot duc tinh --- va ghi diem do o hen chu buoi toi.", "Each week he focused on practicing one virtue --- and recorded how he had done each evening."),
           ("Ong lam dieu nay trong suot cuoc doi --- cuon so tay bi rach boc, duoc don chep va tiep tuc.", "He did this throughout his life --- the notebook wore out, was recopied, and continued."),
           ("Ong viet: 'Toi khong bao gio dat duoc su hoan hao --- nhung noi luc toi co gang hon, toi biet ro hon minh dang o dau.'", "He wrote: 'I never achieved perfection --- but each time I tried harder, I knew more clearly where I stood.'"),
           ("Chinh he thong nay giup Franklin tro thanh thanh tich: nha van, nha khoa hoc, nha chinh khach, nha ngoai giao.", "This very system helped Franklin achieve his breadth: writer, scientist, statesman, diplomat.")],
          "Tu kiem soat kien tri --- khong phai de tro nen hoan hao --- la cach lam cho ban dan dan tro nen nguoi ban muon tro thanh.",
          "Persistent self-monitoring --- not to become perfect --- is how you gradually become the person you want to be."),

    story("Marcus Aurelius --- Hoang De Tu Van Minh", "Marcus Aurelius --- La Ma TK 2",
          "M",
          [("M arcus Aurelius la mot trong nhung vi hoang de la ma quyen luc nhat --- nhung cuon sach ong de lai la mot cuon nhat ky ca nhan.", "Marcus Aurelius was one of Rome's most powerful emperors --- but the book he left behind is a personal diary."),
           ("Ong viet trong cuon 'Suy Nghi' khong phai de xuat ban ma de chinh ong doc lai --- mot ban ghi nho de tu kiem diem.", "He wrote in 'Meditations' not for publication but for his own rereading --- a memo for self-examination."),
           ("Ong viet: 'Nguoi khac han ta khi ho lam ta kho chiu. Dieu duy nhat ta kiem soat duoc la phan ung cua ta.'", "He wrote: 'Others are beyond my control when they annoy me. The only thing I control is my own reaction.'"),
           ("Ong cung viet: 'Moi buoi sang ta nhac lai: khong co ly do nao de khong han che voi tat ca moi nguoi.'", "He also wrote: 'Every morning I remind myself: there is no reason not to be restrained with everyone.'"),
           ("De che La Ma du' canh chien tranh lien mien, song ben vung them hai the ky phan lan vi tri tue tu bien chiet nay.", "The Roman Empire, despite constant warfare, endured stably two more centuries partly because of this philosophy of continuous self-examination.")],
          "Lanh dao lon nhat trong lich su khong la nguoi khong sai lam --- ma la nguoi con buoc di lien tuc tu kiem diem ban than.",
          "The greatest leaders in history are not those who never err --- but those who continuously walk the path of honest self-examination."),

    story("Confucius --- Moi Ngay Tu Kiem Ba Dieu", "Khong Tu --- Trung Hoa TK 5 TCN",
          "C",
          [("C uoc Thuoc --- mot trong nhung hoc tro cu nhat cua Khong Tu --- co thoi quen moi ngay tu kiem ba dieu.", "Zeng Shen --- one of Confucius's oldest students --- had a daily habit of examining himself on three things."),
           ("Thu nhat: 'Ta co lam het long voi nguoi khac khong?' Thu hai: 'Ta co giu chu tin voi ban be khong?'", "First: 'Have I been wholehearted with others?' Second: 'Have I kept my word to friends?'"),
           ("Thu ba: 'Ta co hoc thuc su va thuc hanh nhung gi thay day khong?'", "Third: 'Have I truly studied and practiced what my teacher taught?'"),
           ("Ong khong bat buoc minh dat cac cau hoi phuc tap hon --- ba cau hoi re nay, lam hang ngay, tao nen mot nghia vu kho chap nhan.", "He didn't impose more complex questions on himself --- these three simple questions, done daily, created an obligation hard to meet."),
           ("Khong Tu khen ong la nguoi tien bo nhanh nhat trong so cac mon de --- khong phai vi ong thong minh hon, ma vi ong tu kiem diem kien nhan hon.", "Confucius praised him as the fastest-progressing student --- not because he was smarter, but because he self-examined more consistently.")],
          "Khong can ket thuc ngay voi nhung cau hoi lon --- chi can ba cau hoi nho nhung lam kien tri moi ngay la du.",
          "You need not end the day with great questions --- just three simple ones, asked persistently every day, is enough."),

    story("Gandhi --- Tu Thuong Luong Voi Ban Than", "Mahatma Gandhi --- An Do TK 20",
          "G",
          [("G andhi co mot nguyen tac rat la thuc te: moi chieu toi ong ngoi lai viet ra nhung gi ong da noi, da lam, da nghi trong ngay.", "Gandhi had a very practical principle: every evening he sat and wrote out what he had said, done, and thought during the day."),
           ("Day khong phai la viec ke su --- do la viec doi chieu: minh da song dung dam me minh chua?", "This was not journaling --- it was comparison: had he lived in accordance with his convictions?"),
           ("Ong viet: 'Suc manh den tu viec lam dung dieu minh biet la dung --- khong phai tu nhung gi nguoi khac mong muon.'", "He wrote: 'Strength comes from doing what you know to be right --- not from what others expect.'"),
           ("Moi cuoc thay doi xa hoi to lon phai bat dau tu mot ca nhan tu thay doi --- va ca nhan do phai tu biet ban than minh truoc.", "Every great social change must begin with one person changing themselves --- and that person must first know themselves honestly."),
           ("'Hay la su thay doi ban muon thay tren doi' --- khong the noi cau noi nay neu ban chua biet ban dang o dau.", "'Be the change you wish to see in the world' --- this cannot be said if you don't first know where you yourself stand.")],
          "Truoc khi thay doi the gioi, ban phai thay doi ban than --- va truoc dieu do, ban phai hieu ban than bang su trung thuc tam su.",
          "Before changing the world you must change yourself --- and before that, you must understand yourself with complete honesty."),

    story("Albert Einstein --- Biet Dieu Minh Khong Gioi", "Albert Einstein --- Duc/My TK 20",
          "E",
          [("E instein la bieu tuong cua thien tai hi dai --- nhung it nguoi biet rang chinh ong thuong noi ve su kem coi cua minh.", "Einstein was the symbol of extraordinary genius --- but few knew that he himself often spoke of his own limitations."),
           ("Ong viet: 'Toi khong co tai nang dac biet --- toi chi la nguoi co su hieu ky dat biet.'", "He wrote: 'I have no special talent --- I am only passionately curious.'"),
           ("Ong bat gioi ve nhiều mat: ngheo o xa hoi, hay quen ten nguoi, khong biet cach lam viec theo nhom.", "He was poor in many ways: socially awkward, forgetful of names, unable to work well in groups."),
           ("Nhung ong biet ro nhung kho khan nay va khong de chung can tra dieu ong gioi nhat: suy nghi doc lap.", "But he knew clearly these difficulties and did not let them obstruct what he did best: independent thinking."),
           ("'Tri tue la kha nang thich ung voi su thay doi' --- va thich ung bat dau tu biet minh can thay doi dieu gi.", "'Intelligence is the ability to adapt to change' --- and adaptation begins with knowing what in yourself needs to change.")],
          "Thien tai thiet gua vi ho biet ro dieu gi minh khong biet --- va tap trung het nang luong vao dieu du minh gioi.",
          "Geniuses thrive because they know clearly what they don't know --- and focus all their energy on what they are already good at."),

    story("Tolstoy --- Nha Van Xet Xu Chinh Minh", "Leo Tolstoy --- Nga TK 19",
          "L",
          [("L eo Tolstoy la tac gia cua Chien Tranh Va Hoa Binh --- mot trong nhung tieu thuyet vi dai nhat nhan loai.", "Leo Tolstoy was the author of War and Peace --- one of humanity's greatest novels."),
           ("Nhung cuoi doi, ong goc bo tat ca su nghiep van chuong va tro thanh mot nha tu tuong den gian.", "But in old age, he abandoned his literary career and became a simple moral philosopher."),
           ("Ong soat xet cuoc doi minh va nhan thay: ong da song xa hoa trong khi nong dan lam ruong chet doi.", "He reviewed his life and saw: he had lived in luxury while the peasants who farmed his land starved."),
           ("Ong bat dau tu thu truuc: hoa cho nong dan, chia dat, tu cam lay cay va lam viec tren dong.", "He began to reform himself: freeing his peasants, dividing the land, picking up a plow and working the fields himself."),
           ("Vo ong that vong, cac con khong hieu --- nhung ong noi: 'Toi khong the viet ve su that ma khong song theo su that do.'", "His wife was distraught, his children didn't understand --- but he said: 'I cannot write about truth without living by that truth.'")],
          "Tu biet minh khong du neu khong di kem voi hanh dong thay doi --- biet ma khong lam thi biet cung la nof co nhua.",
          "Self-knowledge is not enough unless paired with the action to change --- knowledge without action is just another way of standing still."),

    story("King Le Thanh Tong --- Vua Hoc Cung Dan", "Le Thanh Tong --- Viet Nam TK 15",
          "V",
          [("V ua Le Thanh Tong la mot trong nhung vi vua hoc rong, thanh tich nhieu nhat trong lich su Viet Nam.", "King Le Thanh Tong was one of the most learned and accomplished rulers in Vietnamese history."),
           ("Ong chu tri Hoi Tao Dan --- mot to chuc van chuong --- va tu minh viet tho cung voi cac tri thuc.", "He presided over the Tao Dan Club --- a literary society --- and himself composed poetry alongside scholars."),
           ("Ong bieu hien hay hoi cac quan chuc: 'Dan dan dang song ra sao --- cac nguoi co biet khong?'", "He repeatedly asked officials: 'How are the people actually living --- do you know?'"),
           ("Mot lan ong nghe bao cao rang mua mang tot --- nhung roi trac tiep di tham lang va thay nguoc lai.", "Once he received a report that harvests were good --- but he personally visited villages and found the opposite."),
           ("Sau chuyen di do, ong canh bao: 'Biet ve quan ly ma khong biet ve dan la biet nua voi --- nua con lai moi la quan trong.'", "After that trip he warned: 'Knowing governance without knowing the people is knowing only half --- the other half is what truly matters.'")],
          "Tri tue quoc gia bat dau tu vua biet minh con nhieu dieu chua biet --- va tu do di tim hieu chu khong cho bao cao may moc.",
          "National wisdom begins with a ruler who knows they still have much to learn --- and who goes to find out themselves rather than waiting for sanitized reports."),

    story("Confucius --- 70 Tuoi Moi Theo Long Muon", "Khong Tu --- Trung Hoa TK 5 TCN",
          "K",
          [("K hong Tu ke lai hanh trinh phat trien ban than trong suot cuoc doi minh bang ngo, ngay trong chuong dau Luan Ngu.", "Confucius recounted his lifetime of self-development in a few words, right in the opening chapter of the Analects."),
           ("'15 tuoi, ta chi am hoc. 30 tuoi, ta dung vung. 40 tuoi, ta khong nghi ngo.'", "'At 15 I set my heart on learning. At 30 I stood firm. At 40 I had no doubts.'"),
           ("'50 tuoi, ta biet menh troi. 60 tuoi, tai ta thuan theo loi noi. 70 tuoi, ta theo long muon khong pha khuon phep.'", "'At 50 I understood heaven's decree. At 60 my ear was attuned to truth. At 70 I followed my heart without transgressing what was right.'"),
           ("Cau cuoi la tat ca tri hue cua ong --- o tuoi 70, tam hon hanh dong hoa lam mot: khong con phai co gang.", "The last sentence contains all his wisdom --- at 70, mind and action became one: no longer needing effort."),
           ("Moi co the dat duoc dieu nay neu biet minh dang o giai doan nao --- va khong bo cac giai doan can thiet.", "Anyone can reach this if they know what stage they are at --- and do not skip the necessary stages.")],
          "Tu biet minh la hanh trinh ca doi --- bay gio ban o giai doan nao la la cau hoi de bi bo qua nhung quan trong nhat.",
          "Self-knowledge is a lifelong journey --- knowing what stage you are at now is the most easily skipped yet most important question."),

    story("Diogenes --- Nguoi Tim Nguoi Trung Thuc", "Diogenes --- Hy Lap TK 4 TCN",
          "D",
          [("D iogenes co mot thi nghiem noi tieng: ong di giua cho ban ngay voi cay den trong tay.", "Diogenes had a famous experiment: he walked through the marketplace at noon with a lantern in hand."),
           ("Nguoi ta hoi: 'Sao ong cam den ban ngay?' Ong tra loi: 'Ta dang tim mot nguoi trung thuc.'", "People asked: 'Why do you carry a lantern in daytime?' He replied: 'I am looking for an honest person.'"),
           ("Ong khong noi ong dang tim nguoi khon --- ong dang tim nguoi trung thuc ---va y noi rang hai dieu nay hiem khi song cung nhau.", "He wasn't looking for a smart person --- he was looking for an honest one --- implying these two qualities rarely coexist."),
           ("Bai hoc sau nhat cua Diogenes: truoc khi tu biet con nguoi khac ban phai hoi --- 'ta co trung thuc voi chinh minh khong?'", "Diogenes's deepest lesson: before knowing other people you must ask --- 'am I honest with myself?'"),
           ("Vi tu tra loi that su cau hoi nay con kho hon bat ky cuoc thi triet hoc nao.", "Because truly answering this question is harder than any philosophical examination.")],
          "Tu biet minh bat dau tu su trung thuc voi chinh minh --- va day la loai trung thuc kho khan nhat cua tat ca.",
          "Self-knowledge begins with honesty toward yourself --- and this is the hardest honesty of all."),
    ])

with open(os.path.join(BASE, "ch07-tu-biet-minh.tex"), "w", encoding="utf-8") as f:
    f.write(ch7)
print("ch07 done")

print("\nChapters 4-7 generated successfully!")
