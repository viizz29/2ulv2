from datetime import datetime
import time
from threading import Thread

class Scheduler:
    def __init__(self):
        self.tasks = []
        self.time_to_stop = False
        self.start_time = datetime.now()
        
        self.thread = Thread(target=self.thread_fun, args = ())
        self.thread.start()
    
    def thread_fun(self):
        while not self.time_to_stop:
            current_time = datetime.now()
            for task in self.tasks:
                type = task['type']
                if type == 'repeat':
                    diff = (current_time - task['last_time']).total_seconds()
                    if diff>task['interval']:
                        function = getattr(task['tool'], task['function'])
                        function()
                        task['last_time']= current_time
                elif type == "once":
                    if current_time >= task['time']:
                        function = getattr(task['tool'], task['function'])
                        function()
                        self.tasks.remove(task)
                        break
            time.sleep(1)
            
    def schedule(self, task):
        if task['type'] == 'repeat':
            task['last_time']=datetime.now()
            self.tasks.append(task)
        elif task['type'] == 'once':
            current_time = datetime.now()
            if task['time'] > current_time:
                self.tasks.append(task)

    

    def close(self):
        self.time_to_stop = True
        self.thread.join()
        print("Scheduler finished ...")
    