# E-Library Data Insights Dashboard

## 1. Project Overview
The **E-Library Data Insights Dashboard** is a Python-based data analysis and management system designed to process and analyze book borrowing transactions. It provides actionable insights into book popularity, borrowing trends over time, user borrowing behavior, and genre distributions.

This project strictly adheres to all specified guidelines and integrates:
- **Control Structures & Loops**: Validating input records and eliminating corrupt, missing, or duplicate entries.
- **Object-Oriented Programming (OOP)**: Encapsulating all operations inside the reusable `LibraryDashboard` class.
- **NumPy**: Calculating duration statistics (mean, median, standard deviation) using NumPy arrays.
- **Pandas**: Data cleaning, filtering, grouping, aggregation, and generating new computed columns (`Late Return`, `Frequent Borrower`).
- **Matplotlib & Seaborn**: Creating 4 insightful charts (Bar Chart, Line Graph, Pie Chart, Heatmap) with complete labels, titles, and legends.

---

## 2. Submission Files
- `library_dashboard.py` — Complete Python application and `LibraryDashboard` class.
- `library_transactions.csv` — Transaction dataset used for testing.
- `README.md` — Project documentation and setup instructions.

---

## 3. Dataset Format
The dataset `library_transactions.csv` contains the following schema:

| Column | Type | Description |
|---|---|---|
| `Transaction ID` | String | Unique transaction identifier |
| `Date` | Date (`YYYY-MM-DD`) | Date the book was borrowed |
| `User ID` | String | Unique library member identifier |
| `Book Title` | String | Title of the borrowed book |
| `Genre` | String | Category / genre of the book |
| `Borrowing Duration (Days)` | Integer | Number of days the book was borrowed |

---

## 4. Requirements & Dependencies
The application strictly uses **only** the 4 approved libraries:
- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`

To install the dependencies:
```bash
pip install numpy pandas matplotlib seaborn
```

---

## 5. Main Class & Method Architecture

### `LibraryDashboard(file_path="library_transactions.csv")`
- **`load_data(self, file_path=None)`**:
  - Loads the CSV into a Pandas DataFrame.
  - Validates required columns using control structures.
  - Uses loops (`for idx, row in self.data.iterrows():`) and conditional statements (`if/else`) to check for missing values, format consistency, positive borrowing durations, and duplicate transaction IDs.
  - Generates two new computed columns:
    * `Late Return`: Flags borrowings exceeding 7 days (`"Yes"` / `"No"`).
    * `Frequent Borrower`: Flags members with 2 or more borrowings (`"Yes"` / `"No"`).
- **`calculate_statistics(self)`**:
  - Uses **NumPy arrays** to compute average borrowing duration, median, and standard deviation.
  - Identifies the most borrowed book and the busiest weekday.
  - Uses **Pandas** to aggregate borrowings per book, compute genre averages, monthly counts, and frequent borrower activity.
- **`display_statistics(self)`**:
  - Formats and displays all calculated summary metrics in the terminal.
- **`filter_transactions(self, condition=None, genre=None, start_date=None, end_date=None, min_duration=None, max_duration=None)`**:
  - Filters transactions using custom query functions, string conditions, or criteria such as genre, date ranges, and duration thresholds.
- **`generate_report(self, output_file="library_report.txt")`**:
  - Exports a formatted summary report to a text file.
- **`visualize(self)`**:
  - Generates and saves 4 comprehensive visualizations with full titles, axes labels, and legends:
    1. **Bar Chart**: Top 5 Most Borrowed Books (`top_5_books.png`).
    2. **Line Graph**: Borrowing Trends Over Months (`monthly_borrowing_trend.png`).
    3. **Pie Chart**: Distribution of Books Borrowed by Genre (`genre_distribution.png`).
    4. **Heatmap**: Borrowing Activity by Day and Time (Day of Week vs Month) (`borrowing_activity_heatmap.png`).

---

## 6. How to Run

1. Open your terminal or PowerShell and navigate to the project folder:
   ```powershell
   cd "c:\PYTHON TASKS\PYTHON PROJECTS\Prcatical Projects"
   ```

2. Execute the script:
   ```powershell
   python library_dashboard.py
   ```

3. When prompted:
   ```text
   Enter CSV path [Press Enter for 'library_transactions.csv']:
   ```
   Press **Enter** to use the default dataset, or provide a custom file path.

4. Select an option from the interactive menu:
   - `1`: View Summary Statistics
   - `2`: Filter Transactions by Genre
   - `3`: Filter Transactions by Duration
   - `4`: View Late Returns
   - `5`: Generate All Charts (Visualizations)
   - `6`: Save Report to File
   - `7`: Exit

---

## 7. Generated Output Files
Running the program produces the following files:
- `library_report.txt` — Summary statistics report.
- `top_5_books.png` — Bar chart visualization.
- `monthly_borrowing_trend.png` — Line graph visualization.
- `genre_distribution.png` — Pie chart visualization.
- `borrowing_activity_heatmap.png` — Heatmap visualization.
