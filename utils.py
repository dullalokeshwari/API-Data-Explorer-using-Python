import csv

def display_posts(posts):
    print()

    for post in posts[:10]:
        print("Post ID :", post["id"])
        print("User ID :", post["userId"])
        print("Title   :", post["title"])
        print("-" * 40)


def search_posts(posts, keyword):
    found = False

    for post in posts:
        if keyword.lower() in post["title"].lower():
            print("\nPost ID :", post["id"])
            print("Title   :", post["title"])
            found = True

    if not found:
        print("No matching posts found.")


def filter_posts_by_user(posts, user_id):
    found = False

    for post in posts:
        if str(post["userId"]) == user_id:
            print("\nPost ID :", post["id"])
            print("Title   :", post["title"])
            found = True

    if not found:
        print("No posts found for this User ID.")


def save_to_csv(posts):
    with open("posts.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["User ID", "Post ID", "Title"])

        for post in posts:
            writer.writerow([
                post["userId"],
                post["id"],
                post["title"]
            ])

    print("posts.csv created successfully.")