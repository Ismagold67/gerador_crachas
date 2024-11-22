# Gerador Automático de Crachás(PT-Br)

## 📋 Descrição do Projeto

Este script Python automatiza a geração de crachás personalizados a partir de uma planilha Excel, criando cartões de identificação únicos para cada funcionário.

## 🛠️ Requisitos de Sistema

- Python 3.8+
- Bibliotecas:
  - pandas
  - Pillow (PIL)
  - python-barcode
  - openpyxl (para leitura de Excel)

## 📦 Instalação

1. Clone o repositório:
```bash
git clone https://seu-repositorio/gerador-crachas.git
cd gerador-crachas
```

2. Crie um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install pandas pillow python-barcode openpyxl
```

## 📂 Estrutura de Pastas

```
projeto-gerador-crachas/
│
├── app.py
├── dados.xlsx
├── fonts/
│   ├── Anton/
│   └── Poppins/
├── template/
│   └── modelo_cracha.png
├── output_folder/
└── bar_codes/
```

## ⚙️ Configuração

### Planilha de Dados
Seu arquivo `dados.xlsx` deve conter as seguintes colunas:
- Nome
- Funcao
- ID
- Email
- Endereco
- Telefone

### Modelo de Crachá
Coloque seu template de crachá em `template/modelo_cracha.png`

### Fontes
O script usa duas fontes:
- `fonts/Anton/Anton-Regular.ttf` (para Nome)
- `fonts/Poppins/Poppins-Regular.ttf` (para outros campos)

## 🚀 Como Usar

1. Prepare sua planilha `dados.xlsx`
2. Verifique o template do crachá
3. Execute o script:
```bash
python app.py
```

Os crachás gerados serão salvos na pasta `output_folder/`

## 🔍 Personalização

Para alterar posicionamentos e estilos, edite as configurações no dicionário `POSICOES` no `app.py`.

## ⚠️ Possíveis Erros

- Verifique se todas as colunas necessárias estão presentes na planilha
- Confirme a existência dos arquivos de fonte
- Certifique-se de que o template de crachá está disponível

## 📄 Licença

MIT License

Copyright (c) 2024 Ismael Roberto

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## 🤝 Contribuições

Pull requests são bem-vindos. Para mudanças importantes, abra primeiro uma issue para discutir o que você gostaria de modificar.

# Automatic Badge Generator(US)

## 📋 Project Description

This Python script automates the generation of personalized badges from an Excel spreadsheet, creating unique identification cards for each employee.

## 🛠️ System Requirements

- Python 3.8+
- Libraries:
  - pandas
  - Pillow (PIL)
  - python-barcode
  - openpyxl (for Excel reading)

## 📦 Installation

1. Clone the repository:
```bash
git clone https://your-repository/badge-generator.git
cd badge-generator
```

2. Create a virtual environment (optional, but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install pandas pillow python-barcode openpyxl
```

## 📂 Folder Structure

```
badge-generator-project/
│
├── app.py
├── dados.xlsx
├── fonts/
│   ├── Anton/
│   └── Poppins/
├── template/
│   └── modelo_cracha.png
├── output_folder/
└── bar_codes/
```

## ⚙️ Configuration

### Data Spreadsheet
Your `dados.xlsx` file must contain the following columns:
- Nome (Name)
- Funcao (Role)
- ID
- Email
- Endereco (Address)
- Telefone (Phone)

### Badge Template
Place your badge template in `template/modelo_cracha.png`

### Fonts
The script uses two fonts:
- `fonts/Anton/Anton-Regular.ttf` (for Name)
- `fonts/Poppins/Poppins-Regular.ttf` (for other fields)

## 🚀 How to Use

1. Prepare your `dados.xlsx` spreadsheet
2. Verify the badge template
3. Run the script:
```bash
python app.py
```

Generated badges will be saved in the `output_folder/`

## 🔍 Customization

To change positioning and styles, edit the settings in the `POSICOES` dictionary in `app.py`.

## ⚠️ Possible Errors

- Verify that all required columns are present in the spreadsheet
- Confirm the existence of font files
- Ensure the badge template is available

## 📄 License

MIT License

Copyright (c) [year] [full name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## 🤝 Contributions

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to modify.

