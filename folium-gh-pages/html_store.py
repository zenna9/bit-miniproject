def popup_html(index, df):
    i = df.index[df['idx'] == index].tolist()
    text1 = df['name'].iloc[i[0]]
    text2 = df['idx'].iloc[i[0]]
    text3 = df['img_src'].iloc[i[0]]
    text4 = df['item_etc'].iloc[i[0]]
    text5 = df['addr1'].iloc[i[0]]
    text6 = df['open_info'].iloc[i[0]]
    text7 = df['close_info'].iloc[i[0]]
    text8 = df['sup_obj'].iloc[i[0]]
    text9 = df['sup_num'].iloc[i[0]]

    html = """<!DOCTYPE html>
    <html>
    <head>

    </head>
    <body style="width:200px">
    <pre>
    <h3 style="text-align:center;">{}""".format(text1) + """</h3>
    <p style="text-align:center;">
    <img class="center" src="{}" """.format(text3) + """, style="width:200px;height:150px;">
    </p>
주소: {}""".format(text5) + """<br>
영업시간: {}""".format(text6) + """<br>
휴업일: {}""".format(text7) + """<br>
제공품목: {}""".format(text4) + """<br>
제공대상: {}""".format(text8) + """ 및 {}""".format(text9) + """<br>
<div style="text-align:center;">
<a href=http://localhost:8000/ddabob/{}""".format(text2) + """ 
target="_blank">자세히보기</a>
</div>
    </pre>
    </body>
    """

    return html
