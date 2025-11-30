import requests, time

def metis_exit():
    print("Metis Andromeda — Whale Exit to Ethereum (> $5M via official bridge)")
    seen = set()
    while True:
        # Metis → Ethereum L1 bridge contract
        r = requests.get("https://andromeda-explorer.metis.io/api?module=account&action=txlist"
                        "&address=0x0000000000000000000000000000000000000000&sort=desc")
        for tx in r.json().get("result", [])[:30]:
            h = tx["hash"]
            if h in seen: continue
            seen.add(h)

            # Official Metis L2 → L1 withdrawal contract
            if tx["to"].lower() != "0x1e143b2580b78e9a7e1e4e8e87df80b6d15c7a0e": continue
            if "withdraw" not in tx.get("input", "").lower(): continue

            value = int(tx["value"]) / 1e18
            if value >= 5_000_000:  # > $5M exiting Metis Andromeda
                print(f"WHALE EXIT CONFIRMED\n"
                      f"${value:,.0f} permanently leaving Metis → Ethereum L1\n"
                      f"Wallet: {tx['from']}\n"
                      f"Tx: https://andromeda-explorer.metis.io/tx/{h}\n"
                      f"→ Capital flight from Layer 2 back to mainnet\n"
                      f"→ Someone just cashed out or lost confidence\n"
                      f"{'-'*70}")
        time.sleep(3.4)

if __name__ == "__main__":
    metis_exit()
