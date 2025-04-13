# Singapore Weather Forecast

CLI tool for retrieving weather forecasts.

For a given area, it will show:
- 24h forecast
- 2h forecast 
- 4-day outlook (Singapore)

## Setup
- Python 3.10+
- Unicode compatible shell recommended

### Dependencies
```bash
pip install requests
```

### Clone
```bash
git clone https://github.com/geraldywz/tcx1004.git
```

### Download
https://github.com/geraldywz/tcx1004/archive/refs/heads/main.zip

## Usage


### Start
```bash
python WeatherCLI.py
```

### Pick an option
```bash
 1. Ang Mo Kio
 2. Bedok
 ...
 48. Exit
```

### Get forecast
```bash
☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁
📍      Clementi
        24h Forecast: Cloudy
         2h Forecast: Cloudy

🇸🇬      Singapore
        4-Day Outlook
        2025-04-14: Afternoon thundery showers
        2025-04-15: Late morning and early afternoon thundery showers
        2025-04-16: Afternoon thundery showers
        2025-04-17: Afternoon thundery showers
☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁

```

### Return to menu
```bash
Press Enter to go back to the menu.
# Pick an option again.
```