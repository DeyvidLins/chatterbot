import  webbrowser

# Url do site Maganize Luiza
url = ['https://www.magazineluiza.com.br/?partner_id=974&gclid=CjwKCAjwgISIBhBfEiwALE19SY6IBYN9jrL33-AHgYdmGmjHHdf_VaHFvCbxan9RZ_3z___RXMZ-YRoC0OUQAvD_BwE']

class Sites:
    def __init__(self,texto):
        self.texto = texto

    def direcionar_sites(self):
        # Direciona para o site Magazine Luiza
        if (self.texto in 'Magazine Luiza') or (self.texto == 'Magazine Luiza'):
            print('Direcionando para o Site...')
            webbrowser.register('firefox', None,
            webbrowser.BackgroundBrowser(r"C:\Program Files\Mozilla Firefox\firefox.exe"))
            webbrowser.get('firefox').open(url[0])

