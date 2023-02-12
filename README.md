Project to create a employee website that has the following functionality:


1)	Home page that shows all employees number of days worked for the past 3 months in a bar chart with days less than 20 shown in red an rest in green.

2)	When clicked on the employees names it should redirect the user to that employee’s detail page.

3)	The employee’s detail page should contain their details along with a bar chart.

4)	The bar chart should represent number of days worked for at least past 12 months with days less than 20 shown in red an rest in green.

5)	The details page should also contain a filter to select between 2 months and export the data in a csv/xlsx in format of months and days worked 
	
E.g. If selected between April and June

Months	Days
April	29
May	30
June	30
 
***********************************************************************************************
***********************************************************************************************
 Things I code with
 * html5
 *JavaScript 
 *sqlite
 * Css
 * Django (python)

****************************************************************************************************
****************************************************************************************************
Create a virtual environment to install dependencies in and activate it:

$ virtualenv2 --no-site-packages env
$ source env/bin/activate
Then install the dependencies:

(env)$ pip install -r requirements.txt
Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv2.

Once pip has finished downloading the dependencies:

(env)$ cd project
(env)$ python manage.py runserver
And navigate to http://127.0.0.1:8000/
******************************************************************************************************************
