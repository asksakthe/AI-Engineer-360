class batsman:
    def __init__(self, profile):
        self.profile = dict(profile)

    def add_batsman(self, name, team, matches, runs, average):
        self.name = name
        self.team = team
        self.matches = matches
        self.runs = runs
        self.average = float(average)
        if self.name not in self.profile:
            self.profile[self.name] = {'Team': self.team, 'matches': self.matches, 'Runs': self.runs, 'Average': self.average}
            return f"Batsman {self.name} added successfully"
        else:
            return "Batsman already exists"

    def update_runs(self, name, new_runs, new_average):
        self.name = name
        self.new_runs = new_runs
        self.new_average = float(new_average)
        if self.name in self.profile:
            self.profile[self.name]['Runs'] = self.new_runs
            self.profile[self.name]['Average'] = self.new_average
            return f"{self.profile[self.name]} are updated"
        else:
            return "BAtsman not found"

    def list_all_profiles(self):
        return f"{self.profile}"


if __name__ == "__main__":
    print("Batsman Profile")
    print("------------------")
    batsman_profile = batsman({})
    print(batsman_profile.add_batsman("Virat Kohli", "India", 254, 12169, 59.07))
    print(batsman_profile.add_batsman("Steve Smith", "Australia", 128   , 4378, 43.34))
    print(batsman_profile.update_runs("Virat Kohli", 12300, 60.5))
    print(batsman_profile.list_all_profiles())