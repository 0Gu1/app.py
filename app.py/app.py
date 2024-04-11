import os

restaurantes = ['Pizza','NAM'] #Lista de nomes de restaurantes

def exibir_nome_do_programa():
    print(""" NAM = 
    """)
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair')

def finaliza_app():
    exibir_subtitulo('Finalizar Bagulho')

def voltar_ao_menu_principal():
    input('\n Digite a tecla "Enter" para voltar ao menu principal')    
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('clear')
    print(texto)
    print()

def exibir_subtitulo(texto):
    os.system('clear')
    print(texto)
    print()

def cadastrar_novo_restaurante():
   exibir_subtitulo('Cadastro do novorestaurante: ')
   nome_do_restaurante  = input('Digite o nome do restaurante')
   restaurantes.append(nome_do_restaurante)
   print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
   voltar_ao_menu_principal()  

def listar_restaurante():
    exibir_subtitulo('Listando os restaurantes: ')

    for restaurante in restaurantes:
        print(f'*{restaurante}')

    voltar_ao_menu_principal()


def escolher_opcao():
 try:
    opcao_escolhida = int(input('Escolha uma opção: '))

    if opcao_escolhida == 1:
        cadastrar_novo_restaurante()
    elif opcao_escolhida == 2:
        listar_restaurante()
    elif opcao_escolhida == 3:
        print('Ativar restaurantes')
    elif opcao_escolhida ==4:
        finaliza_app()
    else:
        opcao_invalida()

 except:
    opcao_invalida()

def main():
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ =='__main__':
    main()