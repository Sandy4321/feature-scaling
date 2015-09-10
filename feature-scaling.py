# Python Script for calculating mean, median and standard deviation for a defined window to use in WEKA.
# Created by Bouke Regnerus September 9 2015

import csv
import statistics

window = 100

with open('example_data.csv', 'rb') as csvfile:
    dataset = csv.reader(csvfile)
    header = next(dataset, None);
    x = 1
    values = [[], [], [], [], [], [], [], [], [], []]
    results = []

    with open('output_data.csv', 'w') as fp:
        output = csv.writer(fp, delimiter=',')
        output.writerow(['Ax_MEAN', 'Ax_MEDIAN', 'Ax_STDEV', 'Ay_MEAN', 'Ay_MEDIAN', 'Ay_STDEV', 'Az_MEAN', 'Az_MEDIAN', 'Az_STDEV', 'Gx_MEAN', 'Gx_MEDIAN', 'Gx_STDEV', 'Gy_MEAN', 'Gy_MEDIAN', 'Gy_STDEV', 'Gz_MEAN', 'Gz_MEDIAN', 'Gz_STDEV', 'Mx_MEAN', 'Mx_MEDIAN', 'Mx_STDEV', 'My_MEAN', 'My_MEDIAN', 'My_STDEV', 'Mz_MEAN', 'Mz_MEDIAN', 'Mz_STDEV', 'Label'])

        for row in dataset:
            y = 0
            results = []

            for value in values:
                if y > 8:
                    results.append(row[y])
                    print(row[y])
                else:
                    values[y].append(float(row[y]))
                    if x > (window - 1):
                        # results.append({
                        #     'mean': statistics.mean(values[y]),
                        #     'median': statistics.median(values[y]),
                        #     'stdev': statistics.stdev(values[y])
                        # })
                        results.append(statistics.mean(values[y]))
                        results.append(statistics.median(values[y]))
                        results.append(statistics.stdev(values[y]))
                y += 1

            if x > (window - 1):
                output.writerow(results)
                values = [[], [], [], [], [], [], [], [], [], []]
                x = 1
            else:
                x += 1
