'''
Derek Yang
CS 325
Homework 4
last_to_start.py
In this program, we take a file named "act.txt" and process
the activities inside.  Each will be processed using the
last to start method.  The sort is used with python's
build in sort function.
'''

def last_to_start(arrIn):
    tmp_arr = sorted(arrIn,key=lambda x: x[1], reverse=True)
    tmp = []
    n = len(tmp_arr)
    k = 0
    tmp.append(tmp_arr[k])
    for m in range(n):
        if tmp_arr[m][2] <= tmp_arr[k][1]:
            tmp.append(tmp_arr[m])
            k = m
    return tmp

def process(arrComboIn):
    print("---------------------")
    for x in range(len(arrComboIn)):
        # set name
        print("Set"+str(x+1))
        # process activities list
        tmp_activities_list = last_to_start(arrComboIn[x])
        # print number of activities selected
        print("Number of activities selected "+ str(len(tmp_activities_list)))
        # print list of activities
        print("Activities:",end="")
        for y in range(len(tmp_activities_list)-1,-1,-1):
            print(str(tmp_activities_list[y][0])+" ",end="")
        print("\n---------------------")

def main():
    combo_array = []
    # arr pos 0 activity, 1 start, 2 end
    tmp_activities = []
    f = open("act.txt","r+")
    read_one = f.read().splitlines()
    for x in read_one:
        if (' ' in x) == True:
            #   creates a temporary activity array
            tmp_act = [int(i) for i in x.split()]
            tmp_activities.append(tmp_act)
        else:
            combo_array.append(tmp_activities)
            tmp_activities = []
    combo_array.append(tmp_activities)
    combo_array.pop(0)
    for x in combo_array:
        print(x)

    process(combo_array)

if __name__ == "__main__":
    main()