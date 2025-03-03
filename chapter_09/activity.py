class Team:

    def __init__(self, team_name, members=[]):
        self.name = team_name
        self.members = members 

    def addMember(self, member):
        self.members.append(member)

    def removeMember(self, member):
        if member in self.members:
            self.members.remove(member)
        else:
            print(f"{member} is not a member of {self.name}")

    def displayInfo(self):
        print(f"Team: {self.name}")

        if self.members:
            print("Members", ", ".join(self.members))
        else:
            print("There are no members in this team.")

team = Team("Function Junction", ["Aidan", "Mieke", "Cadee", "Sibu", "Asanda"])

# Display initial team info
team.displyInfo()

# Adding a new member
team.addMember("Jordan")
team.displyInfo()

# Removing a member
team.removeMember("Cadee")
team.displyInfo()

# Trying to remove a member who is not in the team
team.removeMember("Alex")

# Getting the current list of members
print(team.members)  # Output: ['Aidan', 'Mieke', 'Sibu', 'Asanda', 'Jordan']