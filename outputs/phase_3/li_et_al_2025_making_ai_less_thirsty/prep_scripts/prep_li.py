"""One-off preparation of the Li et al. (2025) source text. Not part of the package.

Reads the PDF text layer with PyMuPDF (reading order assigned per page from the
3-column layout), inserts clearly delimited, locally produced transcriptions for
figures/equations, and writes source.md + prep_record.json.
"""
import hashlib, json, re, sys
from pathlib import Path
import pymupdf

PDF, OUT = Path(sys.argv[1]), Path(sys.argv[2])
doc = pymupdf.open(PDF)
ZW = dict.fromkeys(map(ord, "​    ⁠"), None)

def col(b):
    return 0 if b[0] < 205 else (1 if b[0] < 378 else 2)

def block_text(blk):
    """Text of a dict-block with <sup> for superscripts and ** for bold runs."""
    parts = []
    for line in blk["lines"]:
        runs = []
        for sp in line["spans"]:
            t = sp["text"].translate(ZW)
            if not t.strip() and not t:
                continue
            sup = bool(sp["flags"] & 1)
            bold = bool(sp["flags"] & 16)
            runs.append((t, sup, bold))
        # merge adjacent runs of identical style
        merged = []
        for t, sup, bold in runs:
            if merged and merged[-1][1:] == (sup, bold):
                merged[-1] = (merged[-1][0] + t, sup, bold)
            else:
                merged.append((t, sup, bold))
        s = ""
        for t, sup, bold in merged:
            if not t.strip():
                s += t
            elif sup:
                s += f"<sup>{t.strip()}</sup>"
            elif bold:
                lead = t[: len(t) - len(t.lstrip())]; trail = t[len(t.rstrip()):]
                s += f"{lead}**{t.strip()}**{trail}"
            else:
                s += t
        parts.append(s.rstrip())
    return parts  # list of lines

def join_lines(lines, hyph):
    out = ""
    for i, ln in enumerate(lines):
        is_ref = bool(re.match(r"^(\*\*)?\d{1,2}\.\t", ln))
        ln = ln.replace("\t", " ").replace("˲", "-").strip()
        if is_ref and out:
            out = out + "\n" + ln
            continue
        if not out:
            out = ln
        elif out.endswith("-") and ln[:1].islower():
            head = re.search(r"([A-Za-z]+)-$", out)
            tail = re.match(r"[A-Za-z]+", ln)
            keep = head and tail and f"{head.group(1)}-{tail.group(0)}".lower() in hyph
            out = out + ln if keep else out[:-1] + ln
        else:
            out = out + " " + ln
    return re.sub(r"\*\*\s*\*\*", " ", re.sub(r"[ ]{2,}", " ", out)).strip()

# hyphenated compounds that occur unbroken inside a line anywhere in the document
alltext = " ".join(p.get_text() for p in doc)
hyph = {m.group(0).lower() for m in re.finditer(r"[A-Za-z]+-[A-Za-z]+", alltext.replace("-\n", "\x00"))}

pages = {}
def page_blocks(pn):
    p = doc[pn - 1]
    return [b for b in p.get_text("dict")["blocks"] if b["type"] == 0]

def keep(b):
    x0, y0, x1, y1 = b["bbox"]
    first = "".join(s["text"] for l in b["lines"] for s in l["spans"]).strip()
    if y1 < 45 or y0 > 750:                  # running header / footer
        return False
    if x0 > 550:                              # rotated image credit
        return False
    if first == "sustainability":              # running section header
        return False
    return bool(first)

def render(blocks):
    return [join_lines(block_text(b), hyph) for b in blocks]


def _plain(t):
    return re.sub(r"\*\*", "", re.sub(r"<sup>.*?</sup>", "", t)).rstrip()

def merge_columns(paras):
    """Join a paragraph interrupted only by a column break (no terminal punctuation,
    next paragraph starts lowercase). Does not merge across pages."""
    out = []
    for t in paras:
        if out and t[:1].islower() and not _plain(out[-1]).endswith((".", "?", "!", ":", "”", '"', ")")):
            prev = out[-1]
            if _plain(prev).endswith("-"):
                m = re.search(r"([A-Za-z]+)-(</sup>)?\s*$", prev)
                head = prev.rstrip()
                tail = re.match(r"[A-Za-z]+", t)
                keep_h = m and tail and f"{m.group(1)}-{tail.group(0)}".lower() in hyph
                out[-1] = (head if keep_h else head[:-1]) + t
            else:
                out[-1] = prev + " " + t
        else:
            out.append(t)
    return out

def split_footnotes(blocks, ymin):
    foot = [b for b in blocks if b["bbox"][1] >= ymin and b["bbox"][1] < 750]
    return [b for b in blocks if b not in foot], foot

def foot_text(foot):
    t = " ".join(render(sorted(foot, key=lambda b: b["bbox"][1])))
    m = re.match(r"^([a-z]) ", t)
    return f"[Footnote {m.group(1)}] " + t[2:] if m else "[Footnote] " + t

T = {}   # transcription blocks, filled below
exec(open(Path(__file__).with_name("li_transcriptions.py")).read())

def delimited(tid, kind, page, image, body, caveats):
    return (f"<<<TRANSCRIPTION {tid} kind={kind} pdf_page={page} image={image} "
            f"produced_by=local_visual_inspection (not source text)>>>\n{body.strip()}\n"
            f"Not recoverable / approximate: {caveats}\n<<<END TRANSCRIPTION {tid}>>>")

md = []
def add(label_page, texts):
    md.append(f"[PDF page {label_page}]")
    md.extend(t for t in texts if t)

# ---- page 1
bl = [b for b in page_blocks(1) if keep(b)]
left = sorted([b for b in bl if b["bbox"][0] < 380], key=lambda b: b["bbox"][1])
right = sorted([b for b in bl if b["bbox"][0] >= 380], key=lambda b: b["bbox"][1])
right, foot = split_footnotes(right, 700)
add(1, merge_columns(render(left) + render(right)) + [foot_text(foot)])
# ---- page 2
md.append("[PDF page 2]\n[Full-page decorative illustration (data center in front of waterfalls); no text and no data content.]")
# ---- page 3
bl = [b for b in page_blocks(3) if keep(b)]
c = lambda i: sorted([b for b in bl if col(b["bbox"]) == i], key=lambda b: b["bbox"][1])
mid, foot = split_footnotes(c(1), 640)
add(3, merge_columns(render(mid) + render(c(2))) + [foot_text(foot)]
    + ["[Pull quote, repeated from body text:] " + t for t in render(c(0))])
# ---- page 4 (Figure 1 spans center+right columns above the text)
bl = [b for b in page_blocks(4) if keep(b)]
cap = [b for b in bl if b["bbox"][1] < 100 and b["bbox"][0] > 210]
fig_inner = [b for b in bl if 85 <= b["bbox"][1] < 300 and b["bbox"][0] > 210]
rest = [b for b in bl if b not in cap and b not in fig_inner]
c = lambda i: sorted([b for b in rest if col(b["bbox"]) == i], key=lambda b: b["bbox"][1])
paras = merge_columns(render(c(0)) + render(c(1)) + render(c(2)))
i = next(k for k, t in enumerate(paras) if "two common approaches" in t)
paras = paras[: i + 1] + render(cap) + [delimited("T1", "figure", 4, "images/pdf_p04_figure1.png", T["T1"], T["T1_caveat"])] + paras[i + 1 :]
add(4, paras)
# ---- page 5
bl = [b for b in page_blocks(5) if keep(b)]
c = lambda i: sorted([b for b in bl if col(b["bbox"]) == i], key=lambda b: b["bbox"][1])
add(5, merge_columns(render(c(1)) + render(c(2))) + ["[Pull quote, repeated from body text:] " + t for t in render(c(0))])
# ---- page 6 (Table 1 on top, extracted from text layer)
bl = [b for b in page_blocks(6) if keep(b) and b["bbox"][1] > 380]
tcap = [b for b in page_blocks(6) if keep(b) and b["bbox"][1] < 80]
c = lambda i: sorted([b for b in bl if col(b["bbox"]) == i], key=lambda b: b["bbox"][1])
page6 = doc[5]
rows = [b for b in page6.get_text("blocks") if 130 < b[1] < 380 and b[0] < 60 and "\n" in b[4]]
rows.sort(key=lambda b: b[1])
table_lines = []
for r in rows:
    cells = [x.strip() for x in r[4].split("\n") if x.strip()]
    table_lines.append("| " + " | ".join(cells) + " |")
assert len(table_lines) == 18 and all(l.count("|") == 12 for l in table_lines), [l.count("|") for l in table_lines]
header = ("| Location | PUE | Onsite WUE (L/kWh) | Offsite EWIF (L/kWh) | Training: Onsite Water (million L) | "
          "Training: Offsite Water (million L) | Training: Total Water (million L) | Per request: Onsite Water (mL) | "
          "Per request: Offsite Water (mL) | Per request: Total Water (mL) | # of Requests for 500ml Water |")
table = header + "\n|" + "---|" * 11 + "\n" + "\n".join(table_lines)
add(6, render(tcap) + [f"<<<EXTRACTED TABLE 1 pdf_page=6 note=cell values read directly from the PDF text layer; column header "
                      f"restructured by hand into one row; all 18 rows checked against the page image image=images/pdf_p06_table1.png>>>\n{table}\n<<<END EXTRACTED TABLE 1>>>"]
    + merge_columns(render(c(0)) + render(c(1)) + render(c(2))))
# ---- page 7 (Figure 2 spans full width above text)
bl = [b for b in page_blocks(7) if keep(b)]
cap = [b for b in bl if b["bbox"][1] < 120 and b["bbox"][2] - b["bbox"][0] > 400]
inner = [b for b in bl if 120 <= b["bbox"][1] < 285]
rest = [b for b in bl if b not in cap and b not in inner]
c = lambda i: sorted([b for b in rest if col(b["bbox"]) == i], key=lambda b: b["bbox"][1])
add(7, render(cap) + [delimited("T2", "figure", 7, "images/pdf_p07_figure2.png", T["T2"], T["T2_caveat"])]
    + merge_columns(render(c(0)) + render(c(1)) + render(c(2))))
# ---- page 8
bl = [b for b in page_blocks(8) if keep(b)]
c = lambda i: sorted([b for b in bl if col(b["bbox"]) == i], key=lambda b: b["bbox"][1])
add(8, merge_columns(render(c(0)) + render(c(1)) + render(c(2))))

text = "\n\n".join(md) + "\n"
# equation patches (applied by exact-string replacement; each must match exactly once or the script stops)
for old, new, tid in EQUATIONS:
    n = text.count(old)
    assert n == 1, (tid, n, old[:60])
    text = text.replace(old, new)

body, _, refs = text.partition("\nReferences\n")
def _fix(m):
    a, b = m.group(1), m.group(2)
    return f"{a}-{b}" if f"{a}-{b}".lower() in hyph else a + b
body = re.sub(r"([A-Za-z]{2,})- ([a-z]{2,})", _fix, body)
# put each reference on its own line (numbers are sequential)
_parts = refs.strip().split("\n\n")
refs_text = re.sub(r"\s+", " ", _parts[0]).strip()
pos = 0
n = 1
while True:
    m = re.compile(rf"(?:^|\s){n}\. (?=[A-Za-z])").search(refs_text, pos)
    if not m:
        break
    rep = ("" if m.start() == 0 else "\n") + f"{n}. "
    refs_text = refs_text[: m.start()] + rep + refs_text[m.end():]
    pos = m.start() + len(rep)
    n += 1
refs_text = re.sub(r"(https?://)\s+", r"\1", refs_text)
refs_text = re.sub(r"(?<=[a-z])\.\s+(com|org|edu|gov|google)(?=[/.])", r".\1", refs_text)
REF_COUNT = n - 1
refs_text = "\n" + refs_text + "\n\n" + "\n\n".join(_parts[1:])
text = body + "\nReferences\n" + refs_text

OUT.mkdir(parents=True, exist_ok=True)
(OUT / "source.md").write_text(text, encoding="utf-8")
print(len(text))
