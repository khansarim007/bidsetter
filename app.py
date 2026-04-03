import os

from flask import Flask, render_template, request

app = Flask(__name__)

MOCK_SALES = [118.0, 124.5, 121.0, 129.0, 116.0]
SELLING_FEE_RATE = 0.13
SHIPPING_COST = 6.0
TARGET_MARGIN = 0.25
DEMO_URL = "https://www.ebay.com/itm/demo-listing"


def analyze_listing(url: str) -> dict:
    average_sale = round(sum(MOCK_SALES) / len(MOCK_SALES), 2)
    max_safe_bid = round(average_sale * (1 - SELLING_FEE_RATE - TARGET_MARGIN) - SHIPPING_COST, 2)

    expected_sale_price = average_sale
    platform_fees = round(expected_sale_price * SELLING_FEE_RATE, 2)
    expected_profit = round(expected_sale_price - max_safe_bid - platform_fees - SHIPPING_COST, 2)

    return {
        "listing_url": url,
        "item_name": "2021 Prizm Silver PSA 10",
        "recent_sales": MOCK_SALES,
        "average_sale": average_sale,
        "max_safe_bid": max_safe_bid,
        "platform_fees": platform_fees,
        "shipping_cost": SHIPPING_COST,
        "expected_profit": expected_profit,
        "target_margin": int(TARGET_MARGIN * 100),
    }


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None

    if request.method == "POST":
        listing_url = request.form.get("listing_url", "").strip()
        if not listing_url:
            error = "Paste a listing URL first."
        else:
            result = analyze_listing(listing_url)

    demo_result = analyze_listing(DEMO_URL)
    analysis = result or demo_result
    is_demo = result is None

    return render_template("index.html", result=analysis, error=error, is_demo=is_demo)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port, debug=True)
