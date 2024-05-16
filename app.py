import tkinter as tk
from tkinter import messagebox

class Cliente:
    def __init__(self, id, nombre, correo, direccion, telefono):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.direccion = direccion
        self.telefono = telefono

class Programa:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestión de Clientes")
        self.ventana.configure(bg="#00FFFF")

        self.clientes = []

        self.menu_principal()

    def menu_principal(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

        lbl_titulo = tk.Label(self.ventana, text="Menú Principal", font=("Arial", 18), bg="#00FFFF")  
        lbl_titulo.pack(pady=10)

        btn_registrar = tk.Button(self.ventana, text="Registrar Cliente", command=self.registrar_cliente, bg="#4CAF50", fg="white")
        btn_registrar.pack(pady=5)

        btn_consultar = tk.Button(self.ventana, text="Consultar Cliente", command=self.consultar_cliente, bg="#008CBA", fg="white")  
        btn_consultar.pack(pady=5)

        btn_actualizar = tk.Button(self.ventana, text="Actualizar Cliente", command=self.actualizar_cliente, bg="#f44336", fg="white") 
        btn_actualizar.pack(pady=5)

        btn_salir = tk.Button(self.ventana, text="Salir", command=self.ventana.destroy, bg="#555", fg="white")
        btn_salir.pack(pady=5)

    def registrar_cliente(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

        lbl_titulo = tk.Label(self.ventana, text="Registrar Cliente", font=("Arial", 18), bg="#00FFFF")
        lbl_titulo.pack(pady=10)

        lbl_id = tk.Label(self.ventana, text="ID:", bg="#00FFFF") 
        lbl_id.pack()
        entry_id = tk.Entry(self.ventana)
        entry_id.pack()

        lbl_nombre = tk.Label(self.ventana, text="Nombre:", bg="#00FFFF") 
        lbl_nombre.pack()
        entry_nombre = tk.Entry(self.ventana)
        entry_nombre.pack()

        lbl_correo = tk.Label(self.ventana, text="Correo:", bg="#00FFFF")
        lbl_correo.pack()
        entry_correo = tk.Entry(self.ventana)
        entry_correo.pack()

        lbl_direccion = tk.Label(self.ventana, text="Dirección:", bg="#00FFFF")
        lbl_direccion.pack()
        entry_direccion = tk.Entry(self.ventana)
        entry_direccion.pack()

        lbl_telefono = tk.Label(self.ventana, text="Teléfono:", bg="#00FFFF") 
        lbl_telefono.pack()
        entry_telefono = tk.Entry(self.ventana)
        entry_telefono.pack()

        btn_guardar = tk.Button(self.ventana, text="Guardar", command=lambda: self.guardar_cliente(
            entry_id.get(), entry_nombre.get(), entry_correo.get(), entry_direccion.get(), entry_telefono.get()), bg="#4CAF50", fg="white") 
        btn_guardar.pack(pady=10)

        btn_regresar = tk.Button(self.ventana, text="Regresar", command=self.menu_principal, bg="#555", fg="white") 
        btn_regresar.pack()

    def guardar_cliente(self, id, nombre, correo, direccion, telefono):
        self.clientes.append(Cliente(id, nombre, correo, direccion, telefono))
        messagebox.showinfo("Éxito", "Cliente registrado correctamente.")
        self.menu_principal()

    def consultar_cliente(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

        lbl_titulo = tk.Label(self.ventana, text="Consultar Cliente", font=("Arial", 18), bg="#00FFFF") 
        lbl_titulo.pack(pady=10)

        lbl_id = tk.Label(self.ventana, text="ID:", bg="#00FFFF") 
        lbl_id.pack()
        entry_id = tk.Entry(self.ventana)
        entry_id.pack()

        btn_consultar = tk.Button(self.ventana, text="Consultar", command=lambda: self.mostrar_cliente(entry_id.get()), bg="#008CBA", fg="white")  
        btn_consultar.pack(pady=10)

        btn_regresar = tk.Button(self.ventana, text="Regresar", command=self.menu_principal, bg="#555", fg="white")  
        btn_regresar.pack()

    def mostrar_cliente(self, id):
        encontrado = False
        for cliente in self.clientes:
            if cliente.id == id:
                messagebox.showinfo("Cliente Encontrado", f"Nombre: {cliente.nombre}\nCorreo: {cliente.correo}\nDirección: {cliente.direccion}\nTeléfono: {cliente.telefono}")
                encontrado = True
                break
        if not encontrado:
            messagebox.showerror("Error", "Cliente no encontrado.")

    def actualizar_cliente(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

        lbl_titulo = tk.Label(self.ventana, text="Actualizar Cliente", font=("Arial", 18), bg="#00FFFF")  
        lbl_titulo.pack(pady=10)

        lbl_id = tk.Label(self.ventana, text="ID:", bg="#00FFFF") 
        lbl_id.pack()
        entry_id = tk.Entry(self.ventana)
        entry_id.pack()

        btn_actualizar = tk.Button(self.ventana, text="Actualizar", command=lambda: self.mostrar_formulario_actualizar(entry_id.get()), bg="#f44336", fg="white")
        btn_actualizar.pack(pady=10)

        btn_regresar = tk.Button(self.ventana, text="Regresar", command=self.menu_principal, bg="#555", fg="white")
        btn_regresar.pack()

    def mostrar_formulario_actualizar(self, id):
        for widget in self.ventana.winfo_children():
            widget.destroy()

        lbl_titulo = tk.Label(self.ventana, text="Actualizar Cliente", font=("Arial", 18), bg="#00FFFF")
        lbl_titulo.pack(pady=10)

        encontrado = False
        for cliente in self.clientes:
            if cliente.id == id:
                encontrado = True
                break

        if encontrado:
            lbl_nombre = tk.Label(self.ventana, text="Nombre:", bg="#00FFFF")
            lbl_nombre.pack()
            entry_nombre = tk.Entry(self.ventana)
            entry_nombre.insert(tk.END, cliente.nombre)
            entry_nombre.pack()

            lbl_correo = tk.Label(self.ventana, text="Correo:", bg="#00FFFF")
            lbl_correo.pack()
            entry_correo = tk.Entry(self.ventana)
            entry_correo.insert(tk.END, cliente.correo)
            entry_correo.pack()

            lbl_direccion = tk.Label(self.ventana, text="Dirección:", bg="#00FFFF")
            lbl_direccion.pack()
            entry_direccion = tk.Entry(self.ventana)
            entry_direccion.insert(tk.END, cliente.direccion)
            entry_direccion.pack()

            lbl_telefono = tk.Label(self.ventana, text="Teléfono:", bg="#00FFFF")  
            lbl_telefono.pack()
            entry_telefono = tk.Entry(self.ventana)
            entry_telefono.insert(tk.END, cliente.telefono)
            entry_telefono.pack()

            btn_guardar = tk.Button(self.ventana, text="Guardar", command=lambda: self.guardar_actualizacion(
                id, entry_nombre.get(), entry_correo.get(), entry_direccion.get(), entry_telefono.get()), bg="#4CAF50", fg="white")
            btn_guardar.pack(pady=10)
        else:
            messagebox.showerror("Error", "Cliente no encontrado.")

    def guardar_actualizacion(self, id, nombre, correo, direccion, telefono):
        for cliente in self.clientes:
            if cliente.id == id:
                cliente.nombre = nombre
                cliente.correo = correo
                cliente.direccion = direccion
                cliente.telefono = telefono
                messagebox.showinfo("Éxito", "Cliente actualizado correctamente.")
                self.menu_principal()
                return
        messagebox.showerror("Error", "Cliente no encontrado.")

ventana = tk.Tk()
app = Programa(ventana)
ventana.mainloop()
