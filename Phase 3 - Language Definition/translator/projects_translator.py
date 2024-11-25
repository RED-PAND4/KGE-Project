import json
def translate(source_json):
    # Open and load the target JSON file
    # with open(json_file, 'r') as file:
    #    data = json.load(file)

    with open(source_json, 'r', encoding="utf-8") as file:
        data = json.load(file)

    new_data = []
    for entry in data:
        new_entry = {
            "name": entry["Name"],
            "startDate": entry["Start Date"],
            "endDate": entry["End Date"],
            "coordinator": entry["Coordinator"],
            "partners": entry["Partners"],
            "members": entry["Members partecipating"],
            "funding": entry["Funding"],
            "researchTopic": entry["Related Topics"],
            "keyword": entry["Keywords"]
        }
        new_data.append(new_entry)

    return new_data


# Function to save the filtered data to a new file
def save_filtered_data(filtered_data, output_file):
    with open(output_file, 'w') as file:
        json.dump(filtered_data, file, indent=4)



# Example usage
sources = "./KRG-UNITN-projects.json"

outputs = "./Translated-KRG-UNITN-projects.json"

to_save = translate(sources)
save_filtered_data(to_save, outputs)