n = 3

process = [1,2,3]
arrival = [0,6,2]
burst = [1,10,1]

for x in range(0,n):
    for y in range(0,n-x-1):
        if arrival[y] > arrival[y+1]:
            arrival[y], arrival[y+1] = arrival[y+1], arrival[y]
            burst[y], burst[y+1] = burst[y+1], burst[y]
            process[y], process[y+1] = process[y+1], process[y]

# print(f"""
# {'Process':<10}{'Arrival':<10}{'Burst':<10}
# """)
# for x in range(0,n):
#     print(f"{process[x]:<10}{arrival[x]:<10}{burst[x]:<10}")

waiting = [0]*n
turnaround = [0]*n
service_time = [0] * n


waiting[0] = 0
turnaround[0] = burst[0]
service_time[0] = arrival[0] + burst[0]

for x in range(1,n):
    if service_time[x-1] > arrival[x]:
        service_time[x] = service_time[x-1] + burst[x]
    else:
        service_time[x] = arrival[x] + burst[x]
    turnaround[x] = service_time[x] - arrival[x]
    waiting[x] = turnaround[x] - burst[x]

avg_waiting = sum(waiting)/n
avg_turnaround = sum(turnaround)/n

print(f"""
{'Process':<10}{'Arrival':<10}{'Burst':<10}{'Waiting':<10}{'Turnaround':<10}{'Service':<10}
""")

for x in range(0,n):
    print(f"{process[x]:<10}{arrival[x]:<10}{burst[x]:<10}{waiting[x]:<10}{turnaround[x]:<10}{service_time[x]:<10}")


print(avg_waiting)
print(avg_turnaround)