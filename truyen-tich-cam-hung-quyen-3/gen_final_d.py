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
# CHUONG 8: KHIEM TON
# ================================================================
ch8 = chapter(
    "Khiem Ton Tao Nen Vi Dai", "Humility Creates Greatness",
    "The tallest trees bow the most in storms; greatness knows when to be humble.",
    "Cay cao nhat cung coi nhieu nhat trong bao; vi dai biet khi nao can khiem ton.",
    [
    story("Tuyet Tung Cung Ra Qua Nho", "Cay Tuyet Tung",
          "D",
          [("D ai bang cao lon nhat rung, cay tuyet tung thu khong he phu bong ngan non cac cay nho.", "Though tallest in the forest, the cedar does not shade and block young trees below."),
           ("Re no toa song giup cac cay nho hut nuoc va khoang chat tu dat am bao quanh.", "Its roots spread sharing with young trees to absorb water and minerals from the surrounding moist soil."),
           ("Moi nam no cho qua nho xiu chua chac, khong sang phat rang rang nhu nhieu loai khac.", "Each year it bears tiny sour fruits, nothing flashy and dazzling like many other species."),
           ("Nhung khu rung no tao ra la noi dieu duong cua ca tram loai sinh vat khac nhau.", "But the forest it creates shelters hundreds of different species of creatures."),
           ("Vi dai that su khong can phai duoc chung kien hay ta thuong; no tu the hien qua nhung gi no tao nen.", "True greatness needs no witness or praise; it expresses itself through what it creates.")],
          "Nguoi vi dai nhat trong phong khong phai nguoi noi nhieu nhat ma nguoi de nguoi khac toa sang.",
          "The greatest person in the room is not who speaks most but who lets others shine."),

    story("Vooc Chua Phong La Gui", "Vooc Gia",
          "K",
          [("K hi vooc tre thang loi trong cuoc tu do chon lanh dao moi, vooc gia dung lai nhin.", "When a young vervet wins the contest to choose a new leader, the old one stands aside and watches."),
           ("No khong chong cu, khong tim cach quan ly bong gio; no trao quyen mot cach yen lang.", "It does not resist or seek to manage from behind the scenes; it surrenders power quietly."),
           ("Suot nhung tuan tiep theo no hoa minh vao bays, di sau gan cuoi hang de khong gay ra canh tranh.", "In the following weeks it blends into the troop, walking near the back to avoid creating competition."),
           ("Nhung con tre van tim den no khi can loi khuyen; no tra loi roi bo di khong de lai bong.", "Young ones still seek it for advice; it answers then walks away leaving no shadow."),
           ("Nghiet ngha khiem ton la cho qua va binh an khi ta con u quyen luc, khong phai khi ta bat buoc phai tu bo.", "The hardest humility is surrendering power while still possessing it, not when forced to relinquish it.")],
          "Biet lui ve de nguoi khac tien len la hanh dong vi dai hon la cu bam giu quyen luc den hoi thu cuoi cung.",
          "Knowing when to step back so others can step forward is a greater act than clinging to power until the last breath."),

    story("Chim Non Hoc Bay", "Chim Non",
          "C",
          [("C on chim non truoc khi bay lan dau dung o vach to, nhin xuong vuc sau manh dat xa.", "The young bird before its first flight stands on the nest's edge, looking down at the distant far ground."),
           ("No run ram, but lui lai, nhay len mac du co canh nhung van so hai khon ta.", "It trembles, steps back, pushes forward though having wings but still frightened beyond words."),
           ("Me chim dung phia sau, khong day manh; chi tao khong gian de no tu quyet dinh.", "The mother bird stands behind, not pushing hard; only creating space for it to decide on its own."),
           ("Khi no nhay xo tu vach to, no cam thay gio nang do cap duoi canh lan dau tien.", "When it leaps from the nest's edge, it feels the wind lifting beneath its wings for the first time."),
           ("Khiem ton la nho rang du ta co canh, lan dau bay ta van can gio cua hoan canh nang do.", "Humility is remembering that even though we have wings, the first flight still needs the wind of circumstance to lift us.")],
          "Kho khan va canh truong thanh luon di doi: khiem ton truoc canh truong la khon ngoan that su.",
          "Difficulty and growth always go together: humility before growth is true wisdom."),

    story("Cay Lua Cong Than", "Cay Lua",
          "C",
          [("C ay lua khac cay co dan biet rang hat lu nang hon tra ne cang to cang cong than.", "The rice plant unlike arrogant grass: the heavier the grain the more the stem bends."),
           ("Nong dan nhin dan lua nhin nua bong lua la biet cay nao chin tot cay nao con xanh non.", "Farmers by looking at how the rice bends know which plants are ripe and which are still young."),
           ("Cay nao than thang dung toc doc la cay con re, con xanh hoac de trong.", "Any plant with a stalk standing stiff and straight is young, immature, or has few grains."),
           ("Nhung cay gi nhe nhat la cay khinh thuong nhat; nhung cay gi nang nhat cung cong tan nhat.", "The lightest stalks are the most arrogant; the heaviest stalks bow the deepest."),
           ("Cuoc doi giong dong lua: Cang tich luy nhieu bai hoc va trai nghiem, ta cang bien ra khiem nhung hon.", "Life is like a rice field: The more lessons and experiences we accumulate, the more humble we become.")],
          "Kien thuc that su lam con nguoi khiem ton; chi co su thieu hieu biet moi khien nguoi ta kieu ngao.",
          "True knowledge makes a person humble; only lack of understanding makes people arrogant."),

    story("Nhen Co Tu Chi Viet Truyen", "Nhen Nho",
          "N",
          [("N hen nho day ra khoi bao ca vao vach nua bong toi, minh mot khong ai quan tam.", "A tiny spider climbs from mid-web onto the half-dark wall, alone with no one paying attention."),
           ("No bat dau dan to moi tu nhung cuoi chi mong manh nhat ma no co tu thanh phan than the.", "It begins weaving a new web from the finest silk threads it has from components in its own body."),
           ("Tam luoi tuyen my hinh thanh qua dem, bot suong bam doi vo dem thanh chuoi hat ngoc.", "The exquisite web forms overnight, dew drops clinging in the dark becoming a string of pearls."),
           ("Nhen khong noi rang no da tao nen tac pham sang tao; no chi tiep tuc tao va song.", "The spider does not announce it has created a masterpiece; it simply continues creating and living."),
           ("Khiem ton trong viec tao ra dieu dep tuc la lam viec vi chinh cong viec, khong vi tieng vang.", "Humility in creating beauty means working for the work itself, not for the echo of applause.")],
          "Giam tri gia cua cong viec minh lam bang viec koe hang nhu la gi to lon chang la dau; hay lam tot roi de doi noi.",
          "Do not diminish your work's value by loud boasting; do it well and let the world speak."),

    story("Ca Voi Nho Vang Tieng", "Ca Voi",
          "K",
          [("K hi ca voi lua den vung sinh san, no khong het len goi dan khong gap mat lan nhau.", "When a young whale arrives at the breeding ground, it does not shout loudly calling others before meeting anyone."),
           ("No phat ra am thanh nho, chu dong lang nghe phan hong tu ca voi khac truoc.", "It emits soft sounds, actively listening for responses from other whales first."),
           ("Chi khi am thanh no duoc tra loi ung thuan no moi phat am thanh lon hon va tro nen ro mat.", "Only when its sounds receive affirming responses does it emit louder sounds and make itself known."),
           ("He thong giao tiep nay ngan chan xung dot va dam bao noi thu nhat khong bi de doa.", "This communication system prevents conflict and ensures the newcomer is not threatened."),
           ("Den vao mit cua mot cong dong la biet lang nghe truoc roi moi noi, bat ke ban vi dai den dau.", "Entering the silence of a community means listening before speaking, no matter how great you are.")],
          "Khiem ton la lang nghe du ta biet; vi khi ta thuc su lang nghe ta se hoc duoc dieu minh CHUA biet.",
          "Humility is listening even when you already know; because when you truly listen you learn what you do NOT yet know."),

    story("Bao Chua Biet Viec Hay Khong", "Con Bao",
          "T",
          [("T ro ve trong chau Phi mot con bao khong lo, cac con thiet xau gap bao lan chau bao.", "In African leopard territory, a leopard unmatched in size compared to leopards many times smaller."),
           ("No san moi mot minh, giu xac moi tren cay cao de khong chia se voi ai khac.", "It hunts alone, keeps prey up high in trees to not share with anyone else."),
           ("Nhung mot cua khi gia hoang loai gay tro nan khong buoc duoc tren dat bang phang nua.", "But the day of old age came and it could no longer leap or walk on flat ground properly."),
           ("Khong mot con vat nao trong luc du no tung goi mai luong cuu giup; no chet don doc.", "Not one animal came when it once only would have called for food sharing; it died alone."),
           ("Su tu cach tram hoc khong chia se su giup do cuoi cung khi can cung se khong den.", "The arrogance of never sharing nor helping ultimately ensures no help will come when needed.")],
          "Khiem ton va chia se khi manh me la dau tu cho ngay ban yeu duoi va can nguoi khac.",
          "Humility and sharing when strong is an investment for the day you are weak and need others."),

    story("Trau Co Biet Co Non", "Trau Co",
          "T",
          [("T rau do rung lay mot ngon co non va non toi truoc mat no trong ngay nang nong.", "A wild buffalo spotted a tender sprout right in front of it on a hot dry day."),
           ("Thay vi an ngay, no de lai va di tim co kho va gia hon xa hoi cho cai mieng no.", "Instead of eating right away, it left it and walked to find older drier grass farther away to satisfy its hunger."),
           ("No thay rang ngon co non con nhieu co hoi lon len nhieu hon neu no de cho no song.", "It understood the young sprout had more chances to grow larger if allowed to live."),
           ("Mot con sat de lai mot ngon co non vai ngay, cho no xanh um roi moi an no.", "A few days later it returned to find the sprout fully green and lush, then it ate it."),
           ("Khiem ton cua loai an co la biet rang khong can phai an het ngay hom nay de dam bao ngay mai.", "The humility of a grazer: understanding there is no need to devour everything today to ensure tomorrow.")],
          "Khiem ton vat chat va kinh te: dung an het tat ca khi co the; hay de lai de ngay mai co cai ma an.",
          "Material and economic humility: don't consume everything when you can; leave some for tomorrow to have something to eat."),

    story("Cay Ho Phong Tran Bao Tu", "Ca Ho",
          "T",
          [("T rong mua sinh san, ca ho duc doc dao va long lay de thu hut ca ho cai bang mau sac ruc ro.", "During mating season, male peacock wrasse dives deep and glows to attract females with brilliant colors."),
           ("Nhung khi nguoi san bat den, mau sac ruc ro nay tro thanh su dich chuyen nguy hiem.", "But when hunters come, these brilliant colors become a dangerous billboard."),
           ("Ca ho duc hoc duoc cach tat mau den tuc thi khi cam nhan moi nguy hiem xung quanh.", "The male wrasse learned to instantly darken its colors when sensing any nearby danger."),
           ("Biet tat di su noi bat khi hoan canh doi hoi la dang khiem ton linh hoat bac nhat.", "Knowing how to dim your prominence when circumstances demand it is the highest form of flexible humility."),
           ("Khong phai luc nao ta cung can phu truong; biet khi nao im lang cung la tri tue.", "Not every moment requires display; knowing when to be quiet is also wisdom.")],
          "Lanh dao thong minh biet luc nao nen sang tao noi bat va luc nao nen hoa minh vao nen de bao toan.",
          "The smart leader knows when to stand out brilliantly and when to blend into the background for safety."),

    story("Khi Co Bau Nhuong Thuc An", "Khi",
          "K",
          [("K hi co khi cai mang bau trong bays khi, cac con duc tim kiem va mang lai nhieu thuc an nhat.", "When a female monkey in the troop is pregnant, the males seek and bring the most food."),
           ("Khi co bau an truoc, cac con khac doi cho du chung cung dang doi va thieu nguon an.", "The pregnant female eats first, others wait even though they too are hungry and food is scarce."),
           ("Day khong phai cam thay vui ve boi cam giac doi; day la lua chon khiem ton truoc su suu tam thuyet.", "This is not a pleasant feeling from hunger; it is the humble choice before the survival of the species."),
           ("Su to truong cua loai duoc dat len tren su tiet hanh riet cua ca nhan; do la tri tue tap the.", "The growth of the species is placed above individual gratification; that is collective wisdom."),
           ("Nhung xa hoi manh nhat la nhung xa hoi biet nhuong truoc cho nguoi de bi ton thuong nhat.", "The strongest societies are those that know to yield first for their most vulnerable members.")],
          "Khiem ton don gian la biet rang ban khong phai trung tam vu tru; co nguoi xung dang duoc uu tien hon.",
          "Humility is simply knowing you are not the center of the universe; someone else deserves priority more.")
    ])

with open(os.path.join(BASE, "ch08-khiem-ton.tex"), "w", encoding="utf-8") as f:
    f.write(ch8)
print("ch08 done")

# ================================================================
# CHUONG 9: TRACH NHIEM
# ================================================================
ch9 = chapter(
    "Trach Nhiem Voi Cuoc Song", "Responsibility for Life",
    "The price of greatness is responsibility; own your choices, own your life.",
    "Gia cua su vi dai la trach nhiem; hay so huu qua quyet dinh, so huu cuoc doi.",
    [
    story("Soi Bao Ve Lanh Dia", "Con Soi",
          "B",
          [("B ay soi co lanh dia va chung bao ve no khoi cac bay soi khac hoat dong xam pham.", "A wolf pack has territory and they protect it from other wolf packs infringing."),
           ("Nhung khi chung san qua muc, lanh dia suy kiet, bay soi nhan ra va tu han che san.", "But when they over-hunt, territory depletes, the pack notices and self-limits hunting voluntarily."),
           ("Khong co nha nuoc nao bat chung; chinh ban nang va tri nho tap the thuc day.", "No state forces them; their own instinct and collective memory drives this."),
           ("Khi deer population tang lai, bay soi dan dan mo rong sang muc do hop ly de tiep tuc.", "When deer populations recover, the pack gradually expands hunting to reasonable levels again."),
           ("Trach nhiem voi lanh dia va nguon thuc pham la su song con co the duy tri lau dai.", "Responsibility for territory and food sources is how survival can be maintained for the long term.")],
          "Bao nhieu ban co the lay tu moi truong va bao nhieu ban se de lai cho tuong lai la cau hoi cua trach nhiem.",
          "How much you take from an environment and how much you leave for the future is the question of responsibility."),

    story("Ong Chua Dieu Phoi Dan Ong", "Ong Chua",
          "O",
          [("O ng chua khong pha di sang de ngu hay nghi ngoi; ngoai viec san xuat trung nghia vu cua no ro rang.", "The queen bee does not wander outside to sleep or rest; besides laying eggs her duty is clear."),
           ("San xuat den 2000 trung moi ngay suot bai muoi ngay song, con thang, ngay nay qua ngay khac.", "Laying up to 2000 eggs per day throughout her sixty-day lifespan, month after month, day after day."),
           ("Neu ba ngung mot ngay, ca dan ong mat track phat trien dan so va co the suy sup trong vai thang.", "If she stops even one day, the whole colony loses population growth track and may collapse in months."),
           ("Ba khong bao gio can ai nhac nho bong bo; trach nhiem cua ba la ban nang cot loi.", "She never needs anyone reminding her; her responsibility is her core instinct."),
           ("Nguoi lanh dao khong can nhac nho moi lam viec; viec lam viec la chinh ho, khong can ung thuan.", "A leader doesn't need reminders to work; working IS who they are, requiring no encouragement.")],
          "Trach nhiem cao nhat la khi ban lam viec vi tinh chat cong viec chinh no chu khong vi phan thuong hay gio giac.",
          "The highest responsibility is when you work because of the very nature of the work, not for reward or schedule."),

    story("Ca He Bao Ve San Ho", "Ca He",
          "C",
          [("C a he nho bi nhan nhang soi bong den tren rao san ho noi no sinh song va con cai.", "The small clownfish is seen patrolling the sea anemone area where it lives and raises its young."),
           ("No cham soc kem thuc an cho so goi bien de giu suc khoe khoang san ho.", "It brings food to the sea anemone to maintain health of the coral neighborhood."),
           ("No se tan cong bat ky con ca nao lon hon no gan 20 lan ma dam den lau vung tam cua no.", "It will attack any fish up to 20 times its size that dares to come near its protected zone."),
           ("No chi co mot cai ngoi, mot cai khu vuc trach nhiem, va no bien no thanh ca mot the gioi de bao ve.", "It has only one home, one area of responsibility, and it turns it into an entire world worth protecting."),
           ("Trach nhiem khong nhat thiet phai lon moi co y nghia; bao ve tot nhung gi nho nhat cung la vi dai.", "Responsibility need not be large to be meaningful; protecting well the smallest things is also greatness.")],
          "Hay nhan trach nhiem voi moi truong nho cua ban truoc; khi ban lam tot do, ban moi co the mo rong.",
          "Take responsibility for your small environment first; when you do that well, you can expand."),

    story("Voi Nho De Lai Canh Dong", "Bay Voi",
          "K",
          [("K hi bay voi di qua canh rung, chung de lai nhung khoang trong boi voi o la cac cay xa.", "When elephant herds pass through a forest, they leave open spaces from pulling out trees for food."),
           ("Nhung khoang trong nay cho anh sang vao dat de hat giong nay mam va cac loai co thi de bay.", "These open spaces let sunlight reach the soil for seeds to sprout and short-grass species to seed."),
           ("Que chim kien va soc co dan theo vao o trong khoang trong do va bat dau tao nen he sinh thai rieng.", "Bird, ant and squirrel colonies follow into those clearings and begin forming their own ecosystem."),
           ("Sac de lai tren canh rung cua bay voi khong phai tan pha ma la tai tao da dang sinh hoc.", "Marks left on the forest by elephant herds are not destruction but biodiversity recreation."),
           ("Trach nhiem voi moi truong doi khi co nghia la tao ra nhung thay doi co chon ve vi long tot.", "Responsibility to the environment sometimes means creating intentional changes for the greater good.")],
          "Trach nhiem voi the gioi tu nhien la hieu rang tac dong cua ta co the la qua tang hoac la chan thuong.",
          "Responsibility to the natural world is understanding that our impact can be either a gift or an injury."),

    story("Nhay San Lac Khong Ro Nguoi", "Nhay San",
          "M",
          [("M ot loai nhay san kinh nghiem biet rang mot khi da bat dau tan cong phuc kich thi phai hoan thanh.", "An experienced jumping spider knows that once a pounce attack begins it must be completed."),
           ("Dung lai giua chung chac chan se giup con moi thoat va tiep lat net mang nhot lua che ban than.", "Stopping midway would certainly let the prey escape and expose its web-concealment camouflage."),
           ("No la luon chiu het hau qua cua quyet dinh tan cong du co vang hay thua cuoc.", "It always bears the full consequences of the attack decision whether winning or losing."),
           ("Khong co chuyen nhay san dat len nua roi lui lai vi so mat mat chac tu moi truong khac.", "There is no such thing as a jumping spider beginning its leap then retreating out of fear of loss."),
           ("Trach nhiem la biet rang moi quyet dinh den hau qua va ta can san sang chiu hau qua do.", "Responsibility is knowing every decision has consequences and we must be ready to bear those consequences.")],
          "Truoc khi do quyet dinh, hay suy nghi ky; nhung sau khi da quyet dinh, hay chiu trach nhiem den cung.",
          "Before making a decision, think carefully; but once decided, bear responsibility to the very end."),

    story("Rat Binh Dan Giua Bieu Ro", "Con Rat",
          "T",
          [("T rong nghien cuu noi tieng, con rat duoc dat trong hop co nut bam giai phong dong loai bi chum.", "In a famous study, a rat was placed in a box with a button that released a caged companion."),
           ("Con rat khong huong loi gi tu viec nhan ban nhu; no chi nhan ban boi no cam thay phai lam.", "The rat gained nothing from pressing the button; it only pressed because it felt it had to."),
           ("Chay qua den phan thuong thuc an de nhan ban truoc, roi moi an thuc an sau khi ban da tu do.", "It ran past food rewards to press the release first, then ate food after its companion was free."),
           ("Nhieu con rat con chia phan thuc an cua minh cho dong loai vua duoc giai thoat ra.", "Many rats even shared their own food portions with the companion just freed."),
           ("Trach nhiem voi dong loai, su dong cam, khong phai chi la cua con nguoi; no la dieu toan cau.", "Responsibility to fellow creatures, empathy, is not uniquely human; it is universal.")],
          "Neu con rat biet trach nhiem voi dong loai thi con nguoi cang phai biet hon the rat nhieu.",
          "If a rat knows responsibility to its kind then humans certainly must know it far more."),

    story("Ca Ham Co Den Lap Lua Cho Dan", "Ca Ham",
          "C",
          [("C a ham co den dung kha nang phat sang cua minh de dan dan ca nho theo sau.", "Anglerfish use their bioluminescence ability to lead small fish to follow behind."),
           ("Cac loai ca phiep tang theo lan anh sang de di theo cuoi cung bi an truoc khi hieu ra be.","Naive fish are drawn to follow the light ultimately being eaten before realizing the trap."),
           ("Nhung mot so nha nghien cuu tim thay loai ca co den cung dung den trong muc dich cung sinh.", "But some researchers found anglerfish also use their light for mutualistic purposes."),
           ("Trong vung nuoc toi den cach bo bien 2000 met, hau nhu khong co loai nao tu lam den.", "In pitch-dark zones 2,000 meters from shore almost no species can produce their own light."),
           ("Trach nhiem cua nguoi co tai nang rieng biet la su dung tai nang do cho dieu lon lao hơn luoi ich ca nhan.", "The responsibility of one with a unique gift is to use that gift for something greater than personal gain.")],
          "Bat ky tai nang gi ban co cung dua theo trach nhiem su dung no mot cach co ich cho nguoi khac.",
          "Whatever talent you possess carries the responsibility of using it usefully for others."),

    story("Khi Di Cung Voi Con Gia Benh", "Con Khi",
          "K",
          [("K hi nghien cuu quan sat mot con khi gia bi gai tre be nan di cham, bay khi van di cung toc do do.", "When researchers observed an elderly monkey with a bamboo splinter injury walking slowly, the whole troop walked at its pace."),
           ("Bay khi hoan toan co kha nang bo sung song truoc nhung khong con nao lam vay.", "The troop was fully capable of leaving the injured one behind but not one did so."),
           ("Nhung con khoe manh khi phuc ben nguoi yeu, quan sat, san sang can thiep khi can.", "The healthy ones watched beside the weaker one, observing, ready to intervene when needed."),
           ("Khi khi gia chet di, ca bay ngoi im lang ben xac no trong vai gio truoc khi di.", "When the old monkey died, the whole troop sat quietly beside the body for hours before leaving."),
           ("Trach nhiem voi nguoi yeu duoi khong bao gio la ganh nang; do la dieu co nghia la cuoc doi.", "Responsibility for the weaker is never a burden; it is what gives life meaning.")],
          "Toc do cua mot nhom duoc do bang toc do cham nhat cua ho; dung bo roi nguoi chay cham nhat.",
          "A group's speed is measured by the speed of its slowest member; never leave behind the slowest runner."),

    story("Ran Hoi Khong Can Nhan Nhung Khong Het", "Ran Hoi",
          "K",
          [("K hi ran hoi cat vao con moi, no khong pha co doc toi da ngay ca khi co the lam vay.", "When a king cobra bites prey, it does not inject maximum venom even when it could."),
           ("Cac nghien cuu ghi nhan con ran luon dieu chinh lieu luong doc phu hop voi kich co moi.", "Studies record that the snake always calibrates venom dosage appropriate to the prey's size."),
           ("Dieu nay bao ton nguon co doc quy gia de su dung khi thuc su can biet trong tuong lai.", "This conserves the precious venom supply for truly necessary future use."),
           ("No khong lang phi suc manh; no su dung dung du suc manh can thiet va khong hon nua.", "It does not waste strength; it uses exactly the strength needed and no more."),
           ("Trach nhiem voi suc manh minh co la khong su dung qua muc can thiet bao gio.", "Responsibility with the power you possess means never using more than what is needed.")],
          "Nguoi manh trach nhiem nhat su dung it suc manh nhat; ho biet rang quyen luc lon nen duoc su dung can than.",
          "The most responsible powerful person uses the least power; they know great power should be used sparingly."),

    story("Dan Ca Bao Ve Bien", "Dan Ca Nho",
          "N",
          [("N hieu dan toc bien di bien bao nhieu doi van giu nguyen suc song phong khoang cua nguon ca.", "Many coastal communities have fished the sea for generations yet kept the fish populations thriving."),
           ("Ho co luat khong thanh van: khong san mua ca de, khong san ca con, khong dan pha rao san ho.", "They have unwritten laws: no fishing in spawning season, no catching juvenile fish, no dragging over coral reefs."),
           ("Luat nay khong den tu khoa hoc hai duong hoc; no den tu tri tue dieu nhai qua hang tram nam.", "These laws did not come from marine science; they came from fine-tuned wisdom across hundreds of years."),
           ("Moi nguoi dan bien biet rang neu ho lay qua nhieu hom nay, con cai ho se doi kho ngay mai.", "Every fisherman knows that if they take too much today, their children will go hungry tomorrow."),
           ("Trach nhiem voi nguon tai nguyen la loai tri tue lau doi nhat va quan trong nhat tren hanh tinh.", "Responsibility for natural resources is the oldest and most important wisdom on the planet.")],
          "Hay nghi den nhung nguoi chua sinh ra khi ban dua ra quyet dinh ve tai nguyen ngay hom nay.",
          "Think of the unborn when making decisions about resources today."),
    ])

with open(os.path.join(BASE, "ch09-trach-nhiem.tex"), "w", encoding="utf-8") as f:
    f.write(ch9)
print("ch09 done")

# ================================================================
# CHUONG 10: HY VONG
# ================================================================
ch10 = chapter(
    "Hy Vong Thap Sang Con Duong", "Hope Lights the Path",
    "Hope is the thing with feathers that perches in the soul and sings the tune without the words.",
    "Hy vong la chiec long chim dau trong linh hon va hat khuc ca khong loi.",
    [
    story("Chim Phuong Hoang Tai Sinh", "Phung Hoang",
          "T",
          [("T rong truyen thuyet, phung hoang song 500 nam roi tu thieu minh trong ngon lua cua chinh minh.", "In legend, the phoenix lives 500 years then burns itself in its own flames."),
           ("Tu dong tro tan no tai sinh, lon hon sa hon dep hon truoc va vui ve hon.", "From the ashes it is reborn, larger, more beautiful, more radiant, and more joyful than before."),
           ("Y nghia cua phung hoang khong phai phep mau ma la su that rang sau moi ket thuc co mot bat dau.", "The phoenix's meaning is not magic but the truth that after every ending comes a beginning."),
           ("Nhieu nen van hoa khac nhau tren the gioi deu co huyen thoai ve sinh vat tai sinh tu tro tan.", "Many different cultures around the world have legends about creatures reborn from ashes."),
           ("Nhan loai can hy vong nay; no la ban nang sinh ton cuoi cung khi tat ca phuong an khac deu dung.", "Humanity needs this hope; it is the final survival instinct when all other options have failed.")],
          "Moi ket thuc trong cuoc doi ban deu la co hoi tro lai moi hon; dung goc nhin la mat mat, hay goc nhin la tai sinh.",
          "Every ending in your life is an opportunity to return renewed; don't see it as loss, see it as rebirth."),

    story("Hat Giong Qua Mua Dong", "Hat Giong",
          "N",
          [("N am ngoai mua nan ha khoc liet hat giong corn cat xuong dat kho nut nut song voi hy vong.", "Last year in the harsh drought season corn seeds fall into cracked dry soil and wait with hope."),
           ("Khong ai bao dam rang mua se roi; khong ai hua rang dat se am; nhung hat giong van chon minh xuong.", "No one guarantees rain will come; no one promises the soil will warm; but the seed still buries itself below."),
           ("Trong bong toi cua long dat, hat giong co cau truc phuc tap bao ve noi tang su song.", "In the darkness of the earth's interior, the seed has complex structures protecting its inner life."),
           ("Khi mua lui cham xuong chay vao dat, hat giong khong phoi hop bang ky thuat; no chi mo ra vi no nho.", "When rain slowly seeps into soil, the seed does not coordinate by technique; it simply opens because it remembers."),
           ("Hy vong sinh hoc la tri nho co dieu kien hoa: khi dieu kien du, su song nop lai.", "Biological hope is conditioned memory: when conditions are sufficient, life resumes.")],
          "Hy vong khong phai mo ho; no la nang luc chuan bi tai nguyen sinh luc o the tinh de cho dieu kien thich hop.",
          "Hope is not wishful thinking; it is the capacity to store vital energy in dormancy waiting for the right conditions."),

    story("Ca Heo Khong Bao Gio Tu Bo Hung", "Ca Heo",
          "K",
          [("K hi ca heo bi thung luoi va mat trang, no khong nam chet o may no trong nuoc sau mot minh.", "When a dolphin is net-wounded and loses its pod, it does not lie dying in deep water alone."),
           ("No boi den vung bien nong hon, de lai song, hoi phuc dan dan trong nhieu tuan.", "It swims to warmer shallower waters, stays alive, recovering gradually over many weeks."),
           ("Ca heo bi thuong thuong tim den cac tau thuyen cua nguoi, keu la nhu tim kiem su giup do.", "Injured dolphins often find human boats, crying out as if seeking help."),
           ("Nhieu truong hop ghi nhan ca heo duoc dua len bo, cham soc, roi thuc su boi ra bien lai.", "Many recorded cases of dolphins being lifted ashore, cared for, and truly swimming back to sea."),
           ("Hy vong khong phai tu nhien xuat hien; no la quyet dinh tich cuc di tim noi co anh sang.", "Hope does not appear naturally; it is the active decision to move toward where there is light.")],
          "Khi bi thuong, hay boi den tai nguoi co the giup ban; xin giup do khong phai yeu duoi ma la khon ngoan.",
          "When wounded, swim toward those who can help you; asking for help is not weakness but wisdom."),

    story("Chim Non Lan Dau Mo Mat", "Chim Non",
          "T",
          [("T rong bong toi cua cai trung, chim non khong biet anh sang la gi ngoai soi am nhe qua vo.", "In the darkness of the egg the young bird does not know what light is except a faint warmth through the shell."),
           ("No dung mo be vo, mot cai go nho be, lien tuc, mot each kien tri uong tranh.", "It uses its beak to break the shell, one small tap, continuously, stubbornly against heavy resistance."),
           ("Khi vo trung nut no va anh sang lan dau tien tran vao, no la gi hinh anh dau tien no thay.", "When the shell cracks open and light floods in for the first time, that is the first image it ever sees."),
           ("Tu giay phut do, no bien anh sang la nha, la noi thuoc ve, la thu no luon huong ve.", "From that moment, it makes light its home, its sense of belonging, what it always moves toward."),
           ("Hy vong la khi con vat trong bong toi van goc go ve phia anh sang ma no chua bao gio thay.", "Hope is when a creature in darkness still chips toward the light it has never yet seen.")],
          "Hay tin rang anh sang o phia kia cua bong toi ban dang o trong; no tan tai du ban chua thay duoc.",
          "Trust that light is on the other side of the darkness you are in; it exists even if you cannot yet see it."),

    story("Xa Thanh Vuon Tren Vet Nuoc Kham Pha", "Cay Nao",
          "T",
          [("T o cay nao oc tren toan bo hanh tinh moi sang den nao phat ra tin hieu ky vong va mo ngu.", "The brains of all mammals on the entire planet fire signals of anticipation and dreaming every night."),
           ("Chim va ca trong giac ngu thuc hien lai hanh trinh truoc thi hay chac van dang hoc moi.", "Birds and fish during sleep replay journeys practiced or skills currently being learned."),
           ("Nao tao ra ban nha cua nhung gi se xay ra truoc, mo phong kha nang thu quan trong lieu truoc.", "The brain creates a map of what will happen next, simulating possibilities to test-run important scenarios."),
           ("Hy vong la chuc nang than kinh hoc: nao tao ra tuong lai truoc roi moi goi no lam xuat hien.", "Hope is a neurological function: the brain creates the future first and then calls it into appearance."),
           ("Nhung sinh vat biet mo ve tuong lai tot hon se song sot tot hon nhung con khong biet mo.", "Creatures that dream of a better future survive better than those that cannot dream.")],
          "Mong uoc khong phai lu an; do la he thong tien ich cua nao de tu tao cuoc song tot hon cho ban.",
          "Dreaming is not foolishness; it is the brain's advance-planning system for creating a better life for you."),

    story("Ran Mo Truoc Khi Lay Lan Da Moi", "Con Ran",
          "L",
          [("L uc dau con ran khong the lay duoc lan da moi mot minh co mot minh; no can mat ngoai ma suu.", "First the snake cannot shed its old skin alone; it needs an external abrasive surface."),
           ("No tim mot viha da rao nham, cham mam phia truoc vai ngay truoc va bat dau co day thu.", "It finds a rough rocky surface, rubbing its snout for days in advance and begins slowly pushing through."),
           ("Lan da cu tu tach ra tu phia dau, la nguyen ca mot cai ao cu bi tut nguoc ra ngoai hon.", "The old skin peels back from the head, the entire old shell turned inside out."),
           ("Duoi lop da cu la lan da moi sang bong hoan toan, sac net va tre hon hon truoc.", "Under the old skin is perfectly bright new skin, vibrant and younger-looking than before."),
           ("Hy vong dat cu ve nhung thay doi lon luon bat dau bang viec cho phep buong bo nhung gi da cu khong con phu hop.", "Hope for great changes always begins with allowing yourself to let go of what no longer fits.")],
          "Truoc khi than hinh moi xuat hien, lai da cu phai duoc boc dit ra; dung so viec tu bo thu cu.",
          "For the new form to emerge, the old skin must be shed completely; don't fear discarding old things."),

    story("Rung Chay Hoi Sinh Sau Bao Lua", "Rung Sau Bao Lua",
          "N",
          [("N am 1988 bao lua quet qua 36 phan tram Vuon Quoc Gia Yellowstone that tan tro than.", "In 1988 wildfire swept through 36 percent of Yellowstone National Park, burning everything to ash."),
           ("Mua xuan nam sau, trong dam tro den, hang tram ngan mam cay moc khap noi ta goi la may man.", "The following spring in the black ash bed, hundreds of thousands of sprouts grew everywhere what we call miraculous."),
           ("Lua da mo ra dat, diet sau benh va thuc day hat trong cac loai cay co ham het dau.", "The fire opened the soil, killed pests, and stimulated dormant seeds of serotinous species to germinate."),
           ("Nam muoi sau tran bao lua, Yellowstone co da dang sinh hoc cao hon bat ky thoi diem nao truoc do.", "Fifty years after the wildfire, Yellowstone has higher biodiversity than at any time before."),
           ("Tran bao lua khoc liet nhat van de lai hy vong; no chi la hy vong minh chia khong giong nhu da nghi.", "The fiercest wildfire still leaves hope; it is just hope manifesting differently than imagined.")],
          "Bao gi ban cung co the tim ra dat moi de trong sau bao lua; cuoc song luon tim duong de hoi sinh.",
          "You can always find new soil to plant in after a wildfire; life always finds its way to regenerate."),

    story("Buom Khong Biet Mau Cua Chinh Minh", "Con Buom",
          "N",
          [("N hieu loai buom co mau sac dep tren canh nhung chinh mat no chua bao gio nhin thay mau do.", "Many butterflies have beautiful color patterns on wings but their own eyes have never seen those colors."),
           ("Canh buom duoc tao ra cho su thu nhan cua mat ke khac, khong phai cua minh.", "Butterfly wings are made for the perception of others' eyes, not one's own."),
           ("Dep cua buom la de thu hut ban doi, de canh bao ke thu, de hoa vao hoa loi.", "A butterfly's beauty serves to attract mates, warn enemies, blend into flower benefits."),
           ("No khong can biet minh dep; viec no phat huy ve dep cua minh da mang lai y nghia roi.", "It need not know it is beautiful; the very act of expressing its beauty already brings meaning."),
           ("Doi khi ly do de song khong phai vi ban thay ban dep; ma vi cuoc song dung ban de dep hon.", "Sometimes the reason to live is not because you see yourself as beautiful, but because life needs you to make it more beautiful.")],
          "Ban ton tai de them y nghia vao cuoc song xung quanh ban; du ban co nhan ra hay khong, that su ban.",
          "You exist to add meaning to the life around you; whether you realize it or not, that is true."),

    story("Nha Du Hanh Vu Tru Nhin Trai Dat", "Phi Hanh Gia",
          "N",
          [("N hiing phi hanh gia dau tien nhin Trai Dat tu vu tru mo ta lanh nuoc mat khong the cap duoc.", "The first astronauts looking at Earth from space describe an indescribable chill of tears coming on."),
           ("Ho thay mot qua cau xanh mong manh bao boc boi lop khi quyen mong te de bi.", "They see a fragile blue sphere wrapped in an achingly thin and easily destroyed atmosphere."),
           ("Khong co duong vach quoc gia, khong co gianh gioi dia ly, chi co mot Trai Dat thong nhat.", "No national boundary lines, no geographic borders, only one united Earth."),
           ("Tu tren do ho hieu tai sao chien tranh la phi ly va tai sao bao ve hanh tinh la thien nhiem.", "From up there they understand why war is irrational and why protecting the planet is a sacred mission."),
           ("Hy vong vi dat la khi chung ta du can dam nhin dat tu xu xa de thay ro rang gia tri cua no.", "Hope for the Earth is when we have enough courage to look at it from far away to see its value clearly.")],
          "Hay nhin ban be, gia dinh va cong dong ban tu mot goc nhin xa hoi hon; ban se thay tat ca dang quy biet bao.",
          "Look at your friends, family, and community from a higher perspective; you will see how precious everything is."),

    story("Hoa Bun Sen", "Hoa Sen",
          "G",
          [("G iua dam li bun hoi thoi tanh tuu, hat sen nam duoi lay nguon duong chat tu bun de song.", "In a foul-smelling swamp, the lotus seed lies below drawing nutrients from the mud to survive."),
           ("Cuong hoa vuon thang len qua meters nuoc toi de tim anh mat troi tren mat nuoc.", "The flower stem stretches straight up through meters of dark water to find sunlight on the surface."),
           ("Khi hoa no tren mat nuoc, canh hoa trang tinh khiet khong mot vet bun nao bam lai.", "When it blooms on the water's surface, the pure white petals carry not a single trace of mud."),
           ("Hoa sen biet mot bi mat lon: ta co the truong thanh tu vung bun ma khong can mang bun len.", "The lotus knows one great secret: one can grow from muddy origins without carrying the mud upward."),
           ("Moi nguoi deu co kha nang tro thanh hoa sen: born in mud, bloom in sunlight, remain pure.", "Every person has the capacity to become a lotus flower: born in mud, bloom in sunlight, remain pure.")],
          "Nguon goc khiem ton hay kho khan cua ban khong dinh hinh tuong lai ban; no chi la dat de ban vu ong.",
          "Your humble or difficult origin does not define your future; it is only the soil from which you bloom."),
    ])

with open(os.path.join(BASE, "ch10-hy-vong.tex"), "w", encoding="utf-8") as f:
    f.write(ch10)
print("ch10 done")
print("ALL CHAPTERS DONE!")
