from data_loader import load_data
from analyzer import validate_columns, clean_data, add_total
from analyzer import total_sales, best_product
from visualizer import plot_sales


def main():
    # Veriyi yükle
    df = load_data("data/sales.csv")
    if df is None:
        return

    # Kolonları doğrula
    if not validate_columns(df):
        return

    # Veriyi temizle (Hatalı satırları eler)
    df = clean_data(df)
    if df.empty:
        print("HATA: Temizlikten sonra veri kalmadi.")
        return

    # Toplam kazanç kolonunu ekle
    df = add_total(df)

    # İstatistikleri yazdır
    print("-" * 30)
    print("ANALİZ SONUÇLARI")
    print("-" * 30)
    print("Toplam Satış Geliri:", total_sales(df), "TL")
    print("En Çok Adet Satan Ürün:", best_product(df))
    print("-" * 30)

    # GÖRSELLEŞTİRME İYİLEŞTİRMESİ:
    # Aynı tarihteki satışları toplayarak grafiği netleştiriyoruz
    daily_sales = df.groupby("Date")["Total"].sum().reset_index()

    print("Grafik oluşturuluyor...")
    plot_sales(daily_sales)


if __name__ == "__main__":
    main()