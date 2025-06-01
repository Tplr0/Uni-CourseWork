# Hall Booking System - Python Coursework

**Console-Based Hall Management Application**
A Python project that simulates a basic event hall booking system with admin and user login capabilities. Data is stored in local text files and interactions are handled via the terminal interface.

---

## **Features**

* Admin Panel: View, manage, and edit hall information and bookings
* User Portal: Login, register, and book available halls
* Persistent Storage: All bookings and login credentials stored in `.txt` files
* Modular Codebase: Each component (admin/user/main) separated into different scripts

---

## **Prerequisites**

To run this project, you'll need:

* Python 3.6 or above

No additional libraries required.

---

## **Getting Started**

**Clone the Repository:**

```bash
git clone https://github.com/yourusername/Python_CourseWork.git
cd Python_CourseWork
```

**Run the Script:**

```bash
python main.py
```

---

## **Project Structure**

* `main.py`: Launch point for both user and admin operations
* `admin.py`: Contains admin logic to view/edit bookings and halls
* `User.py`: User logic for hall booking and login
* `User 1.0.py`: Alternate version of the user module (legacy)
* `adminlogin.txt`: Stores admin usernames and passwords
* `userlogin.txt`: Stores user credentials
* `bookinginfo.txt`: Stores user booking records
* `hallinfo.txt`: Hall details such as names and availability

---

## **Usage**

* **Admin Login**: Access admin functions like viewing bookings and updating hall info
* **User Login/Register**: Book a hall from available options
* **Persistent Tracking**: All login data and bookings are written to local text files

---

## **Troubleshooting**

* `FileNotFoundError`: Ensure all `.txt` files are in the same directory as the Python scripts
* `PermissionError`: Make sure your files are not read-only when running the program
* If login fails, verify the contents of `adminlogin.txt` or `userlogin.txt`

---

## **Acknowledgments**

This project uses standard Python libraries and file I/O. No external dependencies were required.

* [Python File Handling Docs](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
* [Python Functions & Modules](https://docs.python.org/3/tutorial/modules.html)

---
