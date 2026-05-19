import argparse
import requests
import time


def get_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"

    my_params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 50,
        "page": 1,
        "sparkline": "false"
    }

    response = requests.get(url, params=my_params)

    if response.status_code != 200:
        print("Sxal, tvyalner chstacvec")
        print("Status code:", response.status_code)
        return []

    data = response.json()
    return data


def filter_data(data, args):
    filtered_data = data

    if args.search:
        filtered_data = [
            coin for coin in filtered_data
            if args.search.lower() in coin["name"].lower()
        ]

    if args.price_gt:
        filtered_data = [
            coin for coin in filtered_data
            if coin["current_price"] > args.price_gt
        ]

    if args.market_cap_gt:
        filtered_data = [
            coin for coin in filtered_data
            if coin["market_cap"] > args.market_cap_gt
        ]

    if args.volume_gt:
        filtered_data = [
            coin for coin in filtered_data
            if coin["total_volume"] > args.volume_gt
        ]

    if args.change_gt:
        filtered_data = [
            coin for coin in filtered_data
            if coin["price_change_percentage_24h"] is not None
            and coin["price_change_percentage_24h"] > args.change_gt
        ]

    return filtered_data


def print_table(data):
    print(f"{'Name':<15} {'Symbol':<8} {'Price':<15} {'Market Cap':<18} {'Volume':<18} {'24h %':<10}")
    print("-" * 90)

    for coin in data:
        name = coin["name"]
        symbol = coin["symbol"].upper()
        price = coin["current_price"]
        market_cap = coin["market_cap"]
        volume = coin["total_volume"]
        change = coin["price_change_percentage_24h"]

        print(f"{name:<15} {symbol:<8} {price:<15} {market_cap:<18} {volume:<18} {change:<10}")


def main():
    parser = argparse.ArgumentParser(description="Crypto statistics program")

    parser.add_argument("--search", help="Search crypto by name")
    parser.add_argument("--price-gt", type=float, help="Show coins with price greater than X")
    parser.add_argument("--market-cap-gt", type=float, help="Show coins with market cap greater than X")
    parser.add_argument("--volume-gt", type=float, help="Show coins with volume greater than X")
    parser.add_argument("--change-gt", type=float, help="Show coins with 24h change greater than X")
    parser.add_argument("--refresh", type=int, help="Refresh data every X seconds")

    args = parser.parse_args()

    if args.refresh:
        while True:
            data = get_crypto_data()
            filtered_data = filter_data(data, args)
            print_table(filtered_data)

            print("\ntarmacvum e", args.refresh, "varkyan...\n")
            time.sleep(args.refresh)
    else:
        data = get_crypto_data()
        filtered_data = filter_data(data, args)
        print_table(filtered_data)


main()