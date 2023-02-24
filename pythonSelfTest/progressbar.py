import time
import sys
import progressbar

def progress_bar(duration):
    widgets = [
        'Progress: ',
        progressbar.FormatLabel(''),
        ' ',
        progressbar.Bar(),
        ' ',
        progressbar.ETA()
    ]
    for i in progressbar.progressbar(range(duration), widgets=widgets):
        time.sleep(1)

if __name__ == "__main__":
    progress_bar(100)
