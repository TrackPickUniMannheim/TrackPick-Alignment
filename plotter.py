import matplotlib.pyplot as plt
import data
import json

plt.style.use('ggplot')
evil_global_var = 0
config = json.load(open('config.json'))


def on_pick(event):
    """
    Method that is called when the user clicks on a point within the plot.
    This is used to find the timestamp of the visually selected end of alignment
    :param event:
    :return:
    """
    artist = event.artist
    xmouse, ymouse = event.mouseevent.xdata, event.mouseevent.ydata
    x, y = artist.get_xdata(), artist.get_ydata()
    ind = event.ind
    print('{} vertices picked'.format(len(ind)))
    print('Data point:', x[ind[0]], y[ind[0]])
    print("")
    global evil_global_var
    evil_global_var = x[ind[0]]


def plot_data(data, synctime=None, upper_bound=None, guess=None):
    """
    Plots the passed data (should be gyration).
    :param data: Gyration data
    :param synctime: Time
    :param upper_bound: Can be used to cut of part of the plot (if it is too long for instance)
    :param guess: Guess for a rough offset of time difference
    :return:
    """
    fig, ax = plt.subplots()
    id, time, x, y, z = zip(*data)

    if upper_bound:
        idx = 0
        for i in range(len(time)):
            if time[i] > upper_bound:
                idx = i
                break
        time = time[:idx]
        x = x[:idx]
        y = y[:idx]
        z = z[:idx]

    ax.plot(time, x, picker=5)
    ax.plot(time, y, picker=5)
    ax.plot(time, z, picker=5)

    if synctime:
        ax.axvspan(synctime, synctime + 1000, alpha=0.5, color='red')

    if guess:
        ax.axvspan(guess - 1500, guess + 1500, alpha=0.4, color='red')

    fig.canvas.mpl_connect('pick_event', on_pick)

    plt.show()


def plot_combine(rec, offset, synctime=0, title='Not given'):
    """
    This method is used to validate the offset visually. It overlays the time of the video alignment
    on the gyration plot of the watch.
    :param rec: Recording dictionary
    :param offset: Calculated offset
    :param synctime: Time at which the alignment motion occured
    :param title:
    :return: -
    """
    fig, ax = plt.subplots()
    ax = [ax]
    gyro_glass = data.get_data(config['glass']['gyro'], rec['glasses_db'])
    gyro_watch = data.get_data(config['watch']['gyro'], rec['phone_db'])
    id_glass, time_glass, x_glass, y_glass, z_glass = zip(*gyro_glass)
    id_watch, time_watch, x_watch, y_watch, z_watch = zip(*gyro_watch)
    time_watch = list(map(lambda t: t+offset, time_watch))

    plt.title(title)
    """
    ax[0].plot(time_glass, x_glass)
    ax[0].plot(time_glass, y_glass)
    ax[0].plot(time_glass, z_glass)
    """

    ax[0].plot(time_watch, x_watch)
    ax[0].plot(time_watch, y_watch)
    ax[0].plot(time_watch, z_watch)
    ax[0].patch.set_color('none')

    ax[0].axvspan(synctime, synctime + 1000, alpha=0.5, color='red')
    """
    accel1 = data.get_data(config['glass']['accel'], rec['glasses_db'])
    accel2 = data.get_data(config['phone']['accel'], rec['phone_db'])
    i, t, xx,yy,zz = zip(*accel1)
    i2, t2, xx2, yy2, zz2 = zip(*accel2)
    t2 = list(map(lambda t: t + offset, t2))

    ax[1].plot(t, xx)
    ax[1].plot(t, yy)
    ax[1].plot(t, zz)

    ax[1].plot(t2, xx2)
    ax[1].plot(t2, yy2)
    ax[1].plot(t2, zz2)

    ax[1].axvspan(synctime, synctime + 1000, alpha=0.5, color='red')
    """
    plt.show()


