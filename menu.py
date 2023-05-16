#en este menu llamaremos a las clases. 
#clase cliente tiene los siguientes atributos: nombre, edad, direccion, email.

from clases import Cliente

cliente1 = Cliente("Rene", 29, "Calle 20, Santiago", "rene@gmail.com")

cliente2 = Cliente("Francisca", 25, "Calle 123, Temuco","hola123@email.com" )


cliente1.comprar("Audifonos")  # ejemplo de hacer una compra

cliente1.actualizar_email("juanlopez@gmail.com")  # ejemplo de actualizar email

print(cliente1) # imprime el nombre del cliente usando el metodo __str__

