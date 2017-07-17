import sqlite3

FETCH_DATA = 'SELECT * FROM {}'


def get_data(table, path):
    """
    :param table: Tablename that contains the data
    :param path: Path to database
    :return:
    """
    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute(FETCH_DATA.format(table))

    result = []

    for row in cursor.fetchall():
        result.append(row)
    cursor.close()
    connection.close()
    return result

