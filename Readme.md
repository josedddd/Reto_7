# Este es el reto 7

Aqui describo como siempre todo: 

1. Usar las fifo. Como se puede ver creo una clase que me maneje ordenes simultaneas (como si fuese un restaurante de verdad), y uso una fila FIFO para realizar esto (uso la que ya esta en python)
```python

class Manage_orders:
    def __init__(self):
        self.list_orders=[]

    
    def add_list_orders(self, order:Order):
        self.list_orders.append(order)


    def manage_order(self):
        cola_fifo=Queue(maxsize=15)
        for order in self.list_orders:
            cola_fifo.put(order)
        
        if cola_fifo.full():
            print("La cola esta llena, por favor esperar")
        
        while not cola_fifo.empty():
            order_removida=cola_fifo.get()
            print ("Enviando orden a cocina ",order_removida.show_order())

```
2. Usar las named tuple en algun lado:
Esto se puede ver aca, donde para guardar los items que se agregan a la orden uso este tipo de dato, el cual es muy conveniente, porque antes solo usaba una tupla normal (sin nombre)
```python

   def __init__(self, number):
        self.number = number
        self.order = []

    def add_items(self, menu_item: MenuItem, quantity: int) -> list:
        prod = namedtuple (f"Orden{self.number}",["prducto","cantidad"]) ##Aqui esta la named tuple, la uso para añadir los objetos al menu
        product= prod( 
            menu_item,
            quantity        
        )
        self.order.append(product)
```
3. Crear las interfaces de menu en una nueva clase (me parece mas logico que hacerlo en la clase orders), Cabe aclarar que esto solo crea el menu, todo lo demas de orders, no funcionaria porque toda la demas logica esta hecha con el menu con las instancias de clase MenuItem (Mucha de la logica se romperia, y tocaria cambiar demasiadas cosas, para eso me hubieran dicho antes v:) 
