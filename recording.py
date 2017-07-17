import os
import datetime as dt
import constants as con


def get_recording(path):
    """
    :param path: Path to single recording session
    :return: Dictionary containing all needed information for the alignment
    """
    result = dict()
    result['path'] = path
    result['id'] = path.split('/')[-1]
    result['glasses_db'] = path + '/' + con.GLASS_DB_NAME
    result['phone_db'] = path + '/' + con.PHONE_DB_NAME

    # Sample: vid_20170118_144959.mp4
    vid = list(filter(lambda x: x.startswith('vid'), os.listdir(path)))[0]
    year = int(vid[4:8])
    month = int(vid[8:10])
    day = int(vid[10:12])
    hours = int(vid[13:15])
    minutes = int(vid[15:17])
    seconds = int(vid[17:19])

    date = dt.datetime(year, month, day, hours, minutes, seconds)
    result['video_start'] = date.timestamp() * 1e3 # Convert to proper unix timestamp
    return result


def get_offset(path):
    """
    :param path: Path to CSV export of Boris Labels
    :return: The time in milliseconds when the alignment actions occured
    """
    line_found = None
    result = None
    with open(path, 'r') as f:
        for line in f:
            if con.ALGINMENT_LBL in line:
                line_found = line
        if line_found:
            result = float(line_found.split(',')[0]) * 1000
    return result


def get_recordings_for_participant(path):
    folders = filter(lambda x: os.path.isdir(path+'/'+x), os.listdir(path))
    result = []
    for folder in folders:
        result.append(get_recording(path+'/'+folder))
    return result