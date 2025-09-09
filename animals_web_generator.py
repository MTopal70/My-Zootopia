import json

def load_data(file_path):
    """loads a JSON-file and returns the information"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

# 1. load the file
animals_data = load_data("animals_data.json")

# 2. generates the animals information as text
output = ""
for animal in animals_data:
    name = animal.get("name")
    diet = animal.get("characteristics", {}).get("diet")
    locations = animal.get("locations", [])
    type_ = animal.get("characteristics", {}).get("type")

    if name:
        output += f"Name: {name}\n"
    if diet:
        output += f"Diet: {diet}\n"
    if locations:
        output += f"Location: {locations[0]}\n"
    if type_:
        output += f"Type: {type_}\n"
    output += "\n"  # Whitespace between the animals

# 3. load the HTML-Template
with open("animals_template.html", "r", encoding="utf-8") as f:
    template = f.read()

# 4. replace the placeholder
final_html = template.replace("__REPLACE_ANIMALS_INFO__", output)

# 5. write the new HTML file
with open("animals.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print("✅ animals.html generated successfully!")

