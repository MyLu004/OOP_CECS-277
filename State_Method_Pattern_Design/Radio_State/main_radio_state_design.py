
#State: a behavioral design pattern that lats an object alter its behavior when its internal state changes.
# Like Finite-State Machine

import radio

def main():
    myRadio = radio.Radio() #create the radio object

    done = False
    myRadio.channel_switch()
    while not done: #while not False -> while True
        choice = input("1.On\n2.Off\n3.Channel\n4.Quit:\n")

        if choice == 1:
            #turn on

            print(myRadio.on_switch())
        elif choice == 2:
            #turn off
            print(myRadio.off_switch())
        elif choice == 3:
            print(myRadio.channel_switch())
            #switch channel
        elif choice ==4:
            #quit
            done = True




main()