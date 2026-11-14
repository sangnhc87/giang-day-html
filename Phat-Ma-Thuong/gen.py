#!/usr/bin/env python3
"""Sinh chương sách PHẠT MÀ THƯƠNG từ noidung/NN.txt -> chapters/chNN.typ
Khóa: CHUONG: EPI: LEAD: | ## Tên tình huống | LOI: (tình huống) | THAY:/TRO: (lời thoại ngắn)
CHIEU: Tên chiêu | cách làm | VS: vì sao hiệu quả | RG: ranh giới | BT: biến tấu | CN: một câu thầy có thể nói
@CUOI: GN: ghi nhớ (nhiều dòng)"""
import pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parent
SRC, OUT = ROOT / "noidung", ROOT / "chapters"
OUT.mkdir(exist_ok=True)
for f in OUT.glob("*.typ"): f.unlink()
PARTS = [
 ("I", "Lớp học ồn ào", "Khi cả lớp cần lấy lại nhịp", "Nói chuyện riêng, ồn tập thể, cười không dừng được. Những chiêu giữ nhịp lớp mà không phải la.", ["01", "02"]),
 ("II", "Nề nếp hằng ngày", "Trễ, quên, ngủ gật, điện thoại", "Những lỗi nhỏ lặp lại mỗi tuần. Mỗi chiêu đều tặng em một công cụ để nhớ, để tỉnh, để tự giữ mình.", ["03", "04", "05"]),
 ("III", "Lời nói và các mối quan hệ", "Nói tục, cãi thầy, làm nhóm", "Nơi em học cách dùng lời nói, cách bất đồng, cách sống cùng nhau.", ["06", "07", "08"]),
 ("IV", "Tình cảm tuổi mới lớn", "Crush, thư tình, quà, tỏ tình, chia tay", "Thích một người không phải là lỗi. Những chiêu giữ nhịp học, giữ sự tôn trọng cho cả hai phía, và biết lúc nào phải dừng chiêu nhẹ để bảo vệ em.", ["15"]),
 ("V", "Trung thực và trách nhiệm", "Gian lận, nói dối, trốn học, phá đồ, nội quy", "Những lỗi chạm đến nguyên tắc. Giữ rõ ranh giới nhưng vẫn mở một đường lùi an toàn để em dám nói thật và sửa.", ["09", "17", "10", "11", "12"]),
 ("VI", "Va chạm và hành vi nguy hiểm", "Đánh nhau, bắt nạt, thuốc lá, vật cấm", "An toàn đi trước, chiêu nhẹ đi sau. Phần này luôn kèm việc báo cáo và phối hợp mà thầy cô không nên bỏ qua.", ["16"]),
 ("VII", "Sân trường và sinh hoạt tập thể", "Chào cờ, xếp hàng, hành lang, cổng trường", "Lỗi xảy ra giữa đám đông, khó phạt trực tiếp. Dùng chiêu đổi vai và giao nhiệm vụ cao cả.", ["18"]),
 ("VIII", "Khi em đang có chuyện, và kho chiêu", "Chiêu không phạt, chiêu đổi mỗi tuần", "Đôi khi câu trả lời hay nhất là không phạt. Cuối cùng là phương pháp để chiêu không bao giờ cạn.", ["13", "14"]),
]
PARTS_EN = ["A noisy classroom: when the whole class needs its rhythm back",
 "Daily routines: lateness, forgetting, dozing, phones",
 "Words and relationships: swearing, talking back, group work",
 "Adolescent feelings: crushes, love notes, gifts, confessions, break-ups",
 "Honesty and responsibility: cheating, lying, truancy, vandalism, rules",
 "Clashes and dangerous behaviour: fighting, bullying, tobacco, prohibited items",
 "School yard and shared activities: flag salute, queues, corridors, the gate",
 "When a student is in trouble, and the toolbox: no-punishment moves, rotating moves"]
q = lambda s: '"' + s.strip().replace("\\", "\\\\").replace('"', '\\"') + '"'
def lst(xs): return "(" + ", ".join(q(x) for x in xs) + ",)"
def parse(path):
    ch = {"title": None, "epi": "", "lead": "", "secs": [], "gn": []}; cur = None
    for ln, raw in enumerate(path.read_text().splitlines(), 1):
        l = raw.strip()
        if not l or l.startswith("//"): continue
        try:
            if l.startswith("## "):
                cur = {"t": l[3:].strip(), "loi": "", "turns": [], "chieu": None, "vs": "", "rg": "", "bt": "", "cn": ""}; ch["secs"].append(cur); continue
            if l == "@CUOI": cur = None; continue
            k, v = [x.strip() for x in l.split(":", 1)]
            if k == "CHUONG": ch["title"] = v
            elif k == "EPI": ch["epi"] = v
            elif k == "LEAD": ch["lead"] = v
            elif k == "GN": ch["gn"].append(v)
            elif cur is None: raise ValueError("ngoài tình huống")
            elif k in ("THAY", "TRO"): cur["turns"].append((k.lower(), v))
            elif k == "CHIEU":
                a = [x.strip() for x in v.split(" | ")]
                if len(a) != 2: raise ValueError("CHIEU cần: tên | cách làm")
                cur["chieu"] = a
            elif k in ("LOI", "VS", "RG", "BT", "CN"): cur[k.lower()] = v
            else: raise ValueError("khóa lạ " + k)
        except Exception as e: sys.exit(f"LỖI {path.name}:{ln}: {e}\n  {l[:90]}")
    return ch
chapters = {f.stem: parse(f) for f in sorted(SRC.glob("[0-9]*.txt"))}
EN = ROOT / "noidung-en"
def struct(c): return ([[t[0] for t in s["turns"]] for s in c["secs"]], len(c["gn"]))
en_ch = {}
for f in sorted(EN.glob("[0-9]*.txt")):
    e = parse(f)
    if f.stem not in chapters: sys.exit(f"EN {f.name}: không có bản Việt")
    if struct(chapters[f.stem]) != struct(e): sys.exit(f"EN {f.name}: cấu trúc không khớp bản Việt")
    for n, (a, b) in enumerate(zip(chapters[f.stem]["secs"], e["secs"]), 1):
        for k in ("loi","vs","rg","cn","bt"):
            if bool(a[k]) != bool(b[k]): sys.exit(f"EN {f.name} @{n}: lệch {k}")
    en_ch[f.stem] = e
qe = lambda v: "" if v is None else f", en: {q(v)}"
names, idx, total, warn = [], 0, 0, []
for pn, (rm, pt, ps, pd, codes) in enumerate(PARTS):
    codes = [c for c in codes if c in chapters]
    if not codes: continue
    titles = [f'({idx + i + 1}, {q(chapters[c]["title"])})' for i, c in enumerate(codes)]
    (OUT / f"part{pn+1}.typ").write_text('#import "../template.typ": *\n\n' + f'#part-open({q(rm)}, {q(pt)}, {q(ps + "  ·  " + PARTS_EN[pn])}, {q(pd)}, ({", ".join(titles)},), idx: {pn+1})\n')
    names.append(f"part{pn+1}.typ")
    for code in codes:
        idx += 1; ch = chapters[code]
        en = en_ch.get(code)
        enarg = f', en: ({q(en["title"])}, {q(en["epi"])}, {q(en["lead"])}, {lst([s["t"] for s in en["secs"]])})' if en else ""
        o = ['#import "../template.typ": *', "", f'#chapter-open({idx}, {q(ch["title"])}, {idx}, {q(ch["epi"])}, {q(ch["lead"])}, {lst([s["t"] for s in ch["secs"]])}{enarg})']
        for n, s in enumerate(ch["secs"], 1):
            total += 1
            for key in ("loi", "vs", "rg", "cn"):
                if not s[key]: warn.append(f"{code} @{n} thiếu {key.upper()}")
            if not s["chieu"]: warn.append(f"{code} @{n} thiếu CHIEU"); continue
            es = en["secs"][n - 1] if en else None
            gg = (lambda k: es[k]) if es else (lambda k: None)
            o.append(f'\n#sec({q(s["t"])}{qe(es["t"] if es else None)})')
            o.append(f'#tinhhuong("{idx}.{n}", {q(s["t"])}, {q(s["loi"])}{qe(gg("loi"))})')
            o.append(f'#chieu({q(s["chieu"][0])}, {q(s["chieu"][1])}' + (f', en: ({q(es["chieu"][0])}, {q(es["chieu"][1])})' if es else "") + ')')
            if s["turns"]:
                o.append('#scene("Thầy nói thế nào · gợi ý")[')
                for ti, (k, v) in enumerate(s["turns"]): o.append(f'  #{k}({q(v)}{qe(es["turns"][ti][1] if es else None)})')
                o.append(']')
            o.append(f'#visao({q(s["vs"])}{qe(gg("vs"))})')
            o.append(f'#ranhgioi({q(s["rg"])}{qe(gg("rg"))})')
            if s["bt"]: o.append(f'#bientau({q(s["bt"])}{qe(gg("bt"))})')
            o.append(f'#caunoi({q(s["cn"])}{qe(gg("cn"))})')
        if ch["gn"]:
            o.append("\n#v(1.6em, weak: true)")
            o.append(f'#heading(level: 2, numbering: none, outlined: false)[Cuối chương {idx}: mang theo bên mình]')
            o.append(f'#listbox1("THẦY CÔ GHI NHỚ{"  ·  KEEP IN MIND" if en else ""}", rgb("1E293B"), softbg, {lst(ch["gn"])}' + (f', en: {lst(en["gn"])}' if en else "") + ')')
        (OUT / f"ch{idx:02d}.typ").write_text("\n".join(o) + "\n"); names.append(f"ch{idx:02d}.typ")
(ROOT / "chapters.typ").write_text("\n".join(f'#include "chapters/{n}"' for n in names) + "\n")
print(f"{idx} chương, {total} tình huống, {len(en_ch)} chương có tiếng Anh"); [print("  !", w) for w in warn]
en_titles = []; en_secs = []; vi_sec_count = []
order = [c for (_,_,_,_,codes) in PARTS for c in codes if c in chapters]
for c in order:
    e = en_ch.get(c)
    en_titles.append(e["title"] if e else "")
    en_secs.append([s["t"] for s in e["secs"]] if e else [])
(ROOT / "toc-data.typ").write_text(f"#let nch = {idx}\n#let nsit = {total}\n#let en-titles = {lst(en_titles)}\n#let en-secs = ({', '.join(lst(x) for x in en_secs)},)\n")
