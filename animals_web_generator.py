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
    html += '  <div class="card__text">\n'
    html += '    <ul class="card__details">\n'

    if characteristics.get("diet"):
        html += f'      <li class="card__detail"><strong>Diet:</strong> {characteristics["diet"]}</li>\n'
    if locations:
        html += f'      <li class="card__detail"><strong>Location:</strong> {locations[0]}</li>\n'
    if characteristics.get("type"):
        html += f'      <li class="card__detail"><strong>Type:</strong> {characteristics["type"]}</li>\n'
    if taxonomy.get("scientific_name"):
        html += f'      <li class="card__detail"><strong>Scientific Name:</strong> {taxonomy["scientific_name"]}</li>\n'
    if characteristics.get("lifespan"):
        html += f'      <li class="card__detail"><strong>Lifespan:</strong> {characteristics["lifespan"]}</li>\n'
    if characteristics.get("slogan"):
        html += f'      <li class="card__detail"><em>{characteristics["slogan"]}</em></li>\n'

    html += '    </ul>\n'
    html += '  </div>\n'
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

