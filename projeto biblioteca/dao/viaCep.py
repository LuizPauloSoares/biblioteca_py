import requests

def verCep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        pergunta = requests.get(url)

        if pergunta.status_code == 200:

            resposta = pergunta.json()

            if resposta.get("erro") == "true":
                print("cep nao encontrado")
            else:
                logradouro = resposta.get('logradouro', '')
                bairro = resposta.get('bairro','')
                cidade = resposta.get('localidade','')
                uf = resposta.get('uf','')
                estado = resposta.get("estado":"")

                print("cep encontrado")
                endereco = endereco(uf,estado,cidade,logradouro,cep,bairro)
                return endereco

        else:
            print("cep nao encontrado")

    except:
        print("erro")