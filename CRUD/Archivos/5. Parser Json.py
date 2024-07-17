import json

def parse_json(path: str)-> list:
    with open(path, "r") as archivo:
        diccionario = json.load(archivo)

    print(diccionario)


parse_json("clientes.json")