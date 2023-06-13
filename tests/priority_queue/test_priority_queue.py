import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    projeto = PriorityQueue()
    projeto.enqueue({"valor": 'Jorgin', "qtd_linhas": 16})
    projeto.enqueue({"valor": 'Setinha', "qtd_linhas": 5})
    assert len(projeto) == 2
    projeto.dequeue()
    assert len(projeto) == 1
    assert projeto.search(0) == {"valor": 'Setinha', "qtd_linhas": 5}
    projeto.enqueue({"valor": 'Setinha', "qtd_linhas": 2})
    projeto.enqueue({"valor": 'Eli', "qtd_linhas": 1})
    assert projeto.search(2) == {"valor": 'Setinha', "qtd_linhas": 5}
    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        projeto.search(-1)
