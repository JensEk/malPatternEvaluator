import json

# Load the json file
with open('attackData.json') as f:
    data = json.load(f)

# Get the 'Tactic' dictionary
tactic_dict = data['ATT&CK']['Tactic']

# Initialize a set to store unique 'T****' keys
unique_keys = set()

# Initialize a set to store unique 'coreLangTarget' values
unique_coreLangTarget_values = set()

cnt = 0
# Iterate over the keys under 'Tactic'
for tactic in tactic_dict:
    print(f"\nTactic: {tactic}")
    
    # Iterate over the keys under each tactic
    for key in tactic_dict[tactic]:
        # Check if the key matches the format 'T****'
        if key.startswith('T') and key[1:].isdigit():
            unique_keys.add(key)
            
            # Get the 'coreLangTarget' dictionary
            coreLangTarget_dict = tactic_dict[tactic][key]['coreLangTarget']
            
            

            # Iterate over the keys in 'coreLangTarget' and add the values to the set
            for target in coreLangTarget_dict:
                unique_coreLangTarget_values.update(coreLangTarget_dict[target])

            if len(coreLangTarget_dict) == 1:
                for target in coreLangTarget_dict:
                    if len(coreLangTarget_dict[target]) == 1:
                        cnt += 1

    # Print the unique 'coreLangTarget' values for each tactic
    print(f"Unique 'coreLangTarget' values for {tactic}: {unique_coreLangTarget_values}")
    
    # Clear the set for the next tactic
    unique_coreLangTarget_values.clear()

# Print the total unique 'T****' keys
print(f"\nTotal unique 'T****' keys: {len(unique_keys)}")

# Print the total unique mapping to coreLang assets
print(f"\nTotal unique mapping to coreLang assets: {cnt}")


# Initialize a dictionary to store the count of unique 'T****' keys for each 'coreLangTarget'
coreLangTarget_key_counts = {}

# Iterate over the keys under 'Tactic'
for tactic in tactic_dict:
    # Iterate over the keys under each tactic
    for key in tactic_dict[tactic]:
        # Check if the key matches the format 'T****'
        if key.startswith('T') and key[1:].isdigit():
            # Get the 'coreLangTarget' dictionary
            coreLangTarget_dict = tactic_dict[tactic][key]['coreLangTarget']
            
            # Iterate over the keys in 'coreLangTarget'
            for target in coreLangTarget_dict:
                # If the target is not in the dictionary, add it with the key as the value
                if target not in coreLangTarget_key_counts:
                    coreLangTarget_key_counts[target] = {key}
                # If the target is in the dictionary, add the key to its value set
                else:
                    coreLangTarget_key_counts[target].add(key)

# Print the count of unique 'T****' keys for each 'coreLangTarget'
for target, keys in coreLangTarget_key_counts.items():
    print(f"{target} is related to {len(keys)} unique keys")


# Initialize a dictionary to store the count of unique 'T****' keys for each value in 'coreLangTarget'
coreLangTarget_value_key_counts = {}

# Iterate over the keys under 'Tactic'
for tactic in tactic_dict:
    # Iterate over the keys under each tactic
    for key in tactic_dict[tactic]:
        # Check if the key matches the format 'T****'
        if key.startswith('T') and key[1:].isdigit():
            # Get the 'coreLangTarget' dictionary
            coreLangTarget_dict = tactic_dict[tactic][key]['coreLangTarget']
            
            # Iterate over the keys in 'coreLangTarget'
            for target in coreLangTarget_dict:
                # Iterate over the values in each 'coreLangTarget'
                for value in coreLangTarget_dict[target]:
                    # If the value is not in the dictionary, add it with the key as the value
                    if value not in coreLangTarget_value_key_counts:
                        coreLangTarget_value_key_counts[value] = {key}
                    # If the value is in the dictionary, add the key to its value set
                    else:
                        coreLangTarget_value_key_counts[value].add(key)

# Print the count of unique 'T****' keys for each value in 'coreLangTarget'
for value, keys in coreLangTarget_value_key_counts.items():
    print(f"{value} is related to {len(keys)} unique keys")


# Initialize a counter for 'T****' keys not mapped to any 'coreLangTarget'
no_coreLangTarget_count = 0

# Iterate over the keys under 'Tactic'
for tactic in tactic_dict:
    # Iterate over the keys under each tactic
    for key in tactic_dict[tactic]:
        # Check if the key matches the format 'T****'
        if key.startswith('T') and key[1:].isdigit():
            # Check if 'coreLangTarget' is empty
            if not tactic_dict[tactic][key]['coreLangTarget']:
                no_coreLangTarget_count += 1

# Print the count of 'T****' keys not mapped to any 'coreLangTarget'
print(f"\nNumber of 'T****' keys not mapped to any 'coreLangTarget': {no_coreLangTarget_count}")


# Initialize a dictionary to store the unique 'CAPEC_id' keys for each key in 'coreLangTarget'
coreLangTarget_key_CAPEC_id_counts = {}

# Iterate over the keys under 'Tactic'
for tactic in tactic_dict:
    # Iterate over the keys under each tactic
    for key in tactic_dict[tactic]:
        # Check if the key matches the format 'T****'
        if key.startswith('T') and key[1:].isdigit():
            # Get the 'coreLangTarget' and 'CAPEC_id' dictionaries
            coreLangTarget_dict = tactic_dict[tactic][key]['coreLangTarget']
            CAPEC_id_dict = tactic_dict[tactic][key]['CAPEC_id']
            
            # Iterate over the keys in 'coreLangTarget'
            for target in coreLangTarget_dict:
                # If the target is not in the dictionary, add it with the 'CAPEC_id' keys as the value
                if target not in coreLangTarget_key_CAPEC_id_counts:
                    coreLangTarget_key_CAPEC_id_counts[target] = set(CAPEC_id_dict.keys())
                # If the target is in the dictionary, add the 'CAPEC_id' keys to its value set
                else:
                    coreLangTarget_key_CAPEC_id_counts[target].update(CAPEC_id_dict.keys())

# Print the unique 'CAPEC_id' keys for each key in 'coreLangTarget'
for target, keys in coreLangTarget_key_CAPEC_id_counts.items():
    print(f"{target} is mapped to {len(keys)} unique 'CAPEC_id' keys")



# Initialize a dictionary to store the unique 'CAPEC_id' keys for each value in 'coreLangTarget'
coreLangTarget_CAPEC_id_counts = {}

# Iterate over the keys under 'Tactic'
for tactic in tactic_dict:
    # Iterate over the keys under each tactic
    for key in tactic_dict[tactic]:
        # Check if the key matches the format 'T****'
        if key.startswith('T') and key[1:].isdigit():
            # Get the 'coreLangTarget' and 'CAPEC_id' dictionaries
            coreLangTarget_dict = tactic_dict[tactic][key]['coreLangTarget']
            CAPEC_id_dict = tactic_dict[tactic][key]['CAPEC_id']
            
            # Iterate over the keys in 'coreLangTarget'
            for target in coreLangTarget_dict:
                # Iterate over the values in each 'coreLangTarget'
                for value in coreLangTarget_dict[target]:
                    # If the value is not in the dictionary, add it with the 'CAPEC_id' keys as the value
                    if value not in coreLangTarget_CAPEC_id_counts:
                        coreLangTarget_CAPEC_id_counts[value] = set(CAPEC_id_dict.keys())
                    # If the value is in the dictionary, add the 'CAPEC_id' keys to its value set
                    else:
                        coreLangTarget_CAPEC_id_counts[value].update(CAPEC_id_dict.keys())

# Print the unique 'CAPEC_id' keys for each value in 'coreLangTarget'
for value, keys in coreLangTarget_CAPEC_id_counts.items():
    print(f"{value} is mapped to {len(keys)} unique 'CAPEC_id' keys")

# Initialize a list to store 'T****' keys not mapped to any 'coreLangTarget'
no_coreLangTarget_keys = []

# Iterate over the keys under 'Tactic'
for tactic in tactic_dict:
    # Iterate over the keys under each tactic
    for key in tactic_dict[tactic]:
        # Check if the key matches the format 'T****'
        if key.startswith('T') and key[1:].isdigit():
            # Check if 'coreLangTarget' is empty
            if not tactic_dict[tactic][key]['coreLangTarget']:
                no_coreLangTarget_keys.append((tactic, key))

# Print the keys and 'T****' keys not mapped to any 'coreLangTarget'
for tactic, key in no_coreLangTarget_keys:
    print(f"Key: {tactic}, Technique Key: {key}")
