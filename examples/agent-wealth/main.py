import requests
from agent import EmailAgent, MeetingAgent

class AgentManager:
    def __init__(self):
        self.email_agent = EmailAgent()
        self.meeting_agent = MeetingAgent()

    def process_email(self, email_data):
        self.email_agent.handle_email(email_data)

    def schedule_meeting(self, meeting_data):
        self.meeting_agent.schedule(meeting_data)

if __name__ == "__main__":
    manager = AgentManager()

    # Пример обработки электронной почты
    email_data = {
        "subject": "Meeting Request",
        "body": "Can we meet tomorrow at 10 AM?",
        "sender": "john.doe@example.com"
    }
    manager.process_email(email_data)

    # Пример планирования встречи
    meeting_data = {
        "participants": ["john.doe@example.com", "jane.doe@example.com"],
        "time": "2023-10-15T10:00:00Z"
    }
    manager.schedule_meeting(meeting_data)