# PROYECTO SISTEMA DE INVENTARIO y VENTAS MS (SIV)
_Sistema de Inventario y Ventas MotoSocios_

*DESCRIPCIÓN FUNCIONAL DEL PROYECTO*   
   Este proyecto busca dar solución al siguiente problema planteado para la materia Desarrollo de Software I 
   De la Universidad del Valle 
   Realizado en el primer semestre del año 2022
  
Se debe desarrollar un producto de software para administrar el inventario y las ventas de un almacén de moto partes “MOTOSOCIOS”. Además de esto se debe realizar una base de datos para la administración de datos de dicho almacén, los que se entienden como todos los datos concernientes al sistema de inventario y ventas.
Características Funcionales del almacén: 
El almacén cuenta con varios requerimientos funcionales:
En estas, se requiere tener un control de los clientes, registrándose en el sistema con los siguientes datos: Nombre, NIT o identificación, Número de contacto, Dirección, Tipo de cliente (habitual o esporádico), como también se cuenta con un sistema de crédito se debe incluir si el cliente cuenta con crédito, se desean conocer los datos del crédito, este mismo lo componen No. Crédito, Fecha de aprobación, cuotas a pagar, y total del valor que se ha dado en crédito, además de esto dado que un cliente puede adquirir varios de los productos que se ofrecen en el almacén, se requiere además tener los datos de facturación, los cuales están compuestos de: Número único de facturación, Datos del almacén los cuales solo son información sobre el almacén (Nombre, NIT, número de contacto y dirección), Datos del día (Fecha, hora), Datos del cliente (nombre y NIT o documento de identificación único), Datos del producto (Nombre, cantidad y valor), Datos del pago, efectivo o crédito y datos del pago (Si el valor fue cancelado con más dinero debe mostrar las devueltas entregadas). Con base en esto también es necesario almacenar los datos de los productos que se venden, datos tales como: Nombre del producto, Número del código de barras del producto, Categoría del producto, que varía en 4 tipos, y que tiene como restricción que los productos solo pueden pertenecer a una sola categoría, las cuales son: partes eléctricas, partes mecánicas, piezas estéticas, y piezas varias. Por último, teniendo en cuenta que el almacén cuenta con varios proveedores, es importante saber los datos de estos, además de que productos son comprados a ellos, ya que a un proveedor se le puede comprar uno o varios productos, y un producto puede ser comprado a varios proveedores, teniendo como base esto, los datos solicitados a almacenar son los siguientes: Nombre del proveedor (persona o empresa), NIT del proveedor, Dirección del proveedor, Numero de contacto del proveedor, Productos que son comprados a los proveedores.
Por último, ya que el almacén cuenta con varios cargos, de los cuales un empleado solo puede desempeñar un  único cargo, se requiere registrar la información de los empleados, para llevar un control de los mismos, en base a esto, los datos a guardar son: Nombre del empleado (que se compone de nombre y apellido), Cargo, Número de identificación, Sueldo que recibe, Numero de contacto y Dirección.
Como se mencionó anteriormente, almacén de moto partes “MOTOSOCIOS” posee varias categorías según sus productos: partes eléctricas, partes mecánicas, piezas de lujo, y tornillería. También tiene varios tipos de cliente: habituales y esporádicos, los clientes frecuentes, también pueden ser clientes corporativos o personas naturales.  
  
Además de esto tenemos que una venta está determinada por los datos del cliente, la categoría del producto incluido en la venta, el nombre del producto, la fecha de venta, la cantidad de elementos individuales, el total de artículos en la venta, el valor final de venta, y el valor de descuento si aplica en la venta.  

Para esto, el almacén cuenta con unos cargos:

El vendedor del almacén debe poder hacer las siguientes operaciones:  
Obtener un listado de los productos disponibles de acuerdo con su categoría.
Preguntar por el precio de un producto.
Preguntar la cantidad de productos adquiridos por un cliente.
Preguntar por el descuento ofrecido a los clientes frecuentes (si han superado 10 productos adquiridos y que además superen un monto de $100.000, el descuento solo aplica al 15% del valor).
Consultar estado de créditos.
Dar productos a crédito a clientes habituales que cumplan un mínimo de 4 compras que superen un total de $400.000.
Preguntar por el precio total para un cliente dado, especificando su número de identificación, tipo de productos y cantidad de productos.  
Reservar productos, especificando su número identificador y la identificación del cliente.  
Realizar el registro de cada cliente cuando adquiere un producto.
Recaudar el pago de los créditos. 
Por otro lado, el personal de bodega podrá usar la aplicación desarrollada para:
Crear nuevos productos.
Agregar nuevos productos a una categoría.
Actualizar la cantidad de productos individuales.
Así mismo, el Administrador, debe poder usar la aplicación desarrollada para:
Cambiar el porcentaje de incremento en el precio de venta de un producto. 
Cambiar los plazos máximos en los que se da un crédito.
Cambiar el valor de compra de un producto.
Conocer el total de productos en el inventario
Crear una nueva compra (la cual debe contar con un consecutivo único de compra, un valor total de compra, el nombre de los elementos que compra, la cantidad individual de elementos que compra, y los datos del proveedor, tales como teléfono, dirección, nit y nombre).
Poder modificar ventas realizadas por un vendedor.
Crear perfiles de empleados.

Por último, el contador podrá usar la aplicación desarrollada para: 
Consultar el histórico de ventas del mes.
Consultar el histórico de compras del mes.
Consultar los datos de los empleados.
Crear pagos a empleados (los cuales constan de un consecutivo único de pago, el nombre del empleado al que corresponde, el cargo que desempeña, y el total de días pagos).
Crear pagos a distribuidores (los cuales constan de un consecutivo único de pago, el consecutivo único de compra, el nombre de la empresa a la que se realiza el pago y el total a pagar).

Cuando una persona llegue a realizar una compra se debe verificar si el producto que requiere está en stock, y su precio de venta; Si el cliente decide comprar el producto se procede a hacer un registro del cliente, si el cliente está registrado se verifica si el cliente es frecuente y si aplican descuentos en su compra.

Los clientes que cuenten con crédito en el almacén pueden consultar datos como: monto total de la deuda, cuotas restantes, fecha de inicio del crédito, productos solicitados en el inicio del crédito. Que deberán ser consultados en el almacén y que pueden ser consultados por cualquier empleado del almacén.

Además de esto cada venta debe generar una factura la cual, puede ser de dos categorías, crédito o contado, si la factura se genera con crédito, esta factura servirá para el pago de las cuotas de este, por su número de identificación único.

Perfiles de usuario y Privilegios  

Por razones de seguridad en el manejo de la información se deben crear diferentes perfiles de usuario y cada perfil tiene unos privilegios asignados.  

*Perfil Vendedor:* Tiene privilegios para crear clientes, visualizar la información registrada por otros usuarios.

*Perfil Bodega:* Tiene permisos para registrar productos y crear nuevas entradas de productos.  

*Perfil Contador:* Tiene permisos para realizar consultas de estados, crear pagos e informes.  

*Perfil Administrador:* Tiene privilegios para gestionar usuarios, clientes. También tiene acceso a las tareas de los demás perfiles.

