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

#Initialize empty 2D array as the DP table
DP = [[0 for i in range(desired_points)] for j in range(num_tasks)]

#Function for Bottom-Up DP
def grade_bottom_up(DP, num_tasks, desired_points, point_vals, effort_hours): 

     #Base case: if i == 0 and j > 0 then DP[i][j] = infinity, "B" is for the traceback step indicating base case
    DP[0][1:] = [float("inf")] * (desired_points -1)

    #Nested for loops to iterate through every cell in the DP table
    for i in range(1, num_tasks):
        for j in range(1, desired_points):

            #Take the minimum of discarding the current task and selecting and continuing
            if j >= int(point_vals[i-1]): 
                if DP[i-1][j] <= DP[i-1][max(0, j - int(point_vals[i-1]))] + int(effort_hours[i-1]):

                    #Discarding the task
                    DP[i][j] = (DP[i-1][j])
                else:

                    #Selecting the current task and continuing
                    DP[i][j] = (DP[i-1][max(0, j - int(point_vals[i-1]))] + int(effort_hours[i-1]))             
            else:

                #Take the minimum of discrading the current task or selecting the current task and ending
                if DP[i-1][j] <= int(effort_hours[i-1]):

                    #Discarding the task
                    DP[i][j] = (DP[i-1][j])
                else:

                    #Selecting and Ending
                    DP[i][j] = (int(effort_hours[i-1]))
    return DP

#Get the DP Table  
DP = grade_bottom_up(DP, num_tasks, desired_points, point_vals, effort_hours)

#If the desired points was not possible to acheive with the tasks given return -1
if DP[num_tasks-1][desired_points-1] == float("inf"):
   print(-1)

#Otherwise print the value of the cell requested and the number of selected tasks
else:
    print(DP[num_tasks-1][desired_points-1])

        
