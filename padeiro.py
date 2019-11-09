# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 07:35:16 2019

@author: hazut (hazuto sou eu)
"""

import time
from random import randint

def run_time_exec(time_exec, process):#função de simulação da região crítica
    print("process {0} critical stage.".format(process))
    time.sleep(time_exec/3)
    print("process {0} critical stage..".format(process))
    time.sleep(time_exec/3)
    print("process {0} critical stage...".format(process))
    time.sleep(time_exec/3)


priority_stack = [0,0,0,0,0,0]#fila de processos
current_process = 0 #processo inical

len_stack = len(priority_stack)#tamanho da fila
for process in range(0,len_stack):#for para definir os pesos (menor peso significa ser o próximo a ser atendido)
   priority_stack[process]=randint(0,100)


while len(priority_stack):  #enquanto houver processos na fila  
    print("start process") #começa
    print(priority_stack) # mostra a fila de prioridade atual
    print('process current {0}'.format(priority_stack.index(min(priority_stack))))#mostra o processo a ser executado(menor peso)
    run_time_exec(3,priority_stack.index(min(priority_stack)))#chamada da função de execução crítica
    priority_stack.remove(min(priority_stack))#remove o processo após sua execução 
    
    control = str(input("Add a new process?\ny/n\n"))#adicionar novos processos
    if control =="y":
        n=int(input("num process?\n"))
        for process in range(n):
            priority_stack.append(randint(0,100))#n processos adicionados
        
    