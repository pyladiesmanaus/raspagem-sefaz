# Raspagem Sefaz
Repositório de Raspagem de dados de despesas expostas no site da Sefaz-AM

### Descrição do Repositório

* Análise.html : notebook salvo em html
* Analise.ipynb : jupyter notebook
* scraping-sefaz.py : script de Raspagem
* output : pasta com arquivos e gráficos de saída

### What's included

Within the download you'll find the following directories and files:
```sh
Raspagem Sefaz
├── Análise.html
├── Análise.ipynb
├── LICENSE
├── README.md
├── output
│   ├── graficos
│   │   ├── barra-a-pagar.png
│   │   └── linha-total.png
│   ├── sefaz-Fonte\ de\ Recurso.csv
│   ├── sefaz-Função.csv
│   ├── sefaz-fonte-final.csv
│   └── sefaz-fonte-total.csv
├── scraping-sefaz.py
└── selenium-step-by-step.txt
```

## Preparação de ambiente

### Ubuntu
1. Instalar python 3

```sh
$ sudo apt install python3 python3-pip
```

2. Instalar bibliotecas

```sh
$ sudo pip3 install selenium pandas seaborn jupyter matplotlib
```

3. Baixar o driver do selenium para seu navegador [aqui](https://selenium-python.readthedocs.io/installation.html)
4. copiar o executável para `/usr/bin`

### Windows

#### 1. Instalar python

Acesse [python.org](https://www.python.org/downloads/windows/) e baixe a opção "Latest Python 3 Release - Python 3.7.3".

#### 2. Teste sua instalação

Abra o terminal clicando em Iniciar -> Digite cmd
Quando abrir, digite python e dê enter. Se estiver tudo ok, deve aparecer:

" Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) MSC v.1914 64 bit (AMD64) on win32

Type "help", "copyright", "credits" or "license" for more information. "

Se aparecer

"Python is not recognized as an internal or external command, operable program or batch file."

Então você deve adicionar o python às suas variáveis.

##### Etapas para adicionar um caminho na variável ambiental PATH do sistema

     1. No sistema Windows, clique com o botão direito em Meu Computador ou Este PC.
     2. Selecione Propriedades.
     3. Selecione configurações avançadas do sistema.
     4. Clique no botão Variáveis de Ambiente.
     5. Em Variáveis do sistema, selecione PATH.
     6. Clique no botão Editar.
     7. Clique no botão Novo
     8. Cole o caminho do arquivo python.exe -- C:\Python37 e C:\Python37/Scripts, separados por ```;```.
     9.Clique OK.
#### 3. Instalar pip
Para isto, baixe o arquivo em https://bootstrap.pypa.io/get-pip.py

Abra o terminal clicando com o botão direito no espaço vazio da pasta em que o arquivo está, e depois em "Abrir Terminal".

Em seguida, execute

```sh
$ python get-pip.py
```

Mais informações de instalaçao [aqui](http://pythonclub.com.br/instalacao-python-django-windows.html)

#### 4. Instalar bibliotecas
Abra o terminal cnforme descrito na seção 2 e digite:

```sh
$ pip install -r requirements.txt
```

#### 5. Baixe a engine do selenium
Encontre a engine do selenium para seu navegador [aqui](https://selenium-python.readthedocs.io/installation.html) e realize o download

#### 6. Adicione a engine ao seu path
Adicione o executável da engine às variáveis do ambiente do seu sistema de maneira análoga à descrita na seção 2.

## Executando o projeto

#### 1. Rodar o arquivo scraping-sefaz.py

Abrir o terminal na pasta do projeto e executar:
```sh
$ python3 scraping-sefaz.py
```

#### 2. Análise

Abrir o jupyter

```sh
$ jupyter notebook
```

Abrir o arquivo `Análise.ipynb`

Para rodar as células, SHIFT + ENTER
