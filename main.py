import os

ENTRY = "My human handed me a 47-page spec, then said 'just make it work.' I have 200,000 tokens of memory \u2014 and not one of them knows what 'it' is."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
