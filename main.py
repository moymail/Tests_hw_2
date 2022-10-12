import requests

token = ""
ya_url = "https://cloud-api.yandex.net/v1/disk/resources"

def get_headers():
    return {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(token)}

def add_folder(folder_name):
    headers = get_headers()
    params = {'path': folder_name}
    response = requests.put(ya_url, headers=headers, params=params)
    print(response)
    return response.status_code


if __name__ == '__main__':
    folder_name = input('Введите название папки: ')
    add_folder(folder_name)
