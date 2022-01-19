from datetime import datetime
from datetime import date
from datetime import timedelta

def start_time():
    current_time = datetime.now()
    return current_time

def end_time():
    end_time = datetime.now()
    return end_time

def ellapsed_time(end, start):
    ellapsed = end - start
    return ellapsed


def main():
    try:
        start_key = input("press any key to start the stopwatch: ")
        start = start_time()

        end_key = input("press any key to end the stopwatch: ")
        end = end_time()

        stop = ellapsed_time(end, start)
        minutes = int(stop.seconds / 60)
        seconds = stop.seconds % 60

        print(f'The amount of time that passed in minutes:seconds is {minutes:02.0f}:{seconds:02.0f}')
    except KeyboardInterrupt as k:
        print("Stopwatch terminated early due to keyboard interrupt. Please rerun the program")


if __name__ == "__main__":
    main()
