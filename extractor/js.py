import re

def extract_js_endpoints(js_text):
    pattern = r"https?://[^\s\"']+|/api/[^\s\"']+"
    return re.findall(pattern, js_text)
