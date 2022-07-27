import requests
import json

data = []

def get_data():
    product_count = 1
    total_variant = 1

    for page in range(1, 4):
        r = requests.get(url=f'https://www.allbirds.com/products.json?limit=250&page={page}')

        if r.status_code == 200:

            products = r.json()['products']
            for product in products:
                id = product['id']
                title = product['title']
                product_type = product['product_type']
                description = product['body_html'].replace('<p>', '').replace('</p>', '')
                published_at = product['published_at']
                vendor = product['vendor']
                for variant in product['variants']:
                    item = {
                        'id': id,
                        'title': title,
                        'product_type': product_type,
                        'description': description,
                        'published_at': published_at,
                        'vendor': vendor,
                        'var_id': variant['id'],
                        'var_title': variant['title'],
                        'sku': variant['sku'],
                        'price': variant['price'],
                        'available': variant['available'],
                        'created_at': variant['created_at'],
                        'updated_at': variant['updated_at']
                    }

                    data.append(item)

                    total_variant += 1

                print(f'[!] Product #{product_count} was completed!')
                product_count += 1

        else:
            print(f'Error! Status Code: {r.status_code}')

    print(f'Total_count - {total_variant}')


def main():
    get_data()

    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    main()

