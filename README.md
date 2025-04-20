# spotdl-web

## Introduction 🚀

spotdl-web is a web-based graphical user interface (GUI) for spotDL, a popular command-line tool for downloading music from Spotify. This project combines the functionality of spotDL with a user-friendly web interface, allowing you to search, browse, and download your favorite tracks, albums, and playlists directly from your web browser. spotdl-web makes it easier than ever to build your offline music library!

## Installation

Follow these steps to install and set up spotdl-web:

### Prerequisites

*   **Python 3.7+:** Ensure you have Python 3.7 or a newer version installed on your system. You can check this by running `python3 --version` in your terminal.
*   **pip:**  pip is the package installer for Python. Most Python installations come with pip. Check if you have it installed with `pip --version` or `pip3 --version`.

### Installation Steps

1.  **Clone the Repository:**
```
bash
    git clone https://github.com/0xfunboy/spotdl-web.git
    cd spotdl-web
    
```
2.  **Install Dependencies:**
```
bash
    pip3 install -r requirements.txt
    
```
This command will install Flask, which is necessary to run the web app.

## Running the App

1.  **Start the Flask App:**
```
bash
    python3 app.py
    
```
This will start the Flask development server.

2.  **Access the Web App:**
    Open your web browser and go to `http://127.0.0.1:5000/`. You should see the spotdl-web interface.

## Features
Here is a detailed list of the features you can enjoy with spotdl-web:

*   **Browse Your Library 📚:**
    *   Easily navigate through your music collection.
    *   View all available albums and their songs.
    *   Click on an album to see all the songs in it.
*   **Powerful Search 🔍:**
    *   Quickly find any track or album in your library.
    *   Search in real time to locate your music.
    *   Search by album or song name.
*   **Download Management 📥:**
    *   View the list of active downloads.
    *   See all the completed downloads.
    * Keep track of your music.
*   **Settings Customization ⚙️:**
    *   Choose your preferred download folder.
    *   Select the music quality.
    * Customize your downloads.
*   **Secure Login 🔐:**
    *   Test login functionality for secure access.
    * User authentication.

## Usage

Once you have the app running, you will see the main menu on top of the page:

*   **Library:** Click on "Library" to see all the available albums. Click on an album to display its songs.
*   **Search:** Click on "Search" and use the text input to look for music.
*   **Downloads:** Click on "Downloads" to check your active and completed downloads.
*   **Settings:** Click on "Settings" to choose the download folder and the music quality.
*   **Login:** Click on "Login" to access the test login functionality. Use `user1` / `password1` or `user2` / `password2` to login.

## Troubleshooting

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes.
4.  Submit a pull request.