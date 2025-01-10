for i in range(3):
    file_input = input()
    if i == 0:
        first_line = file_input.split()
        num_tasks = int(first_line[0])+1
        desired_points = int(first_line[1])+1
    elif i == 1:
        point_vals = file_input.split()
    elif i == 2:
        effort_hours = file_input.split()
DP = [[0 for i in range(desired_points)] for j in range(num_tasks)]

def grade_bottom_up(DP, num_tasks, desired_points, point_vals, effort_hours): 
    DP[0][1:] = [float("inf")] * (desired_points -1)
    for i in range(1, num_tasks):
        for j in range(1, desired_points):
            if j >= int(point_vals[i-1]): 
                if DP[i-1][j] <= DP[i-1][max(0, j - int(point_vals[i-1]))] + int(effort_hours[i-1]):
                    DP[i][j] = (DP[i-1][j])
                else:
                    DP[i][j] = (DP[i-1][max(0, j - int(point_vals[i-1]))] + int(effort_hours[i-1]))             
            else:
                if DP[i-1][j] <= int(effort_hours[i-1]):
                    DP[i][j] = (DP[i-1][j])
                else:
                    DP[i][j] = (int(effort_hours[i-1]))
    return DP
    
DP = grade_bottom_up(DP, num_tasks, desired_points, point_vals, effort_hours)

if DP[num_tasks-1][desired_points-1] == float("inf"):
   print(-1)
else:
    print(DP[num_tasks-1][desired_points-1])

        
