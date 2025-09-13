with open("ko.txt","w") as f:
    f.write("TestCase1 - Passed \nTestCase2 - Failed \nTestCase3 – Passed")
    print("write operation Completed")

with open("ko.txt","a") as f:
    f.write("\nTestCase4 - Passed \nTestCase5 – Failed")
    print("append operation Completed")

with open("ko.txt","r") as f:
    content = f.read()
    print("read operation Completed")
    print(content)
    print("@@@@@@@@@@@")

def Summary_count():
    with open("ko.txt","r") as f:
        content = f.readlines()
        pass_count = 0
        fail_count = 0
        for line in content:
            if "Passed" in line:
                pass_count += 1
            elif "Failed" in line:
                fail_count += 1
        return f"Total Test Cases: {len(content)}, Passed: {pass_count}, Failed: {fail_count}"
    

print(Summary_count())