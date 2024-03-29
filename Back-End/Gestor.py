from Usuarios import Usuario,Admin,Doctor,Paciente,Enfermera,TopDr
from Medicamentos import Medicamento,MasVendidosMed
from Pedidos import Pedido
from Citas import Cita,EnfComun
import random
import json
import re

class Gestor:
    def __init__(self):
        self.usuarios = []
        self.admin = []
        self.doctores = []
        self.pacientes = []
        self.enfermeras = []
        self.medicamentos = []
        self.medMasV = []
        self.docMasA = []
        self.topEnfermedad = []
        self.pedidos = []
        self.citas = []

        #datos quemados------------------------------------
        #-----------------------admin-----------------------------------
        self.usuarios.append(Usuario('admin','admin','1234'))
        self.admin.append(Admin('Herbert','Reyes','2000-12-04','M','admin','1234','12345678'))
        #---------------------------------------------------------------

        """
        #-----------------------doctor----------------------------------
        self.usuarios.append(Usuario('doctor','docUser1','1234'))
        self.docMasA.append(TopDr('docUser1','NombreDoc1','ApellidoDoc1','4'))
        self.doctores.append(Doctor('NombreDoc1','ApellidoDoc1','2000-12-04','M','docUser1','1234','Neurocirugia','12345678'))

        self.usuarios.append(Usuario('doctor','docUser2','1234'))
        self.docMasA.append(TopDr('docUser2','NombreDoc2','ApellidoDoc2','11'))
        self.doctores.append(Doctor('NombreDoc2','ApellidoDoc2','2000-12-04','M','docUser2','1234','Neurocirugia','12345678'))

        self.usuarios.append(Usuario('doctor','docUser3','1234'))
        self.docMasA.append(TopDr('docUser3','NombreDoc3','ApellidoDoc3','15'))
        self.doctores.append(Doctor('NombreDoc3','ApellidoDoc3','2000-12-04','M','docUser3','1234','Neurocirugia','12345678'))

        self.usuarios.append(Usuario('doctor','docUser4','1234'))
        self.docMasA.append(TopDr('docUser4','NombreDoc4','ApellidoDoc4','7'))
        self.doctores.append(Doctor('NombreDoc4','ApellidoDoc4','2000-12-04','M','docUser4','1234','Neurocirugia','12345678'))

        self.usuarios.append(Usuario('doctor','docUser5','1234'))
        self.docMasA.append(TopDr('docUser5','NombreDoc5','ApellidoDoc5','13'))
        self.doctores.append(Doctor('NombreDoc5','ApellidoDoc5','2000-12-04','M','docUser5','1234','Neurocirugia','12345678'))
        #---------------------------------------------------------------
        #-----------------------enfermera-------------------------------
        self.usuarios.append(Usuario('enfermera','enfUser','1234'))
        self.enfermeras.append(Enfermera('NombreEnf','ApellidoEnf','2000-12-04','F','enfUser','1234','12345678'))
        #---------------------------------------------------------------
        #-----------------------paciente--------------------------------
        self.usuarios.append(Usuario('paciente','pacUser','1234'))
        self.pacientes.append(Paciente('NombrePac','ApellidoPac','2000-12-04','M','pacUser','1234','12345678'))
        self.usuarios.append(Usuario('paciente','user1','1234'))
        self.pacientes.append(Paciente('NombrePac1','ApellidoPac1','2000-12-04','M','user1','1234','12345678'))
        self.usuarios.append(Usuario('paciente','user2','1234'))
        self.pacientes.append(Paciente('NombrePac2','ApellidoPac2','2000-12-04','M','user2','1234','12345678'))
        #---------------------------------------------------------------
        #-----------------------medicamentos----------------------------
        self.medicamentos.append(Medicamento('Aspirina','10.50','Calma el dolor','10'))
        self.medicamentos.append(Medicamento('Acetaminofen','15','Calma el dolor','20'))
        self.medicamentos.append(Medicamento('Adenosina','250','Calma el dolor','15'))

        self.medicamentos.append(Medicamento('Mefobarbital','100','Calma el dolor','5'))
        self.medicamentos.append(Medicamento('Paracetamol','25.75','Calma el dolor','13'))
        self.medicamentos.append(Medicamento('Oxymetholone','115.50','Calma el dolor','7'))

        self.medicamentos.append(Medicamento('Penicilamina','250.75','Calma el dolor','14'))
        self.medicamentos.append(Medicamento('Fenitoína','100.50','Calma el dolor','17'))
        self.medicamentos.append(Medicamento('Posaconazol','150','Calma el dolor','8'))

        self.medMasV.append(MasVendidosMed('Aspirina','Calma el dolor','7'))
        self.medMasV.append(MasVendidosMed('Acetaminofen','Calma el dolor','25'))
        self.medMasV.append(MasVendidosMed('Adenosina','Calma el dolor','13'))

        self.medMasV.append(MasVendidosMed('Mefobarbital','Calma el dolor','9'))
        self.medMasV.append(MasVendidosMed('Paracetamol','Calma el dolor','5'))
        self.medMasV.append(MasVendidosMed('Oxymetholone','Calma el dolor','7'))

        self.medMasV.append(MasVendidosMed('Penicilamina','Calma el dolor','14'))
        self.medMasV.append(MasVendidosMed('Fenitoína','Calma el dolor','11'))
        self.medMasV.append(MasVendidosMed('Posaconazol','Calma el dolor','5'))
        #---------------------------------------------------------------
        #-------------------enfermedades comunes------------------------
        self.topEnfermedad.append(EnfComun('Dolor de cabeza','6'))
        self.topEnfermedad.append(EnfComun('Dolor de garganta','7'))
        self.topEnfermedad.append(EnfComun('Dolor de estomago','3'))
        self.topEnfermedad.append(EnfComun('Dolor de espalda','8'))
        #---------------------------------------------------------------
        """
    #Read
    def obtener_usuarios(self):
        return json.dumps([ob.__dict__ for ob in self.usuarios])

    def obtener_medicamentos(self):
        return json.dumps([ob.__dict__ for ob in self.medicamentos])

    def obtener_pedido(self):
        return json.dumps([ob.__dict__ for ob in self.pedidos])
    
    def obtener_citas(self):
        return json.dumps([ob.__dict__ for ob in self.citas])

    def obtener_topMed(self):
        self.ordenamientoVentas(self.medMasV)
        return json.dumps([ob.__dict__ for ob in self.medMasV])
    
    def obtener_topDocCit(self):
        self.ordenamientoDoctoresCitas(self.docMasA)
        return json.dumps([ob.__dict__ for ob in self.docMasA])

    def obtener_topEnf(self):
        self.ordenamientoEnfermedades(self.topEnfermedad)
        return json.dumps([ob.__dict__ for ob in self.topEnfermedad])

    #Update
    def actualizar_usuario(self,usuario,data):
        for i in self.usuarios:
            if i.usuario == usuario:
                if i.usuario == data['usuario'] or self.verificar_usuario(data['usuario']):
                    telefono = 'Sin registrar'
                    if data['telefono'] != '':
                        telefono = data['telefono']
                    if data['tipo'] == 'doctor':
                        for j in self.doctores:
                            if j.usuario == i.usuario:
                                for k in self.docMasA:
                                    if k.usuario == j.usuario:
                                        self.docMasA[self.docMasA.index(k)] = TopDr(data['usuario'],data['nombre'],data['apellido'],k.citasAt)
                                self.usuarios[self.usuarios.index(i)] = Usuario(data['tipo'],data['usuario'],data['password'])
                                self.doctores[self.doctores.index(j)] = Doctor(data['nombre'],data['apellido'],data['fecha'],data['genero'],data['usuario'],data['password'],data['especialidad'],telefono)
                                return '{"data":"actualizado"}'
                    if data['tipo'] == 'enfermera':
                        for j in self.enfermeras:
                            if j.usuario == i.usuario:
                                self.usuarios[self.usuarios.index(i)] = Usuario(data['tipo'],data['usuario'],data['password'])
                                self.enfermeras[self.enfermeras.index(j)] = Enfermera(data['nombre'],data['apellido'],data['fecha'],data['genero'],data['usuario'],data['password'],telefono)
                                return '{"data":"actualizado"}'
                    if data['tipo'] == 'paciente':
                        for j in self.pacientes:
                            if j.usuario == i.usuario:
                                self.usuarios[self.usuarios.index(i)] = Usuario(data['tipo'],data['usuario'],data['password'])
                                self.pacientes[self.pacientes.index(j)] = Paciente(data['nombre'],data['apellido'],data['fecha'],data['genero'],data['usuario'],data['password'],telefono)
                                return '{"data":"actualizado"}'
        return '{"data":"enUso"}'

    def actualizar_medicamento(self,nombre,descripcion,data):
        for i in self.medicamentos:
            if i.nombre == nombre and i.descripcion == descripcion:
                for j in self.medMasV:
                    if j.nombre == i.nombre and j.descripcion == i.descripcion:
                        self.medicamentos[self.medicamentos.index(i)] = Medicamento(data['nombre'],data['precio'],data['descripcion'],data['cantidad'])
                        self.medMasV[self.medMasV.index(j)] = MasVendidosMed(data['nombre'],data['descripcion'],j.unidadesV)
                        return '{"data":"actualizado"}'

    def aceptar_ciDoc(self,usuario,docUser):
        for i in self.citas:
            if i.usuario == usuario:
                self.citas[self.citas.index(i)] = Cita(i.usuario,i.fecha,i.hora,i.motivo,docUser,'','Aceptado')
                return '{"cita":"Aceptado"}'

    def aceptar_ciEnf(self,usuario,docUser,enfUser):
        for i in self.citas:
            if i.usuario == usuario:
                self.citas[self.citas.index(i)] = Cita(i.usuario,i.fecha,i.hora,i.motivo,docUser,enfUser,'Aceptado')
                return '{"cita":"Aceptado"}'

    def rechazar_ciDoc(self,usuario):
        for i in self.citas:
            if i.usuario == usuario:
                self.citas[self.citas.index(i)] = Cita(i.usuario,i.fecha,i.hora,i.motivo,'','','Rechazado')
                return '{"cita":"Rechazado"}'

    #Delete
    def eliminar_usuario(self,tipo,usuario):
        for i in self.usuarios:
            if tipo == 'doctor' and i.usuario == usuario:
                for j in self.doctores:
                    if j.usuario == i.usuario:
                        for k in self.docMasA:
                            if k.usuario == j.usuario:
                                self.docMasA.remove(k)
                        self.usuarios.remove(i)
                        self.doctores.remove(j)
                        return json.dumps(j.__dict__)
            if tipo == 'enfermera' and i.usuario == usuario:
                for j in self.enfermeras:
                    if j.usuario == i.usuario:
                        self.usuarios.remove(i)
                        self.enfermeras.remove(j)
                        return json.dumps(j.__dict__)
            if tipo == 'paciente' and i.usuario == usuario:
                for j in self.pacientes:
                    if j.usuario == i.usuario:
                        for k in self.pedidos:
                            if k.usuario == j.usuario:
                                self.quitar_pedido(k.usuario,k.codigo)
                        self.usuarios.remove(i)
                        self.pacientes.remove(j)
                        return json.dumps(j.__dict__)

    def eliminar_medicamento(self,nombre,descripcion):
        for i in self.medMasV:
            if i.nombre == nombre and i.descripcion == descripcion:
                self.medMasV.remove(i)
        for i in self.pedidos:
            if i.medicamento == nombre and i.descripcion == descripcion:
                self.pedidos.remove(i)
        for i in self.medicamentos:
            if i.nombre == nombre and i.descripcion == descripcion:
                self.medicamentos.remove(i)
                return json.dumps(i.__dict__)
                

    def eliminar_cita(self,usuario):
        for i in self.citas:
            if i.usuario == usuario:
                self.citas.remove(i)
                return '{"solicitud":"eliminada"}'
    
    def completar_citaCont(self,usuario):
        for i in self.docMasA:
            if i.usuario == usuario:
                citas = int(i.citasAt)
                citas += 1
                self.docMasA[self.docMasA.index(i)] = TopDr(i.usuario,i.nombre,i.apellido,citas)
                return '{"citas":"incrementado"}'

    #Buscar
    def buscar_tipo_usuario(self,usuario):
        for i in self.usuarios:
            if i.usuario == usuario:
                if i.tipo == 'admin':
                    for j in self.admin:
                        if j.usuario == i.usuario:
                            return json.dumps(j.__dict__)
                if i.tipo == 'doctor':
                    for j in self.doctores:
                        if j.usuario == i.usuario:
                            return json.dumps(j.__dict__)
                if i.tipo == 'enfermera':
                    for j in self.enfermeras:
                        if j.usuario == i.usuario:
                            return json.dumps(j.__dict__)
                if i.tipo == 'paciente':
                    for j in self.pacientes:
                        if j.usuario == i.usuario:
                            return json.dumps(j.__dict__)

    def buscar_medicamento(self,nombre,descripcion):
        for i in self.medicamentos:
            if i.nombre == nombre and i.descripcion == descripcion:
                return json.dumps(i.__dict__)

    def buscar_cita(self,usuario):
        for i in self.citas:
            if i.usuario == usuario:
                return json.dumps(i.__dict__)
        return '{"cita":"false"}'

    def clasificar_usuario(self,tipo):
        if tipo == 'doctor':
            return json.dumps([ob.__dict__ for ob in self.doctores])
        if tipo == 'paciente':
            return json.dumps([ob.__dict__ for ob in self.pacientes])
        if tipo == 'enfermera':
            return json.dumps([ob.__dict__ for ob in self.enfermeras])

    #Iniciar Sesion
    def iniciar_sesion(self,usuario,password):
        for i in self.usuarios:
            if i.password == password and i.usuario == usuario:
                return json.dumps(i.__dict__)
        return '{"nombre":"false"}'

    #Registrar Usuario
    def registrar_usuario(self,tipo,nombre,apellido,fecha,genero,usuario,password,telefono):
        if self.verificar_usuario(usuario):
            self.usuarios.append(Usuario(tipo,usuario,password))
            self.pacientes.append(Paciente(nombre,apellido,fecha,genero,usuario,password,telefono))
            return '{"data":"creado"}'
        return '{"data":"enUso"}'

    def verificar_usuario(self,usuario):
        for i in self.usuarios:
            if i.usuario == usuario:
                return False
        return True

    #Carga Masiva Doctores
    def cargamasivaDoc(self,data):
        try:
            fila = re.split('\n',data)
            i=1
            while i < len(fila):
                campo = re.split(',',fila[i])
                compFecha = re.split('/',campo[2])
                fecha = compFecha[2]+"-"+compFecha[1]+"-"+compFecha[0]
                telefono='Sin registrar'
                try:
                    if campo[7] != '':
                        telefono = campo[7]
                except:
                    pass
                self.usuarios.append(Usuario('doctor',campo[4],campo[5]))
                self.doctores.append(Doctor(campo[0],campo[1],fecha,campo[3],campo[4],campo[5],campo[6],telefono))
                self.docMasA.append(TopDr(campo[4],data[0],data[1],'0'))
                i += 1
        except:
            pass
    
    #Carga Masiva Enfermeras
    def cargamasivaEnf(self,data):
        try:
            fila = re.split('\n',data)
            i=1
            while i < len(fila):
                campo = re.split(',',fila[i])
                compFecha = re.split('/',campo[2])
                fecha = compFecha[2]+"-"+compFecha[1]+"-"+compFecha[0]
                telefono='Sin registrar'
                try:
                    if campo[6] != '':
                        telefono = campo[6]
                except:
                    pass
                self.usuarios.append(Usuario('enfermera',campo[4],campo[5]))
                self.enfermeras.append(Enfermera(campo[0],campo[1],fecha,campo[3],campo[4],campo[5],telefono))
                i += 1
        except:
            pass

    #Carga Masiva Pacientes
    def cargamasivaPac(self,data):
        try:
            fila = re.split('\n',data)
            i=1
            while i < len(fila):
                campo = re.split(',',fila[i])
                compFecha = re.split('/',campo[2])
                fecha = compFecha[2]+"-"+compFecha[1]+"-"+compFecha[0]
                telefono='Sin registrar'
                try:
                    if campo[6] != '':
                        telefono = campo[6]
                except:
                    pass
                self.usuarios.append(Usuario('paciente',campo[4],campo[5]))
                self.pacientes.append(Paciente(campo[0],campo[1],fecha,campo[3],campo[4],campo[5],telefono))
                i += 1
        except:
            pass

    #Carga Masiva Medicamentos
    def cargamasivaMed(self,data):
        try:
            fila = re.split('\n',data)
            i=1
            while i < len(fila):
                campo = re.split(',',fila[i])
                self.medicamentos.append(Medicamento(campo[0],campo[1],campo[2],campo[3]))
                self.medMasV.append(MasVendidosMed(campo[0],campo[2],'0'))
                i += 1
        except:
            pass

    #Agregar al Pedido
    def agregar_pedido(self,usuario,medicamento,descripcion):
        for i in self.medicamentos:
            if i.nombre == medicamento and i.descripcion == descripcion:
                cant = int(i.cantidad)
                cant -= 1
                self.medicamentos[self.medicamentos.index(i)] = Medicamento(i.nombre,i.precio,i.descripcion,cant)
                self.pedidos.append(Pedido(self.generar_codigo(),usuario,i.nombre,i.precio,1,i.descripcion))
                return '{"estado":"agregado"}'

    #Quitar del Pedido
    def quitar_pedido(self,usuario,codigo):
        for i in self.pedidos:
            if i.usuario == usuario and i.codigo == codigo:
                for j in self.medicamentos:
                    if j.nombre == i.medicamento and j.descripcion == i.descripcion:
                        cant1 = int(i.unidades)
                        cant2 = int(j.cantidad)
                        cant2 += cant1
                        self.medicamentos[self.medicamentos.index(j)] = Medicamento(j.nombre,j.precio,j.descripcion,cant2)
                        self.pedidos.remove(i)
                        return '{"estado":"quitado"}'

    #Agregar Unidades
    def agregar_unidad(self,codigo,usuario):
        try:
            for i in self.pedidos:
                if i.usuario == usuario and i.codigo == codigo:
                    for j in self.medicamentos:
                        if int(j.cantidad) > 0:
                            if j.nombre == i.medicamento and j.descripcion == i.descripcion:
                                cant1 = int(i.unidades)
                                cant1 += 1
                                cant2 = int(j.cantidad)
                                cant2 -= 1
                                self.medicamentos[self.medicamentos.index(j)] = Medicamento(j.nombre,j.precio,j.descripcion,cant2)
                                self.pedidos[self.pedidos.index(i)] = Pedido(i.codigo,i.usuario,i.medicamento,i.precio,cant1,i.descripcion)
                                return '{"estado":"agregado"}'
            return '{"estado":"agotado"}'
        except:
            pass

    #Quitar Unidades
    def quitar_unidad(self,codigo,usuario):
        try:
            for i in self.pedidos:
                if i.usuario == usuario and i.codigo == codigo:
                    for j in self.medicamentos:
                        if int(i.unidades) > 0:
                            if j.nombre == i.medicamento and j.descripcion == i.descripcion:
                                cant1 = int(i.unidades)
                                cant1 -= 1
                                cant2 = int(j.cantidad)
                                cant2 += 1
                                self.medicamentos[self.medicamentos.index(j)] = Medicamento(j.nombre,j.precio,j.descripcion,cant2)
                                self.pedidos[self.pedidos.index(i)] = Pedido(i.codigo,i.usuario,i.medicamento,i.precio,cant1,i.descripcion)
                                return '{"estado":"agregado"}'
        except:
            pass

    #Realizar Cobro
    def cobrar(self,codigo,usuario):
        for i in self.pedidos:
            if i.codigo == codigo and i.usuario == usuario:
                for j in self.medMasV:
                    if j.nombre == i.medicamento and j.descripcion == i.descripcion:
                        cant1 = int(j.unidadesV)
                        cant2 = int(i.unidades)
                        cant1 += cant2
                        self.medMasV[self.medMasV.index(j)] = MasVendidosMed(i.medicamento,i.descripcion,cant1)
                self.pedidos.remove(i)
                return '{"estado":"cancelado"}'

    #Generador Código de Pedido
    def generar_codigo(self):
        mayusculas = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        minusculas = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        simbolos = ['#','$','&','-','_','(',')','|','*','¿','?','¡','!']
        numeros = ['1','2','3','4','5','6','7','8','9','0']
        caracteres = mayusculas + minusculas + simbolos + numeros
        codigo = []
        for i in range(20):
            caracter_random = random.choice(caracteres)
            codigo.append(caracter_random)
        return ''.join(codigo)

    #Agregar Cita
    def agregar_cita(self,usuario,fecha,hora,motivo):
        if self.verificar_cita(usuario):
            self.citas.append(Cita(usuario,fecha,hora,motivo,'','','Pendiente'))
            return '{"solicitud":"enviado"}'
        return '{"solicitud":"enProceso"}'

    def verificar_cita(self,usuario):
        for i in self.citas:
            if i.usuario == usuario:
                return False
        return True

    #Ordenamiento
    def ordenamientoVentas(self,lista):
        n = len(lista)
        for i in range(n):
            for j in range(0,n-i-1):
                if int(lista[j].unidadesV) < int(lista[j+1].unidadesV):
                    lista[j],lista[j+1] = lista[j+1],lista[j]
        return lista

    def ordenamientoDoctoresCitas(self,lista):
        n = len(lista)
        for i in range(n):
            for j in range(0,n-i-1):
                if int(lista[j].citasAt) < int(lista[j+1].citasAt):
                    lista[j],lista[j+1] = lista[j+1],lista[j]
        return lista

    def ordenamientoEnfermedades(self,lista):
        n = len(lista)
        for i in range(n):
            for j in range(0,n-i-1):
                if int(lista[j].casos) < int(lista[j+1].casos):
                    lista[j],lista[j+1] = lista[j+1],lista[j]
        return lista

    #Vitácora enfermedad
    def registrar_enfermedad(self,enfermedad):
        if self.verificar_enfermedad(enfermedad):
            for i in self.topEnfermedad:
                if i.enfermedad == enfermedad:
                    casosH = int(i.casos)
                    casosH += 1
                    self.topEnfermedad[self.topEnfermedad.index(i)] = EnfComun(i.enfermedad,casosH)
                    return '{"casos":"nuevo"}'
        else:
            self.topEnfermedad.append(EnfComun(enfermedad,'1'))
            return '{"casos":"primero"}'
        

    def verificar_enfermedad(self,enfermedad):
        for i in self.topEnfermedad:
            if i.enfermedad == enfermedad:
                return True
        return False