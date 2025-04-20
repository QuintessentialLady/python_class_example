class Robot:
    def __init__(self, name):
        self.name = name
        self.data_storage = []  # Used for storing data
        self.instruction_list = []  # Placeholder if needed
        self.instruction_file = None  # Placeholder if needed

    def write_instruction(self, instruction):
        print(f"Writing Instruction: {instruction}")
        self.instruction_list.append(instruction)

    def store_data(self, data):
        self.data_storage.append(data)
        print(f"Data stored: {data}")

    def add_data(self, new_data):
        self.data_storage += new_data if isinstance(new_data, list) else [new_data]
        print(f"Data added: {new_data}")

    def speak(self, message):
        print(f"{self.name} says: {message}")

def process_command(self, command):
    command = command.lower()

    if "introduce" in command:
        self.speak(f"My name is {self.name}")
    elif "store" in command:
        self.store_data("Example input from text")
    elif "add data" in command:
        self.add_data(["text-based entry"])
    elif "write instruction" in command:
        self.write_instruction("Follow the white line")
    elif "exit" in command or "goodbye" in command:
        self.speak("Goodbye!")
    else:
        self.speak("I don't recognize that command.")


class User:
    def __init__(self, data_input=None, command=None):
        self.command_list = [
            "breakfast", 
            "play_podcast", 
            "read_book", 
            "play_music", 
            "read_daily_affirmation"
        ]
        self.data = data_input if data_input is not None else []
        self.command = command

    def input_data(self, new_data):
        self.data.append(new_data)
        print(f"Data input: {new_data}")

    def delete_data(self, target_data):
        if target_data in self.data:
            self.data.remove(target_data)
            print(f"Data deleted: {target_data}")
        else:
            print(f"{target_data} not found in data.")

    def save_data(self):
        # Placeholder for actual save logic (e.g., to file/database)
        print("Data saved:", self.data)

    def gives_command(self):
        print("Available commands:")
        for element in self.command_list:
            print(f"- {element}")



class Alert:
    def __init__(self, alert_notifications=None):
        self.notifications = alert_notifications if alert_notifications is not None else []

    def give_alert_notification(self):
        print("Alert notifications:")
        for alert in self.notifications:
            print(f"- {alert}")

    def input_notification(self, new_notification):
        self.notifications.append(new_notification)
        print(f"Added: {new_notification}")

    def delete_notification(self, delete_notification):
        if delete_notification in self.notifications:
            self.notifications.remove(delete_notification)
            print(f"Deleted: {delete_notification}")
        else:
            print(f"{delete_notification} not found.")



class EmotionalSupport:
    # Provides support such as reading, affirmations, music, podcasts, and emotion check-ins
    def __init__(self, read, affirmation, music, podcast, emotion_checking):
        self.read = read
        self.affirmation = affirmation
        self.music = music
        self.podcast = podcast
        self.emotion_checking = emotion_checking

    def read_book(self):
        print(f"Reading: {self.read}")

    def state_affirmation(self):
        print(f"Affirmation: {self.affirmation}")

    def play_music(self):
        print(f"Playing music: {self.music}")

    def play_podcast(self):
        print(f"Playing podcast: {self.podcast}")

    def check_in(self):
        print(f"Emotional check-in: {self.emotion_checking}")

support = EmotionalSupport(
    read="Atomic Habits by James Clear",
    affirmation="You are capable of amazing things.",
    music="Wizkid Badgril",
    podcast="The Resilient Mind",
    emotion_checking="How are you feeling today?"
)

support.read_book()
support.state_affirmation()
support.play_music()
support.play_podcast()
support.check_in()

Reading: Atomic_Habits by James Clear, 
Affirmation: You are capable of amazing things., 
Playing music: Wizkid Badgril,
Playing podcast: The Resilient Mind,
Emotional check-in: How are you feeling today?


class Medication:
    # Indicates medication time, name, dosage, and gives low stock reminders
    def __init__(self, name, dosage, alert_times, stock_level):
        self.name = name
        self.dosage = dosage
        self.alert_times = alert_times  # List of times to take medication
        self.stock_level = stock_level  # Number of doses left

    def medication_name(self):
        print(f"Medication Name: {self.name}")

    def medication_dosage(self):
        print(f"Dosage for {self.name}: {self.dosage}")

    def medication_time_alert(self):
        print("Medication Alert Times:")
        for time in self.alert_times:
            print(f"- Take {self.name} at {time}")

    def check_stock(self):
        if self.stock_level < 5:
            print(f"Low stock warning: Only {self.stock_level} doses of {self.name} left!")
        else:
            print(f"Stock is sufficient: {self.stock_level} doses remaining.")
