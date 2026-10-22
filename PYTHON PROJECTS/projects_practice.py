
import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns


# class RetailShopAnalyzer:

#     def __init__(self):
#         self.df = pd.read_csv("retail_shop.csv")

#     def display_data(self):
#         print("\n----- RETAIL SHOP DATA -----")
#         print(self.df.head())

#         print("\nDataset Information:")
#         print(self.df.info())

#         print("\nMissing Values:")
#         print(self.df.isnull().sum())

#     def analyze_data(self):
#         print("\n----- DATA ANALYSIS -----")
#         print("Total Rows:", self.df.shape[0])
#         print("Total Columns:", self.df.shape[1])

#         print("\nStatistical Summary:")
#         print(self.df.describe())

#         print("\nColumn Names:")
#         print(self.df.columns.tolist())

#         numeric = self.df.select_dtypes(include=np.number)

#         print("\nTotal of Numeric Columns:")
#         print(numeric.sum())

#         print("\nAverage of Numeric Columns:")
#         print(numeric.mean())

#     def show_bar_chart(self):
#         numeric = self.df.select_dtypes(include=np.number)
#         numeric.sum().plot(kind="bar")

#         plt.title("Retail Shop Data Analysis")
#         plt.xlabel("Columns")
#         plt.ylabel("Total")
#         plt.tight_layout()
#         plt.show()

#     def show_seaborn_chart(self):
#         numeric = self.df.select_dtypes(include=np.number)

#         if numeric.shape[1] >= 2:
#             sns.scatterplot(
#                 data=numeric,
#                 x=numeric.columns[0],
#                 y=numeric.columns[1]
#             )
#             plt.title("Retail Shop Data Relationship")
#             plt.tight_layout()
#             plt.show()
#         else:
#             print("At least two numeric columns are required.")

#     def show_correlation(self):
#         numeric = self.df.select_dtypes(include=np.number)

#         if numeric.shape[1] >= 2:
#             sns.heatmap(
#                 numeric.corr(),
#                 annot=True,
#                 cmap="coolwarm"
#             )
#             plt.title("Correlation Heatmap")
#             plt.tight_layout()
#             plt.show()
#         else:
#             print("At least two numeric columns are required.")


# shop = RetailShopAnalyzer()

# while True:
#     print("\n===== RETAIL SHOP ANALYSIS =====")
#     print("1. Display Data")
#     print("2. Analyze Data")
#     print("3. Matplotlib Bar Chart")
#     print("4. Seaborn Scatter Plot")
#     print("5. Correlation Heatmap")
#     print("6. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         shop.display_data()
#     elif choice == "2":
#         shop.analyze_data()
#     elif choice == "3":
#         shop.show_bar_chart()
#     elif choice == "4":
#         shop.show_seaborn_chart()
#     elif choice == "5":
#         shop.show_correlation()
#     elif choice == "6":
#         print("Program Ended!")
#         break
#     else:
#         print("Invalid Choice!")

arr1 = np.array([10, 20, 30])
arr2 = np.array([[20], [30], [50]])

print(arr1 + arr2)