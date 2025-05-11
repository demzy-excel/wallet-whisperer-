def run(query: str) -> str:
    if "profit" in query:
        return "You made $76 profit this week based on your latest wallet activity."
    elif "airdrop" in query:
        return "You received 3 small airdrops. The highest one is worth $12."
    elif "gas fee" in query:
        return "Your most expensive token is XYZ, it used $23 in gas last month."
    elif "compare" in query:
        return "Last month: +$50. This week: +$15. Less active but still green."
    else:
        return "Wallet Whisperer here. Ask about profit, gas, or airdrops!"
