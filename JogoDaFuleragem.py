# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 15:03:50 2016

@author: Artur
"""

import random
import time

def regrasDoJogo():
    print("\nNão se sabe muito bem como esse jogo surgiu, mas ele")
    print("foi trazido para o ocidente pelo bardo e mercador Tenório.")
    print("Esse jogo fez muito sucesso no 1º Ano do Ensino Médio")
    print("de um colégio em Aracaju, capital de Sergipe, pois servia")
    print("como atrativo para os alunos sobreviverem às longas")
    print("e tediosas aulas. Agora ele foi transformado em um jogo")
    print("de computador para ser imortalizado em forma digital.")
    
    print("\nAs regras do jogo são bem simples. Você só precisa escrever")
    print("o que o jogo pede e ele criará frases aleatórias baseadas no")
    print("que você escreveu. E sim, nós nos divertíamos muito com isso.")
    
    print("\nPara a primeira experiência, é recomendado jogar com 5 itens.")

def jogoDaFuleragem(num, tema):
    
    while True:
        listTema = []
        count = 1
    
        print("\nDigite", num, tema +": \n")
    
        while count <= num:
            item = input("- ")
            print(count, "-", item)
            listTema.append(item)
            count += 1
        
        print("\nSua lista é:\n", listTema)
        confirm = input("Deseja confirmar essa lista? S/N ")
        if confirm.lower() == "s":
            print("Lista confirmada!\n")
            break
        else:
            print("Vamos refazer a lista, então!")
    return listTema
    
    
def montadorDeFrases(lista1, lista2, lista3, lista4, lista5):
    
    frases = 0    
    while frases < num:
        item1 = random.choice(lista1)
        lista1.remove(item1)
        
        item2 = random.choice(lista2)
        lista2.remove(item2)
        
        item3 = random.choice(lista3)
        lista3.remove(item3)
        
        item4 = random.choice(lista4)
        lista4.remove(item4)
        
        item5 = random.choice(lista5)
        lista5.remove(item5)
        
        print("\n", item1, item2, item3, "no/na", item4, "de", item5)
        
        frases += 1
    
while True:
    regrasDoJogo()
    num = int(input("\nCom quantos items você pretende jogar? \n"))
    lista1 = jogoDaFuleragem(num, "pessoas que você gosta")
    lista2 = jogoDaFuleragem(num, "verbos de movimento na 3ª pessoa")
    lista3 = jogoDaFuleragem(num, "objetos")
    lista4 = jogoDaFuleragem(num, "partes do corpo humano")
    lista5 = jogoDaFuleragem(num, "pessoas que você não gosta")
    montadorDeFrases(lista1, lista2, lista3, lista4, lista5)
    
    print("\nEspero que você tenha se divertido!")
    replay = input("Você quer jogar de novo? S/N ")
    
    if replay.lower() == "s":
        print("Okay, então vamos lá! :D/n/n")
    else:
        print("Tudo bem, nos vemos na próxima! Obrigado por ter jogado! :D")
        time.sleep(4)
        break