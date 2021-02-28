from datetime import datetime
import os

## spl1ffy.tech

def generator(number):
    typebeats = "{} type beat\nfree {} type beat\n{} type beat 2021\nfree {} type beat 2021\n{} hard type beat\n{} hard type beat 2021\n"
    today = datetime.now()
    d1 = today.strftime("%d_%m_%Y-%H:%M:%S")
    filename = d1 +".csv"
    #dirname = os.path.dirname(filename)
    if os.path.exists(filename):
        append_write = 'a' # append if already exists
    else:
        append_write = 'w' # make a new file if not
    f = open("keywords/"+filename, append_write)
    i = 1
    for x in range (number):
        artist = input("Enter " + str(i) + ". Artist: ")
        result = typebeats.format(artist, artist, artist, artist, artist, artist, 6)
        f.write(result)
        i = int(i) + 1 
    print("Done!")
    f.close
    
number = int(input("Number of Artists: "))
generator(number)