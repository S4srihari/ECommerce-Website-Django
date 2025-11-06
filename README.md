**E-Commerce Website with Django**. An end-to-end E-Commerce site built leveraging the Django framework. 
This project provides a fully functional online shopping experience, including user accounts, product management, and a seamless checkout process.

---

Technologies UsedThis project is built using a modern stack, focusing on Python for the backend and standard web technologies for the frontend.
Category Technology 
Backend Framework Python, Django
Database SQLite
Frontend HTML, CSS, JavaScript

---

✨ **Key Features**

The application is designed to handle core e-commerce functionalities for both
customers and administrators: Customer-Facing Features
User Authentication: Secure registration, login, and logout functionality.
Product Catalog: Browse a comprehensive list of products with detailed product pages.
Shopping Cart: Add, update, and remove items from the shopping cart before checkout.
Order Placement: A streamlined checkout process for completing purchases.
User Profile: View and manage personal information and order history.

**Administrator Features**
Admin Dashboard: Utilize the powerful Django 
Admin interface to manage the site.
Product Management: Create, edit, and delete product listings, including images and inventory.
User Management: Oversee and manage customer accounts.
Order Tracking: View and update the status of incoming orders.

---

⚙️ Getting StartedFollow these steps to get your local copy of the project up and running.PrerequisitesYou will need Python installed on your system. It's recommended to use a virtual environment.Bash# Check if python is installed
python --version
InstallationClone the repository:
Bash git clone https://github.com/S4srihari/ECommerce-Website-Django.git
cd ECommerce-Website-Django
Create and activate a virtual environment:
Bash # For Linux/macOS
python3 -m venv venv
source venv/bin/activate

# For Windows (Command Prompt)
python -m venv venv
venv\Scripts\activate
Apply database migrations:
Bash python manage.py makemigrations
python manage.py migrate

Create a superuser (admin account):
Bash python manage.py createsuperuser
Follow the prompts to set up your username and password for the admin panel.

---

💻 Usage
To run the application locally, execute the following command:
Bash
python manage.py runserver
The application will now be running at:
Website: http://127.0.0.1:8000/
Admin Panel: http://127.0.0.1:8000/admin/
Use the superuser credentials you created to log in to the admin panel and start adding products!

---
Feel free to Fork/clone/Star the repo.
