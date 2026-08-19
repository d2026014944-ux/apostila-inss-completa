# Registro de confirmacao das fontes

## Limite da confirmacao

Este registro confirma apenas que as URLs foram testadas a partir do ambiente de desenvolvimento em 19/08/2026. Acessibilidade HTTP nao equivale a conferencia do teor juridico nem substitui a leitura da versao vigente da norma.

## Resultado tecnico

| Fonte | URL | Resultado | Observacao |
|---|---|---:|---|
| Planalto - Constituicao | https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm | nao confirmado | Container retornou erro de rede `000`. |
| Planalto - Lei 8.212 | https://www.planalto.gov.br/ccivil_03/leis/l8212cons.htm | nao confirmado | Container retornou erro de rede `000`. |
| Planalto - Lei 8.213 | https://www.planalto.gov.br/ccivil_03/leis/l8213cons.htm | nao confirmado | Container retornou erro de rede `000`. |
| Planalto - Decreto 3.048 | https://www.planalto.gov.br/ccivil_03/decreto/d3048.htm | nao confirmado | Container retornou erro de rede `000`. |
| Planalto - EC 103 | https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc103.htm | nao confirmado | Container retornou erro de rede `000`. |
| Planalto - Lei 8.112 | https://www.planalto.gov.br/ccivil_03/leis/l8112cons.htm | nao confirmado | Container retornou erro de rede `000`. |
| Planalto - Lei 9.784 | https://www.planalto.gov.br/ccivil_03/leis/l9784.htm | nao confirmado | Container retornou erro de rede `000`. |
| Planalto - Lei 8.429 | https://www.planalto.gov.br/ccivil_03/leis/l8429.htm | nao confirmado | Container retornou erro de rede `000`. |
| Planalto - Decreto 1.171 | https://www.planalto.gov.br/ccivil_03/decreto/d1171.htm | nao confirmado | Container retornou erro de rede `000`. |
| Planalto - LGPD | https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm | nao confirmado | Container retornou erro de rede `000`. |
| Portal INSS | https://www.gov.br/inss/pt-br | HTTP 200 | URL acessível no ambiente. Teor não revisado por este teste. |
| Portal Cebraspe | https://www.cebraspe.org.br/concursos | HTTP 200 | URL acessível no ambiente. Edital específico ainda não identificado. |

## Procedimento exigido para fechar a confirmação

1. Abrir cada fonte no navegador ou em ambiente com acesso ao Planalto.
2. Conferir a versão consolidada e a data de atualização.
3. Registrar os artigos utilizados por tópico.
4. Salvar a data, o nome e a qualificação do revisor.
5. Atualizar `sources.yaml` somente após a conferência humana.

**Status:** fontes oficiais ainda não aprovadas para a edição comercial. Os dois portais com HTTP 200 tiveram apenas acessibilidade confirmada; as dez URLs do Planalto ficaram sem confirmação por bloqueio de rede do ambiente.
