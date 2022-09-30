# Feature Flag Project
### SpaceBook

This project shows how one can target releases 
to specific groups or individuals. It also shows 
how organizations can activate features on the 
fly, and turn them of as necessary.

## Setup

1. In LaunchDarkly, create the following feature flags:
  * `enableRatings`
  * `newLayout`

1. Clone this repo and navigate to its directory in a terminal

1. From the terminal, run: `pip install -r requirements.txt`

1. Next, run: `mv app.ini.example app.ini`

1. Open the `app.ini` file and replace the fake SDK key with your SDK key
```
[App]
SDKKey=YOUR_KEY_HERE
```

1. From the terminal, run: `python app.py`

1. In your browser, navigate to http://127.0.0.1:5000

1. Next, run: `mv monitor.ini.example monitor.ini`

1. Open the `monitor.ini` file and replace the fake API key with your API key
```
[App]
APIKey=YOUR_KEY_HERE
```
1. In another terminal, run `python monitor.py`

1. When you turn on the `enableRatings` flag, the monitor will catch an error and automatically disable the flag

Enjoy!
