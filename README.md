<div align="center">

  # Real-Fruit-Snacks

  **Water-themed offensive security toolkit.**

  [![License: MIT](https://img.shields.io/badge/License-MIT-cba6f7.svg)](https://opensource.org/licenses/MIT)
  
  [Documentation](https://real-fruit-snacks.github.io/) • [Report Issue](https://github.com/Real-Fruit-Snacks/Real-Fruit-Snacks/issues)

</div>

---

## Overview

Real-Fruit-Snacks is a **personal offensive-security toolkit** maintained as ~50 independent GitHub repositories under a single org umbrella. Every project is field-built for authorized red team engagements, pentests, and security research — not academic exercises.

The toolkit spans the full operator workflow: payload delivery, C2, post-exploitation, lateral movement, AD enumeration, credential abuse, and reference environments for the lab. Each tool ships standalone — no shared runtime, no monorepo lock-in. Pick what you need.

*A pantry of real, authentic offensive tooling — no hollow snacks, no corporate filler. Each release is its own discrete drop in the bucket; together they form the watershed.*

### Key Features

- **Massive Toolkit**: 50+ projects across 8 functional categories including C2 frameworks, tunneling, and enumeration.
- **Polyglot Implementations**: Built across 11 stacks including Rust, Go, Python, C, x86 ASM, JS, TS, Lua, Zig, Shell, and HTML.
- **Unified Aesthetic**: Bound by a shared Catppuccin Mocha + Latte color scheme and brutalist branding.
- **No Lock-in**: Standalone deployment with no shared runtime.
- **Multi-call Binaries**: Includes a sail-themed sextet of multi-call binaries demonstrating identical functionalities across six different languages.

---

## C2 & Post-Exploitation

| Tool | What It Does | Language |
|------|--------------|----------|
| [**Kraken**](https://github.com/Real-Fruit-Snacks/Kraken) | OPSEC-first C2 — X25519 ECDH, AES-256-GCM, modular implant with runtime-loadable modules, mesh networking, multi-transport (HTTP/HTTPS/TCP/SMB/DNS), BOF compatibility | Rust |
| [**Aquifer**](https://github.com/Real-Fruit-Snacks/Aquifer) | Linux post-exploitation — kernel namespace isolation, multi-channel C2, polymorphic beacons, 36 stealth modules | Go |
| [**Siphon**](https://github.com/Real-Fruit-Snacks/Siphon) | Lightweight C2 — ECDH P-256 forward secrecy, AES-256-GCM transport, uTLS Chrome fingerprinting | Go |
| [**Wellspring**](https://github.com/Real-Fruit-Snacks/Wellspring) | Payload delivery server — 12 delivery methods, token-gated access, AES-256-GCM at rest, memory zeroing. Single binary. | Go |
| [**Spillway**](https://github.com/Real-Fruit-Snacks/Spillway) | Reverse/bind/dormant FUSE mount — browse remote filesystems locally over TLS 1.3 with mutual PSK auth | Go |

---

## Network & Tunneling

| Tool | What It Does | Language |
|------|--------------|----------|
| [**Flux**](https://github.com/Real-Fruit-Snacks/Flux) | Swiss Army Netcat — replaces nc/ncat/socat/pwncat. TLS + Noise encryption, auto-PTY shells, file transfer with SHA256, SOCKS5 pivoting, TCP scanning. Single static binary. | Rust |
| [**Neap**](https://github.com/Real-Fruit-Snacks/Neap) | Static SSH server — reverse/bind shells with full PTY, SFTP, local/remote/dynamic port forwarding, TLS with SNI spoofing | Rust |
| [**Undertow**](https://github.com/Real-Fruit-Snacks/Undertow) | Static SSH server — reverse/bind shells, SFTP, port forwarding, TLS wrapping with SNI spoofing. Under 1.5 MB. | Go |
| [**Slipstream**](https://github.com/Real-Fruit-Snacks/Slipstream) | Drop-in SSH wrapper — tunnel management, file transfers, passive filesystem mapping, per-command logging, fingerprint identity | Rust |
| [**Conduit**](https://github.com/Real-Fruit-Snacks/Conduit) | SOCAT relay with kernel-level process masquerading — prctl/setproctitle stealth, argument hiding, 50+ channel types | C |
| [**Culvert**](https://github.com/Real-Fruit-Snacks/Culvert) | Pivot under the obstruction — one-command ligolo-ng tunnel setup with TUN, routing, magic 240/4 localhost CIDR, and WebUI | Shell |
| [**Depth**](https://github.com/Real-Fruit-Snacks/Depth) | Full SSH-2.0 in pure assembly — ChaCha20-Poly1305, Ed25519, X25519, SFTP, PTY, port forwarding. 94 KB static ELF, no libc. | x86 ASM |

---

## Shells & Implants

| Tool | What It Does | Language |
|------|--------------|----------|
| [**Vapor**](https://github.com/Real-Fruit-Snacks/Vapor) | Encrypted reverse shell + process injector in pure x86_64 NASM — ChaCha20-Poly1305 AEAD, Hell's Gate syscalls, zero deps | x86 ASM |
| [**Grotto**](https://github.com/Real-Fruit-Snacks/Grotto) | Encrypted netcat in pure assembly — ChaCha20-Poly1305, Linux ELF + Windows PE, ~8 KB, zero dependencies | x86 ASM |
| [**Dew**](https://github.com/Real-Fruit-Snacks/Dew) | HTTPS reverse shell — XChaCha20-Poly1305 over TLS, ~37 KB binary, zero dependencies | C |
| [**Droplet**](https://github.com/Real-Fruit-Snacks/Droplet) | HTTPS reverse shell for Windows — ~50 KB C implant, AES-256 encryption, interactive Python listener | C |
| [**Undercurrent**](https://github.com/Real-Fruit-Snacks/Undercurrent) | io_uring stealth loader in pure assembly — ChaCha20-Poly1305, ~4.2 KB, invisible to syscall monitoring | x86 ASM |

---

## Enumeration & Exploitation

| Tool | What It Does | Language |
|------|--------------|----------|
| [**Abyss**](https://github.com/Real-Fruit-Snacks/Abyss) | Offensive forensic analysis — credentials, keys, persistence from disk/memory images. SAM, NTDS.dit, LSA, DPAPI, browser passwords, SSH keys, LSASS minidumps. Raw/E01/VMDK with NTFS/ext4. | Rust |
| [**Flood**](https://github.com/Real-Fruit-Snacks/Flood) | Async web fuzzer — directory enum, VHost discovery, parameter fuzzing. Recursive scanning, clusterbomb mode, auto-throttle on 429s, JSON/CSV/Hashcat output. | Rust |
| [**Riptide**](https://github.com/Real-Fruit-Snacks/Riptide) | Collaborative browser terminal — real-time sync, credential vault, variable substitution, session recording, playbook workspace | JavaScript |
| [**Runoff**](https://github.com/Real-Fruit-Snacks/Runoff) | AD security audit — extract quick wins, attack paths, and misconfigurations from BloodHound CE | Python |
| [**Maelstrom**](https://github.com/Real-Fruit-Snacks/Maelstrom) | NetExec wrapper — 35+ AD enumeration modules in one command, multi-target scanning, actionable recommendations | Python |
| [**Rapids**](https://github.com/Real-Fruit-Snacks/Rapids) | Credential spraying framework — 28 native protocol modules, adaptive skipping, pass-the-hash support | Python |
| [**Lure**](https://github.com/Real-Fruit-Snacks/Lure) | SMB hash bait — drops poisoned `.url`/`.scf`/`.xml` payloads on writable shares to coerce NTLM auth via Responder | Python |
| [**Seep**](https://github.com/Real-Fruit-Snacks/Seep) | Windows privesc enumeration — 16 checks, 97 tools, MITRE ATT&CK mapping, fileless agent, single-file HTML reports | Python |
| [**Whirlpool**](https://github.com/Real-Fruit-Snacks/Whirlpool) | Privesc reasoning engine — parses LinPEAS/WinPEAS output, generates ranked exploitation playbooks | Python |
| [**Deluge**](https://github.com/Real-Fruit-Snacks/Deluge) | Nmap & RustScan parser — color-coded terminal reports, multi-format export, interactive scanning, Catppuccin styling | Python |

---

## Reference & Environments

| Tool | What It Does | Language |
|------|--------------|----------|
| [**Shallows**](https://github.com/Real-Fruit-Snacks/Shallows) | Browser-native Linux terminals — x86 emulation in the browser. No servers, no installs, no accounts. | JavaScript |
| [**Ripple**](https://github.com/Real-Fruit-Snacks/Ripple) | Browser-based Vim editor — full keybindings via CodeMirror 6, split panes, tabs, virtual filesystem, zero dependencies | JavaScript |
| [**Surge**](https://github.com/Real-Fruit-Snacks/Surge) | Markdown-to-command-reference — fuzzy search, variable substitution, offline-first PWA, Catppuccin themes | Python |
| [**Fathom**](https://github.com/Real-Fruit-Snacks/Fathom) | Offline man pages browser — TLDR summaries, instant search, Catppuccin themes. PWA, works without internet. | JavaScript |
| [**Cascade**](https://github.com/Real-Fruit-Snacks/Cascade) | Native markdown editor — real-time collaboration, live preview, wiki-links, canvas whiteboard, 21+ themes. Tauri + Rust. | TypeScript |
| [**Sunken-Archive**](https://github.com/Real-Fruit-Snacks/Sunken-Archive) | Personal knowledge base — digital garden with interconnected notes, graph view, full-text search. Built on Quartz. | TypeScript |
| [**HydroShot**](https://github.com/Real-Fruit-Snacks/HydroShot) | Screenshot capture & annotation — region select, drawing tools, copy/save. Built with Rust, winit, tiny-skia. | Rust |
| [**Tidepool**](https://github.com/Real-Fruit-Snacks/Tidepool) | Interactive terminal portfolio — explore a developer profile through real shell commands in the browser via xterm.js | JavaScript |
| [**Deadwater**](https://github.com/Real-Fruit-Snacks/Deadwater) | Research publication platform — index, search, and serve computational papers. Full-text search, citation graph, API. | TypeScript |
| [**MyNotes**](https://github.com/Real-Fruit-Snacks/MyNotes) | Tradecraft notebook — personal pentester field reference. MkDocs Material with Catppuccin theming, deployed via GitHub Pages. | Markdown |
| [**x86-assembly-lab**](https://github.com/Real-Fruit-Snacks/x86-assembly-lab) | Interactive x86 assembly lab — simulator, stack visualizer, register quiz, tutorials from fundamentals to reverse engineering | HTML |

---

## AI & Enterprise

| Tool | What It Does | Language |
|------|--------------|----------|
| [**armsforge**](https://github.com/Real-Fruit-Snacks/armsforge) | AI-powered security platform — intelligent automation, Claude Code integration, workflow orchestration for offensive operations | TypeScript |

---

## Multi-Call Binaries

A sail-themed sextet — same idea (BusyBox-style single-binary shell toolkits), six different languages, six different size/portability tradeoffs.

| Tool | What It Does | Language |
|------|--------------|----------|
| [**Rill**](https://github.com/Real-Fruit-Snacks/Rill) | Pure x86_64 NASM — 41 Unix utilities, **~34 KB** static ELF, direct syscalls, no libc | x86 ASM |
| [**Staysail**](https://github.com/Real-Fruit-Snacks/Staysail) | Zig — 84 Unix utilities, **~1 MB** statically-linked, native cross-compile to Linux/macOS/Windows | Zig |
| [**Moonraker**](https://github.com/Real-Fruit-Snacks/Moonraker) | Lua — 81 Unix utilities, **~1.2 MB** static executable via luastatic with embedded Lua VM | Lua |
| [**Jib**](https://github.com/Real-Fruit-Snacks/Jib) | Rust — 73 utilities + `jq`/`http`/`dig`, **~2.4 MB avg** (1.4 MB slim → 3.7 MB full) across 11 platform builds | Rust |
| [**Topsail**](https://github.com/Real-Fruit-Snacks/Topsail) | Go — single-file binary, **~3.4 MB** per platform (Linux/macOS/Windows × amd64/arm64), .deb/.rpm/.apk packages | Go |
| [**Mainsail**](https://github.com/Real-Fruit-Snacks/Mainsail) | Python — 73 utilities, **~5.5 MB** native bundles (or **~110 KB** .pyz with system Python), Linux/Windows/macOS | Python |

---

## Utilities

| Tool | What It Does | Language |
|------|--------------|----------|
| [**Tidemark**](https://github.com/Real-Fruit-Snacks/Tidemark) | Obsidian plugin — variable substitution in markdown via YAML frontmatter. Copy, replace, rename in one command. | TypeScript |

---

## Games

| Tool | What It Does | Language |
|------|--------------|----------|
| [**Blueprint**](https://github.com/Real-Fruit-Snacks/Blueprint) | Browser-based incremental factory game — build, automate, prestige, publish. Zero-dependency vanilla HTML/CSS/JS. | JavaScript |
| [**Crownfall**](https://github.com/Real-Fruit-Snacks/Crownfall) | Pixel-art medieval wave-defense incremental built as a single HTML file. Hold the wall, bank Crowns, return stronger. | HTML |
| [**Tower-Defense**](https://github.com/Real-Fruit-Snacks/Tower-Defense) | Cyberpunk neon tower defense — 6 elements, 14 towers, procedural campaign, endless mode, roguelite unlocks. Phaser 3 + TypeScript + Vite. | TypeScript |

---

## Stack Architecture

| Layer        | Implementation                                                       |
|--------------|----------------------------------------------------------------------|
| **Systems**     | Rust (memory-safe, ergonomic) · Go (single static binary) · C (footprint-critical) |
| **Assembly**    | x86_64 NASM (zero-libc, direct syscall, ELF + PE)                  |
| **Scripting**   | Python 3.10+ (AD tooling, parsers, frameworks) · Bash (orchestration) |
| **Web**         | TypeScript + Vite · Vanilla JavaScript · Tauri (native shell)      |
| **Niche**       | Lua (luastatic) · Zig (cross-compile native)                       |
| **Branding**    | Catppuccin Mocha (dark) + Latte (light) · brutalist 800×200 SVG banners · Inter + JetBrains Mono |
| **Docs**        | Each repo ships a GitHub Pages site under `docs/` matching the brutalist template |
| **CI**          | GitHub Actions across the org — build matrix, test, release artifacts, Pages deploy |

---

## Authorization & Contributing

Every tool in this org is designed for **authorized security testing** with explicit written permission. Targeting systems you do not own or have not been contracted to test is illegal in most jurisdictions and never the intent of this work.

Security vulnerabilities should be reported via the affected project's private security advisories — never public issues. Each repo links its own advisories page.

The `Real-Fruit-Snacks` org **does not**: distribute pre-compiled malicious binaries, host live command infrastructure, package payloads for distribution, or provide operational support for unauthorized engagements.

Contributions from the community are highly encouraged. Please refer to the `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md` files for full guidelines on how to submit pull requests and report issues.

---

## License

Distributed under the MIT License (most), GPLv3 (SSH-derived), CC-BY (notes). See individual repository `LICENSE` files for more information.

---

## Contact

Real-Fruit-Snacks - [https://github.com/Real-Fruit-Snacks](https://github.com/Real-Fruit-Snacks)
