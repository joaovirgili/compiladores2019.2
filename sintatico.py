import json

with open('rl_table.json', 'r') as f:
    parsed_json = json.load(f)
    print(json.dumps(parsed_json, indent=4, sort_keys=True))