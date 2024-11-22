import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import unicodedata
from barcode import Code128  # Tipo de código de barras
from barcode.writer import ImageWriter  # Para salvar como imagem
import os
from io import BytesIO

# Configurações iniciais
output_folder = "output_folder/"  # Pasta para salvar os crachás gerados
spreadsheet = "dados.xlsx"  # Caminho do arquivo Excel com as informações dos funcionários
custom_font_path = [
    "fonts/Anton/Anton-Regular.ttf", 
    "fonts/Poppins/Poppins-Regular.ttf"
]  # Fonte personalizada para o texto
qr_code_folder = "bar_codes/"  # Pasta onde estão os códigos de barra
template_image = "template/modelo_cracha.png"  # Arquivo PNG usado como modelo de crachá

# Criar a pasta de saída (se não existir)
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Verificar se o template existe
if not os.path.exists(template_image):
    raise FileNotFoundError(f"O template '{template_image}' não foi encontrado. Coloque um arquivo de modelo na pasta.")

# Carregar a planilha
df = pd.read_excel(spreadsheet)  # Certifique-se de que o Excel tem as colunas certas

# Verificar se as colunas necessárias existem na planilha
required_columns = ["Nome", "Funcao", "ID", "Email", "Endereco", "Telefone"]  # Nomes das colunas exigidas no Excel
for col in required_columns:
    if col not in df.columns:
        raise ValueError(f"A coluna '{col}' deve estar presente na planilha Excel.")

def remover_acentos(texto):
    return ''.join(
        char for char in unicodedata.normalize('NFD', texto)
        if unicodedata.category(char) != 'Mn'
    )

# Gerar o código de barras
def gerar_codigo_de_barras_memoria(conteudo):
    writer = ImageWriter()
    buffer = BytesIO()
    conteudo = remover_acentos(conteudo)
    codigo_barras = Code128(conteudo, writer=writer)
    codigo_barras.write(buffer)  # Escreve no buffer em memória
    buffer.seek(0)  # Retorna ao início do buffer
    return Image.open(buffer)  # Retorna a imagem PIL do código de barras

# Configurações de posicionamento para a imagem
POSICOES = {
    'ID': {  # Posição e estilo do Nome
        'x': 210,  # Posição X
        'y': 248,  # Posição Y
        'tamanho_fonte': 20,  # Tamanho da fonte
        'cor': (0, 0, 0)  # Cor do texto (branco)
    },
    'Nome': {  # Posição e estilo do Nome
        'x': 63,  # Posição X
        'y': 54,  # Posição Y
        'tamanho_fonte': 60,  # Tamanho da fonte
        'cor': (0, 0, 0)   # Cor do texto (branco)
    },
    'Funcao': {  # Posição e estilo da Funcao
        'x': 63,
        'y': 125,
        'tamanho_fonte': 50,
        'cor': (0, 0, 0) 
    },
    'Email': {  # Posição e estilo da Funcao
        'x': 210,
        'y': 278,
        'tamanho_fonte': 20,
        'cor': (0, 0, 0) 
    },
    'Endereco': {  # Posição e estilo da Funcao
        'x': 210,
        'y': 308,
        'tamanho_fonte': 20,
        'cor': (0, 0, 0) 
    },
    'Telefone': {  # Posição e estilo da Funcao
        'x': 210,
        'y': 338,
        'tamanho_fonte': 20,
        'cor': (0, 0, 0) 
    },
    'bar_code': {  # Posição e tamanho do QR Code
        'x': 63,  # Posição X
        'y': 430,   # Posição Y
        'largura': 300,   # Largura desejada
        'altura': 100     # Altura desejada
    }
}

for font in custom_font_path:
    if not os.path.exists(font):
        raise FileNotFoundError(f"Fonte '{font}' não encontrada.")
    
def fonts_config(fild_list, att_list, POSICOES, Nome, custom_font_path, draw):
    for x, fild in enumerate(fild_list):
        if fild not in POSICOES:
            raise KeyError(f"O campo '{fild}' não está definido em POSICOES.")
        
        fild_font = ImageFont.truetype(
            custom_font_path[0] if fild == 'Nome' else custom_font_path[1],
            POSICOES[fild]['tamanho_fonte']
        )
        
        text_value = Nome if fild == 'Nome' else str(att_list[x])  # Converte para string se necessário
        draw.text(
            (POSICOES[fild]['x'], POSICOES[fild]['y']),
            text_value,
            font=fild_font,
            fill=POSICOES[fild]['cor']
        )

# Gerar os cards personalizados
for index, row in df.iterrows():
    member_id = row['ID']  # ID do funcionário
    Nome = row['Nome']  # Nome da pessoa
    Funcao = row['Funcao']  # Função
    Email = row['Email']  # Email
    Endereco = row['Endereco']  # Endereço
    Telefone = row['Telefone']  # Telefone

    # Abrir o template
    card = Image.open(template_image).convert('RGBA')
    draw = ImageDraw.Draw(card)

    # Lista de campos e atributos
    fild_list = ['ID', 'Nome', 'Funcao', 'Email', 'Endereco', 'Telefone']
    att_list = [member_id, Nome, Funcao, Email, Endereco, Telefone]

    # Desenhar os textos
    fonts_config(fild_list, att_list, POSICOES, Nome, custom_font_path, draw)

    # Gerar o código de barras em memória
    conteudo_barcode = f"{Nome}-{Funcao}-{member_id}"  # Informações no código de barras
    barcode_img = gerar_codigo_de_barras_memoria(conteudo_barcode)

    # Redimensionar e colar o código de barras no crachá
    largura = POSICOES['bar_code']['largura']
    altura = POSICOES['bar_code']['altura']  # Ajuste proporcional
    barcode_img = barcode_img.resize((largura, altura), Image.Resampling.LANCZOS)
    barcode_img = barcode_img.convert("RGBA")

    # Criar uma máscara de transparência
    barcode_mask = barcode_img.split()[3] if barcode_img.mode == "RGBA" else None

    # Colar o código de barras no template
    card.paste(barcode_img, (POSICOES['bar_code']['x'], POSICOES['bar_code']['y']), barcode_mask)

    # Salvar o card gerado
    output_path = os.path.join(output_folder, f"{Nome}.png")
    card.save(output_path, "PNG")
    print(f"Gerado: {output_path}")

print("Todos os cards foram gerados com sucesso!")



