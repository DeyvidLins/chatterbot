import  webbrowser

url = ['https://www.magazineluiza.com.br/?partner_id=974&gclid=CjwKCAjwgISIBhBfEiwALE19SY6IBYN9jrL33-AHgYdmGmjHHdf_VaHFvCbxan9RZ_3z___RXMZ-YRoC0OUQAvD_BwE']

def function(texto):
    if 'magazine luiza'.capitalize().upper().lower().title() in texto:
        print('Direcionando para o Site...')
        webbrowser.register('firefox', None,
        webbrowser.BackgroundBrowser(r"C:\Program Files\Mozilla Firefox\firefox.exe"))
        webbrowser.get('firefox').open(url[0])

    if 'Foto' == texto.capitalize():
        import reconhecimentofacial

    if 'Finalizar' or 'Encerrar' == texto:
        exit()

