def grade(num_tasks, desired_points, point_val,  effort_hours, i):
    if num_tasks == 0 and desired_points > 0:
        return float('inf')
    if desired_points == 0 :
        return  0
    if desired_points >= int(point_val[i]):
        return min(grade(num_tasks - 1, desired_points - int(point_val[i]), point_val, effort_hours, i + 1) + int(effort_hours[i]), 
                   grade(num_tasks - 1, desired_points, point_val, effort_hours, i + 1))
    else:
        return min(int(effort_hours[i]), grade(num_tasks - 1, desired_points, point_val, effort_hours, i + 1))

file_path = input()
for i in range(0, 2):
    if i == 0:
        first_line = file_path.split()
        num_tasks = int(first_line[0])
        desired_points = int(first_line[1])
    if i == 1:
        point_val = input.readline().split()[::-1]
    if i == 2:
        effort_hours = input.readline().split()[::-1]

result = grade(num_tasks, desired_points, point_val, effort_hours, 0)

if result == float('inf'):
    result = -1

print(result)