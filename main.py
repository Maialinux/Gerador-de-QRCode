import qrcode, customtkinter
from tkinter import messagebox, PhotoImage

# Bibliotecas(Módulos) instaladas:>>>> qrcode, pillow 

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")

def gera_qr_code():
    url = website_entry.get()

    if len(url) == 0:
        messagebox.showinfo(
            title="Erro!",
            message="Favor insira uma URL válida")
    else:
        opcao_escolhida = messagebox.askokcancel(
            title=url,
            message=f"O endereço URL é: \n "
                    f"Endereço: {url} \n "
                    f"Pronto para salvar?")

        if opcao_escolhida:
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image(fill_color='black', back_color='white')
            img.save('QRCodeExportado.png')
            messagebox.showinfo(title="QRCode Gerado", message="QRCode gerado com sucesso !")


if __name__ == '__main__':
    window = customtkinter.CTk()
    img = PhotoImage(file="./favicon.png")
    window.iconphoto(True,img)
    window.title("Gerador de Código QR")
    window.geometry("600x400")
    window.resizable(width=False, height=False)
    window.config(padx=10, pady=20)
    

    # Labels
    website_label_titulo = customtkinter.CTkLabel(window,text="Gerador de QR-Code", font=("FFF Tusj", 50))
    website_label_titulo.grid(row=0, column=1,pady=40)
    website_label = customtkinter.CTkLabel(window,text="URL:")
    website_label.grid(row=2, column=0,pady=20)

    # Entries
    website_entry = customtkinter.CTkEntry(window,width=500)
    website_entry.grid(row=2, column=1, columnspan=2,padx=20)
    website_entry.focus()
    add_button = customtkinter.CTkButton(window,text="Gerar QR Code", width=100, command=gera_qr_code)
    add_button.grid(row=4, column=1, columnspan=2,pady=20)
    
    # Rodapé
    website_label_rodape = customtkinter.CTkLabel(window,text="Criado por Eduardo Maia <distromaialinux@gmail.com>", font=("Oswald", 22))
    website_label_rodape.grid(row=5, column=1,pady=60)
    window.mainloop()