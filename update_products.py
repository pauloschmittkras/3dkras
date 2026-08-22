import pandas as pd
import json
import os
from google import genai

# Configura o cliente do Gemini (SDK atual)
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
MODEL_NAME = "gemini-2.5-flash"

# URL do CSV publicado na Web do Google Sheets
SHEETS_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS86DigxOpfYf-Bets0K82F4mc9Z_FyvTR05Wu9F6P959q37-q788JZiV6IWofvJTZ1DGeGY6Om3aHZ/pub?gid=0&single=true&output=csv"


def generate_seo_description(name, base_desc):
    prompt = (
        "Melhore a seguinte descrição de produto para um e-commerce estático, "
        "deixando-a atraente e curta (máximo 200 caracteres). "
        f"Produto: {name}. Descrição: {base_desc}"
    )
    response = client.models.generate_content(model=MODEL_NAME, contents=prompt)
    return response.text.strip()


def main():
    # 1. Ler a planilha (apenas Nome e Descricao)
    df = pd.read_csv(SHEETS_URL, encoding="utf-8")
    print(df.columns)

    products = []
    for _, row in df.iterrows():
        nome = row["Nome"]
        descricao_base = row["Descricao"]

        # Usa IA para melhorar/otimizar a descrição automaticamente
        ai_desc = generate_seo_description(nome, descricao_base)

        products.append({
            "name": nome,
            "description": ai_desc,
        })

    # 2. Salvar como JSON para ser lido pelo JavaScript do site
    with open("products.json", "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()