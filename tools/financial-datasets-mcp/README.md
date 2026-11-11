# Financial Datasets MCP server

Cópia do servidor MCP de https://github.com/financial-datasets/mcp-server (licença MIT, ver `LICENSE`).
É carregado pelo `.mcp.json` na raiz do repositório e dá ao Claude ferramentas de dados de mercado
(demonstrações financeiras, preços de ações e cripto, notícias, SEC filings).

A chave da API **não** fica neste repositório. Em sessões na nuvem ela é salva como segredo de rede
do ambiente para o host `api.financialdatasets.ai` (cabeçalho `X-API-KEY`); o valor
`proxy-injected` no `.mcp.json` é só um marcador que o proxy substitui. Para uso local, troque esse
valor pela sua chave em uma configuração que não seja enviada ao GitHub.
