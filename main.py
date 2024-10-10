from scripts.gerar_registros import GeradorDeRegistros
from scripts.processar_registros import ProcessarRegistros
from scripts.salvar_relatorio import GerarPdf

# Lista de nomes fictícios para os moradores
NOMES = [
    "Jonh Harper", "Cloud Strife", "John Shepard", "Maria Silva", "Carlos Eduardo",
    "Fernanda Lima", "Lucas Oliveira", "Bruna Souza", "Pedro Henrique", "Camila Costa",
    "Rafael Gomes", "Juliana Pereira", "Gustavo Fernandes", "Laura Martins", "Felipe Rocha",
    "Ana Paula", "Marcos Vinícius", "Bianca Castro", "Leonardo Dias", "Sabrina Almeida",
    "Diego Barbosa", "Letícia Ribeiro", "Vitor Henrique", "Patrícia Sousa", "Thiago Nascimento",
    "Amanda Melo", "Bruno Teixeira", "Isabela Martins", "Ricardo Cardoso", "Sofia Pinto",
    "Daniel Lima", "Larissa Gomes", "Eduardo Silva", "Gabriela Santos", "Fábio Costa",
    "Renata Oliveira", "Murilo Ferreira", "Caroline Alves", "Matheus Rocha", "Juliana Dias",
    "Andréia Ribeiro", "Samuel Souza", "Natália Martins", "Victor Henrique", "Mariana Castro",
    "Leonardo Almeida", "Priscila Sousa", "Henrique Nascimento", "Bianca Pinto", "Bruno Melo"
]

# Lista de empresas para os pacotes
EMPRESAS = [
    "Amazon", "Boticário", "N2 Industries", "Apple", "Samsung", "Mercado Livre",
    "Magazine Luiza", "Submarino", "Americanas", "Extra", "Netshoes", "Casas Bahia",
    "Renner", "C&A", "Lojas Americanas", "Ponto Frio", "Fast Shop", "Kalunga",
    "Saraiva", "Livraria Cultura"
]

# Lista de status possíveis
STATUS = [
    "Aguardando",
    "Coletado"
]

def main():
    # Instanciando a classe GeradorDeRegistros
    gerador = GeradorDeRegistros(NOMES, EMPRESAS, STATUS)
    
    # Gerando quantidade de registros aleatórios desejado passando um número inteiro como parametro
    # @param [integer] numero de registros desejado
    registros = gerador.gerar_registros(100)
    
    # Exibindo os registros gerados (Opcional)
    # gerador.exibir_registros(registros)

    # Instanciando a classe ProcessarRegistros
    processador = ProcessarRegistros(registros)
    
    # Gerando o relatório
    relatorio = processador.gerar_relatorio()

    # Salvar o relatório em PDF
    relatorio_pdf = GerarPdf(relatorio)
    relatorio_pdf.gerar_relatorio_pdf()

# Executar apenas se o script for executado diretamente
if __name__ == "__main__":
    main()