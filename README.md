# my-site

my-site { BlogApp } is a web application built with Django for the backend and HTML/CSS for the frontend. It allows users to create and manage blog posts, comment on posts, and mark their favorite posts.

## Features

- **User Authentication:** Secure sign-up, login, and logout functionality.
- **Blog Posts:** Create, read, update, and delete blog posts.
- **Comments:** Users can comment on blog posts.
- **Favorite Posts:** Mark posts as favorites for easy access.
- **Responsive Design:** Ensures the app works well on both desktop and mobile devices.

## Tech Stack

- **Frontend:** HTML, CSS
- **Backend:** Django
- **Database:** SQLite (default with Django, can be configured to use other databases)

## Getting Started

### Prerequisites

- Python installed on your machine
- pip (Python package installer)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/harshitHash2/my_site.git
   cd my_site

2. Apply migrations to set up the database:
   `python manage.py migrate`

3. Create a superuser to access the Django admin:
   `python manage.py createsuperuser`

## Running the Application

1. Start the development server:
   `python manage.py runserver`

2. Open your browser and navigate to `http://localhost:8000`

## Usage

1. Comment on blog posts.
2. Mark posts as favorites to easily find them later.
3. Read the blogs and enjoy.

## Contributing

Contributions are welcome! Please follow these steps:
- Fork the repository.
- Create a new branch `git checkout -b feature/your-feature-name`
- Commit your changes `git commit -m 'Add some feature`
- Push to the branch `git push origin feature/your-feature-name`
- Open a pull request

## Contact

For any questions or suggestions, please reach out to me at `harshit.chauhan2015@gmail.com`.

