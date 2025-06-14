# System Monitor

A simple, real-time terminal system monitor with an adorable ASCII bunny splash. Displays CPU, RAM, disk usage, battery status, uptime, and network speeds in a fixed-width “box” that updates in place.

---

## ✨ Features

- **Real-time stats**: CPU %, RAM %, disk %, battery % & plugged-in status  
- **Uptime**: Days, hours, minutes, seconds  
- **Network throughput**: Download & upload speeds (Mbps)  
- **Clean fixed-width display**: No “growing” borders as numbers change  
- **Escape to quit**: Press `Esc` to exit the monitor  
- **Tiny ASCII bunny**: Makes your terminal a little more fun  

---

## 📋 Requirements

- Python 3.7+  
- [psutil](https://pypi.org/project/psutil/)  
- [keyboard](https://pypi.org/project/keyboard/)  

Install dependencies with:

```bash
pip install psutil keyboard
```

## 📦 Installation

### 📥 Via `pip` (recommended)

Clone the repo and install:

```bash
cd /path/to/project-root
pip install .
```

## 🚀 Usage

```bash
# Run with default settings (0.5s interval)
hopmon

# Customize polling interval (e.g. 1.0s)
hopmon --interval 1.0

# If running the script directly:
python systemMonitor.py --interval 0.5

# Toggle the bunny splash on/off
hopmon --bunny
```
### 🛠 Manual Usage

Download or clone `systemMonitor.py`, then run:

```bash
python systemMonitor.py --interval 0.5
```

## ⚙️ Configuration Options

| Flag               | Description                     | Default |
|--------------------|---------------------------------|---------|
| `-i`, `--interval` | Seconds between updates         | 0.5     |
| `-b`, `--bunny`    | Toggle little bunny splash      | False   |
| `-h`, `--help`     | Show help message and exit      | —       |


Made and Maintained by: Davis Yew
