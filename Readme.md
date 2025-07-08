# Este es el reto 7

Aqui describo como siempre todo: 

1. Usar las fifo. Como se puede ver creo una clase que me maneje las ordenes, y uso una fila FIFO para realizar esto (uso la que ya esta en python)
2. python
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
