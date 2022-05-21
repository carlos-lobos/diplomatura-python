print("Los hexadecimales de emojis (o de cualquier otra cosa) son indicados con \\U (U mayusculas escapadas) y cada codigo ocupa 8 caracteres")
# ninja
# U+1F977
print("\U0001F977", " ninja")

print("En terminal, los emojis compuestos, es decir, los conformados por 2 o mas emojis a la vez, se muestran uno al lado del otro")
# family: man, woman, boy, boy
# U+1F468 U+200D U+1F469 U+200D U+1F466 U+200D U+1F466
print("\U0001F468\U0000200D\U0001F469\U0000200D\U0001F466\U0000200D\U0001F466", " Familia compuesta por un hombre una mujer y 2 hijos varones")
