import sys
import re

with open("/root/codalio/Codalio Projects/codalio-openhands/runtime_app_smoke.py", "r") as f:
    content = f.read()

content = content.replace("preview = (", "preview = PreviewDetails('http://127.0.0.1:5173/', 'http://127.0.0.1:3000/up') # (")

with open("/root/codalio/Codalio Projects/codalio-openhands/runtime_app_smoke.py", "w") as f:
    f.write(content)

print("patched")
