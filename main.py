from myenv import MyEnv
from mymemory import MyMemory
from scheduler import Scheduler
from speaker import Speaker
from tools.reminder import Reminder
from tools.charging_tracker import ChargingTracker

def menu():
    env = MyEnv(".env")
    memory = MyMemory()
    scheduler = Scheduler()
    speaker = Speaker()

    system = {}
    system['env'] = env
    system['memory'] = memory
    system['scheduler'] = scheduler
    system['speaker'] = speaker
    
    options = []
    system['options'] = options
    

    tools = []
    tools.append(Reminder(system))
    tools.append(ChargingTracker(system))

    system['speaker'].speak("Welcome to Tool v2")
    while True:

        print()
        print("___________________________________")
        print("|              2ulv2              |")
        print("|_________________________________|")
        print()


        for i,option in enumerate(options, start=0):
            print("%s. %s"%(i+1,option['name']))
        print("0. Exit")
        choice = input("Enter your choice: ")
        if choice == "0":

            for t in tools:
                t.finish()

            scheduler.close()
            env.close()
            print("Good Bye")
            break
        elif choice.isdigit():
            choice = int(choice)-1
            if choice<len(options):
                option = options[choice]
                tool = option['tool']
                function = getattr(tool,option['function'])
                function()
            else:
                print("Invalid choice. Please try again!")
                system['speaker'].speak("Invalid choice")

        else:
            print("Invalid choice. Please try again!")
            system['speaker'].speak("Invalid choice")

    scheduler.close()
    env.close()
    speaker.speak("Good Bye Sir, have a good day!")
    speaker.complete()
    speaker.finish()


if __name__ == '__main__':
    menu()