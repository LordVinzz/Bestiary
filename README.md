# QuestKeeper MobManager

QuestKeeper is a lightweight web application built with Python and Flask, designed to assist Dungeon Masters in managing a bestiary of enemies and tracking their stats during tabletop role-playing game (RPG) sessions. This tool runs in the browser, providing a user-friendly interface for Dungeon Masters to organize and keep track of various creatures encountered in their campaigns.

## Features

- **Bestiary Management**: Easily add, edit, and delete entries for creatures in your campaign's bestiary.
- **Stat Tracking**: Keep track of important stats such as hit points, armor class, and damage for each enemy.
- **User-Friendly Interface**: Intuitive and responsive web interface for seamless navigation and quick access to information.
- **Lightweight**: Designed to be lightweight and efficient, allowing for smooth performance even on low-resource systems.

## Installation

1. Ensure you have Python installed on your system.
2. Clone this repository to your local machine:

   ```
   git clone https://github.com/LordVinzz/Bestiary.git
   ```
3. Navigate to the project directory:
   ```
   cd Bestiary
   ```
4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
   
## Usage
1. Run the application
	```
	python main.py
	```
2. Open your web browser and go to `http://localhost:5000` to access QuestKeeper.
3. Start managing your bestiary, adding creatures, and tracking their stats as needed.

## Project Paradigm

QuestKeeper follows a unique paradigm aimed at achieving a lightweight frontend with maximum modularity in the backend. The project prioritizes a fixed and minimalistic frontend to ensure a seamless user experience, while the backend is designed to be highly modular. This approach allows for easy extensibility and modification of backend functionalities without the need for significant frontend adjustments. Dungeon Masters can expect a stable and consistent user interface while enjoying the flexibility to customize and expand the backend to suit their specific campaign needs. The goal is to create a powerful tool that evolves with the Dungeon Master's requirements, offering a robust and adaptable platform for managing campaigns.


## Contributing

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix: `git checkout -b feature/new-feature`.
3.  Make your changes and commit them: `git commit -m "Add new feature"`.
4.  Push to the branch: `git push origin feature/new-feature`.
5.  Create a pull request.

## License

QuestKeeper is licensed under the GNU General Public License version 3.0 (GPL-3.0).

Happy questing! 🐉✨
