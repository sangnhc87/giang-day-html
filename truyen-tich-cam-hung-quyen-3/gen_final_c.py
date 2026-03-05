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
        "%============================================================",
        f"\\chapter{{Bai Hoc: {chap_vn} ({chap_en})}}",
        "\\begin{center}",
        f"  \\textit{{\\color{{truyenblue}}{quote_en}}}\\\\",
        f"  \\textit{{({quote_vn})}}\\\\[4pt]",
        "  \\small\\color{truyengold}--- Thien nhien day ta ---",
        "\\end{center}",
        "\\ngancach",
        "",
    ]
    for s in stories:
        lines.append(s)
    return unicodedata.normalize("NFC", "\n".join(lines))

# ================================================================
# CHUONG 5: THONG MINH
# ================================================================
ch5 = chapter(
    "Thong Minh Va Su Sang Tao", "Intelligence and Creativity",
    "Khon ngoan khong phai la biet nhieu dieu ma la biet su dung dieu minh biet.",
    "Intelligence is not knowing many things but knowing how to use what you know.",
    [
    story("Qua Vo Va Con Quang", "Con Quang",
          "M",
          [("M ot con quang va tinh co nhin thay cai qua oc nat gan ben duong nhung khong the be vo.", "A clever crow found a walnut near the road but could not crack it open."),
           ("No bay len cao, thu tha qua oc xuong mat duong cung ma van khong be duoc.", "It flew high and dropped the walnut onto the hard road but still could not crack it."),
           ("Sau do no sang kien the: no cho xe o to chay qua nghi qua oc se bi nghien nat.", "Then it had a clever idea: it waited for a car to drive over, thinking the nut would be crushed."),
           ("Nhung no phai cho sang den do de xe dung lai roi no moi gat lay nhan khong bi xe chet.", "But it had to wait for the red light so the car stopped and then it safely collected the kernel."),
           ("Con quang da ket hop vat ly, giao thong va thoi gian de giai quyet mot bai toan don gian.", "The crow combined physics, traffic, and timing to solve a simple problem.")],
          "Su thong minh that su la tim giai phap dac biet cho van de binh thuong, khong phai lam phuc tap them.",
          "True intelligence is finding a unique solution for an ordinary problem, not making it more complicated."),

    story("Bot Bong Ton Den Va Hoa", "Ong Bong",
          "K",
          [("K hi mua dong den, dong vat muon giu am bang nhieu cach khac nhau dac biet.", "When winter arrives, animals stay warm in many special different ways."),
           ("Dan ong vo dat thanh qua cau lon o trung tam to de thu nhiet the phat ra.", "The bee colony forms a large ball at the center of the hive to capture body heat."),
           ("Nhung con o ngoai cung run that nhanh bam chat vao nhau de tao nhiet ma khong phai di chuyen.", "Those on the outer shell vibrate fast and cling tightly together generating heat without moving."),
           ("Sau do chung luan doi vi tri: con lanh vao trong, con am quay ra ngoai thay phien.", "Then they rotate positions: cold ones move inside, warm ones move outside in turns."),
           ("He thong luan doi do giu toan dan on am suot mua dong ma khong can nhien lieu bao nhieu.", "That rotation system keeps the whole colony warm through winter using very little fuel.")],
          "Thong minh tap the thuong viet hon bat ky tri tue ca nhan nao: hay tan dung moi nao luc cua nhom.",
          "Collective intelligence surpasses any individual intellect: harness all the brainpower of your team."),

    story("Bo Ho Tach Mu Con Moi", "Bo Ho",
          "B",
          [("B o ho can pha cac vet thuong tren da bo de xua duoi cac con rui ruoi muon de trung.", "Oxpecker birds pick wounds on buffalo skin to drive away flies that want to lay eggs."),
           ("Nhung dieu bat ngo la bo ho cung an luon sau bo dang an da bo tren vet thuong.", "But surprisingly, oxpeckers also eat the lice currently eating buffalo hide on the wounds."),
           ("Bo ho len tren lung trau bo khong chi an sau bo ma con dong vai tro bao ve canh gac.", "Oxpeckers on buffalo backs not only eat parasites but also serve as sentinel guards."),
           ("Khi co su tu den gan, bo ho keu to canh bao cho trau bo chay thi ngay.", "When a lion approaches, the oxpecker cries out loudly warning the buffalo to run immediately."),
           ("Moi quan he ky sinh thoat hoat thanh moi quan he cong sinh khi hai ben biet nhin xa hon.", "A parasitic relationship transforms into a mutualistic one when both sides know to look farther ahead.")],
          "Thong minh nhat la bien nguoi tung la ke lay loi ich tu ban thanh nguoi dong hanh giup ich cho ban.",
          "The smartest move is turning someone who once extracted benefit from you into a partner who benefits you."),

    story("Ca Tam Giac Luoi San", "Ca Tam Giac",
          "L",
          [("L oan ca tam giac lon song o vung nuoc am luon san moi bang chien thuat nguoc sang.", "Schools of large triggerfish living in warm waters always hunt prey by moving against the light."),
           ("Chung thuong tan cong khi mat troi o sau lung chung de mat troi chieu vao mat con moi.", "They often attack when the sun is behind them so sunlight shines directly into the prey's eyes."),
           ("Con moi bi loa mat boi anh sang choi chang khong kip nhan biet nguy hiem sap den.", "The prey is blinded by the glare and unable to recognize the approaching danger in time."),
           ("Ca tam giac su dung vat ly quang hoc phu hop voi thoi gian trong ngay mot cach chinh xac.", "Triggerfish use optical physics aligned with the exact time of day with precision."),
           ("Cac nha quan su hoc chien thuat tan cong nguoc sang tu loai ca nay de ung dung vao chien tranh.", "Military strategists learned the counter-sun attack tactic from this fish to apply to warfare.")],
          "Biet su dung moi truong xung quanh nhu vu khi la dinh cao cua tri tue chien luoc.",
          "Knowing how to use the surrounding environment as a weapon is the peak of strategic intelligence."),

    story("Voi Dung Cong Cu", "Voi",
          "N",
          [("N guoi ta tung nghi chi con nguoi moi biet su dung cong cu de thuc hien cong viec.", "People once thought only humans knew how to use tools to perform tasks."),
           ("Nhung voi biet cat canh cay va cam vao voi de quat ruoi va muoi mot cach hieu qua.", "But elephants know to pick up branches and hold them with their trunks to swat flies and mosquitoes effectively."),
           ("Voi cung biet lay da to che vao mieng lo nuoc de nuoc khong bay hoi trong ngay nang nong.", "Elephants also know to use large stones to cover water holes so water doesn't evaporate on hot days."),
           ("Mot so con con biet dung thanh cay dai xoa len tuong de ve hinh theo y thich rieng.", "Some even use long sticks to draw on walls creating pictures according to their own preferences."),
           ("Tri tue khong goi han o bat ky loai nao; no hien huu o noi nao co nhu cau va kham pha.", "Intelligence is not limited to any species; it exists wherever there is need and curiosity.")],
          "Hay mo rong dinh nghia cua ban ve tri tue; nhung giai phap tot nhat co the den tu noi ban it ky vong nhat.",
          "Broaden your definition of intelligence; the best solutions may come from where you least expect them."),

    story("Khi Dau Tien Dung Gguong", "Con Khi",
          "L",
          [("L an dau tien nguoi ta dat guong truoc chuong khi, tat ca bong doi mat o la thay.", "The first time researchers placed a mirror before a monkey cage, all stared in confusion at the stranger."),
           ("Nhungo mot so loai khi cao cap nhu tinh tinh sau vai phut hieu ra minh dang nhin chinh minh.", "But some higher primates like chimpanzees realized after a few minutes they were looking at themselves."),
           ("Tinh tinh bat dau kiem tra mat, rang, long nguoi ban gom bam duoi mat guong.", "The chimpanzee began examining its face, teeth, and fur that was stuck under its eyes using the mirror."),
           ("No dung guong nhu cong cu de lam dep va kiem tra khu vuc co the no khong tu nhin thay duoc.", "It used the mirror as a tool for grooming and checking body areas it cannot see directly."),
           ("Tu nhan thuc la buoc dau tien cua tri tue cao cap ma rat it sinh vat tren Trai Dat co duoc.", "Self-awareness is the first step of higher intelligence that very few creatures on Earth possess.")],
          "Bat dau hieu ban than la cuoc hanh trinh thong minh nhat ma bat ky ai co the bat tay vao.",
          "Beginning to understand yourself is the most intelligent journey anyone can embark upon."),

    story("Nuoc Dang Len Den Ca Tho", "Chim Co",
          "M",
          [("M ot con chim co khong the chen mo vao binh co co mieng nho de uong nuoc.", "A crow could not fit its beak into a bottle with a narrow mouth to drink water."),
           ("No nhin xung quanh va bat dau nhat da nho ne trong vao binh nuoc chiem dat.", "It looked around and began picking up small pebbles to drop into the water bottle occupying space."),
           ("Muc nuoc tu tu dang len theo tung hon da no them vao mot cach kien nhan.", "The water level slowly rose with each pebble it patiently added one by one."),
           ("Sau bay muoi hon da, nuoc len du cao de no thoe mo uong duoc no ne no long.", "After seventy pebbles, the water rose high enough for it to dip its beak in and drink happily."),
           ("Bay gio bai toan nay duoc day trong truong tieu hoc nhu vi du ve tu duy sang tao.", "Today this problem is taught in elementary school as an example of creative thinking.")],
          "Khi khong the di theo duong thang, hay tim cach gian tiep them den de vat can hoa thanh loi the.",
          "When you cannot go straight, find an indirect way to add to the obstacle until it becomes an advantage."),

    story("Ca Voi Dung Am Thanh San Moi", "Ca Voi Xanh",
          "A",
          [("A m thanh cua ca voi xanh co the truyen di xa den 1600 km trong dat nuoc truoc khi tan bien.", "The sound of a blue whale can travel up to 1,600 kilometers through ocean water before disappearing."),
           ("Chung su dung am thanh de tao ban do tinh thon sac nu xac ca hang nghin km vuong xung quanh.", "They use sound to create detailed topographic maps of the seabed thousands of square kilometers around them."),
           ("Khi loai ca moi boi tu xuong sau len mat nuoc, ca voi da do vi tri chinh xac truoc do 20 phut.", "When prey fish swim up from the deep to the surface, whales have pinpointed their exact location 20 minutes before."),
           ("Ca voi dung vat ly am thanh trong nuoc nhu he thong GPS song am tu tu nhieu chieu.", "Whales use underwater acoustic physics like a multidimensional sonar GPS system."),
           ("Chung da thong minh hon nhieu loai cong cu ma con nguoi moi phat minh ra gan day.", "They were smarter than many tools humans only recently invented.")],
          "Tri tue that su khong can nhan mat; no co the lang nghe, cam nhan va ve ban do the gioi bang phuong tien khac.",
          "True intelligence needs no eyes; it can listen, sense, and map the world by other means."),

    story("Nhen Day Cuu Minh", "Nhen",
          "M",
          [("M ot con nhen roi xuong ao nuoc va khong the boi vao bo duoc vi dong nuoc khong ung ho.", "A spider fell into a pond and could not swim to shore because the water current did not help."),
           ("No tuc thi dung chan sau de xoay than tao ra luc day nguoc chieu dong nuoc.", "It immediately used its back legs to spin its body creating a force against the current direction."),
           ("Dong nuoc day no vao bo thay vi ra giua ho theo nhu phuong phap benh vien nguoc.", "The current pushed it toward shore instead of toward the center of the lake, like a reverse paddle method."),
           ("Toan bo hanh dong chi mat vai giay nhung la ket qua cua viec hieu vat ly chat long.", "The whole action took only seconds but was the result of understanding fluid physics."),
           ("Khoa hoc vat ly khong chi la sach giao khoa; no la ky nang song cua moi sinh vat tren dot.", "Physics is not just a textbook; it is the survival skill of every living creature on Earth.")],
          "Hoc vat ly, hoa hoc, sinh hoc khong phai de thi ma de song; thien nhien da biet dieu do tu lau.",
          "Study physics, chemistry, and biology not to pass tests but to live; nature has always known this."),

    story("Biet Doi Du Bao Thoi Tiet", "Biet Doi",
          "K",
          [("K hi ap suat khi quyen thay doi truoc con bao, con nguoi kho nhan ra song biet doi tuc thi cam nhan duoc.", "When atmospheric pressure changes before a storm, humans barely notice but bats immediately sense it."),
           ("Biet doi bay thap hem, co lai long va tim noi truy nen hin an nang xuat doc tuc thoi.", "Bats fly lower, tuck their wings, and find sheltered spots as their instinctive forecast activates."),
           ("Cac nha khoa hoc theo doi hanh vi bat thuong cua biet doi de du bao bao to chinh xac hon.", "Scientists track abnormal bat behavior to forecast storms more accurately."),
           ("Co the nhay cam cua loai vat thuong vuot xa bat ky may moc nao con nguoi che tao ra.", "Animals' sensitive bodies often far surpass any instruments humans have ever created."),
           ("Thong minh khong chi la phan tich so lieu ma con la biet lang nghe tin hieu thien nhien.", "Intelligence is not just analyzing data but also knowing how to listen to nature's signals.")],
          "Hanh vi cua dong vat quanh ban co the la ban tin thoi tiet chinh xac hon bat ky ung dung dien thoai nao.",
          "Animal behavior around you can be a more accurate weather report than any phone app."),
    ])

with open(os.path.join(BASE, "ch05-thong-minh.tex"), "w", encoding="utf-8") as f:
    f.write(ch5)
print("ch05 done")

# ================================================================
# CHUONG 6: THICH NGHI
# ================================================================
ch6 = chapter(
    "Thich Nghi De Song Con", "Adapt to Survive",
    "It is not the strongest who survive, but those most adaptable to change.",
    "Khong phai ke manh nhat ton tai ma la ke thich nghi tot nhat voi su thay doi.",
    [
    story("Ca Thu Thuc Dong", "Ca Thu",
          "K",
          [("K hi mat ho dong bang, ca thu chuyem sang trao doi chat cham den muc gan nhu ngung han.", "When the lake freezes over, the crucian carp shifts its metabolism to near standstill."),
           ("No ngung an, ngung boi, tim xuong day bun lan sau buoc vao giac ngu dong sau.", "It stops eating, stops swimming, sinks to the muddy bottom and enters deep winter sleep."),
           ("Tim dap chi con vai nhip moi phut, nhiet do co the ha xuong gan bang diem dong.", "Heart beats only a few times per minute, body temperature drops near freezing point."),
           ("Khi mua xuan toi no thuc day khoe manh, bat dau an va lai vui song nhu khong co gi xay ra.", "When spring comes it wakes healthy, starts eating and swims joyfully as if nothing happened."),
           ("Kha nang thich nghi hoat dong cua co the la su song con thong minh nhat ma sinh vat biet.", "The ability to adapt bodily functions is the smartest survival skill any organism possesses.")],
          "Doi khi dung lai, lam cham, hoac nguoi than truoc bao to chinh la dang thich nghi khon ngoan nhat.",
          "Sometimes stopping, slowing down, or going quiet before a storm is the wisest form of adaptation."),

    story("Tac Ke Doi Mau Da", "Tac Ke",
          "T",
          [("T ren tang da lich su tac ke doi mau tu xanh la cay sang tim tim nau nau chi trong vai giay.", "On a mossy rock the gecko changes color from green to purple-brown in just a few seconds."),
           ("Khong phai no tu mau nao no muon ma no phan anh chinh xac mau nen phia sau no.", "It does not choose any color it wants but exactly reflects the color of the background behind it."),
           ("He thong sac to trong te bao da no tich hop tin hieu mat tu mat bong va tu nao.", "The pigment system in its skin cells integrates light signals from its eyes and brain simultaneously."),
           ("Ke thu nhin thang vao no ma khong thay gi vi bao mat mau sac cua no hoan hao.", "Predators stare directly at it and see nothing because its color camouflage is perfect."),
           ("Thich nghi khong phai thay doi ban than ma la hoa minh vao hoan canh mot cach tu nhien.", "Adaptation is not changing yourself but naturally blending into circumstances.")],
          "Nghe thuat hoa minh khong co nghia la mat di ban sac; do la biet bieu hien dung dieu dung luc.",
          "The art of blending in does not mean losing identity; it means knowing to show the right thing at the right time."),

    story("Trau Bien Song Tren Bai Nong", "Trau Bien",
          "N",
          [("N oi nui lua am tham phun nham chay ra bien, da lava mat lanh nhanh thanh nhung dao nui nho.", "Where volcanoes quietly erupt into the sea, lava quickly cools into small rocky islands."),
           ("Chi trong nam muoi nam dau tien khong co gi song duoc tren nhung tang da trang tron.", "In the first fifty years nothing can live on those barren bare rock surfaces."),
           ("Roi den loai trau bien: chung bam chat vao da lan nhat xua do, song nho nuoc bien va anh sang.", "Then sea lettuce arrives: it clings tightly to the now-cooled rock, living off seawater and sunlight."),
           ("Chung chet di de lai lop mun huu co mong manh dau tien tren mat da lava lạnh nguoi.", "They die leaving the first thin organic layer on the cold lava surface."),
           ("Tren lop mun do, sau muoi nam, cac loai co va hoa nho bat dau moc len xanh tuoi.", "On that layer, after ten more years, small grasses and flowers begin growing fresh and green.")],
          "Moi truong ky nhat van co the tro nen song duoc neu ai do dam la nguoi di tien phong dau tien.",
          "Even the most hostile environment can become livable if someone dares to be the first pioneer."),

    story("Chim Di Cu Thay Duong Bay", "Chim Di Cu",
          "K",
          [("K hi bieu bien khi hau thay doi khien dong vat den muon hon moi nam khi loai chim cho doi.", "When climate change makes insects arrive later each year than the birds waiting for them."),
           ("Nhung con chim co dau oc linh hoat thay doi lich trinh bay cua minh theo.", "The more flexible-minded birds change their own flight schedules accordingly."),
           ("Mot so loai thay doi han noi dem trung tu khu vuc truyen thong sang cac vi tri moi mat.", "Some species completely shift nesting sites from traditional areas to new locations."),
           ("Nhung con bam vao tap quan cu thi dan dan tuyet chung trong khi loai linh hoat phat trien.", "Those clinging to old habits gradually go extinct while flexible species thrive."),
           ("Thich nghi khong phai phan boi qua khu; do la ton trong qua khu va tien buoc vao tuong lai.", "Adapting is not betraying the past; it is honoring the past while stepping into the future.")],
          "Thay lich trinh, thay dia ban, thay chien thuat khi hoan canh doi, nhung khong bao gio thay muc tieu.",
          "Change the schedule, change the territory, change the tactics when circumstances change, but never change the goal."),

    story("Rang San Ho Trang Hoa", "San Ho",
          "R",
          [("R ang san ho tuoi dep nhat the gioi bi tang nhiet va axit hoa bien lam trang hon toan bo.", "One of the world's most beautiful coral reefs was completely bleached by rising temperature and ocean acidification."),
           ("Nha khoa hoc nghi no da chet nhung sau chin thang mot so polip bat dau thich nghi.", "Scientists thought it was dead but after nine months some polyps began adapting."),
           ("Chung bat dau chap nhan loai tao co kha nang chiu nhiet cao hon len song trong mo.", "They began accepting heat-resistant algae species to live within their tissues."),
           ("Khong dep bang truoc nhung chung song, sinh san va dan dan xay lai rao chan theo cach moi.", "Not as beautiful as before but alive, reproducing, and gradually rebuilding the barrier in a new way."),
           ("Hoi phuc sau ton thuong la dang thich nghi cao quy nhat va can long can dam nhat.", "Recovery after injury is the noblest form of adaptation and requires the most courage.")],
          "Khong can phai hoan la hoa da; can la song sot, phat trien va xay dung lai sau tham hoa.",
          "No need to be perfectly pristine; what counts is surviving, growing, and rebuilding after disaster."),

    story("Loai Ech Dong Bang Va Tan Chay", "Con Ech",
          "V",
          [("V ung Alaska mua dong xuong am 40 do C, loai ech go tim each vuot qua mot cach ky dieu.", "In Alaska when winter drops to minus 40 C, the wood frog overcomes it in a remarkable way."),
           ("No de nhan the gan nhu dong bang hoan toan, tim ngung dap, phoi ngung tho binh thuong.", "It allows its body to nearly completely freeze, heart stopping, lungs ceasing normal breathing."),
           ("Nuoc duong va glycoprotein trong mau no ngan can cac tinh the bang pha vo te bao.", "Sugar and glycoproteins in its blood prevent ice crystals from rupturing cells."),
           ("Mua xuan ve nhiet do tang, tim ech dap lai, phoi thu khi oxy va no nhay di kieu nhu binh thuong.", "Spring comes, temperature rises, the frog's heart beats again, lungs take in oxygen and it hops off normally."),
           ("No da che thach cau tru sinh va vat ly theo cach khoa hoc chua ai ngu o duoc.", "It has mastered biology and physics in ways science has not yet fully understood.")],
          "Doi khi chi can ton tai qua thoi diem kiet suc nhat la mot thanh cong vi dai; hay truong thu nhu con ech.",
          "Sometimes merely surviving through the most exhausted moment is a great achievement; hibernate like the wood frog."),

    story("Gau Bac Cuc Dieu Chinh Che Do An", "Gau Bac Cuc",
          "K",
          [("K hi bien bang tan chay, gau bac cuc mat nguon ca la thuc an chinh cua minh.", "When sea ice melts, polar bears lose their seal hunting grounds, their primary food source."),
           ("Cac nha nghien cuu phat hien mot so con gau bat dau an trung chim, tao bien va qua mam.", "Researchers found some bears began eating bird eggs, seaweed, and berries."),
           ("Loai di ran than tran suot muon nam gio chap nhan che do an thuc vat linh dong hon.", "The species long labeled carnivore now accepts a more flexible plant-heavy diet."),
           ("Chung khong chet nhu tu tung nghi; chung dieu chinh va tim ra cach song trong the gioi moi.", "They did not die as once predicted; they adjusted and found ways to live in the new world."),
           ("Khi nguon sinh ke cu mat di, se lo lang qua lau la mat thu gian quy, hay hanh dong ngay.", "When your old livelihood disappears, worrying too long is wasting precious time; act now.")],
          "Khong ai bi buoc phai tuyet chung boi viec bien doi hoan canh; thay doi la lua chon cua ban.",
          "No one is forced to extinction by changing circumstances; changing with them is your choice."),

    story("Cay Rung Ngap Man", "Cay Man",
          "C",
          [("C ay man song trong nuoc man co nong do muoi cao gap ba lan man nuoc bien binh thuong.", "Mangroves live in salt water three times saltier than average ocean water."),
           ("Chung phat trien he thong re ky la nho ra khoi mat dat de lay khong khi ngap truc tiep.", "They develop strange root systems sticking up from the ground to breathe air directly."),
           ("La cay tiet muoi ra ngoai qua cac te bao dac biet de bao ve he thong noi tai.", "Leaves excrete salt through specialized cells to protect the internal system."),
           ("Chung song o vung ma khong loai cay nao khac chiu duoc, tho dat tho bien lam tam thuong.", "They live where no other trees can survive, claiming estuary land where sea meets land as ordinary."),
           ("Kha nang ton tai o ranh gioi giua hai the gioi la suc manh hiem co cua nhung linh hon doc dao.", "The ability to survive on the boundary between two worlds is the rare strength of truly unique souls.")],
          "Nhung nguoi manh nhat khong song trong moi truong de chiu ma trong moi truong thach thuc.",
          "The strongest people do not live in easy environments but in challenging ones."),

    story("Ca Vang Nho Tao Ra Hang Soa", "Ca Vang",
          "K",
          [("K hi nuoc troi can kho do han han, ca vang song trong ao nho bat dau duoc long dat.", "When water evaporates and dries in drought, goldfish living in small ponds began burrowing into soil."),
           ("Chung vui lon vao lop bun day nhat phat la da am, nam thu minh cho den khi mua den.", "They push deep into the thickest mud layer still moist, curl up and wait until the rain comes."),
           ("Tim dap rat cham, ho hap bang da va lac chat dinh duong du tru tu dong.", "Heart beats very slowly, breathing through skin and consuming stored nutrients automatically."),
           ("Sau muoi tun it nuoc roi xuong, chung thoat khoi bun va boi troi ra binh thuong.", "After ten weeks when water falls, they emerge from mud and swim out normally."),
           ("Co the cua chung bien ao ho thanh noi tru an de song sot qua han ha, khong co gi tu nhien hon.", "Their bodies transform the pond mud into a shelter to survive drought; nothing is more natural.")],
          "Khi moi truong thay doi, hay tim rao can moi trong chinh hoan canh kho khan cua ban.",
          "When your environment changes, find new shelter within your very difficult circumstances."),

    story("Loai Qua Hoc Biet Mo Hop", "Con Qua",
          "Q",
          [("Q ua den cua thanh pho Tokyo hoc duoc cach mo hop ca hop thep bang cach tha tu tren cao.", "Tokyo city crows learned to open canned food by dropping it from height onto hard surfaces."),
           ("Chung cung hoc lot vo hat oc bang cach tha xuong duong va cho xe chay qua no.", "They also learned to peel walnut shells by dropping them on roads and waiting for cars to run over them."),
           ("The he qua sau hoc lai hanh vi moi tu the he truoc, tao thanh mot nen van hoa thi cu tang dan.", "Subsequent crow generations learn new behaviors from previous ones, creating a culture that accumulates."),
           ("Day la mot trong nhung bang chung dau tien ve truyen dat van hoa phi con nguoi trong tu nhien.", "This is one of the first pieces of evidence of non-human cultural transmission in nature."),
           ("Loai co the hoc va day lai cho the he sau se luon thich nghi va ton tai vuot troi.", "Species that can learn and pass on to the next generation will always adapt and survive superbly.")],
          "Kha nang hoc, di truyen va thich nghi voi hoan canh moi la di san quy bau nhat ban co the trao con chau.",
          "The ability to learn, transmit, and adapt to new circumstances is the most precious legacy you can pass to descendants."),
    ])

with open(os.path.join(BASE, "ch06-thich-nghi.tex"), "w", encoding="utf-8") as f:
    f.write(ch6)
print("ch06 done")

# ================================================================
# CHUONG 7: BIET ON
# ================================================================
ch7 = chapter(
    "Biet On Va Tri An", "Gratitude and Appreciation",
    "Gratitude opens the fullness of life; it turns what we have into enough.",
    "Biet on mo ra su phong phu cua cuoc song; no bien nhung gi ta co thanh du day.",
    [
    story("Cho Trung Thanh Hachiko", "Cho Hachiko",
          "H",
          [("H achiko moi ngay den ga tau Shibuya don chu ve nha sau gio lam viec tan ca.", "Hachiko came to Shibuya station every day to welcome his owner home after work ended."),
           ("Mot ngay chu qua doi dot ngot tai noi lam viec va khong bao gio tro ve nua.", "One day the owner died suddenly at work and never returned."),
           ("Nhung Hachiko van tro lai ga tau moi ngay mot cach deu dan trong muoi nam lien tiep.", "But Hachiko still returned to the station every day consistently for ten consecutive years."),
           ("Ong khong biet khai niem cai chet; ong chi biet chu minh la nguoi xung dang duoc cho.", "He did not understand the concept of death; he only knew his owner was someone worth waiting for."),
           ("Long biet on va trung thanh cua Hachiko khong the goi ten bang bat ky loi nao co du.", "Hachiko's gratitude and loyalty cannot be named by any words sufficient enough.")],
          "Trung thanh la biet on theo thoi gian: ta co the biet on mot nguoi ca khi ho khong con o ben ta nua.",
          "Loyalty is gratitude over time: we can be grateful to someone even when they are no longer beside us."),

    story("Ca Heo Biet On Nguoi Cuu", "Ca Heo",
          "M",
          [("M ot nguoi tho lan thay mot con ca heo bi day luoi nguy hiem, linh so cat day giai cuu no.", "A diver saw a dolphin dangerously entangled in nets, instinctively cutting the ropes to free it."),
           ("Con ca heo boi ra tu do, voi lon vong quanh nguoi tho dan de vet thuong.", "The dolphin swam free, then made large circles around the diver checking for wounds."),
           ("No con sung vau vao tay nguoi de to ra su tiep xuc than thiet truoc khi boi di.", "It also nudged the person's hand to show intimate contact before swimming away."),
           ("Ba ngay sau con nguoi do gap kho khan khi lan sau; mot dan ca heo xuat hien day anh len bo.", "Three days later the same person got into difficulty diving deep; a dolphin pod appeared and pushed him to shore."),
           ("Lieu co the la con ca heo do quay lai hay khong, ta khong biet chac, nhung huong ve phia biet on thi co.", "Whether it was that same dolphin we cannot know for sure, but the direction of gratitude points there.")],
          "Nhung gi ta trao di voi long thanh that co the quay tro lai theo nhieu cach ta khong lan tuong duoc.",
          "What we give with true sincerity can return in ways we could never have imagined."),

    story("Suc Seo Che Cho Loai Khac", "Suc Seo",
          "N",
          [("N guoi quan sat thay nhung con chim nho thuong xay to tren canh cay keo chan hom.", "Observers noticed small birds often build nests in the branches of acacia trees housing ants."),
           ("Luc dau nghi chim la nguyen nhan, nhung ky ra la chim chu dong tim den de suc nhung lo an tu cay.", "At first thought birds were the cause, but it turned out birds actively sought out trees with ant colonies."),
           ("Kien bao ve cay khoi sau benh rot vao cay va do lat loai chim an trung chim xuong bai.", "Ants protected the trees from pest borers and drove away thieving birds that stole nestling eggs."),
           ("Chim tu nguyen xay to o do de duoc bao ve mien phi tu he thong an ninh kien dau tien.", "Birds voluntarily nested there to receive free protection from the ant security system."),
           ("Su biet on duoc the hien bang viec tro thanh mot phan cua he sinh thai ho tro lan nhau.", "Gratitude is expressed by becoming part of a mutually supportive ecosystem.")],
          "Khi ai do giup ban, ti le biet on tot nhat khong chi la loi cam on ma la tro nen co ich cho ho.",
          "When someone helps you, the best expression of gratitude is not just saying thank you but becoming useful to them."),

    story("Con Rua Biet On Nguoi Giai Cuu", "Con Rua",
          "T",
          [("T ruyen co ke ve con rua ca bien biet on nguoi fisherman da giai thoat no khoi luoi.", "The old tale tells of a sea turtle grateful to the fisherman who freed it from the net."),
           ("Rua quay lai dan nguoi ra bien sau con bao chi huong den ben bo an toan.", "The turtle returned and guided the person out to sea after the storm toward a safe harbor."),
           ("Phong tuc nguoi Nhat Boc Bong goi la urashima: biet on phai dam nhan tranh nhiem tra lai.", "The Japanese custom called urashima: gratitude must dare to take responsibility in return."),
           ("Cau chuyen co tich nen khong the kiem chung, nhung cam xuc ma no truyen dat la that.", "The fairy tale cannot be verified, but the feeling it conveys is real."),
           ("Biet on khong chi la cam giac; no la quyet dinh hanh dong tra lai cho cuoc song nhung gi cuoc song da trao.", "Gratitude is not just a feeling; it is the decision to act and give back to life what life has given.")],
          "Biet on hoat dong nhu mot vong luon: cang trao di cang nhan lai, doi song cang tro nen phong phu.",
          "Gratitude operates as a cycle: the more you give back the more you receive, life becomes ever richer."),

    story("Hoa Huong Duong Quay Mat Theo Nang", "Hoa Huong Duong",
          "M",
          [("M oi sang hoa huong duong huong mat ve phia dong noi mat troi moc sap den.", "Every morning sunflowers face east where the sun will rise."),
           ("Ca ngay chung xoay than theo hanh trinh cua mat troi tu dong sang tay tu tung phut.", "All day they slowly turn their stems following the sun's journey from east to west minute by minute."),
           ("Ban dem hoa quay tro lai vi tri dong de san sang chao mat troi sang hom sau.", "At night the flowers turn back to the east position to be ready to welcome the next day's sun."),
           ("Hanh dong xoay cua than hoa khong phai phan xa mac dinh; do la su the hien long biet on.", "The stem's turning movement is not just a default reflex; it is an expression of gratitude."),
           ("Biet on la huong mat ve noi soi sang cuoc song ban; lam dieu do moi ngay.", "Gratitude is facing toward what gives your life light; do that every day.")],
          "Hay bat dau moi ngay bang viec quay mat ve phia nhung dieu va nhung nguoi dem anh sang vao doi ban.",
          "Begin every day by turning your face toward the things and people who bring light into your life."),

    story("Cay Hoa Anh Dao Va Mua Xuan", "Hoa Anh Dao",
          "M",
          [("M oi nam cay hoa anh dao chi no trong mot tuan ngan ngui roi rung het trong nac long.", "Each year cherry blossom trees bloom for only one short week then fall completely in heartbreak."),
           ("Nguoi Nhat coi tuan no do la tang qua thieng lieng nhat cua thien nhien va tri an tung canh.", "The Japanese consider that blooming week the most sacred gift of nature and cherish every petal."),
           ("Ho ngoi ben duoi tan canh, khong dung dien thoai, chi lang nghe gio va nhin canh hoa bay.", "They sit beneath the canopy, not using phones, only listening to wind and watching petals fly."),
           ("Hanh dong do goi la mono no aware: cam nhan ve ve dep nang neu cua su qua do.", "That act is called mono no aware: feeling for the fleeting beauty of impermanence."),
           ("Biet on ve dep cua nhung dieu qua do la loai hinh tri tue tinh te nhat con nguoi co the phat trien.", "Appreciating the beauty of fleeting things is the most refined form of intelligence humans can develop.")],
          "Biet on nhung gi dang co mat hom nay vi ngay mai no co the mat di khong thong bao truoc.",
          "Be grateful for what is present today because tomorrow it may disappear without notice."),

    story("Vooc Cham Soc Nguoi Gia", "Vooc",
          "T",
          [("T rong bays vooc chau Phi, cac con tre cham soc va nhg tiep thuc an cho cac con gia yeu duoi.", "In African vervet monkey troops, young members care for and bring food to elderly weak members."),
           ("Vooc gia khong con co the leo hay hanh dong nhanh nhay nhung van duoc bao ve trong bays.", "Old vervets can no longer climb or act swiftly but are still protected within the troop."),
           ("Cac nha nghien cuu phat hien vooc gia cung cap tri thuc kinh nghiem quan trong cho ca bay.", "Researchers found elderly vervets provide important experiential knowledge for the whole troop."),
           ("Ho nho nhung nguon nuoc cu, nhung con duong an toan va nhung mua ba tung xay ra.", "They remember old water sources, safe paths, and past predator seasonal patterns."),
           ("Cham soc nguoi gia khong phai tu thien; do la dau tu khon ngoan vao kho luyen tri tue cua ca tap the.", "Caring for the elderly is not charity; it is a wise investment in the entire group's accumulated wisdom.")],
          "Hay de nguoi lon tuoi trong nhom cua ban truyen dat tri thuc; ho la thu vien song cua tap the ban.",
          "Let older people in your group share their knowledge; they are the living library of your community."),

    story("Ca Heo Giai Cuu Nguoi Bi Chuot Ran", "Ca Heo",
          "T",
          [("T ai New Zealand mot nguoi boi bi dan ca map vay quanh tren bien la ngoai bo.", "In New Zealand a swimmer was surrounded by sharks far offshore."),
           ("Mua dan ca heo bay den tao thanh vong tron bao ve xung quanh nguoi boi do.", "A pod of dolphins immediately arrived forming a protective circle around the swimmer."),
           ("Chung khong chuyen di ma bay lai trong 40 phut cho den khi tau cuu ho den.", "They did not leave but swam in circles for 40 minutes until the rescue boat arrived."),
           ("Mot ca heo con lien tuc vu vao nguoi boi de giup nguoi boi tinh tao khong ngo chim.", "One dolphin continuously nudged the swimmer to help them stay alert and not sink drowsy."),
           ("Loai ca heo khong co ly do gi de cuu con nguoi ngoai bat dong loai; nhung chung van cuu.", "Dolphins have no reason to rescue humans outside of interspecies empathy; yet they do.")],
          "Long biet on va su giup do co the buoc qua ranh gioi loai; hay mo rong vong tay ban ra xa hon.",
          "Gratitude and helping can cross the boundary of species; extend your circle of care wider."),

    story("Khi Con Cuu Minh Khoi Cuon", "Con Khi",
          "K",
          [("K hi lu cuon no lai, mot nha khoa hoc bi mat cu tren bo song ngan duoc cay lon.", "When flood waters swept and rose, a scientist was cut off on a riverbank blocked by a large tree."),
           ("Mot con khi nho bay den, trao cho anh mot doan roi day leo de ket vao canh cay moc danh kia.", "A small monkey came over, handing him a length of twisted vine to tie to the leaning tree branch."),
           ("Anh ket vao and dung dan bo day boi qua doln song lai an toan.", "He tied on and climbed the vine across the flooded river safely."),
           ("Khi day khoa hoc phan tich, loai khi do khong co loi ich cu the nao tu hanh dong nay het.", "When later scientists analyzed it, that monkey species had no concrete benefit from this action at all."),
           ("Altruism, su giup do vo tu, co the xuat hien o nhieu loai hon la chung ta dang nghi.", "Altruism, selfless helping, may appear in more species than we currently think.")],
          "Du ban co la nguoi hay la thu vat, thien tuyen co the thuc day hanh dong tot dep khong tinh toan.",
          "Whether you are human or animal, innate goodness can drive selfless acts without calculation."),

    story("Rua De Trung Tren Bai Bien", "Rua Bien",
          "T",
          [("T rong hanh trinh tuong tu mo cua minh, rua bien chon dung bai bien noi no chao doi de de trung.", "In a journey resembling a circle of memory, the sea turtle chooses the exact beach where it was born to lay eggs."),
           ("Sau hai muoi nam boi khap dai duong no quay lai noi bat dau chinh xac den tung met.", "After twenty years crossing the entire ocean it returns to its starting point accurate to the meter."),
           ("No khong biet gi ve bai bien khac; no chi biet noi day la nha va no phai tra lai.", "It knows nothing of other beaches; it only knows here is home and it must return."),
           ("Bai hoc la: biet on noi ban duoc sinh ra, noi da tao nen con nguoi ban hom nay.", "The lesson is: be grateful for where you were born, the place that created the person you are today."),
           ("Quay ve nguon coi de trao lai qua tang la hanh dong biet on dep de nhat ma sinh vat biet lam.", "Returning to your origins to give a gift back is the loveliest act of gratitude any creature knows how to do.")],
          "Hay nho den noi ban bat dau, nhung nguoi dau tien giup ban, va tim cach tra lai dieu gi do co y nghia.",
          "Remember where you started, the first people who helped you, and find a way to give back something meaningful."),
    ])

with open(os.path.join(BASE, "ch07-biet-on.tex"), "w", encoding="utf-8") as f:
    f.write(ch7)
print("ch07 done")
