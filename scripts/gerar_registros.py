import random
from datetime import datetime, timedelta

class GeradorDeRegistros:
    def __init__(self, moradores, empresas, status):
        self.moradores = moradores
        self.empresas = empresas
        self.status = status
    
   # Função para gerar datas aleatórias no mês de setembro de 2024
    
    def gerar_data(self):
        start_date = datetime(2024, 9, 1)
        end_date = datetime(2024, 9, 30)
        delta = end_date - start_date
        random_days = random.randint(0, delta.days)
        date = start_date + timedelta(days=random_days)
        return date.strftime("%d-%m-%Y")

    def gerar_registro(self):
        nome = random.choice(self.moradores)
        pacote_empresa = random.choice(self.empresas)
        pacote = f"Pacote da {pacote_empresa}"
        data_entrega = self.gerar_data();
        status = random.choice(self.status)

        return {
            "morador": nome,
            "pacote": pacote,
            "recebido": data_entrega,
            "status": status
        }
    
    def gerar_registros(self, n=10):
        return [self.gerar_registro() for _ in range(n)]

    def exibir_registros(self, registros):
        for i, registro in enumerate(registros, 1):
            print(f"Registro {i}: {registro['morador']}, {registro['pacote']}, Entregue: {registro['recebido']}, Status: {registro['status']} ")
    