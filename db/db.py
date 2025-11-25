import psycopg

conn = None

try:
    conn = psycopg.connect(
        dbname="system_inventory",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432",
    )

    print("connetion is exit")

    # with conn.cursor() as cur:
    #     cur.execute("""
    #         create table products (
    #           id bigint primary key generated always as identity,
    #           name text,
    #           purchase_cost numeric,
    #           shipping_cost numeric,
    #           sale numeric,
    #           profits numeric
    #         );""")

    # print("table is create exit")

except Exception as err:
    print(f"error in db:{err}")
