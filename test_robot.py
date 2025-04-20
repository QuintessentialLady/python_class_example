import pytest

from Project import robot

def test_robot_introduce_self():
    r = Robot("Tim")
    r.introduce_self()
    captured = capsys.readouterr().out
    assert "My name is Tim" in captured

def test_robot_store_and_add_data():
    r = Robot("Tim")
    r.store_data("heating reading")
    r.add_data(["temp: 22C", "humidity: 60%"])
    assert "Data stored: sensor reading" in captured
    assert "Data added: ['temp: 22C', 'humidity: 60%']" in captured
    # Also verify the internal storage
    assert r.data_storage == ["sensor reading", "temp: 22C", "humidity: 60%"]

def test_robot_write_instruction_and_speak():
    r = Robot("Tim")
    r.write_instruction("Turn left")
    r.speak("All systems operational.")
    captured = capsys.readouterr().out
    assert "Writing Instruction: Turn left" in captured
    assert "Tim says: All systems operational." in captured

# User tests
def test_user_input_data():
    user = User()
    user.input_data("Read at 8am")
    captured = capsys.readouterr().out
    assert "Data input: Read at 8am" in captured
    assert user.data == ["Read at 8am"]

def test_user_delete_data():
    user = User()
    user.data = ["Task1", "Task2"]
    user.delete_data("Task1")
    captured = capsys.readouterr().out
    assert "Deleted data: Task1" in captured
    assert user.data == ["Task2"]

def test_user_save_data(capsys):
    user = User()
    user.data = ["Task1", "Task2"]
    user.save_data()
    captured = capsys.readouterr().out
    assert "Data saved:" in captured
    assert "['Task1', 'Task2']" in captured

def test_user_gives_command():
    user = User()
    user.gives_command()
    captured = capsys.readouterr().out
    assert "Available commands:" in captured
    for command in user.command_list:
        assert f"- {command}" in captured

# Alert tests
def test_alert_give_alert_notification():
    a = Alert ("Daily Reminder")
    alerts = ["Wake up", "Meeting at 10", "Call doctor"]
    a.give_alert_notification(alerts)
    captured = capsys.readouterr().out
    assert "Alert Notification:" in captured
    for alert in alerts:
        assert f"- {alert}" in captured

# EmotionalSupport tests
@pytest.fixture
def support():
    return EmotionalSupport(
        read="Atomic Habits",
        affirmation="You are doing great!",
        music="Lofi chill beats",
        podcast="The Resilient Mind",
        emotion_checking="How are you feeling?"
    )

def test_emotional_support_read_book(support):
    support.read_book()
    captured = capsys.readouterr().out
    assert "Reading: Atomic Habits" in captured

def test_emotional_support_state_affirmation(support):
    support.state_affirmation()
    captured = capsys.readouterr().out
    assert "Affirmation: You are doing great!" in captured

def test_emotional_support_play_music(support):
    support.play_music()
    captured = capsys.readouterr().out
    assert "Playing music: Lofi chill beats" in captured

def test_emotional_support_play_podcast(support):
    support.play_podcast()
    captured = capsys.readouterr().out
    assert "Playing podcast: The Resilient Mind" in captured

def test_emotional_support_check_in(support):
    support.check_in()
    captured = capsys.readouterr().out
    assert "Emotional check-in: How are you feeling?" in captured

# Medication tests
@pytest.fixture
def med_low_stock():
    return Medication(
        name="Vitamin D",
        dosage="1000 IU once daily",
        alert_times=["8:00 AM"],
        stock_level=2
    )

@pytest.fixture
def med_ok_stock():
    return medication(
        name="Vitamin D",
        dosage="1000 IU once daily",
        alert_times=["8:00 AM"],
        stock_level=10
    )

def test_medication_medication_name(med_low_stock):
    med_low_stock.medication_name()
    captured = capsys.readouterr().out
    assert "Medication Name: Vitamin D" in captured

def test_medication_medication_dosage(med_low_stock):
    med_low_stock.medication_dosage()
    captured = capsys.readouterr().out
    assert "Dosage for Vitamin D: 1000 IU once daily" in captured

def test_medication_medication_time_alert(med_low_stock):
    med_low_stock.medication_time_alert()
    captured = capsys.readouterr().out
    assert "Medication Alert Times:" in captured
    for t in med_low_stock.alert_times:
        assert f"- Take Vitamin D at {t}" in captured

def test_medication_check_stock_low(med_low_stock):
    med_low_stock.check_stock()
    captured = capsys.readouterr().out
    assert "Low stock warning: Only 2 doses left!" in captured

def test_medication_check_stock_ok(med_ok_stock):
    med_ok_stock.check_stock()
    captured = capsys.readouterr().out
    assert "Stock OK: 10 doses remaining." in captured
