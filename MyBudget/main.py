# Made by viniciusgdoliveira


from itertools import count
from tkinter import*
from tkinter import scrolledtext
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox

from turtle import bgcolor
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

from tkinter.ttk import Progressbar
from numpy import pad

################# tkcalendar ###############
from tkcalendar import Calendar, DateEntry
from datetime import date

from PIL import Image, ImageTk

from view import *



################# cores ###############

co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#3fbfb9"   # verde
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde
c10 = "#89181C"   # + vermelho cesusc
c11 = "#006400"   # dark green

colors = ['#5588bb', '#66bbbb','#99bb55', '#ee9944', '#444466', '#bb5555']

################# criando janela ###############

janela = Tk ()
janela.title ("")
janela.geometry('900x650')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")
style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 9)) # Modify the font of the body

################# Frames ####################

frameCima = Frame(janela, width=1043, height=50, bg=co1,  relief="flat",)
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela,width=1043, height=361,bg=co1, pady=20, relief="raised")
frameMeio.grid(row=2, column=0,pady=1, padx=0, sticky=NSEW)

frameBaixo = Frame(janela,width=1043, height=300,bg=co1, relief="flat")
frameBaixo.grid(row=1, column=0, pady=0, padx=10, sticky=NSEW)

frame_gra_2 = Frame(frameMeio, width=580, height=250,bg=co2)
frame_gra_2.place(x=415, y=5)


# abrindo imagem
app_img  = Image.open(r'images\piggybank.png')
app_img = app_img.resize((45, 45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text="                               MyBudgetAPP", width=900, compound=LEFT, padx=5, relief=RAISED, anchor=NW, font=('Verdana 20 bold'),bg=co1, fg=co4 )
app_logo.place(x=0, y=0)

# funcao inserir Categorias despesa

def inserir_categoria_b():
    nome = e_n_categoria.get()
    
    lista_inserir = [nome]
    
    for i in lista_inserir:
        if i=='':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return
        
    inserir_categoria(lista_inserir)

    messagebox.showinfo(
        'Sucesso', 'Os dados foram inseridos com sucesso')
        
    e_n_categoria.delete(0, 'end')
    
    # Pegando os categorias
    categorias_funcao = ver_categorias()
    categorias = []

    for i in categorias_funcao:
        categorias.append(i[1])
    
    # atualizando a lista de categorias
    combo_categoria_despesas['values'] = (categorias)

# funcao inserir Categorias Receita

def inserir_categoria_receita_b():
    nome = e_n_categoria_receita.get()
    
    lista_inserir = [nome]
    
    for i in lista_inserir:
        if i=='':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return
        
    inserir_categoria_receita(lista_inserir)

    messagebox.showinfo(
        'Sucesso', 'Os dados foram inseridos com sucesso')
        
    e_n_categoria_receita.delete(0, 'end')
    
    # Pegando os categorias
    categorias_funcao_receitas = ver_categorias_receita()
    categorias_receita = []

    for i in categorias_funcao_receitas:
        categorias_receita.append(i[1])
    
    # atualizando a lista de categorias
    combo_categoria_receitas['values'] = (categorias_receita)


# funcao inserir Despesas
def inserir_despesas():
    nome = combo_categoria_despesas.get()
    data = e_cal_despeas.get()
    quantia = e_valor_despesas.get()
    
    lista_inserir = [nome, data, quantia]
    
    for i in lista_inserir:
        if i=='':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return
        
    inserir_gastos(lista_inserir)

    messagebox.showinfo(
        'Sucesso', 'Os dados foram inseridos com sucesso')
        
    combo_categoria_despesas.delete(0, 'end')
    e_cal_despeas.delete(0, 'end')
    e_valor_despesas.delete(0, 'end')
    
    # atualizar dados
    mostrar_gastos()
    mostrar_renda()
    percentagem()
    grafico_bar()
    resumo()
    grafico_pie()
    
# funcao inserir Receitas
def inserir_receitas_b():
    nome = combo_categoria_receitas.get()
    data = e_cal_receitas.get()
    quantia = e_valor_receitas.get()
    
    lista_inserir = [nome, data, quantia]
    
    for i in lista_inserir:
        if i=='':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return
        
    inserir_receita(lista_inserir)

    messagebox.showinfo(
        'Sucesso', 'Os dados foram inseridos com sucesso')
    
    combo_categoria_receitas.delete(0,'end')    
    e_cal_receitas.delete(0, 'end')
    e_valor_receitas.delete(0, 'end')
    
    # atualizar dados
    mostrar_gastos()
    mostrar_renda()
    percentagem()
    grafico_bar()
    resumo()
    grafico_pie()

# funcao deletar gastos
def deletar_gasto():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor = treev_lista[0]
        
        deletar_gastos([valor])
                
        messagebox.showinfo(
            'Sucesso', 'Os dados foram deletados com sucesso')
        

    except IndexError:
        messagebox.showerror(
            'Erro', 'Seleciona um dos dados na tabela') 

    mostrar_gastos() 
    mostrar_renda()
    percentagem()
    grafico_bar()
    resumo()
    grafico_pie()

# funcao deletar receitas
def deletar_receita():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor = treev_lista[0]
        
        deletar_receitas([valor])
                
        messagebox.showinfo(
            'Sucesso', 'Os dados foram deletados com sucesso')
        

    except IndexError:
        messagebox.showerror(
            'Erro', 'Seleciona um dos dados na tabela') 

    mostrar_gastos() 
    mostrar_renda()
    percentagem()
    grafico_bar()
    resumo()
    grafico_pie()

# percentagem ------------------------------------

def percentagem():
    l_nome = Label(frameMeio, text="Porcentagem da receita restante                                                      Despesas", height=1,anchor=NW, font=('Verdana 12 '), bg=co1, fg=co4)
    l_nome.place(x=7, y=5)

    style = ttk.Style()
    style.theme_use('default')
    style.configure("black.Horizontal.TProgressbar", background='#daed6b')
    style.configure("TProgressbar", thickness=25)
    bar = Progressbar(frameMeio, length=180,style='black.Horizontal.TProgressbar')
    bar.place(x=10, y=35)
    bar['value'] = percentagem_valor()[0]

    valor = percentagem_valor()[0]
    print(valor)
    l_percentagem = Label(frameMeio, text='{:,.2f} %'.format(valor), height=1,anchor=NW, font=('Verdana 12 '), bg=co1, fg=co4)
    l_percentagem.place(x=200, y=35)

percentagem()


# funcao para grafico bar ------------------------

def grafico_bar():
    # obtendo valores de meses
    lista_meses = ['Renda', 'Despesa', 'Saldo']
    lista_valores = bar_valores()


    # faça figura e atribua objetos de eixo
    figura = plt.Figure(figsize=(4, 3.45), dpi=60)
    ax = figura.add_subplot(111)
    # ax.autoscale(enable=True, axis='both', tight=None)

    ax.bar(lista_meses, lista_valores,  color=colors, width=0.9)
    # create a list to collect the plt.patches data

    c = 0
    # set individual bar lables using above list
    for i in ax.patches:
        # get_x pulls left or right; get_height pushes up or down
        ax.text(i.get_x()-.001, i.get_height()+.5,
                str("{:,.0f}".format(lista_valores[c])), fontsize=17, fontstyle='italic',  verticalalignment='bottom',color='dimgrey')
        c += 1

    ax.set_xticklabels(lista_meses,fontsize=16)

    ax.patch.set_facecolor('#ffffff')
    ax.spines['bottom'].set_color('#CCCCCC')
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['right'].set_linewidth(0)
    ax.spines['top'].set_linewidth(0)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['left'].set_linewidth(1)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(False, color='#EEEEEE')
    ax.xaxis.grid(False)

    canva = FigureCanvasTkAgg(figura, frameMeio)
    canva.get_tk_widget().place(x=10, y=70)

grafico_bar()

# --------------------------------------------------------------------------------------------------------------- 

# funcao de resumo total
def resumo():
    
    valor = bar_valores()
    
    l_linha = Label(frameMeio, text="", width=215, height=1,anchor=NW, font=('arial 1 '), bg='#545454',)
    l_linha.place(x=309, y=52)
    l_sumario = Label(frameMeio, text="Total Renda Mensal      ".upper(), height=1,anchor=NW, font=('Verdana 12'), bg=co1, fg='#83a9e6')
    l_sumario.place(x=306, y=35)
    l_sumario = Label(frameMeio, text='R$ {:,.2f}'.format(valor[0]), height=1,anchor=NW, font=('arial 17 '), bg=co1, fg='#545454')
    l_sumario.place(x=306, y=70)


    l_linha = Label(frameMeio, text="", width=215, height=1,anchor=NW, font=('arial 1 '), bg='#545454',)
    l_linha.place(x=309, y=132)
    l_sumario = Label(frameMeio, text="Total Despesas Mensais".upper(), height=1,anchor=NW, font=('Verdana 12'), bg=co1, fg='#83a9e6')
    l_sumario.place(x=306, y=115)
    l_sumario = Label(frameMeio, text='R$ {:,.2f}'.format(valor[1]), height=1,anchor=NW, font=('arial 17 '), bg=co1, fg='#545454')
    l_sumario.place(x=306, y=150)


    l_linha = Label(frameMeio, text="", width=215, height=1,anchor=NW, font=('arial 1 '), bg='#545454',)
    l_linha.place(x=309, y=207)
    l_sumario = Label(frameMeio, text="Total Saldo da Caixa    ".upper(), height=1,anchor=NW, font=('Verdana 12'), bg=co1, fg='#83a9e6')
    l_sumario.place(x=306, y=190)
    l_sumario = Label(frameMeio, text='R$ {:,.2f}'.format(valor[2]), height=1,anchor=NW, font=('arial 17 '), bg=co1, fg='#545454')
    l_sumario.place(x=306, y=220)


resumo()


# --------------------------------------------------------------------------------------------------------------- 

# funcao grafico pie
def grafico_pie():
    # faça figura e atribua objetos de eixo
    figura = plt.Figure(figsize=(5, 3), dpi=90)
    ax = figura.add_subplot(111)

    lista_valores = pie_valores()[1]
    lista_categorias = pie_valores()[0]

    # only "explode" the 2nd slice (i.e. 'Hogs')

    explode = []
    for i in lista_categorias:
        explode.append(0.05)

    ax.pie(lista_valores, explode=explode, wedgeprops=dict(width=0.2), autopct='%1.1f%%', colors=colors,shadow=True, startangle=90)

    ax.legend(lista_categorias, loc="center right", bbox_to_anchor=(1.55, 0.50))


    canva_categoria = FigureCanvasTkAgg(figura, frame_gra_2)
    canva_categoria.get_tk_widget().grid(row=0,column=0)

grafico_pie()

# ------------- criando frames para tabelas -------------------------

frame_renda = Frame(frameBaixo, width=200, height=250,bg=co1)
frame_renda.grid(row=0,column=1)

frame_configuracao = Frame(frameBaixo, width=185, height=250,bg=co1)
frame_configuracao.grid(row=0,column=0)

frame_operacoes = Frame(frameBaixo, width=185, height=250,bg=co1)
frame_operacoes.grid(row=0,column=2)

frame_despesas = Frame(frameBaixo, width=200, height=250,bg=co1)
frame_despesas.grid(row=0,column=3, padx=1)

# Tabela Renda mensal -------------------------

#l_income = Label(frameMeio, text="Tabela de Receitas", height=1,anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
#l_income.place(x=5, y=309)

# funcao para mostrar_renda
def mostrar_renda():

    # creating a treeview with dual scrollbars
    tabela_head = ['#Id','Categoria','Data','Quantia']

    lista_itens = tabela_receitas()
    
    global tree

    tree = ttk.Treeview(frame_renda, selectmode="extended",columns=tabela_head, show="headings")
    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_renda, orient="vertical", command=tree.yview)
    # horizontal scrollbar
    hsb = ttk.Scrollbar(frame_renda, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    hd=["center","center","center", "center"]
    h=[30,90,60,60]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in lista_itens:
        tree.insert('', 'end', values=item)
         
mostrar_renda()

# Tabela Despesa mensal -------------------------

##l_income = Label(frameMeio, text="Tabela de Gastos", height=1,anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
##l_income.place(x=625, y=309)

# funcao para mostrar_gastos
def mostrar_gastos():

    # creating a treeview with dual scrollbars
    tabela_head = ['#Id','Categoria','Data','Quantia']

    lista_itens = tabela_gastos()
    
    global tree

    tree = ttk.Treeview(frame_despesas, selectmode="extended",columns=tabela_head, show="headings")
    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_despesas, orient="vertical", command=tree.yview)
    # horizontal scrollbar
    hsb = ttk.Scrollbar(frame_despesas, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    hd=["center","center","center", "center"]
    h=[30,90,60,60]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in lista_itens:
        tree.insert('', 'end', values=item)
         
mostrar_gastos()



# Configuracoes Despesas -----------------------------------

l_descricao = Label(frame_operacoes, text="             DESPESAS            ", height=1,anchor=NW,relief="flat", font=('Verdana 10 bold'), bg=c10, fg=co1)
l_descricao.place(x=1, y=1)

l_descricao = Label(frame_operacoes, text="Categoria", height=1,anchor=NW,relief="flat", font=('Ivy 10'), bg=co1, fg=co4)
l_descricao.place(x=1, y=75)

# Pegando os categorias
categorias_funcao = ver_categorias()
categorias = []

for i in categorias_funcao:
    categorias.append(i[1])
    
combo_categoria_despesas = ttk.Combobox(frame_operacoes, width=9,font=('Ivy 10'))
combo_categoria_despesas['values'] = (categorias)
combo_categoria_despesas.place(x=95, y=76)


l_cal_despeas = Label(frame_operacoes, text="Data", height=1,anchor=NW, font=('Ivy 10 '), bg=co1, fg=co4)
l_cal_despeas.place(x=1, y=25)
e_cal_despeas = DateEntry(frame_operacoes, width=11, background='darkblue', foreground='white', borderwidth=2, year=2023, date_pattern='dd/mm/yy')
e_cal_despeas.place(x=95, y=26)

l_valor_despesas = Label(frame_operacoes, text="Quantia em R$", height=1,anchor=NW, font=('Ivy 10 '), bg=co1, fg=co4)
l_valor_despesas.place(x=1, y=50)
e_valor_despesas = Entry(frame_operacoes, width=13, justify='left',relief="solid")
e_valor_despesas.place(x=95, y=51)

# Botao Inserir
img_add_despesas  = Image.open(r'images\add.png')
img_add_despesas = img_add_despesas.resize((20,20))
img_add_despesas = ImageTk.PhotoImage(img_add_despesas)
botao_inserir_despesas = Button(frame_operacoes,command=inserir_despesas, image=img_add_despesas, compound=LEFT, anchor=NW, text=" Adicionar".upper(), width=80, overrelief=RIDGE,  font=('ivy 7 bold'),bg=co1, fg=co0 )
botao_inserir_despesas.place(x=1, y=101)


# Botao Deletar Gastos
img_delete  = Image.open(r'images\delete.png')
img_delete = img_delete.resize((20, 20))
img_delete = ImageTk.PhotoImage(img_delete)
botao_deletar = Button(frame_operacoes,command=deletar_gasto, image=img_delete, compound=LEFT, anchor=NW, text="   Deletar".upper(), width=80, overrelief=RIDGE,  font=('ivy 7 bold'),bg=co1, fg=co0 )
botao_deletar.place(x=95, y=101)

# operacao Nova Categoria Despesa-----------------------

l_n_categoria = Label(frame_operacoes, text="Adicionar nova categoria", height=1,anchor=NW,relief="flat", font=('Verdana 8 bold'), bg=co1, fg=co4)
l_n_categoria.place(x=1, y=135)

l_nova_categoria = Label(frame_operacoes, text="Nome", height=1,anchor=NW, font=('Ivy 10 '), bg=co1, fg=co4)
l_nova_categoria.place(x=1, y=160)

e_n_categoria = Entry(frame_operacoes, width=13, justify='left',relief="solid")
e_n_categoria.place(x=95, y=160)

# Botao Inserir Categoria Despesa
img_add_categoria  = Image.open(r'images\add.png')
img_add_categoria = img_add_categoria.resize((20,20))
img_add_categoria = ImageTk.PhotoImage(img_add_categoria)
botao_inserir_categoria = Button(frame_operacoes,command=inserir_categoria_b, image=img_add_categoria, compound=LEFT, anchor=NW, text=" Adicionar    Categoria".upper(), width=170, overrelief=RIDGE,  font=('ivy 7 bold'),bg=co1, fg=co0 )
botao_inserir_categoria.place(x=1, y=190)

# Configuracoes Receitas -----------------------------------

l_descricao = Label(frame_configuracao, text="             RECEITAS            ", height=1,anchor=NW,relief="flat", font=('Verdana 10 bold'), bg=c11, fg=co1)
l_descricao.place(x=1, y=1)

l_cal_receitas = Label(frame_configuracao, text="Data", height=1,anchor=NW, font=('Ivy 10 '), bg=co1, fg=co4)
l_cal_receitas.place(x=1, y=25)
e_cal_receitas = DateEntry(frame_configuracao, width=11, background='darkblue', foreground='white', borderwidth=2, year=2023, date_pattern='dd/mm/yy')
e_cal_receitas.place(x=95, y=26)

l_valor_receitas = Label(frame_configuracao, text="Quantia em R$", height=1,anchor=NW, font=('Ivy 10 '), bg=co1, fg=co4)
l_valor_receitas.place(x=1, y=50)
e_valor_receitas = Entry(frame_configuracao, width=13, justify='left',relief="solid")
e_valor_receitas.place(x=95, y=51)

# Botao Inserir Receitas
img_add_receitas  = Image.open(r'images\add.png')
img_add_receitas = img_add_receitas.resize((20, 20))
img_add_receitas = ImageTk.PhotoImage(img_add_receitas)
botao_inserir_receitas = Button(frame_configuracao,command=inserir_receitas_b, image=img_add_receitas, compound=LEFT, anchor=NW, text=" Adicionar".upper(), width=80, overrelief=RIDGE,  font=('ivy 7 bold'),bg=co1, fg=co0 )
botao_inserir_receitas.place(x=1, y=101)

# Botao Deletar Receita
img_delete_receita  = Image.open(r'images\delete.png')
img_delete_receita = img_delete_receita.resize((20, 20))
img_delete_receita = ImageTk.PhotoImage(img_delete_receita)
botao_deletar = Button(frame_configuracao,command=deletar_receita, image=img_delete_receita, compound=LEFT, anchor=NW, text="   Deletar".upper(), width=80, overrelief=RIDGE,  font=('ivy 7 bold'),bg=co1, fg=co0 )
botao_deletar.place(x=95, y=101)

# Botao Inserir Categoria Receitas
img_add_categoria_receita  = Image.open(r'images\add.png')
img_add_categoria_receita = img_add_categoria_receita.resize((20,20))
img_add_categoria_receita = ImageTk.PhotoImage(img_add_categoria_receita)
img_add_categoria_receita = Button(frame_configuracao,command=inserir_categoria_receita_b, image=img_add_categoria, compound=LEFT, anchor=NW, text=" Adicionar    Categoria".upper(), width=170, overrelief=RIDGE,  font=('ivy 7 bold'),bg=co1, fg=co0 )
img_add_categoria_receita.place(x=1, y=190)

# operacao Nova Categoria receita-----------------------

l_n_categoria_receita = Label(frame_configuracao, text="Adicionar nova categoria", height=1,anchor=NW,relief="flat", font=('Verdana 8 bold'), bg=co1, fg=co4)
l_n_categoria_receita.place(x=1, y=135)

l_nova_categoria_receita = Label(frame_configuracao, text="Nome", height=1,anchor=NW, font=('Ivy 10 '), bg=co1, fg=co4)
l_nova_categoria_receita.place(x=1, y=160)

e_n_categoria_receita = Entry(frame_configuracao, width=13, justify='left',relief="solid")
e_n_categoria_receita.place(x=95, y=160)

# Pegando os categorias
categorias_funcao_receita = ver_categorias_receita()
categorias_receita = []

for i in categorias_funcao_receita:
    categorias_receita.append(i[1])
    
combo_categoria_receitas = ttk.Combobox(frame_configuracao, width=9,font=('Ivy 10'))
combo_categoria_receitas['values'] = (categorias_receita)
combo_categoria_receitas.place(x=95, y=76)

l_descricao = Label(frame_configuracao, text="Categoria", height=1,anchor=NW,relief="flat", font=('Ivy 10'), bg=co1, fg=co4)
l_descricao.place(x=1, y=75)

janela.mainloop ()