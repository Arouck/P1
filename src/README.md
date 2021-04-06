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

> Certifique-se de que os outros dois scripts, *namespace* e servidor, estão rodando antes de iniciar o `core.py`.

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
