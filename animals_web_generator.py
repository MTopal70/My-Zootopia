import json


def load_data(file_path):
    """Loads a JSON-file and returns the information."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """ creates HTML for one animal object. """
    name = animal_obj.get("name")
    diet = animal_obj.get("characteristics", {}).get("diet")
    locations = animal_obj.get("locations", [])
    type_ = animal_obj.get("characteristics", {}).get("type")

    html = '<li class="cards__item">\n'
    if name:
        html += f'  <div class="card__title">{name}</div>\n'
    html += '  <p class="card__text">\n'
    if diet:
        html += f'    <strong>Diet:</strong> {diet}<br/>\n'
    if locations:
        html += f'    <strong>Location:</strong> {locations[0]}<br/>\n'
    if type_:
        html += f'    <strong>Type:</strong> {type_}<br/>\n'
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

