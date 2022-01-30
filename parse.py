#
#
#

def parse_tweet(text):
    """ Identifica os campos do tweet. Retorna uma tupla (data, hora, tipo da ocorrência, local, bairro). 

    ex. Ocorrência: 29/07 - 15h07 - Queda de altura (&gt; 3 metros)
        Localização: Rua Almirante Tamandare, 45 - Bairro: América

    retorna ('29/07', '15h07', 'Queda de altura (&gt; 3 metros)', 'Rua Almirante Tamandare, 45', 'América')
    """
    # 1. Truncar na quebra de linha 
    parts = text.split("\r")
    
    linha = [None, None]
    linha[0] = parts[0].split(':')[1].strip()
    linha[1] = parts[1].split(' - ')

    # Aqui, parts[0] é a primeira linha. Como podemos ter ocorrências com mais campos,
    # vamos pegar data, hora e o resto.

    data_ocorrencia, hora_ocorrencia, ocorrencia = [campo.strip() for campo in linha[0].split(" - ",maxsplit=2)]

    # Agora vamos tratar a segunda linha
    try:
        local, bairro = [campo.split(":", maxsplit=1)[1].strip() for campo in linha[1]]
    except:
        print("aqui")
        local = ' '.join(linha[1][:-1])
        bairro = linha[1][-1]
        print(local)
        print(bairro)

    return (data_ocorrencia, hora_ocorrencia, ocorrencia, local, bairro)
