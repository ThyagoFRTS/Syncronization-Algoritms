# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 09:35:16 2019

@author: hazut (hazuto sou eu)
"""
import time
#função de simulação da região crítica
def run_time_exec(time_exec, process):
    print("process {0} critical stage.".format(process))
    time.sleep(time_exec/3)
    print("process {0} critical stage..".format(process))
    time.sleep(time_exec/3)
    print("process {0} critical stage...".format(process))
    time.sleep(time_exec/3)

priority_stack = [0,0,0,0] #fila de processos
current_process = 0 #processo inical
len_stack = len(priority_stack)#tamanho da fila


while current_process<len_stack:#enquanto não for o último
    print('process current {0}'.format(current_process))
    priority_stack[current_process]=1#processo recebe 1 se estiver executando
    print("start process")#inicio do processo
    print("current stack {0}".format(priority_stack))#mostra a atual fila de processos
    
    for i in range(0,len(priority_stack)): #for para zerar os outros processos
        priority_stack[i] = 0
        
    run_time_exec(3,current_process)#chamada da função de simulação de região crítica
    
    control = str(input("Add a new process?\ny/n\n"))#adicionar novos processos
    if control =="y":
        n=int(input("num process?\n"))
        add = [0]*n #n processos adicionados
        priority_stack = priority_stack + add #concatenação de listas
        len_stack = len_stack + n #atualizando a tamanho
    
    current_process=current_process+1#vai para o proximo processo

    
     