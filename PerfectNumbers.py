sayi=int(input('Bir sayi giriniz!'))
toplam=0
for i in range(1,sayi):
    if sayi % i==0:
       toplam+=i

if toplam==sayi:
   print('mükemmel')
else :
  print("mükemmel değil")