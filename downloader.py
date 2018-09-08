from urllib.request import urlopen
from bs4 import BeautifulSoup

class Downloader:


    def baixaEp(self):

        self.index = 0
        print("Inicializando...")
        self.url = ['http://eutavala.com.br']
        self.page = urlopen(self.url[self.index])
        self.soup = BeautifulSoup(self.page, 'html.parser')
        self.soup.prettify()

        for h in self.soup.findAll('h2', class_ ='card-title entry-title'): # PARA CADA H2 NA CLASSE
            self.links = h.a.get('href')                                    # ENTRA NO '<a>' E PEGA O HREF
            self.url.append(self.links)
            self.index += 1

            print(self.index)                                           # test
            self.page = urlopen(self.url[self.index])
            self.soup = BeautifulSoup(self.page, 'html.parser')

            for i in self.soup.findAll('article', class_ = 'section section-text'):
                self.enter_links = i.a.get('href')
                print(self.enter_links)                                 # test
                self.page = urlopen(self.enter_links)

                self.file_name = self.enter_links.split('/')[-1]
                with open ('%s' % self.file_name, 'wb') as f:
                    print('Baixando: %s' % self.file_name)              # test
                    f.write(self.page.read())
                    print("Sucesso!")                                   # test
