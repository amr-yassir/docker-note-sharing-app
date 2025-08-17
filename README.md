# 📝 Docker Note Sharing App

A simple **Note Sharing Application** built with **Flask** and **SQLite**, containerized using **Docker**.  
Users can create and view notes stored in a lightweight SQLite database.

---

## 🚀 Features
- Create notes through a web form  
- View all saved notes  
- Persistent storage using SQLite  
- Fully containerized with Docker  

---

## 🛠 Tech Stack

- [Python 3](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [SQLite](https://www.sqlite.org/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)


## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/amr-yassir/docker-note-sharing-app.git
cd secret-notes-app
```

Build and run with Docker Compose:

```bash
docker compose up --build
```
The app will be available at:
```
http://localhost:5000
```

## 🚀 Usage

- Open the app in your browser.
- Add your note in the input field and save it.
- Notes are displayed on the page and stored in SQLite.

