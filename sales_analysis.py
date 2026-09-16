"""Starter sales performance analytics project."""
import pandas as pd

def sales_kpis(df: pd.DataFrame) -> dict:
    data = df.copy()
    data["sales"] = pd.to_numeric(data["sales"], errors="coerce").fillna(0)
    data["quantity"] = pd.to_numeric(data["quantity"], errors="coerce").fillna(0)
    return {
        "revenue": round(data["sales"].sum(), 2),
        "units_sold": int(data["quantity"].sum()),
        "average_order_value": round(data["sales"].mean(), 2),
        "top_product": data.groupby("product")["sales"].sum().idxmax(),
    }

def monthly_sales(df: pd.DataFrame) -> pd.DataFrame:
    data = df.copy()
    data["date"] = pd.to_datetime(data["date"])
    return data.groupby(data["date"].dt.to_period("M"))["sales"].sum().reset_index()

if __name__ == "__main__":
    sample = pd.DataFrame({"date": ["2026-01-01", "2026-01-02"], "product": ["A", "B"], "sales": [500, 700], "quantity": [5, 6]})
    print(sales_kpis(sample))
