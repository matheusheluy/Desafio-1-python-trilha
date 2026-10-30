# Desafio Nível 1 — PDV com Descontos

## O que o código faz

Este programa simula um PDV (Ponto de Venda) que registra compras e aplica descontos progressivos de acordo com regras de negócio. Clientes com 65 anos ou mais recebem 20% de desconto, e compras que, após esse desconto, ainda passam de R$ 100 recebem mais 10%. O sistema permite registrar várias compras seguidas e, ao ser encerrado, mostra um resumo do dia com a quantidade de compras, o total bruto, o total de descontos concedidos e o total final.

## Como ele faz

1. O programa exibe um menu com duas opções: `1` para registrar uma compra e `0` para fechar o sistema.
2. Ao escolher `1`, o código pede o valor da compra e a idade do cliente. Se algum deles for negativo ou zero, exibe um aviso e pede de novo.
3. O valor original é guardado na lista `compras` com `.append()`.
4. O valor final (`z`) começa igual ao valor original.
5. Se a idade for maior ou igual a 65, calcula 20% do valor, subtrai do valor final e guarda o desconto na lista `descontos`.
6. Em seguida, se o valor final (já com o desconto de idade, se houver) for maior que 100, calcula 10% sobre ele, subtrai e guarda esse desconto também na lista `descontos`.
7. Mostra o valor final da compra formatado em reais, com duas casas decimais.
8. O menu volta a aparecer até o usuário escolher `0`.
9. Ao encerrar, o código soma a lista `compras` (total bruto), soma a lista `descontos` (total de descontos) e subtrai um do outro para obter o total final. Depois mostra o resumo junto com a quantidade de compras registradas.

Os dois descontos são verificados com dois `if` independentes (sem `else`), então podem se acumular na mesma compra. O segundo `if` usa o valor já descontado, e não o original.

## Como rodar

```bash
python pdv.py
```

Os valores decimais devem ser digitados com ponto (ex.: `101.50`).

## Tabela de exemplos

| # | Valor (R$) | Idade | Desconto idade | Desconto valor | Valor final esperado |
|---|---|---|---|---|---|
| 1 | 50.00 | 30 | 0% | 0% | R$ 50.00 |
| 2 | 100.00 | 30 | 0% | 0% | R$ 100.00 |
| 3 | 80.00 | 65 | 20% | 0% | R$ 64.00 |
| 4 | 100.00 | 70 | 20% | 0% | R$ 80.00 |
| 5 | 125.00 | 70 | 20% | 0% | R$ 100.00 |
| 6 | 200.00 | 30 | 0% | 10% | R$ 180.00 |
| 7 | 101.00 | 30 | 0% | 10% | R$ 90.90 |
| 8 | 200.00 | 65 | 20% | 10% | R$ 144.00 |
| 9 | 1000.00 | 80 | 20% | 10% | R$ 720.00 |
| 10 | 200.00 | 64 | 0% | 10% | R$ 180.00 |

Todos os 10 casos foram testados e produzem o valor final esperado.

Rodando os 10 casos em sequência, o resumo final é:

```
Quantidade de compras registradas: 10
Total bruto: R$2156.00
Total de descontos concedidos: R$447.10
Total final: R$1708.90
```
