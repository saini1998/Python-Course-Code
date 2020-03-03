# Absolute import
from ecommerce.customer import contact
# Relative import
from ..customer import contact

# Executing Modules as Scripts
print("Sales Initialised", __name__)

contact.contact_customer()


def calc_tax():
    pass


def calc_shipping():
    pass


if __name__ == "__main__":
    print("sales started")
