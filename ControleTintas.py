# ================================================================
# Gerenciamento do Estoque de Tintas da Exiba Outdoor            = 
# Criado por Alecsandro Ferreira Melo - 03/07/2022 - Vesão 1.6.0 =
# ================================================================

import tkinter as tk
import sqlite3
from tkinter import messagebox
from tkinter import IntVar
from tkinter import StringVar

#Cronstruindo a Janela Principal 
class ControlTintas:
    def __init__(self, master):
        self.master = master
        self.master.geometry("630x150+50+50")
        self.master.title("EXIBA - Controle Estoque Tintas")
        self.master.iconbitmap("img/iconefinal.ico")

        #Criando Variáveis Globais
        global C_count, M_count, Y_count, K_count, C_Porce, M_Porce, Y_Porce, K_Porce
       
        C_count = IntVar() #Variavel para receber o valor da cor Ciano
        M_count = IntVar() #Variavel para receber o valor da cor Magenta
        Y_count = IntVar() #Variavel para receber o valor da cor Yellow
        K_count = IntVar() #Variavel para receber o valor da cor Prato

        C_Porce = StringVar() #Variavel que receberá o calculo da Porcetagem da Cor Ciano
        M_Porce = StringVar() #Variavel que receberá o calculo da Porcetagem da Cor Magenta
        Y_Porce = StringVar() #Variavel que receberá o calculo da Porcetagem da Cor Amarelo
        K_Porce = StringVar() #Variavel que receberá o calculo da Porcetagem da Cor Preto        

        
        #Conecta ao Banco de Dados
        self.BancoDados()

        #Atualizar Valores dos Itens com a Função Carrega
        self.Carregar()
        self.JanelaPrincipal()

    def JanelaPrincipal(self):
        global C_count, M_count, Y_count, K_count, C_Porce, M_Porce, Y_Porce, K_Porce

        self.C_Porcetagem = StringVar()
        self.M_Porcetagem = StringVar()
        self.Y_Porcetagem = StringVar()
        self.K_Porcetagem = StringVar()

        #Convertendo e Carregando os valores das Porcetagens 
        self.C_Porcetagem.set(str(C_Porce.get()+"% "))
        self.M_Porcetagem.set(str(M_Porce.get()+"% "))
        self.Y_Porcetagem.set(str(Y_Porce.get()+"% "))
        self.K_Porcetagem.set(str(K_Porce.get()+"% "))
        
        
        #CONSTRUÇÃO -> Instanciando os Widgets
        self.C_img = tk.PhotoImage(file='img/C_ink.png')              #Icone Garrafa Ciano
        self.C_imgLBL = tk.Label(self.master, image=self.C_img)
        self.C_imgLBL.place(x=5, y=15)

        #Imagens Alternativos para Ciano
        self.C_img80 = tk.PhotoImage(file='img/C_ink80.png')
        self.C_img50 = tk.PhotoImage(file='img/C_ink50.png')
        self.C_img20 = tk.PhotoImage(file='img/C_ink20.png')

        self.M_img = tk.PhotoImage(file='img/M_ink.png')              #Icone Garrafa Magenta
        self.M_imgLBL = tk.Label(self.master, image=self.M_img)
        self.M_imgLBL.place(x=135, y=15)

        #Imagens Alternativos para Magenta
        self.M_img80 = tk.PhotoImage(file='img/M_ink80.png')
        self.M_img50 = tk.PhotoImage(file='img/M_ink50.png')
        self.M_img20 = tk.PhotoImage(file='img/M_ink20.png')        

        self.Y_img = tk.PhotoImage(file='img/Y_ink.png')              #Icone Garrafa Amarelo
        self.Y_imgLBL = tk.Label(self.master, image=self.Y_img)
        self.Y_imgLBL.place(x=265, y=15)

        #Imagens Alternativos para Amarelo
        self.Y_img80 = tk.PhotoImage(file='img/Y_ink80.png')
        self.Y_img50 = tk.PhotoImage(file='img/Y_ink50.png')
        self.Y_img20 = tk.PhotoImage(file='img/Y_ink20.png')         

        self.K_img = tk.PhotoImage(file='img/K_ink.png')              #Icone Garrafa Preto
        self.K_imgLBL = tk.Label(self.master, image=self.K_img)       
        self.K_imgLBL.place(x=392, y=15)

        #Imagens Alternativos para Preto
        self.K_img80 = tk.PhotoImage(file='img/K_ink80.png')
        self.K_img50 = tk.PhotoImage(file='img/K_ink50.png')
        self.K_img20 = tk.PhotoImage(file='img/K_ink20.png') 
                
        #Conjuto Ciano
        self.C_ent = tk.Entry(self.master, width=3, textvariable=C_count, justify='center', font=("Arial", 15)) #Display Quantidade CIANO
        self.C_ent.place(x=70, y=25)
        self.C_BtnMais = tk.Button(self.master, text="+", width=1, height=1, command=self.Aumenta_Ciano, relief='groove')
        self.C_BtnMais.place(x=70, y=55)
        self.C_BtnMenos = tk.Button(self.master, text="-", width=1, height=1, command=self.Diminue_Ciano, relief='groove')
        self.C_BtnMenos.place(x=90, y=55)
        self.C_RotEstoque = tk.Label(self.master, text="Estoque")
        self.C_RotEstoque.place(x=66, y=85)
        self.C_Porcentagem = tk.Label(self.master, textvariable=self.C_Porcetagem, font=('Arial', 10, 'bold'))
        self.C_Porcentagem.place(x=66, y=105)
        
        #Conjuto Magenta
        self.M_ent = tk.Entry(self.master, width=3, textvariable=M_count, justify='center', font=("Arial", 15)) #Display Quantidade MAGENTA
        self.M_ent.place(x=200, y=25)
        self.M_BtnMais = tk.Button(self.master, text="+", width=1, height=1, command=self.Aumenta_Magenta, relief='groove')
        self.M_BtnMais.place(x=200, y=55)
        self.M_BtnMenos = tk.Button(self.master, text="-", width=1, height=1, command=self.Diminue_Magenta, relief='groove')
        self.M_BtnMenos.place(x=220, y=55)
        self.M_RotEstoque = tk.Label(self.master, text="Estoque")
        self.M_RotEstoque.place(x=196, y=85)
        self.M_Porcentagem = tk.Label(self.master, textvariable=self.M_Porcetagem, font=('Arial', 10, 'bold'))
        self.M_Porcentagem.place(x=196, y=105)        

        #Conjuto Yellow
        self.Y_ent = tk.Entry(self.master, width=3, textvariable=Y_count, justify='center', font=("Arial", 15)) #Display Quantidade Amarelo
        self.Y_ent.place(x=330, y=25)
        self.Y_BtnMais = tk.Button(self.master, text="+", width=1, height=1, command=self.Aumenta_Yellow, relief='groove')
        self.Y_BtnMais.place(x=330, y=55)
        self.Y_BtnMenos = tk.Button(self.master, text="-", width=1, height=1, command=self.Diminue_Yellow, relief='groove')
        self.Y_BtnMenos.place(x=350, y=55)
        self.Y_RotEstoque = tk.Label(self.master, text="Estoque")
        self.Y_RotEstoque.place(x=326, y=85)
        self.Y_Porcentagem = tk.Label(self.master, textvariable=self.Y_Porcetagem, font=('Arial', 10, 'bold'))
        self.Y_Porcentagem.place(x=326, y=105)
       
        #Conjuto Preto
        self.K_ent = tk.Entry(self.master, width=3, textvariable=K_count, justify='center', font=("Arial", 15)) #Display Quantidade Preto
        self.K_ent.place(x=455, y=25)
        self.K_BtnMais = tk.Button(self.master, text="+", width=1, height=1, command=self.Aumenta_Preto, relief='groove')
        self.K_BtnMais.place(x=455, y=55)
        self.K_BtnMenos = tk.Button(self.master, text="-", width=1, height=1, command=self.Diminue_Preto, relief='groove')
        self.K_BtnMenos.place(x=475, y=55)
        self.K_RotEstoque = tk.Label(self.master, text="Estoque")
        self.K_RotEstoque.place(x=451, y=85)
        self.K_Porcentagem = tk.Label(self.master, textvariable=self.K_Porcetagem, font=('Arial', 10, 'bold'))
        self.K_Porcentagem.place(x=451, y=105)
        

        #Instanciando Os Botões Salva Atualizar               
        self.SalveBTN = tk.Button(self.master,  text="Salvar", width=12, height=3, command=self.Salvar, relief='groove')          #Botão Salvar
        self.SalveBTN.place(x=520, y=20)

        self.AtualizaBTN = tk.Button(self.master, text="Atualizar", width=12, height=2, command=lambda: [self.Carregar(), self.JanelaPrincipal()], relief='groove')   #Botão Atualizar
        self.AtualizaBTN.place(x=520, y=85)        


        #Alterando a Ordem da navegação por TAB
        self.WidgetOrder = (self.C_ent, self.M_ent, self.Y_ent,
                            self.K_ent, self.SalveBTN, self.AtualizaBTN,
                            self.C_BtnMais, self.C_BtnMenos,
                            self.M_BtnMais, self.M_BtnMenos,
                            self.Y_BtnMais, self.Y_BtnMenos,
                            self.K_BtnMais, self.K_BtnMenos
                            )


        for Widget in self.WidgetOrder:
            Widget.lift()

        #Condicionais Garrafas

        
        if float(C_Porce.get()) <= 80.00:
            self.C_imgLBL['image'] = self.C_img80

        if float(C_Porce.get()) <= 50.00:
            self.C_imgLBL['image'] = self.C_img50

        if float(C_Porce.get()) <= 20.00:
            self.C_imgLBL['image'] = self.C_img20

        if float(M_Porce.get()) <= 80.00:
            self.M_imgLBL['image'] = self.M_img80

        if float(M_Porce.get()) <= 50.00:
            self.M_imgLBL['image'] = self.M_img50

        if float(M_Porce.get()) <= 20.00:
            self.M_imgLBL['image'] = self.M_img20

        if float(Y_Porce.get()) <= 80.00:
            self.Y_imgLBL['image'] = self.Y_img80

        if float(Y_Porce.get()) <= 50.00:
            self.Y_imgLBL['image'] = self.Y_img50

        if float(Y_Porce.get()) <= 20.00:
            self.Y_imgLBL['image'] = self.Y_img20
            
        if float(K_Porce.get()) <= 80.00:
            self.K_imgLBL['image'] = self.K_img80

        if float(K_Porce.get()) <= 50.00:
            self.K_imgLBL['image'] = self.K_img50

        if float(K_Porce.get()) <= 20.00:
            self.K_imgLBL['image'] = self.K_img20            

        #Barrinha de Status + Créditos
        self.Barra = tk.Label(self.master, text="PoweredBy: Alecs Melo | versão: 1.6.0", font=('Arial', 6))
        self.Barra.place(x=480, y=130)
            

    #Funções Aumeta e Diminue os valores em cada Cor
    def Aumenta_Ciano(self):
        global C_count
        self.Cmais = C_count.get()
        C_count.set(self.Cmais + 1)
    def Diminue_Ciano(self):
        global C_count
        self.Cmenos = C_count.get()
        self.count = 1
        C_count.set(self.Cmenos - self.count)


    def Aumenta_Magenta(self):
        global M_count
        self.Mmais = M_count.get()
        M_count.set(self.Mmais + 1)
    def Diminue_Magenta(self):
        global M_count
        self.Mmenos = M_count.get()
        self.count = 1
        M_count.set(self.Mmenos - self.count)
        

    def Aumenta_Yellow(self):
        global Y_count
        self.Ymais = Y_count.get()
        Y_count.set(self.Ymais + 1)
    def Diminue_Yellow(self):
        global Y_count
        self.Ymenos = Y_count.get()
        self.count = 1
        Y_count.set(self.Ymenos - self.count)

    def Aumenta_Preto(self):
        global K_count
        self.Kmais = K_count.get()
        K_count.set(self.Kmais + 1)
    def Diminue_Preto(self):
        global K_count
        self.Kmenos = K_count.get()
        self.count = 1
        K_count.set(self.Kmenos - self.count
                    )

    #Criando ou Carregando Banco de Dados Geral
    def BancoDados(self):
        global C_count, M_count, Y_count, K_count
        try:
            self.conexao = sqlite3.connect('EstoqueTintas.db')
            self.cursor = self.conexao.cursor()
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS Tintas(
                                Ciano INT,
                                Magenta INT,
                                Yellow INT,
                                Black INT
                                )
                                """)
                          
        except:
            messagebox.showinfo("Erro", "Erro ao carregar Banco de Dados")

    #Função Salvar -> Pegas oa valores atuais e inclue no Banco de Dados
    def Salvar(self):
        global C_count, M_count, Y_count, K_count

        self.azul = C_count.get()
        self.vermelho = M_count.get()
        self.amarelo = Y_count.get()
        self.preto = K_count.get()

       
        # Conexão com o Banco de Dados        
        
        try:
            self.conexao = sqlite3.connect('EstoqueTintas.db')                   
            self.cursor = self.conexao.cursor()
            self.cursor.execute("UPDATE Tintas SET Ciano=?, Magenta=?, Yellow=?, Black=?", (self.azul, self.vermelho, self.amarelo, self.preto,))
          
        except:
            messagebox.showinfo("Erro", "Impossível Gravar Dados")

        finally:
            self.conexao.commit()
            self.conexao.close()

    #Função para Carregar e atualizar os valores dos Itens, essa função pode ser chamada em qualquer parte
    def Carregar(self):
        global C_count, M_count, Y_count, K_count, C_Porce, M_Porce, Y_Porce, K_Porce

        try:
            self.conexao = sqlite3.connect('EstoqueTintas.db')
            self.cursor = self.conexao.cursor()
            self.cursor.execute("SELECT * FROM Tintas")
            self.carrega = self.cursor.fetchall()
            for i in self.carrega:
                C_count.set(i[0])
                M_count.set(i[1])
                Y_count.set(i[2])
                K_count.set(i[3])
        except:
            messagebox.showinfo("Erro", "Erro ao carregar dados")
        finally:
            self.conexao.commit()
            self.conexao.close()


        #Calculando Porcetagem do Estoque e informando no Display   
        self.porcento = 100
        self.total = 60
        self.azul = C_count.get()
        self.vermelho = M_count.get()
        self.amarelo = Y_count.get()
        self.preto = K_count.get()        
                
        self.PorcAzul = float(self.azul * self.porcento / self.total)
        C_Porce.set(str("{:.2f}".format(self.PorcAzul)))

        self.PorcVermelho = float(self.vermelho * self.porcento / self.total)
        M_Porce.set(str("{:.2f}".format(self.PorcVermelho)))

        self.PorcAmarelo = float(self.amarelo * self.porcento / self.total)
        Y_Porce.set(str("{:.2f}".format(self.PorcAmarelo)))        

        self.PorcPreto = float(self.preto * self.porcento / self.total)
        K_Porce.set(str("{:.2f}".format(self.PorcPreto)))
          
        

    #Função para Conectar com o Banco de Dados dentro de outras funções
    def conecta(self):
        
        try:
            self.conexao = sqlite3.connect('EstoqueTintas.db')
            self.cursor = self.conexao.cursor()
        except:
            messagebox.showinfo("Erro", "Banco de Dados não Localizado")

    #Função para Fechar a conexão quando aberta pela função Conecta()
    def desconecta(self):
        self.conexao.commit()
        self.conexao.close()

        
        
#Instanciando a Janela e Criando o mainloop
def RodaApp():
    raiz = tk.Tk()
    app = ControlTintas(raiz)
    raiz.resizable(False, False)
    raiz.mainloop()
    
    

if __name__ == '__main__':
    RodaApp()
