from datetime import datetime

now= datetime.now()
day= now.strftime("%A")

if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    print("It's a weekday! Time to work or study📚")
else:
    print("It's the weekend! Time to relax and have fun! 🎉")

#     📌 Common Format Codes

# Code Meaning Example

# %A Full day name Monday

# %a Short day Mon

# %B Full month April

# %b Short month Apr

# %d Day 30

# %m Month (number) 04

# %Y Year 2026

# %H Hour (24 hr) 14

# %I Hour (12 hr) 02

# %M Minutes 35

# %S Seconds 20

# %p AM/PM PM