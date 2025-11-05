# def on_click (callback):
#     print("button clicked")
#     callback()

# def show_msg():
#     print("Hello i am starwin")

# on_click(show_msg)


# def name(username):
#     print (f'hello{username}')

# def process_name(callback):
#     user_name = "starwin"
#     callback(user_name)

# process_name(name)


import time

def done():
    print("work finshed")

def do_task(callback):
    print("task starting..")
    time.sleep(3)
    callback()
do_task(done)