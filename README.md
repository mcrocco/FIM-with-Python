

<img src="https://i.imgur.com/2UCYuPe.jpeg" alt="FIM Picture"/>
<p>In this project, I create a File Integrity Monitoring (FIM) System using Python.</p>

<h2>Resources/Technologies Used:</h2>
<p> - MacOS</p>
    <p>- Visual Studio Code</p>
    <p>- Python 3.10.8</p>
    <p>- Pages & TextEdit files</p>
    <p>- Hashing</p>
<h2>Contents of Project:</h2>
<p>1. Base Code Overview</p>
<p>2. Creating Function to Hash File</p>
<p>3. Creating a Baseline File to Store Hash</p>
<p>4. Creating an Infinite While Loop to Monitor File Changes</p>

<h2>Grand Overview of Python Code</h2>
<p>- You can either open the Python file in this repository or follow the screenshots below. Please note, that the file paths in this code will need to be changed to whatever file you would like to monitor.</p>
<img src="https://i.imgur.com/yKl6N3u.png" alt="Beginning of Python code"/>
<p>- The beginning lines of code are for importing libraries so that we can use functions for hashing (hashlib) and setting the time for the infinite loop (time). We also gather the user's input on choosing whether they want to create a new baseline hash or keep the currently used baseline hash. This baseline will be used for comparing if the file has been modified/deleted in any way, as when a user makes any changes to that file, the hash will change.</p>

<h2>Creating a Function to Hash a File</h2>
<img src="https://i.imgur.com/mmRoYAp.png" alt="Creating Function Code Block"/>
<p>- This code block creates our function that will calculate a hash of the file we want to monitor. You may edit which hashing algorithm to use, such as SHA-512. </p>

<h2>Creating a Baseline File to Store Hash</h2>
<img src="https://i.imgur.com/OyhW2Qo.png" alt="Start of If Statement"/>
<p>- The if statement triggers when the user inputs "A" or "a" in the terminal. This will run the calculate_file_hash function that was created earlier, and store the created hash in a text file called "baseline.txt". You can modify this section of code for the file path of choice, and also modify the name of the text file that will store the baseline hash.</p>

<h2>Creating an Infinite While Loop to Monitor File Changes</h2>
<img src="https://i.imgur.com/4gGpyHB.png" alt="Elif Statement"/>
<p>- The elif statement will run when the user inputs "B" or "b". This code block starts with creating an infinite while loop that will loop every second. You can modify how fast/slow the while loop runs by changing the sleep_duration variable at the beginning of the file.</p> 
<p>- The hash variable will continuously calculate the hash of the set monitored file and compare it to the get_hash variable, which collects the hash of the baseline file. Modify the hash variable so that it calculates the hash from the file you want to monitor.</p>
<p>- If the get_hash variable does not contain a hash, it means that someone has deleted the file. The loop would then prompt the user that the file has been deleted.</p>
<p>- If the get_hash variable is different from the hash variable, then it means that someone has modified the file in some way. The loop would then prompt the user that the file has been modified.</p>

<p>That's It! Run the code to the file of your choosing to make sure no one changes your file!</p>
