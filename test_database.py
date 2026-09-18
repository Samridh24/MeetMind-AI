
from database_service import (
    initialize_database,
    save_meeting,
    get_all_meetings,
    get_meeting
)


# Initialize database
initialize_database()

print("Database initialized successfully!")


# Add sample meetings
meeting_id_1 = save_meeting(
    "Team Standup",
    "Team discussed project progress and assigned tasks."
)

meeting_id_2 = save_meeting(
    "Project Discussion",
    "Discussion about project development and deadlines."
)

print("Saved Meeting ID:", meeting_id_1)
print("Saved Meeting ID:", meeting_id_2)


# Fetch all meetings
meetings = get_all_meetings()

print("\nAll Meetings:")

for meeting in meetings:
    print(
        meeting["id"],
        meeting["meeting_name"],
        meeting["created_at"]
    )


# Fetch one meeting
meeting = get_meeting(meeting_id_1)

print("\nSelected Meeting:")

if meeting:
    print("ID:", meeting["id"])
    print("Name:", meeting["meeting_name"])
    print("Report:", meeting["report"])