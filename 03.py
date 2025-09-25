from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, valor: float):
        self.valor = valor

    @abstractmethod
    def processar_pagamento(self):
        raise NotImplementedError("Erro")

class PagamentoPix(Pagamento):
    def __init__(self, valor):
        super().__init__(valor)

    def processar_pagamento(self):
        print("Pagamento via Pix processado com sucesso!")

class PagamentoDinheiro(Pagamento):
    def __init__(self, valor):
        super().__init__(valor)

    def processar_pagamento(self):
        print("Pagamento em dinheiro processado com sucesso!")
           
