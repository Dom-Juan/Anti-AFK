# This Python file uses the following encoding: utf-8
import time       # Lib do python.
import datetime   # Lib do python.
import sys        # Lib que importa execução do sistema.

import pyautogui  # Lib instalada de uso automatico de interface.

# Função principal.
def main():
  # pegando os segundos
  seconds = int(input("Digite quando tempo você acha q vai demorar para voltar: "))
  if(not isinstance(seconds, int)): # Verifica se não foi passado string.
    print("O digitado não é um número inteiro")
    sys.exit(1)
  input("Aperte qualquer tecla para iniciar!. . .")
  # inicio do timer.
  start_afk = time.time()
  # hora atual para comparação.
  t = datetime.datetime.now()
  print("Hora de inicio:", t)
  # Enquanto o tempo atual for menor que o tempo de inicio definido, faça os comandos.
  while(time.time() < start_afk + seconds):
    # Comandos no jogo para evitar afk, time sleep para evitar forçar a CPU.
    pyautogui.press('space')
    time.sleep(3)
    pyautogui.press('left')
    pyautogui.press('right')
    time.sleep(3)
  # pegando o tempo final para comapração
  t = datetime.datetime.now()
  print("Fim do programa em:", t)
  sys.exit(0)

# Iniciando o programa.
if __name__ == "__main__":
    main()