import pandas as pd

def load_data(path):
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        print("HATA: Dosya bulunamadi:", path)
        return None
    except Exception as e:
        print("HATA: Dosya okunamadi. Sebep:", e)
        return None
