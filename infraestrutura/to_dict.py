import jsons

def to_dict(obj):
    return jsons.dump(obj, strip_privates = True)

def to_dict_list(lista):
    resultado = []
    for item in lista:
        resultado.append(to_dict(item))
    return resultado