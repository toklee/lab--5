import re

with open('task2.html', 'r', encoding='utf-8') as file:
    text = file.read()

pattern = r'<\s*([a-zA-Z0-9]+)(\s+[a-zA-Z0-9\-:]+=\"[^\"]*\")*\s*[^/>]*>'
matches = re.findall(pattern, text)
tags = {match[0] for match in matches}

for tag in sorted(tags):
    print(tag)