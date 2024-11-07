# Análise de Dados experimental de Vendas
Nesse projeto, eu irei analisar 
## 1-Definindo quais Dados para serem analisados.
Como tenho poucos recursos para fazer uma coleta de dados própria, eu irei analisar dados já existente desse [link](https://www.kaggle.com/datasets/yusufdelikkaya/online-sales-dataset/data) do kaggle, onde os dados existentes nesse arquivo __online_sales_dataset.csv__ são dados de vendas anônimas e de livre acesso.
## 2-Configurando o arquivo no excel
Próximo passo que fiz é transcrever os dados de __online_sales_dataset.csv__ , para isso precisei configurar um pasta de trabalho chamada __Tabela de vendas.xlsx__ (configurada no meu computador com o suplemento externo traduzir da [macrofaz](https://macrofaz.com.br/)) e inserir esses dados em uma planilha chamada __Main__, a tabela tem 49783 linhas e 17 colunas no total.
### 2.1- Traduzindo informações
Como as informações da tabela estavam em inglês, eu tive que traduzir as informações para PTBR, porém foi bem complicado traduzir todas as informações de uma tabela 17x49783, então filtrei quais palavras deveriam ser traduzidas, como os nomes do cabeçários das colunas e informações das mesmas , de coluna a coluna, alguns eu usando a fórmula =traduzir_EN_PT(). 
### 2.2- Limpando Dados
Antes de fazer uma análise real, precisei consertar a formatação da tabela e eliminar algumas linhas que continham informações imprecisas.
