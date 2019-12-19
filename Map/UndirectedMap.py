import queue

class Person(object):
    def __init__(self,name):
        self.name = name
        self.friends = []
        self.visited = False

    def add_friend(self,friend):
        self.friends.append(friend)

    def display_network(self):
        #记下每个访问过的人
        to_reset = [self]
        #friendQueue = queue()
        friendQueue = queue.Queue()
        #friendQueue = 
        for frend in self.friends:
            friendQueue.put(frend)

        self.visited = True

        while friendQueue.qsize()>0:
            current_vertex = friendQueue.get()
            print(current_vertex.name)

            if len(current_vertex.friends)>0:
                for item in current_vertex.friends:
                    if item.visited == False:
                        to_reset.append(item)
                        friendQueue.put(item)
                        item.visited = True
        for item in to_reset:
            item.visited = False

mary = Person("Mary")
peter = Person("Peter")
mary.add_friend(peter)
#peter.add_friend(mary)
lin = Person("lin")
peng = Person("peng")
mary.add_friend(lin)
lin.add_friend(peng)
cheng = Person("cheng")
mary.add_friend(cheng)
mary.display_network()
