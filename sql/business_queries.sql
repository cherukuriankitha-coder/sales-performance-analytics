-- Revenue by product
SELECT product,
       SUM(quantity) AS units_sold,
       ROUND(SUM(quantity * unit_price), 2) AS revenue
FROM sales
GROUP BY product
ORDER BY revenue DESC;

-- Monthly revenue trend
SELECT DATE_TRUNC('month', order_date) AS month,
       ROUND(SUM(quantity * unit_price), 2) AS revenue
FROM sales
GROUP BY 1
ORDER BY 1;

-- Average order value
SELECT ROUND(SUM(quantity * unit_price) / NULLIF(COUNT(DISTINCT order_id), 0), 2) AS avg_order_value
FROM sales;
