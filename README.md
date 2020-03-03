# Load Balance

This is a simples load balancer algorithm to check how much does it cost to run scalable Virtual Machines.

In order to run it you must:
- Have python 3.x or up
- run ```pip install -r requirements.txt``` on your terminal

The code is ready to run. But, since no input files were given, it'll run a test with a random sample of data.
You can check the results on the _/test_ folder on the files:
  - random_input.txt : inputs generated
  - random_output.txt : the resulte of that random input
the other files (testX.txt) are pre-set date for testing on given condition.


If you want to run the program with your own input files, you should:
- open the _main.py_ on the root folder
- at the end of the file, you can pass the file paths (input_path, output_path) as arguments on the ```main()``` method
