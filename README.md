# Sistemas Distribuídos: P1 (Pyro)

## Instalação

```bash
git clone https://github.com/Helgras/P1.git
cd P1/
pip install -r requirements.txt
```

> Instruções para iniciar o server na pasta `src`.

### Virtual Enviroment (Opcional)

Crie um novo *enviroment*:

```bash
virtualenv p1env
```

Ative o ambiente recém-criado:

* Windows CMD

```bash
p1env\Scripts\activate.bat
```

* Windows Powershell

```bash
p1env\Scripts\activate.ps1
```

* Linux

```bash
cd source p1env/bin/activate
```

## Dependências

* Python>=3.8

> Recomendado: Python 3.9

* Pyro==4.80
* Json==2.0.9
