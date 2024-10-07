import time

import progressbar


def create_progressbar(duration: int):
    with progressbar.ProgressBar(max_value=100*duration) as bar:
        for i in range(duration * 100):
            time.sleep(0.01)
            bar.update(i)

def breath(inhale: int, exhale: int, hold: int | None = None):
    print("Inhale for ", inhale, "sec")
    create_progressbar(inhale)
    if hold is not None:
        print("Hold for ", hold, "sec")
        create_progressbar(hold)
    print("now exhale for ", exhale, "sec")
    create_progressbar(exhale)

def main():
    running = True
    print("Breathing exercise is starting, press 'ctrl+c' for exiting")
    while running:
        breath(4, 4)

        
    
    

if __name__ == "__main__":
    print("Take a deep breath")
    main()
