import tkinter as tk
import random

TAMANHO = 5
TAMANHO_CELULA = 60

class JogoLabirinto:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Jogo do Labirinto - Versão Interface")

        self.labirinto, self.inicio, self.fim = self.gerar_labirinto_aleatorio(TAMANHO)
        self.estado_atual = self.inicio

        self.canvas = tk.Canvas(self.raiz, width=TAMANHO * TAMANHO_CELULA, height=TAMANHO * TAMANHO_CELULA)
        self.canvas.pack()

        self.botao_frame = tk.Frame(self.raiz)
        self.botao_frame.pack()

        self.criar_botoes()
        self.desenhar_labirinto()

    def criar_botoes(self):
        tk.Button(self.botao_frame, text="↑", command=lambda: self.mover("cima")).grid(row=0, column=1)
        tk.Button(self.botao_frame, text="←", command=lambda: self.mover("esquerda")).grid(row=1, column=0)
        tk.Button(self.botao_frame, text="→", command=lambda: self.mover("direita")).grid(row=1, column=2)
        tk.Button(self.botao_frame, text="↓", command=lambda: self.mover("baixo")).grid(row=2, column=1)

    def mover(self, direcao):
        x, y = self.estado_atual
        if direcao == "cima":
            novo = (x - 1, y)
        elif direcao == "baixo":
            novo = (x + 1, y)
        elif direcao == "esquerda":
            novo = (x, y - 1)
        elif direcao == "direita":
            novo = (x, y + 1)
        else:
            return

        if self.estado_valido(novo):
            self.estado_atual = novo
            self.desenhar_labirinto()
            if self.estado_atual == self.fim:
                self.canvas.create_text((TAMANHO * TAMANHO_CELULA) // 2, (TAMANHO * TAMANHO_CELULA) // 2,
                                        text="🎉 Venceu!", font=("Helvetica", 24), fill="green")

    def estado_valido(self, estado):
        x, y = estado
        return 0 <= x < TAMANHO and 0 <= y < TAMANHO and self.labirinto[x][y] != '#'

    def desenhar_labirinto(self):
        self.canvas.delete("all")
        for i in range(TAMANHO):
            for j in range(TAMANHO):
                x1 = j * TAMANHO_CELULA
                y1 = i * TAMANHO_CELULA
                x2 = x1 + TAMANHO_CELULA
                y2 = y1 + TAMANHO_CELULA

                cor = "white"
                if self.labirinto[i][j] == "#":
                    cor = "black"
                elif (i, j) == self.inicio:
                    cor = "blue"
                elif (i, j) == self.fim:
                    cor = "red"
                if (i, j) == self.estado_atual:
                    cor = "green"

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=cor, outline="gray")

    def gerar_labirinto_aleatorio(self, tamanho):
        labirinto = [['#' for _ in range(tamanho)] for _ in range(tamanho)]
        inicio = (0, 0)
        labirinto[0][0] = '.'

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
        fim = (tamanho - 1, tamanho - 1)
        labirinto[fim[0]][fim[1]] = '.'
        return labirinto, inicio, fim


if __name__ == "__main__":
    raiz = tk.Tk()
    app = JogoLabirinto(raiz)
    raiz.mainloop()
