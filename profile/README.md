<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Real-Fruit-Snacks/Real-Fruit-Snacks/main/docs/assets/logo-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Real-Fruit-Snacks/Real-Fruit-Snacks/main/docs/assets/logo-light.svg">
  <img alt="Real-Fruit-Snacks" src="https://raw.githubusercontent.com/Real-Fruit-Snacks/Real-Fruit-Snacks/main/docs/assets/logo-dark.svg" width="520">
</picture>

<br>

Building offensive security tools — one wave at a time.

**46 tools** across 9 categories. Rust, Go, C, Assembly, Python, TypeScript.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?style=flat&logo=go&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-DEA584?style=flat&logo=rust&logoColor=black)
![C](https://img.shields.io/badge/C-A8B9CC?style=flat&logo=c&logoColor=black)
![Assembly](https://img.shields.io/badge/Assembly-6E4C13?style=flat)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat&logo=typescript&logoColor=white)
![Shell](https://img.shields.io/badge/Shell-4EAA25?style=flat&logo=gnubash&logoColor=white)

</div>

---

## ![C2](https://img.shields.io/badge/C2%20%26%20Post--Exploitation-f38ba8?style=flat-square) C2 & Post-Exploitation

Implant frameworks, payload delivery, and post-exploitation infrastructure.

| Tool | Description |
|:-----|:-----------|
| **[Aquifer](https://github.com/Real-Fruit-Snacks/Aquifer)** | Linux post-exploitation with kernel namespace isolation and 36 stealth modules. *Go* |
| **[Kraken](https://github.com/Real-Fruit-Snacks/Kraken)** | OPSEC-first C2 framework with modular implants, mesh networking, and multi-transport. *Rust* |
| **[Siphon](https://github.com/Real-Fruit-Snacks/Siphon)** | Lightweight C2 with ECDH P-256 forward secrecy and uTLS fingerprinting. *Go* |
| **[Spillway](https://github.com/Real-Fruit-Snacks/Spillway)** | Reverse/bind FUSE filesystem mount over TLS 1.3. *Go* |
| **[Undertow](https://github.com/Real-Fruit-Snacks/Undertow)** | Static SSH server with reverse/bind shells, SFTP, and TLS wrapping. *Go* |
| **[Wellspring](https://github.com/Real-Fruit-Snacks/Wellspring)** | Payload delivery server with 12 methods and AES-256-GCM at rest. *Go* |

---

## ![Shells](https://img.shields.io/badge/Shells%20%26%20Implants-eba0ac?style=flat-square) Shells & Implants

Encrypted reverse shells and stealth loaders. Assembly-level precision.

| Tool | Description |
|:-----|:-----------|
| **[Dew](https://github.com/Real-Fruit-Snacks/Dew)** | Encrypted HTTPS reverse shell over XChaCha20-Poly1305 and TLS. ~37 KB. *C* |
| **[Droplet](https://github.com/Real-Fruit-Snacks/Droplet)** | Encrypted HTTPS reverse shell for Windows with interactive Python listener. ~50 KB. *C* |
| **[Grotto](https://github.com/Real-Fruit-Snacks/Grotto)** | Encrypted netcat in pure x86_64 NASM assembly. ~8 KB. *Assembly* |
| **[Undercurrent](https://github.com/Real-Fruit-Snacks/Undercurrent)** | io_uring stealth loader with ChaCha20-Poly1305. ~4.2 KB. *Assembly* |
| **[Vapor](https://github.com/Real-Fruit-Snacks/Vapor)** | Encrypted reverse shell and process injector in pure x86_64 NASM. *Assembly* |

---

## ![Networking](https://img.shields.io/badge/Networking-74c7ec?style=flat-square) Networking

Encrypted tunnels, relays, and protocol implementations.

| Tool | Description |
|:-----|:-----------|
| **[Conduit](https://github.com/Real-Fruit-Snacks/Conduit)** | SOCAT relay with kernel-level process masquerading and 50+ channel types. *C* |
| **[Depth](https://github.com/Real-Fruit-Snacks/Depth)** | Complete SSH-2.0 in pure x86_64 NASM assembly. 94 KB static ELF. *Assembly* |
| **[Flux](https://github.com/Real-Fruit-Snacks/Flux)** | Swiss Army Netcat replacing nc, ncat, socat, and pwncat. Single static binary. *Rust* |
| **[Neap](https://github.com/Real-Fruit-Snacks/Neap)** | Static SSH server with reverse/bind shells, SFTP, TLS wrapping, and SNI spoofing. *Rust* |
| **[Slipstream](https://github.com/Real-Fruit-Snacks/Slipstream)** | SSH wrapper with tunnel management, file transfers, and session logging. *Rust* |

---

## ![Operations](https://img.shields.io/badge/Enumeration%20%26%20Exploitation-94e2d5?style=flat-square) Enumeration & Exploitation

Active Directory, credential attacks, privilege escalation, and offensive analysis.

| Tool | Description |
|:-----|:-----------|
| **[Abyss](https://github.com/Real-Fruit-Snacks/Abyss)** | Offline forensic analysis — extract credentials from disk images and memory dumps. *Rust* |
| **[Deluge](https://github.com/Real-Fruit-Snacks/Deluge)** | Nmap and RustScan output parser with color-coded reports. *Python* |
| **[Flood](https://github.com/Real-Fruit-Snacks/Flood)** | Async web fuzzer with recursive discovery, auto-throttle, and FUZZ keyword placement. *Rust* |
| **[Lure](https://github.com/Real-Fruit-Snacks/Lure)** | SMB hash bait — drops poisoned `.url`/`.scf`/`.xml` payloads to coerce NTLM auth via Responder. *Python* |
| **[Maelstrom](https://github.com/Real-Fruit-Snacks/Maelstrom)** | NetExec wrapper combining 35+ AD enumeration modules into one command. *Python* |
| **[Rapids](https://github.com/Real-Fruit-Snacks/Rapids)** | Credential spraying across 28 protocol modules with pass-the-hash. *Python* |
| **[Riptide](https://github.com/Real-Fruit-Snacks/Riptide)** | Collaborative browser terminal with real-time sync and credential vault. *TypeScript* |
| **[Runoff](https://github.com/Real-Fruit-Snacks/Runoff)** | AD security audit extracting attack paths from BloodHound CE. *Python* |
| **[Seep](https://github.com/Real-Fruit-Snacks/Seep)** | Windows privilege escalation enumeration with MITRE ATT&CK mapping. *Python* |
| **[Whirlpool](https://github.com/Real-Fruit-Snacks/Whirlpool)** | Privilege escalation reasoning engine parsing LinPEAS/WinPEAS output. *Python* |

---

## ![Productivity](https://img.shields.io/badge/Productivity%20%26%20Editors-cba6f7?style=flat-square) Productivity & Editors

Markdown editors, command references, and workflow tools.

| Tool | Description |
|:-----|:-----------|
| **[Cascade](https://github.com/Real-Fruit-Snacks/Cascade)** | Native markdown editor with real-time collaboration and 21+ themes. *Rust/TypeScript* |
| **[HydroShot](https://github.com/Real-Fruit-Snacks/HydroShot)** | Screenshot capture and annotation tool. *Rust* |
| **[Ripple](https://github.com/Real-Fruit-Snacks/Ripple)** | Browser-based Vim editor with CodeMirror 6 and split panes. *JavaScript* |
| **[Surge](https://github.com/Real-Fruit-Snacks/Surge)** | Markdown-to-command-reference with fuzzy search and variable substitution. *JavaScript* |
| **[Tidemark](https://github.com/Real-Fruit-Snacks/Tidemark)** | Obsidian plugin for variable substitution via YAML frontmatter. *TypeScript* |

---

## ![Reference](https://img.shields.io/badge/Reference%20%26%20Environments-89dceb?style=flat-square) Reference & Environments

Knowledge bases, documentation browsers, and interactive environments.

| Tool | Description |
|:-----|:-----------|
| **[Deadwater](https://github.com/Real-Fruit-Snacks/Deadwater)** | Research publication platform with full-text search and citation graph. *Go/TypeScript* |
| **[Fathom](https://github.com/Real-Fruit-Snacks/Fathom)** | Offline man pages browser with TLDR summaries. PWA. *JavaScript* |
| **[Shallows](https://github.com/Real-Fruit-Snacks/Shallows)** | Browser-native Linux terminals powered by x86 emulation. *JavaScript* |
| **[Sunken-Archive](https://github.com/Real-Fruit-Snacks/Sunken-Archive)** | Knowledge base and digital garden built on Quartz. *TypeScript* |
| **[Tidepool](https://github.com/Real-Fruit-Snacks/Tidepool)** | Interactive terminal portfolio via xterm.js. *JavaScript* |
| **[x86-assembly-lab](https://github.com/Real-Fruit-Snacks/x86-assembly-lab)** | Interactive x86 assembly lab — simulator, stack visualizer, register quiz, tutorials. *HTML* |

---

## ![Utilities](https://img.shields.io/badge/Utilities-fab387?style=flat-square) Utilities

Platform tools and automation.

| Tool | Description |
|:-----|:-----------|
| **[armsforge](https://github.com/Real-Fruit-Snacks/armsforge)** | AI-powered security platform with Claude Code integration. *TypeScript* |
| **[Culvert](https://github.com/Real-Fruit-Snacks/Culvert)** | Pivot under the obstruction — one-command ligolo-ng tunnel setup with TUN, routing, and WebUI. *Shell* |

---

## ![Toolboxes](https://img.shields.io/badge/Multi--Call%20Binaries-89b4fa?style=flat-square) Multi-Call Binaries

A sail-themed quartet of BusyBox-style toolkits. Same idea, four languages, four tradeoffs.

| Tool | Description |
|:-----|:-----------|
| **[jib](https://github.com/Real-Fruit-Snacks/jib)** | BusyBox-style multi-call binary in Rust — 73 Unix utilities + `jq`/`http`/`dig` in ~2 MB. *Rust* |
| **[mainsail](https://github.com/Real-Fruit-Snacks/mainsail)** | BusyBox-style multi-call binary in Python — 73 Unix utilities, ~5–7 MB, native on Linux/Windows/macOS. *Python* |
| **[rill](https://github.com/Real-Fruit-Snacks/rill)** | BusyBox-style multi-call binary in pure x86_64 NASM — 41 utilities, ~108 KB static ELF, direct syscalls, no libc. *Assembly* |
| **[topsail](https://github.com/Real-Fruit-Snacks/topsail)** | Single-file BusyBox-like multi-call binary in Go — easy cross-compile, static binary. *Go* |

---

## ![Games](https://img.shields.io/badge/Games-f9e2af?style=flat-square) Games

Browser-based games — vanilla HTML, single-file builds, zero installs.

| Tool | Description |
|:-----|:-----------|
| **[Blueprint](https://github.com/Real-Fruit-Snacks/Blueprint)** | Browser-based incremental factory game — build, automate, prestige, publish. Zero-dependency. *JavaScript* |
| **[Crownfall](https://github.com/Real-Fruit-Snacks/Crownfall)** | Pixel-art medieval wave-defense incremental built as a single HTML file. *HTML* |
| **[Tower-Defense](https://github.com/Real-Fruit-Snacks/Tower-Defense)** | Cyberpunk neon tower defense — 6 elements, 14 towers, procedural campaign, roguelite unlocks. *TypeScript* |

---

<div align="center">

All security tools are for authorized testing and educational purposes only.

</div>
