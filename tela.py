import customtkinter as ctk

ctk.set_appearance_mode('dark')
janela= ctk.CTk('#851C1A')
janela.geometry('500x500')
ctk.CTkLabel(janela, text='Sistema de Login', font=('arial',50,'bold'),text_color='yellow').pack(pady=15)

login= ctk.CTkEntry(janela, placeholder_text='Digite o seu Login',width=450,height=50)
login.pack(pady=10)

senha= ctk.CTkEntry(janela, placeholder_text='Digite a sua Senha',width=450,height=50,show='*')
senha.pack(pady=10)

botao= ctk.CTkButton(janela,text='Acessar',font=('arial',30),fg_color='black')
botao.pack(pady=5)

janela.mainloop()