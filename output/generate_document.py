import pandas as pd


def generate_document(products: list):
    list_product = []

    for index, item in enumerate(products, start=1):
        name, purchase_cost, shipping_cost, sale, profits = item

        list_product.append(
            {
                "id": index,
                "name": name,
                "purchase_cost": purchase_cost,
                "shipping_cost": shipping_cost,
                "sale": sale,
                "profits": profits,
            }
        )

    datos = pd.DataFrame(list_product)

    try:
        datos.to_excel("files/user_file.xlsx", index=False)
        print("create the exel is exit")

    except Exception as err:
        print(err)
