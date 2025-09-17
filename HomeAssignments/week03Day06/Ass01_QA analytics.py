import numpy as np
#QA analytics system

class TestReport:
    def __init__(self,execution_times):
        self.execution_times = execution_times

    def average_time(self):
        #mean execution time
        avg = np.mean(self.execution_times)
        return f"The Average Execution time of test is {avg}"



    def max_time(self):
        maxi = np.max(self.execution_times)
        return f"The Maximum Execution time of test is {maxi}"
    

class RegressionReport(TestReport):

    def slow_tests(self, threshold):
        self.threshold = threshold
        # new_arr = [] 
        # for i in self.execution_times:
        #     if self.threshold > i:
        #         new_arr.append(i)
        new_arr = [int(i) for i in self.execution_times if i > self.threshold]
        
        return f"List of Above threshold Timers: {new_arr}"
    

if __name__ == "__main__":
    exec_timers = np.random.randint(5,20, size=10)
    print(F"The Exec Timers: {exec_timers}")
    newObj = RegressionReport(exec_timers)
    print(newObj.slow_tests(12))
    print (newObj.average_time())
    print(newObj.max_time())

