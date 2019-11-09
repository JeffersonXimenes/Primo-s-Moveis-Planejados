import re
def validar_data(sdata):
    import datetime

    try:
        data = datetime.datetime.strptime(sdata, "%d/%m/%Y")
    except:
        return False
    else:
        return True

def validar_campos(obj, campos, tipos):
    if type(obj) != dict:
        return False
    for k in obj:
        if k not in campos:
            return False
    for k in campos:
        if k not in obj:
            return False
    t = []
    for item in campos:
        t.append(type(obj[item]))
    if t != tipos:
        return False
    return True

def getData():
    from datetime import datetime
    data = datetime.now()
    data_e_hora_em_texto = data.strftime('%d/%m/%Y')
    return (data_e_hora_em_texto)
