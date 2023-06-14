# Boas-vindas ao repositório do Projeto TING (Trybe Is Not Google)!

## Contextualizando

O projeto é um sistema de gerenciamento de "banco de dados". Porém, ele faz acessos a arquivos de .txt, e gerencia os mesmos. Para isso, ele conta com um algoritmo de fila FIFO (First in First Out), algoritmo de fila de prioridades, e gerenciamento de arquivos.

## Instalação

Instalação do projeto

```bash
  git clone git@github.com:vicsantus/Projeto-TING.git
  cd Projeto-TING
  python3 -m venv .venv && source .venv/bin/activate
  python3 -m pip install -r dev-requirements.txt
```

## Funcionalidades

### **Dentro da pasta ting_file_management existe:**

- O arquivo **queue.py** é uma classe de gerenciamento de fila FIFO.

- O arquivo **priority_queue.py** é uma classe de gerenciamento de fila com prioridades, tendo alguns arquivos mais prioridades que outros.

- O arquivo **file_process.py** contém 3 funções:

_process - é a função que adiciona dentro da fila, o arquivo de texto processado por ela;_

_remove - é a função que remove dentro da fila o primeiro elemento;_

_file_metadata - é a função que mostra um elemento expecifico da fila com um index expecifico._

- O arquivo **file_management.py** é uma função que importa o .txt transformando as linhas do arquivo em uma lista de strings.

- O arquivo **abstract_queue.py** é uma classe abstrata de Queue.

### **Dentro da pasta ting_word_searches existe:**

- O arquivo **word_search.py** que tem duas funções:

_exists_word - Faz uma pesquisa na queue e retorna em quantas linhas aconteceram ocorrências de qualquer palavra passada no parâmetro da função;_

_search_by_word - Faz uma pesquisa na queue e retorna em quantas linhas, e também quais linhas aconteceram ocorrências de qualquer palavra passada no parâmetro da função;_

### **Dentro da pasta tests em priority_queue existe:**

- O arquivo **test_priority_queue.py** realiza testes da função priority_queue.

## Stack utilizada

**Back-end:** Python, Algoritmos, FIFO, FILO, Computer Science, PyTest
