import pandas as pd
import json

SHEETS_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS86DigxOpfYf-Bets0K82F4mc9Z_FyvTR05Wu9F6P959q37-q788JZiV6IWofvJTZ1DGeGY6Om3aHZ/pub?gid=0&single=true&output=csv"


def main():
    df = pd.read_csv(SHEETS_URL, encoding="utf-8")
    print(df.columns)

    products = []
    for _, row in df.iterrows():
        raw_images = row["Imagens"]
        if pd.notna(raw_images):
            images = [img.strip() for img in str(raw_images).split(";") if img.strip()]
        else:
            images = []

        products.append({
            "name": row["Nome"],
            "description": row["Descricao"],
            "detail": row["Detalhe"],
            "images": images,
        })

    with open("products.json", "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()