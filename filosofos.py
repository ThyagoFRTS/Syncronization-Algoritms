# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 07:42:05 2019

@author: hazut
"""
import time
from random import randint

class fork:
    def __init__(self):#inicia um garfo
        self.avaliable = True
    def lock(self):#bloqueia o garfo
        self.avaliable = False
    def unlock(self):#desbloqueia o garfo
        self.avaliable = True
    def is_avaliable(self):#verifica se o garfo está disponível
        return self.avaliable
    
class table:
    def __init__(self,n):#cria uma lista de garfos
        self.forks = [fork()]*n
        
class philosopher:
    def eating(self,list_forks,philosophers_id):#comer
        left=philosophers_id#garfo da direita é igual a posiçao
        right=(philosophers_id+1)%len(list_forks)#garfo da direita é igual a posiçao mais 1
        
        if list_forks[left].is_avaliable() and list_forks[right].is_avaliable():#se 2 garfos disponíveis
            list_forks[left].lock()#bloqueia
            list_forks[right].lock()#bloqueia
            time_exec=randint(1,2)#tempo aleatorio
            print("philosoph {0} eating for {1} seconds".format(philosophers_id,time_exec))
            time.sleep(time_exec)#comendo pelo tempo aleatorio
            list_forks[left].unlock()#desbloqueia
            list_forks[right].unlock()#desbloqueia
        else:
            print('Dont eat')#não pode comer
        
            
        
        
    def thinking(self,philosophers_id):#pensar
        time_exec=randint(1,4)#tempo aleatorio
        print("philosoph {0} thinking for {1} seconds".format(philosophers_id,time_exec))
        time.sleep(time_exec)#dormindo pelo tempo aleatorio
    def exist(self,list_forks,philosophers_id):#se a programação fosse concorrente
        while True:
            self.thinking(philosophers_id)
            #print("eating for {0} seconds".format(time.sleep(randint(1,4))))
            self.eating(list_forks,philosophers_id)
            

tab = table(5)#cingo garfos na mesa      
filosoph = [philosopher()]*5#5 filosofos
for i in range(0,len(filosoph)):
    filosoph[i].eating(tab.forks,i)#come
    filosoph[i].thinking(i)#pensa
