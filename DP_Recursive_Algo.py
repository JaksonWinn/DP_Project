#Recursive function to find the minimum number of effoert hours for the desired number of points and the number tasks
def grade(num_tasks, desired_points, point_val,  effort_hours, i):

    #Base case for if the desired points greater than 1 and the number of tasks is 0
    if num_tasks == 0 and desired_points > 0:
        return float('inf')
    
    #Base case for if the desired points is 0
    if desired_points == 0 :
        return  0
    
    #If the desired points is greater than the number of points for the current task find the minimum of discarding
    #the task and selecting the task and continuing
    if desired_points >= int(point_val[i]):
        return min(grade(num_tasks - 1, desired_points - int(point_val[i]), point_val, effort_hours, i + 1) + int(effort_hours[i]), 
                   grade(num_tasks - 1, desired_points, point_val, effort_hours, i + 1))
    
    #return the minimum of discarding the task and selecting and ending the task
    else:
        return min(int(effort_hours[i]), grade(num_tasks - 1, desired_points, point_val, effort_hours, i + 1))

#Assign variables to respected values
for i in range(0, 2):
    file_path = input()

    # Read in the input file from command line
    if i == 0:
        first_line = file_path.split()
        num_tasks = int(first_line[0])
        desired_points = int(first_line[1])
    if i == 1:
        point_val = input.readline().split()[::-1]
    if i == 2:
        effort_hours = input.readline().split()[::-1]

#Find the result 
result = grade(num_tasks, desired_points, point_val, effort_hours, 0)

#If the result is not possible then return -1
if result == float('inf'):
    result = -1

#Otherwsie print the result
else:
    print(result)