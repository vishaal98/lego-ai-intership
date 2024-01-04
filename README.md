# lego-ai-intership

## Setup the project
#### create a virtual environment
```python -m venv venv```

#### start the virutal environment
```source venv/Scripts/activate```

#### install all the required packaged from the requirements file
```pip install -r requirements.txt```


#### DATABASE setup
Setup a postgres SQL on your local system as well and change the details in main.py in connection variable from line 7 to 13


## Questions and answers

#### Question 1
Write a singleton class in python that connects to the sql database [say postgresql] which should have following methods
•	get_connection(): return a database connection
•	fetch() : accepts a sql query [select] and returns its output in JSON format
•	execute(): accepts sql query [delete, insert, update] and returns the affected row number

### Answer:
```cd Q1```

```python singletonClass.py```

change to some other query in line 21 in main.py

#### Question 2
Use pandas to solve the following problem:
•	Create a CSV file from input
•	Parse the file into expected format mentioned in Output section
•	Write the processed data into csv

Input:
...................
sno,product_code,size,color,price
1,"P12XM1","s", "red", 120
1,"P12XM1","s", "green", 120
1,"P12XM1","s", "blue", 120
1,"P12XM1","m", "red", 130
1,"P12XM1","m", "green", 130
1,"P12XM1","m", "blue", 130
1,"P12XM1","l", "red", 150
1,"P12XM1","l", "green", 150
1,"P12XM1","l", "blue", 150
2,"P12XM2","s", "red", 130
2,"P12XM2","l", "red", 160

Output:
...................
sno,product_code,sizes,colors,prices
1,"P12XM1","s|m|l", "red|green|blue", "120|130|150"
2,"P12XM2","s|l", "red", "130|160"


### Answer
```cd Q2```

```python processData.py```


#### Question 3
Write the following content to a file and write a python program to filter the lines from that file where the name satisfies following conditions:
•	Should only start with a – f
•	Should be of minimum 4 characters
•	Should not contain [_]
•	Use regular expression
Input:
….........
abc
abcd
olneb
abcdefhi_
abcdefghij
!abcdefg

Output:
…..........
abcd
abcdefghij


### Answer
```cd Q3```

```python filter.py```