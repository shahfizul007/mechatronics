# Processing Order

This application allows user to buy products from user interface. User can add to cart the products and confirm the order. User can also track the order progression to know the status of the order.
From the owner interface, owner can verify that they receive the order, done preparing, and food is on the way. By verifying these instances, user can track their food.

# Setting up project on vscode

1. Create a file on your file app.
2. Open your vscode, and open the empty folder that you just created.
3. Open the terminal. Under the file directory you just created, clone the repo. 
```
git clone https://github.com/shahfizul007/mechatronics.git
```
4. After successfully cloning the repo, go to the directory. Make sure the last thing on your file path is "/mechatronics"
```
cd mechatronics
```
5. Assuming you already have MySQL workbench installed, open the MySQL and login.
6. Use raw sql to create new database. The suggested name is mechatronics. Run the query. You should see a new database name mechatronics. If not, try to refresh.
```
CREATE DATABASE mechatronics;
```
7. Make sure you have mysqlclient installed.
```
pip install mysqlclient
```
8. Open webTest directory to find settings.py and scroll down to line 84. Update the necessary thing there.
9. After successfuly follow all the steps above, migrate!!
```
python manage.py makemigrations
python manage.py migrate
```
10. Run the server.
```
python manage.py runserver
```
