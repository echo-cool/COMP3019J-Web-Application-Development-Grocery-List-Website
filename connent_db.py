from app import app

app = app.create_app()
app.app_context().push()
from app.extensions import db

print("############################################")
print("Init Finished")
print("Create db: db.create_all()")
print("Drop   db: db.drop_all()")
print("Engine   : " + str(db.get_engine()))
print("############################################")
while True:
    try:
        print(eval(input("Command: ")))

    except KeyboardInterrupt:
        exit()

    except Exception as e:
        print(e.args)
