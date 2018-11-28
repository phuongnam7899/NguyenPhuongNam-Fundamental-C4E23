import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds249503.mlab.com:49503/c4e23-vlog

host = "ds249503.mlab.com"
port = 49503
db_name = "c4e23-vlog"
user_name = "admin"
password = "admin1"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())