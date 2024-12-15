# Todo for Desktop

This is a simple To-Do List application built using Python with Tkinter. It provides basic functionalities to add, delete, and clear tasks. The app offers a simple graphical user interface (GUI) for managing tasks, making it ideal for desktop use.


## Features

- Add Task: Enter a task description and add it to the list.
- Delete Task: Select a task and delete it from the list.
- Clear All Tasks: Remove all tasks from the list at once.
- User Notifications: Alerts for invalid operations like attempting to delete without selecting a task or adding an empty task.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/todo-for-desktop.git
    ```
2. Navigate to the project directory:
    ```sh
    cd todo-for-desktop
    ```
3. Install the dependencies:
    ```sh
    npm install
    ```

## Usage

1. Run the application:
    ```sh
    python app.py
    ```
2. The application will open in a new window titled "To-Do List App".
3. Add tasks by entering a description in the text box and clicking the "Add Task" button.
4. Select a task from the list and click the "Delete Task" button to remove it.
5. Click the "Clear All Tasks" button to remove all tasks from the list.

## How It Works
- The application uses the Tkinter library to create the GUI.
- The tasks are stored in a list and displayed in a Listbox widget.
- Functions are used to add, delete, and clear tasks based on user actions.
- The tasks are managed using a list stored in memory and updated dynamically as tasks are added or removed.
- User input is validated to prevent empty tasks from being added and to ensure a task is selected before deletion.
- User notifications are displayed using message boxes to alert the user of invalid operations.
- The application is designed to be simple and easy to use, making it ideal for managing tasks on a desktop environment.


## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License.