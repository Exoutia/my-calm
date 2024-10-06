import time


def breath(inhale: int, exhale: int, hold: int | None = None):
    print("Inhale for ", inhale)
    time.sleep(inhale)
    if hold is not None:
        print("Hold for ", exhale)
        time.sleep(hold)
    print("now exhale for ", exhale)
    time.sleep(exhale)

def main():
    running = True
    print("Breathing exercise is starting, press 'ctrl+c' for exiting")
    while running:
        breath(4, 4)

        
    
    

if __name__ == "__main__":
    print("Take a deep breath")
    main()
