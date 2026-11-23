<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/board-dark.svg">
  <img alt="Small tools, one job each. A board lists fifteen tools, and for each in turn an orange seam sweeps its job, turning what goes in into what comes out: Ctrl+PrintScreen into screen-mark_2026-11-05_091412.png, Proton's Port pair 51037->51037 into listening port updated: 48213 -> 51037, HEVC 10-bit 1080p into H.264 8-bit 720p, and on through the list" src="assets/board-light.svg" width="100%">
</picture>

I write small tools for jobs I kept doing by hand. Each one does one job, and the board above runs through them: what you hand it, and what you get back. The same list, with a page for each tool, is at **[real-fruit-snacks.github.io](https://real-fruit-snacks.github.io/)**.

| Tool | Its job |
|---|---|
| [**screen-mark**](https://github.com/Real-Fruit-Snacks/screen-mark)<br><sub>Rust · Windows, Linux</sub> | Screenshot capture and annotation in pure Rust |
| [**port-sync**](https://github.com/Real-Fruit-Snacks/port-sync)<br><sub>Rust · Windows</sub> | Keeps qBittorrent's port synced to Proton VPN |
| [**carify**](https://github.com/Real-Fruit-Snacks/carify)<br><sub>sh, PowerShell · Windows, macOS, Linux</sub> | Convert video for Uconnect USB playback, via ffmpeg |
| [**certapi**](https://github.com/Real-Fruit-Snacks/certapi)<br><sub>C# · Windows</sub> | mTLS API client for the Windows certificate store |
| [**identity-gen**](https://github.com/Real-Fruit-Snacks/identity-gen)<br><sub>HTML · browser</sub> | Offline generator for throwaway signup identities |
| [**amazon-order-sync**](https://github.com/Real-Fruit-Snacks/amazon-order-sync)<br><sub>Rust · Windows, Linux</sub> | Syncs your Amazon orders into local Markdown notes |
| [**powershell-toolbox**](https://github.com/Real-Fruit-Snacks/powershell-toolbox)<br><sub>PowerShell · Windows</sub> | A grab-bag of my PowerShell scripts, each one standalone |
| [**forge-framework**](https://github.com/Real-Fruit-Snacks/forge-framework)<br><sub>Python</sub> | Modular offensive-security framework with a console |
| [**pwn-broker**](https://github.com/Real-Fruit-Snacks/pwn-broker)<br><sub>Python · Kali Linux</sub> | Keeps a box's targets, notes, creds and tools in order |
| [**pwn-shop**](https://github.com/Real-Fruit-Snacks/pwn-shop)<br><sub>Python · Kali Linux</sub> | Tool packages for pwn-broker, built from upstream releases |
| [**pwn-playbooks**](https://github.com/Real-Fruit-Snacks/pwn-playbooks)<br><sub>Markdown · Kali Linux</sub> | Playbooks for pwn-broker: read into the note, fill in, run |
| [**open-file**](https://github.com/Real-Fruit-Snacks/open-file)<br><sub>TypeScript · browser</sub> | Learn and play chess in your browser, offline |
| [**proxflow**](https://github.com/Real-Fruit-Snacks/proxflow)<br><sub>TypeScript · Windows</sub> | Proxmox map and lab builder that works offline |
| [**agent-toolkit**](https://github.com/Real-Fruit-Snacks/agent-toolkit)<br><sub>PowerShell · Windows, Linux</sub> | T3 Code and Claude Code on Windows, without admin rights |
| [**dev-toolkit**](https://github.com/Real-Fruit-Snacks/dev-toolkit)<br><sub>C# · Windows</sub> | Developer tools for an offline Windows machine |

Around them: [rfs-brand](https://github.com/Real-Fruit-Snacks/rfs-brand), the brand, profile art and repo templates, and [rfs.tools](https://rfs.tools/), the front door.

Retired: `Kraken` · `Maelstrom` · `Rapids` · `Lure` · `Undertow`, the water series. Archived and read-only, with no fixes or releases.

### How they're built

- One job per tool. If it needs a second README section to explain, it's two tools.
- Install is one line, shown first.
- "Tested on" is a list of real versions, not a promise.
- Known issues sit above the fold.

Issues and PRs welcome on any active repo. No roadmap, no Discord. If one saves you time, you can [sponsor me](https://github.com/sponsors/Real-Fruit-Snacks).

<sub>The board is drawn by [`art/make-board.py`](art/make-board.py) in Schibsted Grotesk and Fragment Mono.</sub>
