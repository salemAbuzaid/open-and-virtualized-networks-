import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("sales_data.csv")
    monthList = df['month_number'].tolist()
    bathingsoapSalesData = df['bathingsoap'].tolist()
    plt.bar(monthList, bathingsoapSalesData)
    plt.xlabel('MonthNumber')
    plt.ylabel('Salesunits in number')
    plt.xticks(monthList)
    plt.grid(True, linewidth=1, linestyle="--")
    plt.title('Bathingsoapsalesdata')
    plt.savefig('C:\Users\salem\Desktop\ sales_data_of_bathingsoap.png', dpi = 150)
    plt.show()


if __name__ == "__main__":
    main()
