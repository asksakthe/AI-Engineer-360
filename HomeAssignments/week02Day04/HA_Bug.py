class BugTracker:
    
    def __init__(self,bugs):
        self.bugs = dict(bugs)
        
       
    def add_bug(self,bug_ID, description, severity, status = 'Open'):
        self.bug_ID = bug_ID
        self.description = description
        self.severity = severity
        self.status = status
        self.bugs[self.bug_ID] = {'Description': self.description, 'Severity': self.severity, 'Status': self.status}
        return f"Bug ID {self.bug_ID} added successfully"
    
    def update_status(self, bug_ID, new_status):
        self.bug_ID = bug_ID
        self.new_status = new_status
        if self.new_status != self.status:
            self.bugs[self.bug_ID]['status'] = self.new_status
            return f"{self.bugs[self.bug_ID]} are updated as {self.new_status}"
        else:
            return "Bug is not Found"
        
        def list_all_bugs(self):
            print(f"{self.bugs}")
        

if __name__ == "__main__":
    print("Bug Tracker System")
    print("------------------")
    bug_tracker = BugTracker({})
    print(bug_tracker.add_bug(101, "Login button not working", "High"))
    print(bug_tracker.add_bug(102, "Page not loading", "Medium"))
    print(bug_tracker.update_status(101, "In Progress"))
    #print(bug_tracker.list_all_bugs())
    print(bug_tracker.update_status(103, "Closed"))
    #print(bug_tracker.list_all_bugs())
    print(bug_tracker.update_status(102, "Closed"))

