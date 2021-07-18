from Cargos import Cargo
class Empleado:
    secuencia=0
    def __init__(self,nom, ced, sue,carg):
        self.codigo= self.generarCodigo()
        self.nombre=nom
        self.cedula=ced
        self.sueldo=sue
        self.cargo=carg
    
    def mostrar(self):
        print("Codigo: {} nombre:{} cargo:{}-{}" .format(self.codigo, self.nombre, self.cargo.codCarg, self.cargo.descripCarg))
    
    def generarCodigo(self):
        Empleado.secuencia+=1
        return Empleado.secuencia

cargo1= Cargo("Docente")
emp1= Empleado("Daniel", "0914", 500, cargo1)
emp1.mostrar()
cargo2= Cargo("Programadora")
emp2= Empleado("María", "0915", 500, cargo2)
emp2.mostrar()