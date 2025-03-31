def change():
    expense = 23.75
    money = 100
    change = money - expense
    pesos = int(change)
    cents = int((change - pesos) * 100)
    print(f'Ingresar gasto:\n{expense}\nDinero recibido\n{money}\n\nVuelto\n\nPesos:\n{pesos}\nCentavos:\n{cents}')

change()