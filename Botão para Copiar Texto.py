import tkinter as tk
from tkinter import messagebox

# Função para copiar o texto para a área de transferência usando tkinter
def copy_text():
    try:
        # Obtém o texto que será copiado
        text = text_label.cget("text")
        # Copia o texto para a área de transferência
        root.clipboard_clear()  # Limpa a área de transferência
        root.clipboard_append(text)  # Adiciona o texto à área de transferência
        root.update()  # Atualiza a área de transferência

        # Mostra a mensagem de sucesso
        messagebox.showinfo("Sucesso", "Texto copiado para a área de transferência!")
    except Exception as e:
        print(f"Erro ao copiar: {e}")
        messagebox.showerror("Erro", "Falha ao copiar o texto.")

# Criando a janela principal
root = tk.Tk()
root.title("Copy To Clipboard")
root.geometry("400x200")
root.configure(bg="#f1f1f1")

# Definindo o estilo
button_color = "#3d91f5"
button_text_color = "#ffffff"
label_color = "#202020"
alert_color = "#202020"
alert_text_color = "#ffffff"

# Adicionando um título (parágrafo)
text_label = tk.Label(root, text="Aqui nesse botão você pode copiar qualquer texto.", 
                      font=("Arial", 16), bg="#f1f1f1", fg=label_color)
text_label.pack(pady=20)

# Adicionando o botão para copiar
copy_button = tk.Button(root, text="Copiar", font=("Arial", 14), bg=button_color, fg=button_text_color, 
                        command=copy_text, relief="flat", padx=20, pady=10)
copy_button.pack()

# Função para mostrar o alerta (mensagem de sucesso)
def show_alert():
    alert = tk.Toplevel(root)
    alert.title("Alerta")
    alert.geometry("250x100")
    alert.configure(bg=alert_color)
    
    alert_label = tk.Label(alert, text="Texto copiado!", font=("Arial", 14), fg=alert_text_color, bg=alert_color)
    alert_label.pack(expand=True)
    
    alert.after(1000, alert.destroy)  # Fecha o alerta após 1 segundo

# Mantendo a aplicação em execução
root.mainloop()
