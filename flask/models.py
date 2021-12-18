from sqlalchemy import create_engine
import pandas as pd
engine = create_engine('postgresql+psycopg2://postgres:postgres@postgres:5432/postgres')
conn = engine.connect()

class get_data():
    def __init__(self, uid:int, prodid:int, storeid:int) -> None:
        self.uid = uid
        self.prodid = prodid
        self.storeid = storeid
    def df(self):
        query = """ select u."name" as user_name
                            ,st."name" as store_name
                            ,p."name" as product_name
                            ,s.date_sale
                            ,s.amount
                    from sale s
                    left join store st on s.store_id = st.store_id
                    left join product p on s.product_id = p.product_id
                    left join users u on s.user_id = u.user_id
                    where s.user_id = {}""".format(self.uid)
        df = pd.read_sql(query, engine)
        result = df.to_json(orient='records')
        return result

conn.close()



