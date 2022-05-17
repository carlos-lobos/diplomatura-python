lista = ["elemento1n1", "elemento2n1", "elemento3n1",
["elemento1n2", "elemento2n2", "elemento3n2",
["elemento1n3", "elemento2n3", "elemento3n3"]]]

def recorrer_lista(item=[], nivel=0):
    for x in item:
        if isinstance(x, list):
            recorrer_lista(x,nivel+1)
        else:
            print("    "*nivel + x)

recorrer_lista(lista)

# Adivina el mensaje oculto ... (los 8 escalones, jeje)
recorrer_lista(["8", "_",["7", "_",["6", "_",["5", "_",["4", "_",["3", "_",["2", "_",["1", "_",["0", "_"]]]]]]]]])
