# -*- coding: utf-8 -*-
"""projeto media

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1m9GuUMK6iTqBNdFiBuOgH_7jxutR64v6
"""

print('     CALCULADOR DE MEDIAS')
print("===============================")
nota1 = float(input('Digite 1ª nota: '))
nota2 = float(input('Digite 2ª nota: '))
nota3 = float(input('Digite 3ª nota: '))
media = (nota1+nota2+nota3)/3
print("===============================")
print(f"A media do aluno foi: {media:.1f}")
if(media>=7):
    print("Resultado: Aprovado")
elif(media>=4):
    print("Resultado: Recuperação")
else:
    print("Resultado: Reprovado")