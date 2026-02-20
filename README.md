
# ⚡ SocialIntellax

# Advanced OSINT & Threat Intelligence Framework 
Built for Ethical Hacking, Cybersecurity Research, and Digital Footprinting.


> **Author:** Inayat Hussain Chohan  
> Cybersecurity Researcher | OSINT Builder | AI Strategist  
> Country: Pakistan 🇵🇰

---

## 🔍 Overview

**SocialIntellax** is a modular, command-line-based framework designed for **open-source intelligence (OSINT)** and **threat intelligence gathering** across major platforms. It combines automation, ethical reconnaissance techniques, and modular intelligence into a unified Python-based toolkit.

This project is purpose-built for:

- Penetration testers
- Threat analysts
- Cybercrime investigators
- Red teams
- Digital forensics professionals
- Ethical hackers

---

## 🧠 Core Features

- ✅ 20 OSINT modules targeting usernames, emails, domains, and IPs
- ✅ Google dorking automation for asset exposure
- ✅ DeepScan mode for multi-vector intelligence in a single run
- ✅ Clean CLI interface with banner, color-coded output, and logging
- ✅ Data output saving with timestamped files
- ✅ Designed for extensibility, ethical use, and security research

---

## 📦 Modules

| # | Module                 | Description |
|---|------------------------|-------------|
| 01 | Instagram OSINT        | Metadata, profile checks, Google dorks |
| 02 | Facebook OSINT         | Public visibility and mentions |
| 03 | LinkedIn OSINT         | Profile & company dorks |
| 04 | Twitter/X OSINT        | Handle checks, dorks |
| 05 | YouTube OSINT          | Channel presence & mentions |
| 06 | GitHub OSINT           | Profile leaks, exposed secrets |
| 07 | Google Dorking         | Automated dork-based reconnaissance |
| 08 | Email Lookup           | Leak discovery & pattern generation |
| 09 | Username Search        | Cross-platform identity detection |
| 10 | Pastebin Scraper       | Leaked dumps and email discovery |
| 11 | Dark Web (Simulated)   | Breach simulation & dorks |
| 12 | GeoIP Lookup           | IP location & ISP metadata |
| 13 | Metadata Extractor     | File creation data (simulated) |
| 14 | Reverse Image Search   | Google, Yandex, TinEye |
| 15 | Phishing URL Check     | TLD, SSL, and shortening detection |
| 16 | Mutuals Detector       | Identity overlaps across platforms |
| 17 | Reddit OSINT           | Public post and credential exposure |
| 18 | Archive.org Lookup     | Time-based domain snapshots |
| 19 | Company Dorking        | Employee leaks, internal portals |
| 20 | Discord Lookup         | Server, mention, invite tracking |

---

## 🚀 DeepScan Mode

Run all applicable modules against a single target:
```bash
python3 socialintellax.py
# Select Option 21: Deep Scan

🛠 Installation
🔗 Requirements

    Python 3.7+

    Linux/macOS/WSL (Parrot OS, Kali Linux, Ubuntu tested)

📦 Install via Virtual Environment (Recommended)

# Clone the repo
git clone https://github.com/inayathussain786305/socialintellax.git
cd socialintellax

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the tool
python3 socialintellax.py

✅ Required Packages:

    requests

    colorama

    beautifulsoup4

    tabulate

If not using a requirements.txt, install manually:

pip install requests colorama beautifulsoup4 tabulate

📂 Output

Results are saved in:

/socialintellax_output/

Each file is timestamped and categorized by module and target.
⚖️ Legal Disclaimer

This tool is intended for educational and lawful purposes only.
Misuse of SocialIntellax for unauthorized access, surveillance, or profiling may violate laws in your jurisdiction.

    Always obtain proper authorization before conducting any form of reconnaissance or OSINT targeting.

🤝 Contribution

Contributions, feature suggestions, and pull requests are welcome.

    Fork the project

    Create a new branch (feature/your-feature)

    Commit your changes

    Push and submit a pull request

If you're an OSINT researcher or cybersecurity enthusiast — feel free to collaborate.
📫 Contact

Inayat Hussain Chohan
Email: your_email@example.com
Location: Ghotki, Sindh, Pakistan 🇵🇰
LinkedIn: linkedin.com/in/inayatchohan
Medium: medium.com/@yourusername
⭐ Credits

This framework was built through strategic use of automation, intelligent assistance, and deep manual engineering.

    SocialIntellax is a symbol of what is possible when human determination meets modern technology.

📜 License

This project is licensed under the MIT License — see the LICENSE file for details.
