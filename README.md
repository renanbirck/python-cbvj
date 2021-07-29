######

O script `download_tweets.py` faz _
download_ dos tweets do perfil do [Corpo de Bombeiros de Joinville/SC](https://twitter.com/bvsc_joinville) e salva eles em um arquivo para permitir a análise. Após, é possível usar o script `analisa_bvsc.py` para visualizar os dados.

# Requisitos
* tweepy
* matplotlib
* gerar uma chave de aplicação no https://developer.twitter.com/en/apps

# Configuração

Primeiramente, certifique-se que a `matploblib` e a `tweepy` estão instaladas.

No arquivo `keys.py`, criar as variáveis `ACCESS_KEY`, `ACCESS_SECRET_KEY`, `API_KEY`, `API_SECRET_KEY` e `BEARER_TOKEN`, com os dados que são fornecidos quando você cria uma nova app no portal de dev do Twitter; como essa chave é confidencial, não colocarei as minhas aqui.

# Lendo os tweets

# Jogando eles em um arquivo do SQLite

# Gerando gráficos