import json

with open("./src/theme.json", 'r') as f:
    theme = json.load(f)

print(theme['version'])
print(theme['colours']['equation'])