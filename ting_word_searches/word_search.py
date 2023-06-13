# from ting_file_management.queue import Queue
# from ting_file_management.file_process import process


def check_dict_for_exists_word(the_dict, word):
    ocorrencia = [{"linha": idx + 1} for idx in range(len(
        the_dict["linhas_do_arquivo"]
    )) if word in the_dict["linhas_do_arquivo"][idx].lower()]

    if len(ocorrencia) <= 0:
        return

    new_dict = {
        "palavra": word,
        "arquivo": the_dict["nome_do_arquivo"],
        "ocorrencias": ocorrencia
    }

    return new_dict


def exists_word(word, instance):
    new_value = [check_dict_for_exists_word(
        instance.search(idx), word.lower()) for idx in range(
        len(instance)) if check_dict_for_exists_word(
        instance.search(idx), word.lower()) is not None]

    return new_value


def check_dict_for_search_by_word(the_dict, word):
    ocorrencia = [{
        "linha": idx + 1,
        "conteudo": the_dict["linhas_do_arquivo"][idx]
    } for idx in range(len(
        the_dict["linhas_do_arquivo"]
    )) if word in the_dict["linhas_do_arquivo"][idx].lower()]

    if len(ocorrencia) <= 0:
        return

    new_dict = {
        "palavra": word,
        "arquivo": the_dict["nome_do_arquivo"],
        "ocorrencias": ocorrencia
    }

    return new_dict


def search_by_word(word, instance):
    new_value = [check_dict_for_search_by_word(
        instance.search(idx), word.lower()) for idx in range(
        len(instance)) if check_dict_for_search_by_word(
        instance.search(idx), word.lower()) is not None]

    return new_value


# if __name__ == "__main__":
#     text_search_by_word = [
#         {
#             "palavra": "pedro",
#             "arquivo": "statics/nome_pedro.txt",
#             "ocorrencias": [
#                 {
#                     "linha": 1,
#                     "conteudo": "Aqui contem um texto que fala sobre um menino pobre chamado Pedro.",  # noqa
#                 },
#                 {
#                     "linha": 3,
#                     "conteudo": "Pedro tinha uma amiga chamada Carol.",  # noqa
#                 }
#             ],
#         }
#     ]
#     project = Queue()
#     process("statics/nome_pedro.txt", project)
#     word = search_by_word("pedro", project)
#     print(word)
#     assert word == text_search_by_word
#     assert len(project) == 1
