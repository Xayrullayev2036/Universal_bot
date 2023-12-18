import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()



class DB:
    con  = psycopg2.connect(
    dbname = os.getenv('DB_NAME'),
    user = os.getenv('DB_USER'),
    password  = os.getenv('DB_PASSWORD'),
    host = os.getenv('DB_HOST'),
    port = "5432"
    )

    cur = con.cursor()

    def select(self,*args):
        fields = ''.join(args) if args else "*"
        table_name = self.__class__.__name__.lower()
        query = f"select {fields} from {table_name}"
        self.cur.execute(query)
        return self.cur


    def insert_into(self,**kwargs):
        fields = ', '.join(kwargs.keys())
        table_name = self.__class__.__name__.lower()
        param = tuple(kwargs.values())
        query = f"""insert into {table_name}({fields}) values({','.join(['%s']*len(param))})"""
        self.cur.execute(query,param)
        self.con.commit()

    def update(self, **kwargs):
        w = list(self.fields.keys())
        w.append(" ")

        table_name = self.__class__.__name__.lower()
        f = list(kwargs.keys())
        f.append(' ')

        set_fields = " = %s,".join(f).strip(', ')
        where_fields = " = %s and ".join(w).strip('and ')

        params = list(kwargs.values())
        params.extend(list(self.fields.values()))

        query = f"""update {table_name} set {set_fields} where {where_fields}"""
        self.cur.execute(query, params)
        self.con.commit()


    def delete(self,**kwargs):
        f = list(kwargs.keys())
        f.append(' ')
        fields = ' =%s,'.join(f).strip(', ')
        param = tuple(kwargs.values())
        table_name = self.__class__.__name__.lower()
        query = f"delete from {table_name} where {fields}"
        self.cur.execute(query,param)
        self.con.commit()
