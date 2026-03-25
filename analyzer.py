import pandas as pd

REQUIRED_COLUMNS = {"Date", "Product", "Quantity", "Price"}

def validate_columns(df):
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        print("HATA: Eksik kolonlar:", ", ".join(sorted(missing)))
        print("Beklenen kolonlar:", ", ".join(sorted(REQUIRED_COLUMNS)))
        return False
    return True

def clean_data(df):
    df = df.copy()
    df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
    df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
    df = df.dropna()
    return df

def add_total(df):
    df = df.copy()
    df["Total"] = df["Quantity"] * df["Price"]
    return df

def total_sales(df):
    return float(df["Total"].sum())

def best_product(df):
    grouped = df.groupby("Product")["Quantity"].sum()
    return str(grouped.idxmax())