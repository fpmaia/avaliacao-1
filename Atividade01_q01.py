# -*- coding: utf-8 -*-
"""
Atividade 01
Questão 01: Implemente um programa que entre no site do UOL e imprima apenas a seguinte mensagem: 
			A cotação atual do dólar é: <cotação>, onde <cotação> vai ser o valor capturado do site no momento. 
			Procure uma forma de omitir as mensagens de log na execução do seu programa para aparecer apenas essa mensagem como saída.
			
Comando Execução: scrapy runspider --nolog Atividade01_q01.py

@author: Felipe Pedro
"""
import scrapy
from scrapy.utils.response import open_in_browser

class TerraSpider(scrapy.Spider):
    name = "Terra"
    
    start_urls = { 'https://www.uol.com.br/' }
    
    def parse(self, response):
        #open_in_browser(response)
		valor = str(response.css('.currency_quote__down::text').extract_first())
		print('A cotação atual do dólar é: '+valor)