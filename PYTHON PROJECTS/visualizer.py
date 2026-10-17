import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class SalesDataAnalyzer:
    """
    Manages and analyzes sales datasets using Pandas and NumPy.
    Cleans data, performs operations, and calculates statistics.
    Creates visualizations and saves charts using Matplotlib and Seaborn.
    """

    def __init__(self):
        """
        Initializes the analyzer with empty dataset variables.
        Sets the primary and secondary DataFrames to None.
        Initializes the figure variable for storing visualizations.
        """
        self.df = None
        self.other_df = None
        self.fig = None

    def load_dataset(self):
        """
        Accepts the CSV file path from the user.
        Loads the dataset and displays its first five rows.
        Handles file, parsing, permission, and other loading errors..
        """
        path = input("Enter CSV file path: ").strip()

        try:
            self.df = pd.read_csv(path)
            print("Dataset loaded successfully!")
            print(self.df.head())
        except (FileNotFoundError, pd.errors.ParserError,
                PermissionError) as e:
            print("Unable to load dataset:", e)
        except Exception as e:
            print("Error:", e)

    def explore_data(self):
        """
        Displays options for exploring the loaded dataset.
        Shows rows, columns, data types, information, and statistics.
        Provides dataset dimensions and a menu to return to the main menu.
        """
        if not self.check_data():
            return

        while True:
            print("""
1. First 5 rows
2. Last 5 rows
3. Column names
4. Data types
5. Dataset information
6. Descriptive statistics
7. Dataset shape
8. Return
""")
            ch = input("Enter choice: ")

            if ch == "1":
                print(self.df.head())
            elif ch == "2":
                print(self.df.tail())
            elif ch == "3":
                print(self.df.columns.tolist())
            elif ch == "4":
                print(self.df.dtypes)
            elif ch == "5":
                self.df.info()
            elif ch == "6":
                print(self.df.describe(include="all"))
            elif ch == "7":
                print("Rows, Columns:", self.df.shape)
            elif ch == "8":
                break
            else:
                print("Invalid choice")

    def clean_data(self):
        """
        Displays missing values and provides data-cleaning options.
        Removes missing or duplicate rows and fills numeric missing values.
        Converts selected columns to numeric types after validating column names.
        """
        if not self.check_data():
            return

        print("\nMissing values:")
        print(self.df.isnull().sum())

        print("""
1. Remove rows containing missing values
2. Fill numeric missing values with column means
3. Remove duplicate rows
4. Convert a column to numeric
5. Return
""")
        ch = input("Enter choice: ")

        if ch == "1":
            self.df = self.df.dropna()
            print("Rows with missing values removed.")

        elif ch == "2":
            cols = self.df.select_dtypes(include=np.number).columns
            self.df[cols] = self.df[cols].fillna(
                self.df[cols].mean()
            )
            print("Numeric missing values filled.")

        elif ch == "3":
            self.df = self.df.drop_duplicates()
            print("Duplicate rows removed.")

        elif ch == "4":
            col = input("Enter column name: ")
            if col in self.df.columns:
                self.df[col] = pd.to_numeric(
                    self.df[col], errors="coerce"
                )
                print("Column converted to numeric.")
            else:
                print("Column not found.")

        elif ch == "5":
            return
        else:
            print("Invalid choice")

    def dataframe_operations(self):
        """
        Performs arithmetic operations on numeric DataFrame columns.
        Supports concatenating, merging, splitting, and re-indexing datasets.
        Validates inputs and optionally saves split datasets as CSV files.
        """
        if not self.check_data():
            return

        print("""
1. Mathematical operation on a column
2. Concatenate another CSV
3. Merge another CSV
4. Split data by column value
5. Re-index rows
6. Return
""")
        ch = input("Enter choice: ")

        if ch == "1":
            col = input("Enter numeric column: ")

            if col not in self.df.columns:
                print("Column not found.")
                return

            if not pd.api.types.is_numeric_dtype(self.df[col]):
                print("Choose a numeric column.")
                return

            print("1. Add  2. Subtract  3. Multiply  4. Divide")
            op = input("Enter operation: ")

            try:
                value = float(input("Enter number: "))

                if op == "1":
                    self.df[col] = self.df[col] + value
                elif op == "2":
                    self.df[col] = self.df[col] - value
                elif op == "3":
                    self.df[col] = self.df[col] * value
                elif op == "4":
                    if value == 0:
                        print("Cannot divide by zero.")
                        return
                    self.df[col] = self.df[col] / value
                else:
                    print("Invalid operation.")
                    return

                print(self.df.head())

            except ValueError:
                print("Enter a valid number.")

        elif ch == "2":
            path = input("Enter second CSV path: ")

            try:
                other = pd.read_csv(path)
                self.df = pd.concat(
                    [self.df, other], ignore_index=True
                )
                print("DataFrames concatenated.")
                print(self.df.head())
            except Exception as e:
                print("Error:", e)

        elif ch == "3":
            path = input("Enter second CSV path: ")

            try:
                other = pd.read_csv(path)

                print("Common columns:", list(
                    set(self.df.columns) & set(other.columns)
                ))

                key = input("Enter common column for merge: ")

                if (key not in self.df.columns or
                        key not in other.columns):
                    print("Merge column not found in both files.")
                    return

                self.df = pd.merge(
                    self.df, other, on=key, how="inner"
                )
                print("DataFrames merged.")
                print(self.df.head())

            except Exception as e:
                print("Error:", e)

        elif ch == "4":
            col = input("Enter column to split by: ")

            if col not in self.df.columns:
                print("Column not found.")
                return

            value = input("Enter value to keep in first part: ")
            mask = self.df[col].astype(str) == value

            first = self.df[mask]
            second = self.df[~mask]

            print("First part:")
            print(first)

            print("Remaining part:")
            print(second)

            if input("Save both parts? (yes/no): ").lower() == "yes":
                first.to_csv("sales_part1.csv", index=False)
                second.to_csv("sales_part2.csv", index=False)
                print("Saved as sales_part1.csv and sales_part2.csv")

        elif ch == "5":
            self.df = self.df.reset_index(drop=True)
            print("DataFrame re-indexed.")
            print(self.df.head())

        elif ch == "6":
            return
        else:
            print("Invalid choice")

    def search_sort_filter(self):
        """
        Searches dataset records using values entered by the user.
        Sorts records and filters data by numeric values or categories.
        Validates columns and inputs before displaying matching records.
        """
        if not self.check_data():
            return

        print("""
1. Search for a value
2. Sort ascending
3. Sort descending
4. Filter numeric values
5. Filter by category
6. Return
""")
        ch = input("Enter choice: ")

        if ch == "1":
            col = input("Enter column: ")

            if col not in self.df.columns:
                print("Column not found.")
                return

            value = input("Enter search value: ")

            result = self.df[
                self.df[col].astype(str).str.contains(
                    value, case=False, na=False
                )
            ]

            print(result if not result.empty else "No matches found.")

        elif ch in ("2", "3"):
            col = input("Enter column to sort: ")

            if col not in self.df.columns:
                print("Column not found.")
                return

            result = self.df.sort_values(
                by=col, ascending=(ch == "2")
            )
            print(result)

        elif ch == "4":
            col = input("Enter numeric column: ")

            if col not in self.df.columns:
                print("Column not found.")
                return

            if not pd.api.types.is_numeric_dtype(self.df[col]):
                print("Choose a numeric column.")
                return

            try:
                value = float(input("Show values greater than: "))
                print(self.df[self.df[col] > value])
            except ValueError:
                print("Enter a valid number.")

        elif ch == "5":
            col = input("Enter category column: ")

            if col not in self.df.columns:
                print("Column not found.")
                return

            value = input("Enter category value: ")
            print(self.df[self.df[col].astype(str) == value])

        elif ch == "6":
            return
        else:
            print("Invalid choice")

    def aggregates_statistics(self):
        """
        Calculates descriptive statistics for numeric dataset columns.
        Supports grouped aggregation, transformations, pivot tables, and correlations.
        Displays statistical results after validating the selected columns.
        """
        if not self.check_data():
            return

        nums = self.df.select_dtypes(include=np.number)

        if nums.empty:
            print("No numeric columns available.")
            return

        print("\nSum:\n", nums.sum())
        print("\nMean:\n", nums.mean())
        print("\nCount:\n", nums.count())
        print("\nMinimum:\n", nums.min())
        print("\nMaximum:\n", nums.max())
        print("\nStandard deviation:\n", nums.std())
        print("\nVariance:\n", nums.var())
        print(
            "\n25th, 50th and 75th percentiles:\n",
            nums.quantile([0.25, 0.50, 0.75])
        )

        print("""
1. Group by a column
2. Transform within groups
3. Create pivot table
4. Correlation matrix
5. Return
""")
        ch = input("Enter choice: ")

        if ch == "1":
            group = input("Enter grouping column: ")

            if group not in self.df.columns:
                print("Column not found.")
                return

            col = input("Enter numeric column: ")

            if col not in nums.columns:
                print("Numeric column not found.")
                return

            print(self.df.groupby(group)[col].agg(
                ["sum", "mean", "count", "min", "max"]
            ))

        elif ch == "2":
            group = input("Enter grouping column: ")
            col = input("Enter numeric column: ")

            if group not in self.df.columns or col not in nums.columns:
                print("Invalid column.")
                return

            result = self.df.copy()
            result["GroupMean"] = result.groupby(group)[col].transform("mean")
            print(result)

        elif ch == "3":
            index = input("Enter pivot row column: ")
            columns = input("Enter pivot column: ")
            values = input("Enter numeric values column: ")

            if (index not in self.df.columns or
                    columns not in self.df.columns or
                    values not in nums.columns):
                print("Invalid column.")
                return

            print(pd.pivot_table(
                self.df,
                index=index,
                columns=columns,
                values=values,
                aggfunc="sum",
                fill_value=0
            ))

        elif ch == "4":
            print(nums.corr())

        elif ch == "5":
            return
        else:
            print("Invalid choice")

    def visualize_data(self):
        """
        Creates charts using Matplotlib and Seaborn from the loaded dataset.
        Supports bar, line, scatter, pie, histogram, stack, heatmap, and box plots.
        Validates selected columns and displays the generated visualization.
        """
        if not self.check_data():
            return

        print("""
1. Bar plot
2. Line plot
3. Scatter plot
4. Pie chart
5. Histogram
6. Stack plot
7. Seaborn heatmap
8. Seaborn box plot
9. Multiple subplots
""")
        ch = input("Enter choice: ")

        try:
            numeric = self.df.select_dtypes(
                include=np.number
            ).columns.tolist()

            if ch == "1":
                col = input("Enter category column: ")
                val = input("Enter numeric column: ")

                if col not in self.df.columns or val not in numeric:
                    print("Invalid columns.")
                    return

                data = self.df.groupby(col)[val].sum()
                self.fig, ax = plt.subplots()
                data.plot(kind="bar", ax=ax, color="steelblue")
                ax.set_xlabel(col)
                ax.set_ylabel(val)

            elif ch == "2":
                col = input("Enter numeric column: ")

                if col not in numeric:
                    print("Invalid numeric column.")
                    return

                self.fig, ax = plt.subplots()
                ax.plot(self.df[col], marker="o", label=col)
                ax.set_ylabel(col)
                ax.legend()

            elif ch == "3":
                x = input("Enter X numeric column: ")
                y = input("Enter Y numeric column: ")

                if x not in numeric or y not in numeric:
                    print("Invalid numeric columns.")
                    return

                self.fig, ax = plt.subplots()
                ax.scatter(self.df[x], self.df[y], color="orange")
                ax.set_xlabel(x)
                ax.set_ylabel(y)

            elif ch == "4":
                col = input("Enter category column: ")

                if col not in self.df.columns:
                    print("Column not found.")
                    return

                data = self.df[col].value_counts().head(10)
                self.fig, ax = plt.subplots()
                ax.pie(data, labels=data.index, autopct="%1.1f%%")

            elif ch == "5":
                col = input("Enter numeric column: ")

                if col not in numeric:
                    print("Invalid numeric column.")
                    return

                self.fig, ax = plt.subplots()
                ax.hist(self.df[col].dropna(), bins=10, edgecolor="black")
                ax.set_xlabel(col)

            elif ch == "6":
                cols = input(
                    "Enter numeric columns separated by commas: "
                )
                cols = [c.strip() for c in cols.split(",")]

                if not cols or any(c not in numeric for c in cols):
                    print("Invalid numeric columns.")
                    return

                self.fig, ax = plt.subplots()
                ax.stackplot(
                    self.df.index,
                    *[self.df[c].fillna(0) for c in cols],
                    labels=cols
                )
                ax.legend(loc="upper left")

            elif ch == "7":
                if len(numeric) < 2:
                    print("At least two numeric columns are required.")
                    return

                self.fig, ax = plt.subplots()
                sns.heatmap(
                    self.df[numeric].corr(),
                    annot=True,
                    cmap="coolwarm",
                    ax=ax
                )

            elif ch == "8":
                col = input("Enter numeric column: ")

                if col not in numeric:
                    print("Invalid numeric column.")
                    return

                self.fig, ax = plt.subplots()
                sns.boxplot(data=self.df, x=col, ax=ax)

            elif ch == "9":
                if len(numeric) < 2:
                    print("At least two numeric columns are required.")
                    return

                cols = numeric[:4]
                self.fig, axes = plt.subplots(
                    2, 2, figsize=(10, 8)
                )

                for i, ax in enumerate(axes.flat):
                    if i < len(cols):
                        ax.hist(self.df[cols[i]].dropna(), bins=10)
                        ax.set_title(cols[i])
                    else:
                        ax.set_visible(False)

            else:
                print("Invalid choice")
                return

            plt.suptitle("Sales Data Analysis")
            plt.tight_layout()
            plt.show()

        except Exception as e:
            print("Unable to create plot:", e)

    def save_visualization(self):
        """ 
        Checks whether a visualization is available for saving.
        Allows the user to choose a filename and PNG or JPEG format.
        Saves the figure and handles invalid formats or file errors.
        """
        if self.fig is None:
            print("Create a visualization first.")
            return

        name = input("Enter file name (without extension): ").strip()

        if not name:
            print("File name cannot be empty.")
            return

        print("1. PNG")
        print("2. JPEG")
        ch = input("Choose format: ")

        if ch == "1":
            filename = name + ".png"
            fmt = "png"
        elif ch == "2":
            filename = name + ".jpg"
            fmt = "jpeg"
        else:
            print("Invalid format.")
            return

        try:
            self.fig.savefig(
                filename, format=fmt, bbox_inches="tight"
            )
            print("Visualization saved as", filename)
        except Exception as e:
            print("Unable to save image:", e)

    def check_data(self):
        """
        Checks whether a dataset has been loaded into the analyzer.
        Displays a warning message when no dataset is available.
        Returns True if data exists and False otherwise.
        """
        if self.df is None:
            print("Please load a dataset first.")
            return False
        return True

    @classmethod
    def project_name(cls):
        """
        Defines a class method for displaying project information.
        Uses the class reference without requiring an instance-specific variable.
        Prints the project name, Sales Data Analyzer.
        """
        print("Sales Data Analyzer")

    @staticmethod
    def show_libraries():
        """
        Defines a class method for displaying project information.
        Uses the class reference without requiring an instance-specific variable.
        Prints the project name, Sales Data Analyzer.
        """
        print("Pandas, NumPy, Matplotlib and Seaborn")

    def show_documentation(self):
        """Displays class and method documentation without using inspect."""
        print("\n" + "=" * 60)
        print("       SALES DATA ANALYZER - DOCUMENTATION")
        print("=" * 60)

        print("\nCLASS DOCUMENTATION:")
        print(self.__class__.__doc__)

        methods = [
            self.__init__,
            self.load_dataset,
            self.explore_data,
            self.clean_data,
            self.dataframe_operations,
            self.search_sort_filter,
            self.aggregates_statistics,
            self.visualize_data,
            self.save_visualization,
            self.check_data,
            self.project_name,
            self.show_libraries,
            self.show_documentation,
            self.run
        ]

        for method in methods:
            print("\n" + "-" * 60)
            print("FUNCTION:", method.__name__ + "()")
            print("-" * 60)
            print(method.__doc__ or "Documentation unavailable.")

        print("\n" + "=" * 60)
        print("       END OF DOCUMENTATION")
        print("=" * 60)

    def run(self):
        """Displays the main menu and runs the selected operation."""
        while True:
            print("""
========================================
         SALES DATA ANALYZER
========================================
1. Load Dataset
2. Explore Data
3. Clean Missing Data
4. DataFrame Operations
5. Search, Sort and Filter
6. Aggregates and Statistics
7. Data Visualization
8. Save Visualization
9. Project Information
10. Exit
""")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.load_dataset()
            elif choice == "2":
                self.explore_data()
            elif choice == "3":
                self.clean_data()
            elif choice == "4":
                self.dataframe_operations()
            elif choice == "5":
                self.search_sort_filter()
            elif choice == "6":
                self.aggregates_statistics()
            elif choice == "7":
                self.visualize_data()
            elif choice == "8":
                self.save_visualization()
            elif choice == "9":
                self.project_name()
                self.show_libraries()
            elif choice == "10":
                self.show_documentation()
                print("\nThank you for using Sales Data Analyzer!")
                break
            else:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    analyzer = SalesDataAnalyzer()
    analyzer.run()