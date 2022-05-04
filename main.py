from Hcatpcha import hCaptcha


PAGINA_IMEI = 'https://www.imeicolombia.com.co/'

class ImeiColombia:
    def __init__(self, imei):
        self.imei = imei

    def pagina_imei(self, url: str):
        self.driver.get(url)

    def run(self):
        self.pagina_imei(PAGINA_IMEI)



if __name__ == '__main__':
    hcatpcha = hCaptcha() #init hCaptcha class.
    hcatpcha.download_usercript() #Download the hCaptcha solver userscript
    checking_imeis = ImeiColombia() #Dentro de parentésis irán el argumento "imei"
    checking_imeis.run()
    #with open('imeis.txt', 'r') as file:
     #   for numero in file:
            
