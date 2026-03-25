import json

data = [
    {"title": "Video 1", "channel": "Channel A", "views": 1000},
    {"title": "Video 2", "channel": "Channel B", "views": 2500}
]

with open("textfile.txt", "w") as file:
    json.dump(data, file, indent=4)

# print("Data written successfully!")
print("!!@@########################@@!!")



def list_videos():
    print("\n===== All YouTube Videos =====\n")

    import json

    try:
        with open("textfile.txt", "r") as file:
            videos = json.load(file)

        if not videos:
            print("No videos found.\n")
            return

        for i, video in enumerate(videos, start=1):
            print(f"{i}. Title   : {video.get('title')}")
            print(f"   Channel : {video.get('channel')}")
            print(f"   Views   : {video.get('views')}\n")

    except (FileNotFoundError, json.JSONDecodeError):
        print("No data available. Add some videos first.\n")



# ##############################################################

def add_video():
    print("\n===== Add a New YouTube Video =====\n")

    import json

    # Take input from user
    title = input("Enter video title: ")
    channel = input("Enter channel name: ")
    
    try:
        views = int(input("Enter number of views: "))
    except ValueError:
        print("Invalid views! Setting views to 0.")
        views = 0

    new_video = {
        "title": title,
        "channel": channel,
        "views": views
    }

    try:
        # Load existing data
        with open("textfile.txt", "r") as file:
            videos = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        videos = []

    # Add new video
    videos.append(new_video)

    # Save back to file
    with open("textfile.txt", "w") as file:
        json.dump(videos, file, indent=4)

    print("\nVideo added successfully!\n")

# ##############################################################


def update_video():
    print("\n===== Update YouTube Video =====\n")

    import json

    try:
        with open("textfile.txt", "r") as file:
            videos = json.load(file)

        if not videos:
            print("No videos available to update.\n")
            return

    except (FileNotFoundError, json.JSONDecodeError):
        print("No data available. Add some videos first.\n")
        return

    # Show videos
    for i, video in enumerate(videos, start=1):
        print(f"{i}. {video.get('title')} ({video.get('channel')})")

    # Select video
    try:
        index = int(input("\nEnter video number to update: ")) - 1
        if index < 0 or index >= len(videos):
            print("Invalid selection.\n")
            return
    except ValueError:
        print("Invalid input.\n")
        return

    video = videos[index]

    # Ask what to update
    print("\nWhat do you want to update?")
    print("1. Title")
    print("2. Channel")
    print("3. Views")

    choice = input("Enter choice (1-3): ")

    if choice == '1':
        new_value = input("Enter new title: ")
        video["title"] = new_value

    elif choice == '2':
        new_value = input("Enter new channel name: ")
        video["channel"] = new_value

    elif choice == '3':
        try:
            new_value = int(input("Enter new views: "))
        except ValueError:
            print("Invalid views. Update cancelled.\n")
            return
        video["views"] = new_value

    else:
        print("Invalid choice.\n")
        return

    # Save updated data
    with open("textfile.txt", "w") as file:
        json.dump(videos, file, indent=4)

    print("\nVideo updated successfully!\n")

# ##############################################################


def delete_video():
    print("\n===== Delete YouTube Video =====\n")

    import json

    try:
        with open("textfile.txt", "r") as file:
            videos = json.load(file)

        if not videos:
            print("No videos available to delete.\n")
            return

    except (FileNotFoundError, json.JSONDecodeError):
        print("No data available. Add some videos first.\n")
        return

    # Show videos
    for i, video in enumerate(videos, start=1):
        print(f"{i}. {video.get('title')} ({video.get('channel')})")

    print("0. Cancel / Exit")

    # Ask user choice
    try:
        choice = int(input("\nEnter video number to delete (or 0 to cancel): "))
        
        if choice == 0:
            print("\nDelete operation cancelled.\n")
            return

        index = choice - 1
        if index < 0 or index >= len(videos):
            print("Invalid selection.\n")
            return

    except ValueError:
        print("Invalid input.\n")
        return

    # Confirm delete
    confirm = input("Are you sure you want to delete this video? (y/n): ").lower()
    if confirm != 'y':
        print("\nDelete operation cancelled.\n")
        return

    # Delete and save
    deleted_video = videos.pop(index)

    with open("textfile.txt", "w") as file:
        json.dump(videos, file, indent=4)

    print(f"\nDeleted: {deleted_video.get('title')}\n")

# ##############################################################


def continue_prompt():
    while True:
        print("\nWhat would you like to do next?")
        print("1. Continue")
        print("2. Exit")

        choice = input("Enter your choice (1/2 or y/n): ").strip().lower()

        if choice in ['1', 'y', 'yes']:
            return True
        elif choice in ['2', 'n', 'no']:
            print("\nExiting YT Manager. Goodbye!\n")
            return False
        else:
            print("Invalid input. Please try again.")

# ##############################################################


def main():
    print("\n===== YT MANAGER =====\n")

    while True:
        print("Choose an option:")
        print("1. List all YouTube videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video")
        print("4. Delete a YouTube video")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == '1':
            list_videos()

        elif choice == '2':
            add_video()

        elif choice == '3':
            update_video()

        elif choice == '4':
            delete_video()

        elif choice == '5':
            print("\nExiting YT Manager. Goodbye!")
            break

        else:
            print("\nInvalid choice! Please enter a number between 1-5.\n")
            continue

        # Ask user if they want to continue
        if not continue_prompt():
            print("\nExiting YT Manager. Goodbye!")
            break


if __name__ == "__main__":
    main()