# -*- coding: utf-8 -*-
"""Gen chapters 1-3 for Quyen IV: Triet Ly Nhan Sinh"""
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
# CHUONG 1: KHOAN DUNG
# ================================================================
ch1 = chapter(
    "Khoan Dung --- Suc Manh Cua Su Tha Thu", "Forgiveness --- The Greatest Power",
    "Tha thu khong phai la yeu duoi; do la long can dam cua nguoi manh.",
    "Forgiveness is not weakness; it is the courage of the strong.",
    [
    story("Lincoln Va Ke Thu Chinh Tri", "Lincoln --- Hoa Ky 1860",
          "A",
          [("A braham Lincoln sau khi dac cu Tong Thong da lam dieu ma ca nuoc My khong ai ngo toi.", "Abraham Lincoln, after winning the presidency, did something no one in America expected."),
           ("Ong bo nhiem Edwin Stanton --- nguoi da cong khai che gieu ong la 'con khi tu Illinois' --- vao chuc Bo truong Chien tranh.", "He appointed Edwin Stanton --- who had publicly mocked him as 'the gorilla from Illinois' --- as Secretary of War."),
           ("Cac cong su kinh ngac hoi tai sao; Lincoln tra loi that gian di: 'Ong ta la nguoi gioi nhat cho vi tri nay.'", "His aides were stunned and asked why; Lincoln replied simply: 'He is the best man for the position.'"),
           ("Stanton, duoc trong nha nhu vay, tro thanh Bo truong tan tuy nhat trong lich su nuoc My.", "Stanton, treated with such respect, became the most dedicated Secretary in American history."),
           ("Khi Lincoln bi am sat, chinh Stanton la nguoi khoc va noi: 'Day la nguoi vi dai nhat toi tung biet.'", "When Lincoln was assassinated, it was Stanton who wept and said: 'He is the greatest man I have ever known.'")],
          "Tha thu ke thu va trao ho co hoi la cach bien ke thu thanh dong minh --- va viet nen lich su.",
          "Forgiving an enemy and giving them a chance is how you transform foes into allies --- and make history."),

    story("Mandela Ra Tu Khong Cam Thu", "Nelson Mandela --- Nam Phi 1990",
          "S",
          [("S au 27 nam bi giam can trong nha tu Robben Island vi dau tranh chong phan biet chung toc, Nelson Mandela buoc ra tu.", "After 27 years imprisoned in Robben Island for fighting apartheid, Nelson Mandela walked free."),
           ("Phong vien hoi ong co cam thu nhung ke da giam cam ong suot gan ba muoi nam khong.", "A reporter asked if he hated those who had imprisoned him for nearly thirty years."),
           ("Mandela tra loi: 'Neu toi buoc ra kia voi long cam thu, toi se van con la tu nhan, du ma cua tu da mo tra.'", "Mandela answered: 'If I walked out there with hatred, I would still be a prisoner, even if the prison door had opened.'"),
           ("Ong khong chi tha thu --- ong moi nguoi canh sat tung giam giu ong den du le nhau chuc tong thong.", "He didn't just forgive --- he invited the guard who had once imprisoned him to attend his presidential inauguration."),
           ("Nam Phi thoat khoi vung xoay bao luc nho chinh su khoan dung phi thuong do cua Mandela.", "South Africa escaped a cycle of violence largely because of Mandela's extraordinary forgiveness.")],
          "Long cam thu chi giam cam ban trong bung; su tha thu giai phong chinh ban truoc khi giai phong ke thu.",
          "Hatred imprisons you inside yourself; forgiveness liberates you before it liberates your enemy."),

    story("Khong Tu Tha Hoc Tro Phan Boi", "Khong Tu --- Trung Quoc TK 5 TCN",
          "M",
          [("M ot hoc tro cua Khong Tu da cong khai bat vua dung loi khuyen cua su phu de kiem loi ca nhan.", "A student of Confucius openly urged a lord to use the master's advice for personal gain."),
           ("Cac mon sinh khac yeu cau Khong Tu duoi hoc tro nay di; nha trien hoc im lang hoi tham.", "Other disciples demanded Confucius expel the student; the philosopher calmly asked questions first."),
           ("Nghe cau tra loi, Khong Tu noi: 'Nguoi ay chua hieu dao; day la loi ta, khong phai loi nguoi ay.'", "After hearing the answer, Confucius said: 'He has not understood the Way yet; that is my fault, not his.'"),
           ("Ong tiep tuc day hoc tro do them ba nam cho den khi nguoi nay that su hieu va thay doi.", "He continued teaching that student for three more years until the person truly understood and changed."),
           ("Hoc tro nay ve sau tro thanh mot trong nhung quan chuc cong bang nhat cua thoi dai do.", "That student later became one of the most just officials of that era.")],
          "Nguoi phan boi ban thuong la nguoi chu truoc day ban da khong day du; hay nhan trach nhiem truoc khi phan xet.",
          "Someone who betrays you is often someone you didn't teach enough before; take responsibility before judging."),

    story("Vua Ly Thai To Tha Ke Thu Cu", "Ly Thai To --- Viet Nam 1010",
          "K",
          [("K hi Ly Cong Uan len ngoi thanh lap vuong trieu Ly, nhieu ke tung chong doi ong van con song.", "When Ly Cong Uan ascended the throne and founded the Ly Dynasty, many who had opposed him still lived."),
           ("Cac quan de nghi truy sat de tru hau hoa; nha vua im lang truoc roi quay sang van de khac.", "Officials proposed hunting them down to prevent future threats; the king fell silent then turned to other matters."),
           ("Cuoi nam do, ong ban chinh sach an xa rong rai --- tha tat ca toi pham chinh tri va moi nguoi tro ve.", "That year's end, he announced a broad amnesty --- pardoning all political offenders and welcoming all to return."),
           ("Mot vi quan co cu tra lai va phuc vu Ly Thai To trung thanh den cuoi doi, lam nen nhieu cong tich.", "A former official returned and served Ly Thai To faithfully for life, accomplishing many great things."),
           ("Trieu dai Ly ke sang mot trong nhung giai doan hung cuong nhat lich su Viet Nam.", "The Ly Dynasty went on to become one of the most prosperous periods in Vietnamese history.")],
          "Bau du khoan dung bao gio cung tao ra mot dat nuoc manh hon la bau du nuoc mat va thu han sinh ra.",
          "Sowing forgiveness always creates a stronger nation than sowing resentment and hatred."),

    story("Corrie Ten Boom Tha Ten Linh Duc", "Corrie ten Boom --- Duc 1947",
          "S",
          [("S au Chien tranh The gioi II, Corrie ten Boom--- nguoi phu nu Ha Lan da song sot sau trai tap trung --- den Duc de giang ve su tha thu.", "After World War II, Corrie ten Boom --- a Dutch woman who survived the concentration camps --- came to Germany to speak about forgiveness."),
           ("Sau bai giang, mot nguoi dan ong buoc den bat tay ba; Corrie nhan ra day chinh la ten linh da bao hanh ba trong trai.", "After the lecture, a man approached to shake her hand; Corrie recognized him as the very guard who had brutalized her in the camp."),
           ("Tim ba dong cung, tay ba khong muon dua ra, nhung ba van cu cau nguyen va dua tay biet ra.", "Her heart froze and her hand refused to move, but she prayed and slowly extended her hand anyway."),
           ("Ngay khi tay ba cham vao tay ong, ba cam nhan su binh an tuon chay qua nguoi nhu mot dong dien.", "The moment her hand touched his, she felt peace flowing through her like an electric current."),
           ("Ba viet lai: 'Tinh yeu la thu manh me hon bat ky cam xuc nao khac --- va su tha thu la co the chon lua.'", "She wrote: 'Love is stronger than any feeling --- and forgiveness is a choice that can be made.'")],
          "Su tha thu chua lan luot ca nguoi tha thu lan nguoi duoc tha; no an me boi vung tuong gan nang ne nhat.",
          "Forgiveness heals both the one who forgives and the one forgiven; it opens the heaviest gates."),

    story("Gandhi Va Nguoi Linh Bao Hanh", "Mahatma Gandhi --- An Do 1922",
          "N",
          [("N am 1922, Gandhi bi bat giam va bi dua ra toa vi toi xui gio cuoc noi loan chong thuc dan Anh.", "In 1922, Gandhi was arrested and brought to trial for the charge of inciting rebellion against British rule."),
           ("Thay quan toa - mot nguoi Anh ten Broomfield --- nói rang ong rat kho xu voi truong hop nay.", "The judge --- an Englishman named Broomfield --- said he found this case deeply difficult to handle."),
           ("Broomfield noi: 'Neu phap luat cho toi, toi se tha ong di; nhung luat phap bat toi phai xu ong.'", "Broomfield said: 'If the law allowed me, I would set you free; but the law requires me to sentence you.'"),
           ("Gandhi mim cuoi dap: 'Thua quy toa, toi biet quy toa da lam tat ca nhung gi quy toa co the lam.'", "Gandhi smiled and replied: 'Your Honor, I know you have done everything within your power.'"),
           ("Chinh su khoan dung lan nhin nhan su khoan dung do da lam mem long nhieu nguoi Anh hon bat ky cuoc bieu tinh nao.", "That mutual recognition of respect moved more English hearts than any protest march ever had.")],
          "Khoan dung voi ke đang bat minh la hanh dong manh me nhat co the thuc hien truoc mat mot the gioi dang nhin.",
          "Being gracious to those who oppress you is the most powerful act you can perform before a watching world."),

    story("Tong Tu Truong --- Chi Mot Noi Lan", "Truyen Co Trung Hoa --- TK 6 TCN",
          "T",
          [("T ong Tu Truong la quan dai phu nuoc te thoi Xuan Thu co tieng la nguoi hieu lua, biet nguoi.", "Tong Ziqi was a high official of the state of Qi during the Spring and Autumn period, famed for understanding people."),
           ("Mot nguoi quan chuc cap duoi da vu cao ong truoc vua de gianh chuc vi cua ong.", "A subordinate official had falsely accused him before the king to seize his position."),
           ("Sau khi sac thu chung minh ong vo toi, moi nguoi doi biet ong se tra thu ke vu cao.", "When evidence proved his innocence, everyone waited to see him take revenge on his accuser."),
           ("Ong khong lam vay; thay vao do ong chu dong de nghi vua khoan hong cho ke do, noi rang: 'Ke do chi lam vi qua khat vong.'", "He did not; instead he proactively asked the king to pardon the man, saying: 'He only did it out of too much ambition.'"),
           ("Nguoi quan chuc nay sau do tro thanh nguoi ung ho nhiet tinh nhat cua ong, biet on suot ca doi.", "The official afterward became his most zealous supporter, grateful for the rest of his life.")],
          "Kho khoan dung hon sang tac; nhung phan thuong cua no -- long trung thanh -- khong tien nao mua duoc.",
          "Forgiveness is harder than revenge; but its reward --- loyalty --- cannot be bought with any price."),

    story("Archbishop Tutu Va Uy Ban Hoa Giai", "Desmond Tutu --- Nam Phi 1995",
          "S",
          [("S au khi che do apartheid sup do, Nam Phi dung truoc lua chon: xet xu toan bo hay hoa giai.", "After apartheid collapsed, South Africa faced a choice: total prosecution or reconciliation."),
           ("Archbishop Desmond Tutu dung ra lanh dao Uy Ban Su That va Hoa Giai --- mot thi nghiem chua tung co.", "Archbishop Desmond Tutu led the Truth and Reconciliation Commission --- an unprecedented experiment."),
           ("Nhung ke hanh hung phai ra khai nhan toi truoc cong chung; nan nhan duoc quyen noi ve noi dau cua ho.", "Perpetrators had to confess their crimes publicly; victims were given the right to speak of their pain."),
           ("Nhieu nan nhan --- nhung nguoi co quyen cam thu nhat --- da chon su tha thu thay vi tra thu.", "Many victims --- those with the greatest right to hatred --- chose forgiveness over revenge."),
           ("Uy Ban nay giup Nam Phi tranh duoc mot cuoc noi chien ma nhieu nguoi du doan se khong the tranh khoi.", "The Commission helped South Africa avoid a civil war that many had predicted was unavoidable.")],
          "Su that khong co tha thu se tao nen bao luc; tha thu khong co su that se la lua doi --- chi co ca hai moi chua lanh.",
          "Truth without forgiveness creates violence; forgiveness without truth is deception --- only both together can heal."),

    story("Hoang De Minh --- Dai An Xa Cho Sinh Linh", "Minh Thai To --- Trung Hoa 1368",
          "S",
          [("S au khi thanh lap trieu Minh va danh duoi nguoi Mong Co, Chu Nguyen Chuong dung truoc yeu cau cua quan lanh.", "After founding the Ming Dynasty and expelling the Mongols, Zhu Yuanzhang faced demands from his generals."),
           ("Ho thuc ep ong tru diet toan bo gia dinh cac tong binh Mong Co de tru hau hoa mai sau.", "They pressed him to exterminate the entire families of Mongol commanders to prevent future threats."),
           ("Hoang de hoi cac binh linh Mong Co con lai: 'Cac nguoi se trung thanh neu nhan duoc khoan dung?'", "The emperor asked the remaining Mongol soldiers: 'Will you be loyal if you receive mercy?'"),
           ("Khi ho ban hon, ong ra lenh bo vu khi di va trao dat de canh tac --- khong giet them mot ai nua.", "When they wavered, he ordered them to lay down arms and gave them land to farm --- killing no one more."),
           ("Bien gioi phia bac giu yen tinh trong nhieu thap nien nhot nho chinh sach an hoa bat ngo nay.", "The northern border remained peaceful for decades precisely because of this unexpected policy of mercy.")],
          "Mot quy dao tha thu co the mang lai hoa binh lau dai hon mot tram tran chien thang quan su.",
          "One royal act of forgiveness can bring longer peace than a hundred military victories."),

    story("Vo Nguyen Giap Tha Tu Binh Phap", "Vo Nguyen Giap --- Viet Nam 1954",
          "S",
          [("S au chien thang Dien Bien Phu nam 1954, Viet Nam co hang ngan tu binh Phap trong tay.", "After the victory at Dien Bien Phu in 1954, Vietnam held thousands of French prisoners of war."),
           ("Tuong Vo Nguyen Giap ra lenh doi xu nhan dao voi tu binh --- cham soc thuong binh, cung cap thuc an du.", "General Vo Nguyen Giap ordered humane treatment for prisoners --- caring for the wounded, providing sufficient food."),
           ("Nhieu van phong nguoc chieu mong doi su bao thu; nhung de nghi tra thu bi tuong tu choi.", "Many historical accounts note expectations of retaliation; but requests for revenge were refused by the general."),
           ("Mot so si quan Phap ve nuoc da viet sach ke lai su doi xu co nhan nay voi long kinh trong sau sac.", "Some French officers returned home and wrote books recounting this humane treatment with deep respect."),
           ("Su khoan hoa nay gop phan xay dung hinh anh dau tranh chinh nghia cua Viet Nam truoc mat the gioi.", "This magnanimity helped build Vietnam's image as a righteous struggle in the eyes of the world.")],
          "Doi xu nhan dao voi ke thua tran khong chi la dao duc --- do con la chien luoc ngoai giao khon ngoan nhat.",
          "Treating defeated enemies humanely is not only moral --- it is the wisest diplomatic strategy."),
    ])

with open(os.path.join(BASE, "ch01-khoan-dung.tex"), "w", encoding="utf-8") as f:
    f.write(ch1)
print("ch01 done")

# ================================================================
# CHUONG 2: BIET LANG NGHE
# ================================================================
ch2 = chapter(
    "Biet Lang Nghe --- Nghe De Hieu, Khong Chi Nghe De Tra Loi", "Listening to Understand, Not to Reply",
    "Most people do not listen with the intent to understand; they listen with the intent to reply.",
    "Phan lon moi nguoi nghe khong phai de hieu; ho nghe de chuan bi tra loi.",
    [
    story("Socrates Va Nghe Thuat Dat Cau Hoi", "Socrates --- Hy Lap TK 5 TCN",
          "S",
          [("S ocrates noi tieng khap Athens khong phai vi ong ta biet nhieu, ma vi ong ta biet dat cau hoi.", "Socrates was famous throughout Athens not because he knew much, but because he knew how to ask questions."),
           ("Ong thuong ngoi vao goc pho bat chuyen voi nguoi qua duong --- nghe truoc, hoi sau, khong bao gio ngat loi.", "He would sit at street corners and strike up conversations --- listening first, asking later, never interrupting."),
           ("Mot lan mot vi tuong kieu ngao den tranh luan; Socrates luong hoi dong thoi khong noi gi.", "Once an arrogant general came to debate; Socrates simply asked questions and said nothing himself."),
           ("Sau ba gio, vi tuong tu nguyen noi: 'Toi chua bao gio nghi sau ve van de nay cho den hom nay.'", "After three hours, the general voluntarily said: 'I have never thought so deeply about this until today.'"),
           ("Socrates tra loi: 'Toi khong day ong dieu gi; toi chi dat cau hoi de ong tu tim ra su that cua chinh ong.'", "Socrates replied: 'I taught you nothing; I only asked questions so you could find your own truth.'")],
          "Su kien thuc that su nam o viec biet dat cau hoi dung --- nguoi nao dat duoc cau hoi tot lam chu buoi tro chuyen.",
          "True knowledge lies in knowing how to ask the right questions --- the one who asks well masters the conversation."),

    story("Lincoln Nghe Dan Truoc Khi Quyet Dinh", "Abraham Lincoln --- Hoa Ky 1862",
          "M",
          [("M oi tuan, Lincoln doi han cho bat ky ai den gap ong tai Nha Trang --- tu binh si, dan oan, den phu no co con nho.", "Every week, Lincoln kept open hours for anyone to meet him at the White House --- from soldiers to petitioners to mothers with small children."),
           ("Cac co van khuyen ong dung lang phi thoi gian; ong tra loi: 'Day la bat mach cong luan cua toi.'", "Advisors urged him not to waste time; he replied: 'This is how I take the pulse of public opinion.'"),
           ("Mot lan mot ba cu toi xin tha cho con trai sap bi xu ban vi doi quan; Lincoln lang nghe het mot tieng dong ho.", "Once an old woman came to beg clemency for her son about to be shot for desertion; Lincoln listened for a full hour."),
           ("Sau do ong viet tay mot lanh thu an xa va cho ba cam theo di.", "Afterward he personally handwrote a clemency letter and let her take it with her."),
           ("Ong noi voi co van: 'Bat cu ai chiu lang nghe noi dau cua nguoi khac --- chinh ho la nguoi co quyen duoc duoc lang nghe.'", "He told an aide: 'Anyone who takes the time to hear others' pain --- they themselves are the ones deserving to be heard.'")],
          "Lang de nghe khong phai mat thoi gian ma la dau tu vao long tin --- va long tin la nen tang cua moi lanh dao.",
          "Taking time to listen is not wasting time but investing in trust --- and trust is the foundation of all leadership."),

    story("Khong Tu Hoc Tu Bo Con", "Khong Tu --- Trung Quoc TK 5 TCN",
          "M",
          [("M ot hom tren duong di qua mot moi lang, Khong Tu nghe mot dua tre dang hat bai dan ca ve mua.", "One day on a rural road, Confucius heard a child singing a folk song about the harvest season."),
           ("Bai hat co mot cau dat rat hay ve thien nhien ma Khong Tu chua tung suy nghi den.", "The song contained a line about nature so well-crafted that Confucius had never considered it before."),
           ("Ong dung lai, hoi ten tro nho, bat dua tre hat lai lan nua, roi ghi vao so tay cua minh.", "He stopped, asked the child's name, had the child sing it again, then wrote it in his notebook."),
           ("Cac mon do ngac nhien: 'Thu truoc sao thay lai hoc tu tre con?' Khong Tu tra loi tu te:", "His disciples were surprised: 'Why would the master learn from a child?' Confucius replied calmly:"),
           ("'Lang nghe chi mot lan la hoc; doi biet het cu khong lang nghe la loai.' --- Ong luon de loi tim lang nghe.", "'To listen even once is to learn; to think you know all and not listen is to decay.' --- He always kept his ears open.")],
          "Kien thuc den voi nhung ai con chiu lang nghe --- du nguon goc cua kien thuc do la mot dua tre hay mot nguoi khac minh.",
          "Knowledge comes to those who still choose to listen --- even if its source is a child or someone seemingly lesser."),

    story("Theodore Roosevelt Nho Ten Tat Ca Moi Nguoi", "Theodore Roosevelt --- Hoa Ky 1901",
          "K",
          [("K hi Theodore Roosevelt tro thanh Tong Thong, ong co mot thoi quen bat thuong: ong nho ten tat ca nhan vien.", "When Theodore Roosevelt became President, he had an unusual habit: he remembered the names of everyone he worked with."),
           ("Tu nguoi lam bep, nguoi giu cua, den nguoi lau san --- ong deu chao bang ten khi gap.", "From the cook to the doorman to the floor-sweeper --- he greeted each by name when passing."),
           ("Ong giai thich: 'Nho ten ai la noi rang ho quan trong voi toi --- va ho thi that su quan trong.'", "He explained: 'Remembering someone's name says they matter to me --- and they genuinely do matter.'"),
           ("Mot nguoi lau san ke lai rang khi Tong Thong chao ong bang ten, ong cam thay minh la mot phan cua lich su.", "One floor-sweeper recalled that when the President greeted him by name, he felt himself to be part of history."),
           ("Roosevelt noi: 'La lanh dao, cong viec cua toi la lang nghe khong chi loi noi ma ca con nguoi trong loi noi do.'", "Roosevelt said: 'As a leader, my job is to listen not just to words but to the person behind those words.'")],
          "Nho ten va lang nghe ai do la dieu re nhat ban co the lam --- nhung hieu qua cua no lon hon bat ky khoan thuong nao.",
          "Remembering someone's name and listening to them is the cheapest thing you can do --- but its effect surpasses any bonus."),

    story("Bac Ho Nghe Dan Khieu Kien", "Ho Chi Minh --- Viet Nam 1945",
          "H",
          [("H oi dau nam 1945, khi vua lap nuoc, co mot ba cu nong dan di bo may chuc km len Ha Noi gap Chu tich.", "In early 1945, just after independence, an elderly peasant woman walked dozens of kilometers to Hanoi to meet the Chairman."),
           ("Nguoi bao ve ngan khong cho vao vi khong co lich hen; ba cu ngoi cho ben ngoai suot buoi sang.", "Guards would not let her in because she had no appointment; she sat waiting outside for the whole morning."),
           ("Bac Ho di bo ngang qua thay ba cu, dung lai hoi tham, roi dan vao van phong ngoi nghe ba ke.", "Uncle Ho, walking by, noticed the old woman, stopped to ask, then led her into his office to hear her story."),
           ("Ba keu oan dat dai bi chiem dung boi cuong hao; Bac ghi lai va chi thi cap duoi giai quyet ngay.", "She complained of land seized by local bullies; Uncle Ho wrote it down and instructed subordinates to resolve it at once."),
           ("Ong noi voi can bo: 'Moi nguoi dan di gap lanh dao la mang theo mot buoc cua cach mang den truoc mat ta.'", "He told his staff: 'Every citizen who comes to see a leader brings a brick of the revolution before our eyes.'")],
          "Lang nghe dan khong phai hanh dong cua su khiem ton --- do la hanh dong cua lanh dao biet rang suc manh cua minh den tu dau.",
          "Listening to the people is not an act of humility --- it is the act of a leader who knows the source of their strength."),

    story("Kofi Annan Va Nghe Thuat Hoa Giai", "Kofi Annan --- LHQ 1997",
          "K",
          [("K ofi Annan, Tong Thu Ky LHQ, noi tieng voi kha nang hoa giai cac ben dang xung dot du doi.", "Kofi Annan, UN Secretary-General, was famed for his ability to reconcile fiercely opposing sides."),
           ("Bi mat cua ong rat don gian: ong ngoi nghe moi ben noi triet de --- khong ngat loi, khong chuan bi phan bac.", "His secret was simple: he sat listening to each side speak exhaustively --- not interrupting, not preparing a rebuttal."),
           ("Sau khi ca hai ben noi xong, ong don gian tom tat lai dieu moi ben noi --- de moi ben nghe chinh minh qua loi ke lai.", "After both sides finished, he simply summarized what each had said --- letting each side hear themselves through his retelling."),
           ("Nhieu cuoc xung dot giam nhiet chi sau buoc nay --- vi phan lon mau thuan bat nguon tu chua bao gio duoc nghe.", "Many conflicts cooled after just this step --- because most conflicts originate from never having been truly heard."),
           ("Annan noi: 'Chua co cuoc dan phan nao that su that bai vi nghe qua nhieu; chung chi that bai vi noi qua nhieu.'", "Annan said: 'No negotiation has ever truly failed from listening too much; they only fail from talking too much.'")],
          "Trong bat ky cuoc dan phan nao, ben nao chiu lang nghe nhieu hon se co loi the hon --- vi ho hieu ro hon.",
          "In any negotiation, the side that listens more has the advantage --- because they understand better."),

    story("Bac Si William Osler Va Kien Nhan Voi Benh Nhan", "William Osler --- Canada 1890",
          "B",
          [("B ac si William Osler, nguoi duoc goi la 'cha de cua y hoc hien dai', co mot nguyen tac b~at di bat dich.", "Dr. William Osler, called 'the father of modern medicine,' had one inviolable principle."),
           ("Moi khi gap benh nhan, ong tu ban than minh: 'Benh nhan nay co dieu gi muon noi ma ho chua noi?'", "Whenever he met a patient, he asked himself: 'What does this patient want to say that they haven't said yet?'"),
           ("Ong ngoi xuong ngang tam mat voi benh nhan, khong nhin dong ho, va hoi: 'Ban co the ke cho toi nghe khong?'", "He sat down to the patient's eye level, didn't look at his watch, and asked: 'Can you tell me about it?'"),
           ("Mot nghien cuu sau nay cho thay: neu bac si ngan khong ngat loi, benh nhan chi mat trung binh 92 giay de mo ta het trieu chung.", "A later study showed: if a doctor doesn't interrupt, patients take an average of only 92 seconds to describe all their symptoms."),
           ("Nhung 80 phan tram bac si ngat loi benh nhan truoc 23 giay --- va 40 phan tram bo lo chan doan chinh xac vi the.", "But 80 percent of doctors interrupt patients before 23 seconds --- and 40 percent miss the correct diagnosis because of it.")],
          "Lang nghe la ky nang y khoay quan trong nhat ma cac truong y hoc it truyen day nhat --- va cung la ky nang tri lieu hieu qua nhat.",
          "Listening is the most important clinical skill that medical schools teach the least --- and also the most effective healing tool."),

    story("Diogenes Cha Biet Nhung Nguoi Noi Nhieu", "Diogenes --- Hy Lap TK 4 TCN",
          "D",
          [("D iogenes xu Sinope, nha triet hoc noi tieng voi loi song khoac kho, co mot cach day doc dao.", "Diogenes of Sinope, the philosopher famous for his austere lifestyle, had a unique teaching method."),
           ("Khi mot hoc tro chuong loi hoa hoay den hoi, Diogenes nham mat ngoi yeu lang khong noi gi.", "When a student prone to long-winded speeches came to ask a question, Diogenes closed his eyes and sat quietly saying nothing."),
           ("Hoc tro hoi mai, cuoi cung dung len bo di; Diogenes mo mat goi lai: 'Bay gio ta se tra loi.'", "The student kept asking, finally stood up to leave; Diogenes opened his eyes and called him back: 'Now I will answer.'"),
           ("Hoc tro hoi: 'Sao truoc thay khong tra loi?' Diogenes noi: 'Vi luc do ta chua hieu te het dieu nguoi muon hoi.'", "The student asked: 'Why didn't you answer before?' Diogenes said: 'Because I hadn't yet fully understood what you were asking.'"),
           ("Bai hoc: Ngu si noi truoc khi hieu; ke khon lang nghe cho den khi that su hieu.", "The lesson: Fools speak before understanding; the wise listen until they truly understand.")],
          "Hai tai, mot mieng --- su thu giao nay khong phai ngau nhien; hay lang nghe gap doi khi noi.",
          "Two ears, one mouth --- this proportion is not accidental; listen twice as much as you speak."),

    story("Florence Nightingale Va Suc Manh Cua Hoi Tham", "Florence Nightingale --- Anh 1854",
          "T",
          [("T rong chien tranh Crimea, Florence Nightingale den cham soc thuong binh trong cac benh xa khung khiep.", "During the Crimean War, Florence Nightingale arrived to care for wounded soldiers in appalling hospitals."),
           ("Cac be tren quan su chi muon xu ly thong ke; Nightingale muon biet ten tung nguoi binh si.", "Military superiors only wanted statistics handled; Nightingale wanted to know each soldier's name."),
           ("Moi dem ba di may khu nha thuong voi den lang tay, ngoi lai ben giuong tung nguoi de hoi tham.", "Each night she walked miles of wards with her lamp, sitting beside each bed to ask after each person."),
           ("Thuong binh viet thu ve nha: 'Co ay ngoi voi toi luc nua dem va hoi toi que o dau.'", "The wounded soldiers wrote home: 'She sat with me at midnight and asked where I was from.'"),
           ("Ty le tham vong giam tu 40 phan tram xuong con 2 phan tram --- khong chi vi thuoc ma vi moi nguoi duoc biet rang ho duoc nghe.", "The mortality rate dropped from 40 to 2 percent --- not only from medicine but from each person knowing they were heard.")],
          "Doi khi dieu tri hieu qua nhat khong phai la thuoc --- ma la biet rang co mot nguoi dang thuc su lang nghe nguoi benh.",
          "Sometimes the most effective treatment is not medicine --- but knowing there is someone truly listening."),

    story("Teng Wen-Kung Hoi Khong Tu Ve Lam Nguoi", "Triet Hoc --- Trung Hoa TK 5 TCN",
          "T",
          [("T eng Van Cong, mot vi hoang tu tre, mot lan den gap Khong Tu va hoi: 'Lam nguoi can nhat phai hoc gi?'", "Teng Wen-Gong, a young prince, once visited Confucius and asked: 'What is the most essential thing a person must learn?'"),
           ("Khong Tu khong tra loi ngay; thay ngoi im trong mot thoi gian dai, nhin nguoi hoc tro.", "Confucius did not answer immediately; he sat silent for a long while, looking at the young questioner."),
           ("Roi thay hoi nguoc lai: 'Truoc khi ta tra loi, nguoi hay noi cho ta biet: nguoi nghe dieu nay de lam gi?'", "Then the master asked back: 'Before I answer, you tell me: what will you do with whatever I say?'"),
           ("Hoc tro dam ra suy nghi --- va tu do bat dau lang nghe mot cach khac han, voi muc dich ro rang.", "The student paused to think --- and from that day on began listening in a completely different way, with clear purpose."),
           ("Khong Tu sau do noi: 'Lang nghe dung cach con quan trong hon nguoi noi hay --- vi nguoi nghe quyet dinh gia tri cua loi noi.'", "Confucius later said: 'Listening rightly matters more than speaking well --- because the listener determines the value of words.'")],
          "Nghe ma khong co muc dich chi la tieng on; nghe voi nguyen nhan ro rang moi la hoc.",
          "Listening without purpose is just noise; listening with clear intention is genuine learning."),
    ])

with open(os.path.join(BASE, "ch02-lang-nghe.tex"), "w", encoding="utf-8") as f:
    f.write(ch2)
print("ch02 done")

# ================================================================
# CHUONG 3: LOI NOI VA HANH DONG
# ================================================================
ch3 = chapter(
    "Loi Noi Va Hanh Dong --- Hanh Dong Noi To Hon Loi Noi", "Actions Speak Louder Than Words",
    "Well done is better than well said.",
    "Lam tot con hon la noi hay.",
    [
    story("Gandhi --- Hay La Su Thay Doi Ban Muon Thay", "Mahatma Gandhi --- An Do TK 20",
          "M",
          [("M ot ba me dan con trai den gap Gandhi va noi: 'Nha lanh dao oi, xin ong noi voi con toi dung an duong --- no an qua nhieu duong.'", "A mother brought her son to Gandhi and said: 'Leader, please tell my son not to eat sugar --- he eats too much.'"),
           ("Gandhi im lang roi noi: 'Tuan sau hay cho nguoi den gap toi.' Ba me boi roi nhung van lam theo.", "Gandhi was silent then said: 'Bring him back next week.' The mother was puzzled but complied."),
           ("Tuan sau, Gandhi chi nhin dua tre noi: 'Con oi, dung an qua nhieu duong --- no khong tot cho suc khoe.'", "The following week, Gandhi simply looked at the boy and said: 'Son, don't eat too much sugar --- it's not good for you.'"),
           ("Ba me hoi: 'Tai sao tuan truoc ong khong noi? Sao lai cho chung toi di roi den?' Gandhi tra loi:", "The mother asked: 'Why didn't you say that last week? Why make us go and come back?' Gandhi replied:"),
           ("'Tuan truoc, chinh toi cung dang an nhieu duong. Toi can mot tuan de bo no truoc khi day nguoi khac.'", "'Last week I myself was still eating much sugar. I needed a week to give it up before teaching others.'")],
          "Chi day dieu minh thuc hanh; khong ai co quyen day nguoi khac dieu ma minh chua song qua.",
          "Only teach what you practice; no one has the right to teach others what they have not yet lived."),

    story("Lincoln Va Buc Thu Khong Gui", "Abraham Lincoln --- Hoa Ky 1864",
          "K",
          [("K hi ai do lam Lincoln tuc gian, ong co mot thoi quen la viet ngay mot buc thu gian du vao ho.", "Whenever someone angered Lincoln, he had a habit of immediately writing a furious letter to them."),
           ("Ong viet that that, xuong het buc xuc, roi... gap thu lai de o ngan ban khong bao gio gui.", "He wrote everything out, releasing all frustration, then... folded the letter, kept it in his drawer, never mailed it."),
           ("Bi thu ky hoi tai sao, ong giai thich: 'Sau khi viet xong, toi da noi nhung dieu minh can noi.'", "Asked by his secretary why, he explained: 'After writing it, I've already said what I needed to say.'"),
           ("'Gui di thi chi gay them mau thuan --- ma toi can giai phap, khong can mot ke thu them.'", "'Sending it would only create more conflict --- and I need solutions, not another enemy.'"),
           ("Sau khi mat ong, nguoi ta tim thay hang chuc buc thu gian du chua bao gio gui trong ngan ban cua ong.", "After his death, people found dozens of furious, never-sent letters in his desk drawers.")],
          "Hanh dong khon ngoan nhat doi khi la khong hanh dong --- viet ra de xa stress nhung dung bao gio gui di khi dang tuc.",
          "The wisest action is sometimes inaction --- write it out to release stress but never send it when angry."),

    story("Socrates Va Tam Cai Ro Cua Tin Tuc", "Socrates --- Hy Lap TK 5 TCN",
          "M",
          [("M ot man nguoi chay den gap Socrates: 'Thay oi, toi can noi cho thay nghe mot chuyen ve ban cua thay!'", "A man ran to Socrates: 'Master, I need to tell you something about your friend!'"),
           ("Socrates noi: 'Khoan da --- truoc het ban hay cho loi noi cua minh qua ba cai ro.'", "Socrates said: 'Wait --- first let your words pass through three sieves.'"),
           ("'Cai ro thu nhat: No co that khong? Cai ro thu hai: Co tot khong? Cai ro thu ba: Co can thiet khong?'", "'First sieve: Is it true? Second sieve: Is it good? Third sieve: Is it necessary?'"),
           ("Nguoi dan ong do lung: 'Cai ma toi dinh noi khong that chac, khong tot, va co le cung khong can thiet.'", "The man faltered: 'What I was going to say is not certainly true, not good, and perhaps not necessary either.'"),
           ("Socrates mim cuoi: 'Neu loi noi cua ban khong vượt qua duoc ba cai ro nay --- hay giu no lai cho minh.'", "Socrates smiled: 'If your words cannot pass these three sieves --- keep them to yourself.'")],
          "Truoc khi noi, hoi ban than: No co that? No co tot? No co can? Neu khong co it nhat hai cai, thi tot nhat la dung noi.",
          "Before speaking, ask yourself: Is it true? Is it good? Is it needed? If you can't answer yes to at least two, it's best left unsaid."),

    story("Thomas Edison --- Lam Duc Ket Qua Bai Hoc", "Thomas Edison --- Hoa Ky 1879",
          "S",
          [("S au khi chay thi den dien 10.000 lan, ai do hoi Edison co cam thay minh that bai khong.", "After testing the light bulb 10,000 times, someone asked Edison if he felt like a failure."),
           ("Edison tra loi binh tinh: 'Toi chua that bai mot lan nao ca --- toi da hoc duoc 10.000 cach khong hoat dong.'", "Edison replied calmly: 'I have not failed even once --- I have learned 10,000 ways that do not work.'"),
           ("Nhung dieu Edison noi khong chi la cau noi dep; oa la cach on thuc su song va lam viec.", "What Edison said was not just a pretty quote; that was how he genuinely lived and worked."),
           ("Ong giu nhat ky thi nghiem --- ghi lai ket qua tung lan that bai mot cach chi tiet va khoa hoc.", "He kept experiment journals --- recording the results of each failed attempt in meticulous scientific detail."),
           ("Khi den dien cuoi cung sang len, no sang len tren nen tang cua chinh nhung lan that bai do.", "When the light bulb finally lit up, it did so built upon the foundation of those very failures.")],
          "Nguoi goi bat cu ket qua nao la 'that bai' thuc ra dang tu choi bai hoc quy gia nhat trong thuc nghiem.",
          "Anyone who calls any result 'failure' is actually refusing the most valuable lesson in the experiment."),

    story("Nguyen Trai --- Tu La Trung Va Nghia Quan", "Nguyen Trai --- Viet Nam TK 15",
          "K",
          [("K hi Nguyen Trai viet Binh Ngo Dai Cao, ong khong chi viet mot tuyen ngon chien thang --- ong viet no de day dan.", "When Nguyen Trai wrote the Great Proclamation of Victory over the Wu, he was not just writing a victory declaration --- he was teaching the people."),
           ("Ong viet: 'Viec nhan nghia cot o yen dan; quan dieu co du thuat la trong bi ham ho.'", "He wrote: 'The purpose of humanity and justice is to bring peace to the people; military strategy must prioritize removing disaster.'"),
           ("Bai hoc ong neu ra o day la: dung suc manh quan su nen phai di kem theo muc dich nhan van.", "The lesson he stated was: the use of military force must be accompanied by a humane purpose."),
           ("Sau khi duoi duoc giac Minh, ong de nghi tha bo tuong bi bat thay vi xu tham --- vi 'giang nhuc ke thua chua bao gio tao ra hoa binh dai lau'.", "After expelling the Ming invaders, he proposed releasing captured enemy generals instead of executing them --- because 'humiliating the defeated never creates lasting peace.'"),
           ("Chinh sach nay giup Viet Nam giu hoa binh vung chac voi trung Hoa trong su the ky tiep theo.", "This policy helped Vietnam maintain stable peace with China for the following century.")],
          "Hanh dong nhan nghia sau khi chien thang con kho hon hanh dong anh hung trong khi chien tranh --- va cung quan trong hon nhieu.",
          "Acting with humanity after victory is harder than acting heroically during war --- and far more important."),

    story("Marcus Aurelius --- De Quoc Rung Manh Nhung Tam Long Binh Than", "Marcus Aurelius --- Rome TK 2",
          "N",
          [("N guoi ta noi rang Marcus Aurelius la vi Hoang De Roman vi dai nhat vi ong la nha chien thuat tai ba.", "People say Marcus Aurelius was Rome's greatest emperor because he was a brilliant strategist."),
           ("Nhung bi mat thuc su nam o nhat ky ca nhan cua ong --- Suy Nghi -- ma ong khong bao gio dinh se xuat ban.", "But the real secret lay in his personal journal --- Meditations --- which he never intended to publish."),
           ("Ong viet cho chinh minh: 'Nguoi khac han ta khi ho xuc pham ta. Loi cua ta la phan ung cua ta.'", "He wrote to himself: 'Others are beyond my control when they offend me. What is mine is my reaction.'"),
           ("Moi sang ong tu nhan minh tru'oc khi ra quyet dinh --- nhu mot triet hoc tan tinh toan mon nhung quan doi kho ung.", "Every morning he cross-examined himself before making decisions --- like a rigorous philosopher commanding difficult armies."),
           ("Ong lam nhung gi ong viet --- va de che La Ma song ben vung them hai the ky nho tinh than do.", "He did what he wrote --- and the Roman Empire endured two more centuries partly because of that spirit.")],
          "Nhat ky tu chon thuc la truong tap luyen su tu chon --- viet ra de kiem tra chinh minh truoc, roi moi hanh dong.",
          "A self-examination journal is actually a self-discipline training ground --- write to test yourself first, then act."),

    story("Churchill --- Loi Noi Cuu Nuoc Anh", "Winston Churchill --- Anh 1940",
          "T",
          [("T hang 5/1940, quan Duc da chiem Phap, da pha chong Hoa Lan va Bi --- nuoc Anh gan nhu don doc.", "In May 1940, Germany had taken France, had broken through Holland and Belgium --- Britain stood nearly alone."),
           ("Churchill len lam Thu tuong trong hoan canh tan nhoai nhat co the tuong tuong; ong len san dien doc bai phat bieu.", "Churchill became Prime Minister in the most desperate circumstances imaginable; he mounted the podium to deliver a speech."),
           ("Khong mot loi hua chien thang de dang; ong noi: 'Toi khong co gi de dem het ngoai mau, mo hoi va nuoc mat.'", "Not one promise of easy victory; he said: 'I have nothing to offer but blood, toil, tears, and sweat.'"),
           ("Nhung Quoc Hoi Anh va ca nuoc Anh cam thay khac --- ho cam thay duoc nghe thay su that lan lanh dao that su.", "But the British Parliament and the whole nation felt something different --- they felt they were hearing the truth and real leadership."),
           ("Loi noi thieu su that khong bao gio dong vien duoc ai; chi loi noi song voi su that moi co the cam hoa con tim.", "Words devoid of truth never truly inspire anyone; only words alive with truth can move hearts.")],
          "Hanh dong trung thuc --- ke ca khi su that la bi thu --- luon hieu qua hon su lua doi duong nhu dep den khi can thiet.",
          "Honest action --- even when the truth is bleak --- always works better than comforting deception when it counts."),

    story("Mark Twain --- Noi Dieu Ban tin, Khong Noi Dieu Ban Muon", "Mark Twain --- Hoa Ky 1880",
          "M",
          [("M ark Twain la nhà van My noi tieng it ai biet rang ong biet cach im lang gioi hon cach noi.", "Mark Twain was a famous American writer who few knew was equally skilled at knowing when to be silent."),
           ("Mot lan ong duoc moi phat bieu truoc mot dam dong uu tu ve chinh sach thue khoa bat cong.", "Once he was invited to speak before a crowd angry about unjust tax policies."),
           ("Thay dam dong dang nuong nau, thay vi gap them lua, ong chi noi mot cau: 'Nhung gi mieng tui dang noi het roi.'", "Seeing the crowd already heated, instead of fueling the fire, he said only one sentence: 'The empty pockets say it all.'"),
           ("Bai phat bieu ngan gon nhat trong su nghiep ong --- nhung ghi nho lau nhat khi nhung nguoi chung kien ke lai.", "His shortest speech ever --- but remembered the longest by those who witnessed it."),
           ("Twain viet: 'Su khac biet giua tu dung va tu suyt dung cung lon nhu su khac biet giua sap setam va con doi'.", "Twain wrote: 'The difference between the almost right word and the right word is the difference between the lightning bug and lightning.'")],
          "Mot tu dung dung co the thay doi cuoc tro chuyen; phan con lai cua ngon ngu la de bao ve tu dung do.",
          "One right word can change a conversation; the rest of language exists to protect that right word."),

    story("Ho Xuan Huong --- Tho La Chien Luoc Xa Hoi", "Ho Xuan Huong --- Viet Nam TK 18",
          "H",
          [("H o Xuan Huong song trong xa hoi phong kien khe khe rang buoc phu nu --- nhung ba da su dung tho ca nhu vu khi.", "Ho Xuan Huong lived in a feudal society that tightly restricted women --- but she used poetry as a weapon."),
           ("Ba khong can an thuong, khong can xin phep --- ba noi dieu ba muon noi qua cac bai tho day an du.", "She did not need permission or approval --- she said what she wanted through poems full of metaphors."),
           ("Nhung bai tho cua ba co hai tang y nghia: tang ngoai von lat va tang trong can dam dot pha.", "Her poems had two layers of meaning: a surface layer of wit and an inner layer of bold subversion."),
           ("Nhung ke doc tu tuong chi thay cai ben ngoai; nhung ke hieu thi kinh ngac truoc su can dam cua tu tuong.", "Those who read narrowly only saw the surface; those who understood were stunned by the courage of the thought."),
           ("Ngon ngu --- dung kheo --- la thu vu khi co the xuyen qua rao can xa hoi ma khong can bat ky bao luc nao.", "Language --- used cleverly --- is a weapon that can penetrate social barriers without needing any violence.")],
          "Khi ban khong the noi thang, hay hoc cach noi vong quanh --- va doi khi con xuc tich va sac ben hon.",
          "When you cannot speak directly, learn to speak indirectly --- and sometimes it is even more precise and sharp."),

    story("Bertrand Russell --- Hanh Dong Theo Nhung Gi Ban Tin", "Bertrand Russell --- Anh TK 20",
          "B",
          [("B ertrand Russell la mot triet hoc gia noi tieng cua nuoc Anh da nghi den chien tranh va hoa binh trong suot cuoc doi.", "Bertrand Russell was a famous British philosopher who thought about war and peace throughout his entire life."),
           ("Trong the chien I, khi chan tranh duoc ton vinh, ong con lai la mot trong so it nguoi cong khai phan doi.", "During World War I, when war was being glorified, he was among the very few who publicly opposed it."),
           ("Ong bi mat viec lam o dai hoc, bi bat giam 6 thang --- nhung khong bao gio im lang hay tu choi.", "He lost his university position, was imprisoned for 6 months --- but never went silent or recanted."),
           ("Gan cuoi doi, o tuoi 90, ong xuong duong bieu tinh chong vu khi hat nhan giua Chien tranh Lanh.", "Near the end of his life at 90, he marched in the streets protesting nuclear weapons during the Cold War."),
           ("Ong noi: 'Cam giac toi pham nghiem trong nhat la lam dieu gi do ma ban biet la sai vi nguoi khac mong ban lam.'", "He said: 'The most serious moral crime is doing something you know is wrong because others expect you to.'")],
          "Noi dieu ban tin --- du the gioi cho ban la sai --- la hanh dong ung xu tri thuc cao nhat con nguoi co the thuc hien.",
          "Speaking what you believe --- even when the world tells you you're wrong --- is the highest intellectual act a person can perform."),
    ])

with open(os.path.join(BASE, "ch03-loi-noi-hanh-dong.tex"), "w", encoding="utf-8") as f:
    f.write(ch3)
print("ch03 done")
print("Chapters 1-3 generated successfully!")
