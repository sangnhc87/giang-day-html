import os, re, unicodedata

base = '/Users/admin/Giang-Day-html/truyen-tich-cam-hung-quyen-3/chapters'
fixed_files = 0
for fn in os.listdir(base):
    if not fn.endswith('.tex'):
        continue
    path = os.path.join(base, fn)
    with open(path, encoding='utf-8') as f:
        lines = f.readlines()
    new = []
    changed = False
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith('%'):
            # Keep LaTeX comment lines unchanged
            new.append(line)
        else:
            # Escape bare % that is NOT already escaped
            fixed_line = re.sub(r'(?<!\\)%', r'\\%', line)
            if fixed_line != line:
                changed = True
            new.append(fixed_line)
    if changed:
        content = unicodedata.normalize('NFC', ''.join(new))
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        fixed_files += 1
        print(f"  Fixed: {fn}")

print(f"\nDone. Fixed {fixed_files} files.")
