import json

# Create a json data
json_data = {
    '001': {
        'Name': 'Allen',
        'Age': 22,
        'Interest': ['music', 'instruments']
    },
    '002': {
        'Name': 'Ted',
        'Age': 25,
        'Interest': ['reading', 'sports']
    }
}

# Dumps the data to string
json_string = json.dumps(json_data)
print(type(json_string))
print(json_string)

with open('./test.json', 'w', encoding='utf-8') as f:
    f.write(json_string)

with open('./test.json', 'r', encoding='utf-8') as f:
    loaded_json_string = f.read()

# Load the string to dictionary and list
loaded_json_data = json.loads(loaded_json_string)
print(type(loaded_json_data))
print(loaded_json_data)
