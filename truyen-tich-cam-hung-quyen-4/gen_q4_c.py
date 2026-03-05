# -*- coding: utf-8 -*-
"""Gen chapters 8-10 for Quyen IV: Triet Ly Nhan Sinh"""
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
# CHUONG 8: THIEN LUONG
# ================================================================
ch8 = chapter(
    "Thien Luong --- Tam Long Tot Lanh La Tai San Quy Nhat", "Goodness of Heart --- The Most Precious Wealth",
    "No act of kindness, no matter how small, is ever wasted.",
    "Khong co hanh dong tot lanh nao, du nho bao nhieu, la bi lang phi.",
    [
    story("Mother Teresa --- Phuc Vu Nguoi Ngheo La Phuc Vu Chua", "Mother Teresa --- An Do TK 20",
          "M",
          [("M other Teresa den Calcutta nam 1948 va chung kien nhung canh doi nguoi chet doi ngoai pho.", "Mother Teresa arrived in Calcutta in 1948 and witnessed people dying of hunger in the streets."),
           ("Ba bo truong hoc Loreto --- noi ba day trong an toan --- ra ngoai song voi nhung nguoi ngheo kho nhat.", "She left the Loreto school --- where she taught in safety --- to live with the poorest of the poor."),
           ("Ba thuong noi voi cac co: 'Moi lan ban cham vao mot thu ve thuong ta noi: Day la Chua trong y phuc kho so'.", "She often told her sisters: 'Every time you touch the wounds of the poor, say: This is Christ in a distressing disguise.'"),
           ("Nha cua ba o Calcutta --- Nirdhi House --- chep voi nhung nguoi bi tu bo tren pho, cho chet trong pham gia.", "Her home in Calcutta --- Nirmal Hriday --- filled with people abandoned in the streets, dying with dignity."),
           ("Ba nhan Giai Nobel Hoa Binh 1979 --- va to chuc cua ba tiep tuc lam viec o 133 quoc gia cho den ngay nay.", "She received the Nobel Peace Prize in 1979 --- and her organization continues working in 133 countries to this day.")],
          "Thien luong khong can su ton vinh de tiep tuc --- no tu chay trong tam hon nguoi lam viec vi no la dung.",
          "Goodness needs no recognition to continue --- it flows naturally in the heart of one who acts because it is right."),

    story("Albert Schweitzer --- Bac Si Rung Xanh Chau Phi", "Albert Schweitzer --- Chau Phi 1913",
          "A",
          [("A lbert Schweitzer o tuoi 30 la mot nha than hoc noi tieng, nhac si dat ten, tac gia nhieu sach ban chay.", "Albert Schweitzer at 30 was a famous theologian, an acclaimed organist, author of several bestselling books."),
           ("Roi ong doc bai bao keu goi bac si cho vung Chau Phi --- va dat xuong cu quyen sach de di hoc y khoa.", "Then he read an article calling for doctors in Africa --- and set down his books to study medicine."),
           ("O tuoi 38, ong sang Gabon, Chau Phi, xay mot benh xa bang tre nua giua rung xanh.", "At age 38 he went to Gabon, Africa, and built a hospital from bamboo in the middle of the jungle."),
           ("Ong lam bac si ky niem o day nam 52 nam --- vo ket hon cung o lai phuc vu cung ong.", "He served as a tropical doctor there for 52 years --- his wife stayed and served alongside him."),
           ("Ong noi: 'Toi khong biet phan thuong cua cuoc song cua ban la gi --- nhung toi biet rang nen ban phuc vu nguoi khac, ban se hanh phuc.'", "He said: 'I don't know what your destiny will be --- but I know that if you serve others, you will be happy.'")],
          "Su nghiep lon nhat cua mot con nguoi khong phai la nhung gi ho dat duoc cho ban than --- ma la nhung gi ho giup nguoi khac dat duoc.",
          "A person's greatest achievement is not what they attain for themselves --- but what they help others attain."),

    story("Dr. Norman Bethune --- Bac Si Quoc Te O Mat Tran Trung Quoc", "Norman Bethune --- Canada/Trung Hoa 1938",
          "D",
          [("D r. Norman Bethune la bac si phau thuat Nguyen Nhat Chinh tai Canada --- nhung ong to ra suc manh lon nhat khi roi nuoc de lai sau lung.", "Dr. Norman Bethune was a leading surgeon in Canada --- but he showed his greatest strength by leaving it all behind."),
           ("Nam 1938, o tuoi 48, ong di Trung Quoc de phuc vu cac chien binh Cong san chong Nhat.", "In 1938, at age 48, he went to China to serve Communist resistance fighters against Japan."),
           ("Ong to chuc he thong phau thuat luu dong --- mang phong mo truc tiep den mat tran.", "He organized a mobile surgery system --- bringing the operating room directly to the front lines."),
           ("Trong mot ca phau thuat khan cap, ong bi dut tay va nhiem trung --- ong tu choi nghi ngoi cho den khi chiu khong noi nua.", "During an emergency surgery his hand was cut and infected --- he refused to rest until he physically could not continue."),
           ("Ong mat nam 1939; Mao Trach Dong viet bai 'Phuc Vu Nhan Dan' de tuong niem ong --- ten ong duoc biet khap Trung Quoc.", "He died in 1939; Mao Zedong wrote 'Serve the People' in his memory --- his name became known throughout China.")],
          "Thien luong khong biet bien gioi quoc gia --- nguoi tot lanh that su tim den noi ho nhat can thiet, du khoang cach la bao xa.",
          "Goodness knows no national borders --- the truly good find their way to where they are most needed, no matter how far."),

    story("Miep Gies --- Nguoi Giau An No Co Anne Frank", "Miep Gies --- Ha Lan 1942",
          "M",
          [("M iep Gies la mot thu ky binh thuong lam viec cho Otto Frank o Amsterdam trong The chien II.", "Miep Gies was an ordinary secretary working for Otto Frank in Amsterdam during World War II."),
           ("Khi gia dinh Frank --- bao gom Anne Frank --- phai an tron, Miep toi chap nhan mang thuc pham den cho ho moi ngay.", "When the Frank family --- including Anne Frank --- had to go into hiding, Miep quietly agreed to bring them food every day."),
           ("Day la hanh dong toi hinh --- tat ca bi bat co the bi xu ban; nhung Miep khong ngan ngai.", "This was a capital offense --- anyone caught could be shot; but Miep did not hesitate."),
           ("Khi ho bi phat hien, Miep thu thap ban thao nhat ky cua Anne va giu lai --- voi hy vong se tra lai co be sau chien tranh.", "When they were discovered, Miep gathered Anne's diary manuscript and kept it --- hoping to return it to the girl after the war."),
           ("Anne chet trong trai tap trung, nhung nhat ky cua co, duoc Miep giu gin, tro thanh mot trong nhung cuon sach noi tieng nhat the ky XX.", "Anne died in the camps, but her diary, preserved by Miep, became one of the most famous books of the 20th century.")],
          "Hanh dong thien luong khong phai luc nao cung cuu song duoc nguoi ban giu --- nhung no co the cho thay the gioi rang nhan vat cua ho xung dang duoc nho den.",
          "Acts of goodness don't always save the one you protect --- but they can show the world that person's life was worth remembering."),

    story("Nicholas Winton --- Nguoi Cu'u 669 Tre Em Khoi Phat Xit", "Nicholas Winton --- Anh/Czech 1939",
          "I",
          [("I n 1938, khi nguoi co tuoi su ba muoi, Nicholas Winton di nghi He o Prague --- va bat gap nhung gia dinh Do Thai tuyet vong.", "In 1938, when he was just 29, Nicholas Winton went on holiday to Prague --- and encountered desperate Jewish families."),
           ("Thay vi nghi tiep, ong o lai va to chuc chuyen tau dua tre em Do Thai den Anh truoc khi Duc xam luoc.", "Instead of continuing his holiday, he stayed and organized trains to bring Jewish children to England before the German invasion."),
           ("Ong khong duoc phep; ong lam van kien gia, thuyet phuc gia dinh Anh cham soc cac chau be, lo tien ve.", "He had no permission; he forged documents, persuaded English families to care for the children, arranged funding."),
           ("669 tre em duoc cuu; con tau thu 10 --- lon nhat --- bi can lai boi quoc tang Duc xam luoc; nhung tre tren do cu'u khong thoat.", "669 children were saved; the 10th train --- the largest --- was stopped by the German invasion; the children on board did not escape."),
           ("Ong khong noi gi ve viec lam cua minh suot 50 nam --- cho den khi vo ong tim thay cuon so trong gac mia chua day ten tat ca 669 dua tre.", "He said nothing about what he had done for 50 years --- until his wife found a scrapbook in his attic containing the names of all 669 children.")],
          "Nguoi co tam long tot lanh that su khong can ai biet --- va chinh vi vay, khi su that lo lo, no can hon bao gio het.",
          "Those with truly good hearts need no one to know --- and precisely because of that, when the truth finally emerges, it moves us all the more."),

    story("Clara Barton --- Nu Than Ho Nuoc My", "Clara Barton --- Hoa Ky 1861",
          "T",
          [("T rong noi kinh hoang cua Noi chien My, Clara Barton --- mot phu nu khong co dao tao y te chinh quy --- tu minh den chien truong cham soc thuong binh.", "In the horror of the American Civil War, Clara Barton --- a woman with no formal medical training --- independently went to battlefields to care for the wounded."),
           ("Ba phan phoi thuoc men, bang bong, do an cho thuong binh ca hai phia Bac va Nam.", "She distributed medicine, bandages, and food to wounded soldiers from both the North and South."),
           ("Sau chien tranh, ba to chuc tim kiem va xac nhan ten cua 22.000 binh si mat tich --- mot viec chua ai lam.", "After the war, she organized searching for and identifying the names of 22,000 missing soldiers --- work no one had done before."),
           ("Ba sang lap Hoi Ho Thap Do My nam 1881 va phong vai la chu tich dau tien trong 23 nam.", "She founded the American Red Cross in 1881 and served as its first president for 23 years."),
           ("Ong noi: 'Toi khong biet co gi tot hon trong cuoc song nay ngoai viec nhin thay nguoi khac thoat khoi dau kho.'", "She said: 'I know nothing better in this life than seeing others relieved from suffering.'")],
          "Lam dieu tot voi nguoi khong quen biet --- va lam dieu do kien tri suot ca cuoc doi --- la cuoc doi dang song nhat.",
          "Doing good for strangers --- and doing so persistently for an entire lifetime --- is the most worthwhile life of all."),

    story("Raoul Wallenberg --- Nha Ngoai Giao Cuu 100.000 Nguoi Do Thai", "Raoul Wallenberg --- Hungary 1944",
          "R",
          [("R aoul Wallenberg, mot nha ngoai giao Thuy Dien tre tuoi, duoc cua den Budapest nam 1944 de 'bao ve' nguoi Do Thai.", "Raoul Wallenberg, a young Swedish diplomat, was sent to Budapest in 1944 to 'protect' the Jewish population."),
           ("Ong khong co quan doi, khong co phap y --- chi co mot quyen 'ho chieu bao ho' cua chinh ong tu soan --- va long qua cam.", "He had no army, no legal authority --- only a 'protective passport' he had invented himself --- and extraordinary courage."),
           ("Khi tau hoa chua nguoi Do Thai sap roi ga, ong leo len tau, pha cua, tra 'ho chieu' cho cang nhieu nguoi cang tot truoc mat linh SS.", "When a train carrying Jews was about to leave the station, he climbed onto the train, broke through doors, and handed 'passports' to as many as possible in front of SS soldiers."),
           ("Ong noi voi bon linh SS: 'Nhung nguoi nay duoi su bao ho cua nuoc Thuy Dien --- ban khong duoc dong dau den ho.'", "He told the SS soldiers: 'These people are under Swedish protection --- you may not touch them.'"),
           ("Uoc tinh 100.000 nguoi Do Thai duoc cuu --- ong bi Lien Xo bat giu sau Chien tranh va mat tich --- khong ai biet chinh xac ong chet nhu the nao.", "An estimated 100,000 Jews were saved --- he was arrested by the Soviets after the war and disappeared --- no one knows exactly how he died.")],
          "Mot nguoi co tam long thien luong va su qua cam co the lam nhung dieu ma ca mot he thong chinh phu khong the lam.",
          "One person with a good heart and extraordinary courage can do what an entire government system could not."),

    story("Nguyen Trai --- Minh Oan Cho Dan Trong Thu Yen Be", "Nguyen Trai --- Viet Nam TK 15",
          "N",
          [("N guyen Trai --- nha chinh tri, nha van hoa lon cua Viet Nam the ky XV --- sau khi giup dat nuoc doc lap, khong xin phan thuong gi.", "Nguyen Trai --- the great statesman and cultural figure of 15th century Vietnam --- after helping win independence, asked for no reward."),
           ("Ong xin nghí ve o an at Bich Dong --- mot ngoi lang yem tinh giua nui rung Ninh Binh.", "He asked to retire to Bich Dong --- a secluded village in the mountains of Ninh Binh."),
           ("O day ong day hoc cho dan lang, viet thu phap, lam tho --- va viet Quoc Am Thi Tap bang chu Nom.", "There he taught the villagers, practiced calligraphy, wrote poetry --- and composed a poetry collection in Nom script."),
           ("Ong viet: 'Bui tra ngon ngot dat Cong Thanh --- Truyen doc may tran dua cho ai.'", "He wrote: 'The dust of fame sweetens the earth of my homeland --- pass down these lessons to those who come after.'"),
           ("Chinh tam long yeu nuoc va thuong dan cua moi con nguoi binh di --- khong phai vi quyen loi --- la tinh than Nguyen Trai truyen cho hau the.", "It is the love of country and compassion for the common people --- not for personal gain --- that forms the spirit Nguyen Trai passed to posterity.")],
          "Thien luong lon nhat khong can phan thuong, khong can tuong niem --- no chi can duoc thuc hanh trong khi ban con dang song.",
          "The greatest goodness needs no reward, no memorial --- it only needs to be practiced while you are still alive."),

    story("Su Tich An Toan Tre Em --- Eglantyne Jebb", "Eglantyne Jebb --- Anh 1919",
          "E",
          [("E glantyne Jebb la mot phu nu Anh da ra trai truoc toa an vi phat tan to roi co hinh anh tre em Duc dang chet doi sau The chien I.", "Eglantyne Jebb was an English woman who stood trial for distributing leaflets showing starving German children after World War I."),
           ("Dan Anh luc do van con cam thu Duc --- anh huong tre em Duc dang chet khong khien ai co cam xuc.", "The British public was still bitter against Germany --- images of starving German children moved no one."),
           ("Quan toa xu phat ba; chinh vi nhan nhuong cua quan toa da sung coi voi ba, da nop tien bao la cho quy cua ba.", "The judge fined her; moved by her composure the judge himself contributed to her fund."),
           ("Ba sang lap Cuu Te Tre Em --- tien than cua UNICEF ngay nay --- vi tin rang tre em cua moi quoc gia la vo toi.", "She founded Save the Children --- the precursor of today's UNICEF --- believing the children of every nation are innocent."),
           ("Ba soat thao 'Bua Bao Ve Tre Em' --- co so cua Cong Uoc LHQ ve Quyen Tre Em 60 nam sau do.", "She drafted the 'Declaration of the Rights of the Child' --- the foundation of the UN Convention on the Rights of the Child 60 years later.")],
          "Thien luong khong biet thu --- khong phan biet ban hay thu, tre em My hay tre em Duc, nguoi quen hay nguoi la.",
          "Goodness knows no boundaries --- it does not distinguish friend or foe, American or German children, the known or the stranger."),

    story("Phanh Boi Chau --- Long yeu Nuoc La Su Thien Luong Cao Ca", "Phan Boi Chau --- Viet Nam TK 20",
          "P",
          [("P han Boi Chau dat moi su nghiep ca nhan --- hoc vi, danh tieng, cuoc song an lanh --- de di tim duong cuu nuoc.", "Phan Boi Chau sacrificed every personal achievement --- his degree, reputation, comfortable life --- to seek a path to save his country."),
           ("Ong sang Nhat, sang Trung Quoc, song chet song canh trong hang chuc nam voi hong vong Viet Nam doc lap.", "He went to Japan, to China, lived on the edge of life and death for decades in hope of Vietnamese independence."),
           ("Bi Phap bat giam va xu khat --- nhieu dong chi cua ong da bo mang --- nhung ong khong he lung lay xuc cam.", "Arrested and sentenced to death by the French --- many of his comrades perished --- but he never wavered in conviction."),
           ("Ong viet khi trong tu: 'Sinh the noi nay, khong co gi lon hon tinh yeu dan toc --- va khong co gi nho hon ban than minh.'", "He wrote in prison: 'Born in this land, nothing is greater than love of one's people --- and nothing smaller than oneself.'"),
           ("Ong duoc tra tu, bi quan che trong Hue --- nhung tinh than dan toc ong nhen len tiep tuc lan ta trong toan quoc.", "He was released and put under house arrest in Hue --- but the national spirit he ignited continued spreading throughout the country.")],
          "Long yeu nuoc thien luong --- khong vi quyen loi ca nhan --- la dang cap cao nhat cua thien luong con nguoi co the dat den.",
          "Patriotic goodness --- not for personal gain --- is the highest level of human goodness a person can reach."),
    ])

with open(os.path.join(BASE, "ch08-thien-luong.tex"), "w", encoding="utf-8") as f:
    f.write(ch8)
print("ch08 done")

# ================================================================
# CHUONG 9: TRI TUE CO NHAN
# ================================================================
ch9 = chapter(
    "Tri Tue Co Nhan --- Kho Tang Muon Doi Khong Can", "Ancient Wisdom --- Timeless Treasure",
    "The more things change, the more they stay the same.",
    "Cang nhieu thu thay doi, chung cang van nhu cu.",
    [
    story("Ton Tu --- Biet Nguoi Biet Ta Tram Tran Tram Thang", "Ton Tu --- Trung Hoa TK 5 TCN",
          "T",
          [("T on Tu viet 'Binh Phap Ton Tu' khoang 500 nam TCN --- cuon sach ngan nhat ve chien thuat va von vat sac nhon nhat con ton tai.", "Sun Tzu wrote 'The Art of War' around 500 BC --- the shortest yet sharpest book on strategy still in existence."),
           ("Cau noi noi tieng nhat: 'Biet nguoi biet ta, tram tran tram thang; khong biet nguoi biet ta, mot thang mot bai; khong biet nguoi khong biet ta, tran tran bai.'", "Its most famous line: 'Know yourself and know your enemy, and you will win a hundred battles; know yourself but not the enemy, one win one loss; know neither, lose every time.'"),
           ("Cuon sach khong chi la binh phap --- la triet hoc ve su hieu biet, su kien nhan, va cach chien thang ma khong can danh nhau.", "The book is not just tactics --- it is a philosophy of understanding, patience, and winning without fighting."),
           ("Chien luoc 'Muon nuoc dat ca' --- tao ra cho doi phuong cuoc gia ma khong tro mat mot binh sy --- la dinh cao.", "The strategy of 'Disturbing the Water to Catch Fish' --- creating situations to win without losing a single soldier --- is the pinnacle."),
           ("Den ngay nay, cuon sach duoc day trong cac Truong Kinh Doanh lon nhat the gioi --- vi khai niem khong bao gio loi thoi.", "Today the book is taught in the world's top Business Schools --- because its concepts never become outdated.")],
          "Tri tue co nhan khong bi lai thoi boi vi no de cap den ban chat con nguoi --- ban chat nay khong thay doi theo cong nghe hay thoi dai.",
          "Ancient wisdom never becomes outdated because it addresses human nature --- and human nature does not change with technology or era."),

    story("Lao Tu --- Nuoc Mem Thang Da Cung", "Lao Tu --- Trung Hoa TK 6 TCN",
          "L",
          [("L ao Tu la nguoi sang lap Tu Tuong Dao Giao --- nguoi ta noi ong viet 'Dao De Kinh' trong mot buoi toi khi sap roi Trung Quoc.", "Laotzi was the founder of Taoist thought --- legend says he wrote the 'Tao Te Ching' in one night as he was leaving China."),
           ("Mot cau noi cua ong da lam say long bao trien hoc gia: 'Thien ha chi nhuoc nho hu nuoc --- ma nuoc chuyen thang da cung.'", "One saying of his has captivated generations of philosophers: 'Nothing in the world is as soft and yielding as water --- yet nothing is better at overcoming the hard and strong.'"),
           ("Nguoi cuong cuong se gap canh cuong cuong --- nguoi nhu hoa thich ung voi moi hoan canh nhu nuoc.", "The stubbornly rigid will meet rigid resistance --- those who flow adapt to every circumstance like water."),
           ("Triet hoc 'Vo Vi' --- hanh dong khong cang nhac, khong phai la khong lam gi --- la tieu bieu nhat cua Lao Tu.", "The philosophy of 'Wu Wei' --- acting without rigidity, not meaning doing nothing --- is most representative of Laotzi."),
           ("Dao De Kinh chi co 5.000 chu --- nhung da duoc dich sang hon 250 ngon ngu --- chi sau Kinh Thanh.", "The Tao Te Ching has only 5,000 characters --- yet has been translated into over 250 languages --- second only to the Bible.")],
          "Suc manh that su khong phai la cung nhac ma la uyen chuyen --- nuoc khong bao gio thua tran, vi no luon tim duoc con duong lach qua.",
          "True strength is not rigidity but flexibility --- water never loses, because it always finds its way through."),

    story("Khong Tu --- Truoc Het Hay Lam Giang", "Khong Tu --- Trung Hoa TK 5 TCN",
          "T",
          [("T u Cong hoi Khong Tu: 'Neu phai bo bao mot trong ba: luong thuc, quan doi, hay long tin cua dan --- thu nao bo truoc?'", "Zigong asked Confucius: 'If one must give up one of three: food, army, or the people's trust --- which goes first?'"),
           ("Khong Tu tra loi: 'Bo quan doi.' Tu Cong hoi: 'Neu van phai bo them?' Thay noi: 'Bo luong thuc.'", "Confucius replied: 'Give up the army.' Zigong asked: 'If you must give up another?' The master said: 'Give up the food.'"),
           ("'Nguoi ta vit tu xua den nay deu chet --- nhung neu khong co long tin cua dan, quoc gia khong dung vung duoc mot ngay nao.'", "'People have always died since antiquity --- but without the trust of the people, a nation cannot stand for even one day.'"),
           ("Cau noi nay --- de len tren ca luong thuc lan an ninh --- la hoc thuyet tri quoc tam tho lon nhat truoc khi Kinh Dich theo cach trin.", "This saying --- placing trust above both food and security --- is the grandest governance philosophy before the Book of Changes in that interpretation."),
           ("Quoc gia nao mat long tin cua dan --- van de quan su hay kinh te gi cung khong cuu duoc.", "Any nation that loses the trust of its people --- no military or economic measure can save it.")],
          "Long tin cua dan la nen tang cua moi chinh quyen --- mat long tin thi tuong vua cung sup do; giu duoc long tin thi dat nuoc ben vung.",
          "The trust of the people is every government's foundation --- lose that trust and the tallest tower falls; keep it and the nation endures."),

    story("Trang Tu --- Chuyen Bay Cua Con Buo'm", "Trang Tu --- Trung Hoa TK 4 TCN",
          "M",
          [("M ot hom, Trang Tu mo thay ong ta la mot con buom dang bay luon tu do giua vuon hoa.", "One day, Zhuangzi dreamed he was a butterfly flying freely among garden flowers."),
           ("Roi ong tinh day --- va cau hoi dau tien ong dat ra la: 'Bay gio ta la nguoi nam mo la buom, hay la buom dang mo la nguoi?'", "Then he awoke --- and the first question he asked was: 'Am I now a person who dreamed of being a butterfly, or a butterfly dreaming of being a person?'"),
           ("Dieu Trang Tu muon noi la: thuc tai ma ta tin la thuc chua chac la toan bo thuc tai.", "What Zhuangzi was saying is: the reality we believe is real may not be the whole of reality."),
           ("Su nhan co va mo nho nay buoc nguoi dat lai cau hoi --- cai gi la that su quan trong, cai gi chi la nhung nhan mac toi nghia?", "This gentle blurring of wake and dream forces us to ask --- what is truly important, and what is merely label and meaning we impose?"),
           ("Trang Tu khong day chung ta an tam --- ong day chung ta nghi khac di, nhin rong hon, mot cach vui ve va khong co tinh than bi lich.", "Zhuangzi did not teach us to be complacent --- he taught us to think differently, see more broadly, with joy and without tragedy.")],
          "Tri tue khong phai luc nao cung di kem voi su nghiem tuc --- doi khi no an trong mot bai kho va buoi cuoi biet on su thay doi.",
          "Wisdom is not always accompanied by solemnity --- sometimes it hides in a poem and in grateful laughter at the possibility of change."),

    story("Manh Tu --- Tinh Nguoi Von Thien", "Manh Tu --- Trung Hoa TK 4 TCN",
          "M",
          [("M ach Mencius day rang con nguoi khi sinh ra da co bon mam mong thien luong: nhan, nghia, le, tri.", "Mencius taught that humans at birth already possess four moral sprouts: humanity, righteousness, propriety, and wisdom."),
           ("Ong dung vi du: khi thay mot dua tre sap roi xuong gieng, bat ky ai cung cam thay bong kinh hai muon chay lai cuu.", "He gave an example: seeing a child about to fall into a well, any person feels sudden alarm and wants to rush to help."),
           ("Cam giac nay khong phai vi so bi che bai hay muon duoc khen --- do la phan ung tu nhien cua tam nguoi.", "This feeling is not from fear of blame or desire for praise --- it is the natural response of the human heart."),
           ("Ong noi: 'Neu khong co tam biec khac kho --- khong phai nguoi. Neu khong co tam xau ho --- khong phai nguoi.'", "He said: 'Without a heart of shame and discomfort --- not human. Without a heart of compassion --- not human.'"),
           ("Mot xa hoi tot phat sinh khi moi ca nhan duoc nuoi duong bon mam mong thien luong nay, khong phai khi bi nen.", "A good society arises when every individual nurtures these four moral sprouts, not when they are suppressed.")],
          "Con nguoi ban chat khong xau --- chi la hoan canh da khong nuoi duong dieu tot trong ho; hay tao ra hoan canh tot hon.",
          "Human nature is not evil --- only circumstances have failed to nurture the good within; create better circumstances instead."),

    story("Han Phi Tu --- Phap Tri La Nen Tang Cua Nuoc Manh", "Han Phi Tu --- Trung Hoa TK 3 TCN",
          "H",
          [("H an Phi Tu la nha triet hoc phap gia noi tieng trong lich su Trung Hoa co dai --- nguoi bat ke tinh tot hay xau cua con nguoi.", "Han Fei was the famous Legalist philosopher in ancient Chinese history --- who discarded assumptions about human nature's goodness or evil."),
           ("Ong lap luan: 'Luat phap tot khong can nguoi tot de thuc thi ---no hoat dong vi ai cung phai theo.'", "He argued: 'Good laws do not need good people to enforce them --- they work because everyone must follow them.'"),
           ("Ong phe phan truong phai duc hanh cua Khong Tu: 'Dat nuoc khong the duoc cai tri chi bang duc hanh --- can luat le ro rang va hinh phat cong bang.'", "He criticized Confucius's virtue school: 'A nation cannot be governed by virtue alone --- it needs clear rules and impartial punishment.'"),
           ("Tuong Phan trinh vua Tan --- nguoi lap thong nhat Trung Hoa --- dua tren hoc thuyet Han Phi Tu lam nen tang.", "Chief Minister of Qin --- who unified China --- built on Han Fei's political theory as a foundation."),
           ("Cau noi cua Han Phi Tu van con mang tinh thoi su: 'Co o luat phap roi moi noi ve duc hanh --- khong phai nguoc lai.'", "Han Fei's words remain relevant: 'First establish the rule of law, then speak of virtue --- not the other way around.'")],
          "Tri tue co nhan khong diem nhau --- Khong Tu va Han Phi deu dung --- ho chi nhin tu cac goc do khac nhau cua cung mot su that.",
          "Ancient wisdom does not contradict itself --- Confucius and Han Fei are both right --- they simply look from different angles at the same truth."),

    story("Aristotle --- Hanh Dong La Tap Quen, Khong Phai Ta Tu Nhien", "Aristotle --- Hy Lap TK 4 TCN",
          "C",
          [("C hiu anh huong lon tu Plato, Aristotle da phat trien mot nhin nhan rat thuc te ve dao duc.", "Deeply influenced by Plato, Aristotle developed a very practical view of ethics."),
           ("Ong noi: 'Chua chac ai sinh ra da tot --- dieu tot la tap quen; chua chac ai sinh ra da xau --- dieu xau cung la tap quen.'", "He said: 'No one is born good --- goodness is a habit; no one is born bad --- badness is also a habit.'"),
           ("Ong dat ra khai niem 'Arete' -- su xuat sac trong cuoc song -- dat duoc bang cach ren luyen kien tri.", "He put forward the concept of 'Arete' --- excellence in living --- achieved through persistent practice."),
           ("Nho biet hanh dong dung lan mot tien den dan cuoc song tot; nhu tuong dat nuoc di nuoc lai.", "Knowing how to act rightly leads step by step to a good life; like a swimmer going back and forth in water."),
           ("'Cuoc song tot la ket qua cua viec lam viec tot --- va viec tot la ket qua cua thoi quen tot.' Day la triet ly thuc te nhat nhan loai tung co.", "'The good life is the result of good work --- and good work is the result of good habit.' This is the most practical philosophy humanity has ever had.")],
          "Tinh cach khong tao nen hanh dong --- hanh dong tao nen tinh cach. Hay chon thoi quen ngay hom nay vi chung se chon nen ban ngay mai.",
          "Character does not create actions --- actions create character. Choose your habits today because they will choose who you are tomorrow."),

    story("Ibn Sina --- Bac Si Va Triet Gia Cu'u Nhiet", "Ibn Sina --- Ba Tu TK 10",
          "I",
          [("I bn Sina --- duoc Chau Au goi la Avicenna --- la bac si, triet gia, nha tho lon nhat Hoi Giao co dai.", "Ibn Sina --- called Avicenna by Europe --- was the greatest physician, philosopher, and poet of classical Islam."),
           ("Cuon sach 'Qui Phap Y Khoa' cua ong la giao trinh chuan cho cac truong y o chau Au suot 600 nam.", "His 'Canon of Medicine' was the standard textbook for European medical schools for 600 years."),
           ("Ong phat hien ra rang benh truyen qua khong khi va nuoc --- va khuyen dat bo y phuc bi nhiem benh.", "He discovered that disease spreads through air and water --- and advised burning infected clothing."),
           ("Ong viet vao dem truoc khi mat: 'Tam linh toi da nhac lua cho the xac minh sang --- bay gio no da mo ra canh cua; no da tu di.'", "He wrote on the night before he died: 'My soul has lit the lamp of my body --- now it has opened the gate; it has gone its way.'"),
           ("Kien thuc y hoc cua ong vuot truoc thoi dai cua ong nhieu the ky --- vi ong dat cau hoi bang tri tue, khong bang tin dieu.", "His medical knowledge was centuries ahead of his time --- because he asked questions with reason, not faith alone.")],
          "Tri tue co nhan song qua hang the ky boi no dat cau hoi bang ly luong khoa hoc --- va su kien nhan de tim cau tra loi tan cung.",
          "Ancient wisdom survives through centuries because it asks questions with reasoned inquiry --- and the patience to pursue answers to their end."),

    story("Plato --- Hang Dong Va Su That", "Plato --- Hy Lap TK 4 TCN",
          "P",
          [("P lato ke cau chuyen ve nhung nguoi bi xich trong mot hang dong, chi nhin duoc cai bong tren vach --- ho tin do la toan bo the gioi.", "Plato told of people chained in a cave, able to see only shadows on the wall --- they believed this was the whole world."),
           ("Mot nguoi thoat ra --- thay mat troi, thay cay co, thay the gioi that --- roi quay vao noi voi nhung nguoi kia.", "One person escapes --- sees the sun, trees, the real world --- then returns to tell the others."),
           ("Ho khong tin --- ho chi thay bong; va hoat nghie an --- ho giet nguoi do.", "They don't believe --- they only trust shadows; and out of fear they kill the escaped one."),
           ("Plato muon noi: tri tue that su luon bi nguoi so hang dong chong lai, khi no dat cau hoi ve thuc tai.", "Plato's message: genuine wisdom is always resisted by those comfortable in the cave, when it questions reality."),
           ("Cuon 'Cong Hoa' cua ong --- viet 2500 nam truoc --- van la nen tang cua triet hoc chinh tri va giao duc hien dai.", "His 'Republic' --- written 2,500 years ago --- remains the foundation of modern political philosophy and education.")],
          "Tri tue that su doi khi bi xa hoi chong lai --- vi no dat cau hoi lam lo rung chuyen nhung su thoai mai cua nen khong bi xao tron.",
          "Genuine wisdom is sometimes resisted by society --- because it asks questions that disturb the comfort of those who prefer not to be disturbed."),

    story("Nguyen Binh Khiem --- Tinh Toan Cu'a Thanh Nhan", "Nguyen Binh Khiem --- Viet Nam TK 16",
          "N",
          [("N guyen Binh Khiem --- Trang Trinh --- la nha tri thuc lon nhat Viet Nam the ky XVI, co tai tien tri huyen bi.", "Nguyen Binh Khiem --- Trang Trinh --- was the greatest Vietnamese intellectual of the 16th century, known for mysterious prophetic abilities."),
           ("Ong tu ngai khi triều chinh nhieu dang, ong lui ve que song doi gian tien nong dan, viet tho Nam.", "Wearied by factional court politics, he withdrew to his home village to live the simple life of a farmer, composing Nom poetry."),
           ("Cau tho ong de lai lam chay oc nhieu the he: 'Ta dai nguoi biet ta la ai --- khong cho ai biet ta la ai cung duoc.'", "One verse he left behind has given generations pause: 'I wait for those who know who I am --- those who don't know, that is also fine.'"),
           ("Ong goi ra cai goi la 'tri en tri an' --- biet dung luc nao ra, luc nao lui --- triet ly cua con nuoc len xuong.", "He articulated what he called 'knowing times and seasons' --- knowing when to advance, when to withdraw --- a philosophy of tides."),
           ("Den ngay nay, cac cau sau luu truyen duoc nhan la bat ly tri cua ong --- khon nguoan ai cung biet nhung khong phai ai cung song theo.", "Even today, his sayings are recognized as his unrivaled wisdom --- wisdom everyone acknowledges but few actually live by.")],
          "Tri tue co nhan hay nhat he sinh tu nhung nguoi biet khi nao nen tien, khi nao nen lui --- va du can dam de chon chac chan.",
          "The finest ancient wisdom is born in those who know when to advance and when to withdraw --- and have the courage to choose deliberately."),
    ])

with open(os.path.join(BASE, "ch09-tri-tue-co-nhan.tex"), "w", encoding="utf-8") as f:
    f.write(ch9)
print("ch09 done")

# ================================================================
# CHUONG 10: KIEN TAO CUOC DOI
# ================================================================
ch10 = chapter(
    "Kien Tao Cuoc Doi --- Ban La Kien Truc Su Cua Chinh Minh", "Building One's Life --- You Are Your Own Architect",
    "Your life is your message to the world. Make sure it's inspiring.",
    "Cuoc doi ban la thong diep ban gui toi the gioi. Hay dam bao no truyen cam hung.",
    [
    story("Steve Jobs --- Stay Hungry, Stay Foolish", "Steve Jobs --- Hoa Ky 2005",
          "N",
          [("N am 2005, Steve Jobs dung truoc sinh vien tot nghiep Stanford va ke ba cau chuyen ve cuoc doi minh.", "In 2005, Steve Jobs stood before Stanford graduates and told three stories from his life."),
           ("Thu nhat: bi Apple sa thai la dieu tot nhat tung xay ra voi ong --- vi ta tu do de sang tao ra Pixar va Mac moi.", "First: being fired from Apple was the best thing that ever happened to him --- giving him freedom to create Pixar and the new Mac."),
           ("Thu hai: chan doan ung thu mang lai tinh giac --- 'thoi gian la huu han, dung song theo cuoc doi cua nguoi khac'.", "Second: his cancer diagnosis brought awakening --- 'time is finite, don't live by others' expectations.'"),
           ("Thu ba: 'Hay khat vong, hay ngo ngan' --- Stay hungry, stay foolish --- la ten goi cua long dam me chua the giam.", "Third: 'Stay hungry, stay foolish' --- the name for a passion that cannot be diminished."),
           ("Apple truoc o sau thoi ky ong quay lai la cong ty gia tri nhat the gioi --- vi Jobs da xay dung no bang chien luoc dua tren tri tue va dam me.", "Apple before and after his return became the world's most valuable company --- because Jobs built it on a strategy grounded in vision and passion.")],
          "Nhung khuc quanh dau don trong cuoc doi khong chi la mat mat --- chung thuong la cua mo dan den noi ban can phai den.",
          "Painful turning points in life are not only losses --- they are often doors opening to where you were always meant to go."),

    story("Walt Disney --- Bi Sa Thai Roi Tro Thanh Bieu Tuong", "Walt Disney --- Hoa Ky 1919",
          "N",
          [("N am 1919, Walter Disney bi editor to bao sa thai vi 'thieu suc sang tao va khong co y tuong hay'.", "In 1919, Walter Disney was fired by a newspaper editor for 'lacking creativity and having no good ideas.'"),
           ("Ong ra di lam hoat hinh --- bi phat san lan thu nhat khi mua quyen hop dong roi mat tro lai truoc khi hoan thanh.", "He went on to make cartoons --- went bankrupt a first time when the studio buying his contract collapsed before completion."),
           ("Sau do ong tao ra Oswald the Rabbit --- roi mat ban quyen vi khong biet luat kinh doanh.", "Then he created Oswald the Rabbit --- then lost the copyright because he didn't understand business law."),
           ("Tren chuyen tau ve la, ong phac thao mot nhan vat moi --- chuot Mickey --- tren day giay an. Vo ong la ban dau tien xem.", "On the train home he sketched a new character --- Mickey Mouse --- on scrap paper. His wife was the first to see it."),
           ("Disney ngay nay la de che giai tri gia tri 200 ty do la --- xay tren nen tang mot nhan vat phac thao tren chuyen tau sau that bai.", "Disney today is an entertainment empire worth 200 billion dollars --- built on the foundation of a character sketched on a train after failure.")],
          "Biet sa thai --- du dau khi ban dang thua --- nhieu khi la bat dau cua con duong dung, chi la muon hon ban du dinh.",
          "Being fired --- painful at the moment --- is often the start of the right path, only later than you planned."),

    story("Oprah Winfrey --- Tu Ngheo Kho Den Bieu Tuong TG", "Oprah Winfrey --- Hoa Ky 1954",
          "O",
          [("O prah Winfrey sinh ra trong ngheo tung, lon len bi bao hanh, bi te nan o tuoi tho --- nhung ba con lai va bac len.", "Oprah Winfrey was born in poverty, grew up with abuse, experienced childhood trauma --- but she endured and rose."),
           ("O tuoi 19, ba duoc nhan lam phat thanh vien --- roi bi sa thai khi lam truyen hinh vi chi 'qua xuc cam voi cac chu de'.", "At 19 she was hired as a news anchor --- then fired from television for being 'too emotionally involved with her subjects.'"),
           ("'Qua xuc cam' chinh xac tro thanh suc manh lon nhat cua ba khi ba tao ra chuong trinh talkshow Oprah.", "'Too emotional' became precisely her greatest strength when she created The Oprah Winfrey Show."),
           ("Chuong trinh len song 25 nam --- 1986 den 2011 --- tro thanh chuong trinh truyen hinh ban ngay xuat sac nhat lich su My.", "The show aired 25 years --- 1986 to 2011 --- becoming the highest-rated daytime TV show in American history."),
           ("Ba noi: 'Dieu lon nhat trong cuoc doi la dat hon ban la chinh ban --- la ke chuyen den cua cuoc doi chinh minh.'", "She said: 'The biggest adventure you can take is to live the life of your dreams --- you are the storyteller of your own life.'")],
          "Diem yeu ban bi che bai nhat doi khi chinh la the manh ban can khai thac nhat --- chi can dat no dung hoan canh.",
          "The weakness you are most criticized for is often the strength you most need to develop --- just put it in the right context."),

    story("Thomas Edison --- Kho Tang Cua Su Kien Nhan", "Thomas Edison --- Hoa Ky 1847",
          "T",
          [("T homas Edison khong chi sang tac den dien --- ong sang tac ra phong thi nghiem hien dai.", "Thomas Edison didn't just invent the light bulb --- he invented the modern research laboratory."),
           ("Ong xay dung Menlo Park --- 'xuong chui sang tao' dau tien tren the gioi, voi nhom nha khoa hoc lam viec cung nhau theo ke hoach.", "He built Menlo Park --- the world's first 'invention factory,' with a team of scientists working together with a plan."),
           ("Ong noi: 'Thien tai la 1 phan tram cam hung va 99 phan tram mo hoi.'", "He said: 'Genius is one percent inspiration and ninety-nine percent perspiration.'"),
           ("Nhung phat minh cua ong lam thay doi cuoc song hang ngay: den dien, may phat am, may chieu phim, tram dien luc.", "His inventions transformed daily life: the light bulb, phonograph, movie projector, power station."),
           ("Den cuoi doi, ong co 1.093 bang sang che --- ky luc the gioi con co gia tri cho den ngay nay.", "By the end of his life he held 1,093 patents --- a world record still standing today.")],
          "Sang tao khong chi la tai nang --- do la qua trinh co to chuc, kien nhan va lam viec dau tu day di den cung.",
          "Innovation is not merely talent --- it is an organized, patient process of working all the way to the end."),

    story("J.K. Rowling --- Viet Trong Quan Ca Phe", "J.K. Rowling --- Anh 1994",
          "S",
          [("S au khi ly hon va mat viec, J.K. Rowling song nho tro cap xa hoi o Edinburgh voi con gai nho cua ba.", "After her divorce and job loss, J.K. Rowling lived on welfare in Edinburgh with her young daughter."),
           ("Moi sang, sau khi cho con di ngu, ba day xe ra quan ca phe --- vi benh nha re hon benh sua tam tu dien.", "Every morning after putting her daughter to sleep, she wheeled her stroller to a cafe --- because the heat was cheaper than heating the apartment."),
           ("Ba viet ban thao cuon Harry Potter trong quan ca phe do o nhiet do an toan --- viet tren may gay nhat co the tim.", "She wrote her Harry Potter manuscript in that cafe at warm temperature --- writing on paper scraps she could find."),
           ("Cuoi sach ba lam 60 ban sao voi may in nha --- vi khong du tien mua giay copy du luong.", "At the book's end she made 60 photocopies on a rented machine --- not having enough money for sufficient copy paper."),
           ("Cuon sach dau tien do om co ban duoc 500 trieu ban, Harry Potter tro thanh thuong hieu trieu do la.", "That cramped first book sold 500 million copies; Harry Potter became a multi-billion dollar brand.")],
          "Ban thao vi dai nhat cua ban co the dang duoc viet trong hoat canh kho khat nhat --- kho khat doi khi la phuong phap luong tot nhat cho su sang tao.",
          "Your greatest manuscript may be being written in your most difficult circumstances --- hardship is sometimes the best fertilizer for creativity."),

    story("Elon Musk --- Ho Tho Cuoi Cung Truoc Boc Cua", "Elon Musk --- Nam Phi/Hoa Ky 2008",
          "N",
          [("N am 2008, Elon Musk dang lam hai cong ty cung luc: Tesla dang sat pha san va SpaceX vua mat chiec ten lua thu ba.", "In 2008, Elon Musk was running two companies simultaneously: Tesla was nearing bankruptcy and SpaceX had just lost its third rocket."),
           ("Ong bo tat ca tien ca nhan vao hai cong ty nay --- tat ca --- va bay gio sap mat het.", "He had put all his personal money into both companies --- everything --- and was about to lose it all."),
           ("Ong chia so: 'Toi thuc day nua ngay va khong the ngo duoc --- toi chi hieu tai sao Elon Musk khong ngu duoc.'", "He shared: 'I woke up at 3am and couldn't sleep --- I finally understood why Elon Musk couldn't sleep.'"),
           ("Ten lua thu tu cua SpaceX thanh cong --- va Tesla nhan duoc von dau tu lu'ot song cuoi nam.", "SpaceX's fourth rocket succeeded --- and Tesla received a last-minute investment in late that year."),
           ("Bay gio mot trong hai cong ty la lon nhat the gioi theo tung linh vuc cua minh --- nhung o nam 2008, chi co mot su lua chon la tiep tuc.", "Today each company is among the world's largest in its field --- but in 2008, there was only one option: to continue.")],
          "Thuong chi can them mot lan thu nua sau tat ca cac lan thu truoc --- nhung ca gan lam, nen co gang than chon su kien nhan len tren he that vong.",
          "It often takes just one more try after all previous tries --- the trick is choosing patience over despair, even when hope seems gone."),

    story("Warren Buffett --- Kien Nhan La Vo Khi Bi Mat", "Warren Buffett --- Hoa Ky TK 20",
          "W",
          [("W arren Buffett bat dau dau tu tu luc 11 tuoi --- va giu co phieu dau tien cua minh qua nhung bien dong lon.", "Warren Buffett started investing at age 11 --- and held his first stock through major market swings."),
           ("Triet ly dau tu cua ong don gian den muc ai cung biet: 'Mua co phieu cua cong ty tot va giu chu khong ban.'", "His investment philosophy is so simple everyone knows it: 'Buy stock in good companies and simply hold, don't sell.'"),
           ("Nhung su don gian nay doi hoi mot dieu hiem hoi: kien nhan muoi nam, 20 nam, 30 nam.", "But this simplicity demands something rare: patience for 10 years, 20 years, 30 years."),
           ("Nam tuoi 90, Buffett van di lam moi ngay, van doc 5-6 tia tuc kinh te moi buoi sang.", "At age 90, Buffett still goes to work every day, still reads 5-6 financial newspapers every morning."),
           ("Ong noi: '99 phan tram tai san cua toi duoc tao ra sau tuoi 50 --- vi toi co du kien nhan cho lai suat kep lam viec.'", "He said: '99 percent of my wealth was created after age 50 --- because I had enough patience to let compound interest work.'")],
          "Lai kep --- trong dau tu hay trong hoc tap --- can thoi gian de phat huy suc manh; kien nhan khong phai la chon dung ma la vu khi tich cuc.",
          "Compound interest --- in investment or in learning --- needs time to unleash its power; patience is not passive waiting but an active weapon."),

    story("Ho Chi Minh --- Hanh Trinh 30 Nam Tim Duong Cuu Nuoc", "Ho Chi Minh --- Viet Nam TK 20",
          "N",
          [("N am 1911, Nguyen Tat Thanh --- 21 tuoi --- roi Bo Me Ha Noi tren mot con tau lam bep di tim duong giai phong dat nuoc.", "In 1911, Nguyen Tat Thanh --- 21 years old --- left the port of Saigon on a ship as a cook, going to find a path to liberate his country."),
           ("Ong song va lam viec o nhieu nuoc: Anh, Phap, My, Nga, Trung Quoc --- lam nhieu nghe khac nhau de ton tai trong khi hoc hoi.", "He lived and worked in many countries: England, France, America, Russia, China --- taking many jobs to survive while learning."),
           ("Tai Phap, ong tham gia phong trao cong nhan va dang Cong san, gui ban yeu sach len Hoa hoi Hoa binh Paris --- khong ai de y.", "In France he joined the workers' movement and the Communist Party, submitted a petition to the Paris Peace Conference --- no one noticed."),
           ("Sau ba muoi nam --- 1941 --- ong moi ve nuoc, lap Mat tran Viet Minh va lanh dao cach mang thanh cong nam 1945.", "After thirty years --- in 1941 --- he finally returned home, established the Viet Minh Front, and led the successful revolution of 1945."),
           ("Ong noi: 'Khong co gi quy hon doc lap tu do' --- cau noi cua mot nguoi da dang ca cuoc doi de ket luan dieu do.", "He said: 'Nothing is more precious than independence and freedom' --- words of a man who spent his entire life to reach that conclusion.")],
          "Anh cua viet nam cuoc doi --- hanh trinh 30 nam --- chung minh rang nhung muc tieu lon can thoi gian lon; dung do so qua thoi gian ma bo cuoc.",
          "Uncle Ho's life journey --- 30 years --- proves that great goals require great time; don't abandon your goal fearing the passage of time."),

    story("Marie Curie --- Hai Giai Nobel, Mot Nguoi Phu Nu", "Marie Curie --- Ba Lan/Phap 1903",
          "M",
          [("M arie Curie vi sinh ra la phu nu o the ki XIX, khong duoc vao dai hoc o Ba Lan --- phu nu khong duoc hoc.", "Marie Curie, born female in the 19th century, was denied university education in Poland --- women were not admitted."),
           ("Ba theo hoc tin hoc tai Paris --- song trong phong thue lanh buot, mac ao dong cuoi chua, an banh mi qua ngay.", "She attended secret lectures in Paris --- living in a freezing rented room, wearing the cheapest winter coat, eating bread to get through the day."),
           ("Ba dong chung voi Pierre Curie --- mot nha khoa hoc cung say me nghien cuu --- va ca hai kham pha ra Polonium va Radium.", "She collaborated with Pierre Curie --- a fellow scientist equally passionate about research --- and together they discovered Polonium and Radium."),
           ("Nam 1903, ba tro thanh nguoi phu nu dau tien nhan Nobel Vat ly; nam 1911, nhan Nobel Hoa hoc - nguoi duy nhat nhan ca hai.", "In 1903 she became the first woman to receive the Nobel Prize in Physics; in 1911 the Nobel in Chemistry --- the only person to receive both."),
           ("Vien Hoc Vien Khoa Hoc Phap tu choi ba vi la phu nu trong nhieu nam --- nhung hoc thuyet khoa hoc cua ba thi khong ai tu choi duoc.", "The French Academy of Sciences refused her membership for years because she was a woman --- but no one could refuse her scientific discoveries.")],
          "Rao can xa hoi khong phai cai chet cua uoc mo --- chung chi la vat can cuoc duong chay. Nhu'ng nguoi chon chay tiep la nhung nguoi thay doi lich su.",
          "Social barriers are not the death of dreams --- they are only hurdles on the race course. Those who choose to keep running are the ones who change history."),

    story("Nguyen Truong To --- Nha Cai Cach Viet Nam TK 19", "Nguyen Truong To --- Viet Nam 1863",
          "N",
          [("N guyen Truong To la mot tri thuc Viet Nam Cong giao, di Phap va Italia, the ky XIX, va nhin thay su phat trien cua phuong Tay.", "Nguyen Truong To was a Vietnamese Catholic intellectual who traveled to France and Italy in the 19th century and witnessed Western development."),
           ("Ong gui len trieu Nguyen 58 ban diec nghi ve canh tan --- canh tan giao duc, quan doi, thuong mai, ngoai giao.", "He submitted 58 memoranda to the Nguyen court calling for reform --- reforming education, military, trade, and diplomacy."),
           ("Trieu dinh nghe --- roi khong lam gi hoac lam qua cham; va Phap da xam luoc truoc khi bat ky cai cach nao duoc thuc hien.", "The court listened --- then did nothing or acted too slowly; and France invaded before any reform was implemented."),
           ("Ong viet: 'Nu'oc muon manh thi nuoc phai hoc, phai thay, phai tien --- khong the nhin the gioi thay doi con minh duc'", "He wrote: 'A nation wanting strength must learn, must change, must advance --- one cannot watch the world change while standing still.'"),
           ("Ong mat o tuoi 38, khi cuoc canh tan chu'a kip bat dau --- nhung tu tuong cua ong van con song cho den ngay nay.", "He died at 38, when reform had barely begun --- but his ideas live on to this day.")],
          "Kien taO cuoc doi khong chi la kien tao ban than --- nguoi co tam nhin cung kien tao xa hoi va the he sau, du ho khong song de thay ket qua.",
          "Building one's life is not only building oneself --- those with vision also build society and future generations, even if they don't live to see the result."),
    ])

with open(os.path.join(BASE, "ch10-kien-tao-cuoc-doi.tex"), "w", encoding="utf-8") as f:
    f.write(ch10)
print("ch10 done")

print("\nAll 10 chapters generated successfully! Total: 100 stories.")
