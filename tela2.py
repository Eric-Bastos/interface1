import customtkinter as ctk 

def combustivel():
    d= int(distancia.get())
    c=int(veiculo.get())
    p=float(preco.get())
    
    calculo= (d/c)*p
    resultado.configure(text=f'O valor total para a viagem será de R${calculo:.2f} ')

ctk.set_appearance_mode('dark')
janela=ctk.CTk()
janela.geometry('500x500')
ctk.CTkLabel(janela, text= 'aplicativo saude',font=('arial',50,'bold'),text_color='white').pack(pady=15)

distancia= ctk.CTkEntry(janela, placeholder_text='Digite a distância',width=450,height=50)
distancia.pack(pady=10)
veiculo= ctk.CTkEntry(janela, placeholder_text='Digite o consumo do veículo',width=450,height=50)
veiculo.pack(pady=10)
preco=ctk.CTkEntry(janela,placeholder_text='Digite o preço do Combustivel',width=450,height=50)
preco.pack(pady=10)
calcular=ctk.CTkButton(janela,text='calcular',font=('arial',30),fg_color='green',command=combustivel)
calcular.pack(pady=5)

resultado= ctk.CTkLabel(janela, text='', font=('arial',18))
resultado.pack(pady=5)

janela.mainloop()