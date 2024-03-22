import gspread
from google.oauth2.service_account import Credentials

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

data = get_sales_data()