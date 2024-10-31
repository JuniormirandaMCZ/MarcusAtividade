def ler_arquivo_e_ordenar(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read().strip()
        numeros = list(map(int, conteudo.split()))
        numeros_ordenados = sorted(numeros)
        return ' '.join(map(str, numeros_ordenados))
arquivo_nome = 'extra.txt'
resultado = ler_arquivo_e_ordenar(arquivo_nome)
print(f'Números ordenados: {resultado}')
