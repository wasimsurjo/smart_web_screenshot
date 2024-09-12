
---

**NOTE:** Highly recommended that you update your browser and libraries, especially if you are on Linux, for the best experience.

I'm working on packing everything up so that you don't have to. Will release 2.0.0 when that milestone is reached ان شاء الله.

This package provides an easy-to-use tool for capturing screenshots of web pages. It supports custom user agents, proxies, and handles popups. Ideal for automated web scraping and testing purposes.

**Features:**
- Custom user agents
- Proxy support
- Popup handling
- Screenshot capture with configurable screen dimensions

**Installation:**
You can install this package using pip:

    pip3 install smart-web-screenshot

**Usage:**
Here’s a basic example of how to use the package:

```python3
from smart_web_screenshot import SmartWebScreenShot

# Initialize the screenshotter
screenshotter = SmartWebScreenShot()

# Setup the driver with optional parameters
screenshotter.setup_driver(
    headless=True,              # Run browser in headless mode
    user_agent="Your User Agent", # Optional: Custom user agent string
    proxy="http://your.proxy:port" # Optional: Proxy address
)

# Capture a screenshot
screenshotter.take_screenshot('https://google.com'8⅞
Feel free to adjust the parameters and example usage as needed for your specific requirements.