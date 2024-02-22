import psutil 

class ChargingTracker:
    def __init__(self, system):
        self.system = system
        self.scheduler = system['scheduler']
        self.speaker = system['speaker']

        system['scheduler'].schedule({
            'type': 'repeat',
            'interval': 60, 
            'tool': self, 
            'function': 'check_charge_state'
            })
        
        system['options'].append({
            'name': 'battery percent ?',
            'tool': self, 
            'function': 'show_power_percent'
            })


    def check_charge_state(self):
    
        battery = psutil.sensors_battery()

        if battery.power_plugged and battery.percent>=99:
            self.system['speaker'].speak("sir, Power level at "+str(int(battery.percent)) + " kindly switch off charging.")
            return
        elif not battery.power_plugged and battery.percent<40:
            self.system['speaker'].speak("sir, Power level at "+str(int(battery.percent)) + " kindly switch on charging.")
            return
        
    def show_power_percent(self):
        battery = psutil.sensors_battery()
        print(battery)
        
    
    def finish(self):
        self.speaker.speak("Charging tracker finished.")
