try:
    with open("test_report.txt","w") as foo:
        foo.write("TestCase01 - Passed\n")
        foo.write("TestCase02 - Passed\n")
        foo.write("TestCase03 - Failed\n")
except FileNotFoundError:
    print("Fille not found")


try:
    with open("test_report.txt", "a") as aoo:
        aoo.write("TestCase04 - Passed\n")
        aoo.write("TestCase05 - Failed\n")
except FileNotFoundError:
    print("File not found")


def Result_Summary():
    pass_Count = 0
    fail_Count = 0
    with open("test_report.txt","r") as fo:
        content = fo.readlines()
        for line in content:
            if "Passed" in line:
                pass_Count += 1
            elif "Failed" in line:
                fail_Count += 1

        return f"Total cases count is {len(content)} \n\t Passed:{pass_Count} \n\t Failed:{fail_Count}"


summary = Result_Summary()
print(summary)





    


    
