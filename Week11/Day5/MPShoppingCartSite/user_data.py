import json


def add_user(username: str, email: str, password: int):
    users_file = "users.json"

    with open(users_file, 'w+') as file_obj:
        users_list = json.load(file_obj)
        if check_user(users_list, username):
            users_list[username] = {"username": username, "email": email, "password": password}
            json.dump(users_list, file_obj, indent=2, sort_keys=True)


def check_user(users_list: dict, username: str):
    return username not in users_list.keys() and username.isalnum() and username[0].isalpha()


