import os
import pyinotify

wm = pyinotify.WatchManager()  # Watch Manager
mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE | pyinotify.IN_CLOSE_WRITE  # watched events

class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        print "Creating:", event.pathname

    def process_IN_DELETE(self, event):
        print "Removing:", event.pathname

    def process_IN_CLOSE_WRITE(self, event):
        filename = event.pathname.split('/')[-1]
        if "command" in filename:
            print "command"
        if "schedule" in filename:
            print "schedule"
        print "Modifying:", event.pathname

notifier = pyinotify.ThreadedNotifier(wm, EventHandler())
notifier.start()

cwd = os.getcwd()
wdd = wm.add_watch(cwd, mask)
