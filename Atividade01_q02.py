# -*- coding: utf-8 -*-
"""
Atividade 01
Questão 02: Implemente um programa que receba um produto como parâmetro e liste o nome e o preço de todos esses produtos no mercado livre, 
			com paginação incluída. Busque uma forma de passar um parâmetro para o seu programa.

Comando Execução: scrapy runspider --nolog Atividade01_q02.py

@author: Felipe Pedro
"""
import scrapy
from scrapy.shell import inspect_response 
from scrapy.utils.response import open_in_browser

class MercadoLivreSpider(scrapy.Spider):
	name = "Mercado_Livre"
	produto = "bicicleta"
	
	start_urls = { 'https://lista.mercadolivre.com.br/{}'.format(produto) }
	
	def parse(self, response):
		#open_in_browser(response)
		#inspect_response(response, self)
		prods = response.css('.item--show-right-col')
		
		
		for produto in prods:
			nomeProd  = produto.css('.main-title::text').extract_first()
			precoProd = produto.css('.price__fraction::text').extract_first()
			print('Nome: ' +nomeProd+'\n'+'Valor: '+precoProd)
			
			
       