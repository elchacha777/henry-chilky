from peewee import *






db_psql = PostgresqlDatabase(database='postgres', user='postgres', password='password', host='postgres_host', port=5432)
class Emails(Model):
    email = CharField()
    password = CharField()

    class Meta:
        database = db_psql


def save_email(email, password):
    obj = Emails(email=email, password=password)
    obj.save()


def get_all_emails():
    count = Emails.select().count()
    return count


def get_email(id=id):
    email = Emails.get(Emails.id == id)
    return (email.email, email.password)


def create_table():
    try:
        with db_psql.atomic():
            db_psql.create_tables([Emails])
    except:
        pass

def drop_table():
    try:
        with db_psql.atomic():
            db_psql.drop_tables([Emails])
    except:
        pass



if __name__ == '__main__':
    drop_table()
    create_table()





    with open('data.txt', 'r+') as file:
        lines = file.readlines()
        for line in lines:
            string = line.replace('\n', '')
            lst = string.split(' ')
            res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst)-1)}
            for email, password in res_dct.items():
                save_email(email, password)



