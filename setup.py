from setuptools import setup, find_packages

setup(
    name="smart_web_screenshot",
    version="1.1",
    packages=find_packages(),
    install_requires=["selenium", "undetected-chromedriver", "requests","webdriver-manager","selenium_stealth"],
    author="Wasim Surjo",
    author_email="wasimmiller55@gmail.com",
    description="A smart web screenshot taker that is designed to bypass several issues commonly faced by scapers",
    url="https://github.com/wasimsurjo/smart_web_screenshot",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
