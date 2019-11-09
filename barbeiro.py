# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 23:06:09 2019

@author: hazut (hazuto sou eu)
"""
import time
import numpy as np
#considerações: a caderira na posição 0 é a cadeira de corte de cabelo

def verify_chairs_avaliables(chairs,n_chairs,clients):#função para para adicionar clientes nas cadeiras
    if clients+len(chairs[chairs==1])>n_chairs:#se houver mais clientes que cadeiras
        print('{0} clients go out'.format(clients+len(chairs[chairs==1])-n_chairs))#mostrar o número de clientes que saíram da loja
        chairs[len(chairs[chairs==1]):n_chairs]=1#se há mais clientes que cadeiras, logo todas as cadeiras serão ocupadas
    else:#se houver mais caddeiras que clientes
        chairs[len(chairs[chairs==1]):clients+len(chairs[chairs==1])]=1#ocupar as cadeiras

class cutter:
    def __init__(self,name,sleeping):#construtor
        self.id = name
        self.sleeping = sleeping
    def awake(self):#acordar
        self.sleeping=False
        print('barber is awake')
    def sleep(self):#dormir
        self.sleeping=True
        print('barber is sleeping with sirens')
    def cut(self,time_exec, process):#função de simulação da região crítica
        print("cutting {0} critical stage.".format(process))
        time.sleep(time_exec/3)
        print("cutting {0} critical stage..".format(process))
        time.sleep(time_exec/3)
        print("cutting {0} critical stage...".format(process))
        time.sleep(time_exec/3)
        print("cutting {0}".format(process))
    
n_chairs = int(input('Enter with a integer number of chairs '))#numero de cadeiras    
chairs = np.array([0]*n_chairs)#conversão para vetor da numpy (porque vai facilitar)
barber = cutter("Thyago",True)#instancia o barbeiro
n_clients = int(input('Enter with a integer number of start clients '))#numero de clientes iniciais
verify_chairs_avaliables(chairs,n_chairs,n_clients)#chama a função de ocupação
barber.awake()#tem clientes, logo o barbeiro acorda

#considerações: a caderira na posição 0 é a cadeira de corte de cabelo
control = True #controle do laço
while control:#enquanto houver clientes na fila
    if len(chairs[chairs==1])>0:
        barber.cut(3,len(chairs[chairs==1]))#corta quem estiver na cadeira de corte
        chairs[len(chairs[chairs==1])-1]=0#zera a último 1, afinal um cliente acabou de sair
        print(chairs)#cadeiras atuais ocupadas
        
        new_clients=int(input("How many clients arrived? "))#adicionar novas clientes
        verify_chairs_avaliables(chairs,n_chairs,new_clients)#função de ocupação
        print(chairs)#cadeiras atuais ocupadas
    else:
        barber.sleep()#sem clientes, logo o barbeiro dorme
        switcher=str( input('exit? y/n'))#verificar se desejamos parar
        if switcher=='y':
            control=False
        ew_clients=int(input("How many clients arrived? "))#adicionar novas clientes
        verify_chairs_avaliables(chairs,n_chairs,new_clients)#função de ocupação
        print(chairs)#cadeiras atuais ocupadas

    

