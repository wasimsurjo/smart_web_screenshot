# Info

A smart web screenshot taker that is designed to bypass several issues commonly faced by scapers

from smart_screenshot import SmartWebScreenShot


client = SmartWebScreenShot()

client.setup_driver()

client.take_screenshot("https://www.google.com")