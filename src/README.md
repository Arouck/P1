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

> Certifique-se de que os outros dois scripts, *namespace* e servidor, estão rodando antes de iniciar o `core.py`.
> Se você estiver tendo o erro **'type' object is not subscriptable**, use o Python 3.9 ou copie os arquivos da pasta `older/` para esta.
