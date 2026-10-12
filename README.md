<div align="center">

  # Real-Fruit-Snacks

  **Water-themed offensive security tooling — plus the editors, themes, utilities and games built along the way.**

  [![License: MIT](https://img.shields.io/badge/License-MIT-cba6f7.svg)](https://opensource.org/licenses/MIT)

  [Documentation](https://real-fruit-snacks.github.io/) • [Report Issue](https://github.com/Real-Fruit-Snacks/Real-Fruit-Snacks/issues)

</div>

---

## Overview

Real-Fruit-Snacks is a collection of **100+ independent repositories**. At its core is a personal offensive-security toolkit, field-built for authorized red team engagements, pentests, and security research: payload delivery, C2, post-exploitation, tunneling, AD enumeration, credential abuse, and privilege escalation.

Around that core sits everything an operator ends up building for their own desk — offline reference sites, single-page command builders, Obsidian plugins, a cross-application theme family, and a shelf of browser games. Every project ships standalone: no shared runtime, no monorepo lock-in. Pick what you need.

*A pantry of real, authentic tooling — no hollow snacks, no corporate filler. Each release is its own discrete drop in the bucket; together they form the watershed.*

### Key Features

- **Offensive core**: 40+ security tools across C2, tunneling, implants, Active Directory, and enumeration.
- **Polyglot**: Rust, Go, Python, C, C#, x86-64 NASM, Zig, Lua, TypeScript, JavaScript, Shell, and HTML.
- **Offline-first**: reference sites and browser tools run entirely client-side — no servers, no accounts, no network calls.
- **Unified aesthetic**: Catppuccin Mocha + Latte across the security tools; the Terminal Workbench theme family across editors, browsers, and terminals.
- **Multi-call binaries**: a sail-themed sextet of BusyBox-style toolkits implementing the same idea in six languages.

---

# Security

## C2 & Post-Exploitation

| Tool | What It Does | Language |
|------|--------------|----------|
| [**Kraken**](https://github.com/Real-Fruit-Snacks/Kraken) | OPSEC-first C2 — minimal core, runtime-loadable modules, X25519 ECDH + AES-256-GCM, multi-transport | Rust |
| [**Aquifer**](https://github.com/Real-Fruit-Snacks/Aquifer) | Linux post-exploitation — kernel namespace isolation, multi-channel C2, polymorphic beacons, 36 stealth modules | Go |
| [**Siphon**](https://github.com/Real-Fruit-Snacks/Siphon) | Lightweight C2 — ECDH P-256 forward secrecy, zero-disk configuration | Go |
| [**Wellspring**](https://github.com/Real-Fruit-Snacks/Wellspring) | Payload delivery server — 12 delivery methods, token-gated access, AES-256-GCM at rest, memory zeroing. Single binary. | Go |
| [**Spillway**](https://github.com/Real-Fruit-Snacks/Spillway) | Reverse/bind/dormant FUSE mount — browse remote filesystems locally over TLS 1.3 with mutual PSK auth | Go |

## Network & Tunneling

| Tool | What It Does | Language |
|------|--------------|----------|
| [**Flux**](https://github.com/Real-Fruit-Snacks/Flux) | Swiss Army Netcat — replaces nc/ncat/socat/pwncat. TLS + Noise channels, auto-PTY shells, SHA256-verified transfers, SOCKS5 pivoting, scanning. | Rust |
| [**Neap**](https://github.com/Real-Fruit-Snacks/Neap) | Static SSH server — reverse/bind shells with full PTY, SFTP, local/remote/dynamic forwarding, TLS with SNI spoofing | Rust |
| [**Undertow**](https://github.com/Real-Fruit-Snacks/Undertow) | Static SSH server — reverse/bind shells, SFTP, port forwarding, TLS wrapping with SNI spoofing. Under 1.5 MB. | Go |
| [**Slipstream**](https://github.com/Real-Fruit-Snacks/Slipstream) | Drop-in SSH wrapper — tunnel management, file transfers, passive filesystem mapping, per-command logging, fingerprint identity | Rust |
| [**Conduit**](https://github.com/Real-Fruit-Snacks/Conduit) | SOCAT relay with kernel-level process masquerading — prctl/setproctitle stealth, argument hiding, 50+ channel types | C |
| [**Culvert**](https://github.com/Real-Fruit-Snacks/Culvert) | One-command ligolo-ng tunnel setup — TUN, routing, and proxy abstraction | Shell |
| [**Depth**](https://github.com/Real-Fruit-Snacks/Depth) | Full SSH-2.0 in pure assembly — ChaCha20-Poly1305, Ed25519, X25519, SFTP, PTY, forwarding. 94 KB static ELF, no libc. | x86 ASM |
| [**xfer**](https://github.com/Real-Fruit-Snacks/xfer) | Prints ready-to-paste file-transfer commands (scp/sftp/tar over SSH, openssl, netcat) in both directions. Stdlib-only. | Python |

## Shells & Implants

| Tool | What It Does | Language |
|------|--------------|----------|
| [**Vapor**](https://github.com/Real-Fruit-Snacks/Vapor) | Encrypted reverse shell + process injector in pure x86_64 NASM — ChaCha20-Poly1305, Hell's Gate syscalls, zero deps | x86 ASM |
| [**Grotto**](https://github.com/Real-Fruit-Snacks/Grotto) | Encrypted netcat in pure assembly — ChaCha20-Poly1305, cross-platform, ~8 KB, zero dependencies | x86 ASM |
| [**Dew**](https://github.com/Real-Fruit-Snacks/Dew) | HTTPS reverse shell — XChaCha20-Poly1305 over TLS, ~37 KB binary, zero dependencies | C |
| [**Droplet**](https://github.com/Real-Fruit-Snacks/Droplet) | HTTPS reverse shell for Windows — ~50 KB C implant, AES-256, interactive Python listener | C |
| [**Undercurrent**](https://github.com/Real-Fruit-Snacks/Undercurrent) | io_uring stealth loader in pure assembly — ChaCha20-Poly1305, ~4.2 KB, invisible to syscall monitoring | x86 ASM |

## Active Directory & Credentials

| Tool | What It Does | Language |
|------|--------------|----------|
| [**forge-framework**](https://github.com/Real-Fruit-Snacks/forge-framework) | Metasploit-style console with 60+ modules for AD, AD CS, Kerberos, SMB and web — plus self-contained Docker labs every module is tested against | Python |
| [**anvil**](https://github.com/Real-Fruit-Snacks/anvil) | Active Directory recon and attack CLI built on gopacket | Go |
| [**Runoff**](https://github.com/Real-Fruit-Snacks/Runoff) | AD security audit — quick wins, attack paths, and misconfigurations from BloodHound CE | Python |
| [**Maelstrom**](https://github.com/Real-Fruit-Snacks/Maelstrom) | NetExec wrapper — 35+ AD enumeration modules in one command | Python |
| [**Rapids**](https://github.com/Real-Fruit-Snacks/Rapids) | Modular credential spraying framework | Python |
| [**Lure**](https://github.com/Real-Fruit-Snacks/Lure) | SMB hash bait — drops poisoned `.url`/`.scf`/`.xml` files on writable shares to coerce NTLM auth via Responder | Python |
| [**Abyss**](https://github.com/Real-Fruit-Snacks/Abyss) | Offensive forensics — credentials, keys, and persistence from disk and memory images. SAM, NTDS.dit, LSA, DPAPI, LSASS minidumps. Raw/E01/VMDK. | Rust |

## Enumeration & Privilege Escalation

| Tool | What It Does | Language |
|------|--------------|----------|
| [**Flood**](https://github.com/Real-Fruit-Snacks/Flood) | Async web fuzzer — directories, VHosts, parameters. Recursive, clusterbomb mode, auto-throttle on 429s, Burp replay. | Rust |
| [**Seep**](https://github.com/Real-Fruit-Snacks/Seep) | Windows privesc enumeration with a fileless agent | Python |
| [**Whirlpool**](https://github.com/Real-Fruit-Snacks/Whirlpool) | Privesc reasoning engine — parses LinPEAS/WinPEAS output into ranked exploitation playbooks | Python |
| [**Deluge**](https://github.com/Real-Fruit-Snacks/Deluge) | Nmap & RustScan parser — color-coded terminal reports, multi-format export, interactive scanning | Python |

## Operator Platforms

| Tool | What It Does | Language |
|------|--------------|----------|
| [**Riptide**](https://github.com/Real-Fruit-Snacks/Riptide) | Collaborative browser terminal and playbook workspace — real-time sync, credential vault, variable substitution, session recording | JavaScript |
| [**armsforge**](https://github.com/Real-Fruit-Snacks/armsforge) | AI-assisted offensive operations — automation, Claude Code integration, workflow orchestration | JavaScript |
| [**Surge**](https://github.com/Real-Fruit-Snacks/Surge) | Searchable command reference — fuzzy search, variable substitution, offline PWA | JavaScript |

## Multi-Call Binaries

A sail-themed sextet — the same idea (BusyBox-style single-binary toolkits) in six languages, six different size/portability tradeoffs.

| Tool | What It Does | Language |
|------|--------------|----------|
| [**Rill**](https://github.com/Real-Fruit-Snacks/Rill) | Pure x86_64 NASM — **~34 KB** static ELF, direct syscalls, no libc | x86 ASM |
| [**Staysail**](https://github.com/Real-Fruit-Snacks/Staysail) | 84 Unix utilities in one static executable, native cross-compile | Zig |
| [**Moonraker**](https://github.com/Real-Fruit-Snacks/Moonraker) | Static executable via luastatic with an embedded Lua VM | Lua |
| [**Jib**](https://github.com/Real-Fruit-Snacks/Jib) | 78 Unix utilities in one executable | Rust |
| [**Topsail**](https://github.com/Real-Fruit-Snacks/Topsail) | 84 Unix utilities, **~3 MB** static executable, native on Linux, macOS, and Windows | Go |
| [**Mainsail**](https://github.com/Real-Fruit-Snacks/Mainsail) | Cross-platform multi-call binary | Python |

---

# Reference & Tools

## Offline Reference

| Tool | What It Does | Language |
|------|--------------|----------|
| [**manpages**](https://github.com/Real-Fruit-Snacks/manpages) | Offline man page lookup — 58,464 pre-rendered Ubuntu pages, zero network calls | Python |
| [**tldr**](https://github.com/Real-Fruit-Snacks/tldr) | Offline tldr pages — fully static, instant search, open straight from disk | Python |
| [**windows-event-id-reference**](https://github.com/Real-Fruit-Snacks/windows-event-id-reference) | The Windows Event IDs that matter to defenders — logon, Kerberos, process, PowerShell, Sysmon — each with a ready `Get-WinEvent` query | JavaScript |
| [**port-reference**](https://github.com/Real-Fruit-Snacks/port-reference) | Searchable table of well-known ports | JavaScript |
| [**x86-x64-assembly-lab**](https://github.com/Real-Fruit-Snacks/x86-x64-assembly-lab) | x86 & x86-64 simulator and RE lab — step-through 32/64-bit engines, stack playground, 28 tutorials | HTML |
| [**Shallows**](https://github.com/Real-Fruit-Snacks/Shallows) | Browser-native Linux terminals via x86 emulation in WebAssembly | JavaScript |
| [**Ripple**](https://github.com/Real-Fruit-Snacks/Ripple) | Browser-based Vim editor powered by CodeMirror 6 | JavaScript |

## Browser Utilities

Single-page, offline, no build step.

| Tool | What It Does |
|------|--------------|
| [**nmap-command-builder**](https://github.com/Real-Fruit-Snacks/nmap-command-builder) | Assemble an nmap command live, every flag explained |
| [**tcpdump-filter-builder**](https://github.com/Real-Fruit-Snacks/tcpdump-filter-builder) | Build a tcpdump command and BPF filter from protocol, host, port, and direction |
| [**curl-request-builder**](https://github.com/Real-Fruit-Snacks/curl-request-builder) | Build a curl command with correct POSIX quoting |
| [**openvpn-inspector**](https://github.com/Real-Fruit-Snacks/openvpn-inspector) | Inspect an `.ovpn`/`.crt`/`.pem` — certificate expiry, details, and config security flags |
| [**ip-cidr-calculator**](https://github.com/Real-Fruit-Snacks/ip-cidr-calculator) | Network, broadcast, host range, wildcard mask, and binary breakdown |
| [**chmod-calculator**](https://github.com/Real-Fruit-Snacks/chmod-calculator) | Unix permissions as checkboxes, octal, and symbolic, kept in sync |
| [**cron-parser**](https://github.com/Real-Fruit-Snacks/cron-parser) | Validate and explain a cron expression, preview next run times |
| [**systemd-service-generator**](https://github.com/Real-Fruit-Snacks/systemd-service-generator) | Generate a complete systemd `.service` unit and install commands |
| [**windows-task-builder**](https://github.com/Real-Fruit-Snacks/windows-task-builder) | Generate `schtasks /create` commands, plus a Last Run Result code reference |
| [**text-codec**](https://github.com/Real-Fruit-Snacks/text-codec) | Base64, URL-safe Base64, percent-encoding, and hex — both directions |
| [**timestamp-converter**](https://github.com/Real-Fruit-Snacks/timestamp-converter) | Unix epoch ↔ human dates, UTC and local side by side |
| [**character-analyzer**](https://github.com/Real-Fruit-Snacks/character-analyzer) | Classify every character in a string, with Unicode code points |
| [**color-format-converter**](https://github.com/Real-Fruit-Snacks/color-format-converter) | Hex ↔ RGB ↔ HSL with WCAG 2.1 contrast checks |
| [**identity-gen**](https://github.com/Real-Fruit-Snacks/identity-gen) | Throwaway signup identities — names, handles, passwords, avatars |
| [**worldclock**](https://github.com/Real-Fruit-Snacks/worldclock) | Offline world clock with a live day/night map |

## Desktop & Dev Tools

| Tool | What It Does | Language |
|------|--------------|----------|
| [**Cascade**](https://github.com/Real-Fruit-Snacks/Cascade) | Native markdown editor — real-time collaboration, live preview, wiki-links, canvas whiteboard. Tauri + Rust. | TypeScript |
| [**HydroShot**](https://github.com/Real-Fruit-Snacks/HydroShot) | Screenshot capture & annotation — 14 annotation tools, OCR, pin-to-screen | Rust |
| [**windows-cert-api-tester**](https://github.com/Real-Fruit-Snacks/windows-cert-api-tester) | API tester that authenticates with a client certificate from the Windows store (mTLS). Single-file exe. | C# |
| [**team-calendar**](https://github.com/Real-Fruit-Snacks/team-calendar) | Static, git-backed team calendar edited in the browser — no backend | JavaScript |
| [**Tidepool**](https://github.com/Real-Fruit-Snacks/Tidepool) | Interactive terminal portfolio built with xterm.js | JavaScript |
| [**youtube-automation-toolkit**](https://github.com/Real-Fruit-Snacks/youtube-automation-toolkit) | Chrome extension to bulk-clear Watch Later and mass-unsubscribe | JavaScript |

---

# Obsidian

## Plugins

| Plugin | What It Does |
|--------|--------------|
| [**obsidian-better-store**](https://github.com/Real-Fruit-Snacks/obsidian-better-store) | Replacement community plugin browser — filters, categories, README previews, trending |
| [**obsidian-github-updater**](https://github.com/Real-Fruit-Snacks/obsidian-github-updater) | Install and update unofficial plugins straight from GitHub |
| [**obsidian-filen-cloud-sync**](https://github.com/Real-Fruit-Snacks/obsidian-filen-cloud-sync) | Two-way, end-to-end encrypted sync with Filen — desktop and mobile |
| [**obsidian-vault-publisher**](https://github.com/Real-Fruit-Snacks/obsidian-vault-publisher) | Publish a vault as a fast static website |
| [**obsidian-nested-vaults**](https://github.com/Real-Fruit-Snacks/obsidian-nested-vaults) | Scope the whole vault — explorer, search, graph, backlinks — to one folder |
| [**Graphite**](https://github.com/Real-Fruit-Snacks/Graphite) | Calm, Todoist-like task manager; tasks stay as Markdown files |
| [**obsidian-Thoughtbin**](https://github.com/Real-Fruit-Snacks/obsidian-Thoughtbin) | Memos-style private timeline for quick thoughts |
| [**obsidian-linkhaven**](https://github.com/Real-Fruit-Snacks/obsidian-linkhaven) | Linkwarden-style bookmark navigator over plain Markdown notes |
| [**Cove**](https://github.com/Real-Fruit-Snacks/Cove) | Bookmark manager with switchable layouts — one Markdown file per bookmark |
| [**wayback-linker**](https://github.com/Real-Fruit-Snacks/wayback-linker) | Archive note links with the Wayback Machine |
| [**Tidemark**](https://github.com/Real-Fruit-Snacks/Tidemark) | Variable substitution in Markdown via YAML frontmatter |
| [**obsidian-gym-tracker**](https://github.com/Real-Fruit-Snacks/obsidian-gym-tracker) | Track strength workouts and rucks, mobile and desktop |
| [**obsidian-speedlog**](https://github.com/Real-Fruit-Snacks/obsidian-speedlog) | Run an internet speed test and log each result as a note |
| [**amazon-order-sync**](https://github.com/Real-Fruit-Snacks/amazon-order-sync) | Sync Amazon orders into the vault with analytics and image caches |
| [**obsidian-plugin-lab**](https://github.com/Real-Fruit-Snacks/obsidian-plugin-lab) | Plugin pre-flight review against the official linter and community rules |
| [**obsidian-theme-lab**](https://github.com/Real-Fruit-Snacks/obsidian-theme-lab) | Build themes in-app — CSS rule inspector, screenshot contact sheets, contrast report |
| [**obsidian-plugins**](https://github.com/Real-Fruit-Snacks/obsidian-plugins) | Ready-to-install snapshot bundle of the plugins I use |

## Themes

| Theme | Look |
|-------|------|
| [**obsidian-glow**](https://github.com/Real-Fruit-Snacks/obsidian-glow) | Calm dark charcoal with a periwinkle accent |
| [**obsidian-outrun**](https://github.com/Real-Fruit-Snacks/obsidian-outrun) | Synthwave — neon pink and cyan, striped sun, horizon grid |
| [**obsidian-dossier**](https://github.com/Real-Fruit-Snacks/obsidian-dossier) | Case files — manila folders, typewriter type, hover-to-reveal redactions |
| [**obsidian-comic**](https://github.com/Real-Fruit-Snacks/obsidian-comic) | Halftone paper, hard black panels, speech-bubble callouts |
| [**obsidian-grimoire**](https://github.com/Real-Fruit-Snacks/obsidian-grimoire) | Tarot cards — gold on black, Cinzel titles, callouts that flip face down |

---

# Terminal Workbench

A theme family with one spec: graphite surfaces, restrained ANSI-style accents, color only on signal. Dark and light everywhere.

| Port | Target |
|------|--------|
| [**terminal-workbench-suite**](https://github.com/Real-Fruit-Snacks/terminal-workbench-suite) | Everything in one repo — spec, tokens, demo, all ports, and the Terminal Workbench Mono typeface |
| [**terminal-workbench-design-system**](https://github.com/Real-Fruit-Snacks/terminal-workbench-design-system) | Portable theme spec, drop-in CSS tokens, live demo |
| [**terminal-workbench**](https://github.com/Real-Fruit-Snacks/terminal-workbench) | Obsidian |
| [**terminal-workbench-vscode**](https://github.com/Real-Fruit-Snacks/terminal-workbench-vscode) | VS Code |
| [**terminal-workbench-vim**](https://github.com/Real-Fruit-Snacks/terminal-workbench-vim) | Vim — true color with 256-color fallback |
| [**terminal-workbench-windows-terminal**](https://github.com/Real-Fruit-Snacks/terminal-workbench-windows-terminal) | Windows Terminal |
| [**terminal-workbench-notepad-plus-plus**](https://github.com/Real-Fruit-Snacks/terminal-workbench-notepad-plus-plus) | Notepad++ — all 92 lexers |
| [**terminal-workbench-brave**](https://github.com/Real-Fruit-Snacks/terminal-workbench-brave) | Brave browser |
| [**terminal-workbench-cursor**](https://github.com/Real-Fruit-Snacks/terminal-workbench-cursor) | Obsidian cursor engine — box/line/underline carets, torch spotlight, Ghost Trail |
| [**terminal-workbench-pet**](https://github.com/Real-Fruit-Snacks/terminal-workbench-pet) | A floating ghost companion for your Obsidian vault |

---

# Games

| Game | What It Is | Language |
|------|------------|----------|
| [**chess-trainer**](https://github.com/Real-Fruit-Snacks/chess-trainer) | Lessons, puzzles, drills, repertoires, and game review — Stockfish and Maia run in the browser, free and offline | TypeScript |
| [**novafall**](https://github.com/Real-Fruit-Snacks/novafall) | Arcade roguelite — you're a dying star racing to go supernova | TypeScript |
| [**snowball-effect**](https://github.com/Real-Fruit-Snacks/snowball-effect) | Survivors-like where you are the weapon: a snowball that grows by absorbing everything smaller | JavaScript |
| [**benthic**](https://github.com/Real-Fruit-Snacks/benthic) | Incremental where the progress bar is depth, with procedural WebAudio | JavaScript |
| [**Blueprint**](https://github.com/Real-Fruit-Snacks/Blueprint) | Engineering-sheet factory incremental — build, prestige, publish, exhibit | JavaScript |
| [**Crownfall**](https://github.com/Real-Fruit-Snacks/Crownfall) | Pixel-art medieval wave-defense incremental | HTML |
| [**closed-circuit**](https://github.com/Real-Fruit-Snacks/closed-circuit) | Horror — a night-shift security guard and the cameras | JavaScript |
| [**sunny.exe**](https://github.com/Real-Fruit-Snacks/sunny.exe) | Horror — DayBreak OS and an AI assistant who knows too much | JavaScript |

---

## Stack

| Layer | Implementation |
|-------|----------------|
| **Systems** | Rust · Go · C · C# · Zig |
| **Assembly** | x86_64 NASM — zero-libc, direct syscalls, ELF + PE |
| **Scripting** | Python 3.10+ (AD tooling, parsers, frameworks) · Bash · Lua |
| **Web** | TypeScript + Vite · vanilla JavaScript · Tauri · WebAssembly |
| **Branding** | Catppuccin Mocha + Latte (security tools) · Terminal Workbench (themes, utilities, desktop tools) |
| **CI** | GitHub Actions — build matrix, tests, release artifacts, Pages deploys |

---

## Authorization & Contributing

Every security tool here is designed for **authorized security testing** with explicit written permission. Targeting systems you do not own or have not been contracted to test is illegal in most jurisdictions and never the intent of this work.

Security vulnerabilities should be reported via the affected project's private security advisories — never public issues.

Real-Fruit-Snacks **does not**: distribute pre-compiled malicious binaries, host live command infrastructure, package payloads for distribution, or provide operational support for unauthorized engagements.

Contributions are welcome. See [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).

---

## License

MIT for most projects, GPLv3 for SSH-derived ones. See each repository's `LICENSE` file.
