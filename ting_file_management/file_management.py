import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        print("Formato inválido", file=sys.stderr)
        return None
    try:
        with open(path_file, 'r') as arquivo:
            linhas = [linha.strip() for linha in arquivo.readlines()]
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return None

    print(linhas)
    return linhas


if __name__ == "__main__":
    txt_importer("statics/arquivo_teste.txt")
