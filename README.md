# 🚀 Web Attack Surface Mapper (WASM)

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![Async](https://img.shields.io/badge/async-aiohttp-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)
![Status](https://img.shields.io/badge/status-active-success)

A fast, asynchronous web crawler built for **attack surface discovery** in web security testing.

WASM maps:

* URLs and endpoints
* Query parameters
* Forms (inputs, methods, actions)
* JavaScript-exposed endpoints

---

## 🧠 Overview

This tool is designed for:

* Penetration testers
* Bug bounty hunters
* Security engineers
* Developers validating application exposure

Inspired by methodologies from OWASP, WASM focuses on **visibility before exploitation**.

---

## ✨ Features

* ⚡ Async crawling (`aiohttp`)
* 🔍 Attack surface mapping
* 📄 Form + parameter extraction
* 🧬 JavaScript endpoint discovery
* 🧾 JSON reporting
* 🖥️ Verbose debug mode
* 📊 End-of-scan summary
* 🎯 Scope-restricted crawling


## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/wasm.git
cd wasm
```

### 2. Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate     # Linux / Mac
venv\Scripts\activate        # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### Basic Scan

```bash
python main.py -u https://example.com
```

### Verbose Mode

```bash
python main.py -u https://example.com -v
```

### Deep Crawl

```bash
python main.py -u https://example.com -d 4
```

### Full Custom Run

```bash
python main.py -u https://target.com -d 3 -r 10 -o results.json -v
```

---

## 🧾 CLI Options

| Option          | Description                        |
| --------------- | ---------------------------------- |
| `-u, --url`     | Target URL (required)              |
| `-d, --depth`   | Crawl depth (default: 2)           |
| `-r, --rate`    | Concurrent requests (default: 5)   |
| `-o, --output`  | Output file (default: output.json) |
| `-v, --verbose` | Enable debug output                |

---

## 📊 Output Format

Example JSON output:

```json
{
  "url": "https://example.com/login",
  "status": 200,
  "params": [],
  "forms": [
    {
      "action": "/auth",
      "method": "post",
      "inputs": ["username", "password"]
    }
  ],
  "depth": 1
}
```

---

## 🖥️ Sample Terminal Output

### Verbose Mode

```
[FETCH] https://example.com
[CRAWL] Depth 0 -> https://example.com (Status: 200)
[DISCOVERED] https://example.com/login
[FORMS] Found 1 forms
[RECORDED] https://example.com/login
```

### Scan Summary

```
========== SCAN SUMMARY ==========
Total URLs Crawled     : 12
Total Forms Found      : 3
Total Parameters Found : 5

Status Code Distribution:
  200 → 10
  404 → 2
==================================
```

---

## 🧱 Project Structure

```
webcrawler/
│
├── core/
├── extractors/
├── utils/
├── storage/
├── main.py
└── requirements.txt
```

---

## ⚠️ Limitations

* No JavaScript execution (SPA limitations)
* No authentication handling (yet)
* Not a vulnerability scanner (mapping only)

---

## 🛣️ Roadmap

* 🔐 Authentication (cookies, JWT)
* 🌐 Playwright integration (JS rendering)
* 🧪 Vulnerability scanning modules
* 📄 HTML report generation
* 🔌 Plugin architecture
* 📦 pip-installable CLI (`wasm`)

---

## 🧠 Best Practices

* Start with shallow depth (1–2)
* Increase rate gradually to avoid blocking
* Use verbose mode to debug behavior
* Combine with fuzzers/scanners for full assessments

---

## ⚖️ Disclaimer

This tool is intended for **authorized security testing and educational use only**.

Unauthorized scanning of systems without permission may be illegal.

---

## 📜 License

MIT License

---

## 🤝 Contributing

Pull requests are welcome. For major changes, open an issue first to discuss what you'd like to change.

---

## ⭐ Support

If you find this useful:

* Star the repo ⭐
* Share with the security community
* Contribute improvements

---
