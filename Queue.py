#DECLARE len_queue, head_pointer, tail_pointer : INTEGER
#DECLARE queue : ARRAY[0:4] OF STRING
len_queue = 5
queue = [""] * 5
head_pointer = -1
tail_pointer = 0
flag = False

def enqueue(data):
    global queue
    global head_pointer
    global tail_pointer

    if tail_pointer >= len_queue:
        print("Queue is Full!")
        return False
    else:
        queue[tail_pointer] = data
        tail_pointer += 1
        if head_pointer == -1:
            head_pointer = 0
        return True

def dequeue():
    global queue
    global head_pointer
    global tail_pointer

    if head_pointer == -1:
        print("Queue is Empty!")
        return -1
    else:
        element = queue[head_pointer]
        queue[head_pointer] = ""
        head_pointer += 1
        if head_pointer == tail_pointer:
            head_pointer = -1
            tail_pointer = 0
        return element

while flag == False:
    print("1.Push")
    print("2.Pop")
    print("3.Print")
    print("4.Exit")

    choice = int(input("Enter Your Choice:"))
    if choice == 1:
        value = input("Enter Your Value:")
        check = enqueue(value)
        if check == True:
            print("Data has been Pushed")
    elif choice == 2:
        popped = dequeue()
        if popped != -1:
            print(f"{popped} has been Popped")
    elif choice == 3:
            print(queue)
    elif choice == 4:
        flag = True
    else:
        print("Invalid Option Was Entered")