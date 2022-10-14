"""
Jogo simples de matemática utilizando a biblioteca Tkinter para criar uma interface gráfica.

Opções de dificuldade:
    - Fácil: Operações com números entre 0 e 10;
    - Médio: Operações com números entre 0 e 100;
    - Difícil: Operações com números entre 0 e 1000;
    - Muito difícil: Operações com números entre 0 e 10000;
    
Operações:
    - Adição(+);
    - Subtração(-);
    - Multiplicação(x)
"""

import tkinter as tk
import tkinter.messagebox
from models.calcular import Calcular
from tkinter import *


class Principal(tk.Tk):
    
    def __init__(self):
        """Configurações da janela do jogo."""
        super().__init__()
        self.dificuldade = None
        self.pontos = 0
        self.title('Jogo de Matemática')
        self.resizable(False, False)
        self.geometry('500x400')
        self.background = PhotoImage(file='game2(1).png')
        self.bg = Label(self, image=self.background).place(relx=0.48, rely=0.5, anchor=CENTER)
        self.creditos = Label(self, text='Criador: Elisson Douglas', font='Bold')
        self.creditos.place(relx=0.5, rely=0.96, anchor=CENTER)
        # StringVar
        self.auxiliar_pontos = StringVar()
        self.auxiliar_pontos.set(self.pontos)
        
        
        #Inicio do game
        
        self.button = Button(self, text='INICIAR O JOGO', background='green', foreground='white', command=lambda: self.jogar(), padx=15, pady=15)
        self.button.place(relx=0.5, rely=0.6, anchor=CENTER)
        
        # Menu de Dificuldades
        self.opcoes = {'Fácil': 1, 'Médio': 2, 'Dificil': 3, 'Muito dificil':4}
        self.variavel = tk.StringVar(self)
        self.variavel.set('Selecione')
        self.menu_dificuldade = OptionMenu(self, self.variavel, *self.opcoes.keys(), command=self.menu_de_dificuldade).place(relx=0.5, rely=0.2, anchor=CENTER, height=25)
        self.l2 = Label(self, text='Dificuldade', background='#f6f6f6', foreground='black', font='Bold').place(relx=0.5, rely=0.140, anchor=CENTER)

    
    def menu_de_dificuldade(self, *args):
        """Ler a dificuldade escolhida e setar a pergunta."""
        selecao = self.variavel.get()
        self.dificuldade = self.opcoes[selecao]
        self.calculos = Calcular(self.dificuldade)
        

    def sair(self):
        """Terminar o jogo e mostrar a pontuação final."""
        self.variavel.set('Selecione')
        self.dificuldade = None
        terminou = Label(self, text=f'SUA PONTUAÇÃO: {self.pontos}', background='#f6f6f6', foreground='black', font=('Arial', 18))
        terminou.place(relx=0.5, rely=0.43, width=320, height=100, anchor=CENTER)
        self.pontos = 0
        self.auxiliar_pontos.set(self.pontos)
        botao1 = Button(app, text='Sair do jogo', command=lambda: app.destroy(), background='red', foreground='white')
        botao1.pack(side=BOTTOM)
        botao2 = Button(app, text='Jogar Novamente', command=lambda: [[self.jogar(),terminou.destroy(),botao2.pack_forget(), botao1.pack_forget()] if self.dificuldade != None else tkinter.messagebox.showwarning(title='ERRO!', message='Por favor, selecione uma dificuldade antes de jogar.')]
                        , background='green', foreground='white')
        botao2.pack(side=BOTTOM)


    def checar(self, en):
        """Checar se a resposta está correta
            Se estiver correta o jogador ganhar +1 ponto.
            Se estiver incorreta mostrará o resultado correto na tela e o usuário não ganha nenhum ponto.
        """
        def proxima():   
            self.calculos = Calcular(self.dificuldade)
            self.auxiliar.set(self.calculos.mostrar_operação())
        
        if self.calculos.checar_resultado(en):
            acertou = Label(self, text=f'RESPOSTA CORRETA! +1 Ponto', background= '#f6f6f6', foreground='green')
            acertou.place(relx=0.5, rely=0.6, width=210, anchor=CENTER)
            self.pontos += 1
            self.auxiliar_pontos.set(self.pontos)
            terminar = Button(app, text='Finalizar jogo', command=lambda: [self.sair(), terminar.pack_forget(), proximaQ.pack_forget(), acertou.destroy()], pady=1)
            terminar.pack(side=BOTTOM)
            proximaQ = Button(app, text='Próxima', command=lambda: [proximaQ.pack_forget(), self.jogar(), terminar.pack_forget(), acertou.destroy()], pady=1)
            proximaQ.pack(side=BOTTOM)
        else:
            errou = Label(self, text=f'RESPOSTA ERRADA!\n{self.calculos.valor1} {self.calculos._op_simbolo} {self.calculos.valor2} = {self.calculos.resultado}', background='#f6f6f6', foreground='red')
            errou.place(relx=0.5, rely=0.6, width=150, anchor=CENTER)
            terminar = Button(app, text='Finalizar jogo', command=lambda: [self.sair(), terminar.pack_forget(), proximaQ.pack_forget(), errou.destroy()], pady=1)
            terminar.pack(side=BOTTOM)
            proximaQ = Button(app, text='Próxima', command=lambda: [proximaQ.pack_forget(), self.jogar(), terminar.pack_forget(), errou.destroy()], pady=1)
            proximaQ.pack(side=BOTTOM)
            
            
                   
    def jogar(self) -> None:
        """Tela inicial do jogo onde o jogador vai selecionar a dificuldade e clicar em INICIAR O JOGO.
            Caso não selecione nenhuma dificuldade vai aparecer uma mensagem de erro.
        """
        if isinstance(self.dificuldade, int):
            self.creditos.destroy()
            self.button.destroy()
            self.calculos = Calcular(self.dificuldade)
            self.auxiliar = tk.StringVar()
            self.auxiliar.set(self.calculos.mostrar_operação())
        
            l1 = Label(self, text='Sua resposta:', background='#f6f6f6', foreground='black', font='Bold').place(relx=0.5, rely=0.73, anchor=CENTER)
            entrada = Entry(app, background='#84daff')
            entrada.place(relx=0.5, rely=0.8, anchor=CENTER, width=50)
            
            
            self.pergunta = Label(self, textvariable=self.auxiliar, font='Arial 32', background='#f6f6f6').place(relx=0.5, rely=0.42, height=100, width=310, anchor=CENTER)
            
            # Pontos
            ver_pontos = Label(self, text=f'Pontos:', anchor=W, font='24', background='#84daff').place(x=350, y=15, width=100)
            vpontos = Label(self, textvariable=self.auxiliar_pontos, font='24', background='#84daff').place(x=415, y=15, width=20)
            
            # Botão confirmar
            confirmar_resultado = Button(self, text='Confirmar', command=lambda: [self.checar(int(entrada.get())), confirmar_resultado.pack_forget(), entrada.delete(0, 'end')], background='green', foreground='white')
            confirmar_resultado.pack(side=BOTTOM)
        else:
            tkinter.messagebox.showwarning(title='ERRO!', message='Por favor, selecione uma dificuldade antes de jogar.')
            
        

if __name__ == '__main__':
    app = Principal()
    app.mainloop()
