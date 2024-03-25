import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint # Importa a funcao pprint para imprimir os dados de uma forma mais legivel

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPE_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPE_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

def get_sales_data(): # Pegar os dados de vendas de usuários
    
    while True: # O loop ira rodar ate que o usuario insira os dados corretos
        print("Please enter sales data from the last market.")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60\n")

        data_str = input("Enter your data here:") #Cria um INPUT para o usuário inserir os dados de vendas
        sales_data = data_str.split(",") #  divide uma string em uma lista de strings usando um delimitador dentro do parentenses. "10,20,30,40,50,60" para ["10", "20", "30", "40", "50", "60"]
    
        if validate_data(sales_data): # Roda a funcao para validar dados validate_data e o parametro sales_data. Se a funcao retornar True, o loop ira parar por causa do break
            print("Data is valid!")
            break
        
    return sales_data

def validate_data(values): # Cria a Funcao de validacao de dados
    """
    Essa funcao ira validar/analistar os dados inseridos pelo usuario
    1 - Se tem 6 valores inseridos pelo usuario, uma vez que a planilha tem 6 colunas.
    2 - Se os valores inseridos sao numeros inteiros uma vez que vamos obter strings
    """

    try: 
        [int(value) for value in values]
        """
        O Loop pega cada valor individular (value) dentro da lista de valores (values), converta o valor em um valor inteiro (int(value))
        CASO SEJA UM VALOR NAO NUMERICO DENTRO DA STRING IRA RETORNAR ERROR EX: 12,12,12,CARRO
        """ 
        if len(values) != 6: # 1- Se o numero de valores inseridos pelo usuario for diferente de 6, ira retornar um erro
            raise ValueError( 
                f"Exactly 6 values are required, you provided {len(values)}"
            )
    except ValueError as e: # 2- Se o valor inserido pelo usuario for diferente de um numero inteiro, ira retornar um erro
        print(f"Invalid data: {e}, please try again.\n")
        return False
    
    return True
    """
    O `return True` é o que indica que os dados passaram pela validação
    com sucesso. Quando a função `validate_data` retorna `True`, isso significa que os dados são válidos.
    No loop `while True`, há uma verificação condicional `if validate_data(sales_data):`.
    Se essa condição for verdadeira, ou seja, se `validate_data` retornar `True`, o programa imprimirá
    "Data is valid!" e então sairá do loop infinito usando `break`, pois o objetivo de obter dados válidos foi alcançado.
    Portanto, o `return True` no final da função é crucial para permitir que o loop avance e conclua 
    sua execução quando os dados forem considerados válidos.
    """


def update_sales_worksheet(data): 
    """
    Funcao criada para inserir os dados dentro da planilha de excel.
    """
    print("Updating sales worksheet...\n") # Mensagem de atualizacao da planilha
    sales_worksheet = SHEET.worksheet('sales') # Atribui a variavel sales_worksheet a aba na planilha de excel chamada SALES
    sales_worksheet.append_row(data) # Adiciona uma linha de dados a planilha de excel
    print("Sales worksheet updated successfully.\n") # Mensagem de sucesso


def calculate_surplus_data(sales_row):
    """
    Cria funcao para calcular o excedente de produtos, pegando como informacao
    os dados de vendas do usuario.
    """
    print("Calculating surplus data...\n") # Mensagem de calculo de excedente
    stock = SHEET.worksheet("stock").get_all_values() # Atribui a variavel stock a aba na planilha de excel chamada STOCK. Isso pegara todos os valores da aba
    stock_row = stock[-1] # Atribui a variavel stock_row para pegar a ultima linha da aba stock da planilha de excel. -1 pega a ultima linha, -2 pega a penultima linha e assim por diante
    
    
    surplus_data = [] # Cria uma lista vazia para armazenar os valores de excedente
    for stock, sales in zip(stock_row, sales_row): # O loop ira rodar para cada valor de stock e sales usando metodo zip
        surplus = int(stock) - sales # usar o metodo int para converter o valor de stock e sales em inteiros e subtrair o valor de stock pelo valor de sales.
        surplus_data.append(surplus) # Adiciona o valor de surplus a lista de surplus criada acima vazia.
    
    return surplus_data # Retorna o valor de surplus_data

def main():
    """
    'E de pratica boa criar a funcao main para envolver todas as funcoes'
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data] #issos ira converter os valores de string para inteiros
    update_sales_worksheet(sales_data) # chama a funcao update_sales_worksheet e passa o parametro sales_data
    new_surplus_data = calculate_surplus_data(sales_data) # chama a funcao calculate_surplus_data e passa o parametro sales_data
    print(new_surplus_data) # Imprime o valor de new_surplus_data

print("Welcome to Love Sandwiches Data Automation") # Cria Mensagem de boas vindas sera exibida ao rodar o programa
main() # Chama a funcao main para rodar o programa. Achamada da funcao tem que estar sempre abaixo da funcao
