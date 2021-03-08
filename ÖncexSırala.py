kelimeler = []
xlebaslayanlar = []
yazi = "1"
while yazi != "":
    yazi = input("Bir yazı giriniz:")
    if yazi.startswith("x"):
        xlebaslayanlar.append(yazi)
    else:
        kelimeler.append(yazi)

xlebaslayanlar.sort()
kelimeler.sort()
xlebaslayanlar.extend(kelimeler)
for sırala in xlebaslayanlar:
    print(sırala)
