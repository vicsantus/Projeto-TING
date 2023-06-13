from ting_file_management.file_management import txt_importer
import sys
from ting_file_management.queue import Queue


def process(path_file, instance):
    for idx in range(len(instance)):
        if instance.search(idx)["nome_do_arquivo"] == path_file:
            return
    linhas = txt_importer(path_file)
    dados_arquivo = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(linhas),
        "linhas_do_arquivo": linhas
    }
    instance.enqueue(dados_arquivo)
    print(dados_arquivo)


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos")
        return
    deleted_value = instance.dequeue()
    path = deleted_value['nome_do_arquivo']
    print(f"Arquivo {path} removido com sucesso")


def file_metadata(instance, position):
    try:
        element = instance.search(position)
        print(element)
    except IndexError:
        print("Posição inválida", file=sys.stderr)


if __name__ == '__main__':
    project = Queue()
    process("statics/novo_paradigma_globalizado-min.txt", project)
    file_metadata(project, 0)
