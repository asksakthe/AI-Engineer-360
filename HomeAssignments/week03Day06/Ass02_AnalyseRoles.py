import numpy as np
import pandas as pd

class ManualTester:
    def analyze(self, data):
        #self.data = data
        return f"Test execution times are : {data[:6]}"

class AutomationTester:
    def analyze(self, data):
        return f"fastest test case : {np.min(data)})"

class PerformanceTester:
    def analyze(self, data):
        return f"percentile execution time: {np.percentile(data,95)}"
    

def show_analysis(data, tester):
    test_Obj = tester()
    act_out = test_Obj.analyze(data)
    return f"The Analysis of Test Result is {act_out} and exec by {tester.__name__}"


if __name__ == "__main__":
    data = np.random.randint(10,50, size=12)
    print(f"Data Input : {data}")
    role_map = {"ManualTester": ManualTester,"AutomationTester": AutomationTester,"PerformanceTester": PerformanceTester}
    role = input("Enter your role from choices (PerformanceTester / ManualTester / AutomationTester): ")
    tester_role = role_map.get(role)
    if tester_role is None:
        print("invalid role entered")
    else:
        out = show_analysis(data,tester_role)
    print(out)
    

1