import customtkinter as tk
tk.set_appearance_mode("light")

def clique():
    var1 = int(caixa1.get())
    var2 = int(caixa2.get())
    media = (var1+var2)/2
    if media  >= 6 :
        texto1.configure(text="Aprovado!")
    else:
        texto1.configure(text="reprovado!")

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
texto1.grid(row=6, column=6)
btn1 = tk.CTkButton(janela, text="Enviar", command=clique, width=70, height=50, fg_color="black", hover_color="white")
btn1.grid(row=10, column=6)
caixa1= tk.CTkEntry(janela, placeholder_text="Digite a primeira nota:", width=200, height=30)
caixa1.grid(row=7, column=6)
caixa2= tk.CTkEntry(janela, placeholder_text="Digite a segunda nota:", width=200, height=30)
caixa1.grid(row=7, column=6)
caixa2.grid(row=8, column=6)

janela.mainloop()