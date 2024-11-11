class Actor:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def display_info(self):
        print(f"Actor: {self.name} - {self.description}")


class UseCase:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def display_info(self):
        print(f"Use Case: {self.name} - {self.description}")


def main():
    # Define actors
    actors = [
        Actor("Citizen", "Reports potholes, checks repair status, and submits damage claims."),
        Actor("PWD Staff", "Manages pothole records, assigns priorities, and creates work orders."),
        Actor("Repair Crew", "Updates work orders and logs repair details."),
        Actor("Administrator", "Oversees the system and manages user access.")
    ]

    # Define use cases
    use_cases = [
        UseCase("Report Pothole", "Citizen reports the location, severity, and details of a pothole."),
        UseCase("Check Repair Status", "Citizen checks the current status of a reported pothole."),
        UseCase("Submit Damage Claim", "Citizen submits a damage claim related to a pothole."),
        UseCase("View Pothole Reports", "PWD Staff views all reported potholes and their details."),
        UseCase("Assign Repair Priority", "PWD Staff assigns repair priorities based on severity."),
        UseCase("Generate Work Order", "PWD Staff creates work orders for pothole repairs."),
        UseCase("Update Repair Status", "Repair Crew logs the repair status of assigned potholes."),
        UseCase("Log Repair Details", "Repair Crew enters repair details like materials used and costs."),
        UseCase("Manage System", "Administrator manages user roles and system permissions.")
    ]

    # Print out actors and use cases
    print("Pothole Tracking and Repair System (PHTRS) - UML Use Case Diagram\n")
    print("Actors:")
    for actor in actors:
        actor.display_info()
    print("\nUse Cases:")
    for use_case in use_cases:
        use_case.display_info()

    # Brief description of the diagram
    print("\nDiagram Description:")
    print("The PHTRS Use Case Diagram represents interactions between different actors and the system. "
          "Citizens can report potholes, check repair status, and submit damage claims. "
          "PWD Staff manage pothole records, assign priorities, and generate work orders. "
          "Repair Crews update repair statuses and log repair details, while the Administrator oversees system access "
          "and user roles. Each use case represents a core interaction that facilitates pothole tracking, repair "
          "management, and damage reporting.")


if __name__ == "__main__":
    main()
