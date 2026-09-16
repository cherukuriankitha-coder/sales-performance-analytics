"""Sales cleaning and KPI utilities."""
import pandas as pd


def prepare_sales(df: pd.DataFrame) -> pd.DataFrame:
    required = {"order_date", "product", "quantity", "unit_price"}
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")
    out = df.copy()
    out["order_date"] = pd.to_datetime(out["order_date"], errors="raise")
    out["quantity"] = pd.to_numeric(out["quantity"], errors="raise")
    out["unit_price"] = pd.to_numeric(out["unit_price"], errors="raise")
    out["sales"] = out["quantity"] * out["unit_price"]
    return out


def product_performance(df: pd.DataFrame) -> pd.DataFrame:
    clean = prepare_sales(df)
    return (clean.groupby("product", as_index=False)
            .agg(units_sold=("quantity", "sum"), revenue=("sales", "sum"))
            .sort_values("revenue", ascending=False))


def monthly_sales(df: pd.DataFrame) -> pd.DataFrame:
    clean = prepare_sales(df)
    return clean.set_index("order_date").resample("MS")["sales"].sum().rename("revenue").reset_index()
