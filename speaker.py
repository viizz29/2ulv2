import pyttsx3
import threading
import time
from datetime import datetime


class Speaker:
    def __init__(self):    
        self.queue = []
        self.should_stop = False
        self.thread = threading.Thread(target=self.thread_fun, args=(1,))
        self.lock = threading.Lock()
        self.thread.start()

    def speak(self, text):
        self.lock.acquire()
        self.queue.append(text)
        self.lock.release()

    def thread_fun(self, args):
        while not self.should_stop:
            self.lock.acquire()
            if len(self.queue)>0:
                text = self.queue.pop(0)
                self.lock.release()

                engine = pyttsx3.init()        
                print(datetime.now().strftime("%H:%M:%S"), "speaker: ",  text)
                engine.say(text)
                engine.runAndWait()
            else:
                self.lock.release()
            time.sleep(1)
        print("Speaker is shutting down!")

    def complete(self):
        while len(self.queue)>0:
            time.sleep(1)

    def finish(self):
        self.should_stop = True
        self.thread.join()
        print("Speaker finished!")

if __name__ == "__main__":
    speaker = Speaker()
    speaker.speak("Hello, How are you?")
    print("Hi")
    speaker.speak("Good Night")
    print("Hello")
    time.sleep(10)
    speaker.finish()