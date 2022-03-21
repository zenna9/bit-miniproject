import pymysql
# free = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='bit123', db='free', charset='utf8')
# cursor = free.cursor(pymysql.cursors.DictCursor)
# cursor.execute()


def children():
    free = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='bit123', db='free', charset='utf8')
    cursor = free.cursor(pymysql.cursors.DictCursor)

    child = []
    # for i in range(len(table)):
    #     if '01' in table['target2_code'].iloc[i]:
    #         child.append(table['name'].iloc[i])
    cursor.execute("""
    SELECT idx FROM stores
    WHERE target2_code LIKE concat('%', 1, '%')
    """)

    result = cursor.fetchall()
    # print(result)
    for i in range(len(result)):
        child.append(result[i]['idx'])

    return child


def old():
    free = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='bit123', db='free', charset='utf8')
    cursor = free.cursor(pymysql.cursors.DictCursor)

    old = []
    cursor.execute("""
    SELECT idx FROM stores
    WHERE target2_code LIKE concat('%', 2, '%')
    """)

    result = cursor.fetchall()
    print(result, type(result))
    for i in range(len(result)):
        old.append(result[i]['idx'])

    return old


def firefighter():
    free = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='bit123', db='free', charset='utf8')
    cursor = free.cursor(pymysql.cursors.DictCursor)

    fire = []
    cursor.execute("""
    SELECT idx FROM stores
    WHERE target2_code LIKE concat('%', 99, '%')
    """)

    result = cursor.fetchall()
    print(result, type(result))
    for i in range(len(result)):
        fire.append(result[i]['idx'])

    return fire


# print(children())
# print(old())
# print(firefighter())
