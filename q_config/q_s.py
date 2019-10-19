class Q:
    def __init__(self, q, a, A, is_final):
        self.q = q
        self.a = a
        self.A = A
        self.is_final = is_final
    
    def get_q(self):
        return self.q


    def get_a(self):
        return self.a


    def get_A(self):
        return self.A


    def get_is_final(self):
        return self.is_final

q_list = [
    [
        Q('Артем гей?', [['Да', 'True'], ['Нет', 'False']], 'True', False),
        Q('Николай гей?', [['Да', 'True'], ['Нет', 'False']], 'False', False),
        Q('Темир гей?', [['Да', 'True'], ['Нет', 'False']], 'True', False),
        Q('Даниил гей?', [['Да', 'True'], ['Нет', 'False']], 'False', True),
    ]
]