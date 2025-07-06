#!/usr/bin/env python3
"""Weather CLI Tool"""

import sys
import requests


def main():
    """Main function to get weather information for a given location."""
    if len(sys.argv) == 2:
        location = sys.argv[1]
    else:
        print("Usage: python main.py <location>")
        sys.exit(1)
    url = f"https://wttr.in/{location}"
    respomse = requests.get(url, timeout=10)
    print(respomse.text)


if __name__ == "__main__":
    main()
