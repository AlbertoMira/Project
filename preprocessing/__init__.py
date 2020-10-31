from scipy.fft import fft
from scipy.signal import blackman

import pickle


__version__ = '0.0.1'

# Number of columns which are meta-data
META_COLS = 2
DELIMITER = ';'


def fft_vector(vector):
    """
    Perform the fft of the given data. Expects a single line vector

    see https://docs.scipy.org/doc/scipy/reference/tutorial/fft.html
    """
    window = blackman(len(vector))
    return fft(vector*window)


def pickle_data(data, f_out):
    """
    Store the data using Pickle.
    """
    with f_out:
        pickle.dump(data, f_out)


def process(f_in, f_out):
    """
    - Read the measurements coming from the .txt files.
    - Store the data you process.
    - Process several movements.

    """
    with f_in:
        # Assume data-structure where the first three lines are metadata
        movement = f_in.readline().split(DELIMITER)[1]
        timestamp = f_in.readline().split(DELIMITER)[1]
        num_sensors = int(f_in.readline().split(DELIMITER)[1])

        # Read all the lines of data
        data = f_in.readlines()
        # Init container for sensor data only - one list per sensor
        sensor_data = [[] for _ in range(num_sensors)]

        # Fill container
        for line in data:
            # Remove trailing whitespace; split into chunks
            line = line.strip().split(DELIMITER)
            # Put only the relevant chunks into the sensor data array
            line = line[META_COLS:(META_COLS+num_sensors)]
            i = 0
            for chunk in line:
                sensor_data[i].append(chunk)
                i += 1

        # Perform FFT on the data
        # fft_data = []
        # for sensor in sensor_data:
        #    fft_data.append(fft_vector(sensor))

        pickle_data(sensor_data, f_out)
    exit(0)
