class CuentaBancaria:
    def __init__(self, titular, nroCuenta, saldo):
        self.titular=titular
        self.nroCuenta=nroCuenta
        self.saldo=saldo
    def depositar(self, dinero):
        if dinero<=0:
            print("Error: el depósito debe ser mayor a 0")
        else:
            self.saldo=self.saldo+dinero
            print("Depósito realizado")
    def retirar(self, dinero):
        if dinero>self.saldo:
            print("Error: no tiene suficiente dinero")
        else:
            self.saldo=self.saldo-dinero
            print("Retiro realizado")
    def mostrarDatos(self):
        print("Titular:", self.titular)
        print("Número de cuenta:", self.nroCuenta)
        print("Saldo:", self.saldo)
cuenta = CuentaBancaria("Raqi", "280108", 1000)
cuenta.mostrarDatos()
cuenta.depositar(500)
cuenta.retirar(200)
cuenta.depositar(0)
cuenta.retirar(2000)
cuenta.mostrarDatos()