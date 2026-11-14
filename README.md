<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/board-dark.svg">
  <img alt="Small tools, one job each. A board lists eleven tools, and for each in turn an orange seam sweeps its job, turning what goes in into what comes out: Ctrl+PrintScreen into screen-mark_2026-11-05_091412.png, Proton's Port pair 51037->51037 into listening port updated: 48213 -> 51037, HEVC 10-bit 1080p into H.264 8-bit 720p, and on through the list" src="assets/board-light.svg" width="100%">
</picture>

I write small tools for jobs I kept doing by hand. Each one does one job, and the board above runs through them: what you hand it, and what you get back. The same list, with a page for each tool, is at **[real-fruit-snacks.github.io](https://real-fruit-snacks.github.io/)**.

| Tool | Its job |
|---|---|
| [**screen-mark**](https://github.com/Real-Fruit-Snacks/screen-mark)<br><sub>Rust · Windows, Linux</sub> | Screenshot capture and annotation in pure Rust<br>`Ctrl+PrintScreen` → `screen-mark_2026-11-05_091412.png` |
| [**port-sync**](https://github.com/Real-Fruit-Snacks/port-sync)<br><sub>PowerShell · Windows</sub> | Keeps qBittorrent's port synced to Proton VPN<br>`Port pair 51037->51037` → `listening port updated: 48213 -> 51037` |
| [**carify**](https://github.com/Real-Fruit-Snacks/carify)<br><sub>sh, PowerShell · Windows, macOS, Linux</sub> | Convert video for Uconnect USB playback, via ffmpeg<br>HEVC 10-bit · 1080p · AC3 5.1 → H.264 8-bit · 720p · AAC stereo |
| [**certapi**](https://github.com/Real-Fruit-Snacks/certapi)<br><sub>C# · Windows</sub> | mTLS API client for the Windows certificate store<br>a client certificate in `CurrentUser\My` → 200 OK; the key never left the store |
| [**identity-gen**](https://github.com/Real-Fruit-Snacks/identity-gen)<br><sub>HTML · browser</sub> | Offline generator for throwaway signup identities<br>a signup form that wants too much → a stand-in: name, handle, passphrase |
| [**amazon-order-sync**](https://github.com/Real-Fruit-Snacks/amazon-order-sync)<br><sub>JavaScript · Windows, Linux</sub> | Syncs your Amazon orders into local Markdown notes<br>Amazon's order history → one `Order-<id>.md` per order |
| [**powershell-toolbox**](https://github.com/Real-Fruit-Snacks/powershell-toolbox)<br><sub>PowerShell · Windows</sub> | A grab-bag of my PowerShell scripts, each one standalone<br>every repo your `gh` login sees → one at a time: keep, archive or delete |
| [**forge-framework**](https://github.com/Real-Fruit-Snacks/forge-framework)<br><sub>Python</sub> | Modular offensive-security framework with a console<br>`use`, `set`, `run` → hosts, creds and loot in one workspace |
| [**open-file**](https://github.com/Real-Fruit-Snacks/open-file)<br><sub>TypeScript · browser</sub> | Learn and play chess in your browser, offline<br>a blunder in one of your games → a puzzle made from it |
| [**proxflow**](https://github.com/Real-Fruit-Snacks/proxflow)<br><sub>TypeScript · Windows</sub> | Proxmox map and lab builder that works offline<br>a Proxmox with no internet → a domain lab, built from one canvas |
| [**agent-toolkit**](https://github.com/Real-Fruit-Snacks/agent-toolkit)<br><sub>PowerShell · Windows, Linux</sub> | Pinned installers and config for my coding setup<br>a bare Windows machine → the same pinned coding setup |

Around them: [rfs-brand](https://github.com/Real-Fruit-Snacks/rfs-brand), the brand, profile art and repo templates, and [rfs.tools](https://rfs.tools/), the front door.

Retired: `Kraken` · `Maelstrom` · `Rapids` · `Lure` · `Undertow`, the water series. Archived and read-only, with no fixes or releases.

### How they're built

- One job per tool. If it needs a second README section to explain, it's two tools.
- Install is one line, shown first.
- "Tested on" is a list of real versions, not a promise.
- Known issues sit above the fold.

Issues and PRs welcome on any active repo. No roadmap, no Discord.

<sub>The board is drawn by [`art/make-board.py`](art/make-board.py) in Schibsted Grotesk and Fragment Mono.</sub>
