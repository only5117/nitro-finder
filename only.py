import random
import string
import requests
import time

# ── Configuration ────────────────────────────────────────────────────────────
WEBHOOK_URL = "https://discord.com/api/webhooks/YOUR_WEBHOOK_ID/YOUR_WEBHOOK_TOKEN"
DELAY = 1.0  # seconds between requests (be respectful / avoid rate-limits)
# ─────────────────────────────────────────────────────────────────────────────

CHARS = string.ascii_letters + string.digits


def generate_code(length: int = 18) -> str:
    return "".join(random.choices(CHARS, k=length))


def check_code(code: str) -> bool:
    url = (
        f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}"
        "?with_application=false&with_subscription_plan=true"
    )
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print(f"[HIT] Valid code found: {code}")
            send_to_webhook(code, response.json())
            return True
        else:
            print(f"[MISS] {code} → {response.status_code}")
            return False
    except requests.RequestException as e:
        print(f"[ERROR] Request failed for {code}: {e}")
        return False


def send_to_webhook(code: str, data: dict) -> None:
    payload = {
        "content": f"✅ **Valid Discord gift code found!**\n```{code}```",
        "embeds": [
            {
                "title": "Gift Code Details",
                "description": f"**Code:** `{code}`",
                "color": 0x57F287,
                "fields": [
                    {
                        "name": "Raw Response",
                        "value": f"```json\n{str(data)[:1000]}\n```",
                    }
                ],
            }
        ],
    }
    try:
        r = requests.post(WEBHOOK_URL, json=payload, timeout=10)
        if r.status_code in (200, 204):
            print(f"[WEBHOOK] Successfully sent code {code} to webhook.")
        else:
            print(f"[WEBHOOK] Failed to send — status {r.status_code}: {r.text}")
    except requests.RequestException as e:
        print(f"[WEBHOOK ERROR] {e}")


def main() -> None:
    print("Starting gift code checker… (Ctrl+C to stop)\n")
    checked = 0
    hits = 0
    try:
        while True:
            code = generate_code()
            if check_code(code):
                hits += 1
            checked += 1
            print(f"  Checked: {checked} | Hits: {hits}", end="\r")
            time.sleep(DELAY)
    except KeyboardInterrupt:
        print(f"\n\nStopped. Checked {checked} codes, found {hits} hits.")


if __name__ == "__main__":
    main()
