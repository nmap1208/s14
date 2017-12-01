#Auther nmap
def file_db_handle(database):
    db_path='%s/%s' %(database['path'],database['name'])
    return db_path

def handle(database):
    if database['db_tool']=='file_storage':
        db_path=file_db_handle(database)
        return db_path
