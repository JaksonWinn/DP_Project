# Read in the input file from command line
for i in range(3):
    file_input = input()
    
    #Assign variables to respected values
    if i == 0:
        first_line = file_input.split()
        num_tasks = int(first_line[0])+1
        desired_points = int(first_line[1])+1
    elif i == 1:
        point_vals = file_input.split()
    elif i == 2:
        effort_hours = file_input.split()

#initialize empty 2D array of tuples (the first value is the value of the cell, the second value is the type of cell 
# for traceback implmentation) as the DP table
DP = [[(0,  "empty") for i in range(desired_points)] for j in range(num_tasks)]

#Function for Bottom-Up DP
def grade_bottom_up(DP, num_tasks, desired_points, point_vals, effort_hours): 

    #Base case: if i == 0 and j > 0 then DP[i][j] = infinity, "B" is for the traceback step indicating base case
    DP[0][1:] = [(float("inf"), "B")] * (desired_points -1)

    #Nested for loops to iterate through every cell in the DP table 
    for i in range(1, num_tasks):
        for j in range(1, desired_points):
            if j >= int(point_vals[i-1]): 

                #Take the minimum of 
                if DP[i-1][j][0] <= DP[i-1][max(0, j - int(point_vals[i-1]))][0] + int(effort_hours[i-1]):
                    DP[i][j] = (DP[i-1][j][0], "D")
                else:
                    DP[i][j] = (DP[i-1][max(0, j - int(point_vals[i-1]))][0] + int(effort_hours[i-1]), "SK")             
            else:
                if DP[i-1][j][0] <= int(effort_hours[i-1]):
                    DP[i][j] = (DP[i-1][j][0], "D")
                else:
                    DP[i][j] = (int(effort_hours[i-1]), "SE")
    return DP

def trace_back(DP, num_tasks, desired_points):
    num_selected = 0
    selected_tasks = []
    curr_row = num_tasks-1
    curr_col = desired_points-1
    while curr_row > 0 and curr_col > 0:
        decision = DP[curr_row][curr_col][1]
        if decision == "SK":
            num_selected += 1
            selected_tasks.append(curr_row)
            curr_col -= int(point_vals[curr_row -1])
        elif decision == "D":
            curr_row -= 1
        elif decision == "SE":
            num_selected += 1
            selected_tasks.append(curr_row)
            curr_col -= int(point_vals[curr_row -1])
    return num_selected, selected_tasks
    
DP = grade_bottom_up(DP, num_tasks, desired_points, point_vals, effort_hours)
num_selected, selected_tasks = trace_back(DP, num_tasks, desired_points)

if DP[num_tasks-1][desired_points-1][0] == float("inf"):
   print(-1)
else:
    num_selected, selected_tasks = trace_back(DP, num_tasks, desired_points)
    print(DP[num_tasks-1][desired_points-1][0])
    print(num_selected)
    if not selected_tasks:
        print(0)
    else:
        print(*selected_tasks[::-1])

        
