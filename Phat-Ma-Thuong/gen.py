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
 ("IV", "Trung thực và trách nhiệm", "Gian lận, trốn học, phá đồ, nội quy", "Những lỗi chạm đến nguyên tắc. Giữ rõ ranh giới nhưng vẫn mở cửa để em sửa.", ["09", "10", "11", "12"]),
 ("V", "Khi em đang có chuyện, và kho chiêu", "Chiêu không phạt, chiêu đổi mỗi tuần", "Đôi khi câu trả lời hay nhất là không phạt. Cuối cùng là phương pháp để chiêu không bao giờ cạn.", ["13", "14"]),
]
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
names, idx, total, warn = [], 0, 0, []
for pn, (rm, pt, ps, pd, codes) in enumerate(PARTS):
    codes = [c for c in codes if c in chapters]
    if not codes: continue
    titles = [f'({idx + i + 1}, {q(chapters[c]["title"])})' for i, c in enumerate(codes)]
    (OUT / f"part{pn+1}.typ").write_text('#import "../template.typ": *\n\n' + f'#part-open({q(rm)}, {q(pt)}, {q(ps)}, {q(pd)}, ({", ".join(titles)},), idx: {pn+1})\n')
    names.append(f"part{pn+1}.typ")
    for code in codes:
        idx += 1; ch = chapters[code]
        o = ['#import "../template.typ": *', "", f'#chapter-open({idx}, {q(ch["title"])}, {idx}, {q(ch["epi"])}, {q(ch["lead"])}, {lst([s["t"] for s in ch["secs"]])})']
        for n, s in enumerate(ch["secs"], 1):
            total += 1
            for key in ("loi", "vs", "rg", "cn"):
                if not s[key]: warn.append(f"{code} @{n} thiếu {key.upper()}")
            if not s["chieu"]: warn.append(f"{code} @{n} thiếu CHIEU"); continue
            o.append(f'\n#sec({q(s["t"])})')
            o.append(f'#tinhhuong("{idx}.{n}", {q(s["t"])}, {q(s["loi"])})')
            o.append(f'#chieu({q(s["chieu"][0])}, {q(s["chieu"][1])})')
            if s["turns"]:
                o.append('#scene("Thầy nói thế nào · gợi ý")[')
                for k, v in s["turns"]: o.append(f'  #{k}({q(v)})')
                o.append(']')
            o.append(f'#visao({q(s["vs"])})')
            o.append(f'#ranhgioi({q(s["rg"])})')
            if s["bt"]: o.append(f'#bientau({q(s["bt"])})')
            o.append(f'#caunoi({q(s["cn"])})')
        if ch["gn"]:
            o.append("\n#v(1.6em, weak: true)")
            o.append(f'#heading(level: 2, numbering: none, outlined: false)[Cuối chương {idx}: mang theo bên mình]')
            o.append(f'#listbox1("THẦY CÔ GHI NHỚ", rgb("1E293B"), softbg, {lst(ch["gn"])})')
        (OUT / f"ch{idx:02d}.typ").write_text("\n".join(o) + "\n"); names.append(f"ch{idx:02d}.typ")
(ROOT / "chapters.typ").write_text("\n".join(f'#include "chapters/{n}"' for n in names) + "\n")
print(f"{idx} chương, {total} tình huống"); [print("  !", w) for w in warn]
