from datetime import datetime

now= datetime.now()

hour= now.hour

if hour >= 5 and hour < 12:
    print("Good Morning! time to go study📚")
elif hour >= 12 and hour < 17:
    print("Good Afternoon! Stay productive💻")
elif hour >= 17 and hour < 21:
    print("Good Evening! Time to relax 🏖️")
else:
    print("Good Night! Time to sleep 😴")