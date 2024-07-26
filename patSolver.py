import json

# Load your JSON data
with open('patterns.json', 'r') as file:
    data = json.load(file)

# Count the keys like "remoteAccessMFA"
key_count = len(data)

# Find all unique values in attackIDs that start with "T"
unique_values = set()
unique_mvalues = set()
for key in data:
    attack_ids = data[key]['attackIDs']['Tactic']
    for tactic in attack_ids:
        for value in attack_ids[tactic]:
            if value.startswith('T'):
                unique_values.add(value)
    attack_mit = data[key]['attackIDs']['Mitigations']
    for mit in attack_mit:
        unique_mvalues.add(mit)


# Count the unique values
unique_values_count = len(unique_values)

print(f'Number of keys like "remoteAccessMFA": {key_count}')
print(f'Number of unique values in attackIDs starting with "T": {unique_values_count}')
print(f'Number of unique values in attackIDs starting with "M": {len(unique_mvalues)}')
