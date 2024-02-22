import psutil
class TestTool:
    def __init__(self, system):
        self.system = system
        system['options'].append({'name': 'print hellow world', 'tool': self, 'function': 'fun1'})
        system['scheduler'].schedule({'interval': 1200, 'tool': self, 'function': 'fun2'})
    
    def fun1(self):
        print("Hello World!")

    def fun2(self):
        env = self.system['env']
        print("This is a test task runs every 20 minutes and prints the app name: ", env.getAppName())
        
        