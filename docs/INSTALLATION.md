# Installation Guide for spotdl-web

This guide will walk you through the steps to install and set up spotdl-web on your local machine.

## Prerequisites

Before you begin, ensure you have the following installed:

1.  **Python 3.x:** spotdl-web requires Python 3.x. You can check if you have Python installed by opening your terminal and typing:
```
bash
    python3 --version
    
```
If Python is not installed, download it from the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2.  **pip:** pip is the package installer for Python. It's usually included with Python installations. To check if you have pip, run:
```
bash
    pip --version
    
```
If pip is not installed, follow the instructions here: [https://pip.pypa.io/en/stable/installation/](https://pip.pypa.io/en/stable/installation/)

3. **Git:** You need git to clone the repository. You can check if you have Git installed by opening your terminal and typing:
```
bash
    git --version
    
```
If Git is not installed, download it from the official Git website: [https://git-scm.com/downloads](https://git-scm.com/downloads)

## Installation Steps

Follow these steps to install spotdl-web:

1.  **Clone the Repository:**

    Open your terminal and navigate to the directory where you want to install spotdl-web. Then, clone the repository from GitHub:
```
bash
    git clone https://github.com/0xfunboy/spotdl-web.git
    
```
This will create a `spotdl-web` directory in your current location.

2.  **Navigate to the Project Directory:**
```
bash
    cd spotdl-web
    
```
3.  **Install Dependencies:**

    Install the required Python packages using pip. These packages are listed in the `requirements.txt` file:
```
bash
    pip install -r requirements.txt
    
```
This command will install Flask and any other necessary libraries.

## Running spotdl-web

Once you have completed the installation, follow these steps to run spotdl-web:

1.  **Start the Flask App:**

    In your terminal, navigate to the `spotdl-web` directory (if you are not already there) and run the Flask app:
```
bash
    python app.py
    
```
2.  **Open Your Browser:**

    Open your web browser and go to:
```
    http://127.0.0.1:5000/
    
```
You should now see the spotdl-web interface.

## Troubleshooting

*   **ModuleNotFoundError:** If you encounter a `ModuleNotFoundError` (e.g., `ModuleNotFoundError: No module named 'flask'`), it means that you have not correctly installed the dependencies. Ensure you have run `pip install -r requirements.txt` in the `spotdl-web` directory.
*   **Port 5000 in Use:** If you receive an error indicating that port 5000 is in use, another process is using the same port. You can try changing the port in `app.py` or closing the other process.

## Uninstall

If you need to uninstall the project, just delete the folder.