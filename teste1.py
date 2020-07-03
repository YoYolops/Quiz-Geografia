import json
def ler_json():
    with open('dados.json', 'r', encoding = 'utf8') as f:
        return json.load(f)

data = ler_json()
usuarios = data['usuarios']
print(usuarios)
