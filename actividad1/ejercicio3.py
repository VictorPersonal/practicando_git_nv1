import sys
#Importando sys
descuento=float(input("Ingrese el descuento. tenga en cuenta que lo debe colocar como decimal: 19% --> 0.19: "))
valor=int(input("Ingrese el precio: "))
valorDec=(valor*descuento)/1.0
total=valor-valorDec
print("el valor correspondiente al porcentanje ingresado dentro del precio/producto es: {}".format(valorDec))
print("El valor original es: {}".format(total))
print("El peso de la variable del descuento es: ", sys.getsizeof(descuento))
print("El peso de la variable del precio del producto",sys.getsizeof(valor))
print("El peso del valor que se descontará o restará del valor original es: ",sys.getsizeof(valorDec))
print("El peso de la variable del valor original del producto es",sys.getsizeof(total))