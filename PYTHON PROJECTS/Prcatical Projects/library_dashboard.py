"""
E-Library Data Insights Dashboard
Integrates Control Structures, OOP, NumPy, Pandas, Matplotlib, and Seaborn.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class LibraryDashboard:
    """Manages, cleans, analyzes, and visualizes library borrowing transactions."""

    def __init__(self, file_path="library_transactions.csv"):
        self.file_path = file_path
        self.cleaned_data = pd.DataFrame()

    def load_data(self, file_path=None):
        """Loads and cleans dataset using loops and conditions, then adds computed columns."""
        if file_path:
            self.file_path = file_path

        try:
            raw_data = pd.read_csv(self.file_path)
            print(f"Successfully loaded '{self.file_path}'.")
        except Exception:
            try:
                alt_path = "PYTHON PROJECTS/Prcatical Projects/" + self.file_path
                raw_data = pd.read_csv(alt_path)
                self.file_path = alt_path
                print(f"Successfully loaded '{self.file_path}'.")
            except Exception as e:
                print(f"Error loading CSV file: {e}")
                return False
                
        required_cols = [
            "Transaction ID", "Date", "User ID",
            "Book Title", "Genre", "Borrowing Duration (Days)"
        ]
        for col in required_cols:
            if col not in raw_data.columns:
                print(f"Validation Error: Missing column '{col}'.")
                return False

        valid_rows = []
        seen_ids = set()

        for _, row in raw_data.iterrows():

            if row[required_cols].isnull().any() or any(str(row[c]).strip() == "" for c in required_cols):
                continue

            trans_id = str(row["Transaction ID"]).strip()
            if trans_id in seen_ids:
                continue

            try:
                date = pd.to_datetime(row["Date"])
                duration = int(float(row["Borrowing Duration (Days)"]))
                if duration <= 0:
                    continue
            except (ValueError, TypeError):
                continue

            seen_ids.add(trans_id)
            valid_rows.append({
                "Transaction ID": trans_id,
                "Date": date,
                "User ID": str(row["User ID"]).strip(),
                "Book Title": str(row["Book Title"]).strip(),
                "Genre": str(row["Genre"]).strip(),
                "Borrowing Duration (Days)": duration
            })

        self.cleaned_data = pd.DataFrame(valid_rows)
        if self.cleaned_data.empty:
            print("No valid records found.")
            return False

        self.cleaned_data = self.cleaned_data.sort_values("Date").reset_index(drop=True)

        self.cleaned_data["Late Return"] = np.where(
            self.cleaned_data["Borrowing Duration (Days)"] > 7, "Yes", "No"
        )
        user_counts = self.cleaned_data["User ID"].value_counts()
        self.cleaned_data["Frequent Borrower"] = self.cleaned_data["User ID"].map(
            lambda uid: "Yes" if user_counts.get(uid, 0) >= 2 else "No"
        )

        print(f"Data cleaned successfully: {len(self.cleaned_data)} valid records retained.")
        return True

    def _has_data(self):
        """Helper to ensure data is loaded."""
        if self.cleaned_data.empty:
            print("Please load a valid dataset first.")
            return False
        return True

    def calculate_statistics(self):
        """Calculates key metrics using NumPy arrays and Pandas aggregations."""
        if not self._has_data():
            return None

        df = self.cleaned_data
        durations = np.array(df["Borrowing Duration (Days)"])

        return {
            "Total Transactions": len(df),
            "Unique Books": df["Book Title"].nunique(),
            "Unique Users": df["User ID"].nunique(),
            "Most Borrowed Book": df["Book Title"].value_counts().idxmax(),
            "Average Borrowing Duration": float(np.mean(durations)),
            "Median Borrowing Duration": float(np.median(durations)),
            "Standard Deviation of Duration": float(np.std(durations)),
            "Busiest Day": df["Date"].dt.day_name().value_counts().idxmax(),
            "Top 5 Most Borrowed Books": df["Book Title"].value_counts().head(5),
            "Total Borrowings per Book": df.groupby("Book Title").size().sort_values(ascending=False),
            "Genre Distribution": df["Genre"].value_counts(),
            "Average Duration by Genre": df.groupby("Genre")["Borrowing Duration (Days)"].mean().round(2),
            "Monthly Borrowings": df.groupby(df["Date"].dt.to_period("M")).size(),
            "Frequent Borrowers": df[df["Frequent Borrower"] == "Yes"]["User ID"].value_counts(),
            "Late Returns Count": int((df["Late Return"] == "Yes").sum())
        }

    def display_statistics(self):
        """Displays calculated metrics clearly in the console."""
        stats = self.calculate_statistics()
        if not stats:
            return

        print("\n" + "=" * 45)
        print("          E-LIBRARY SUMMARY STATISTICS")
        print("=" * 45)
        for key, value in stats.items():
            print(f"\n{key}:")
            if isinstance(value, pd.Series):
                print(value.to_string())
            elif isinstance(value, float):
                print(round(value, 2))
            else:
                print(value)

    def filter_transactions(self, genre=None, min_duration=None, max_duration=None, condition=None):
        """Filters transactions by genre, duration range, or a custom lambda/query."""
        if not self._has_data():
            return pd.DataFrame()

        df = self.cleaned_data
        if genre:
            df = df[df["Genre"].str.lower() == genre.strip().lower()]
        if min_duration is not None:
            df = df[df["Borrowing Duration (Days)"] >= min_duration]
        if max_duration is not None:
            df = df[df["Borrowing Duration (Days)"] <= max_duration]
        if condition is not None:
            df = df[condition(df)] if callable(condition) else df.query(condition)

        return df.reset_index(drop=True)

    def generate_report(self, output_file="library_report.txt"):
        """Generates and saves a text summary report of the library analysis."""
        stats = self.calculate_statistics()
        if not stats:
            return

        with open(output_file, "w", encoding="utf-8") as file:
            file.write("=" * 50 + "\n        E-LIBRARY DATA INSIGHTS REPORT\n" + "=" * 50 + "\n\n")
            for key, value in stats.items():
                file.write(f"{key}:\n")
                if isinstance(value, pd.Series):
                    file.write(value.to_string() + "\n\n")
                elif isinstance(value, float):
                    file.write(f"{round(value, 2)}\n\n")
                else:
                    file.write(f"{value}\n\n")

        print(f"Report successfully saved to '{output_file}'.")

    def visualize(self):
        """Generates and saves 4 visualizations: Bar, Line, Pie, and Heatmap."""
        if not self._has_data():
            return

        df = self.cleaned_data

        top_books = df["Book Title"].value_counts().head(5)
        plt.figure(figsize=(9, 4.5))
        sns.barplot(x=top_books.values, y=top_books.index, hue=top_books.index, palette="viridis", legend=False)
        plt.title("Top 5 Most Borrowed Books", fontsize=13, fontweight="bold")
        plt.xlabel("Borrowings Count")
        plt.tight_layout()
        plt.savefig("top_5_books.png")
        plt.show()

        monthly = df.groupby(df["Date"].dt.to_period("M")).size()
        plt.figure(figsize=(9, 4.5))
        plt.plot(monthly.index.astype(str), monthly.values, marker="o", color="royalblue", linewidth=2, label="Monthly Trend")
        plt.title("Borrowing Trends Over Months", fontsize=13, fontweight="bold")
        plt.xlabel("Month")
        plt.ylabel("Borrowings Count")
        plt.grid(True, linestyle="--", alpha=0.5)
        plt.legend()
        plt.tight_layout()
        plt.savefig("monthly_borrowing_trend.png")
        plt.show()

        genre_counts = df["Genre"].value_counts()
        plt.figure(figsize=(6, 6))
        plt.pie(genre_counts.values, labels=genre_counts.index, autopct="%1.1f%%", startangle=140)
        plt.title("Distribution of Books by Genre", fontsize=13, fontweight="bold")
        plt.legend(title="Genres", loc="upper right")
        plt.tight_layout()
        plt.savefig("genre_distribution.png")
        plt.show()

        heat_df = df.copy()
        heat_df["Day"] = pd.Categorical(
            heat_df["Date"].dt.day_name(),
            categories=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            ordered=True
        )
        months_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        active_months = [m for m in months_order if m in heat_df["Date"].dt.strftime("%b").values]
        heat_df["Month"] = pd.Categorical(heat_df["Date"].dt.strftime("%b"), categories=active_months, ordered=True)
        pivot = heat_df.pivot_table(index="Day", columns="Month", values="Transaction ID", aggfunc="count", fill_value=0, observed=False)

        plt.figure(figsize=(9, 5))
        sns.heatmap(pivot, annot=True, fmt="d", cmap="YlGnBu", cbar_kws={"label": "Borrowings Count"})
        plt.title("Borrowing Activity (Day of Week vs Month)", fontsize=13, fontweight="bold")
        plt.tight_layout()
        plt.savefig("borrowing_activity_heatmap.png")
        plt.show()


if __name__ == "__main__":
    print("=" * 50)
    print("      E-LIBRARY DATA INSIGHTS DASHBOARD")
    print("=" * 50)

    try:
        user_path = input("Enter CSV path [Press Enter for 'library_transactions.csv']: ").strip()
    except (EOFError, KeyboardInterrupt):
        user_path = ""
    file_name = user_path if user_path else "library_transactions.csv"

    dashboard = LibraryDashboard(file_name)
    if not dashboard.load_data():
        exit()

    while True:
        print("\n" + "=" * 45)
        print("          DASHBOARD MAIN MENU")
        print("=" * 45)
        print("1. View Summary Statistics")
        print("2. Filter Transactions by Genre")
        print("3. Filter Transactions by Duration")
        print("4. View Late Returns")
        print("5. Generate All Visualizations (Charts)")
        print("6. Save Report to File")
        print("7. Exit")
        print("=" * 45)

        try:
            choice = input("Enter your choice (1-7): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting dashboard. Goodbye!")
            break

        if choice == "1":
            dashboard.display_statistics()

        elif choice == "2":
            genre = input("Enter genre (e.g., Fiction, Technology): ").strip()
            result = dashboard.filter_transactions(genre=genre)
            print(f"\n--- Transactions for Genre: '{genre}' ---")
            print(result.to_string(index=False) if not result.empty else "No transactions found.")

        elif choice == "3":
            try:
                min_d = int(input("Enter minimum duration in days: ").strip())
                result = dashboard.filter_transactions(min_duration=min_d)
                print(f"\n--- Transactions with Duration >= {min_d} Days ---")
                print(result.to_string(index=False) if not result.empty else "No transactions found.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == "4":
            result = dashboard.filter_transactions(condition=lambda d: d["Late Return"] == "Yes")
            print("\n--- Late Return Transactions ---")
            print(result.to_string(index=False) if not result.empty else "No late returns found.")

        elif choice == "5":
            print("\nGenerating charts (close each popup window to see the next)...")
            dashboard.visualize()
            print("All 4 charts displayed and saved as PNG images!")

        elif choice == "6":
            dashboard.generate_report()

        elif choice == "7":
            print("\nExiting dashboard. Goodbye!")
            break

        else:
            print("Invalid choice! Please select an option from 1 to 7.")

