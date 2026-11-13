#!/usr/bin/env python3
"""(Song ngữ: noidung-en/NN.txt cùng cấu trúc từng dòng với noidung/NN.txt; thiếu file EN thì chương in một ngôn ngữ.)
Sinh chương cho sách THƯƠNG CON CHO KHÉO: noidung/NN.txt -> chapters/chNN.typ
Chạy: python3 gen.py && typst compile main.typ
Cú pháp noidung/NN.txt (mỗi mục một dòng):
  CHUONG: tên chương      EPI: câu đề từ      LEAD: đoạn mở đầu
  ## Tên tình huống
  BC: chuyện xảy ra       PX: câu dễ buột miệng | con nghe thành gì
  CON:/ME:/BA: lượt lời   VS: hiểu sâu        BH: điều cốt lõi
  LN: làm ngay tối nay    CN: một câu nói với con      TN: câu tự hỏi (2 dòng)
  @CUOI  rồi  TR: nên tránh | nên thử ;  GN: ghi nhớ ;  DH: dấu hiệu cần giúp ;  TT: thử thách 7 ngày
"""
import pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent
SRC, EN, OUT = ROOT / "noidung", ROOT / "noidung-en", ROOT / "chapters"
OUT.mkdir(exist_ok=True)
for f in OUT.glob("*.typ"):
    f.unlink()

# (số La Mã, tên phần, dòng phụ, mô tả, [mã chương])
PARTS = [
    ("I", "Trước khi mở lời", "Giữ mình trước, rồi mới giữ được con",
     "Con không nhớ hết những gì ba mẹ nói, nhưng nhớ rất lâu cảm giác khi đứng trước ba mẹ. Ba chương đầu là cái nền: bình tĩnh lại, nghe cho tới nơi, và khen chê sao cho con lớn lên.",
     ["01", "02", "03"]),
    ("II", "Chuyện học của con", "Điểm số, bài vở, thi cử, thầy cô",
     "Chỗ ba mẹ và con dễ va nhau nhất. Bốn chương này đi qua tờ điểm kém, cái bàn học bỏ trống, mùa thi, và những lần nhà trường gọi điện.",
     ["04", "05", "06", "07"]),
    ("III", "Chuyện bạn bè của con", "Bị bắt nạt, lỡ sai với bạn, rung động đầu đời",
     "Với con, bạn bè là cả một thế giới. Khi thế giới đó làm con đau, hoặc khi chính con làm bạn đau, ba mẹ đứng ở đâu?",
     ["08", "09", "10"]),
    ("IV", "Màn hình và những lần con trượt chân", "Điện thoại, nói dối, tiền bạc, thử cái không nên thử",
     "Những chuyện làm ba mẹ sợ nhất và dễ nổi nóng nhất. Giữ được bình tĩnh ở đây là giữ được đường cho con quay về.",
     ["11", "12"]),
    ("V", "Dưới một mái nhà", "Cãi lại, anh chị em, và những ngày nhà có sóng gió",
     "Nhà là nơi con tập cách thương và cách giận. Ba chương về cánh cửa phòng đóng sầm, chuyện anh em, và những biến cố người lớn cũng đang chật vật.",
     ["13", "14", "15"]),
    ("VI", "Những ngày con không ổn, và ngày ba mẹ làm lại", "Tự ti, buồn kéo dài, lời xin lỗi của người lớn",
     "Có những ngày thương thôi là chưa đủ, cần biết thêm cách và biết lúc nào phải tìm người giúp. Và có một điều không bao giờ muộn: ba mẹ bắt đầu lại.",
     ["16", "17", "18"]),
]

KEYS = {"CON": "con", "ME": "me", "BA": "ba"}

def q(s):
    return '"' + s.strip().replace("\\", "\\\\").replace('"', '\\"') + '"'

def pair(s, n=2):
    p = [x.strip() for x in s.split(" | ")]
    if len(p) != n:
        raise ValueError(f"cần {n} phần ngăn bởi ' | ': {s[:70]}")
    return p

def lst(items):
    return "(" + ", ".join(q(x) for x in items) + ",)"

def parse(path):
    ch = {"title": None, "epi": "", "lead": "", "secs": [], "tr": [], "gn": [], "dh": [], "tt": []}
    cur = None
    for ln, raw in enumerate(path.read_text().splitlines(), 1):
        l = raw.strip()
        if not l or l.startswith("//"):
            continue
        try:
            if l.startswith("## "):
                cur = {"t": l[3:].strip(), "bc": None, "px": None, "turns": [], "vs": None, "bh": None, "ln": None, "cn": None, "tn": []}
                ch["secs"].append(cur); continue
            if l == "@CUOI":
                cur = None; continue
            k, v = l.split(":", 1)
            k, v = k.strip(), v.strip()
            if k == "CHUONG": ch["title"] = v
            elif k == "EPI": ch["epi"] = v
            elif k == "LEAD": ch["lead"] = v
            elif k in ("GN", "DH", "TT"): ch[k.lower()].append(v)
            elif k == "TR": pair(v); ch["tr"].append(v)
            elif cur is None: raise ValueError("dòng nằm ngoài tình huống")
            elif k in KEYS: cur["turns"].append((KEYS[k], v))
            elif k == "PX": pair(v); cur["px"] = v
            elif k == "TN": cur["tn"].append(v)
            elif k in ("BC", "VS", "BH", "LN", "CN"): cur[k.lower()] = v
            else: raise ValueError(f"khóa lạ {k}")
        except Exception as e:
            sys.exit(f"LỖI {path.name}:{ln}: {e}\n  {l[:100]}")
    return ch

PARTS_EN = [
    ("Before you speak", "Steady yourself first, then you can steady your child", "Children forget most of what we say, but long remember how it felt to stand in front of us. These three chapters are the foundation: calming down, listening all the way, and praising or correcting in ways that help a child grow."),
    ("Your child's schoolwork", "Marks, homework, exams, teachers", "Where parents and children collide most often. Four chapters on the bad mark, the empty desk, exam season, and the days the school calls."),
    ("Your child's friendships", "Being bullied, wronging a friend, first feelings", "To a child, friends are a whole world. When that world hurts them, or when they hurt someone in it, where do parents stand?"),
    ("Screens and stumbles", "Phones, lies, money, trying what they should not", "The things that frighten parents most and make us lose our temper fastest. Staying calm here keeps the road home open."),
    ("Under one roof", "Talking back, siblings, and stormy days at home", "Home is where children practise loving and being angry. Three chapters on the slammed door, brothers and sisters, and crises the adults are struggling with too."),
    ("When your child is not okay, and when you start again", "Low self-worth, lasting sadness, a parent's apology", "Some days love alone is not enough; you need to know how, and when to find help. And one thing is never too late: beginning again."),
]

def struct(ch):
    return [[s["turns"][i][0] for i in range(len(s["turns"]))] + [len(s["tn"])] for s in ch["secs"]], len(ch["tr"]), len(ch["gn"]), len(ch["dh"]), len(ch["tt"])

chapters = {f.stem: parse(f) for f in sorted(SRC.glob("[0-9]*.txt"))}
en_ch = {}
for f in sorted(EN.glob("[0-9]*.txt")):
    e = parse(f)
    if f.stem not in chapters: sys.exit(f"EN {f.name}: không có bản Việt")
    a, b = struct(chapters[f.stem]), struct(e)
    if a != b:
        for n, (x, y) in enumerate(zip(a[0], b[0]), 1):
            if x != y: print(f"  LỆCH {f.name} tình huống {n}: VI {x} / EN {y}")
        sys.exit(f"EN {f.name}: cấu trúc không khớp bản Việt: VI {a[1:]} secs={len(a[0])} / EN {b[1:]} secs={len(b[0])}")
    en_ch[f.stem] = e

def E(v):
    return "" if v is None else f", en: {q(v)}"

names, idx, total, warn = [], 0, 0, []
for pn, (roman, ptitle, psub, pdesc, codes) in enumerate(PARTS):
    codes = [c for c in codes if c in chapters]
    if not codes:
        continue
    bi = all(c in en_ch for c in codes)
    titles = []
    for i, c in enumerate(codes):
        t = chapters[c]["title"]
        titles.append(f'({idx + i + 1}, {q(t)})')
    pe = PARTS_EN[pn]
    pname = f"part{pn + 1}.typ"
    desc = pdesc
    sub = psub + ("  ·  " + pe[0] if bi else "")
    (OUT / pname).write_text('#import "../template.typ": *\n\n'
        f'#part-open({q(roman)}, {q(ptitle)}, {q(sub)}, {q(desc)}, ({", ".join(titles)},), idx: {pn + 1})\n')
    names.append(pname)
    for code in codes:
        idx += 1
        ch = chapters[code]
        en = en_ch.get(code)
        o = ['#import "../template.typ": *', ""]
        enarg = ""
        if en:
            enarg = f', en: ({q(en["title"])}, {q(en["epi"])}, {q(en["lead"])}, {lst([s["t"] for s in en["secs"]])})'
        o.append(f'#chapter-open({idx}, {q(ch["title"])}, {idx}, {q(ch["epi"])}, {q(ch["lead"])}, {lst([s["t"] for s in ch["secs"]])}{enarg})')
        for n, s in enumerate(ch["secs"], 1):
            total += 1
            es = en["secs"][n - 1] if en else None
            g = (lambda k: es[k]) if es else (lambda k: None)
            for key in ("bc", "px", "vs", "bh", "ln", "cn"):
                if not s[key]: warn.append(f"{code} @{n} thiếu {key.upper()}")
                if es and not es[key]: warn.append(f"EN {code} @{n} thiếu {key.upper()}")
            if len(s["tn"]) != 2: warn.append(f"{code} @{n} có {len(s['tn'])} TN")
            o.append(f'\n#sec({q(s["t"])}{E(es["t"] if es else None)})')
            if s["bc"]: o.append(f'#boicanh({q(s["bc"])}{E(g("bc"))})')
            if s["px"]:
                a, b = pair(s["px"])
                pe2 = ""
                if es and es["px"]:
                    x, y = pair(es["px"]); pe2 = f', en: ({q(x)}, {q(y)})'
                o.append(f'#phanxa({q(a)}, {q(b)}{pe2})')
            o.append(f'#scene("Tình huống {idx}.{n} · Thử nói cách khác")[')
            for ti, (k, v) in enumerate(s["turns"]):
                o.append(f'  #{k}({q(v)}{E(es["turns"][ti][1] if es else None)})')
            o.append(']')
            if s["vs"]: o.append(f'#hieusau1({q(s["vs"])}{E(g("vs"))})')
            if s["bh"]: o.append(f'#cotloi({q(s["bh"])}{E(g("bh"))})')
            if s["ln"]: o.append(f'#lamngay1({q(s["ln"])}{E(g("ln"))})')
            if s["cn"]: o.append(f'#caunoi({q(s["cn"])}{E(g("cn"))})')
            if s["tn"]: o.append(f'#tusoi({lst(s["tn"])}' + (f', en: {lst(es["tn"])}' if es else "") + ')')
        o.append("\n#v(1.6em, weak: true)")
        o.append(f'#heading(level: 2, numbering: none, outlined: false)[Cuối chương {idx}: mang theo bên mình]')
        def LE(key):
            return f', en: {lst(en[key])}' if en else ""
        if ch["tr"]:
            rows = []
            for ti, t in enumerate(ch["tr"]):
                parts = pair(t) + (pair(en["tr"][ti]) if en else [])
                rows.append("(" + ", ".join(q(x) for x in parts) + ")")
            o.append("#doicau1((" + ", ".join(rows) + ",))")
        if ch["gn"]: o.append(f'#listbox1("BA MẸ GHI NHỚ  ·  KEEP IN MIND", rgb("1E293B"), softbg, {lst(ch["gn"])}{LE("gn")})')
        if ch["dh"]: o.append(f'#listbox1("KHI NÀO CẦN TÌM NGƯỜI GIÚP  ·  WHEN TO SEEK HELP", crimson, rgb("FFF5F5"), {lst(ch["dh"])}, mark: sym.triangle.filled.small.r{LE("dh")})')
        if ch["tt"]: o.append(f'#listbox1("THỬ THÁCH 7 NGÀY CHO CẢ NHÀ  ·  A 7-DAY FAMILY CHALLENGE", teal, rgb("F0FDFA"), {lst(ch["tt"])}, mark: sym.star.filled{LE("tt")})')
        for key in ("tr", "gn", "tt"):
            if not ch[key]: warn.append(f"chương {code} thiếu {key.upper()}")
        name = f"ch{idx:02d}.typ"
        (OUT / name).write_text("\n".join(o) + "\n")
        names.append(name)

(ROOT / "chapters.typ").write_text("\n".join(f'#include "chapters/{n}"' for n in names) + "\n")
print(f"{idx} chương, {total} tình huống, {len(en_ch)} chương có tiếng Anh")
for w in warn: print("  !", w)
