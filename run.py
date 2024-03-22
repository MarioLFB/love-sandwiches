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

def get_sales_data():
    """ 
    Pegar os dados de vendas de usuários
    """
    print("Please enter sales data from the last market.")
    print("Data should be six numbers, separated by commas.")
    print("Example: 10,20,30,40,50,60\n") # \n é um caractere de escape que pula uma linha


    data_str = input("Enter your data here:") 
    """
    Cria um INPUT para o usuário inserir os dados de vendas
    """
    sales_data = data_str.split(",")
    validate_data(sales_data)
    """
    chama a funcao validate_data criada a baixo. o Resultado da funcao atual,  que sao os dados coletados do usuario no formato de lista e passados 
    para a variavel SALES_DATA sao usados como parametro para a funcao validate_data.
    """


# ESSA FUNCAO ESTA DENTRO DO GET_SALES_DATA E VALIDA OS DADOS INSERIDOS PELO USUARIO
def validate_data(values):
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
        if len(values) != 6: # 2 - Depois do Loop e alista convertida em Numeros Inteiros, vai percorrer a lista de valores inseridos pelo usuario e verifica se tem 6 valores
            raise ValueError( #caso tenha MAIS de 6 valores, a funcao ira retornar um erro e acinar o except, descrito no except ValueError as e:
                f"Exactly 6 values are required, you provided {len(values)}"
            )
    except ValueError as e: #caso o erro seja retornado dentro do IF(ou seja mais de 6 valores) 'e acionado, a funcao E ira printar a mensagem de erro e pedir para o usuario tentar novamente
        print(f"Invalid data: {e}, please try again.\n")




    print(values)



get_sales_data()