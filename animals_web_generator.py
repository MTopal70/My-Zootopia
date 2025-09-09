import json

def load_data(file_path):
    """Load a JSON-File and returns the information"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

# Load the file
animals_data = load_data("animals_data.json")

# Iterate trough the animals json file and print the informations
for animal in animals_data:
    name = animal.get("name")
    diet = animal.get("characteristics", {}).get("diet")
    locations = animal.get("locations", [])
    type_ = animal.get("characteristics", {}).get("type")

    if name:
        print(f"Name: {name}")
    if diet:
        print(f"Diet: {diet}")
    if locations:
        print(f"Location: {locations[0]}")
    if type_:
        print(f"Type: {type_}")
    print()  # white space between the animals
