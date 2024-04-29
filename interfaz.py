import tkinter as tk
from tkinter import filedialog, messagebox
import servicio
import os.path

ancho_ventana = 400
alto_ventana = 300
archivo = None

# Función para ejecutar al hacer clic en el botón
def abrir_segunda_ventana():
    ventana.iconify()
    segunda_ventana = tk.Toplevel(ventana)
    segunda_ventana.title("Segunda Ventana")
    segunda_ventana.configure(bg="#FFFFCC")
    segunda_ventana.geometry("500x400+20+20")
    
    label_titulo = tk.Label(segunda_ventana, text="Mensajeria - MIME", font=("Helvetica", 16, "bold"))
    label_titulo.grid(row=0, column=0, columnspan=2, pady=10)

    label_destinatario = tk.Label(segunda_ventana, text="Destinatario: ", font=("Helvetica", 12, "bold"))
    label_destinatario.grid(row=1, column=0, pady=5)
    input_destinatario = tk.Entry(segunda_ventana, width=40)
    input_destinatario.grid(row=1, column=1, pady=10)

    label_asunto = tk.Label(segunda_ventana, text="Asunto:", font=("Helvetica", 12, "bold"))
    label_asunto.grid(row=2, column=0, pady=5)
    input_asunto = tk.Entry(segunda_ventana, width=40)
    input_asunto.grid(row=2, column=1, pady=10)
    
    label_texto = tk.Label(segunda_ventana, text="Mensaje:", font=("Helvetica", 12, "bold"))
    label_texto.grid(row=3, column=0, pady=5)
    input_texto = tk.Text(segunda_ventana, width=40, height=10)
    input_texto.grid(row=3, column=1, pady=10)

    def agregar_archivo():
        global archivo
        archivo = filedialog.askopenfilename()  # Abre el diálogo para seleccionar archivos
        label_archivo = tk.Label(segunda_ventana, text=archivo)
        label_archivo.grid(row=4, column=1, pady=5)
      
    def conectar():
        correo = input_correo.get()
        password = input_password.get()
        destinatario = input_destinatario.get()
        asunto = input_asunto.get()
        texto = input_texto.get("1.0", "end-1c")
        base, extension = os.path.splitext(archivo)

        servicio.enviar_correo(correo, password, destinatario, asunto, texto, archivo, extension[1:])
        #Mensaje de confirmacion
        messagebox.showinfo(message="Correo enviado  con exito", title="Confirmacion")
              
    boton_adjuntar = tk.Button(segunda_ventana, text="Agregar Archivo", command=agregar_archivo)
    boton_adjuntar.grid(row=4, column=0, pady=5)
    
    boton_enviar = tk.Button(segunda_ventana, text="Enviar correo", command=conectar, bg="green", fg="white")
    boton_enviar.grid(row=5, column=0, columnspan=2, pady=10)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicacion - Servicios Telematicos")
ventana.configure(bg="#FFFFCC")

label_titulo = tk.Label(ventana, text="Mensajeria - MIME", font=("Helvetica", 16, "bold"))
label_titulo.grid(row=0, column=0, columnspan=2, pady=10)

# Dimensiones y posicionamiento
x = (ventana.winfo_screenwidth() // 2) - (ancho_ventana // 2)
y = (ventana.winfo_screenheight() // 2) - (alto_ventana // 2)
ventana.geometry(f'{ancho_ventana}x{alto_ventana}+{x}+{y}')

# Crear componenetes
label_correo = tk.Label(ventana, text="Correo Electronico:", font=("Helvetica", 12, "bold"))
label_correo.grid(row=2, column=0, pady=5)
input_correo = tk.Entry(ventana, width=40)
input_correo.grid(row=2, column=1, pady=10)

label_password = tk.Label(ventana, text="Contraseña:", font=("Helvetica", 12, "bold"))
label_password.grid(row=3, column=0, pady=5)
input_password = tk.Entry(ventana, width=40, show="*")
input_password.grid(row=3, column=1, pady=10)

boton_acceder = tk.Button(ventana, text="Acceder", command=abrir_segunda_ventana, bg="green", fg="white")
boton_acceder.grid(row=5, column=0, columnspan=2, pady=10)

# Iniciar la aplicación
ventana.mainloop()
