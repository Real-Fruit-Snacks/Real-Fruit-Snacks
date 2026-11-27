"""Draw the Real-Fruit-Snacks profile README board: assets/board-dark.svg & assets/board-light.svg.

World: Cyclorama Dawn (Steel & Beacon Orange).
Architecture: 17-Channel Stage Lighting DMX Patch Console (1000x548).
  - Row 1: Unified Cyclorama RFS tile, REAL-FRUIT-SNACKS masthead, and LX cue tag.
  - Row 2: Live Stage Patch Deck showing active channel identity, plain description,
           dwell progress bar, and recessed IN -> OUT Signal Patch Bay with Beacon scan reveal.
  - Row 3: 17-Channel Cyclorama Dawn DMX Fader Bank spanning all 17 active tools across
           the Steel -> Beacon Horizon -> Flame -> Alabaster spectrum. As each channel activates,
           its hardware fader cap glides smoothly up to 86% live output while its Beacon frame
           and cue LED lock in.

Static-First Invariant: Base DOM (outside prefers-reduced-motion: no-preference) renders
Channel #01 (screen-mark) at full live peak with unobstructed IN -> OUT traces and Channels
#02-#17 resting along the standby dawn curve—zero hidden content in static renderers or
reduced-motion mode.

All glyphs are outlined from self-hosted variable .woff2 fonts in art/fonts/ and deduplicated
via <use href="#..."/>, so SVGs render identically on GitHub camo, browsers, and resvg.

Run from the repo root:
    python -m pip install -r art/requirements.txt
    python art/make-board.py
"""
import os
import sys

from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "fonts")
OUT = os.path.join(HERE, "..", "assets")

# Live public active tools, synced 1:1 with Real-Fruit-Snacks.github.io/tools.json.
# Tuple: (repo, language, platform, description, in_text, out_text, short_lines)
TOOLS = [
    (
        "screen-mark",
        "Rust",
        "Windows, Linux",
        "Screenshot capture and annotation in pure Rust",
        "`Ctrl+PrintScreen`",
        "`screen-mark_2026-11-05_091412.png`",
        ("screen-", "mark"),
    ),
    (
        "port-sync",
        "Rust",
        "Windows",
        "Keeps qBittorrent's port synced to Proton VPN",
        "`Port pair 51037->51037`",
        "`listening port updated: 48213 -> 51037`",
        ("port-", "sync"),
    ),
    (
        "carify",
        "sh / PS",
        "Windows, macOS, Linux",
        "Convert video for Uconnect USB playback, via ffmpeg",
        "HEVC 10-bit · 1080p · AC3 5.1",
        "H.264 8-bit · 720p · AAC stereo",
        ("carify",),
    ),
    (
        "certapi",
        "C#",
        "Windows",
        "mTLS API client for the Windows certificate store",
        "a client certificate in `CurrentUser\\My`",
        "200 OK; the key never left the store",
        ("certapi",),
    ),
    (
        "identity-gen",
        "HTML",
        "Browser",
        "Offline generator for throwaway signup identities",
        "a signup form that wants too much",
        "a stand-in: name, handle, passphrase",
        ("identity-", "gen"),
    ),
    (
        "amazon-order-sync",
        "Rust",
        "Windows, Linux",
        "Syncs your Amazon orders into local Markdown notes",
        "Amazon's order history",
        "one `Order-<id>.md` per order",
        ("amazon-", "order-sync"),
    ),
    (
        "powershell-toolbox",
        "PowerShell",
        "Windows",
        "A grab-bag of my PowerShell scripts, each one standalone",
        "every repo your `gh` login sees",
        "one at a time: keep, archive or delete",
        ("powershell-", "toolbox"),
    ),
    (
        "pwn-broker",
        "Python",
        "Kali Linux",
        "Keeps a box's targets, notes, creds, and tools in order",
        "`pwn-broker new`",
        "`2026-11-16_htb_forest.finished.tar.gz`",
        ("pwn-", "broker"),
    ),
    (
        "pwn-shop",
        "Python",
        "Kali Linux",
        "Tool packages for pwn-broker, built from upstream releases",
        "an upstream release, pinned by SHA-256",
        "`kerbrute-1.0.3-1.zip`",
        ("pwn-", "shop"),
    ),
    (
        "pwn-playbooks",
        "Markdown",
        "Kali Linux",
        "Playbooks for pwn-broker: read into the note, fill in, run",
        "`:Pb smb` in the note window",
        "`Playbook: SMB enumeration`, to fill in",
        ("pwn-", "playbooks"),
    ),
    (
        "pwn-report",
        "Python",
        "Kali Linux",
        "Private, evidence-linked reports from pwn-broker archives",
        "`2026-11-16_htb_forest.finished.tar.gz`",
        "`report.md`, every file with its SHA-256",
        ("pwn-", "report"),
    ),
    (
        "open-file",
        "TypeScript",
        "Browser",
        "Learn and play chess in your browser, offline",
        "a blunder in one of your games",
        "a puzzle made from it",
        ("open-", "file"),
    ),
    (
        "one-billion-pixels",
        "TypeScript",
        "Browser",
        "Excavate one billion pixels in your browser, offline",
        "a single empty origin square",
        "one billion pixels carved offline",
        ("one-billion-", "pixels"),
    ),
    (
        "hash-bait",
        "Rust",
        "Windows, Linux",
        "Drop poisoned shortcuts on SMB shares to coerce NTLM hashes",
        "`//dc1/public` + responder IP",
        "poisoned `.url`/`.scf`/`.xml`, NetNTLMv2",
        ("hash-", "bait"),
    ),
    (
        "cred-spray",
        "Python",
        "Windows, Linux",
        "Bounded, protocol-aware credential spraying",
        "`scan.xml` + `credentials.txt`",
        "`results.json`, 7 explicit statuses",
        ("cred-", "spray"),
    ),
    (
        "ad-sweep",
        "Rust",
        "Windows, Linux",
        "Runs isolated Active Directory enumeration with NetExec",
        "`10.0.0.1-2` + `credentials.txt`",
        "ordered `results.json` per target",
        ("ad-", "sweep"),
    ),
    (
        "shell-tunnel",
        "Go",
        "Windows, Linux",
        "Static SSH server for bind and reverse shells, PTY and SFTP",
        "`./build.sh reverse 10.10.14.5:4444`",
        "PTY shell, SFTP & `-L`/`-R`/`-D` via ssh",
        ("shell-", "tunnel"),
    ),
]

# 17-step Cyclorama Dawn gel spectrum marching from Blackout Steel -> LX 263 Beacon Horizon -> Flame -> Alabaster Day
# (top_c, mid_c, bot_c, polarity)
CHANNEL_GELS = [
    ("#07090E", "#0E1520", "#16283B", "dark"),
    ("#080B12", "#112132", "#18364E", "dark"),
    ("#080E16", "#132C42", "#1B4463", "dark"),
    ("#09131C", "#163B57", "#1F547A", "dark"),
    ("#0B1620", "#194466", "#2D5B7B", "dark"),
    ("#0D1B28", "#1C4B6F", "#655858", "dark"),
    ("#102436", "#1E4D72", "#AE5126", "dark"),
    ("#122F46", "#1F547A", "#F06E2B", "dark"),
    ("#15202A", "#463B40", "#EC6A27", "dark"),
    ("#18100C", "#68280E", "#E86624", "dark"),
    ("#1A0A06", "#8B2F0B", "#F06E2B", "dark"),
    ("#210E08", "#9B3810", "#F27B3B", "dark"),
    ("#26120B", "#A63F14", "#F48A4C", "dark"),
    ("#2C1913", "#AE572F", "#E6B393", "dark"),
    ("#C9D8E4", "#E6DFDA", "#F9F1EC", "light"),
    ("#DCE5ED", "#EFE4DB", "#FDF8F5", "light"),
    ("#EAEEF2", "#F5F7F9", "#FFFFFF", "light"),
]

# Cyclorama Dawn — Steel & Beacon Orange (LX 263 Dark / LX 512 Alabaster Day)
THEMES = {
    "dark": dict(
        bg="#050507",
        card="#0C0C10",
        deck="rgba(12,12,16,0.90)",
        code_bg="#08080B",
        line="#27272E",
        line_strong="#464852",
        frame="rgba(255,255,255,0.14)",
        ink="#F4F5F8",
        mute="#B3B5C0",
        steel="#74B8E8",
        steel_fill="#18496B",
        beacon="#FF9254",
        beam="#F06E2B",
        wash_op="0.44",
        rule_a="#74B8E8",
        rule_b="#3B85B8",
        rule_c="#F06E2B",
    ),
    "light": dict(
        bg="#F5F7F9",
        card="#FFFFFF",
        deck="rgba(255,255,255,0.94)",
        code_bg="#EEF2F5",
        line="#CFD5DC",
        line_strong="#8B94A0",
        frame="rgba(13,16,22,0.15)",
        ink="#0D1016",
        mute="#474D59",
        steel="#164669",
        steel_fill="#18496B",
        beacon="#AD3D0A",
        beam="#D85B1C",
        wash_op="0.14",
        rule_a="#18496B",
        rule_b="#1F547A",
        rule_c="#AD3D0A",
    ),
}

W, H = 1000, 548
SLOT = 3.2
CYCLE = SLOT * len(TOOLS)
SWEEP_AT, SWEEP = 0.35, 0.80
FADER_MOVE = 0.42
EASE = "cubic-bezier(0.16,1,0.3,1)"

DISPLAY = "big-shoulders-stencil-latin.woff2"
SANS = "albert-sans-latin.woff2"
MONO = "azeret-mono-latin.woff2"
_files = {}
_faces = {}
_glyphs = {}


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

    def ink_box(self, s, size, ls=0.0):
        k = size / self.upm
        track = ls * self.upm
        pen_x = 0.0
        min_x, min_y, max_x, max_y = 1e9, 1e9, -1e9, -1e9
        for n in self.names(s):
            bp = BoundsPen(self.gs)
            self.gs[n].draw(bp)
            if bp.bounds:
                x0, y0, x1, y1 = bp.bounds
                min_x = min(min_x, (pen_x + x0) * k)
                max_x = max(max_x, (pen_x + x1) * k)
                min_y = min(min_y, -y1 * k)
                max_y = max(max_y, -y0 * k)
            pen_x += self.gs[n].width + track
        return min_x, min_y, max_x, max_y


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
    w = fc.width(s, size, ls)
    if anchor == "end":
        x -= w
    elif anchor == "middle":
        x -= w / 2.0
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


def tokens(s, sans, mono_fc, base_sz):
    out, runs, buf, code, space = [], [], "", False, False

    def flush_run():
        nonlocal buf
        if buf:
            runs.append((buf, mono_fc if code else sans, base_sz * 0.84 if code else base_sz))
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


def wrap_rich(s, sans, mono_fc, base_sz, max_w):
    lines, line, x = [], [], 0.0
    for space, runs in tokens(s, sans, mono_fc, base_sz):
        w = sum(fc.width(t, sz, -0.01) for t, fc, sz in runs)
        gap = sans.width(" ", base_sz) if space and line else 0.0
        if line and x + gap + w > max_w:
            lines.append(line)
            line, x, gap = [], 0.0, 0.0
        line.append((x + gap, runs))
        x += gap + w
    if line:
        lines.append(line)
    return lines


def wrap_plain(s, fc, sz, max_w):
    lines, cur = [], ""
    for word in s.split():
        trial = f"{cur} {word}".strip()
        if cur and fc.width(trial, sz) > max_w:
            lines.append(cur)
            cur = word
        else:
            cur = trial
    if cur:
        lines.append(cur)
    return lines


def line_width(line):
    x, runs = line[-1]
    return x + sum(fc.width(t, sz, -0.01) for t, fc, sz in runs)


def draw_rich_lines(lines, x, y, lh, fill):
    o = []
    for i, line in enumerate(lines):
        for lx, runs in line:
            px = x + lx
            for t, fc, sz in runs:
                o.append(text(t, px, y + i * lh, sz, fc, fill, ls=-0.01))
                px += fc.width(t, sz, -0.01)
    return "".join(o)


def pct(t):
    return f"{(t / CYCLE) * 100:.3f}%"


def toggle_kf(name, t0, t1):
    """Step-end visibility keyframe active strictly on [t0, t1)."""
    pts = [(0.0, 1 if t0 <= 0.0 < t1 else 0)]
    if 0.0 < t0 < CYCLE:
        pts.append((t0, 1))
    if 0.0 < t1 < CYCLE:
        pts.append((t1, 0))
    body = "".join(f"{pct(t)}{{opacity:{v}}}" for t, v in pts)
    return f"@keyframes {name}{{{body}100%{{opacity:{pts[0][1]}}}}}"


def rfs_tile(c, theme, tx, ty, ts, disp):
    """Unified Cyclorama Dawn RFS Monogram Tile matching rfs-mark-{dark,light}.svg."""
    rx = round(14.0 * ts / 64.0, 2)
    sz = ts * (31.0 / 64.0)
    ls = 0.05
    bx0, by0, bx1, by1 = disp.ink_box("RFS", sz, ls)
    ink_w, ink_h = bx1 - bx0, by1 - by0
    gap = ts * (5.0 / 64.0)
    bar_h = ts * (3.8 / 64.0)
    group_h = ink_h + gap + bar_h
    group_top = ty + (ts - group_h) / 2.0
    cx = tx + ts / 2.0 - (bx0 + bx1) / 2.0
    cy = group_top - by0
    bar_y = group_top + ink_h + gap

    if theme == "dark":
        bg = (
            f'<rect x="{tx}" y="{ty}" width="{ts}" height="{ts}" rx="{rx}" fill="#050507"/>'
            f'<rect x="{tx}" y="{ty}" width="{ts}" height="{ts}" rx="{rx}" fill="url(#cyc-h)" opacity="0.76" mask="url(#tile-m)"/>'
            f'<rect x="{tx + 0.6}" y="{ty + 0.6}" width="{ts - 1.2}" height="{ts - 1.2}" '
            f'rx="{max(0, rx - 0.6):.2f}" fill="none" stroke="rgba(255,255,255,0.18)" stroke-width="1.2"/>'
        )
        fg = "#F4F5F8"
        bar_fill = "url(#rule)"
    else:
        bg = (
            f'<rect x="{tx + 0.75}" y="{ty + 0.75}" width="{ts - 1.5}" height="{ts - 1.5}" '
            f'rx="{max(0, rx - 0.75):.2f}" fill="#FFFFFF" stroke="{c["line"]}" stroke-width="1.5"/>'
        )
        fg = c["ink"]
        bar_fill = "url(#rule)"

    glyph_el = text("RFS", cx, cy, sz, disp, fg, ls=ls)
    bar = f'<rect x="{tx + (ts - ink_w) / 2.0:.2f}" y="{bar_y:.2f}" width="{ink_w:.2f}" height="{bar_h:.2f}" rx="{bar_h / 2.0:.2f}" fill="{bar_fill}"/>'
    return bg + glyph_el + bar


def build(theme):
    c = THEMES[theme]
    disp = face(DISPLAY, 800)
    sans_r = face(SANS, 450)
    sans_m = face(SANS, 600)
    sans_b = face(SANS, 680)
    mono_r = face(MONO, 450)
    mono_b = face(MONO, 600)

    o, css, base, rules = [], [], [], []

    # 1. Outer Console Chassis + Cyclorama Dawn floor wash
    o.append(f'<rect width="{W}" height="{H}" fill="{c["bg"]}"/>')
    o.append(f'<rect width="{W}" height="{H}" fill="url(#cyc-h)" opacity="{c["wash_op"]}" mask="url(#cyc-m)"/>')
    o.append(f'<rect x="0" y="{H - 3}" width="{W}" height="3" fill="url(#rule)"/>')
    o.append(f'<rect x="0.75" y="0.75" width="{W - 1.5}" height="{H - 1.5}" rx="17.25" fill="none" stroke="{c["frame"]}" stroke-width="1.5"/>')

    # 2. Row 1: Console Masthead
    o.append(rfs_tile(c, theme, 32, 22, 42, disp))
    o.append(text("REAL-FRUIT-SNACKS", 88, 49, 30, disp, c["ink"], ls=0.05))
    o.append(text("BUILT LOCAL-FIRST.", 88, 63, 10, mono_b, c["steel"], ls=0.09))

    cue_tag = "LX 263 · BEACON HORIZON" if theme == "dark" else "LX 512 · ALABASTER DAY"
    o.append(text(cue_tag, 968, 39, 10.5, mono_b, c["steel"], ls=0.08, anchor="end"))
    o.append(text("real-fruit-snacks.github.io  ·  rfs.tools", 968, 58, 10, mono_r, c["mute"], ls=0.03, anchor="end"))
    o.append(f'<rect x="32" y="76" width="936" height="2" rx="1" fill="url(#rule)"/>')

    # 3. Row 2: Active Stage Patch Deck (x=32, y=92, w=936, h=198)
    DECK_X, DECK_Y, DECK_W, DECK_H = 32, 92, 936, 198
    o.append(f'<rect x="{DECK_X}" y="{DECK_Y}" width="{DECK_W}" height="{DECK_H}" rx="12" fill="{c["card"]}"/>')
    o.append(f'<rect x="{DECK_X}" y="{DECK_Y}" width="{DECK_W}" height="3.5" fill="url(#rule)" clip-path="url(#deck-clip)"/>')
    o.append(f'<rect x="{DECK_X + 0.5}" y="{DECK_Y + 0.5}" width="{DECK_W - 1}" height="{DECK_H - 1}" rx="11.5" fill="none" stroke="{c["line"]}"/>')

    # Vertical divider separating identity column (left) & signal patch bay (right)
    o.append(f'<line x1="398" y1="112" x2="398" y2="270" stroke="{c["line"]}" stroke-width="1"/>')

    # Static structural frame for Signal Patch Bay on right
    BAY_X, BAY_W = 422, 522
    o.append(text("SIGNAL PATCH BAY", BAY_X, 123, 9.5, mono_b, c["mute"], ls=0.10))
    o.append(text("LOCAL EXECUTION · ZERO ACCOUNTS", BAY_X + BAY_W, 123, 9.5, mono_r, c["steel"], ls=0.06, anchor="end"))

    # Recessed IN box (y=134..192) & OUT box (y=212..270) with corner-clipped accent rails
    IN_Y, OUT_Y, BOX_H = 134, 212, 58
    o.append(f'<rect x="{BAY_X}" y="{IN_Y}" width="{BAY_W}" height="{BOX_H}" rx="4" fill="{c["code_bg"]}"/>')
    o.append(f'<rect x="{BAY_X}" y="{IN_Y}" width="3.5" height="{BOX_H}" fill="{c["steel"]}" clip-path="url(#in-box-clip)"/>')
    o.append(f'<rect x="{BAY_X + 0.5}" y="{IN_Y + 0.5}" width="{BAY_W - 1}" height="{BOX_H - 1}" rx="3.5" fill="none" stroke="{c["line"]}"/>')
    o.append(text("IN", BAY_X + 16, IN_Y + 33, 10.5, mono_b, c["steel"], ls=0.12))

    # Signal Conduit Bridge between IN and OUT (use <rect> so objectBoundingBox linearGradient renders cleanly)
    bridge_y = 202
    o.append(f'<rect x="{BAY_X}" y="{bridge_y - 0.75}" width="{BAY_W}" height="1.5" rx="0.75" fill="url(#rule)" opacity="0.78"/>')
    o.append(f'<rect x="{BAY_X + 208}" y="{bridge_y - 8.5}" width="106" height="17" rx="2" fill="{c["card"]}" stroke="{c["line"]}" stroke-width="1"/>')
    o.append(text("IN -> OUT", BAY_X + 261, bridge_y + 3.2, 9, mono_b, c["beacon"], ls=0.10, anchor="middle"))

    o.append(f'<rect x="{BAY_X}" y="{OUT_Y}" width="{BAY_W}" height="{BOX_H}" rx="4" fill="{c["code_bg"]}"/>')
    o.append(f'<rect x="{BAY_X}" y="{OUT_Y}" width="3.5" height="{BOX_H}" fill="{c["beam"]}" clip-path="url(#out-box-clip)"/>')
    o.append(f'<rect x="{BAY_X + 0.5}" y="{OUT_Y + 0.5}" width="{BAY_W - 1}" height="{BOX_H - 1}" rx="3.5" fill="none" stroke="{c["line"]}"/>')
    o.append(text("OUT", BAY_X + 16, OUT_Y + 33, 10.5, mono_b, c["beacon"], ls=0.12))

    # Dwell progress track under left identity column
    PROG_X, PROG_Y, PROG_W = 56, 268, 318
    o.append(f'<rect x="{PROG_X}" y="{PROG_Y}" width="{PROG_W}" height="3" rx="1.5" fill="{c["line"]}"/>')
    o.append(f'<rect class="dwell-bar" x="{PROG_X}" y="{PROG_Y}" width="{PROG_W}" height="3" rx="1.5" fill="url(#rule)"/>')
    css.append("@keyframes dwell{0%{transform:scaleX(0)}100%{transform:scaleX(1)}}")
    rules.append(f".dwell-bar{{transform-origin:{PROG_X}px {PROG_Y}px;animation:dwell {SLOT}s linear infinite}}")

    # 4. Row 3: 17-Channel Cyclorama Dawn DMX Fader Bank (x=32, y=304, w=936, h=222)
    BANK_X, BANK_Y, BANK_W, BANK_H = 32, 304, 936, 222
    o.append(f'<rect x="{BANK_X}" y="{BANK_Y}" width="{BANK_W}" height="{BANK_H}" rx="12" fill="{c["deck"]}" stroke="{c["line"]}" stroke-width="1.2"/>')
    o.append(text(f"CYCLORAMA DAWN  ·  {len(TOOLS)}-CHANNEL DMX FADER BANK", BANK_X + 20, BANK_Y + 23, 10, mono_b, c["steel"], ls=0.10))
    o.append(text("LX 001 — 512", BANK_X + BANK_W - 20, BANK_Y + 23, 10, mono_r, c["mute"], ls=0.08, anchor="end"))
    o.append(f'<rect x="{BANK_X + 20}" y="{BANK_Y + 33}" width="{BANK_W - 40}" height="1" fill="{c["line"]}"/>')

    # Fader channel grid geometry
    n = len(TOOLS)
    col_gap = 5.0
    cols_x = BANK_X + 18.0
    cols_w = BANK_W - 36.0
    col_w = (cols_w - col_gap * (n - 1)) / n  # ~48.24px per channel for 17 tools
    col_top = BANK_Y + 43.0
    col_h = 122.0
    col_bot = col_top + col_h
    slot_top = col_top + 18.0
    slot_bot = col_bot - 16.0
    slot_span = slot_bot - slot_top
    led_rest_w = 22.0
    led_lit_w = 26.0
    tick_hw = 4.0
    cap_w, cap_h = round(col_w * 0.58, 1), 10.5

    # Draw static fader columns + slots + standby ticks + resting labels first
    col_meta = []
    for i, (repo, lang, plat, desc, job_in, job_out, short_lines) in enumerate(TOOLS):
        cx = cols_x + i * (col_w + col_gap)
        mid_x = cx + col_w / 2.0
        polarity = CHANNEL_GELS[i][3]
        slot_stroke = "rgba(255,255,255,0.22)" if polarity == "dark" else "rgba(13,16,22,0.18)"
        led_dim = "rgba(255,255,255,0.20)" if polarity == "dark" else "rgba(13,16,22,0.16)"

        # Gel-lit vertical channel background
        o.append(
            f'<rect x="{cx:.1f}" y="{col_top:.1f}" width="{col_w:.1f}" height="{col_h:.1f}" '
            f'rx="6" fill="url(#ch-{i})" stroke="{c["line"]}" stroke-width="1"/>'
        )
        # Resting dim top LED bar
        o.append(f'<rect x="{mid_x - led_rest_w / 2:.1f}" y="{col_top + 6:.1f}" width="{led_rest_w:.1f}" height="3" rx="1.5" fill="{led_dim}"/>')
        # Vertical DMX fader slot + 3 micro calibration ticks
        o.append(f'<line x1="{mid_x:.1f}" y1="{slot_top:.1f}" x2="{mid_x:.1f}" y2="{slot_bot:.1f}" stroke="{slot_stroke}" stroke-width="1.5" stroke-linecap="round"/>')
        for frac in (0.25, 0.5, 0.75):
            ty = slot_bot - frac * slot_span
            o.append(f'<line x1="{mid_x - tick_hw:.1f}" y1="{ty:.1f}" x2="{mid_x + tick_hw:.1f}" y2="{ty:.1f}" stroke="{slot_stroke}" stroke-width="1"/>')

        # Resting muted channel number & repo label under column
        o.append(text(f"{i + 1:02d}", mid_x, col_bot + 16, 8.5, mono_b, c["mute"], ls=0.05, anchor="middle"))
        for li, sline in enumerate(short_lines):
            o.append(text(sline, mid_x, col_bot + 28 + li * 10.0, 8.0, sans_m, c["mute"], anchor="middle"))

        rest_level = 0.16 + 0.34 * (i / (n - 1))
        peak_level = 0.86
        rest_y = slot_bot - rest_level * slot_span
        peak_y = slot_bot - peak_level * slot_span
        col_meta.append((cx, mid_x, polarity, rest_y, peak_y))

    # 5. Per-Tool Active Stage Viewport + Active Fader Highlight + Animated Hardware Fader Cap
    TEXT_X = BAY_X + 56
    MAX_IO_W = (BAY_X + BAY_W - 16) - TEXT_X
    IO_SZ = 18.0
    IO_LH = 22.0

    for i, (repo, lang, plat, desc, job_in, job_out, short_lines) in enumerate(TOOLS):
        t0 = i * SLOT
        t1 = (i + 1) * SLOT
        a = t0 + SWEEP_AT
        b = t0 + SWEEP_AT + SWEEP
        init_op = "" if i == 0 else ' opacity="0"'
        cx, mid_x, polarity, rest_y, peak_y = col_meta[i]

        # ---- Active Stage Group (Viewport + Active Channel Frame/LED/Label) ----
        g = [f'<g class="t{i}"{init_op}>']

        # Terminal Token Cue Tag ([ch 01/17]) + Stack/Platform
        ch_lbl = f"[ch {i + 1:02d}/{n:02d}]"
        tag_w = mono_b.width(ch_lbl, 10, 0.04) + 16
        g.append(f'<rect x="56" y="112" width="{tag_w:.1f}" height="22" rx="4" fill="{c["code_bg"]}" stroke="{c["line"]}"/>')
        g.append(text(ch_lbl, 64, 126.5, 10, mono_b, c["beacon"], ls=0.04))

        stack_txt = f"{lang.upper()} · {plat.upper()}"
        stack_x = 56 + tag_w + 10
        stack_avail = 382 - stack_x
        stack_sz = 9.5
        while mono_r.width(stack_txt, stack_sz, 0.04) > stack_avail and stack_sz > 7.5:
            stack_sz -= 0.5
        g.append(text(stack_txt, stack_x, 126.5, stack_sz, mono_r, c["steel"], ls=0.04))

        # Monumental Repo Slug (auto-fitted cleanly to 322px left column)
        slug_up = repo.upper()
        slug_sz = 50.0
        while disp.width(slug_up, slug_sz, 0.045) > 322 and slug_sz > 30:
            slug_sz -= 1.0
        g.append(text(slug_up, 56, 188, slug_sz, disp, c["ink"], ls=0.045))

        # Plain description (max 2 lines)
        desc_lines = wrap_plain(desc, sans_r, 13.5, 322)
        for di, dl in enumerate(desc_lines[:2]):
            g.append(text(dl, 56, 216 + di * 19, 13.5, sans_r, c["mute"]))

        # IN & OUT Signal Patch traces (vertically centered in each 58px slot)
        lines_in = wrap_rich(job_in, sans_r, mono_r, IO_SZ, MAX_IO_W)
        lines_out = wrap_rich(job_out, sans_m, mono_b, IO_SZ, MAX_IO_W)
        if len(lines_in) > 2 or len(lines_out) > 2:
            sys.exit(f"{repo}: IN/OUT exceeds 2 lines ({len(lines_in)}/{len(lines_out)})")

        y_in = IN_Y + (34.5 if len(lines_in) == 1 else 24.0)
        y_out = OUT_Y + (34.5 if len(lines_out) == 1 else 24.0)
        g.append(draw_rich_lines(lines_in, TEXT_X, y_in, IO_LH, c["mute"]))
        g.append(draw_rich_lines(lines_out, TEXT_X, y_out, IO_LH, c["ink"]))

        # Beacon Scan Beam reveal strictly clipped to OUT text slot (opacity="0" in static base state!)
        reveal = max(line_width(l) for l in lines_out) + 12
        g.append(
            f'<g clip-path="url(#out-clip)">'
            f'<rect class="c{i}" x="{TEXT_X - 4}" y="{OUT_Y + 4}" width="{reveal + 10:.1f}" height="{BOX_H - 8}" fill="{c["code_bg"]}" opacity="0"/>'
            f'<rect class="s{i}" x="{TEXT_X - 4}" y="{OUT_Y + 6}" width="3.5" height="{BOX_H - 12}" rx="1.75" fill="{c["beam"]}" opacity="0"/>'
            f'</g>'
        )

        # Active Fader Channel Frame + Lit Top LED + Highlighted Channel Number & Repo Label
        led_lit = "#FFFFFF" if polarity == "dark" else c["beam"]
        g.append(
            f'<rect x="{cx:.1f}" y="{col_top:.1f}" width="{col_w:.1f}" height="{col_h:.1f}" '
            f'rx="6" fill="none" stroke="{c["beam"]}" stroke-width="2.2"/>'
        )
        g.append(f'<rect x="{mid_x - led_lit_w / 2:.1f}" y="{col_top + 5.5:.1f}" width="{led_lit_w:.1f}" height="3.5" rx="1.75" fill="{led_lit}"/>')
        g.append(text(f"{i + 1:02d}", mid_x, col_bot + 16, 8.5, mono_b, c["beacon"], ls=0.05, anchor="middle"))
        for li, sline in enumerate(short_lines):
            g.append(text(sline, mid_x, col_bot + 28 + li * 10.0, 8.0, sans_b, c["ink"], anchor="middle"))

        g.append("</g>")
        o.append("".join(g))

        # ---- Hardware Fader Cap (drawn ON TOP of active frame; glides up to 86% live peak!) ----
        cap_fill = "#FFFFFF" if polarity == "dark" else "#0D1016"
        cap_stroke = "#050507" if polarity == "dark" else "#FFFFFF"
        base_y = peak_y if i == 0 else rest_y
        notch_base_op = "1" if i == 0 else "0"

        cap_svg = (
            f'<g class="cap{i}">'
            f'<rect x="{mid_x - cap_w / 2:.1f}" y="{base_y - cap_h / 2:.1f}" width="{cap_w:.1f}" height="{cap_h:.1f}" '
            f'rx="2.5" fill="{cap_fill}" stroke="{cap_stroke}" stroke-width="1.2"/>'
            f'<line x1="{mid_x - cap_w / 2 + 4:.1f}" y1="{base_y:.1f}" x2="{mid_x + cap_w / 2 - 4:.1f}" y2="{base_y:.1f}" '
            f'stroke="{cap_stroke}" stroke-width="1.5" opacity="0.55"/>'
            f'<line class="t{i}" x1="{mid_x - cap_w / 2 + 3.5:.1f}" y1="{base_y:.1f}" x2="{mid_x + cap_w / 2 - 3.5:.1f}" y2="{base_y:.1f}" '
            f'stroke="{c["beam"]}" stroke-width="2.2" opacity="{notch_base_op}"/>'
            f'</g>'
        )
        o.append(cap_svg)

        # ---- Keyframes ----
        css.append(toggle_kf(f"v{i}", t0, t1))
        e = 0.001
        css.append(
            f"@keyframes c{i}{{0%{{transform:translateX(0);opacity:1}}"
            f"{pct(a)}{{transform:translateX(0);opacity:1;animation-timing-function:{EASE}}}"
            f"{pct(b)}{{transform:translateX({reveal:.1f}px);opacity:1}}"
            f"{pct(b + e)}{{transform:translateX({reveal:.1f}px);opacity:0}}"
            f"100%{{transform:translateX({reveal:.1f}px);opacity:0}}}}"
        )
        css.append(
            f"@keyframes s{i}{{0%{{transform:translateX(0);opacity:0}}{pct(a - e)}{{transform:translateX(0);opacity:0}}"
            f"{pct(a)}{{transform:translateX(0);opacity:1;animation-timing-function:{EASE}}}"
            f"{pct(b)}{{transform:translateX({reveal:.1f}px);opacity:1}}{pct(b + e)}{{transform:translateX({reveal:.1f}px);opacity:0}}"
            f"100%{{transform:translateX({reveal:.1f}px);opacity:0}}}}"
        )

        # Hardware fader cap motion keyframe (compositor-only translateY)
        lift = rest_y - peak_y
        if i == 0:
            # Base position is peak_y (0); drops to +lift when slot 0 ends, climbs back to 0 right before cycle wrap
            css.append(
                f"@keyframes cap0{{"
                f"0%{{transform:translateY(0)}}"
                f"{pct(t1)}{{transform:translateY(0);animation-timing-function:{EASE}}}"
                f"{pct(t1 + FADER_MOVE)}{{transform:translateY({lift:.1f}px)}}"
                f"{pct(CYCLE - FADER_MOVE)}{{transform:translateY({lift:.1f}px);animation-timing-function:{EASE}}}"
                f"100%{{transform:translateY(0)}}}}"
            )
        else:
            # Base position is rest_y (0); climbs smoothly to -lift at t0, drops back to 0 after t1
            t_up_end = min(CYCLE - 0.01, t0 + FADER_MOVE)
            if t1 < CYCLE:
                t_dn_end = min(CYCLE, t1 + FADER_MOVE)
                css.append(
                    f"@keyframes cap{i}{{"
                    f"0%{{transform:translateY(0)}}"
                    f"{pct(t0)}{{transform:translateY(0);animation-timing-function:{EASE}}}"
                    f"{pct(t_up_end)}{{transform:translateY({-lift:.1f}px)}}"
                    f"{pct(t1)}{{transform:translateY({-lift:.1f}px);animation-timing-function:{EASE}}}"
                    f"{pct(t_dn_end)}{{transform:translateY(0)}}"
                    f"100%{{transform:translateY(0)}}}}"
                )
            else:
                # Last channel: lifts at t0, returns smoothly right before cycle end
                css.append(
                    f"@keyframes cap{i}{{"
                    f"0%{{transform:translateY(0)}}"
                    f"{pct(t0)}{{transform:translateY(0);animation-timing-function:{EASE}}}"
                    f"{pct(t_up_end)}{{transform:translateY({-lift:.1f}px)}}"
                    f"{pct(CYCLE - FADER_MOVE)}{{transform:translateY({-lift:.1f}px);animation-timing-function:{EASE}}}"
                    f"100%{{transform:translateY(0)}}}}"
                )

        base.append(f".t{i}{{opacity:{1 if i == 0 else 0}}}.c{i}{{opacity:0}}.s{i}{{opacity:0}}")
        rules.append(
            f".t{i}{{animation:v{i} {CYCLE}s step-end infinite}}"
            f".c{i}{{animation:c{i} {CYCLE}s linear infinite}}"
            f".s{i}{{animation:s{i} {CYCLE}s linear infinite}}"
            f".cap{i}{{animation:cap{i} {CYCLE}s linear infinite}}"
        )

    style = f"<style>{''.join(base)}@media (prefers-reduced-motion:no-preference){{{''.join(css)}{''.join(rules)}}}</style>"

    # Gradients, masks, clips, and deduplicated glyph paths
    gel_defs = "".join(
        f'<linearGradient id="ch-{i}" x1="0%" y1="0%" x2="0%" y2="100%">'
        f'<stop offset="0%" stop-color="{top_c}"/>'
        f'<stop offset="56%" stop-color="{mid_c}"/>'
        f'<stop offset="100%" stop-color="{bot_c}"/>'
        f'</linearGradient>'
        for i, (top_c, mid_c, bot_c, _) in enumerate(CHANNEL_GELS)
    )
    grad_defs = (
        f'<linearGradient id="cyc-h" x1="0%" y1="0%" x2="100%" y2="0%">'
        f'<stop offset="0%" stop-color="#133954"/><stop offset="44%" stop-color="#1F547A"/>'
        f'<stop offset="76%" stop-color="#CC5016"/><stop offset="100%" stop-color="#F06E2B"/>'
        f'</linearGradient>'
        f'<linearGradient id="cyc-f" x1="0%" y1="0%" x2="0%" y2="100%">'
        f'<stop offset="0%" stop-color="#FFFFFF" stop-opacity="0"/>'
        f'<stop offset="42%" stop-color="#FFFFFF" stop-opacity="0.06"/>'
        f'<stop offset="76%" stop-color="#FFFFFF" stop-opacity="0.45"/>'
        f'<stop offset="100%" stop-color="#FFFFFF" stop-opacity="1"/>'
        f'</linearGradient>'
        f'<mask id="cyc-m"><rect width="{W}" height="{H}" fill="url(#cyc-f)"/></mask>'
        f'<linearGradient id="tile-f" x1="0%" y1="0%" x2="0%" y2="100%">'
        f'<stop offset="0%" stop-color="#FFFFFF" stop-opacity="0"/>'
        f'<stop offset="42%" stop-color="#FFFFFF" stop-opacity="0.08"/>'
        f'<stop offset="74%" stop-color="#FFFFFF" stop-opacity="0.58"/>'
        f'<stop offset="100%" stop-color="#FFFFFF" stop-opacity="1"/>'
        f'</linearGradient>'
        f'<mask id="tile-m" maskContentUnits="objectBoundingBox"><rect width="1" height="1" fill="url(#tile-f)"/></mask>'
        f'<linearGradient id="rule" x1="0%" y1="0%" x2="100%" y2="0%">'
        f'<stop offset="0%" stop-color="{c["rule_a"]}"/>'
        f'<stop offset="52%" stop-color="{c["rule_b"]}"/>'
        f'<stop offset="100%" stop-color="{c["rule_c"]}"/>'
        f'</linearGradient>'
        f'<clipPath id="outer-clip"><rect width="{W}" height="{H}" rx="18"/></clipPath>'
        f'<clipPath id="deck-clip"><rect x="{DECK_X}" y="{DECK_Y}" width="{DECK_W}" height="{DECK_H}" rx="12"/></clipPath>'
        f'<clipPath id="in-box-clip"><rect x="{BAY_X}" y="{IN_Y}" width="{BAY_W}" height="{BOX_H}" rx="4"/></clipPath>'
        f'<clipPath id="out-box-clip"><rect x="{BAY_X}" y="{OUT_Y}" width="{BAY_W}" height="{BOX_H}" rx="4"/></clipPath>'
        f'<clipPath id="out-clip"><rect x="{TEXT_X - 6}" y="{OUT_Y + 2}" width="{MAX_IO_W + 18}" height="{BOX_H - 4}"/></clipPath>'
        + gel_defs
    )
    glyph_defs = "".join(f'<path id="{gid}" d="{d}"/>' for gid, d in _glyphs.values() if d)

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
        f'aria-label="Real-Fruit-Snacks {n}-Channel Cyclorama Dawn DMX Patch Console showing all {n} active open-source tools and their IN to OUT signal traces.">'
        f'{style}<defs>{grad_defs}{glyph_defs}</defs>'
        f'<g clip-path="url(#outer-clip)">{"".join(o)}</g></svg>'
    )


def main():
    os.makedirs(OUT, exist_ok=True)
    for theme in THEMES:
        _glyphs.clear()
        path = os.path.join(OUT, f"board-{theme}.svg")
        svg = build(theme)
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(svg + "\n")
        print(f"wrote {os.path.relpath(path)} ({os.path.getsize(path) // 1024} KB)")


if __name__ == "__main__":
    main()
