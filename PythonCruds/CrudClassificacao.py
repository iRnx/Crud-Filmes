import mysql.connector


def conectar():
    """
    Função para conectar ao servidor
    """
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='todos_filmes')
        return conn
    except mysql.connector.Error as e:
        print(f'Erro ao se Conectar ao Servidor MySQL {e}')


def desconectar(conn):
    """
    Função para desconectar do servidor.
    """
    if conn:
        conn.close()


def listar():
    """
    Função para listar os produtos
    """
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM classificacao')
    linhas = cursor.fetchall()
    if len(linhas) > 0:
        print('=' * 20)
        for linha in linhas:
            print(f'ID: {linha[0]}')
            print(f'Idade: {linha[1]}')
            print('=' * 20)
    else:
        print('Não existe filmes cadastrados')
    desconectar(conn)


def inserir():
    """
    Função para inserir um produto
    """
    conn = conectar()
    cursor = conn.cursor()
    idade = str(input('Digite a Classificação Indicativa do Filme: ')).strip().title()
    cursor.execute(f'INSERT INTO classificacao (idade) VALUES ("{idade}")')
    conn.commit()
    if cursor.rowcount == 1:
        print(f'Classificação Indicativa Inserida com sucesso: {idade}!')
    else:
        print('Erro ao inserir Classificação Indicativa!!!')
    desconectar(conn)


def atualizar():
    """
    Função para atualizar um produto
    """
    conn = conectar()
    cursor = conn.cursor()
    codigo = int(input('Codigo da Classificação Indicativa: '))
    idade = int(input('Nova Classificação indicativa: '))
    cursor.execute(f'UPDATE classificacao SET idade = {idade} WHERE id = {codigo}')
    conn.commit()

    if cursor.rowcount == 1:
        print(f'Classificação Indicativa Atualizada com sucesso!')
    else:
        print('Erro ao Atualizar Classificação Indicativa')
    desconectar(conn)


def deletar():
    """
    Função para deletar um produto
    """
    conn = conectar()
    cursor = conn.cursor()
    codigo = int(input('Insira o código da classificação que queira Deletar: '))
    cursor.execute(f'DELETE FROM classificacao WHERE id = {codigo}')
    conn.commit()
    if cursor.rowcount == 1:
        print(f'Classificação Indicativa Deletada com Sucesso!!')
    else:
        print(f'Erro ao Deletar Classificação Indicativa com Id = {codigo}')
    desconectar(conn)


def menu():
    """
    Função para gerar o menu inicial
    """
    while True:
        print('=========Gerenciamento de Produtos==============')
        print('Selecione uma opção: ')
        print('1 - Listar produtos.')
        print('2 - Inserir produtos.')
        print('3 - Atualizar produto.')
        print('4 - Deletar produto.')
        print('5 - Sair do Programa')
        opcao = int(input('Insira um número: '))
        if opcao in [1, 2, 3, 4, 5]:
            if opcao == 1:
                listar()
            elif opcao == 2:
                inserir()
            elif opcao == 3:
                atualizar()
            elif opcao == 4:
                deletar()
            elif opcao == 5:
                break
            else:
                print('Opção inválida')
        else:
            print('Opção inválida')


if __name__ == '__main__':
    menu()
