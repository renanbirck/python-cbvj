# 2023-05-23: Não uso mais o Twitter e não quero mais saber da plataforma desde o dia em que ela foi estragada após a compra pelo Elon Musk. Dessa forma, estou arquivando o projeto e não irei mais mexer nele.

O [Corpo de Bombeiros de Joinville/SC](http://www.cbvj.com.br/) (CBVJ, que é como eu irei chamar daqui em diante) divulga, por meio do seu [twitter](https://twitter.com/bvsc_joinville), as ocorrências no município. Isso fornece um material bastante interessante para projetos de análise de dados.

Neste projeto, iremos coletar os dados do tweet para podermos gerar gráficos e análises diversas.

######

O script `download_tweets.py` faz _download_ dos tweets do perfil do CBVJ e salva eles em um arquivo para permitir a análise. 

# Requisitos
* tweepy
* gerar uma chave de aplicação no https://developer.twitter.com/en/apps

# Configuração

Primeiramente, certifique-se que a `tweepy` estão instaladas. No arquivo `keys.py`, criar as variáveis `ACCESS_KEY`, `ACCESS_SECRET_KEY`, `API_KEY`, `API_SECRET_KEY` e `BEARER_TOKEN`, com os dados que são fornecidos quando você cria uma nova app no portal de dev do Twitter; como essa chave é confidencial, não colocarei as minhas aqui.

# Execução

Com as chaves configuradas, execute o `main.py`, que irá capturar os dados (número do tweet - nossa chave primária, conteúdo do tweet e data de sua criação) e jogá-los na tabela `tweets`. 

Não é preciso criar o banco de dados manualmente, pois ele é criado dentro de `store.py`, que é chamado na `main`; inclusive, embora não tenha testado, se for necessário adaptar a aplicação para outros bancos de dados, isso será feito nesta camada. Qualquer banco de dados deverá funcionar.

A "desmontagem" do tweet é feita dentro do arquivo `parse.py`, que quebra o tweet em data, hora, tipo da ocorrência, local, bairro e data da ocorrência. Após, `store.py` armazena as partes do tweet na tabela `parsed_tweets`.

Para repetir a execução do comando e coletar dados novos, pode-se usar a crontab ou, para desenvolvimento, o comando `watch`.

# TODO

* Dockerizar o script.
