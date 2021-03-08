kelime1 = input("")
kelime2 = input("")
temp = kelime1[0:2]
kelime1 = kelime1.replace(kelime1[0:2], kelime2[0:2])
kelime2 = kelime2.replace(kelime2[0:2], temp)
print(kelime1, kelime2)
