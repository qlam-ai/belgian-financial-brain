import yfinance as yf
import pandas as pd


"""
Here are the data points that we try to extract from every stock
- last traded price - check
- currency - check
- since open +-? - check
- since previous close +-? check
- isin?
- which stock market is it traded on? - check
- volume? - check
- turnover - check
- market cap - check 
- historical performance (downloadable) check
- admitted shares - check
- all the company information you can have from the page - check

And for ETFs : 
- description
- fund overview
- fund operations
- asset classes
- top holdings
- equity holidings
- bond holdings
- bond ratings
- sector weightings

"""


def extract_data_stocks(stck_id):
    # Define the ticker symbol for UCB on Euronext Brussels
    ticker = yf.Ticker(stck_id)

    # 1. Last Traded Price
    last_traded_price = ticker.history(period="1d")["Close"].iloc[0]

    # 2. Currency
    currency = ticker.info.get("currency")

    # 3. Since Open Change (+/-)
    data = ticker.history(period="1d")
    open_price = data["Open"].iloc[0]
    close_price = data["Close"].iloc[0]
    change_since_open = close_price - open_price

    # 4. Since Previous Close (+/-)
    previous_close = ticker.info.get("previousClose")
    change_since_previous = close_price - previous_close

    # 5. Stock Market (Exchange)
    exchange = ticker.info.get("exchange")

    # 6. Volume
    volume = data["Volume"].iloc[0]

    # 7. Turnover (Volume * Last Traded Price)
    turnover = volume * last_traded_price

    # 8. Market Cap
    market_cap = ticker.info.get("marketCap")

    # 9. Historical Performance (Downloadable)
    historical_data = ticker.history(period="5d")
    json_data = historical_data.to_json(orient="records")

    # 10. Shares Outstanding (Admitted Shares)
    shares_outstanding = ticker.info.get("sharesOutstanding")

    # 11. Company Info (CEO, Net Income)
    comp_inf = ticker.info.get("companyOfficers")[0:3]

    # Extract key variables (add more variables as needed)
    variables = {
        "Yahoo ID of Stock": stck_id,
        "last traded price": last_traded_price,
        "currency": currency,
        "stock value change since market open": change_since_open,
        "stock value change since market last close": change_since_previous,
        "stock exchange on which stock is traded": exchange,
        "volume": volume,
        "turnover": turnover,
        "market Cap": market_cap,
        "number of shares outstanding": shares_outstanding,
        "company information in json format": comp_inf,
        "historical data over 5 days": json_data,
    }

    # Write each variable to a new line in a .txt file
    filename = "data/" + stck_id + ".txt"
    with open(filename, "w") as file:
        for key, value in variables.items():
            file.write(f"{key}: {value}\n")


def extract_data_etfs(etf_id):
    # Define the ticker symbol for UCB on Euronext Brussels
    ticker = yf.Ticker(etf_id)
    data = ticker.funds_data

    # show fund description
    description = data.description

    # show operational information
    fund_overview = data.fund_overview
    fund_ops = data.fund_operations

    # show holdings related information
    ass_class = data.asset_classes
    tp_holdings = data.top_holdings
    eq_hold = data.equity_holdings
    bond_hold = data.bond_holdings
    bond_rat = data.bond_ratings
    sec_wei = data.sector_weightings
    # Extract key variables (add more variables as needed)
    variables = {
        "Yahoo ID of ETF": etf_id,
        "description of the ETF": description,
        "ETF Fund Overview": fund_overview,
        "ETF Fund Operations": fund_ops,
        "ETF Asset Classes": ass_class,
        "ETF Top Holdings": tp_holdings,
        "ETF Equity Holdings": eq_hold,
        "ETF Bond Holdings": bond_hold,
        "ETF Bond Ratings": bond_rat,
        "ETF Sector weightings": sec_wei,
    }

    # Write each variable to a new line in a .txt file
    filename = "data/" + etf_id + ".txt"
    with open(filename, "w") as file:
        for key, value in variables.items():
            file.write(f"{key}: {value}\n")


def extract_bel20_stocks():
    bel20_list = [
        "ABI.BR",
        "AED.BR",
        "AGS.BR",
        "APAM.AS",
        "ARGX.BR",
        "COFB.BR",
        "ELI.BR",
        "GLPG.AS",
        "GBLB.BR",
        "KBC.BR",
        "MELE.BR",
        "PROX.BR",
        "SOF.BR",
        "SOLB.BR",
        "BNB.BR",
        "UCB.BR",
        "UMI.BR",
        "UPG.BR",
        "WDP.BR",
        "XIOR.BR",
    ]
    for stock_id in bel20_list:
        extract_data_stocks(stock_id)


def extract_bel20_etf():
    bel20_list = ["EWK"]
    for stock_id in bel20_list:
        extract_data_etfs(stock_id)


def main():
    extract_bel20_stocks()
    extract_bel20_etf()


# Ensures that main() is only called if this script is executed directly
if __name__ == "__main__":
    main()
