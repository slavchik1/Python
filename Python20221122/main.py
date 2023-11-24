songs = []
singers = []


def help():
    print("""Показати це повідомлення знову: help
Додати пісню: add song
Список пісень: songs list
Прибрати пісню: remove song
Змінити виконавця пісні: change singer
""")


def add_song():
    song = input("Введіть ім'я пісні.\n")
    singer = input("Введіть виконавця пісні.\n")
    songs.append(song)
    singers.append(singer)


def songs_list():
    for i in range(len(songs)):
        print(songs[i] + " - " + singers[i])


def remove_song():
    remove = input("Введіть назву чи виконавця пісню яку ви хоті ли б прибрати.\n")
    for i in range(len(songs)):
        if songs[i] == remove or singers[i] == remove:
            songs.pop(i)
            singers.pop(i)
            break


def change_singer():
    change = input("Введіть ім'я пісні у якої ви хоті ли б змінити виконаця.\n")
    for i in range(len(songs)):
        if songs[i] == change:
            change = input("Виконавець вашої пісні: " + singers[
                i] + ", введіть виконавця на якого ви хотіли б змінити цього виконавця.\n")
            singers[i] = change


help()


while True:
    answer = input()
    if answer == "help":
        help()
    elif answer == "add song":
        add_song()
    elif answer == "songs list":
        songs_list()
    elif answer == "remove song":
        remove_song()
    elif answer == "change singer":
        change_singer()
    elif answer != "":
        print("Помилка: такої команди не існує.\n")
