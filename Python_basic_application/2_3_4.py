class multifilter:
    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        if pos >= neg:
            return True
        else:
            return False

    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        if pos >= 1:
            return True
        else:
            return False

    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        if neg == 0:
            return True
        else:
            return False

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.func = funcs
        self.judge = judge
        self.count = 0

    def __iter__(self):
        # возвращает итератор по результирующей последовательности
        return self

    def __next__(self):
        neg = 0
        pos = 0
        if self.count < len(self.iterable):
            tmp = self.count
            self.count += 1
            for i in self.func:
                if i(self.iterable[tmp]):
                    pos += 1
                else:
                    neg += 1
            if self.judge(pos, neg):
                return self.iterable[tmp]
            else:
                return next(self)
        else:
            raise StopIteration




def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0


a = [i for i in range(0, 50)]

print(list(multifilter(a, mul2, mul3, mul5)))
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# [0, 6, 10, 12, 15, 18, 20, 24, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
# [0, 30]
