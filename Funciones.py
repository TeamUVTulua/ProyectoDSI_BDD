#-------- FUNCION CARGAR DATOS EN GUI ROL

self.CargarInfoUsuarioEnLabels()
        # INFORMACIO CARGADA QUE NO SE MODIFICA
        Label(frameDerechoAdmin, text=self.id_usu, font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=270, y=60)
        Label(frameDerechoAdmin, text=self.nombre_usu, font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=270, y=100)
        Label(frameDerechoAdmin, text=self.apellido_usu, font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=270, y=140)
        Label(frameDerechoAdmin, text=self.cargo_usu, font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=270, y=180)
        self.listboxUsuario = Listbox(frameDerechoAdmin, width=25, heigh=2, bg="#18344A", fg="white", font=("comic sans MS", 20,))

        self.listboxUsuario.insert(0, self.dir_usu)
        self.listboxUsuario.insert(1, self.tel_usu)

        self.listboxUsuario.place(x=270, y=220)

        BotonModificarDatos = Button(frameDerechoAdmin, text="Modificar datos", command=self.retornarSelecListBoxUsuario, font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonModificarDatos.place(x=80, y=400, width=240)

        BotonCambiarContraseña = Button(frameDerechoAdmin, text="Cambiar Contraseña", command=self.modContraseña, font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonCambiarContraseña.place(x=380,y=400, width=240)


def retornarSelecListBoxUsuario(self):
        gestionUsuarios = gestionUsuario()
        aux = self.listboxUsuario.curselection()
        if (self.listboxUsuario.selection_includes(0)):
                print(aux)
                aux2 = askstring('Modificación de información', 'Ingrese la nueva direccion de usuario')

                if (aux2 == None):
                        showinfo('Modificación de información', 'No se realizó ningun cambio')
                else:
                        showinfo('Modificación de información', 'Tu nombre quedó:  {}'.format(aux2))

                        gestionUsuarios.modificar_direccion(aux2, self.id_usu)
                        print(aux2)

        if (self.listboxUsuario.selection_includes(1)):
                print(aux)
                aux2 = askstring('Modificación de información', 'Ingrese la nueva telefono de usuario')
                if (aux2 == None):
                        showinfo('Modificación de información', 'No se realizó ningun cambio')
                else:
                        showinfo('Modificación de información', 'Tus telefono quedaron: {}'.format(aux2))
                        gestionUsuarios.modificar_telefono(aux2, usuario.get_id_usu())
                print(aux2)


def modContraseña(self):
        gestionUsuarios = gestionUsuario()
        nuevaContraseña = ""
        confirNuevaContra = ""
        contraseñaActual = askstring('Cambiar contraseña', 'Escribe tu contraseña actual')
        if (contraseñaActual == self.contraseña_usu):
                nuevaContraseña = askstring('Cambiar contraseña', 'Escribe tu nueva contraseña')
                if (contraseñaActual == nuevaContraseña):
                        showinfo('Cambiar contraseña', 'La contraseña es igual a la antigua, trata con otra')
                else:
                        confirNuevaContra = askstring('Cambiar contraseña', 'Confirma tu nueva contraseña')
                        if (nuevaContraseña == confirNuevaContra):
                                showinfo('Cambiar contraseña', 'Cambio exitoso, vuelve a hacer login')
                                gestionUsuarios.cambiar_contraseña(confirNuevaContra, usuario.get_contraseña(),
                                                                   usuario.get_id_usu())
                                self.login()
                        else:
                                showinfo('Cambiar contraseña', 'Las contraseñas no coinciden')
        if (contraseñaActual == None):
                showinfo('Modificación de información', 'No se realizó ningun cambio')
        else:
                showinfo('Cambiar contraseña', 'Contraseña incorrecta')

def CargarInfoUsuarioEnLabels(self):
        # print(usuario.get_nombre())

        self.id_usu = usuario.get_id_usu()
        self.nombre_usu = usuario.get_nombre()
        self.apellido_usu = usuario.get_apellido()
        self.cargo_usu = usuario.get_cargo()
        self.dir_usu = usuario.get_direccion()
        self.tel_usu = usuario.get_telefono()
        self.contraseña_usu = usuario.get_contraseña()

        #------------------ volver al login cuando cierra sesion o cambia de contraseña
        def login(self):
                self.rootGUIVendedor.destroy()
                import LoginUsuario as l
                l.iniciar()