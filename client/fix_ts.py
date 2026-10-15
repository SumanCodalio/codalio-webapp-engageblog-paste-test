import os
import re

for root, _, files in os.walk("src"):
    for file in files:
        if file.endswith(".tsx") or file.endswith(".ts"):
            path = os.path.join(root, file)
            with open(path, "r") as f:
                content = f.read()

            # Fix VariantProps type import
            content = re.sub(r'import { cva, VariantProps } from "class-variance-authority"', r'import { cva, type VariantProps } from "class-variance-authority"', content)

            # Fix React unused import
            content = re.sub(r'import React(?:, \{[^}]*\})? from "react";\n', '', content)
            content = re.sub(r'import React, \{', 'import {', content)
            
            # FormEvent type import
            content = re.sub(r'import { useState, FormEvent } from "react";', r'import { useState, type FormEvent } from "react";', content)

            with open(path, "w") as f:
                f.write(content)
