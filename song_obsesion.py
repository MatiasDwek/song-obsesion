from datetime import datetime
from matplotlib import pyplot, dates

if __name__ == '__main__':
    filename = 'resources/song-data/high_to_death.txt'
    with open(filename) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    dates_lines = []
    for x in content:
        dates_lines.append(datetime.strptime(x, '%d %b %Y'))

    num_dates = dates.date2num(dates_lines)

    fig, ax = pyplot.subplots(1, 1)
    ax.hist(num_dates, bins=50, color='lightblue')
    ax.xaxis.set_major_locator(dates.YearLocator())
    ax.xaxis.set_major_formatter(dates.DateFormatter('%d.%m.%y'))
    pyplot.show()
