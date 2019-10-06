print ("Welkom")
print ("bij de Km -> Miles omzetter")

onemore = "ja"

while onemore == "ja":
    km = input("Welke aantal Km's wil je omzetten naar Miles?:")
    km = km.replace(" ","")
    km = km.replace(".","")
    if not km.isdigit():
        print ("de ingegeven waarde is geen cijfer")
        onemore = input("Wil je opnieuw invoeren? (ja of nee):")
        if onemore == "ja":
            continue
        else:
            print("Nog een fijne dag verder.")
            break
    else:
        km = int(km)
        miles = float(km*0.62137)
        print (" %.2f  Miles" % (miles))
        onemore = input("Wil je nog meer omzetten? (ja of nee):")
        if onemore == "ja":
            continue
        else:
            print ("Nog een fijne dag verder.")
            break