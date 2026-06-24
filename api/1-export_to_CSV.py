#!/usr/bin/python3
import csv
import requests
import sys


def main():
    """Fetch data and write CSV rows with all tasks for the user."""
    if len(sys.argv) < 2:
        sys.exit(0)

    try:
        user_id = int(sys.argv[1])
    except ValueError:
        sys.exit(0)

    base_url = "https://jsonplaceholder.typicode.com"
    reddit_user = requests.get(f"{base_url}/users/{user_id}").json()
    print(reddit_user)
    todos = requests.get(f"{base_url}/todos", params={"userId": user_id}).json()

    username = reddit_user.get("username")
    filename = f"{user_id}.csv"
    print(username, filename)

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for t in todos:
            writer.writerow([
                str(user_id),
                username,
                str(t.get("completed")),
                t.get("title")
            ])


if __name__ == "__main__":
    main()
