import d_PersonClass as p

def main():
    name = 'John'
    address = '123 Main'
    phoneNumber = '555-555-5555'
    on_list_flag = False


person1 = p.Person(name,address,phoneNumber)

customer1 = p.Customer(name,address,phoneNumber, cust_number)


person1.print_person()

customer1.print_person()


main()