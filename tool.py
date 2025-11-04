# tool.py

import pandas as pd

def simple_screener(criteria: dict = None):
    """
    A simple stock screener tool that filters a mock dataset
    based on user-specified criteria.

    Args:
        criteria (dict): Filters such as {'PE': '<15', 'ROE': '>10', 'MarketCap': '>5000'}

    Returns:
        dict: Filtered results and summary
    """

    # 1. Create mock stock data (you can later replace this with real API data)
    data = [
        {"Ticker": "TCS", "PE": 28, "ROE": 35, "MarketCap": 1200000},
        {"Ticker": "INFY", "PE": 22, "ROE": 28, "MarketCap": 700000},
        {"Ticker": "HDFCBANK", "PE": 19, "ROE": 16, "MarketCap": 1000000},
        {"Ticker": "ITC", "PE": 12, "ROE": 28, "MarketCap": 500000},
        {"Ticker": "ONGC", "PE": 8, "ROE": 14, "MarketCap": 300000},
    ]

    df = pd.DataFrame(data)

    # 2. Apply filters if any criteria given
    if criteria:
        for key, condition in criteria.items():
            if key in df.columns:
                if ">" in condition:
                    val = float(condition.replace(">", ""))
                    df = df[df[key] > val]
                elif "<" in condition:
                    val = float(condition.replace("<", ""))
                    df = df[df[key] < val]
                elif "=" in condition:
                    val = float(condition.replace("=", ""))
                    df = df[df[key] == val]

    # 3. Convert result to dictionary for LLM output
    results = df.to_dict(orient="records")

    return {
        "criteria": criteria,
        "count": len(results),
        "results": results
    }
