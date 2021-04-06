# Instruções

## Local

```bash
python -m Pyro4.naming
python system.py
python core.py
```

## Remoto

```bash
python -m Pyro4.naming
python system.py --remote -host 'your_host' -port 'your_port'
python core.py --remote -host 'your_host' -port 'your_port'
```

## Tempo de comunicação

O tempo de comunicação entre o cliente e o servidor é calculado automaticamente pelo Sistema Operacional.

* **Windows Powershell:** ```Measure-Command {python .\src\core.py | Out-Default}```;

## Observações importantes
> O sistema, de forma padrão, imprime apenas o tempo de 20 execuções para cada operação, em milissegundos. Caso você queira que sejam impressas as saídas de cada operação, é só remover o *#* que comenta os prints dessas operações.

> Certifique-se de que os outros dois scripts, *namespace* e servidor, estão rodando antes de iniciar o `core.py`.

> Se você estiver tendo o erro **'type' object is not subscriptable**, use o Python 3.9 ou copie os arquivos da pasta `older/` para esta.
