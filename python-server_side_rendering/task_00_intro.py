import os

def generate_invitations(template, attendees):
    """
    Generates personalized invitation files by replacing placeholders in the template.

    :param template: (str) The text template containing placeholders.
    :param attendees: (list) A list of dictionaries with attendee information.
    """
    
    # Check if `template` is a string
    if not isinstance(template, str):
        print("Error: The template must be a string.")
        return
    
    # Check if `attendees` is a list of dictionaries
    if not isinstance(attendees, list) or not all(isinstance(person, dict) for person in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Check if the template is empty
    if template.strip() == "":
        print("Error: The template is empty, no output files generated.")
        return

    # Check if the attendees list is empty
    if len(attendees) == 0:
        print("Error: No attendees, no output files generated.")
        return

    # Process each attendee and generate an invitation file
    for index, person in enumerate(attendees, start=1):
        # Replace placeholders in the template, using "N/A" for missing values
        invitation_text = template.format(
            name=person.get("name", "N/A"),
            event_title=person.get("event_title", "N/A"),
            event_date=person.get("event_date", "N/A"),
            event_location=person.get("event_location", "N/A")
        )

        # Generate a file named `output_X.txt`
        filename = f"output_{index}.txt"
        with open(filename, "w") as file:
            file.write(invitation_text)

        print(f"File {filename} successfully generated.")

    print("All invitations have been successfully generated!")
