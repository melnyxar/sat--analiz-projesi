import matplotlib.pyplot as plt

def plot_sales(df):
    plt.plot(df["Date"], df["Total"])
    plt.title("Satis Trendi")
    plt.xlabel("Tarih")
    plt.ylabel("Toplam Satis")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()