#
#
#

def parse_tweet(text):
    """ Identifica os campos do tweet. Retorna uma tupla (data, hora, tipo da ocorrência, local, bairro). 

    ex. Ocorrência: 29/07 - 15h07 - Queda de altura (&gt; 3 metros)
        Localização: Rua Almirante Tamandare, 45 - Bairro: América

    retorna ('29/07', '15h07', 'Queda de altura (&gt; 3 metros)', 'Rua Almirante Tamandare, 45', 'América')
    """

    # 1. Troca a quebra de linha por um traço, e depois trunca no traço.
    parts = text.replace('\r', ' - ').split(' - ')
                                     
    # Aqui teremos algo no formato
    # ['Ocorrência: DD/MM', 'HHhMM', 'tipo da ocorrência', 'Localização: XXX', 'Bairo: XXX'].
    # Vamos quebrar em partes depois do ":" e pegar o último elemento, 
    # dessa forma iremos ter apenas os valores que nos interessam. Se houver ":", pegamos a parte depois dele.
    
    return tuple([part.split(": ")[-1] for part in parts])
