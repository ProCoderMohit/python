from threading import Thread,current_thread
from tkinter.ttk import tclobjs_to_py

#Using Multiple Threads in program or process:MultiThreading

# t=threading.current_thread().name#gives the current thread.
# print("Mohit")
# print(t)

#********creating a thread without using a class.(but we have to use thread class)***********

# def disp(a):
#     print("Thread running...")
    
# t=Thread(target=disp,args=(10,))

# t.start()#starts our own thread.

#after starting our own thread there are two threads present which are main thread and our own thread.
# def disp1():
#     for i in range(5):
#         print("Child Thread")
# t=Thread(target=disp1)


# for i in range(5):
#     print("Main Thread")

#set and get thread name

# def disp():
#     print("Child_Thread",current_thread())
    
# t=Thread(target=disp)
# t.start()

# print("Main Thread",current_thread())

# def disp():
#     print("Child_Thread",current_thread().getName())
    
# t=Thread(target=disp)
# t.start()

# print("Main Thread",current_thread().getName())


# def disp():
#     print("Child_Thread",current_thread().getName())
#     current_thread().setName("Mohit")
#     print("Child_Thread",current_thread().getName())
    
# t=Thread(target=disp)
# t.start()

# print("Main Thread",current_thread().getName())
# current_thread().setName("Kumar")
# print("Main Thread",current_thread().getName())


# def disp():
#     print("Default Child Name",current_thread().name)
#     current_thread().name="Mohit"
#     print("Changed Child Name",current_thread().name)
    
    
# t=Thread(target=disp)
# t.start()

# print("Default Main Name",current_thread().name)
# current_thread().name="Kumar"
# print("Changed Main Name",current_thread().name)


# def disp():
#     pass

# t=Thread(target=disp)
# print(t.getName())
# t.setName("Mohit")
# print(t.name)

# def disp():
#     pass

# t=Thread(target=disp,name="Mohit's Thread")
# print(t.name)





#******Creating a thread by creating a child class to Thread class*********
# class Mythread(Thread):
#     pass

# t=Mythread()
# print(t.name)

#methods of thread class

# class Mythread(Thread):
#    def run(self):
#        print("Run Method")

# t=Mythread()
# t.start()#run method is called when the start method is called 
# t.join()#pauses all the other threads till it completes its execution
# print("Main Thread")



#****Multitasking using multiple threads**** 

# class Hotel:
#     def __init__(self,t):
#         self.t=t 
#     def food(self):
#         for i in range(1,6):
#             print(self.t,i)
# h1=Hotel('Take order from table')
# h2=Hotel('Serve order to table')
# t1=Thread(target=h1.food)
# t2=Thread(target=h2.food)
# t1.start()
# t2.start()

#thread race
class Flight:
    def __init__(self,available_seats):
        self.available_seats=available_seats
        
    def reserve(self,need_seats):
        print('Available seats:',self.available_seats)
        if self.available_seat>=need_seats:
            name=current_thread().name
            print(f'{need_seats} seta is alloted for {name}')
            self.available_seats-=need_seats
            
        else:
            print('Sorry! All seats has been alloted')
            
f=Flight(1)
t1=Thread(target=f.reserve,args=(1,),name="Mohit")
t2=Thread(target=f.reserve,args=(1,),name="Shivam")
t1.start()
t2.start()
            