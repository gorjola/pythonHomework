import json

class Student:
    stud_avarage={}

    def read_json(self):
            with open("jsonfile.json","r") as file:
                data = json.load(file)
            return data

    def calculate_average(self,stud):
            for i in stud["students"]:
                self.stud_avarage[i["name"]]=round(sum(i["grades"])/len(i["grades"]),2)
            return self.stud_avarage
    def new_json(self):
        with open("newjason.json","w") as file:
            json.dump(self.stud_avarage,file,indent=2)




file=Student()
jfile=file.read_json()
file.calculate_average(jfile)
file.new_json()
