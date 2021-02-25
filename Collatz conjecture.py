sayi= int(input('bir sayi girin'))
sayilar=[]
while(1==1):
  if(sayi==1):
    sayilar.append(sayi);
    break;

  if(sayi%2==0):
     sayi=sayi/2;
     sayilar.append(sayi)

  else:
    sayi=3*sayi+1;
    sayilar.append(sayi);

print(len(sayilar)-1)