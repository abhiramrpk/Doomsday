# Doomsday

Welcome to *Doomsday*! This web application, developed using Django, HTML, CSS, Bootstrap, and JavaScript, offers a captivating gaming experience. Players embark on a journey through a story-driven treasure hunt, cracking progressively challenging levels to emerge victorious.

## Features

- *Story-Driven Gameplay:* Engage with an intriguing story that progresses through conversations between characters.
- *Animations and Characters:* Enjoy rich animations and dynamic characters that bring the story to life.
- *7 Challenging Levels:* Each level increases in difficulty, testing your wit and problem-solving skills.
- *User Accounts:* Each player registers and logs in to track their progress.
- *Leaderboard:* A dynamic leaderboard showcases the top players and their achievements.

## Technologies Used

- *Django:* Backend framework for robust and scalable web applications.
- *HTML & CSS:* For creating structured and styled web pages.
- *Bootstrap:* For responsive design and pre-built components.
- *JavaScript:* To add interactivity and dynamic behavior to the web pages.

## Installation

Follow these steps to set up the project locally:

1. *Clone the repository:*
   bash
   git clone https://github.com/abhiramrpk/doomsday.git
   cd doomsday
   

2. *Create a virtual environment:*
   bash
   python3 -m venv env
   source env/bin/activate   # On Windows use `env\Scripts\activate`
   

3. *Install dependencies:*
   bash
   pip install -r requirements.txt
   

4. *Apply migrations:*
   bash
   python manage.py migrate
   

5. *Create a superuser:*
   bash
   python manage.py createsuperuser
   

6. *Run the development server:*
   bash
   python manage.py runserver
   

7. *Access the application:*
   Open your web browser and go to http://127.0.0.1:8000/

## Usage

1. *Register an Account:* Sign up to create your player account.
2. *Login:* Use your credentials to log in.
3. *Start the Hunt:* Begin your adventure from the first level.
4. *Crack the Levels:* Solve puzzles and advance through the story.
5. *Check the Leaderboard:* See where you stand among other players.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch: git checkout -b my-feature-branch
3. Make your changes and commit them: git commit -m 'Add some feature'
4. Push to the branch: git push origin my-feature-branch
5. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to the Django, Bootstrap, and open-source communities for their invaluable tools and resources.
