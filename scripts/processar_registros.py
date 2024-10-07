class ProcessarRegistros:
    def __init__(self, dict):
        self.dict = dict

    def mostrar_registros(self):
        morador = {}
        empresa = {}
        for index, regist in enumerate(self.dict):
            morador[regist['morador']] = morador.get(regist['morador'], 0) + 1
            # empresa[regist['pacote']] = empresa.get(regist['pacote'], 0) + 1
        return morador
        