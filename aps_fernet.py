from cryptography.fernet import Fernet
from time import sleep
import os
loop_chave = 1
while loop_chave == 1:
    chave_mem = Fernet.generate_key()
    arquivo = open("chave.key", "wb")
    arquivo.write(chave_mem)
    arquivo.close()
    loop_chave -= 1
mensagem = 0
mensagem_criptografada = 0
mensagem_original = 0
loop_cripto = 1
while loop_cripto == 1:
    arquivo = open("chave.key", "rb")
    chave = arquivo.read()
    arquivo.close()
    print("\nCriptografia de textos\n")
    print("1. Escrever um texto\n"
          "2. Criptografar o texto escrito\n"
          "3. Descriptografar o texto\n"
          "4. Mostrar texto criptografado\n"
          "5. Mostrar texto descriptografado\n"
          "S. Sair\n")
    escolha = input("Digite sua escolha: ")
    os.system("cls")
    while escolha == "1":
        if mensagem != 0:
            print("Se você já escreveu uma mensagem anteriormente,"
                  "a mesma será reescrita.")
        mensagem = input("Digite uma mensagem ou texto. ")
        print("Texto escrito.")
        sleep(0.5)
        print("Voltando ao menu.")
        sleep(0.5)
        escolha = 0
    while escolha == "2":
        if mensagem == 0:
            print("Não há como criptografar se o texto não foi escrito.")
            sleep(0.5)
            print("Voltando ao menu.")
            sleep(0.5)
            escolha = 0
        else:
            print("Criptografando texto... ")
            mensagem_codificada = mensagem.encode()
            f = Fernet(chave)
            mensagem_criptografada = f.encrypt(mensagem_codificada)
            print("Texto criptografado.")
            print("Voltando ao menu. ")
            escolha = 0
    while escolha == "3":
        if mensagem_criptografada == 0:
            print("Não há como descriptografar se o texto não foi criptografado.")
            sleep(0.5)
            print("Voltando ao menu.")
            sleep(0.5)
            escolha = 0
        else:
            print("Descriptografando texto... ")
            sleep(0.5)
            f2 = Fernet(chave)
            mensagem_descriptografada = f2.decrypt(mensagem_criptografada)
            mensagem_criptografada = 0
            mensagem_original = mensagem_descriptografada.decode()
            print("Texto descriptografado.")
            sleep(0.5)
            print("Voltando ao menu.")
            sleep(0.5)
            mensagem_criptografada = 0
            escolha = 0
    while escolha == "4":
        if mensagem_criptografada == 0:
            print("Não há como mostrar o texto criptografado se ele não foi feito ou descriptografado. ")
            sleep(0.5)
            print("Voltando ao menu.")
            sleep(0.5)
            escolha = 0
        else:
            print("A mensagem criptografada é: {}".format(mensagem_criptografada))
            sleep(0.5)
            print("Voltando ao menu.")
            sleep(0.5)
            escolha = 0
    while escolha == "5":
        if mensagem_original == 0:
            print("Não há como mostrar o texto descriptografado se ele não foi feito.")
            sleep(0.5)
            print("Voltando ao menu.")
            sleep(0.5)
            escolha = 0
        else:
            print("A mensagem original é: {}".format(mensagem_original))
            sleep(0.5)
            print("Voltando ao menu.")
            sleep(0.5)
            escolha = 0
    while escolha == "S" or escolha == "s":
        print("Saindo... ")
        sleep(0.5)
        escolha = 0
        loop_cripto = 0
