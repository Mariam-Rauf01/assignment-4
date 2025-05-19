import time

def countdown_timer(seconds):
    """Function to create a countdown timer."""
    while seconds:
        mins, secs = divmod(seconds, 60)  # Convert seconds to minutes and seconds
        timer = '{:02d}:{:02d}'.format(mins, secs)  # Format MM:SS
        print(f"⏳ Time Left: {timer}", end='\r')  # Display timer on the same line
        time.sleep(1)
        seconds -= 1

    print("\n⏰ Time's up!")  # Message when countdown ends

def main():
    print("⏱️ Welcome to the Countdown Timer!")
    try:
        total_seconds = int(input("Enter the time in seconds: "))
        print(f"Starting countdown for {total_seconds} seconds...\n")
        countdown_timer(total_seconds)
    except ValueError:
        print("❌ Please enter a valid integer.")

if __name__ == "__main__":
    main()
