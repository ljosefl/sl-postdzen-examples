class Agent:
    def handle_email(self, email_data):
        raise NotImplementedError

class EmailAgent(Agent):
    def handle_email(self, email_data):
        print(f"Processing email: {email_data['subject']} from {email_data['sender']}")

class MeetingAgent(Agent):
    def schedule(self, meeting_data):
        print(f"Scheduling meeting with participants {meeting_data['participants']} at {meeting_data['time']}")