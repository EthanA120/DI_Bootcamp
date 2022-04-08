import requests
import json


def api_to_json():
    data = []
    file_name = "pets_json"

    for num in range(1, 100):
        a = requests.get(f"https://getyourpet.com/api/partnerpetsearch/{num}").json()
        if not a['PetId'] == ["PetId is invalid."]:
            data.append(a)
        else:
            num -= 1

    with open(f'static/{file_name}.json', 'w') as w_file:
        json.dump(data, w_file, indent=2, sort_keys=True)


if __name__ == '__main__':
    api_to_json()
