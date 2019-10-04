from pizzapy.customer import Customer
from pizzapy.store import StoreLocator
from pizzapy.menu import Menu
from pizzapy.order import Order

customer = Customer('Samir', 'Ingle', 'samir.ingle@students.makeschool.com', '4088052279', '855 California Street, San Francisco, CA, 94108')
#print(customer)

my_local_dominos = StoreLocator.find_closest_store_to_customer(customer)
#print(f'Local Store: {my_local_dominos}')

menu = my_local_dominos.get_menu()
#menu.search(Name='Brooklyn') #Pizza #P14IBKCZ 6 cheese #P14IBKUH Large (14") Brooklyn Honolulu Hawaiian $18.99

order = Order.begin_customer_order(customer, my_local_dominos)
#order.remove_item('20BCoke')

card = CreditCard('asdlfkj', 'exp', 'sec', 'zip')

def OrderUp(orde, car, custome, my_local_domino)
    order = Order.begin_customer_order(custome, my_local_domino)
    order.place(car)
    my_local_dominos.place_order(orde,car)


#OrderUp(order, card, customer, my_local_dominos)
