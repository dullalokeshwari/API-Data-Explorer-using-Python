from api_service import get_posts
from utils import display_posts, search_posts, filter_posts_by_user, save_to_csv

def main():
    posts = get_posts()

    if not posts:
        print("No data available.")
        return

    while True:
        print("\n===== API DATA EXPLORER =====")
        print("1. View First 10 Posts")
        print("2. Search Post by Title")
        print("3. Filter Posts by User ID")
        print("4. Save Posts to CSV")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_posts(posts)

        elif choice == "2":
            keyword = input("Enter keyword: ")
            search_posts(posts, keyword)

        elif choice == "3":
            user_id = input("Enter User ID: ")
            filter_posts_by_user(posts, user_id)

        elif choice == "4":
            save_to_csv(posts)

        elif choice == "5":
            print("Thank You!")
            break

        else:
            print("Invalid Choice.")

if __name__ == "__main__":
    main()