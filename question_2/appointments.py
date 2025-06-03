doctors = {
    "Dr. Smith": ["09:00", "10:00", "11:00"],
    "Dr. Adams": ["10:00", "13:00", "14:00"]
}
appointments = []
def book_appointment(patient_name, preferred_doctor, preferred_time):
    if preferred_time in doctors.get(preferred_doctor, []):
        appointment = {
            "patient": patient_name,
            "doctor": preferred_doctor,
            "time": preferred_time,
            "reminder_time": (datetime.strptime(preferred_time, "%H:%M") - timedelta(minutes=30)).strftime("%H:%M")
        }
        appointments.append(appointment)
        doctors[preferred_doctor].remove(preferred_time)
        print(f"Appointment booked for {patient_name} with {preferred_doctor} at {preferred_time}")
    else:
        print("Requested time not available. Please choose a different slot.")
def send_reminders():
    for appt in appointments:
        print(f"Reminder: {appt['patient']}, your appointment with {appt['doctor']} is at {appt['time']}")