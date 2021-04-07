# Instruções

Primeiro, inicie o *namespace*.

```bash
python -m Pyro4.naming
```

Agora é so iniciar o servidor (`system`) e realizar as operações através do cliente (`core`).


```bash
# Servidor Local
python system.py
python core.py

# Servidor Remoto
python system.py --remote -host 'your_host' -port 'your_port'
python core.py --remote -host 'your_host' -port 'your_port'
```

## Tempo de comunicação

O tempo de comunicação entre o cliente e o servidor é calculado automaticamente pelo Sistema Operacional.

* **Windows Powershell:** ```Measure-Command {python .\src\core.py | Out-Default}```;
* **Linux Terminal:** ```time python core.py```.

#### Exemplo

```bash
time python core.py --remote -host **.*.*.* -port ****
________________________________________________________
Executed in   73.79 millis    fish           external
   usr time   57.01 millis  153.00 micros   56.86 millis
   sys time   13.43 millis   39.00 micros   13.39 millis
```

## Observações importantes
1. O sistema, de forma padrão, imprime apenas o tempo de 20 execuções para cada operação, em milissegundos. Caso você queira que sejam impressas as saídas de cada operação, utilize o argumento `--verbose`.

2. Certifique-se de que os outros dois scripts, *namespace* e servidor, estão rodando antes de iniciar o `core.py`.

## 'type' object is not subscriptable.

Se você estiver tendo este erro, certifique-se de estar utilizando o Python 3.9, pois o *typing* utilizado nos métodos das classes não são suportados por versões mais antigas.

Se você não pretende atualizar o Python agora, utilize os arquivos da pasta `older/`. Desse modo os comandos listados acima ficarão um pouco diferentes:

```bash
python older/system.py
python older/core.py
```

```bash
python older/system.py --remote -host 'your_host' -port 'your_port'
python older/core.py --remote -host 'your_host' -port 'your_port'
```

## Argumentos

```bash
➜  src git:(main) ✗ python core.py --help
Usage: core.py [OPTIONS]

Options:
  --verbose
  --remote
  -host TEXT
  -port INTEGER
  --help         Show this message and exit.
```
