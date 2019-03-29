import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

import pandas as pd

class SefazDriver(webdriver.Firefox, webdriver.Chrome, webdriver.Ie):
    def __init__(self, url, navegador):
        '''Inicializa o webdriver com o navegador especificado.

        url: endereço da página web da sefaz
        navegador: nome do navegador
        '''
        if navegador.lower() == 'chrome':
            webdriver.Chrome.__init__(self)
        elif navegador.lower() == 'firefox':
            webdriver.Firefox.__init__(self)
        elif navegador.lower() == 'ie':
            webdriver.Ie.__init__(self)
        self.get(url)

    def set_filter_by_text(self, elements):
        '''Configura os filtros da página de acordo com os elementos

        elements é uma lista de elementos:
            [elemento1, elemento2, ..., elemento n]

            em que cada elemento é da forma:
            [id do elemento, texto visível do elemento]
        '''
        for element in elements:
            select = Select(self.find_element_by_id(element[0]))
            select.select_by_visible_text(element[1])

    def set_filter_by_value(self, elements):
        '''Configura os filtros da página  de acordo com os elementos

        elements é uma lista de elementos:
            [elemento1, elemento2, ..., elemento n]

            em que cada elemento é da forma:
            [id do elemento, valor do elemento]
        '''
        for element in elements:
            select = Select(self.find_element_by_id(element[0]))
            select.select_by_value(element[1])

    def get_options_by_id(self, element_id):
        '''Pega opções de menu dropdown por meio do id do elemento

        retorna lista de opções no formato de texto
        '''
        select = Select(self.find_element_by_id(element_id))
        return [element.text for element in select.options]

class SefazScraper():
    def __init__(self, consultas):
        '''Inicializa um dicionário de dataframes, um pra cada tipo de consulta'''
        self.dfs = {}
        for consulta in consultas:
            self.dfs[consulta] = pd.DataFrame()

    def set_df_consulta(self, html, ano, periodo, grupo, consulta):
        '''Cria e aumenta o dataframe de cada consulta
        '''
        dfs = pd.read_html(html)
        for df in dfs:
            df['ano'] = ano
            df['periodo'] = 'Consolidado'
            df['grupo'] = 'Estado'
            df['consulta'] = consulta
            self.dfs[consulta] = self.dfs[consulta].append(df, ignore_index=True, sort=False)

    def save_df_consulta(self, consulta, nome):
        '''Salva o dataframe da consulta com o nome especificado
        '''
        self.dfs[consulta].to_csv(nome)



if __name__ == '__main__':
    URL_SEFAZ = 'http://www.transparenciafiscal.am.gov.br/transpprd/mnt/despesa/execDespAno.do'

    sefaz_driver = SefazDriver(URL_SEFAZ, 'firefox')

    anos = sefaz_driver.get_options_by_id('anoexercicio')

    sefaz_driver.set_filter_by_text([['grupo', 'Estado']])

    consultas = sefaz_driver.get_options_by_id('consulta')
    consultas.remove('Natureza de Despesa')

    sefaz_scraper = SefazScraper(consultas)

    for consulta in consultas:
        for ano in anos:
            sefaz_driver.implicitly_wait(20)

            OPCOES = [
                      ['anoexercicio', ano],
                      ['periodo', 'Consolidado'],
                      ['grupo', 'Estado'],
                      ['consulta', consulta]
                     ]
            sefaz_driver.set_filter_by_text(OPCOES)

            #//*[@id="search"] : botão Pesquisar
            sefaz_driver.find_element_by_xpath('//*[@id="search"]').click()

            html = sefaz_driver.page_source

            sefaz_scraper.set_df_consulta(html, ano, 'Consolidado', 'Estado', consulta)

            sefaz_driver.execute_script("window.history.go(-1)")

        sefaz_scraper.save_df_consulta(consulta, nome='output/sefaz-'+consulta+'.csv')

    sefaz_driver.quit()
