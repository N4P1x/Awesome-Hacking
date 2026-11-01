<div align="center">

# :crossed_swords: Awesome Red Team

[![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)
[![Stars](https://img.shields.io/github/stars/geevarghesekthomas84-sys/awesome-red-team?style=for-the-badge&color=00ff41&logo=github)](https://github.com/geevarghesekthomas84-sys/awesome-red-team/stargazers)
[![Forks](https://img.shields.io/github/forks/geevarghesekthomas84-sys/awesome-red-team?style=for-the-badge&color=ff0040)](https://github.com/geevarghesekthomas84-sys/awesome-red-team/network/members)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

**A curated collection of awesome tools, frameworks, resources, and references for Red Team operations and offensive security professionals.**

*Organized by the MITRE ATT&CK Kill Chain phases.*

---

:star: **Star this repo** if you find it useful — it helps others discover it!

</div>

---

## :bookmark_tabs: Table of Contents

- [Reconnaissance](#reconnaissance)
- [OSINT](#osint)
- [Weaponization](#weaponization)
- [Initial Access](#initial-access)
- [Execution](#execution)
- [Persistence](#persistence)
- [Privilege Escalation](#privilege-escalation)
- [Defense Evasion](#defense-evasion)
- [Credential Access](#credential-access)
- [Lateral Movement](#lateral-movement)
- [Collection & Exfiltration](#collection--exfiltration)
- [Command & Control (C2)](#command--control-c2)
- [Active Directory Attacks](#active-directory-attacks)
- [Wireless Attacks](#wireless-attacks)
- [Web Application Attacks](#web-application-attacks)
- [Social Engineering](#social-engineering)
- [Cloud Security & Exploitation](#cloud-security--exploitation)
- [Mobile Security](#mobile-security)
- [Hardware Hacking](#hardware-hacking)
- [Reporting & Documentation](#reporting--documentation)
- [Training & Labs](#training--labs)
- [Books & References](#books--references)

---

## Reconnaissance

> *Mapping the attack surface before firing the first shot.*

| Tool | Description |
|------|-------------|
| [Nmap](https://github.com/nmap/nmap) | The gold standard network scanner — port scanning, service detection, OS fingerprinting |
| [Masscan](https://github.com/robertdavidgraham/masscan) | Fastest Internet port scanner — scan entire Internet in 6 minutes |
| [RustScan](https://github.com/RustScan/RustScan) | Modern, fast port scanner that feeds into Nmap |
| [Amass](https://github.com/owasp-amass/amass) | In-depth attack surface mapping and asset discovery |
| [Subfinder](https://github.com/projectdiscovery/subfinder) | Fast passive subdomain enumeration tool |
| [httpx](https://github.com/projectdiscovery/httpx) | Multi-purpose HTTP toolkit for probing |
| [Shodan](https://www.shodan.io/) | Search engine for Internet-connected devices |
| [Censys](https://censys.io/) | Internet-wide scanning search engine |
| [Recon-ng](https://github.com/lanmaster53/recon-ng) | Full-featured web reconnaissance framework |
| [theHarvester](https://github.com/laramies/theHarvester) | E-mails, subdomains, hosts, IPs discovery |
| [dnsrecon](https://github.com/darkoperator/dnsrecon) | DNS enumeration and scanning tool |
| [Gobuster](https://github.com/OJ/gobuster) | Directory/file & DNS busting tool |
| [ffuf](https://github.com/ffuf/ffuf) | Fast web fuzzer written in Go |
| [Nuclei](https://github.com/projectdiscovery/nuclei) | Fast and customizable vulnerability scanner |
| [WhatWeb](https://github.com/urbanadventurer/WhatWeb) | Web scanner for identifying technologies |

---

## OSINT

> *Open Source Intelligence — know thy target before they know you.*

| Tool | Description |
|------|-------------|
| [Maltego](https://www.maltego.com/) | Interactive data mining and link analysis |
| [SpiderFoot](https://github.com/smicallef/spiderfoot) | Automated OSINT collection tool |
| [Sherlock](https://github.com/sherlock-project/sherlock) | Hunt down social media accounts by username |
| [GHunt](https://github.com/mxrch/GHunt) | Investigate Google accounts with emails |
| [Photon](https://github.com/s0md3v/Photon) | Incredibly fast crawler designed for OSINT |
| [Twint](https://github.com/twintproject/twint) | Twitter scraping without API |
| [Holehe](https://github.com/megadose/holehe) | Check if email is attached to accounts |
| [linkedin2username](https://github.com/initstring/linkedin2username) | Generate usernames from LinkedIn |
| [Maigret](https://github.com/soxoj/maigret) | Collect user accounts across 2500+ sites |
| [ExifTool](https://exiftool.org/) | Read/write metadata in files |

---

## Weaponization

> *Crafting payloads, building implants.*

| Tool | Description |
|------|-------------|
| [msfvenom](https://www.metasploit.com/) | Payload generation (part of Metasploit) |
| [Veil](https://github.com/Veil-Framework/Veil) | Generate AV-evading payloads |
| [Shellter](https://www.shellterproject.com/) | Dynamic shellcode injection tool |
| [Donut](https://github.com/TheWover/donut) | Generate position-independent shellcode from .NET assemblies |
| [ScareCrow](https://github.com/Optiv/ScareCrow) | EDR bypass payload creation framework |
| [Nim](https://nim-lang.org/) + [OffensiveNim](https://github.com/byt3bl33d3r/OffensiveNim) | Nim for implant development |
| [macro_pack](https://github.com/sevagas/macro_pack) | Automate Office doc weaponization |
| [Evil-WinRM](https://github.com/Hackplayers/evil-winrm) | WinRM shell for pentesting |

---

## Initial Access

> *Getting the first foothold.*

| Tool | Description |
|------|-------------|
| [Evilginx2](https://github.com/kgretzky/evilginx2) | Man-in-the-middle attack framework for phishing |
| [GoPhish](https://github.com/gophish/gophish) | Open-source phishing framework |
| [King Phisher](https://github.com/rsmusllp/king-phisher) | Phishing campaign toolkit |
| [SET (Social Engineering Toolkit)](https://github.com/trustedsec/social-engineer-toolkit) | Advanced social engineering attacks |
| [Modlishka](https://github.com/drk1wi/Modlishka) | Reverse proxy for phishing |
| [o365spray](https://github.com/0xZDH/o365spray) | Microsoft O365 password spraying tool |
| [TREVORspray](https://github.com/blacklanternsecurity/TREVORspray) | Multi-threaded O365 sprayer |

---

## Execution

> *Running code on the target.*

| Tool | Description |
|------|-------------|
| [Metasploit Framework](https://github.com/rapid7/metasploit-framework) | The legendary exploitation framework |
| [CrackMapExec](https://github.com/Porchetta-Industries/CrackMapExec) | Swiss army knife for pentesting networks |
| [Impacket](https://github.com/fortra/impacket) | Collection of Python network protocol tools |
| [PowerSploit](https://github.com/PowerShellMafia/PowerSploit) | PowerShell post-exploitation framework |
| [Nishang](https://github.com/samratashok/nishang) | Offensive PowerShell scripts |
| [LOLBAS](https://lolbas-project.github.io/) | Living Off The Land Binaries |
| [GTFOBins](https://gtfobins.github.io/) | Unix binaries for privilege escalation |

---

## Persistence

> *Making sure you keep coming back.*

| Tool | Description |
|------|-------------|
| [SharPersist](https://github.com/mandiant/SharPersist) | Windows persistence toolkit in C# |
| [PoshC2](https://github.com/nettitude/PoshC2) | C2 with built-in persistence |
| [Registry Persistence](https://attack.mitre.org/techniques/T1547/) | MITRE ATT&CK registry run key techniques |
| [Scheduled Tasks](https://attack.mitre.org/techniques/T1053/) | Task-based persistence |
| [WMI Persistence](https://attack.mitre.org/techniques/T1546/003/) | WMI event subscription persistence |

---

## Privilege Escalation

> *Going from user to god.*

| Tool | Description |
|------|-------------|
| [WinPEAS](https://github.com/carlospolop/PEASS-ng/tree/master/winPEAS) | Windows Privilege Escalation Awesome Script |
| [LinPEAS](https://github.com/carlospolop/PEASS-ng/tree/master/linPEAS) | Linux Privilege Escalation Awesome Script |
| [BeRoot](https://github.com/AlessandroZ/BeRoot) | Privilege escalation checker |
| [PowerUp](https://github.com/PowerShellMafia/PowerSploit/tree/master/Privesc) | PowerShell privesc checks |
| [Linux Exploit Suggester](https://github.com/The-Z-Labs/linux-exploit-suggester) | Suggest kernel exploits |
| [PrintSpoofer](https://github.com/itm4n/PrintSpoofer) | Service account to SYSTEM |
| [JuicyPotato](https://github.com/ohpe/juicy-potato) | Windows local privilege escalation |
| [Potato attacks](https://jlajara.gitlab.io/Potatoes_Windows_Privesc) | All potato-based privesc techniques |
| [pspy](https://github.com/DominicBreuker/pspy) | Monitor Linux processes without root |

---

## Defense Evasion

> *Flying under the radar.*

| Tool | Description |
|------|-------------|
| [ScareCrow](https://github.com/Optiv/ScareCrow) | EDR bypass framework |
| [Inceptor](https://github.com/klezVirus/inceptor) | Bypass AV/EDR through automation |
| [AMSI Bypass](https://amsi.fail/) | AMSI bypass techniques collection |
| [Invoke-Obfuscation](https://github.com/danielbohannon/Invoke-Obfuscation) | PowerShell script obfuscator |
| [Chameleon](https://github.com/klezVirus/chameleon) | PowerShell obfuscation tool |
| [Nimcrypt2](https://github.com/icyguider/Nimcrypt2) | PE packer/loader using Nim |
| [Freeze](https://github.com/Optiv/Freeze) | Payload toolkit for EDR bypass |

---

## Credential Access

> *Stealing the keys to the kingdom.*

| Tool | Description |
|------|-------------|
| [Mimikatz](https://github.com/gentilkiwi/mimikatz) | The legendary credential dumping tool |
| [Hashcat](https://github.com/hashcat/hashcat) | World's fastest password recovery |
| [John the Ripper](https://github.com/openwall/john) | Open-source password cracker |
| [Responder](https://github.com/lgandx/Responder) | LLMNR/NBT-NS/mDNS poisoner |
| [LaZagne](https://github.com/AlessandroZ/LaZagne) | Credentials recovery from local computer |
| [Rubeus](https://github.com/GhostPack/Rubeus) | Kerberos abuse toolkit |
| [Kerbrute](https://github.com/ropnop/kerbrute) | Kerberos brute-forcing tool |
| [Spray](https://github.com/Greenwolf/Spray) | Password spraying tool |
| [DonPAPI](https://github.com/login-securite/DonPAPI) | DPAPI credential dumper |

---

## Lateral Movement

> *Moving through the network like a ghost.*

| Tool | Description |
|------|-------------|
| [CrackMapExec](https://github.com/Porchetta-Industries/CrackMapExec) | Swiss army knife for pentesting networks |
| [Impacket](https://github.com/fortra/impacket) | PSExec, WMIExec, SMBExec, etc. |
| [Evil-WinRM](https://github.com/Hackplayers/evil-winrm) | WinRM pentesting shell |
| [Chisel](https://github.com/jpillora/chisel) | Fast TCP/UDP tunnel over HTTP |
| [Ligolo-ng](https://github.com/nicocha30/ligolo-ng) | Advanced tunneling/pivoting tool |
| [ProxyChains](https://github.com/haad/proxychains) | TCP connection redirection through proxies |
| [sshuttle](https://github.com/sshuttle/sshuttle) | Poor man's VPN over SSH |
| [rpivot](https://github.com/klsecservices/rpivot) | Reverse SOCKS proxy for pivoting |

---

## Collection & Exfiltration

> *Getting the loot out.*

| Tool | Description |
|------|-------------|
| [DNSExfiltrator](https://github.com/Arno0x/DNSExfiltrator) | Data exfiltration over DNS |
| [PyExfil](https://github.com/ytisf/PyExfil) | Python exfiltration techniques |
| [Cloakify](https://github.com/TryCatchHCF/Cloakify) | Data exfiltration & infiltration |
| [PacketWhisper](https://github.com/TryCatchHCF/PacketWhisper) | Stego-based data exfiltration |
| [rclone](https://rclone.org/) | Cloud storage data transfer (used by APTs) |

---

## Command & Control (C2)

> *Maintaining access and control.*

| Tool | Description |
|------|-------------|
| [Cobalt Strike](https://www.cobaltstrike.com/) | Industry-standard adversary simulation (Commercial) |
| [Sliver](https://github.com/BishopFox/sliver) | Open-source cross-platform C2 |
| [Havoc](https://github.com/HavocFramework/Havoc) | Modern, malleable C2 framework |
| [Mythic](https://github.com/its-a-feature/Mythic) | Collaborative, multi-platform C2 |
| [PoshC2](https://github.com/nettitude/PoshC2) | PowerShell-based C2 proxy |
| [Merlin](https://github.com/Ne0nd0g/merlin) | HTTP/2 cross-platform C2 |
| [Villain](https://github.com/t3l3machus/Villain) | C2 framework with auto-bypass |
| [Covenant](https://github.com/cobbr/Covenant) | .NET-based C2 framework |

---

## Active Directory Attacks

> *Owning the enterprise — because AD is always the crown jewel.*

| Tool | Description |
|------|-------------|
| [BloodHound](https://github.com/BloodHoundAD/BloodHound) | AD attack path mapping |
| [SharpHound](https://github.com/BloodHoundAD/SharpHound) | Data collector for BloodHound |
| [Rubeus](https://github.com/GhostPack/Rubeus) | Kerberos interaction and abuse |
| [Certify](https://github.com/GhostPack/Certify) | AD Certificate Services abuse |
| [Certipy](https://github.com/ly4k/Certipy) | AD CS exploitation in Python |
| [ADCSKiller](https://github.com/grimlockx/ADCSKiller) | Automated AD CS attacks |
| [PowerView](https://github.com/PowerShellMafia/PowerSploit/blob/master/Recon/PowerView.ps1) | AD enumeration in PowerShell |
| [Pingcastle](https://github.com/vletoux/pingcastle) | AD security assessment |
| [ADRecon](https://github.com/adrecon/ADRecon) | Active Directory recon tool |
| [Coercer](https://github.com/p0dalirius/Coercer) | Windows authentication coercion |

---

## Wireless Attacks

> *When wires aren't required.*

| Tool | Description |
|------|-------------|
| [Aircrack-ng](https://github.com/aircrack-ng/aircrack-ng) | Complete WiFi security toolkit |
| [Bettercap](https://github.com/bettercap/bettercap) | Swiss army knife for network attacks |
| [Wifite2](https://github.com/derv82/wifite2) | Automated wireless attack tool |
| [hostapd-mana](https://github.com/sensepost/hostapd-mana) | Rogue AP and credential harvesting |
| [Fluxion](https://github.com/FluxionNetwork/fluxion) | Evil twin attack tool |
| [WiFi Pumpkin](https://github.com/P0cL4bs/wifipumpkin3) | Rogue AP framework |
| [Flipper Zero](https://flipperzero.one/) | Multi-tool for hardware & wireless hacking |

---

## Web Application Attacks

> *Because every company has a website.*

| Tool | Description |
|------|-------------|
| [Burp Suite](https://portswigger.net/burp) | The web application security testing platform |
| [SQLMap](https://github.com/sqlmapproject/sqlmap) | Automated SQL injection tool |
| [XSStrike](https://github.com/s0md3v/XSStrike) | Advanced XSS detection suite |
| [Dalfox](https://github.com/hahwul/dalfox) | Fast XSS scanner |
| [Arjun](https://github.com/s0md3v/Arjun) | HTTP parameter discovery |
| [ParamSpider](https://github.com/devanshbatham/ParamSpider) | Parameter mining from web archives |
| [Commix](https://github.com/commixproject/commix) | Command injection exploiter |
| [NoSQLMap](https://github.com/codingo/NoSQLMap) | NoSQL injection tool |
| [JWT_Tool](https://github.com/ticarpi/jwt_tool) | JWT security testing toolkit |
| [WPScan](https://github.com/wpscanteam/wpscan) | WordPress security scanner |

---

## Social Engineering

> *Hacking the human.*

| Tool | Description |
|------|-------------|
| [SET](https://github.com/trustedsec/social-engineer-toolkit) | Social Engineering Toolkit |
| [GoPhish](https://github.com/gophish/gophish) | Phishing campaigns framework |
| [Evilginx2](https://github.com/kgretzky/evilginx2) | MitM phishing framework |
| [Lucy](https://lucysecurity.com/) | Social engineering platform |
| [BeEF](https://github.com/beefproject/beef) | Browser Exploitation Framework |
| [Zphisher](https://github.com/htr-tech/zphisher) | Automated phishing tool |
| [CredSniper](https://github.com/ustayready/CredSniper) | Phishing framework with 2FA bypass |

---

## Cloud Security & Exploitation

> *The cloud is just someone else's computer — and it's hackable.*

| Tool | Description |
|------|-------------|
| [Pacu](https://github.com/RhinoSecurityLabs/pacu) | AWS exploitation framework |
| [ScoutSuite](https://github.com/nccgroup/ScoutSuite) | Multi-cloud security auditing |
| [Prowler](https://github.com/prowler-cloud/prowler) | AWS/Azure/GCP security tool |
| [CloudFox](https://github.com/BishopFox/cloudfox) | Cloud penetration testing automation |
| [S3Scanner](https://github.com/sa7mon/S3Scanner) | Scan for misconfigured S3 buckets |
| [MicroBurst](https://github.com/NetSPI/MicroBurst) | Azure security assessment scripts |
| [ROADtools](https://github.com/dirkjanm/ROADtools) | Azure AD exploration framework |

---

## Mobile Security

> *Billions of targets in everyone's pocket.*

| Tool | Description |
|------|-------------|
| [Frida](https://github.com/frida/frida) | Dynamic instrumentation toolkit |
| [Objection](https://github.com/sensepost/objection) | Runtime mobile exploration |
| [MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF) | Mobile security framework |
| [APKTool](https://github.com/iBotPeaches/Apktool) | Reverse engineer Android APKs |
| [Jadx](https://github.com/skylot/jadx) | Android DEX to Java decompiler |

---

## Hardware Hacking

> *When software isn't enough.*

| Tool | Description |
|------|-------------|
| [Flipper Zero](https://flipperzero.one/) | Multi-tool for RFID, Sub-GHz, NFC, IR |
| [HackRF One](https://greatscottgadgets.com/hackrf/) | Software Defined Radio |
| [WiFi Pineapple](https://shop.hak5.org/products/wifi-pineapple) | Wireless auditing platform |
| [USB Rubber Ducky](https://shop.hak5.org/products/usb-rubber-ducky) | Keystroke injection attack tool |
| [Bash Bunny](https://shop.hak5.org/products/bash-bunny) | Multi-vector USB attack platform |
| [LAN Turtle](https://shop.hak5.org/products/lan-turtle) | Covert network access tool |
| [Proxmark3](https://proxmark.com/) | RFID research and cloning |

---

## Reporting & Documentation

> *If you didn't document it, it didn't happen.*

| Tool | Description |
|------|-------------|
| [Ghostwriter](https://github.com/GhostManager/Ghostwriter) | Engagement management and reporting |
| [Pwndoc](https://github.com/pwndoc/pwndoc) | Pentest report generator |
| [PlexTrac](https://plextrac.com/) | Security assessment reporting (Commercial) |
| [Dradis](https://github.com/dradis/dradis-ce) | Collaborative security reporting |
| [SysReptor](https://github.com/Syslifters/sysreptor) | Pentest reporting tool |

---

## Training & Labs

> *Practice makes perfect. Stay sharp.*

| Platform | Description |
|----------|-------------|
| [HackTheBox](https://www.hackthebox.com/) | Hands-on cybersecurity training |
| [TryHackMe](https://tryhackme.com/) | Beginner-friendly security labs |
| [PentesterLab](https://pentesterlab.com/) | Web security exercises |
| [PortSwigger Web Security Academy](https://portswigger.net/web-security) | Free web security training |
| [VulnHub](https://www.vulnhub.com/) | Vulnerable VMs for practice |
| [DVWA](https://github.com/digininja/DVWA) | Damn Vulnerable Web Application |
| [GOAD](https://github.com/Orange-Cyberdefense/GOAD) | Game of Active Directory lab |
| [Exploit Education](https://exploit.education/) | Learn exploit development |
| [OverTheWire](https://overthewire.org/wargames/) | Wargames for security |
| [CyberDefenders](https://cyberdefenders.org/) | Blue team challenge platform |

---

## Books & References

> *Knowledge is the ultimate weapon.*

| Book | Author |
|------|--------|
| **The Hacker Playbook 3** | Peter Kim |
| **Red Team Field Manual (RTFM)** | Ben Clark |
| **Penetration Testing** | Georgia Weidman |
| **Hacking: The Art of Exploitation** | Jon Erickson |
| **The Web Application Hacker's Handbook** | Dafydd Stuttard |
| **Active Directory Attacks** | Nikhil Mittal |
| **Black Hat Python** | Justin Seitz |
| **Malware Analysis Techniques** | Dylan Barker |

---

## :handshake: Contributing

Contributions are welcome! Please submit a PR to add a new tool or resource.

1. Fork the repository
2. Add your resource in the appropriate category
3. Submit a pull request

---

## :page_facing_up: License

This project is licensed under the MIT License.

---

<div align="center">

**:star: If this helped you, give it a star!**

*Curated with :skull: by [Gg](https://github.com/geevarghesekthomas84-sys)*

</div>
