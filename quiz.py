print('Qual é o maior planeta do nosso sistema solar?:')
print('1 : Jupter')
print('2 : Venus')
print('3 : Terra')
print('4 : Saturno')
print('5 : Urano')
print('6 : Netuno')
print('7 : Plutão')
print('8 : Mercurio')
print('9 : Pandora')
print('10 : Tatooine')
print('11 : Makemake')
print('12 : Marte')
planet = int(input('digite um numero correspondente:'))
ct = 0
while planet >= 2:
   if planet >= 2:
    print('Oh, não! Parece que você acertou o botão de autodestruição do foguete de conhecimento! 🚀💥 Tente novamente e não se preocupe, você não explodirá desta vez! 😄')
    planet = int(input('digite novamente um numero correspondente:'))
    if planet == 9:
      print("Por acaso você acha que estamos no Filme Avatar? NÃO! Tente novamente")
      planet = int(input('digite novamente um numero correspondente:'))
      if planet == 10:
        print("Esse ai é do Star Was 😄, Tente novamente")
        planet = int(input('digite novamente um numero correspondente:'))
        if planet == 11:
          print("Esse NAO EXISTE HAHA 😄, Tente novamente")
          planet = int(input('digite novamente um numero correspondente:'))
        
    ct = ct + 1
print ("Voce conseguiu, depois de" ,ct, " tentativa. Parabéns, você é mais esperto do que um gato espacial em um jogo de xadrez! Você acertou! 🚀😺✨" )    
    

