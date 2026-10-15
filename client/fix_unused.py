import subprocess
import re
import os

res = subprocess.run(["npm", "run", "build"], capture_output=True, text=True)
output = res.stdout

for line in output.split("\n"):
    m = re.match(r'^src/(.*\.tsx?):(\d+):(\d+) - error TS6133: \'(.*?)\' is declared but its value is never read.', line)
    if m:
        filepath = "src/" + m.group(1)
        line_no = int(m.group(2))
        ident = m.group(4)
        
        # We know the line number. Let's remove the identifier from the line.
        with open(filepath, "r") as f:
            lines = f.readlines()
            
        target_line = lines[line_no - 1]
        
        # If it's a destructured import: import { A, B } from ...
        # Regex to remove `ident,` or `, ident` or `ident`
        new_line = re.sub(r'\b' + ident + r'\b\s*,?', '', target_line)
        new_line = re.sub(r',\s*}', ' }', new_line)
        new_line = re.sub(r'\{\s*,', '{ ', new_line)
        new_line = re.sub(r'\{\s*\}', '{}', new_line)
        
        # If the line becomes `import {} from ...` we can just delete it or leave it
        if "import {}" in new_line or "import { }" in new_line or new_line.strip() == "":
            new_line = ""
            
        # Or if it's a variable declaration: const { data, isLoading } = ...
        if "const" in target_line or "let" in target_line:
            new_line = re.sub(r'\b' + ident + r'\b\s*(:\s*[^,}]+)?\s*,?', '', target_line)
            new_line = re.sub(r',\s*}', ' }', new_line)
            new_line = re.sub(r'\{\s*,', '{ ', new_line)
            
        lines[line_no - 1] = new_line
        
        with open(filepath, "w") as f:
            f.writelines(lines)
