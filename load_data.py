import requests

security_backend = "http//127.0.0.1:8080"
headers = {"Content-Type": "application/json; charset=utf-8"}

# create roles
roles = [
    {"name": "Administrador", "descripción": "Administrador del sistema de la registraduria"},
    {"name": "jurado", "descripción": "Jurado que ingresa los votos"},
    {"name": "candidato", "descripción":"Quien participa para ser elegido"}
]

url = f'{security_backend}/rol/insert'
admin = None
for rol in roles:
    response = requests.post(url, headers=headers, json=rol)
    if rol.get('name') == "Administrador":
        admin = response.json()
    print('=' * 30)

# Add registry permissions
modules = ['table', 'candidate', 'political_party', 'vote', 'user', 'rol']
endpoints = [('s', 'GET'), ('/?', 'GET'), ('/insert', 'POST'), ('/update/?', 'PUT'), ('/delete/?', 'DELETE')]
url = f'{security_backend}/permission/insert'
for module in modules:
    for endpoint in endpoints:
        permission = f'/{module}{endpoint}'
        body = {
            "url": permission,
            "method": method
        }
        response = requests.post(url, headers=headers, json=body)
        print(response.json())
        data_ = response.json()
        url_relation = f'{security_backend}/rol/update/{admin.get("idRol")}/add_permission/{data_.get("id")}'
        response = requests.put(url_relation, headers=headers)
