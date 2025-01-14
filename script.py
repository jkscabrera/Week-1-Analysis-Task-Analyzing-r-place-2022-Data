import datetime
from datetime import datetime
from time import perf_counter_ns
from collections import Counter
import csv

# get most placed color and pixel coord
def colorpixel():
    while True:
        try:
            # get start and end hours
            start_hour = input("Choose a start time using a YYYY-MM-DD HH format.")
            end_hour = input("Choose an end time using a YYYY-MM-DD HH format.")

            start = datetime.strptime(start_hour, "%Y-%m-%d %H")
            end = datetime.strptime(end_hour, "%Y-%m-%d %H")
            
            # checking end hour is after start hour
            if end > start:

                # keep track of unique colors and pixel coords
                color = Counter()
                pixel = Counter()

                # record start time 
                start_time = perf_counter_ns()

                # get data
                with open('2022_place_canvas_history.csv') as file_obj: 
                    reader_obj = csv.reader(file_obj)

                    # remove heading
                    next(file_obj) 

                    for row in reader_obj: 
                        # get time in row
                        curr_time = row[0]

                        try:
                            time = datetime.strptime(curr_time, 
                                                     "%Y-%m-%d %H:%M:%S.%f %Z")
                            
                            # check row time is in between start and end hour
                            if start <= time and time <= end:
                                # hex code
                                colorhex = row[2]
                                
                                # update unique color counter
                                color[colorhex] = color[colorhex] + 1

                                # pixel location
                                pixelloc = row[3]

                                # update unique pixel location counter
                                pixel[pixelloc] = pixel[pixelloc] + 1

                        except ValueError:
                            pass

                # record end time
                end_time = perf_counter_ns()

                # get execution time
                execution_time = (end_time - start_time) / 1000000

                return color.most_common(1), pixel.most_common(1), execution_time


            else:
                print("End Hour is not after Start Hour")

        except ValueError:
            print("Invalid Format")

def main():
    color, pixel, executiontime = colorpixel()
    print(color, pixel, executiontime)

if __name__ == "__main__":
    main()