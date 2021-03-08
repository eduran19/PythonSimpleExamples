kelime=input('')
firstLetter=kelime[0]
result=firstLetter

for x in range(1,len(kelime)):
  if kelime[x]==firstLetter:
    result=result+"*"
  else:
    result=result+kelime[x]

print(result)