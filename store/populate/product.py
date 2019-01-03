from populate import base
from products.models import Products

def populate():
    print('Populating articles and comments ... ', end='')
    Products.objects.all().delete()


    
    
if __name__ == '__main__':
    populate()