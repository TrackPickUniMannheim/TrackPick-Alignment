import data
import json
#import plotter
import recording
import constants as con
import matplotlib.pyplot as plt

config = json.load(open('config.json'))

'''
def get_offset(path, align_time):
    """
    :param path: Path to a specific recording session
    :param align_time: Time in milliseconds when the alignment motion starts from the beginning of the egocentric video (boris csv file)
    :return: Time difference between the glass and the smartphone
    """
    instance = recording.get_recording(path)
    plotter.plot_data(data.get_data(config['glass']['gyro'], instance['glasses_db']),
                      instance['video_start'] + align_time)
    end_align = plotter.evil_global_var
    plotter.plot_data(data.get_data(config['watch']['gyro'], instance['phone_db']), None, None,
                      instance['video_start'] + align_time + con.DIFFERENCE_GUESS)
    watch_align = plotter.evil_global_var

    return end_align - watch_align
'''
# Implement your logic here
start = 1498489091317
end = 1498489099134

path = 'F:\\Course\\Team Project\\Smart Glass Data\\Niranjan\\Scenario1_Negative\\db1498489359202.sqlite'

accel = data.get_data('SDC_62c7c4a8aa33b123SensorGyroscopeData', path)
print(accel)

plot_x = [i[2] for i in accel if i[1] > start-2000 and i[1] < end+2000]
plot_y = [i[3] for i in accel if i[1] > start-2000 and i[1] < end+2000]
plot_z = [i[4] for i in accel if i[1] > start-2000 and i[1] < end+2000]

dummy =  [i[1] for i in accel if i[1] > start-2000 and i[1] < end+2000]

fig, ax = plt.subplots()

ax.plot(dummy, plot_x)
ax.plot(dummy, plot_y)
ax.plot(dummy, plot_z)

ax.axvspan(start, end,  alpha=0.4, color='red')
plt.show()

'''
paths = ['path1', 'path2']
result = {}
for i in paths:
    result[i] = get_offset(i, recording.get_offset(i + '/boris.csv'))
'''