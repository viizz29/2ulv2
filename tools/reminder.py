from datetime import datetime

class Reminder:
    def __init__(self, system):
        self.system = system
        self.scheduler = system['scheduler']
        self.speaker = system['speaker']

        self.scheduler.schedule({
                'type': 'once', 
                'time': datetime.now().replace(hour=12, minute=55, second=0), 
                'tool': self, 
                'function': 'remind_about_lunch_time'
                })
    
        self.scheduler.schedule({
                'type': 'once', 
                'time': datetime.now().replace(hour=18, minute=25, second=0), 
                'tool': self, 
                'function': 'remind_go_pack_up'
                })
        
        self.scheduler.schedule({
            'type': 'repeat', 
            'interval': 1200,
            'tool': self,
            'function': 'speak_give_rest_to_eyes'
            })



    def speak_give_rest_to_eyes(self):
        self.speaker.speak("sir, kindly look at some far away object for 20 seconds")

    def remind_about_lunch_time(self):
        self.speaker.speak("sir, it is time to have lunch")

        
    def remind_go_pack_up(self):
        self.speaker.speak("sir, it is time to pack up todays work")
    
    def finish(self):
        self.speaker.speak("reminder finished")
