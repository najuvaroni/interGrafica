import customtkinter as tk
tk.set_appearance_mode("light")
def clique1():
    var1 = caixa1
    var2 = caixa2
    soma = var1 + var2
    texto1.configure(text=soma)
def clique2():
    var1 = caixa1
    var2 = caixa2
    sub = var1 - var2
    texto1.configure(text=sub)

def clique4():
    var1 = caixa1
    var2 = caixa2
    soma = var1 / var2
    texto1.configure(text=soma)

def clique5():
    var1 = caixa1
    var2 = caixa2
    soma = var1 * var2
    texto1.configure(text=soma)

janela = tk.CTk()
janela.title("janela 01")
janela.geometry("400x350")
janela.configure(fg_color="white")
janela.resizable(width=False, height=False)
colunas = list (range(13))
linhas = list(range(13))
janela.grid_columnconfigure(colunas, weight=1)
janela.grid_rowconfigure(linhas, weight=1)
texto1 = tk.CTkLabel(janela, text="Média: ", text_color="black")
texto1.grid(row=1, column=4, columnspan=2)
btn1 = tk.CTkButton(janela, text="+", command=clique1, width=70, height=50, fg_color="black", hover_color="white")
btn1.grid(row=6, column=2)
btn2 = tk.CTkButton(janela, text="-", command=clique2, width=70, height=50, fg_color="black", hover_color="white")
btn2.grid(row=6, column=3)
btn4 = tk.CTkButton(janela, text="/", command=clique4 , width=70, height=50, fg_color="black", hover_color="white")
btn4.grid(row=8, column=2)
btn5 = tk.CTkButton(janela, text="*", command=clique5 , width=70, height=50, fg_color="black", hover_color="white")
btn5.grid(row=8, column=3)
caixa1= tk.CTkEntry(janela, placeholder_text="Digite primeiro número:", width=200, height=30)
caixa2= tk.CTkEntry(janela, placeholder_text="Digite o segundo número:", width=200, height=30)
caixa1.grid(row=3, column=4, columnspan=2)
caixa2.grid(row=4, column=4, columnspan=2)




janela.mainloop()