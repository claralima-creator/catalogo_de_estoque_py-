print("Catálogo de Estoque e Etiquetas de Produtos (CLI)")

catalogo = {}

sku = input("Digte o SKU:")
nome = input("Digite o nome:")
preco = input("Digite o preço(em centavos):")
qtd = input("Digite a quantidade:")
etiquetas =input("Digite as etiquetas:")

def cadastrar_produto(catalogo, sku, nome, preco, qtd, etiquetas = None):

    if sku in catalogo:
        print("SKU já cadastrado!")
        return

    if (preco.isdigit()):
        print('Sucesso')
    else:
        print('Erro')
        return
    
    preco = (int(preco))

    if preco > 0:
         print('Preço válido')
    else:
         print('Preço inválido')
         return

    if (qtd.isdigit()):
            print('Sucesso')
    else:
            print('Erro')
            return
    
    qtd = (int(qtd))

    if qtd > 0:
         print('Quantidade válida')
    else:
         print('Quantidade inválida')
         return

    if etiquetas is None:
        etiquetas = set() 

    else:
        etiquetas_limpas = set()

        for etiqueta in etiquetas.split(','):
             etiqueta = etiqueta.strip()
             print(etiqueta)
             etiquetas_limpas.add(etiqueta)

        etiquetas = etiquetas_limpas
    
    informacoes_produtos = {
        "nome": nome, 
        'preco': preco, 
        'qtd': qtd, 
        'etiquetas': etiquetas}

    catalogo[sku] = informacoes_produtos

cadastrar_produto(catalogo, sku, nome, preco, qtd, etiquetas)
print(catalogo)

sku = input("Digte o SKU:")
nome = input("Digite o nome:")
preco = input("Digite o preço(em centavos):")
qtd = input("Digite a quantidade:")
etiquetas =input("Digite as etiquetas:")

cadastrar_produto(catalogo, sku, nome, preco, qtd, etiquetas)
print(catalogo)
        
def aplicar_desconto(preco, percentual):
    desconto = preco * percentual / 100
    preco_final = preco - desconto
    return (preco_final, desconto)

resultado = aplicar_desconto(1000, 10)
print(resultado)

sku1_autorizado = input('Digite o primeiro SKU')
if sku1_autorizado in catalogo:
     etiquetas_produto1 = catalogo.get(sku1_autorizado)['etiquetas']
     print('SKU cadastrado')
     print(etiquetas_produto1)
else:
     print('Produto não encontrado, não é possível acessar as etiquetas')

sku2_autorizado = input('Digite o segundo SKU')
if sku2_autorizado in catalogo:
    etiquetas_produto2 = catalogo.get(sku2_autorizado)['etiquetas']
    print('SKU cadastrado')
    print(etiquetas_produto2)
else:
     print('Produto não encontrado, não é possível acessar as etiquetas')

etiquetas_comuns = etiquetas_produto1 & etiquetas_produto2
print(sorted(etiquetas_produto1 & etiquetas_produto2))

etiquetas_exclusivas = etiquetas_produto1 ^ etiquetas_produto2
print(sorted(etiquetas_produto1 ^ etiquetas_produto2))

etiquetas_primeiro = etiquetas_produto1 - etiquetas_produto2
print(sorted(etiquetas_primeiro))

sku = input('Digite o SKU que deseja alterar etiquetas:')
if sku in catalogo:
     etiquetas_produto = catalogo.get(sku) ['etiquetas']
     print('Etiquetas cadastrada')
     print(etiquetas_produto)
else:
     print('SKU informado não existente,etiquetas não localizadas')

acao = input('Deseja adicionar ou remover alguma etiqueta?')

etiqueta = input('Digte aqui sua etiqueta')

if acao == 'adicionar':
    etiquetas_produto.add(etiqueta)
    print(etiquetas_produto)
else:
    etiquetas_produto.discard(etiqueta)
    print(etiquetas_produto)

valor_total = 0

for sku, produto in catalogo.items():
    subtotal = produto['preco'] * produto['qtd'] 
    print(subtotal)
    valor_total += subtotal

valor_editado = valor_total / 100
print(f'{valor_editado:.2f}')

conjunto_etiquetas = set()

for sku, dados in catalogo.items():
    dados['etiquetas']
    conjunto_etiquetas = conjunto_etiquetas | dados['etiquetas']
    print(sorted(conjunto_etiquetas))

while True:
    print(f"{'='*15}CATÁLOGO DE ESTOQUE{'='*15}")
    print("1 - Cadastrar produto")
    print("2 - Aplicar desconto")
    print("3 - Comparar etiquetas")
    print("4 - Alterar etiquetas")
    print("5 - Relatório do estoque")
    print("0 - Sair")
    opcao = input("Digite qual opção você deseja escolher")

    if opcao == '1':
        sku = input("Digite o SKU do produto:")
        nome = input("Digite o nome do produto:")
        preco = input("Digite o preço do produto:")
        qtd = input("Digite a quantidade do produto:")
        etiquetas = input("Digite as etiquetas do produto:")

        cadastrar_produto(catalogo, sku, nome, preco, qtd, etiquetas)

    elif opcao == '2':
        sku = input('Digite o sku do produto:')

        if sku in catalogo:
            preco = catalogo.get(sku)['preco']

            percentual = input(
            "Digite qual a porcentagem de desconto você deseja nesse produto:"
        )

        if percentual == '':
            percentual = 10
        else:
            percentual = int(percentual)

            preco_final, economia = aplicar_desconto(preco, percentual)

            preco_final_reais = preco_final / 100
            print(f'Preço final: R$ {preco_final_reais:.2f}')

            economia_reais = economia / 100
            print(f'Você economizou: R$ {economia_reais:.2f}')

    else:
        print('Erro, SKU inválido, tente novamente')

    if opcao == '3':
      sku1 = input('Digite o primeiro SKU:')
      sku2 = input('Digite o segundo SKU:')

      if sku1 in catalogo and sku2 in catalogo:
            etiquetas_produto1 = catalogo.get(sku1)['etiquetas']
            etiquetas_produto2 = catalogo.get(sku2)['etiquetas']

            etiquetas_comuns = etiquetas_produto1 & etiquetas_produto2
            etiquetas_exclusivas = etiquetas_produto1 ^ etiquetas_produto2
            etiquetas_primeiro = etiquetas_produto1 - etiquetas_produto2

            print('Etiquetas em comum:', sorted(etiquetas_comuns))
            print('Etiquetas exclusivas:', sorted(etiquetas_exclusivas))
            print('Etiquetas apenas do primeiro produto:', sorted(etiquetas_primeiro))

      else:
        print('Erro: um ou ambos os SKUs não foram encontrados.')


    elif opcao == '4':
        sku = input("Digite o SKU do produto: ")

        if sku in catalogo:
            etiquetas_produto = catalogo.get(sku)['etiquetas']

            print("Etiquetas cadastradas:", sorted(etiquetas_produto))

            acao = input("Deseja adicionar ou remover uma etiqueta? ").lower()
            etiqueta = input("Digite a etiqueta: ").strip()

            if acao == 'adicionar':
                etiquetas_produto.add(etiqueta)
                print("Etiqueta adicionada!")

            elif acao == 'remover':
                etiquetas_produto.discard(etiqueta)
                print("Etiqueta removida!")

            else:
                print("Ação inválida!")

            print("Etiquetas atuais:", sorted(etiquetas_produto))

        else:
            print("SKU informado não existe!")
            
    elif opcao == '5':
        print("===== RELATÓRIO DO ESTOQUE =====")
        print(f"Valor total do estoque: R$ {valor_editado:.2f}")
        print("Todas as etiquetas:", sorted(conjunto_etiquetas))
              
    elif opcao == '0':
        print("Encerrando o catálogo. Até mais!")
        break

    else:
        print("Opção inválida! Tente novamente.")

