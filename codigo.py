# -*- coding: utf-8 -*-
def registrar_mensagem(tipo, mensagem):
    arquivo = f"{tipo}.txt"
    with open(arquivo, "a") as arquivo_destino:
        arquivo_destino.write(f"{mensagem}\n")

def verificar_palavras_improprias(mensagem):
    palavras_improprias = ["caralho", "porra", "puta", "merda", "bosta", "cu", "fodase", "foder", "viado", "baitola", "cacete", "corno"]
    for palavra in palavras_improprias:
        if palavra in mensagem:
            return True
    return False

def exibir_menu():
    print("Digite o tipo de mensagem (elogio, reclamacao ou sair):")
    return input().lower()

def obter_mensagem():
    print("Digite a mensagem:")
    return input()

def main():
    while True:
        tipo = exibir_menu()
        if tipo == 'sair':
            break

        if tipo not in ['elogio', 'reclamacao']:
            print("Tente novamente.")
            continue

        mensagem = obter_mensagem()

        if verificar_palavras_improprias(mensagem):
            registrar_mensagem("palavras_improprias", mensagem)
            print("Mensagem registrada como contendo palavras impróprias.")
        elif tipo == 'reclamacao':
            registrar_mensagem("reclamacoes", mensagem)
            print("Reclamação registrada com sucesso.")
        else:
            registrar_mensagem("elogios", mensagem)
            print("Elogio registrado com sucesso.")

if __name__ == "__main__":
    main()

