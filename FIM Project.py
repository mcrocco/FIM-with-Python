import hashlib
import time

#ask the user if they would like to create a baseline for the file or not
print("")
print("     A: Collect new  baseline")
print("     B: Begin file monitoring with saved baseline")
print("")
new_baseline_or_current = input("Would you like to create a baseline or start from an already collected baseline?")


#creating sleep variable for infinite while loop
sleep_duration = 1

#function to create hash of file
def calculate_file_hash(filepath, algorithm="sha256"):
    with open(filepath, "rb") as f:
        # create hash object
        hash_object = hashlib.new(algorithm)
        # update hash with file content
        hash_object.update(f.read())
        # return the digest of the hash
        return hash_object.hexdigest()


if new_baseline_or_current.lower() == "a":
    #calculate the hash from the target files and store in baseline.txt
    print("Option A Selected")
    hash = calculate_file_hash("/Users/masoncrocco/Desktop/Untitled.pages") #edit this with your file path
    #make a new file to store baseline hash in
    with open("baseline.txt", "w") as file:
        file.write(hash)
    print("Baseline hash has been created and stored in baseline.txt")
elif new_baseline_or_current.lower() == "b":
    #Begin monitoring files with saved baseline hash
    while True:
        time.sleep(sleep_duration)
        #continuously calculate hash of text file
        hash = calculate_file_hash("/Users/masoncrocco/Desktop/Untitled.pages") #edit this with your file path
        #Grab baseline.txt file containing hash
        with open("baseline.txt", "r") as file:
            grab_hash = file.read()
        if grab_hash == "":
            #notify the user as the text file has been deleted
            print("a file has been deleted")
        elif grab_hash != hash:
            #notify the user as the text file has been modified
            print("the file has been modified")
            
            