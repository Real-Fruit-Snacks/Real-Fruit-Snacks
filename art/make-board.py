"""Draw the profile README's board: assets/board-dark.svg and assets/board-light.svg.

The board is the first screen of real-fruit-snacks.github.io as one image: the headline, the index of
tools, and one tool's job at a time, what goes in and what comes out. An Ember seam sweeps each job
and the output appears behind it; then the marker moves down the index to the next tool. It loops
through all of them, 3.2 s each, and the board grows to fit the index. The SVG's base styles are a
finished still of the first tool, which is what a viewer that skips the animation, or asks for
reduced motion, shows.

Text is converted to paths from the site's fonts (art/fonts), because an SVG shown through <img>
can't load fonts. Run from the repo root:

    python -m pip install -r art/requirements.txt
    python art/make-board.py
"""
import os
import sys

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "fonts")
OUT = os.path.join(HERE, "..", "assets")

# The tools and their jobs, in the site's order. Keep in step with tools.json in
# Real-Fruit-Snacks/Real-Fruit-Snacks.github.io. `backticks` set a part in mono.
TOOLS = [
    ("screen-mark", "Rust · Windows, Linux", "`Ctrl+PrintScreen`", "`screen-mark_2026-11-05_091412.png`"),
    ("port-sync", "Rust · Windows", "`Port pair 51037->51037`", "`listening port updated: 48213 -> 51037`"),
    ("carify", "sh, PowerShell · Windows, macOS, Linux", "HEVC 10-bit · 1080p · AC3 5.1", "H.264 8-bit · 720p · AAC stereo"),
    ("certapi", "C# · Windows", "a client certificate in `CurrentUser\\My`", "200 OK; the key never left the store"),
    ("identity-gen", "HTML · browser", "a signup form that wants too much", "a stand-in: name, handle, passphrase"),
    ("amazon-order-sync", "Rust · Windows, Linux", "Amazon's order history", "one `Order-<id>.md` per order"),
    ("powershell-toolbox", "PowerShell · Windows", "every repo your `gh` login sees", "one at a time: keep, archive or delete"),
    ("forge-framework", "Python", "`use`, `set`, `run`", "hosts, creds and loot in one workspace"),
    ("pwn-broker", "Python · Kali Linux", "`pwn-broker new`", "`2026-11-16_htb_forest.finished.tar.gz`"),
    ("pwn-shop", "Python · Kali Linux", "an upstream release, pinned by SHA-256", "`kerbrute-1.0.3-1.zip`"),
    ("pwn-playbooks", "Markdown · Kali Linux", "`:Pb smb` in the note window", "`Playbook: SMB enumeration`, to fill in"),
    ("open-file", "TypeScript · browser", "a blunder in one of your games", "a puzzle made from it"),
    ("agent-toolkit", "PowerShell · Windows, Linux", "a Windows desktop where you aren't admin", "T3 Code and Claude Code, no UAC prompt"),
    ("dev-toolkit", "C# · Windows", "a Windows PC with no internet or admin", "Rust, Python, Node and .NET, all offline"),
]

# RFS Nightshift and Dayshift
THEMES = {
    "dark": dict(bg="#0C0D10", line="#262A33", strong="#636872", ink="#E8E6E1", mute="#8A8F99",
                 ember="#FF6A3D", amber="#FFC247", mint="#3DDC97", glow=True),
    "light": dict(bg="#F6F5F2", line="#D6D3CB", strong="#89867F", ink="#1A1B1E", mute="#666A73",
                  ember="#C03B0A", amber="#925F00", mint="#15794D", glow=False),
}

W = 1000
SLOT = 3.2                     # seconds per tool
CYCLE = SLOT * len(TOOLS)
SWEEP_AT, SWEEP = 0.35, 0.9     # the seam starts 0.35 s into a slot and takes 0.9 s
EASE = "cubic-bezier(.65,0,.35,1)"

# Layout
X0, X1 = 40, 960                # outer edges
IDX_NO, IDX_NAME, IDX_END = 40, 82, 330
ROW0, ROW_H = 150, 31           # index rows
H = ROW0 + len(TOOLS) * ROW_H + 18   # the index, then 18 px below it: 540 for twelve tools
DX, DX_TEXT = 384, 452          # the display: labels, then the job text
JOB = 36                        # job type size

SANS = "schibsted-grotesk-latin-var.woff2"
MONO = "fragment-mono-latin-400.woff2"
_files = {}
_faces = {}
_glyphs = {}                    # (face key, glyph name) -> (id, path); drawn once in <defs>


class Face:
    def __init__(self, fname, wght=None):
        if fname not in _files:
            _files[fname] = TTFont(os.path.join(FONTS, fname))
        f = _files[fname]
        self.key = f"{fname}@{wght}"
        self.gs = f.getGlyphSet(location={"wght": wght}) if wght else f.getGlyphSet()
        self.cmap = f.getBestCmap()
        self.upm = f["head"].unitsPerEm

    def names(self, s):
        out = []
        for ch in s:
            if ord(ch) not in self.cmap:
                sys.exit(f"{self.key} has no glyph for {ch!r}")
            out.append(self.cmap[ord(ch)])
        return out

    def width(self, s, size, ls=0.0):
        names = self.names(s)
        return (sum(self.gs[n].width for n in names) + ls * self.upm * max(len(names) - 1, 0)) * size / self.upm


def face(fname, wght=None):
    k = (fname, wght)
    if k not in _faces:
        _faces[k] = Face(fname, wght)
    return _faces[k]


def glyph(fc, name):
    key = (fc.key, name)
    if key not in _glyphs:
        pen = SVGPathPen(fc.gs, ntos=lambda v: "%d" % round(v))
        fc.gs[name].draw(pen)
        _glyphs[key] = (f"g{len(_glyphs):x}", pen.getCommands())
    gid, d = _glyphs[key]
    return gid if d else None


def text(s, x, y, size, fc, fill, ls=0.0, anchor="start", cls=None):
    """`s` as glyph uses, baseline at y. ls is letter spacing in em."""
    if anchor == "end":
        x -= fc.width(s, size, ls)
    k = size / fc.upm
    track = ls * fc.upm
    pen, uses = 0.0, []
    for n in fc.names(s):
        gid = glyph(fc, n)
        if gid:
            uses.append(f'<use href="#{gid}" x="{round(pen)}"/>')
        pen += fc.gs[n].width + track
    attr = f' class="{cls}"' if cls else ""
    return f'<g{attr} transform="translate({x:.1f} {y:.1f}) scale({k:.5f} {-k:.5f})" fill="{fill}">{"".join(uses)}</g>'


# ---- jobs: mixed sans and mono, wrapped at spaces (or after _ / \ in mono, never at a hyphen) ----
def tokens(s, sans):
    """[(space_before, [(text, face, size)])] for a job string at JOB size."""
    mono = face(MONO)
    out, runs, buf, code, space = [], [], "", False, False

    def flush_run():
        nonlocal buf
        if buf:
            runs.append((buf, mono if code else sans, JOB * 0.88 if code else JOB))
            buf = ""

    def flush_token(next_space):
        nonlocal runs, space
        flush_run()
        if runs:
            out.append((space, runs))
        runs, space = [], next_space

    for ch in s:
        if ch == "`":
            flush_run()
            code = not code
        elif ch == " ":
            flush_token(True)
        else:
            buf += ch
            if code and ch in "_/\\":
                flush_token(False)
    flush_token(False)
    return out


def wrap(s, sans, max_w):
    lines, line, x = [], [], 0.0
    for space, runs in tokens(s, sans):
        w = sum(fc.width(t, sz, -0.015) for t, fc, sz in runs)
        gap = sans.width(" ", JOB) if space and line else 0.0
        if line and x + gap + w > max_w:
            lines.append(line)
            line, x, gap = [], 0.0, 0.0
        line.append((x + gap, runs))
        x += gap + w
    if line:
        lines.append(line)
    return lines


def line_width(line):
    x, runs = line[-1]
    return x + sum(fc.width(t, sz, -0.015) for t, fc, sz in runs)


def draw_lines(lines, x, y, lh, fill):
    o = []
    for i, line in enumerate(lines):
        for lx, runs in line:
            px = x + lx
            for t, fc, sz in runs:
                o.append(text(t, px, y + i * lh, sz, fc, fill, ls=-0.015))
                px += fc.width(t, sz, -0.015)
    return "".join(o)


def pct(t):
    return f"{t / CYCLE * 100:.3f}%"


def toggle(name, windows):
    """Keyframes (run with step-end) that show an element only inside the given (start, end) windows."""
    shown = lambda t: int(any(a <= t < b for a, b in windows))
    points = sorted({0.0} | {t for w in windows for t in w if 0 < t < CYCLE})
    body = "".join(f"{pct(t)}{{opacity:{shown(t)}}}" for t in points)
    return f"@keyframes {name}{{{body}100%{{opacity:{shown(0.0)}}}}}"


def build(theme):
    c = THEMES[theme]
    head, name_f, idx_f = face(SANS, 800), face(SANS, 800), face(SANS, 640)
    label_f, meta_f, in_f, out_f = face(SANS, 700), face(SANS, 450), face(SANS, 450), face(SANS, 640)
    mono = face(MONO)
    o, css, base = [], [], []

    # --- the headline and the address ---
    o.append(text("Small tools, one job each.", X0 - 2, 84, 60, head, c["ink"], ls=-0.045))
    o.append(text("real-fruit-snacks.github.io", X1, ROW0 + len(TOOLS) * ROW_H - 10, 16, mono, c["mute"], anchor="end"))

    # --- the board head ---
    o.append(text(str(len(TOOLS)), X0, 132, 13, label_f, c["ink"], ls=0.12))
    o.append(text("TOOLS", X0 + label_f.width(str(len(TOOLS)), 13, 0.12) + 6, 132, 13, label_f, c["mute"], ls=0.12))
    o.append(text(f"/ {len(TOOLS):02d}", X1, 132, 14, mono, c["mute"], anchor="end"))
    o.append(f'<rect x="{X0}" y="142" width="{X1 - X0}" height="2" fill="{c["ink"]}"/>')

    # --- the index: every name in grey; the active one is drawn again in ink below ---
    for i, (repo, meta, _, _) in enumerate(TOOLS):
        y = ROW0 + i * ROW_H
        o.append(text(f"{i + 1:02d}", IDX_NO, y + 20, 12, mono, c["mute"]))
        o.append(text(repo, IDX_NAME, y + 21, 19, idx_f, c["mute"], ls=-0.015))
        o.append(f'<rect x="{X0}" y="{y + ROW_H - 1}" width="{IDX_END - X0}" height="1" fill="{c["line"]}"/>')
    o.append(f'<rect class="marker" x="{IDX_NAME - 14}" y="{ROW0}" width="4" height="{ROW_H - 1}" fill="{c["ember"]}"/>')
    mk = "".join(f"{pct(i * SLOT)}{{transform:translateY({i * ROW_H}px)}}" for i in range(len(TOOLS)))
    css.append(f"@keyframes marker{{{mk}100%{{transform:translateY(0)}}}}")

    if c["glow"]:
        o.append('<defs><filter id="glow" x="-400%" y="-10%" width="900%" height="120%"><feGaussianBlur stdDeviation="4" result="b"/>'
                 '<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>')
    glow = ' filter="url(#glow)"' if c["glow"] else ""

    # --- one group per tool: its index name in ink, the counter, and the display ---
    max_w = X1 - DX_TEXT
    lh = JOB * 1.14
    for i, (repo, meta, job_in, job_out) in enumerate(TOOLS):
        t0 = i * SLOT
        a, b = t0 + SWEEP_AT, t0 + SWEEP_AT + SWEEP
        g = [f'<g class="t{i}">']
        y = ROW0 + i * ROW_H
        g.append(text(repo, IDX_NAME, y + 21, 19, idx_f, c["ink"], ls=-0.015))
        g.append(text(f"{i + 1:02d}", X1 - mono.width(f"/ {len(TOOLS):02d}", 14) - 8, 132, 14, mono, c["ink"], anchor="end"))
        g.append(text(repo, DX, 210, 46, name_f, c["ink"], ls=-0.035))
        g.append(text(meta, DX, 242, 17, meta_f, c["mute"]))

        lines_in, lines_out = wrap(job_in, in_f, max_w), wrap(job_out, out_f, max_w)
        if len(lines_in) + len(lines_out) > 4:
            sys.exit(f"{repo}: the job takes {len(lines_in) + len(lines_out)} lines; shorten it")
        y_in = 312
        y_out = y_in + (len(lines_in) - 1) * lh + JOB * 1.42
        g.append(text("IN", DX, y_in - 2, 13, label_f, c["amber"], ls=0.14))
        g.append(text("OUT", DX, y_out - 2, 13, label_f, c["mint"], ls=0.14))
        g.append(draw_lines(lines_in, DX_TEXT, y_in, lh, c["mute"]))
        g.append(draw_lines(lines_out, DX_TEXT, y_out, lh, c["ink"]))

        # The seam: a cover over the output slides right and reveals it; the Ember line rides its left edge.
        reveal = max(line_width(l) for l in lines_out) + 8
        top_out, bottom = y_out - JOB * 0.92, y_out + (len(lines_out) - 1) * lh + JOB * 0.34
        g.append(f'<rect class="c{i}" x="{DX_TEXT - 3}" y="{top_out:.1f}" width="{reveal + 6:.1f}" height="{bottom - top_out:.1f}" fill="{c["bg"]}"/>')
        g.append(f'<rect class="s{i}" x="{DX_TEXT - 4}" y="{y_in - JOB * 0.92:.1f}" width="4" height="{bottom - y_in + JOB * 0.92:.1f}" fill="{c["ember"]}"{glow}/>')
        g.append("</g>")
        o.append("".join(g))

        css.append(toggle(f"v{i}", [(t0, t0 + SLOT)]))
        e = 0.001
        css.append(f"@keyframes c{i}{{0%{{transform:translateX(0)}}{pct(a)}{{transform:translateX(0);animation-timing-function:{EASE}}}"
                   f"{pct(b)}{{transform:translateX({reveal:.1f}px)}}100%{{transform:translateX({reveal:.1f}px)}}}}")
        css.append(f"@keyframes s{i}{{0%{{transform:translateX(0);opacity:0}}{pct(a - e)}{{transform:translateX(0);opacity:0}}"
                   f"{pct(a)}{{transform:translateX(0);opacity:1;animation-timing-function:{EASE}}}"
                   f"{pct(b)}{{transform:translateX({reveal:.1f}px);opacity:1}}{pct(b + e)}{{transform:translateX({reveal:.1f}px);opacity:0}}"
                   f"100%{{transform:translateX({reveal:.1f}px);opacity:0}}}}")
        base.append(f".t{i}{{opacity:{1 if i == 0 else 0}}}.c{i}{{transform:translateX({reveal:.1f}px)}}.s{i}{{opacity:0}}")

    rules = "".join(f".t{i}{{animation:v{i} {CYCLE}s step-end infinite}}.c{i}{{animation:c{i} {CYCLE}s linear infinite}}"
                    f".s{i}{{animation:s{i} {CYCLE}s linear infinite}}" for i in range(len(TOOLS)))
    rules += f".marker{{animation:marker {CYCLE}s step-end infinite}}"
    style = f"<style>{''.join(base)}@media (prefers-reduced-motion:no-preference){{{''.join(css)}{rules}}}</style>"

    defs = "".join(f'<path id="{gid}" d="{d}"/>' for gid, d in _glyphs.values() if d)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img">'
            f'{style}<defs>{defs}</defs><rect width="{W}" height="{H}" rx="18" fill="{c["bg"]}"/>{"".join(o)}</svg>')


for theme in THEMES:
    _glyphs.clear()
    path = os.path.join(OUT, f"board-{theme}.svg")
    svg = build(theme)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(svg + "\n")
    print(f"wrote {os.path.relpath(path)} ({os.path.getsize(path) // 1024} KB)")
