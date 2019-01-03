from populate import base
from products.models import Products,two

def populate():
    print('Populating articles and comments ... ', end='')
    Products.objects.all().delete()
    two.objects.all().delete()


    
    
if __name__ == '__main__':
    populate()