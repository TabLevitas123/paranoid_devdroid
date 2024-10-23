
class CommunicationProtocol:
    def __init__(self):
        self.message_log = []

    def send_message(self, sender, receiver, message):
        # Send a message from one agent to another
        log_entry = f"{sender} -> {receiver}: {message}"
        self.message_log.append(log_entry)
        print(log_entry)

    def display_message_log(self):
        # Display all messages that have been sent
        print("Message Log:")
        for message in self.message_log:
            print(message)

# Example usage
if __name__ == "__main__":
    protocol = CommunicationProtocol()
    
    # Simulating agents sending messages
    protocol.send_message("Roastmaster", "Marvin", "Your decision is terrible.")
    protocol.send_message("Hallucination Monitor", "Marvin", "Potential hallucination detected.")
    
    protocol.display_message_log()
