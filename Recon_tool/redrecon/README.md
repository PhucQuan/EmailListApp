# RedRecon-Lite

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A lightweight cybersecurity reconnaissance tool for subdomain enumeration, port scanning, DNS analysis, technology fingerprinting, and directory discovery.

## 🎯 Features

- **Subdomain Enumeration** - Discover subdomains using Certificate Transparency logs (crt.sh)
- **Port Scanning** - Fast multi-threaded scanning of common service ports
- **DNS Records** - Comprehensive DNS record lookup (A, AAAA, MX, NS, TXT, CNAME, SOA)
- **Tech Stack Fingerprinting** - Identify web technologies, frameworks, and servers
- **Directory Fuzzing** - Discover exposed directories and sensitive files
- **JSON Export** - Structured output for further analysis
- **Risk Categorization** - Automatic risk assessment of findings

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/redrecon-lite.git
cd redrecon-lite

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage

```bash
# Scan a domain
python main.py --domain example.com

# Specify output file
python main.py --domain example.com --output my_report.json

# Limit number of subdomains to scan
python main.py --domain example.com --limit 10
```

## 📋 Requirements

- Python 3.8 or higher
- Internet connection
- Dependencies (auto-installed):
  - `requests` - HTTP requests
  - `dnspython` - DNS queries
  - `urllib3` - HTTP client

## 🔧 Usage Examples

### Scan a single domain
```bash
python main.py --domain tesla.com
```

### Scan with custom output
```bash
python main.py --domain github.com --output github_recon.json
```

### Quick scan (limit subdomains)
```bash
python main.py --domain example.com --limit 5
```

## 📊 Output Format

Results are saved in JSON format with the following structure:

```json
{
  "domain": "example.com",
  "scan_time": "2024-12-07T17:00:00",
  "subdomains": ["sub1.example.com", "sub2.example.com"],
  "hosts": {
    "sub1.example.com": {
      "ports": [{"port": 443, "service": "HTTPS"}],
      "dns": {"A": ["1.2.3.4"], "MX": ["mail.example.com"]},
      "technologies": {"server": "nginx", "technologies": ["React", "Cloudflare"]},
      "directories": [{"url": "https://sub1.example.com/admin", "status": 403}]
    }
  }
}
```

## 🎓 Educational Purpose

This tool is designed for:
- Learning cybersecurity reconnaissance techniques
- Understanding web infrastructure
- Practicing ethical hacking skills
- Security research and bug bounty hunting

## ⚠️ Legal Disclaimer

**IMPORTANT:** Only use this tool on domains you own or have explicit permission to test.

- Unauthorized scanning may be illegal in your jurisdiction
- Always obtain written permission before testing
- Respect rate limits and terms of service
- Use responsibly and ethically

The authors are not responsible for misuse of this tool.

## 🛠️ Project Structure

```
redrecon/
├── core/
│   ├── subdomain.py      # Subdomain enumeration
│   ├── portscan.py       # Port scanning
│   ├── dnsinfo.py        # DNS lookup
│   ├── techstack.py      # Technology fingerprinting
│   └── dirscan.py        # Directory fuzzing
├── utils/
│   └── __init__.py
├── main.py               # CLI interface
├── requirements.txt      # Dependencies
└── README.md            # This file
```

## 🔮 Roadmap

Future enhancements planned:
- [ ] Colored terminal output
- [ ] Risk scoring system
- [ ] PDF report generation
- [ ] Web UI dashboard
- [ ] Shodan API integration
- [ ] Email enumeration
- [ ] Subdomain takeover detection
- [ ] SSL/TLS analysis

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)

## 🙏 Acknowledgments

- [crt.sh](https://crt.sh) - Certificate Transparency logs
- [dnspython](https://www.dnspython.org/) - DNS toolkit
- Python community for excellent libraries

## 📚 Resources

- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [Bug Bounty Methodology](https://github.com/jhaddix/tbhm)
- [Penetration Testing Framework](http://www.vulnerabilityassessment.co.uk/Penetration%20Test.html)

---

**⭐ If you find this tool useful, please give it a star!**
