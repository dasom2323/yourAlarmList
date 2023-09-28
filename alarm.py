import datetime
import os
import time
import random
import webbrowser

#Fall 2020
#Dasom Lee
#Seungpil Huh

def check_alarm_input(alarm_time):
    """Checks to see if the user has entered in a valid alarm time"""
    if len(alarm_time) == 1: # [Hour] Format
        if alarm_time[0] < 24 and alarm_time[0] >= 0:
            return True
    if len(alarm_time) == 2: # [Hour:Minute] Format
        if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
           alarm_time[1] < 60 and alarm_time[1] >= 0:
            return True
    elif len(alarm_time) == 3: # [Hour:Minute:Second] Format
        if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
           alarm_time[1] < 60 and alarm_time[1] >= 0 and \
           alarm_time[2] < 60 and alarm_time[2] >= 0:
            return True
    return False

#Make music list by genre
def genre_alarm():
    cnt = 0
    global genreNames_array
    genreNames_array = []
    global link_array
    link_array = []

    add = input("Do you want to add genre for your list?\n1. Yes\n2. No\nEnter your choice: ")
    if add == "2":
        main()
    while add == "1":
        genreName = input("Enter the genre name for your list: ")
        genreNames_array.append(genreName)
        # If video URL file does not exist, create one
        if not os.path.isfile(genreName):
            print('Creating ' + genreName + ' list for you')
            with open(genreName+'.txt', "w") as alarm_file:
                alarm_file.write(genreName)
        ans = input("Do you want to add link for this genre?\n"
                "1. Yes\n2. No\nEnter your choice: ")
        while ans == "1":
            link = input("Enter the link that you want to add for " + genreName + ": ")
            text_file = open(genreName+'.txt', "a+")
            text_file.write("\n" + link)
            link_array.append(link)
            ans = input("1. Adding more links for this genre\n2. Done\nEnter your choice: ")

        text_file.close()

        add = input("Do you want to add another genre of music?\n"
                     "1. Yes\n2. No\nEnter your choice: ")
        if add == "2":
            main()


#Show the music list
def show_alarm():
    cnt = 0
    print("Here is your music list")
    for x in range(len(genreNames_array)):
        print(str(cnt+1) + ". " + genreNames_array[cnt])
        cnt += 1

    ans = int(input("Enter the number to see the link for the genre you want: "))
    openFile = genreNames_array[ans-1]
    text_file = open(openFile + '.txt', "r")
    Lines = text_file.readlines()[1:]

    print("Here is the link for " + openFile)

    count = 0
    for line in Lines:
        print("Link{}: {}".format(count+1, line.strip()))
        count += 1
    text_file.close()
    main()

#Set up for the alarm
def setup_alarm():
    cnt = 0
    print("Here is your music list")
    for x in range(len(genreNames_array)):
        print(str(cnt + 1) + ". " + genreNames_array[cnt])
        cnt += 1

    ans = int(input("Which genre of music do you want for the alarm?\nEnter your choice:  "))

    print("Set a time for the alarm (Ex. 06:30 or 18:30:00)")

    while True:
        alarm_input = input(">> ")
        try:
            alarm_time = [int(n) for n in alarm_input.split(":")]
            if check_alarm_input(alarm_time):
                break
            else:
                raise ValueError
        except ValueError:
            print("ERROR: Enter time in HH:MM or HH:MM:SS format")

    # Convert the alarm time from [H:M] or [H:M:S] to seconds
    seconds_hms = [3600, 60, 1]  # Number of seconds in an Hour, Minute, and Second
    alarm_seconds = sum([a * b for a, b in zip(seconds_hms[:len(alarm_time)], alarm_time)])

    # Get the current time of    day in seconds
    now = datetime.datetime.now()
    current_time_seconds = sum([a * b for a, b in zip(seconds_hms, [now.hour, now.minute, now.second])])

    # Calculate the number of seconds until alarm goes off
    time_diff_seconds = alarm_seconds - current_time_seconds

    # If time difference is negative, set alarm for next day
    if time_diff_seconds < 0:
        time_diff_seconds += 86400  # number of seconds in a day

    # Display the amount of time until the alarm goes off
    print("Alarm set to go off in %s" % datetime.timedelta(seconds=time_diff_seconds))

    # Sleep until the alarm goes off
    time.sleep(time_diff_seconds)

    # Time for the alarm to go off
    print("Wake Up!")

    # Load list of possible video URLs
    genre = genreNames_array[ans - 1]
    fileToOpen = random_line(genre + ".txt")
    with open(genre + ".txt", "r") as alarm_file:
        videos = fileToOpen

    # Open a random video from the list
    webbrowser.open(videos)
    main()
#Getting random line

def random_line(fname):
    with open(fname) as f:
        lines = f.readlines()[1:]
        myline = random.choice(lines)
        return myline


# main
def main():
    ans = input("=========== Main ===========\n1. Show my music list\n2. Make a new music list. \n3. Set the time for the alarm.\n4. Done\n Enter your choice: ")
    while ans != "4" :
     if ans == "1":
        show_alarm()
     elif ans == "2":
         genre_alarm()
     elif ans == "3":
         setup_alarm()
     else:
         print("You entered wrong number. Please try again! Thank you.")

    if ans == "4":
        print("Thanks. You have a good day!")
        exit()

#Basic
main()