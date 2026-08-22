import pandas as pd
import json

# URL do CSV publicado na Web do Google Sheets
SHEETS_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS86DigxOpfYf-Bets0K82F4mc9Z_FyvTR05Wu9F6P959q37-q788JZiV6IWofvJTZ1DGeGY6Om3aHZ/pub?gid=0&single=true&output=csv"


def main():
    # 1. Ler a planilha (apenas Nome e Descricao)
    df = pd.read_csv(SHEETS_URL, encoding="utf-8")
    print(df.columns)

    products = []
    for _, row in df.iterrows():
        products.append({
            "name": row["Nome"],
            "description": row["Descricao"],
        })

    # 2. Salvar como JSON para ser lido pelo JavaScript do site
    with open("products.json", "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()