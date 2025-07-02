#!/usr/bin/env python3
import requests
import sys


def main():
    if len(sys.argv) == 2:
        location = sys.argv[1]
    else:
        print("Usage: python main.py <location>")
        sys.exit(1)
    url = f"https://wttr.in/{location}"
    respomse = requests.get(url)
    print(respomse.text)


if __name__ == "__main__":
    main()
