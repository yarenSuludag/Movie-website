# Film Management Website

- **Description:**
  - A comprehensive web-based application for managing film records.
  - Built using Flask and MySQL.
  - Allows adding new films, deleting films, and performing search, filter, and sort operations on film data.
  - Dynamically builds SQL queries based on user inputs.

## Table of Contents
- Overview
- Technologies Used
- Installation
- Configuration
- Usage
- Project Structure
- Contributing
- License

## Overview
- **Purpose:**
  - To manage film records efficiently and in a user-friendly manner.
- **Key Features:**
  - **Add Films:** Insert film records with details such as title, director, genre, release year, duration (minutes), IMDb rating, country, language, and production company.
  - **Delete Films:** Remove films from the database by their ID.
  - **Search & Filter:** Search films by title and filter results based on genre, country, language, and production company.
  - **Sort:** Order the film list by attributes like IMDb rating or release year.
- **Benefits:**
  - Streamlines film data management.
  - Reduces manual effort.
  - Improves data accuracy and reliability.

## Technologies Used
- **Flask:** A lightweight Python web framework for building the application.
- **MySQL:** A relational database management system to store film data.
- **MySQL Connector for Python:** A library to connect and interact with the MySQL database.
- **HTML/CSS:** Used in conjunction with Flask’s templating engine to create and style the web interface.

## Installation
- **Clone the Repository:**
  - Run: `git clone https://github.com/yourusername/film-management-website.git`
  - Navigate into the project directory: `cd film-management-website`
- **Set Up a Virtual Environment (Optional but Recommended):**
  - Create a virtual environment: `python -m venv venv`
  - Activate it:
    - On Unix/Mac: `source venv/bin/activate`
    - On Windows: `venv\Scripts\activate`
- **Install Dependencies:**
  - Execute: `pip install flask mysql-connector-python`
- **Set Up MySQL Database:**
  - Ensure MySQL is installed and running.
  - Create a new database named `film_sorgu`.
  - Create a table named `films` using the following SQL schema:
    ```sql
    CREATE TABLE films (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        director VARCHAR(255),
        genre VARCHAR(255),
        release_year INT,
        duration_minutes INT,
        imdb_rating FLOAT,
        country VARCHAR(255),
        language VARCHAR(255),
        production_company VARCHAR(255)
    );
    ```
- **Configure Database Credentials:**
  - In the `app.py` file, update the MySQL connection details:
    ```python
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="yourpassword",  # Replace with your actual MySQL password
        database="film_sorgu"
    )
    ```

## Configuration
- **Database Configuration:**
  - Verify that the `film_sorgu` database is set up correctly and accessible using the provided credentials.
- **Flask Configuration:**
  - The Flask application is currently set to run in debug mode, which is ideal for development.
  - For production, disable debug mode and implement additional security measures as needed.

## Usage
- **Starting the Application:**
  - Run the command: `python app.py`
- **Accessing the Website:**
  - Open your web browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).
- **Homepage Functionality:**
  - View all films stored in the database.
  - Use the search and filter form to query films by title, genre, country, language, and production company.
  - Sort films based on criteria such as IMDb rating or release year.
- **Adding a Film:**
  - Navigate to the film addition form via the `/ekle` route.
  - Fill in the film details and submit the form to add a new film to the database.
- **Deleting a Film:**
  - Each film entry on the homepage includes a delete option.
  - Click the delete button next to a film to remove it from the database.

## Project Structure
- **app.py:**
  - Contains the main Flask application.
  - Defines routes for:
    - `/` – The homepage displaying films with search, filter, and sort functionality.
    - `/ekle` – Route for adding a new film.
    - `/sil/<int:film_id>` – Route for deleting a film by its ID.
- **templates/ Directory:**
  - Holds HTML templates (e.g., `index.html`) used for rendering web pages.
- **static/ Directory:**
  - Contains static assets like CSS files, JavaScript files, and images used in the application.

## Contributing
- **How to Contribute:**
  - Fork the repository and create a new branch for your changes.
  - Develop new features or fix bugs on your branch.
  - Submit a pull request with detailed information about your changes.
  - For major changes, please open an issue first to discuss your proposed modifications.

## License
- **License Information:**
  - This project is distributed under the MIT License.
  - For more details, please see the [LICENSE](LICENSE) file in the repository.
