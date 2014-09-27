
import sys, signal, time

running = True

def handler(signum = None, frame = None):
    global running
    print 'Signal handler called with signal', signum
    running = False

for sig in [signal.SIGTERM, signal.SIGINT, signal.SIGHUP, signal.SIGQUIT]:
    signal.signal(sig, handler)

while running:
    time.sleep(6)
print "done"

