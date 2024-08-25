arquivo1 = 'opr1.txt'

def proce_opr(arquivo1):     # leitura do arquivo e processar as operações
    file = open(arquivo1, 'r')
    linhas = file.readlines()
    file.close()  # fecha o arquivo depois da leitura

    num_opr = int(linhas[0].strip())
    index = 1
    resultados = []

    for _ in range(num_opr):
        opr = linhas[index].strip()
        conjunto1 = set(linhas[index + 1].strip().split(', '))
        conjunto2 = set(linhas[index + 2].strip().split(', '))
        index += 3

        if opr == 'U':
            result = conjunto1.union(conjunto2)
            descricao = "União"
        elif opr == 'I':
            result = conjunto1.intersection(conjunto2)
            descricao = "Interseção"
        elif opr == 'D':
            result = conjunto1.difference(conjunto2)
            descricao = "Diferença"
        elif opr == 'C':
            result = {(x, y) for x in conjunto1 for y in conjunto2}
            descricao = "Produto Cartesiano"
        else:
            continue  # ignora opr inválidas

        result_mudado = ', '.join(result) if opr != 'C' else ', '.join([f"({x}, {y})" for x, y in result])
        resultados.append(f"{descricao}: conjunto 1 {{{', '.join(conjunto1)}}}, conjunto 2 {{{', '.join(conjunto2)}}}. Resultado: {{{result_mudado}}}")

    return resultados

def main():         # executa o programa
    arq_entrada = 'opr1.txt'
    resultados = proce_opr(arq_entrada)

    # resultados finais
    for resultado in resultados:
        print(resultado)

    # arquivo para escrita
    file = open('resultados.txt', 'w')
    for resultado in resultados:
        file.write(resultado + '\n')
    file.close()  # fecha o arquivo após a escrita

if __name__ == '__main__':
    main()