from PyQt5.QtCore import QDate
import json


class Project():
    PRIORITIES={
        0: "низкий",
        1: "высокий"
    }

    def __init__(self, name,date_p=QDate.currentDate(), is_done_p=False, priority=0,tasks_p=[]):
        self.name_project=name
        self.date=date_p
        self.is_done=is_done_p
        self.priority=priority
        self.tasks=tasks_p


    def dictionary(self):
        d={
            'name': self.name_project,
            'date': self.date.toString('dd.MM.yyyy'),
            'is_done': self.is_done,
            'priority':self.priority,
            'tasks_s': [i.dictionary() for i in self.tasks]
        }
        return d

    @staticmethod
    def list_from_dictionary(pp):
        task_p=[Task.list_from_dictionary(t) for t in pp['tasks_s']]
        return Project(pp['name'], QDate.fromString(pp['date'], 'dd.MM.yyyy'), pp['is_done'],pp['priority'], task_p)


    def add_task(self, t):
        self.tasks.append(t)

    def delete_task(self,t):
        if t in self.tasks:
            self.tasks.remove(t)

    def change_time(self, day, month, year):
        self.date = QDate(year, month, day)

    def rename_project(self,new_name):
        self.name_project=new_name

    def change_status_1(self):
        if  not self.is_done:
            self.is_done=True
        else:
            self.is_done=False
        return self.is_done

    def change_priority_1(self, new_p):
        self.priority=new_p







class Task():
    PRIORITIES = {
        0: "низкий",
        1: "высокий"
    }

    def __init__(self, name_t,date_t=QDate.currentDate(), is_done_t=False, priority=0):
        self.name_task=name_t
        self.date=date_t
        self.is_done=is_done_t
        self.priority=priority

    def change_time(self, day, month, year):
        self.date = QDate(year, month, day)

    def rename_task(self, new_name_t):
        self.name_task = new_name_t

    def change_status_1(self):
        if  not self.is_done:
            self.is_done=True
        else:
            self.is_done=False
        return self.is_done

    def change_priority_1(self, new_t):
        self.priority=new_t





    def dictionary(self):
        d={
            'name': self.name_task,
            'date': self.date.toString('dd.MM.yyyy'),
            'is_done': self.is_done,
            'priority': self.priority
        }
        return d


    @staticmethod
    def list_from_dictionary(tt):
        return Task(tt['name'], QDate.fromString(tt['date'],'dd.MM.yyyy'), tt['is_done'], tt['priority'])




class Event():
    def __init__(self, name_e,date_e=QDate.currentDate()):
        self.name_event=name_e
        self.date=date_e

    def change_the_time_for_a_event(self, day, month, year):
        self.date = QDate.setDate(day, month, year)

    def rename_event(self, new_name_e):
        self.name_event = new_name_e

    def dictionary(self):
        d={
            'name': self.name_event,
            'date': self.date.toString('dd.MM.yyyy'),

        }
        return d


    @staticmethod
    def list_from_dictionary(e):
        return Event(e['name'], QDate.fromString(e['date'],'dd.MM.yyyy'))

#
# t_1=Task('PPP')
# print(t_1.dictionary())
#
#
# t_2=Task('OOO')
# t_3=Task('WWWW')
# p=Project('Qa')
# p.add_task(t_1)
# p.add_task(t_2)
# p.add_task(t_3)
# with open('json.json','w',encoding='utf-8') as file_1:
#     json.dump(p.dictionary(), file_1,indent=4)














#
# a=Project('Flower')
# t_1=Task('QW')
# t_2=Task('ZX')
# t_2.is_done=True
# a.add_task(t_1)
# a.add_task(t_2)
# print(a.tasks)

# d={
#     'Россия':'Москва',
#     'Китай':'Пекин',
#     'Великобритания':'Лондон'
# }
# print(d['Китай'])