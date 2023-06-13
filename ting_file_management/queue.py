from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._data = list()

    def __len__(self):
        if len(self._data) == 0:
            return 0
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if len(self._data) == 0:
            return None
        return self._data.pop(0)

    def search(self, index):
        if len(self._data) <= 0 or (index
                                    is None) or not (0 <= index
                                                     < len(
                                                         self._data)
                                                     ) or not isinstance(
                index, int):
            raise IndexError("Índice Inválido ou Inexistente")
        return self._data[index]


if __name__ == "__main__":
    testeQ = Queue()
    # testeQ.enqueue(3)
    # testeQ.enqueue(7)
    # testeQ.enqueue(5)
    testeQ.search(len(testeQ))
