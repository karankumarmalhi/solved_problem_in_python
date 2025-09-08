import sqlite3

con = sqlite3.connect("video_manager.db")

cursor = con.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')

def list_all_videos():
        cursor.execute("SELECT * FROM videos")
        for row in cursor.fetchall():
            print(row)

def add_video():
    name = input("Enter the name of video:")
    time = input("Enter the duration of video:")
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    cursor.commit()
    

def update_video(video_id, name, time):
    cursor.execute("UPDATE videos SET naame = ? , time = ? WHERE id = ?",(name, time , video_id))
    cursor.commit()


def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    cursor.commit()

def main():
    while True:
        print("\n Video manager app with Database")
        print("1. List Videos")
        print("2. Add Video")
        print("3. Upadate Video")
        print("4. Delete Video")
        print("5. Exit App")

        choice = input("Enter you choice:")

        if choice == '1':
            list_all_videos()
        elif choice == '2':
            add_video()
        elif choice == '3':
            video_id = input("Enter the id of video:")
            name = input("Enter the of video name:")
            time = input("Enter the duration of the video:")
            update_video(video_id,name, time)
        elif choice == '4':
            video_id = input("Enter the id of video:")
            delete_video(video_id)
        elif choice == ' 5':
            break
        else:
            print("Invalid choice please choose ccorrect option!")
    
    con.close()

if __name__ == "__main__":
    main()