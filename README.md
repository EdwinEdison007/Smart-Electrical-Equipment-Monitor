# VoltWatch — Smart Electrical Equipment Monitoring Website

A full-stack educational website that simulates electrical current and temperature readings, classifies equipment conditions, plots sensor trends, stores session history, and exports events as CSV.

## Features
- Responsive dashboard for desktop and mobile
- Flask Python backend and JSON API
- Simulated current and temperature readings
- Normal, warning, critical, and sensor-fault scenarios
- Interactive dual-axis trend chart
- Recent event table and CSV export
- Clear session history and unit tests

## Safety note
This is a **software simulation**. It does not connect to physical sensors, operate a relay, or provide certified electrical protection. Thresholds are illustrative only. Do not use this project to control real electrical equipment without qualified engineering design, hardware isolation, fail-safe logic, validation, and appropriate protection devices.

## Requirements
- Windows, Linux, or macOS
- Python 3.10 or newer
- Internet access on first dashboard load for Chart.js and Google Fonts CDN; the Python backend runs locally.

## Run on Windows / VS Code
1. Extract the ZIP and open the folder in VS Code.
2. Create a virtual environment:
   ```powershell
   py -3.11 -m venv .venv
   ```
3. Activate it:
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```
   If PowerShell blocks activation, run this in the current terminal only, then activate again:
   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   .\.venv\Scripts\Activate.ps1
   ```
4. Install dependencies:
   ```powershell
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```
5. Start the website:
   ```powershell
   python app.py
   ```
6. Open **http://127.0.0.1:5000** in your browser.

## Run tests
```powershell
python -m pytest -v
```

## API endpoints
| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Website dashboard |
| GET | `/api/status` | Latest reading, recent history, status counts |
| POST | `/api/readings` | Generate a reading; JSON body: `{"mode":"CRITICAL"}` |
| POST | `/api/clear` | Clear in-memory session history |
| GET | `/api/export.csv` | Download readings as CSV |

Modes: `AUTO`, `NORMAL`, `WARNING`, `CRITICAL`, `SENSOR FAULT`.

## Demo thresholds
- **NORMAL:** current below 5 A and temperature below 50 °C
- **WARNING:** current at least 5 A or temperature at least 50 °C
- **CRITICAL:** current at least 7 A or temperature at least 70 °C
- **SENSOR FAULT:** missing, non-numeric, non-finite, negative current, or temperature outside -40 °C to 200 °C

Critical thresholds take priority over warning thresholds. Session history is held in memory and resets when the server restarts.

## Folder structure
```text
smart-electrical-equipment-monitor-website/
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
├── templates/index.html
├── static/css/styles.css
├── static/js/dashboard.js
├── src/fault_detection.py
├── src/sensor_simulator.py
├── tests/test_fault_detection.py
├── docs/architecture.md
├── docs/flowchart.md
└── data/.gitkeep
```

## Upload to GitHub
Create a new empty GitHub repository, then run these commands in this folder:
```powershell
git init
git add .
git commit -m "Build VoltWatch monitoring website"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/smart-electrical-equipment-monitor-website.git
git push -u origin main
```
Replace `YOUR_USERNAME` with your GitHub username.
