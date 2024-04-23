import os

restaurantes = [{'nome':'restaurante NAM','categoria':'Alimento','ativo':False},
                {'nome':'Santa','categoria':'carne','ativo':True},
                {'nome':'CWB','categoria':'Sushi','ativo':False}
                ]
def exibir_nome_do_programa():
    '''Exibe o nome do restaurante na tela
    '''
    print(""" NAM = 
    """)
def exibir_opcoes():
    '''Mostra as opções que podem ser escolhidas para cadastrar o restaurante
    '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair')

def finaliza_app():
    '''Serve para finalizar o cadastro
    '''
    exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal():
    '''Esta função serve para voltar ao menu do site
    Input:
    - Tecla "Enter" para voltar

    Output:
    -Volta ao menu principal
    '''
    input('\n Digite a tecla "Enter" para voltar ao menu principal')    
    main()

def opcao_invalida():
    '''Se algo estiver errado mostrará o texto na tela
    '''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
     '''Deixa o nome mais bonito
     '''
     os.system('clear')
     linha = '=' * (len(texto))
     print(linha)
     print(texto)
     print(linha)
     print()

def cadastrar_novo_restaurante():
   '''Essa função é responsável por cadastrar um novo restaurante
   Inputs:
   - Nome do restaurante
   - Categoria

   Output:
   - Adiciona um novo restaurante a lista de restaurantes
   '''
   exibir_subtitulo('Cadastro do novo restaurante: ')
   nome_do_restaurante  = input('Digite o nome do restaurante: ')
   categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
   dado_do_restaurante ={'nome':nome_do_restaurante,'categoria':categoria,'ativo':False}
   restaurantes.append(dado_do_restaurante)
   print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
   voltar_ao_menu_principal()

def listar_restaurante():
    '''Esta função é responsável por mostrar a lista e categoria de restaurantes cadastrados
    '''
    exibir_subtitulo('Listando os restaurantes: ')

    print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
   '''Esta função anterna o estado do restaurante entre ativado e desativado
   Input:
   - Nome do restaurante que deseja alterar o estado

   Output: Alterna entre ativado e desativado
   '''
   exibir_subtitulo('Alternando estado do restaurante')
   nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
   restaurante_encontrado = False

   for restaurante in restaurantes:
      if nome_restaurante == restaurante['nome']:
         restaurante_encontrado = True
         restaurante['ativo'] = not restaurante['nome']
         mensagem = f'O restaurante {nome_restaurante} foi ativo com sucesso' if restaurante ['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
         print(mensagem)

   if not restaurante_encontrado:
      print('O restaurante não foi encontrado')
   voltar_ao_menu_principal()

def escolher_opcao():
 '''Serve para escolher qual opção você quer
 '''
 try:
     opcao_escolhida = int(input('Escolha uma opção: '))

     if opcao_escolhida == 1:
         cadastrar_novo_restaurante()
     elif opcao_escolhida == 2:
         listar_restaurante()
     elif opcao_escolhida == 3:
         alternar_estado_restaurante()
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