class Carro:  # Definición de la clase Carro
    def __init__(self, request):  # Método constructor que inicializa la clase
        self.request = request  # Asigna el parámetro request al atributo request de la instancia
        self.session = request.session  # Obtiene la sesión desde el objeto request y la asigna a session
        carro = self.session.get("carro")  # Intenta obtener el carro de la sesión

        if not carro:  # Si no hay un carro en la sesión
            carro = self.session["carro"] = {}  # Crea un nuevo diccionario vacío y lo asigna a carro en la sesión
        #else:  # Si hay un carro en la sesión
        self.carro = carro  # Asigna el carro de la sesión al atributo carro de la instancia

    def agregar(self, producto):  # Definición de la función agregar que toma un producto como argumento
        if (str(producto.id) not in self.carro.keys()):  # Comprueba si el ID del producto no está en las llaves del carro
            self.carro[producto.id] = {  # Si el producto no está en el carro, lo agrega
                'producto_id': producto.id,  # ID del producto
                'nombre': producto.nombre,  # Nombre del producto
                'precio': str(producto.precio),  # Precio del producto convertido a cadena
                'cantidad': 1,  # Cantidad del producto inicializada en 1
                'imagen': producto.imagen.url,  # URL de la imagen del producto
            }
        else:  # Si el producto ya está en el carro
            for key, value in self.carro.items():  # Itera sobre cada par clave-valor en el carro
                if key == str(producto.id):  # Si la clave coincide con el ID del producto
                    value["cantidad"] = value["cantidad"] + 1
                    value["precio"]=float(value["precio"])+producto.precio   # Incrementa la cantidad del producto en 1
                    break  # Sale del bucle después de actualizar la cantidad

        self.guardar_carro()  # Llama al método guardar_carro() para guardar los cambios en el carro
        
    def guardar_carro(self): # Función para guardar los cambios del carro
        self.session["carro"]=self.carro # Verificamos que el el carro este con su contenido 
        self.session.modified=True # Modificamos el carro 
        
    def eliminar(self, producto): # Función para eliminar un producto.
        producto.id=str(producto.id)  # Verificamos el id del producto y lo convertimos a un STR para la verificación.
        
        if producto.id in self.carro:   # Verificamos si el producto esta en el carro.
            del self.carro[producto.id] # Si el producto está, el producto se elimina según su id.
            self.guardar_carro() # Invocamos la función guardar para realizar los cambios.
    
    def restar(self, producto): # Creamos una función para restar un producto.
        for key,value in self.carro.items(): # Inicializamos un iterador para recorrer los items del carro.
            if key == str(producto.id): # Validamos que la llave sea igual que el id.
                value["cantidad"]= value["cantidad"]-1 # Si la llave coincide con el id, le restamos -1 un producto
                if value["cantidad"]<1: # Si la cantidad queda menor a 1, el producto se eliminará del carrito.
                    self.eliminar(producto) # Invocamos la función eliminar y le pasamos el parametro producto.
                    break # Y detenemos el proceso.
        self.guardar_carro() # Invocamos la función guardar, para realizar los cambios satisfactoriamente si es que se hay.
        
    def limpiar(self): #Función para vaciar el carrito.
        self.session["carro"]={} # Le especificamos que en la sessio el carro va ser igual a vacío.
        self.session.modified=True # Y hacemos la modificación del objecto.