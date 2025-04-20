import random

class AutomatoLabirinto:
    def __init__(self, labirinto, inicio, fim):
        self.labirinto = labirinto
        self.inicio = inicio
        self.fim = fim
        self.estado_atual = inicio
        self.linhas = len(labirinto)
        self.colunas = len(labirinto[0])

    def mover(self, direcao):
        x, y = self.estado_atual
        if direcao == 'cima':
            novo_estado = (x - 1, y)
        elif direcao == 'baixo':
            novo_estado = (x + 1, y)
        elif direcao == 'esquerda':
            novo_estado = (x, y - 1)
        elif direcao == 'direita':
            novo_estado = (x, y + 1)
        else:
            print("Direção inválida. Use: cima, baixo, esquerda ou direita.")
            return False

        if self.estado_valido(novo_estado):
            self.estado_atual = novo_estado
            return True
        else:
            print("Não é possível mover para essa direção. É uma parede ou está fora do labirinto.")
            return False

    def estado_valido(self, estado):
        x, y = estado
        return 0 <= x < self.linhas and 0 <= y < self.colunas and self.labirinto[x][y] != '#'

    def estado_final(self):
        return self.estado_atual == self.fim

    def exibir_labirinto(self):
        for i in range(self.linhas):
            linha_exibida = ""
            for j in range(self.colunas):
                if (i, j) == self.estado_atual:
                    linha_exibida += 'P '
                elif (i, j) == self.inicio:
                    linha_exibida += 'S '
                elif (i, j) == self.fim:
                    linha_exibida += 'E '
                else:
                    linha_exibida += self.labirinto[i][j] + ' '
            print(linha_exibida)
        print()


def gerar_labirinto_aleatorio(tamanho):
    # Inicializa tudo como parede
    labirinto = [['#' for _ in range(tamanho)] for _ in range(tamanho)]

    # Define ponto de início
    inicio = (0, 0)
    labirinto[inicio[0]][inicio[1]] = '.'

    # Função recursiva para montar o labirinto
    def dfs(x, y):
        direcoes = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(direcoes)

        for dx, dy in direcoes:
            nx, ny = x + 2 * dx, y + 2 * dy
            if 0 <= nx < tamanho and 0 <= ny < tamanho and labirinto[nx][ny] == '#':
                labirinto[x + dx][y + dy] = '.'
                labirinto[nx][ny] = '.'
                dfs(nx, ny)

    dfs(0, 0)

    # Define saída no canto inferior direito
    fim = (tamanho - 1, tamanho - 1)
    labirinto[fim[0]][fim[1]] = '.'

    return labirinto, inicio, fim


def main():
    tamanho = 5
    labirinto, inicio, fim = gerar_labirinto_aleatorio(tamanho)
    automato = AutomatoLabirinto(labirinto, inicio, fim)

    print("Bem-vindo ao Jogo do Labirinto!")
    print("Movimente-se usando: cima, baixo, esquerda, direita. Chegue ao 'E' para vencer.")
    print("Paredes são marcadas com '#'. Você é 'P', início é 'S' e a saída é 'E'.\n")

    while not automato.estado_final():
        automato.exibir_labirinto()
        direcao = input("Digite sua direção: ").strip().lower()
        automato.mover(direcao)

    automato.exibir_labirinto()
    print("🎉 Parabéns! Você encontrou a saída!")


if __name__ == "__main__":
    main()
