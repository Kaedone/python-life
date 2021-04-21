# Импорты

import pickle  # Для реализации потоков

inf = float("inf")  # Создаём бесконечность


class Model:
    """""
        Наследуется от self
        Является оновным блоком выполнения кода
    """""

    def __init__(self):
        # Конструктор
        self.cells = {}
        self.minX = inf
        self.maxX = -inf
        self.minY = inf
        self.maxY = -inf

        # Создание матрицы и системы координат

    def insert_cell(self, posItion) -> None:
        # Реализация установки новой точки
        if (posItion not in self.cells) or (not self.cells[posItion][0]):
            # Проверяем, что там ничего не стоит
            x, y = posItion
            self.minX = min(x, self.minX)
            self.maxX = max(x, self.maxX)
            self.minY = min(y, self.minY)
            self.maxY = max(y, self.maxY)
            # Устанавливаем туда точку
            n = 0

            def neighbor(pos) -> int:
                # Проверяем на наличие "братьев"
                if pos in self.cells:
                    c1, c2 = self.cells[pos]
                    self.cells[pos] = (c1, c2 + 1)
                    return int(c1)
                else:
                    self.cells[pos] = (False, 1)
                    return 0

            n += neighbor((x - 1, y - 1))
            n += neighbor((x - 1, y))
            n += neighbor((x - 1, y + 1))
            n += neighbor((x, y - 1))
            n += neighbor((x, y + 1))
            n += neighbor((x + 1, y - 1))
            n += neighbor((x + 1, y))
            n += neighbor((x + 1, y + 1))
            #  Если есть, то прибавляем
            self.cells[posItion] = (True, n)

    def delete_cell(self, posItion) -> None:
        #  Реализуем удаление клеток
        if (posItion in self.cells) and (self.cells[posItion][0]):
            # Тут могут "испортиться" минимумы и максимумы, но мы это игнорируем
            x, y = posItion

            def dec_c2(pos):
                c1, c2 = self.cells[pos]
                self.cells[pos] = (c1, c2 - 1)

            # Реализуем игнорирование
            dec_c2((x - 1, y - 1))
            dec_c2((x - 1, y))
            dec_c2((x - 1, y + 1))
            dec_c2((x, y - 1))
            dec_c2((x, y + 1))
            dec_c2((x + 1, y - 1))
            dec_c2((x + 1, y))
            dec_c2((x + 1, y + 1))

            self.cells[posItion] = (False, self.cells[posItion][1])

    def clean(self) -> None:
        # Реализуем очистку поля
        self.minX = inf
        self.maxX = -inf
        self.minY = inf
        self.maxY = -inf
        new_cells = {}
        for posItion in iter(self.cells):
            if self.cells[posItion] != (0, 0):
                x, y = posItion
                self.minX = min(x, self.minX)
                self.maxX = max(x, self.maxX)
                self.minY = min(y, self.minY)
                self.maxY = max(y, self.maxY)
                new_cells[posItion] = self.cells[posItion]
        self.cells = new_cells
        #  Удаляем данные из матрицы

    def next_gen(self):
        # Создаём следующее поколение
        model = Model()
        for posItion in iter(self.cells):
            c1, c2 = self.cells[posItion]
            if (c2 == 3) or (c1 and c2 == 2):
                model.insert_cell(posItion)
        return model

    def save_to_file(self, name) -> None:
        #  Реализация сохранения данных
        file = open(name, 'wb')
        pickle.dump(self, file)
        file.close()

    def load_from_file(self) -> None:
        # Реализация загрузки файла
        file = open(self, 'rb')
        model = pickle.load(file)
        file.close()
        return model
