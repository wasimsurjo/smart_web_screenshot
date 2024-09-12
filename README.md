This package provides an easy-to-use tool for capturing screenshots of web pages. It supports custom user agents, proxies, and handles popups. 
    Ideal for automated web scraping and testing purposes. 

    **Features:**
    - Custom user agents
    - Proxy support
    - Popup handling
    - Screenshot capture with configurable screen dimensions

    **Installation:**
    You can install this package using pip:

        pip install smart-web-screenshot

    **Usage:**
    Here’s a basic example of how to use the package:

    ```python3
    from smart_web_screenshot import SmartWebScreenshot

    screenshotter = SmartWebScreenshot()
    screenshotter.setup_driver(headless=True)
    screenshotter.take_screenshot('https://google.com')
    screenshotter.close_driver()
    
    For more details, please refer to the documentation or GitHub repository. 
