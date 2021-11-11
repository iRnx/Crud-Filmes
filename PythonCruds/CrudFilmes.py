import mysql.connector


def conectar():
    """
    Função para conectar ao servidor
    """
    try:
        conn = mysql.connector.connect(
            host='localhost',
            database='todos_filmes',
            user='root',
            password='root')
        return conn
    except mysql.connector.Error as e:
        print(f'Erro ao se conectar ao MySQL: {e}')


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
    cursor.execute('SELECT * FROM filmes')
    linhas = cursor.fetchall()
    if len(linhas) > 0:
        print('=' * 20)
        for linha in linhas:
            print(f'ID: {linha[0]}')
            print(f'Nome do Filme: {linha[1]}')
            print(f'Ano do Filme: {linha[2]}')
            print(f'Distribuidor: {linha[3]}')
            print(f'Gênero do Filme: {linha[4]}')
            print(f'Classificação Indicativa: {linha[5]}')
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
    nome = str(input('Nome do Filme: ')).strip().title()
    ano = int(input('Ano do Filme: '))
    id_distribuidor = int(input('Filme Distribuído por: '))
    id_genero = int(input('Genero do filme: '))
    id_classificacao = int(input('Classificação indicativa: '))
    injetar = f"""INSERT INTO filmes (nome, ano, id_distribuidor, id_genero, id_classificacao) VALUES
              ('{nome}', {ano}, {id_distribuidor}, {id_genero}, {id_classificacao})"""
    cursor.execute(injetar)
    conn.commit()

    if cursor.rowcount == 1:
        print(f'O filme {nome} foi inserido com Sucesso!')
    else:
        print('\033[31mProblema ao inserir o filme.\033[m')
    desconectar(conn)


def atualizar():
    """
    Função para atualizar um produto
    """
    conn = conectar()
    cursor = conn.cursor()
    codigo = int(input('Código do filme que deseja atualizar: '))
    nome = str(input('Novo nome do Filme: ')).strip().title()
    ano = int(input('Novo ano do Filme: '))
    id_distribuidor = int(input('ID do Distribuidor: '))
    id_genero = int(input('ID do Gênero do filme: '))
    id_classificacao = int(input('Classificação Indicativa: '))
    att = f"""UPDATE filmes
          SET nome = '{nome}', ano = {ano}, id_distribuidor = {id_distribuidor}, id_genero = {id_genero},
          id_classificacao = {id_classificacao}
          WHERE id = {codigo}"""
    cursor.execute(att)
    conn.commit()

    if cursor.rowcount == 1:
        print(f'Produto {nome} atualizado com Sucesso!')
    else:
        print('Não foi Possível atualizar o produto.')
    desconectar(conn)


def deletar():
    """
    Função para deletar um produto
    """
    conn = conectar()
    cursor = conn.cursor()
    codigo = int(input('Insira o id que deseja deletar: '))
    cursor.execute(f'DELETE FROM filmes WHERE id = {codigo}')
    conn.commit()

    if cursor.rowcount == 1:
        print('Produto deletado com Sucesso!!')
    else:
        print(f'Erro ao excluir o produto com id={codigo}')
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
        print('5 - Sair do Programa.')
        opcao = int(input('Digite um número: '))
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
    