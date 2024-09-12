from setuptools import setup, find_packages

setup(
    name="smart_web_screenshot",
    version="1.2.4",
    packages=find_packages(),
    install_requires=["selenium", "undetected-chromedriver", "requests","webdriver-manager","selenium_stealth"],
    author="Wasim Surjo",
    author_email="wasimmiller55@gmail.com",
    description="A smart web screenshot taker that is designed to bypass several issues commonly faced by scapers",
    long_description='''
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
        from smart_web_screenshot import SmartWebScreenShot

        screenshotter = SmartWebScreenShot()
        screenshotter.setup_driver(headless=True)
        screenshotter.take_screenshot('https://google.com')
        screenshotter.close_driver()
        
        For more details, please refer to the documentation or GitHub repository. ''', 
    long_description_content_type='text/markdown', 
    license='MIT',
    python_requires='>=3.6',
    url="https://github.com/wasimsurjo/smart_web_screenshot",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
