from pathlib import Path
class MyMemory:
    def __init__(self):
        self.file_name = "./memory.txt"
        path = Path(self.file_name)
        if path.is_file():
            file = open(self.file_name)
            lines = file.readlines()
            data = {}
            for line in lines:
                line = line.strip()
                if line != "":
                    kv = line.split('=')
                    data[kv[0]]=kv[1]
            self.data = data
            file.close()
        else:
            self.data={}

    def get(self, key):
        if key in self.data:
            return self.data[key]
        else:
            return None

    def set(self,data):
        for key in data:
            self.data[key] = data[key]

        myfile = open("memory.txt","w")
        for key in self.data:
            print(key+"="+self.data[key], file=myfile)
        myfile.flush()
        myfile.close()

        