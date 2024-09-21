import json
from collections import defaultdict

# Load the json file
with open('attackData.json') as f:
    data = json.load(f)

# Get the 'Tactic' dictionary
tactic_dict = data['ATT&CK']['Tactic']
miti_dict = data['ATT&CK']['Mitigation']

unique_coreLangAsset_miti = {}
coreLangAsset_count = defaultdict(lambda: defaultdict(int))
empty_coreLangAsset_count = 0
mitig = 0
# Iterate through each mitigation
for mitigation in miti_dict.values():
    
    mitig += 1
    if not mitigation["coreLangAsset"].items():
        empty_coreLangAsset_count += 1
        continue
    for asset_type, assets in mitigation["coreLangAsset"].items():
        if not asset_type in unique_coreLangAsset_miti:
            unique_coreLangAsset_miti[asset_type] = 1
        else:
            unique_coreLangAsset_miti[asset_type] += 1
        for asset in assets:
            coreLangAsset_count[asset_type][asset] += 1

# Print the results
for asset_type, assets in coreLangAsset_count.items():
    for asset, count in assets.items():
        print(f"{asset_type}, {asset}, {count}")

print(f"Mitigations: {mitig}")
print(f"Mitigations with empty coreLangAsset: {empty_coreLangAsset_count}")
print(f"Unique coreLangAsset in Mitigations: {unique_coreLangAsset_miti}")

# Initialize a set to store unique 'T****' keys
unique_keys = set()

# Initialize a set to store unique 'coreLangAsset' values
unique_coreLangAsset_values = set()

cnt = 0
# Iterate over the keys under 'Tactic'
for tactic in tactic_dict:
    print(f"\nTactic: {tactic}")
    
    # Iterate over the keys under each tactic
    for key in tactic_dict[tactic]:
        # Check if the key matches the format 'T****'
        if key.startswith('T') and key[1:].isdigit():
            unique_keys.add(key)
            
            # Get the 'coreLangAsset' dictionary
            coreLangAsset_dict = tactic_dict[tactic][key]['coreLangAsset']
            
            

            # Iterate over the keys in 'coreLangAsset' and add the values to the set
            for target in coreLangAsset_dict:
                unique_coreLangAsset_values.update(coreLangAsset_dict[target])

            if len(coreLangAsset_dict) == 1:
                for target in coreLangAsset_dict:
                    if len(coreLangAsset_dict[target]) == 1:
                        cnt += 1

    # Print the unique 'coreLangAsset' values for each tactic
    print(f"Unique 'coreLangAsset' values for {tactic}: {unique_coreLangAsset_values}")
    
    # Clear the set for the next tactic
    unique_coreLangAsset_values.clear()

# Print the total unique 'T****' keys
print(f"\nTotal unique 'T****' keys: {len(unique_keys)}")

# Print the total unique mapping to coreLang assets
print(f"\nTotal unique mapping to coreLang assets: {cnt}")




# Initialize a dictionary to store the count of unique 'T****' keys for each 'coreLangAsset'
coreLangAsset_key_counts = {}

# Iterate over the keys under 'Tactic'
for tactic in tactic_dict:
    # Iterate over the keys under each tactic
    for key in tactic_dict[tactic]:
        # Check if the key matches the format 'T****'
        if key.startswith('T') and key[1:].isdigit():
            # Get the 'coreLangAsset' dictionary
            coreLangAsset_dict = tactic_dict[tactic][key]['coreLangAsset']
            
            # Iterate over the keys in 'coreLangAsset'
            for target in coreLangAsset_dict:
                # If the target is not in the dictionary, add it with the key as the value
                if target not in coreLangAsset_key_counts:
                    coreLangAsset_key_counts[target] = {key}
                # If the target is in the dictionary, add the key to its value set
                else:
                    coreLangAsset_key_counts[target].add(key)

# Print the count of unique 'T****' keys for each 'coreLangAsset'
for target, keys in coreLangAsset_key_counts.items():
    print(f"{target} is related to {len(keys)} unique keys")


# Initialize a dictionary to store the count of unique 'T****' keys for each value in 'coreLangAsset'
coreLangAsset_value_key_counts = {}

# Iterate over the keys under 'Tactic'
for tactic in tactic_dict:
    # Iterate over the keys under each tactic
    for key in tactic_dict[tactic]:
        # Check if the key matches the format 'T****'
        if key.startswith('T') and key[1:].isdigit():
            # Get the 'coreLangAsset' dictionary
            coreLangAsset_dict = tactic_dict[tactic][key]['coreLangAsset']
            
            # Iterate over the keys in 'coreLangAsset'
            for target in coreLangAsset_dict:
                # Iterate over the values in each 'coreLangAsset'
                for value in coreLangAsset_dict[target]:
                    # If the value is not in the dictionary, add it with the key as the value
                    if value not in coreLangAsset_value_key_counts:
                        coreLangAsset_value_key_counts[value] = {key}
                    # If the value is in the dictionary, add the key to its value set
                    else:
                        coreLangAsset_value_key_counts[value].add(key)

# Print the count of unique 'T****' keys for each value in 'coreLangAsset'
for value, keys in coreLangAsset_value_key_counts.items():
    print(f"{value} is related to {len(keys)} unique keys")


# Initialize a counter for 'T****' keys not mapped to any 'coreLangAsset'
no_coreLangAsset_count = 0

# Iterate over the keys under 'Tactic'
for tactic in tactic_dict:
    # Iterate over the keys under each tactic
    for key in tactic_dict[tactic]:
        # Check if the key matches the format 'T****'
        if key.startswith('T') and key[1:].isdigit():
            # Check if 'coreLangAsset' is empty
            if not tactic_dict[tactic][key]['coreLangAsset']:
                no_coreLangAsset_count += 1

# Print the count of 'T****' keys not mapped to any 'coreLangAsset'
print(f"\nNumber of 'T****' keys not mapped to any 'coreLangAsset': {no_coreLangAsset_count}")


# Initialize a dictionary to store the unique 'CAPEC_id' keys for each key in 'coreLangAsset'
coreLangAsset_key_CAPEC_id_counts = {}

# Iterate over the keys under 'Tactic'
for tactic in tactic_dict:
    # Iterate over the keys under each tactic
    for key in tactic_dict[tactic]:
        # Check if the key matches the format 'T****'
        if key.startswith('T') and key[1:].isdigit():
            # Get the 'coreLangAsset' and 'CAPEC_id' dictionaries
            coreLangAsset_dict = tactic_dict[tactic][key]['coreLangAsset']
            CAPEC_id_dict = tactic_dict[tactic][key]['CAPEC_id']
            
            # Iterate over the keys in 'coreLangAsset'
            for target in coreLangAsset_dict:
                # If the target is not in the dictionary, add it with the 'CAPEC_id' keys as the value
                if target not in coreLangAsset_key_CAPEC_id_counts:
                    coreLangAsset_key_CAPEC_id_counts[target] = set(CAPEC_id_dict.keys())
                # If the target is in the dictionary, add the 'CAPEC_id' keys to its value set
                else:
                    coreLangAsset_key_CAPEC_id_counts[target].update(CAPEC_id_dict.keys())

# Print the unique 'CAPEC_id' keys for each key in 'coreLangAsset'
for target, keys in coreLangAsset_key_CAPEC_id_counts.items():
    print(f"{target} is mapped to {len(keys)} unique 'CAPEC_id' keys")



# Initialize a dictionary to store the unique 'CAPEC_id' keys for each value in 'coreLangAsset'
coreLangAsset_CAPEC_id_counts = {}

# Iterate over the keys under 'Tactic'
for tactic in tactic_dict:
    # Iterate over the keys under each tactic
    for key in tactic_dict[tactic]:
        # Check if the key matches the format 'T****'
        if key.startswith('T') and key[1:].isdigit():
            # Get the 'coreLangAsset' and 'CAPEC_id' dictionaries
            coreLangAsset_dict = tactic_dict[tactic][key]['coreLangAsset']
            CAPEC_id_dict = tactic_dict[tactic][key]['CAPEC_id']
            
            # Iterate over the keys in 'coreLangAsset'
            for target in coreLangAsset_dict:
                # Iterate over the values in each 'coreLangAsset'
                for value in coreLangAsset_dict[target]:
                    # If the value is not in the dictionary, add it with the 'CAPEC_id' keys as the value
                    if value not in coreLangAsset_CAPEC_id_counts:
                        coreLangAsset_CAPEC_id_counts[value] = set(CAPEC_id_dict.keys())
                    # If the value is in the dictionary, add the 'CAPEC_id' keys to its value set
                    else:
                        coreLangAsset_CAPEC_id_counts[value].update(CAPEC_id_dict.keys())

# Print the unique 'CAPEC_id' keys for each value in 'coreLangAsset'
for value, keys in coreLangAsset_CAPEC_id_counts.items():
    print(f"{value} is mapped to {len(keys)} unique 'CAPEC_id' keys")

# Initialize a list to store 'T****' keys not mapped to any 'coreLangAsset'
no_coreLangAsset_keys = []

# Iterate over the keys under 'Tactic'
for tactic in tactic_dict:
    # Iterate over the keys under each tactic
    for key in tactic_dict[tactic]:
        # Check if the key matches the format 'T****'
        if key.startswith('T') and key[1:].isdigit():
            # Check if 'coreLangAsset' is empty
            if not tactic_dict[tactic][key]['coreLangAsset']:
                no_coreLangAsset_keys.append((tactic, key))

# Print the keys and 'T****' keys not mapped to any 'coreLangAsset'
for tactic, key in no_coreLangAsset_keys:
    print(f"Key: {tactic}, Technique Key: {key}")
