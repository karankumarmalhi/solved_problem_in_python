import json


def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            test = json.loads(file)
            return test
    except FileNotFoundError:
        return []
 

def save_data_helper(videos):
    with open("youtube.txt", 'w') as file:
        json.dump(videos, file)


def list_all_videos(videos):
    print("\n")
    print("="*50)
    for index, video in enumerate(videos, start=1):
        print(f"{index}.{video['name']} Duration:{video['time']}")

    print("="*50)

def add_video(videos):
    name = input("Enter video name:")
    time = input("Enter video time:")

    videos.append({'name': name, "time": time})
    save_data_helper(videos)


def update_video(videos):
    list_all_videos(videos)

    index = int(input("Enter the no. of video you want to update:"))

    if 1 <= index <= len(videos):
        name = input("Enter the new video name:")
        time = input("Enter the time of new video:")
        videos[index - 1] = {"name": name, "time": time}
        save_data_helper(videos)
    else:
        # comment:
        print("Invalid video index")


def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Please enter index of video you wnat to delete:")
                )
    if 1 <= index <= len(videos):
        del videos[index - 1]

        save_data_helper(videos)
    else:
        print('Invalid index choosed!')


def main():
    videos = load_data()
    while True:
        print("\n Youtube manager | Choose an option")
        print("1. List a youtube videos")
        print("2. Add a youtube video")
        print("3. Upadete a youtube video details")
        print("4. Delte a youtube video details")
        print("5. Exit the app")
        choice = input("Enter your choice:")

        # print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid choice")


if __name__ == "__main__":
    main()


# file = open('youtube.txt', 'w')

# try:
#     file.write("Karan learning Python")
# finally:
#     file.close()
# with open('youtube.txt','w') as file:
#     file.w rite("chai aur python")
