import json


def load_data(file_path):
    """Loads a JSON-file and returns the information."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """ creates HTML for one animal object. """
    name = animal_obj.get("name")
    taxonomy = animal_obj.get("taxonomy", {})
    characteristics = animal_obj.get("characteristics", {})
    locations = animal_obj.get("locations", [])

    html = '<li class="cards__item">\n'
    if name:
        html += f'  <div class="card__title">{name}</div>\n'
    html += '  <p class="card__text">\n'

    if characteristics.get("diet"):
        html += f'    <strong>Diet:</strong> {characteristics["diet"]}<br/>\n'
    if locations:
        html += f'    <strong>Location:</strong> {locations[0]}<br/>\n'
    if characteristics.get("type"):
        html += f'    <strong>Type:</strong> {characteristics["type"]}<br/>\n'
    if taxonomy.get("scientific_name"):
        html += f'    <strong>Scientific Name:</strong> {taxonomy["scientific_name"]}<br/>\n'
    if characteristics.get("lifespan"):
        html += f'    <strong>Lifespan:</strong> {characteristics["lifespan"]}<br/>\n'
    if characteristics.get("skin_type"):
        html += f'    <strong>Skin Type:</strong> {characteristics["skin_type"]}<br/>\n'
    if characteristics.get("top_speed"):
        html += f'    <strong>Top Speed:</strong> {characteristics["top_speed"]}<br/>\n'
    if characteristics.get("slogan"):
        html += f'    <em>{characteristics["slogan"]}</em><br/>\n'

    html += '  </p>\n'
    html += '</li>\n'
    return html


def generate_html(data, template_path, output_path):
    """Creates the final HTML-file with animal cards."""
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    cards_html = "".join(serialize_animal(animal) for animal in data)
    final_html = template.replace("__REPLACE_ANIMALS_INFO__", cards_html)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(final_html)


def main():
    animals_data = load_data("animals_data.json")
    generate_html(animals_data, "animals_template.html", "animals.html")
    print("🎉 animals.html wurde erfolgreich erstellt!")


if __name__ == "__main__":
    main()

