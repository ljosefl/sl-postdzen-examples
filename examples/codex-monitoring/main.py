import win32evtlog
import win32evtlogutil
import pywintypes

def get_diagnostic_events():
    server = 'localhost'
    logtype = 'DiagTrack'
    hand = win32evtlog.OpenEventLog(server, logtype)
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
    events = win32evtlog.ReadEventLog(hand, flags, 0)
    while events:
        for event in events:
            if 'codex.exe' in event.StringInserts:
                print(f"Event ID: {event.EventID}, Time Generated: {event.TimeGenerated}, String Inserts: {event.StringInserts}")
        events = win32evtlog.ReadEventLog(hand, flags, 0)
    win32evtlog.CloseEventLog(hand)

if __name__ == "__main__":
    try:
        get_diagnostic_events()
    except pywintypes.error as e:
        print(f"An error occurred: {e}")