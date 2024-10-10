from fpdf import FPDF

class GerarPdf:
    def __init__(self, relatorio):
        self.relatorio = relatorio

    # Função para criar o relatório em PDF
    def gerar_relatorio_pdf(self):
        pdf = FPDF()
        pdf.add_page()

        # Definindo a fonte
        pdf.set_font('Arial', 'B', 14)

        # Título
        pdf.cell(200, 10, txt='Relatório de Entregas na Portaria', ln=True, align='C')
        pdf.ln(10)

        # Informações gerais
        pdf.set_font('Arial', '', 12)
        pdf.cell(0, 6, f"Total de Registros: {self.relatorio['total_registros']}", ln=True)
        pdf.cell(0, 6, f"Total Aguardando Coleta: {self.relatorio['total_aguardando_coleta']}", ln=True)
        pdf.cell(0, 6, f"Total Coletado: {self.relatorio['total_coletado']}", ln=True)
        pdf.ln(10)

        # Cabeçalho da tabela com tom escuro
        pdf.set_font('Arial', 'B', 12)
        pdf.set_text_color(50, 50, 50)  # Tom escuro
        pdf.cell(60, 7, 'Morador', border=1)
        pdf.cell(50, 7, 'Pacote', border=1)
        pdf.cell(30, 7, 'Recebido', border=1, align='C')
        pdf.cell(40, 7, 'Status', border=1, align='C')
        pdf.ln()

        # Resetando para o texto padrão
        pdf.set_font('Arial', '', 12)
        pdf.set_text_color(0, 0, 0)

        # Adicionando os detalhes das entregas
        for entrega in self.relatorio['detalhes_entregas']:
            pdf.cell(60, 7, entrega['morador'], border=1)
            pdf.cell(50, 7, entrega['pacote'], border=1)
            pdf.cell(30, 7, entrega['recebido'], border=1, align='C')
            pdf.cell(40, 7, entrega['status'], border=1, align='C')
            pdf.ln()

        # Salvando o arquivo PDF
        pdf.output('relatorio_portaria.pdf')
        print("Relatório salvo com sucesso!")