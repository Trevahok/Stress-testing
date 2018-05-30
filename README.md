# web-testing
This script tests a website's ability to accomodate the number of people - stress testing, by automating the users actions. 
It can be run on a Selenium grid running on different docker containers. 
# multi_node_user_interaction.py
- Before simulating a user, in the code:
- Comment or uncomment the methods a user interacts in the Node.
- Add or change the list of users that will be tested with. 
### Usage:
```python
python3 multi_user_node_interaction.py
```
- Enter the number of users you would like to simulate:

# plot.py
- It connects to the file specified and removes all the entries that said "Could not connecto host" errors 
- Plots the files with pyplot and saves the plot as .png file of the same file name 

### Usage:
```python
python3 plot.py your-filename-here
```

