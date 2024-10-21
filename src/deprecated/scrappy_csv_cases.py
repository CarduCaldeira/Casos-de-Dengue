import requests

def extract_csv(html: str):
    pass


def execute_scrappy():
    
    url = ( "https://www.saude.sp.gov.br/cve-centro-de-vigilancia-epidemiologica-prof.-alexandre-vranjac/" +
    "areas-de-vigilancia/doencas-de-transmissao-por-vetores-e-zoonoses/" +
    "arboviroses-urbanas/dengue-dados-estatisticos"
    )
    response = requests(url)

    if response.status_code == 200:
        extract_csv(response.txt)
    else:
        print(f'Falha na requisição. Código de status: {response.status_code}')

if '__main__' == __name__:
    
    execute_scrappy()