import speak_receive
import sys
import take_command


speak_receive.wishMe()
if __name__ == "__main__":
    while True:
        query = speak_receive.takeCommand().lower()
        take_command.queries(query)
sys.exit()