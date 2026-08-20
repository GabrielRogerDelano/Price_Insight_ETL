import config
from transform import transform
from load import load
from models import Product, User

products_columns = ['id', 'title', 'price', 'category', 'rating.rate', 'rating.count']
products_mapping = {
    "id": "id",
    "title": "title",
    "price": "price",
    "category": "category",
    "rating": "rating.rate",
    "reviews": "rating.count"
}

users_columns = ["id", "address.city", "email", "name.firstname", "name.lastname"]
users_mapping = {
    "id":"id",
    "address_city": "address.city",
    "email": "email",
    "firstname": "name.firstname",
    "lastname": "name.lastname"
}

def carregar_produtos():
    df = transform(f"{config.BASE_URL_API}/products", products_columns)

    try:
        load(df, Product, products_mapping)
        print('Produtos carregados com sucesso!')
        
    except:
        print('\033[31mFalha ao carregar produtos!\033[0m')

def carregar_usuarios():
    df = transform(f"{config.BASE_URL_API}/users", users_columns)

    try:
        load(df, User, users_mapping)
        print('usuarios carregados com sucesso!')
    except:
        print('\033[31mFalha ao carregar usuarios!\033[0m')

if __name__ == "__main__":
    carregar_produtos()
    carregar_usuarios()