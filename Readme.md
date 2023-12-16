## Assignment Title: Backend Engineering Challenge
Welcome to our project  assesment!
This Flask application provides a basic e-commerce API with user authentication and product management functionalities.

### Introduction

We have made a basic **E-Commerce Website** from scratch with full functionalities and checking it through **Postamn Api**. In the `prod_app.py` the basic user authentication with user name and password is included. The password is tehn converted to a hash value so that other than the user can not understand or read the password. This ensures the security feature of the basic application processing. Upon `Registration` the user pasword is converted to a much secured values and the access token is generated so that the user when `Login` the access token can automatecally fetched and the user can be logged in to the portal. User can enter the products, quantity and price in the **JSON** format in the postman API and then hit the URL. This would enable a succesfull transfer of the data to the application. The test cases written in the `testing_prod.py` makes sures every possible scenario the user can use the application. You can also see the pictures for your understanding how the data looks like when it is saved in the MySQL data base also you can refer the test cases pictures too.

## How to Run

This guide provides the basic introduction on how to run the **Flask Application** for the **Backend Engineering Challenge**

### Local Execution

1. **Clone the Repository:**

    ```bash
    https://github.com/
    cd 
    ```

2. **Create and Activate Virtual Environment:**

    If `virtualenv` is not installed:

    ```
    bash
    pip install virtualenv
    ```

    Then create and activate the virtual environment:

    ```
    bash
    python3.8 -m venv virtualenv
    source virtualenv/bin/activate  
    # On Windows, use `virtualenv\Scripts\activate`
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Make a MySQL Connection and the Database:**

    Set the connection name to **root** and the password to **12345**
    Now make the database by clicking the database option and name it **e_commerce**
    The structure will look like this.

    ```
    mysql://root:12345@localhost:3306/e_commerce'
    ```

5. **Run the Application:**
    
    Execute the provided `prod_list.py` file

    ```
    python prod_list.py
    ```

6. **Testing of USER through Postman API:**
    
    For registering the user in the database through Postman hit the POST to `http://127.0.0.1:5000/register`, send the username and password in throgh JSON format by the Postman as the flask application starts as by default 5000 port and hit the **POST**, after successful registration of the user you can see the access token and the hash password and username in the MySQL Database.
    ```
    {
        "username": "ahsan",
        "password": "abc12345"
    }
    ```
    To Login the register user trough Postman `http://127.0.0.1:5000/login` send the same username and password through the same format as registering the user and hit the **GET or POST**. After successful login you can see the access token.
    ```
    {
        "username": "ahsan",
        "password": "abc12345"
    }
    ```
    If the user exists in the database as the time of registering you will get an error of user already exists. In the case of login if the username or the password is not matched you will get the error of username or password is invalid.

7. **Testing of PRODUCTS through Postman API:**

    Basic CRUD is made for the products 
    ↣ To check the Postman is working properly gust hit the `GET` with the url `http://127.0.0.1:5000/` and the result will pop up saying 'Application is been started, hit /products to continue.'

    ↠ To **Create** the products hit the `POST` on the url `http://127.0.0.1:5000/products` and send the data in the **JSON** format in the body of the Postman 
    ```
    {
        "name": "Watch",
        "price": 9.99,
        "quantity": 3
    }
    ```

    ↠ To **Read** the products hit the `GET` on the url `http://127.0.0.1:5000/products`. You will abe to see all the products saved in the **MySQL Database**, to see some specific products you have hit to url to the specific product ID that is auto generated `http://127.0.0.1:5000/products/<product id>`

    ↠ To **Update** any of the product hit the `PUT` on the url `http://127.0.0.1:5000/products/<product id>`, then update the produced in the following manner.
    ```
    {
        "name": "Updated Watch",
        "price": 99.99,
        "quantity": 33
    }
    ```
    You will see the success status after successfully updating the products.

    ↠ To **Delete** any of the product hit the `DELETE` on the url `http://127.0.0.1:5000/products/<product id>`, to delete the specific product. You will the success status after successfully deleting the specific product.

8. **Run the Test Cases:**
    
    Execute the provided `testing_prod.py` file

    ```
    pytest testing_prod.py
    ```

Your Application is been started and you are good to go.