import os
import re

for root, _, files in os.walk("src/pages"):
    for file in files:
        if file.endswith(".tsx") or file.endswith(".ts"):
            path = os.path.join(root, file)
            with open(path, "r") as f:
                content = f.read()

            # Add back imports that were deleted if they are used
            if "useState(" in content and "import { useState" not in content and "import React, { useState" not in content:
                content = 'import { useState, useEffect, useMemo } from "react";\n' + content
                
            # Replace React.useEffect with useEffect
            content = content.replace("React.useEffect", "useEffect")

            with open(path, "w") as f:
                f.write(content)
