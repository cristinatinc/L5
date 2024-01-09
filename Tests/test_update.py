from Modelle.Kunde import Customer
from Repository.CustomerRepo import CustomerRepo

test_update_customer = Customer(12,'Carla', 'Bucuresti')
test_update_cust_repo = CustomerRepo('test_update_file.txt')
test_update_cust_repo.create(test_update_customer)
cust1 = Customer(12, 'Carla', 'Hasdeu')

def test_update_customer():
    test_update_cust_repo.update(12, new_address='Hasdeu')
    assert test_update_cust_repo.read()[0] == cust1