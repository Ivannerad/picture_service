import psycopg2


conn = psycopg2.connect(dbname='postgres', user='postgres', password='password', host='localhost', port=5432)
cur = conn.cursor()


def db_get_list(extension=None):
    if not extension:
        query = '''SELECT extension.name as extension, images.name as name FROM extension 
                   LEFT JOIN images ON extension.id=images.extension_id'''
        cur.execute(query)
    else:
        query = """SELECT extension.name as extension, images.name as name FROM images 
                   LEFT JOIN extension ON extension.id=images.extension_id
                   WHERE extension_id = (SELECT id FROM extension WHERE name=%s)"""
        cur.execute(query, (extension,))
    records = cur.fetchall()

    res = {}
    if records:
        for record in records:
            img_extension, img_name = record
            if img_extension not in res:
                res[img_extension] = [img_name]
            else:
                res[img_extension].append(img_name)
        if extension:
            res = res[extension]
    return res


def db_create_extension(extension):
    cur.execute('INSERT INTO extension (name) VALUES (%s)', (extension, ))
    conn.commit()


def db_delete_list(extension):
    cur.execute("DELETE FROM extension WHERE name = %s", (extension, ))
    conn.commit()


def db_create_image(extension, name):
    query = 'INSERT INTO images (extension_id, name) VALUES ((SELECT id FROM extension WHERE name=%s), %s)'
    cur.execute(query, (extension, name))
    conn.commit()
