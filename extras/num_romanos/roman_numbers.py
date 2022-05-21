
# Practica para diccionarios, funciones y impresion de informacion, sumando unicode y nros romanos

def imprimir_dicc(dict):
    for id, item in dict.items():
        romstr=item["romanum"]
        decstr=str(item["decnum"])
        description=item["desc"]
        print(f"{romstr}\t{decstr}\t{description}")

print("Los caracteres unicodes de números romanos (o cualquier otro unicode) se indican con \\u (u escapada minúscula) y cada codigo ocupa 4 caracteres.")

print("\nNumeros romanos en mayúsculas para uso en relojes analógicos:")
I="\u2160" # 1
II="\u2161" # 2
III="\u2162" # 3
IV="\u2163" # 4
V="\u2164" # 5
VI="\u2165" # 6
VII="\u2166" # 7
VIII="\u2167" # 8
IX="\u2168" # 9
X="\u2169" # 10
XI="\u216A" # 11
XII="\u216B" # 12
hour_dict = {
    1: { "romanum": I, "decnum": 1, "desc": "Uno" },
    2: { "romanum": II, "decnum": 2, "desc": "Dos" },
    3: { "romanum": III, "decnum": 3, "desc": "Tres" },
    4: { "romanum": IV, "decnum": 4, "desc": "Cuatro" },
    5: { "romanum": V, "decnum": 5, "desc": "Cinco" },
    6: { "romanum": VI, "decnum": 6, "desc": "Seis" },
    7: { "romanum": VII, "decnum": 7, "desc": "Siete" },
    8: { "romanum": VIII, "decnum": 8, "desc": "Ocho" },
    9: { "romanum": IX, "decnum": 9, "desc": "Nueve" },
    10: { "romanum": X, "decnum": 10, "desc": "Diez" },
    11: { "romanum": XI, "decnum": 11, "desc": "Once" },
    12: { "romanum": XII, "decnum": 12, "desc": "Doce" }
}
imprimir_dicc(hour_dict)


print("\nNumeros romanos en minúsculas para uso en relojes analógicos:")
i="\u2170" # 1
ii="\u2171" # 2
iii="\u2172" # 3
iv="\u2173" # 4
v="\u2174" # 5
vi="\u2175" # 6
vii="\u2176" # 7
viii="\u2177" # 8
ix="\u2178" # 9
x="\u2179" # 10
xi="\u217A" # 11
xii="\u217B" # 12
hour_dict = {
    1: { "romanum": i, "decnum": 1, "desc": "Uno" },
    2: { "romanum": ii, "decnum": 2, "desc": "Dos" },
    3: { "romanum": iii, "decnum": 3, "desc": "Tres" },
    4: { "romanum": iv, "decnum": 4, "desc": "Cuatro" },
    5: { "romanum": v, "decnum": 5, "desc": "Cinco" },
    6: { "romanum": vi, "decnum": 6, "desc": "Seis" },
    7: { "romanum": vii, "decnum": 7, "desc": "Siete" },
    8: { "romanum": viii, "decnum": 8, "desc": "Ocho" },
    9: { "romanum": ix, "decnum": 9, "desc": "Nueve" },
    10: { "romanum": x, "decnum": 10, "desc": "Diez" },
    11: { "romanum": xi, "decnum": 11, "desc": "Once" },
    12: { "romanum": xii, "decnum": 12, "desc": "Doce" }
}
imprimir_dicc(hour_dict)


print("\nLetras de los números romanos (en mayúsculas):")
I="\u2160" # 1
V="\u2164" # 5
X="\u2169" # 10
L="\u216C" # 50
C="\u216D" # 100
D="\u216E" # 500
M="\u216F" # 1000
Cc="\u2180" # 1000 (alternativa)
leters_dict = {
    1: { "romanum": I, "decnum": 1, "desc": "Uno" },
    2: { "romanum": V, "decnum": 5, "desc": "Cinco" },
    3: { "romanum": X, "decnum": 10, "desc": "Diez" },
    4: { "romanum": L, "decnum": 50, "desc": "Cincuenta" },
    5: { "romanum": C, "decnum": 100, "desc": "Cien" },
    6: { "romanum": D, "decnum": 500, "desc": "Quinientos" },
    7: { "romanum": M, "decnum": 1000, "desc": "Mil" },
    8: { "romanum": Cc, "decnum": 1000, "desc": "Mil (otra forma alternativa)" },
}
imprimir_dicc(leters_dict)

print("\nLetras de los números romanos (en minúsculas):")
i="\u2170" # 1
v="\u2174" # 5
x="\u2179" # 10
l="\u217C" # 50
c="\u217D" # 100
d="\u217E" # 500
m="\u217F" # 1000
leters_dict = {
    1: { "romanum": i, "decnum": 1, "desc": "Uno" },
    2: { "romanum": v, "decnum": 5, "desc": "Cinco" },
    3: { "romanum": x, "decnum": 10, "desc": "Diez" },
    4: { "romanum": l, "decnum": 50, "desc": "Cincuenta" },
    5: { "romanum": c, "decnum": 100, "desc": "Cien" },
    6: { "romanum": d, "decnum": 500, "desc": "Quinientos" },
    7: { "romanum": m, "decnum": 1000, "desc": "Mil" },
}
imprimir_dicc(leters_dict)

print("\nUnicode posee caracteres especiales para representar algunos numeros grandes, multiplicando x10 el valor por cada raya interna:")
Dd="\u2181" # 5000 (D = 500 => con una D mas pequeña interior multiplica x10)
Cc="\u2182" # 10000 (La forma alternativa de mil con la misma forma mas pequena interior multiplica x10)
Ddd="\u2187" # 50000 (Idem Dd pero sumando 2 formas mas pequeñas => x 100)
Ccc="\u2188" # 100000 (Idem Cc pero sumando 2 formas mas pequeñas => x 100)
leters_dict = {
    1: { "romanum": Dd, "decnum": 5000, "desc": "Cinco mil" },
    2: { "romanum": Cc, "decnum": 10000, "desc": "Diez mil" },
    3: { "romanum": Ddd, "decnum": 50000, "desc": "Cincuenta mil" },
    4: { "romanum": Ccc, "decnum": 100000, "desc": "Cien mil" }
}
imprimir_dicc(leters_dict)
