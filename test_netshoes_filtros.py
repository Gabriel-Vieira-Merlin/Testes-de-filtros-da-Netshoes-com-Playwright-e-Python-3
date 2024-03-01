#importação das bibliotecas
from playwright.sync_api import sync_playwright
import time

#Teste 1: Testar os filtro "Mais populares" da categoria de camisas de time
#Dado que eu tenha um dispositivo com acesso ao site da netshoes
#E clique em camisas de time abaixo do banner de promoções
#Então como automaticamente está em mais populares, garantir que o filtro está funcionando com o produto
#"Camisa São Paulo I 24/25 s/n° Torcedor New Balance Masculina - Branco+Vermelho" aparecendo como primeiro

#Testa o filtro "Mais populares"
def test_filtro_mais_populares():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch()

        #Criando a página
        pagina = navegador.new_page()

        #Indica a página a ser acessada
        pagina.goto("https://www.netshoes.com.br")

        #Clica em "Camisas de time"
        pagina.click('xpath=//*[@id="home-gamma-categories-list"]/section/div[2]/ul/li[8]/a/div')
        time.sleep(2)

        #Ceritifica que o produto "Camisa São Paulo I 24/25 s/n° Torcedor New Balance Masculina" é o primeiro a aparecer
        assert pagina.inner_text('xpath=//*[@id="item-list"]/div[1]/a[1]/div/div[2]/div[1]/span') == "Camisa São Paulo I 24/25 s/n° Torcedor New Balance Masculina"

#Teste 2: Testar os filtro "mais vendidos" da categoria de camisas de time
#Dado que eu tenha um dispositivo com acesso ao site da netshoes
#E clique em camisas de time abaixo do banner de promoções
#E clique no filtro superior direito
#E selecione "Mais vendidos" em ordenar itens
#Então o primeiro item que aparece é o item "Camisa São Paulo I 24/25 s/n° Torcedor New Balance Masculina"

#Testa o filtro "Mais vendidos"
def test_filtro_mais_vendidos():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch()

        #Criando a página
        pagina = navegador.new_page()

        #Indica a página a ser acessada
        pagina.goto("https://www.netshoes.com.br")

        #Clica em "Camisas de time"
        pagina.click('xpath=//*[@id="home-gamma-categories-list"]/section/div[2]/ul/li[8]/a/div')

        #Seleciona a opção mais vendidos
        pagina.click('xpath=//*[@id="content"]/section/section[2]/div[2]/div/div/ul/li/a')
        pagina.click('xpath=//*[@id="content"]/section/section[2]/div[2]/div/div/ul/li/div/a[2]')
        time.sleep(2)


        #Ceritifica que o produto "Camisa São Paulo I 24/25 s/n° Torcedor New Balance Masculina" é o primeiro a aparecer
        assert pagina.inner_text('xpath=//*[@id="item-list"]/div[1]/a[1]/div/div[2]/div[1]/span') == "Camisa São Paulo I 24/25 s/n° Torcedor New Balance Masculina"

#Teste 3: Testar o filtro "Lançamentos"
#Dado que eu tenha um dispositivo com acesso ao site da netshoes
#E clique em camisas de time abaixo do banner de promoções
#E clique no filtro superior direito
#E selecione "Lançamentos" em ordenar itens
#Então o primeiro item que aparece é o item "Camisa Goleiro I Flamengo 24/25 Adidas Masculina"

#Testa o filtro "Lançamentos"
def test_filtro_lançamentos():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch()

        #Criando a página
        pagina = navegador.new_page()

        #Indica a página a ser acesssada
        pagina.goto("https://www.netshoes.com.br")

        #Clica em "Camisas de time"
        pagina.click('xpath=//*[@id="home-gamma-categories-list"]/section/div[2]/ul/li[8]/a/div')

        #Seleciona a opção "Lançamentos"
        pagina.click('xpath=//*[@id="content"]/section/section[2]/div[2]/div/div/ul/li/a')
        pagina.click('xpath=//*[@id="content"]/section/section[2]/div[2]/div/div/ul/li/div/a[3]')
        time.sleep(2)

        #Certifica que o produto "Camisa Goleiro I Flamengo 24/25 Adidas Masculina" é o primeiro produto que aparece
        assert pagina.inner_text('xpath=//*[@id="item-list"]/div[1]/a[1]/div/div[2]/div[1]/span') == "Camisa Goleiro I Flamengo 24/25 Adidas Masculina"

#Teste 4: Testar o filtro "Ofertas"
#Dado que eu tenha um dispositivo com acesso ao site da netshoes
#E clique em camisas de time abaixo do banner de promoções
#E clique no filtro superior direito
#E selecione "Ofertas" em ordenar itens
#Então o primeiro item que aparece é o item "Camisa Polo Topper Figueirense Viagem 2018 Mascul"

#Testa o filtro "Ofertas"
def test_filtro_ofertas():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch()

        #Criando a página
        pagina = navegador.new_page()

        #Indica a página a ser acesssada
        pagina.goto("https://www.netshoes.com.br")

        #Clica em "Camisas de time"
        pagina.click('xpath=//*[@id="home-gamma-categories-list"]/section/div[2]/ul/li[8]/a/div')

        #Seleciona a opção "Ofertas"
        pagina.click('xpath=//*[@id="content"]/section/section[2]/div[2]/div/div/ul/li/a')
        pagina.click('xpath=//*[@id="content"]/section/section[2]/div[2]/div/div/ul/li/div/a[4]')
        time.sleep(2)

        #Certifica que o produto "Camisa Polo Topper Figueirense Viagem 2018 Mascul" é o primeiro produto que aparece
        assert pagina.inner_text('xpath=//*[@id="item-list"]/div[1]/a[1]/div/div[2]/div[1]/span') == "Camisa Polo Topper Figueirense Viagem 2018 Mascul"

#Teste 5: Testar o filtro "Melhor Avaliados"
#Dado que eu tenha um dispositivo com acesso ao site da netshoes
#E clique em camisas de time abaixo do banner de promoções
#E clique no filtro superior direito
#E selecione "Melhor Avaliados" em ordenar itens
#Então o primeiro item que aparece é o item "Camisa Flamengo I 24/25 s/n° Torcedor Adidas Masculina"

#Testa o filtro "Melhor avaliados"
def test_filtro_melhor_avaliados():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch()

        #Criando a página
        pagina = navegador.new_page()

        #Indica a página a ser acesssada
        pagina.goto("https://www.netshoes.com.br")

        #Clica em "Camisas de time"
        pagina.click('xpath=//*[@id="home-gamma-categories-list"]/section/div[2]/ul/li[8]/a/div')

        #Seleciona a opção "Melhor avaliados"
        pagina.click('xpath=//*[@id="content"]/section/section[2]/div[2]/div/div/ul/li/a')
        pagina.click('xpath=//*[@id="content"]/section/section[2]/div[2]/div/div/ul/li/div/a[5]')
        time.sleep(2)

        #Certifica que o produto "Camisa Flamengo I 24/25 s/n° Torcedor Adidas Masculina" é o primeiro produto que aparece
        assert pagina.inner_text('xpath=//*[@id="item-list"]/div[1]/a[1]/div/div[2]/div[1]/span') == "Camisa Flamengo I 24/25 s/n° Torcedor Adidas Masculina"

#Teste 6: Testar o filtro "Maior preço"
#Dado que eu tenha um dispositivo com acesso ao site da netshoes
#E clique em camisas de time abaixo do banner de promoções
#E clique no filtro superior direito
#E selecione "Maior preço" em ordenar itens
#Então o primeiro item que aparece é o item "Kit C/ 6 Bolas de Basquete Magussy Pro 6"

#Testa o filtro "Maior preço"
def test_filtro_maior_preço():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch()

        #Criando a página
        pagina = navegador.new_page()

        #Indica a página a ser acesssada
        pagina.goto("https://www.netshoes.com.br")

        #Clica em "Camisas de time"
        pagina.click('xpath=//*[@id="home-gamma-categories-list"]/section/div[2]/ul/li[8]/a/div')

        #Seleciona a opção "Maior preço"
        pagina.click('xpath=//*[@id="content"]/section/section[2]/div[2]/div/div/ul/li/a')
        pagina.click('xpath=//*[@id="content"]/section/section[2]/div[2]/div/div/ul/li/div/a[6]')
        time.sleep(2)

        #Certifica que o produto "Kit C/ 6 Bolas de Basquete Magussy Pro 6" é o primeiro produto que aparece
        assert pagina.inner_text('xpath=//*[@id="item-list"]/div[1]/a[1]/div/div[2]/div[1]/span') == "Kit C/ 6 Bolas de Basquete Magussy Pro 6"

#Teste 7: Testar o filtro "Menor preço"
#Dado que eu tenha um dispositivo com acesso ao site da netshoes
#E clique em camisas de time abaixo do banner de promoções
#E clique no filtro superior direito
#E selecione "Menor preço" em ordenar itens
#Então o primeiro item que aparece é o item "Copo Grêmio Prudente"

#Testa o filtro "Menor preço"
def test_filtro_menor_preço():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch()

        #Criando a página
        pagina = navegador.new_page()

        #Indica a página a ser acesssada
        pagina.goto("https://www.netshoes.com.br")

        #Clica em "Camisas de time"
        pagina.click('xpath=//*[@id="home-gamma-categories-list"]/section/div[2]/ul/li[8]/a/div')

        #Seleciona a opção "Menor preço"
        pagina.click('xpath=//*[@id="content"]/section/section[2]/div[2]/div/div/ul/li/a')
        pagina.click('xpath=//*[@id="content"]/section/section[2]/div[2]/div/div/ul/li/div/a[7]')
        time.sleep(2)

        #Certifica que o produto "Copo Grêmio Prudente" é o primeiro produto que aparece
        assert pagina.inner_text('xpath=//*[@id="item-list"]/div[1]/a[1]/div/div[2]/div[1]/span') == "Copo Grêmio Prudente"