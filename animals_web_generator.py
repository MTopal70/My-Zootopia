import json

def load_data(file_path):
    """loads a JSON-file and returns the information"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

# 1. load the file
animals_data = load_data("animals_data.json")

# 2. Generate HTML-Cards
output = ""
for animal in animals_data:
    name = animal.get("name")
    diet = animal.get("characteristics", {}).get("diet")
    locations = animal.get("locations", [])
    type_ = animal.get("characteristics", {}).get("type")

    output += '<li class="cards__item">\n'
    if name:
        output += f"Name: {name}<br/>\n"
    if diet:
        output += f"Diet: {diet}<br/>\n"
    if locations:
        output += f"Location: {locations[0]}<br/>\n"
    if type_:
        output += f"Type: {type_}<br/>\n"
    output += '</li>\n'

# 3. Load HTML-Template
with open("animals_template.html", "r", encoding="utf-8") as f:
    template = f.read()

# 4. replace placeholder
final_html = template.replace("__REPLACE_ANIMALS_INFO__", output)

# 5. write the new HTML file
with open("animals.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print("✅ HTML-Cards generated successfully!")

