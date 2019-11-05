from datetime import datetime
from matplotlib import pyplot, dates
from os import listdir
from os.path import isfile, join
import numpy as np

if __name__ == '__main__':
    path = 'resources/song-data/'
    files = [f for f in listdir(path) if isfile(join(path, f))]

    for file in files:
        fig, ax = pyplot.subplots(1, 1)
        path_file = path + file
        with open(path_file) as f:
            content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        content = [x.strip() for x in content]
        dates_lines = []
        for x in content:
            dates_lines.append(datetime.strptime(x, '%d %b %Y'))

        num_dates = dates.date2num(dates_lines)

        # ax.hist(num_dates, bins=100, color=np.random.rand(3,))

        counts, bin_edges = np.histogram(num_dates, 50)
        bin_centres = (bin_edges[:-1] + bin_edges[1:]) / 2.
        ax.plot(bin_centres, counts)

        ax.xaxis.set_major_locator(dates.YearLocator())
        ax.xaxis.set_major_formatter(dates.DateFormatter('%d.%m.%y'))
        ax.set(xlabel='date (d.m.y)',
               ylabel='play count',
               title=file[:-4])
    pyplot.show()
