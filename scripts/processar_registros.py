from datetime import datetime

class ProcessarRegistros:
    def __init__(self, registros):
        self.registros = registros

# Função para ordenar o dicionário por data
    def ordenar_por_data(self, lista_registros):
        lista_ordenada = sorted( lista_registros, key=lambda x: datetime.strptime(x['recebido'], '%d-%m-%Y'))
        return lista_ordenada
    
    def gerar_relatorio(self):
        total_aguardando_coleta = 0
        total_coletado = 0

        entregas_ordenadas = self.ordenar_por_data(self.registros)

        for registro in self.registros:
            if registro['status'] == "Aguardando":
                total_aguardando_coleta += 1
            else:
                total_coletado += 1

        # Criando o relatório
        relatorio = {
            "total_registros": len(self.registros),
            "total_aguardando_coleta": total_aguardando_coleta,
            "total_coletado": total_coletado,
            "detalhes_entregas": entregas_ordenadas,
        }
        
        return relatorio
