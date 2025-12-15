import psycopg

conn = None

try:
    conn = psycopg.connect(
       "postgresql://system_inventory_user:IsxphiBUxU2Dmv5vNvTU2BWwubHTdFUi@dpg-d500f9d6ubrc73a5p8eg-a.oregon-postgres.render.com/system_inventory"       
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

    print("table is create exit")

except Exception as err:
    print(f"error in db:{err}")
