import json

def load_data(file_path):
    """loads a JSON-file and returns the information"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

# 1. load the file
animals_data = load_data("animals_data.json")

# 2. Generate HTML-Cards with final cards
output = ""
for animal in animals_data:
    name = animal.get("name")
    diet = animal.get("characteristics", {}).get("diet")
    locations = animal.get("locations", [])
    type_ = animal.get("characteristics", {}).get("type")

    output += '<li class="cards__item">\n'
    if name:
        output += f'  <div class="card__title">{name}</div>\n'
    output += '  <p class="card__text">\n'
    if diet:
        output += f'    <strong>Diet:</strong> {diet}<br/>\n'
    if locations:
        output += f'    <strong>Location:</strong> {locations[0]}<br/>\n'
    if type_:
        output += f'    <strong>Type:</strong> {type_}<br/>\n'
    output += '  </p>\n'
    output += '</li>\n'

# 3. load HTML-Template
with open("animals_template.html", "r", encoding="utf-8") as f:
    template = f.read()

# 4. replace placeholder
final_html = template.replace("__REPLACE_ANIMALS_INFO__", output)

# 5. write new HTML-file
with open("animals.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print("🎉 animals.html generated successfully!")

