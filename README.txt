Hi,

I am attaching a POSTMAN collection for testing of the APIs with this project.
Since the API is protected with JWT Auth so you have to extract the access token by hitting '/api/v1/token' and add it in header. You can declare a global variable in Postman with this header for the convinence I have increased the token live team to 59 minutes. 

To start run the migrations
python manage.py makemigrations
python manage.py migrate

Data Creation:
For the database to populate just need to run the command:

python manage.py shell < ProfileUser/creator.py

This will create the data and populate the database.

API:
1.) '/api/v1/token': POST
	Providing the JWT auth token for the authentication

2.) '/api/contact/add': POST 
	Adding data in the database 

3.) 'api/contact/1': PUT,GET
	Spamming the user phone number and getting the detail of that user

4.) '/contact': GET
	Showing all the data from database

5.) '/contact/?search=': GET
	Show the search results as asked in the assignment
	If the name is entered in search query it will first show the user whose full name starts with the input search query and then the rest of the users from the database.
	If the phone number is entered in search query it will simply show the
	user with the input query 

6.) '/api/user': POST
	Endpoint is used for registering new user.
	You need password,username,full_name,num to register a new user

Please let me know if you need any more information.

