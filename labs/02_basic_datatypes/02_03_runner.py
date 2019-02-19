'''

If a runner runs 10 miles in 30 minites and 30 seconds,
What is his/her average speed in kilometers per hour? (Tip: 1 mile = 1.6 km)

'''

speedkm = 10 * 1.6
time = 30 * 60 + 30
speedperhour = speedkm * (time / 60 / 60)

print(speedperhour)