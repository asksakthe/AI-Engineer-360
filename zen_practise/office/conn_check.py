import yaml
from pathlib import Path

def readYaml(fileNext):
    p = Path(fileNext)

    with p.open('r',encoding='utf-8') as foo:
        data = yaml.safe_load(foo)
        return data
    

yamlFile = 'con.yaml'
data = readYaml(yamlFile)

db_list = data.get('database',[])

if db_list:
    first_item = db_list[0]
    dbName = first_item.get('name','local')
    dbport = first_item.get('name',343)
    sec_item = db_list[1]
    appName = sec_item.get('name','local')
    appport = sec_item.get('port', 89)

    print(dbName ,'&', dbport)
    print(f"This is appname: {appName}")


    
