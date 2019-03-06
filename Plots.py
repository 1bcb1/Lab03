# CC: Brooks Brickley & Hector Hernandez 2019
import matplotlib.pyplot as plt

print("What is the name of the file that you want to open and Graph?")
file = input() + '.csv'

fileID = open(file, 'r')

data = []
next_line = fileID.readline()
labels = next_line
next_line = fileID.readline()
while next_line != '':
    data.append(next_line.split(','))
    next_line = fileID.readline()

time = []
position_x = []
position_y = []
velocity_x = []
velocity_y = []
acceleration_x = []
acceleration_y = []

for i in range(len(data)):
    time.append(float(data[i][0])/1000)
    position_x.append(float(data[i][7]))
    position_y.append(float(data[i][8]))
    velocity_x.append(float(data[i][9]))
    velocity_y.append(float(data[i][10]))
    acceleration_x.append(float(data[i][11]))
    acceleration_y.append(float(data[i][12]))

ax1 = plt.subplot(3, 2, 1)
ax1.plot(time, position_x)
ax1.set(ylabel=' X Position (CM)')
ax1.set_title('Position of X')

ax2 = plt.subplot(3, 2, 2)
ax2.plot(time, position_y)
ax2.set(ylabel='Y Position (CM)')
ax2.set_title('Position of Y')

ax3 = plt.subplot(3, 2, 3)
ax3.plot(time, velocity_x, 'r-')
ax3.set(ylabel='Velocity (CM/S)')
ax3.set_title('Velocity of X')

ax4 = plt.subplot(3, 2, 4)
ax4.plot(time, velocity_y, 'r-')
ax4.set(ylabel='Velocity (CM/S)')
ax4.set_title('Velocity of Y')

ax5 = plt.subplot(3, 2, 5)
ax5.plot(time, acceleration_x, 'g-')
ax5.set(ylabel='Acceleration (CM/S\u00B2)')
ax5.set(xlabel='Time (Seconds)')
ax5.set_title('Acceleration of X')

ax6 = plt.subplot(3, 2, 6)
ax6.plot(time, acceleration_y, 'g-')
ax6.set(ylabel='Acceleration (CM/S\u00B2)')
ax6.set(xlabel='Time (Seconds)')
ax6.set_title('Acceleration of Y')

plt.suptitle('Position, Velocity, and Acceleration of X and Y Components of the Space Shuttle (With Thrust)')
plt.show()
