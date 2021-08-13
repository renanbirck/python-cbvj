O [Corpo de Bombeiros de Joinville/SC](http://www.cbvj.com.br/) divulga, por meio do seu [twitter](https://twitter.com/bvsc_joinville), as ocorrências no município. Isso fornece um material bastante interessante para projetos de análise de dados.

Neste projeto, iremos coletar os dados do tweet para podermos gerar gráficos diversos.

######

O script `download_tweets.py` faz _
download_ dos tweets do perfil do  e salva eles em um arquivo para permitir a análise. Após, é possível usar o script `analisa_bvsc.py` para visualizar os dados.

# Requisitos
* tweepy
* matplotlib
* gerar uma chave de aplicação no https://developer.twitter.com/en/apps

# Configuração

Primeiramente, certifique-se que a `matploblib` e a `tweepy` estão instaladas.

No arquivo `keys.py`, criar as variáveis `ACCESS_KEY`, `ACCESS_SECRET_KEY`, `API_KEY`, `API_SECRET_KEY` e `BEARER_TOKEN`, com os dados que são fornecidos quando você cria uma nova app no portal de dev do Twitter; como essa chave é confidencial, não colocarei as minhas aqui.

    #### Autenticação
    def authenticate_oauth():
        auth = tweepy.OAuthHandler(keys.API_KEY, keys.API_SECRET_KEY)
        auth.set_access_token(keys.ACCESS_KEY, keys.ACCESS_SECRET_KEY)
        api = tweepy.API(auth, wait_on_rate_limit_notify=True, wait_on_rate_limit=True)
        return api


# Lendo os tweets

# Jogando eles em um arquivo do SQLite

# Fazendo processamento dos tweets
Até aqui temos os dados "brutos", isto é, sem a separação do tipo de ocorrência, local, data e hora. Como iremos precisar


# Gerando gráficos
