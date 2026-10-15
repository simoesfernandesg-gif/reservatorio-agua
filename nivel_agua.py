import os # Importando a bliblioteca para limpar o terminal
os.system ("cls" if os.name == "nt" else "clear")

from colorama import Fore, Style, init, Back

init (autoreset = True) # Inicializando o COLORAMA para Windows

# Função para definir a cor e a mensagem conforme o nível do reservatório.
def exibir_cor_nivel (nivel):
    if nivel == "Nível 1":
        return Fore.RED + "Muito baixo (crítico)"
    elif nivel == "Nível 2":
        return Fore.YELLOW + "Baixo"
    elif nivel == "Nível 3":
        return Fore.GREEN + "Médio"
    elif nivel == "Nível 4":
        return Fore.CYAN + "Alto"
    elif nivel == "Nível 5":
        return Fore.BLUE + "Muito alto (alerta)"
    else:
        return "Nível desconhecido"

# Função principal para gerenciar a lista.
def exibir_nivel():
        # Lista com a descrição dos níveis do reservatório
        nivel_reservatorio = ["Nível 1", "Nível 2", "Nível 3", "Nível 4", "Nível 5"]

        # Exibe o cabeçalho formatado com a biblioteca COLORAMA
        print( Back.WHITE + Fore.BLACK + "*** Controle de Níveis de Água ***")
        print("\n")

        # FOR para percorrer cada nível da lista, buscar a cor e a mensagem de acordo com cada nível.
        for nivel in nivel_reservatorio:
            mensagem = exibir_cor_nivel (nivel)
            print(f"{nivel}: {mensagem}")
        print("\n")

# Chamada da função principal para executar o programa
exibir_nivel()  
 

