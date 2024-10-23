
class InterAgentCommunication:
    def __init__(self):
        self.communication_log = []

    def send_message(self, sender_id, recipient_id, message):
        log_entry = {
            "from": sender_id,
            "to": recipient_id,
            "message": message
        }
        self.communication_log.append(log_entry)
        return f"Message from Agent {sender_id} to Agent {recipient_id}: {message}"

    def get_communication_log(self):
        return self.communication_log

# Example Usage
if __name__ == "__main__":
    communication = InterAgentCommunication()
    communication.send_message(1, 2, "Please share your results.")
    print(communication.get_communication_log())
