<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:14b8a6&height=170&section=header&text=CSV%20Formula%20Guard&fontColor=ffffff&fontSize=38&animation=fadeIn" alt="CSV Formula Guard banner" width="100%"/>
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=19&duration=3000&pause=900&color=14B8A6&center=true&vCenter=true&width=820&lines=Detect%20spreadsheet%20formula%20injection%20before%20sharing%20CSV%20exports" alt="Typing title"/>

[![License](https://img.shields.io/github/license/CyberLoop-dev/csv-formula-guard)](LICENSE)
![Language](https://img.shields.io/github/languages/top/CyberLoop-dev/csv-formula-guard)
![Stars](https://img.shields.io/github/stars/CyberLoop-dev/csv-formula-guard?style=flat)
![Last commit](https://img.shields.io/github/last-commit/CyberLoop-dev/csv-formula-guard)

<img src="assets/illustration.svg" alt="CSV Formula Guard illustration" width="92%"/>
</div>

## :compass: Overview

A conservative local CSV scanner that flags cells beginning with spreadsheet formula characters and can write a sanitized copy with a leading apostrophe. The original file is never modified.

## :sparkles: Features

- :white_check_mark: Scans every CSV cell and reports row and column
- :white_check_mark: Flags values beginning with =, +, -, or @ after whitespace
- :white_check_mark: Can write a separate apostrophe-prefixed sanitized copy
- :white_check_mark: Uses Python's CSV parser and preserves table structure

## :clapper: Demo

```bash
python main.py scan examples/untrusted.csv
```

The example runs locally; no hosted service or upload is required.

## :rocket: Quick Start

```bash
python -m pip install -r requirements.txt
python main.py scan examples/untrusted.csv
```

Run `python main.py --help` to see all supported options.

## :toolbox: Tech Stack

- Python 3.10+ standard library (csv)
- Automated tests: unittest
- Local-first processing

## :file_folder: Folder Structure

```text
csv-formula-guard/\n├── main.py\n├── requirements.txt\n├── tests/test_core.py\n├── examples/untrusted.csv\n└── assets/illustration.svg
```

## :world_map: Roadmap

- [x] Core workflow and CLI
- [x] Example input and tests
- [ ] Additional report formats
- [ ] Continuous integration on supported platforms

## :handshake: Contributing

Issues and pull requests are welcome. Keep changes focused, document behavior changes, and add tests for new features.

## :page_facing_up: License

MIT - see [LICENSE](LICENSE).

<div align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:14b8a6,100:0f172a&height=100&section=footer" alt="Animated wave footer" width="100%"/></div>
