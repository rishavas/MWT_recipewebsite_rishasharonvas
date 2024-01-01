from sqlalchemy import create_engine
from sqlalchemy import text

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
print(engine)

def create_recipe_table(engine):
    with engine.connect() as conn:
        conn.execute(text("CREATE TABLE recipe_list (id integer primary key autoincrement, title text, ingredients text)"))
        conn.commit()

def insert_recipe(engine,title,ingredients):
    with engine.connect() as conn:
        conn.execute(text("INSERT INTO recipe_list (title, ingredients) VALUES (:title, :ingredients)"),
        [{"title": title, "ingredients": ingredients}],)
        conn.commit()


def read_recipes(engine):
    with engine.connect() as conn:
        result=conn.execute(text("select * from  recipe_list"))
    print(result)
    return result

def update_recipes(engine,id,title,ingredients):
    with engine.connect() as conn:
        conn.execute(text("update recipe_list set title=:title, ingredients=:ingredients where id=:id"),
                     [{"title":title,"ingredients":ingredients,"id":id}])
        conn.commit()

def delete_recipes(engine,id):
    with engine.connect() as conn:
        conn.execute(text("delete from recipe_list where id=:id"),
                     [{"id":id}])
        conn.commit()

# create_recipe_table(engine)
# print("table created")
# ingredients="""a cup of water and 2 tbdhwhfcheiy
# nckjscjsiji
# kjck"""
# insert_recipe(engine,"maggi",ingredients)
# print("inserted rows")
# result=read_recipes(engine)
# for row in result:
#     id=row.id
#     print(row.id)
#     print(row.title)
#     print(row.ingredients)
# print("reading...")
# delete_recipes(engine,id)
# print("deleted")
