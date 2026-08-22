import pandas as pd
import json
import google.generativeai as genai
import os

# Configura a chave da API do Gemini/OpenAI
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

# URL do CSV publicado na Web do Google Sheets
SHEETS_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS86DigxOpfYf-Bets0K82F4mc9Z_FyvTR05Wu9F6P959q37-q788JZiV6IWofvJTZ1DGeGY6Om3aHZ/pub?gid=0&single=true&output=csv"

def generate_seo_description(name, base_desc):
    prompt = f"Melhore a seguinte descrição de produto para um e-commerce estático, deixando-a atraente e curta (máximo 200 caracteres). Produto: {name}. Descrição: {base_desc}"
    response = model.generate_content(prompt)
    return response.text.strip()

def main():
    # 1. Ler a planilha
    df = pd.read_csv(SHEETS_URL)
    
    products = []
    for _, row in df.iterrows():
        # Usa IA para melhorar/otimizar as descrições automaticamente
        ai_desc = generate_seo_description(row['Nome'], row['Descrição Base'])
        
        products.append({
            "name": row['Nome'],
            "price": row['Preço'],
            "description": ai_desc,
            "image": row['URL da Imagem']
        })
    
    # 2. Salvar como JSON para ser lido pelo JavaScript do seu site
    with open("products.json", "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()