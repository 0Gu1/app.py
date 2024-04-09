import os

restaurantes = ['Pizza','VSFD'] #Lista de nomes de restaurantes

def exibir_nome_do_programa():
    print(""" VSFD = Vacas Saborosas & Farinhas Douradas = 
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



opcao_escolhida = int(input('Escolha uma opção: '))
#print('Você escolheu a opção', opcao_escolhida)
#print(f'Você escolheu a opção {opcao_escolhida}')

def exibir_subtitulo(texto):
    os.system('clear') #os.system('clear')
    print(texto)
    print()

def escolher_opcao():

    if opcao_escolhida == 1:
        print('Cadastrar restaurante')
    elif opcao_escolhida == 2:
        print('Listar restaurantes')
    elif opcao_escolhida == 3:
        print('Ativar restaurantes')
    else:
        finaliza_app()

def main():
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ =='__main__':
    main()