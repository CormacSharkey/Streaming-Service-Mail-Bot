# Streaming-Service-Mail-Script

<!-- [![Contributors][contributors-shield]][contributors-url] -->
![GitHub contributors](https://img.shields.io/github/contributors/CormacSharkey/Streaming-Service-Mail-Script?style=flat)
![GitHub forks](https://img.shields.io/github/forks/CormacSharkey/Streaming-Service-Mail-Script?style=flat)
![GitHub Repo stars](https://img.shields.io/github/stars/CormacSharkey/Streaming-Service-Mail-Script?style=flat)
![GitHub Issues or Pull Requests](https://img.shields.io/github/issues/CormacSharkey/Streaming-Service-Mail-Script?style=flat)
![GitHub License](https://img.shields.io/github/license/CormacSharkey/Streaming-Service-Mail-Script)
[![GitHub][github-shield]][github-url]
[![Goodreads][goodreads-shield]][goodreads-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

A Python script that uses the Watchmode API to notify you about new releases on streaming services on a daily basis.

Author: CormacSharkey

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about">About</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributions">Contributions</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## About

I created this project to keep myself updated on new releases from streaming services through a common medium; email. To my knowledge, there's no easy and reliable way to know every release from all major streaming services without subscribing to every single one. So I made the tool!

Using this script, I know what movies and tv shows release every day, on each platform. I get the new releases from Watchmode API, format them presentably and send them in email format. Automating the script to run every day through a Cron job means I receive daily emails on new releases and where to watch them. 

And the best part: the API is free for personal use and runs in Python!

## Getting Started 

### Prerequisites

- Get a free API Key from [Watchmode API](https://api.watchmode.com/)

- Create a Gmail Account ([Google Account](https://accounts.google.com))

- Create an App Password ([Gmail](https://support.google.com/mail/answer/185833?hl=en))

### Installation

1. Clone the repo
````
git clone https://github.com/CormacSharkey/Streaming-Service-Mail-Script.git
````

2. Create a `.env`

3. Add your Watchmode API Key, your App Password, your Sender and Receiver Emails, and your Release Date Delta
````
API_KEY="XXXXXXXXXXXXXXXX"
APP_PASSWORD=XXXX XXXX XXXX XXXX
SENDER_EMAIL=sender_email@gmail.com
RECEIVER_EMAIL=receiver_email@gmail.com
RELEASE_DATE_DELTA=-1
````
> [!NOTE]
> The Sender Email is the Gmail Account with your App Password.

4. Install the required packages
````
pip install -r requirements.txt
````  

5. Change the remote git url to avoid pushing to base project
````
git remote set-url origin github_username/repo_name
git remote -v # confirm the changes
````

## Usage

- Running the script:
````
python src/main.py
````

- Automating the script:
  - On **Linux**, create a [Cron job](https://stackoverflow.com/questions/34753831/execute-a-shell-script-everyday-at-specific-time)

  - On **Windows**, use the [Task Scheduler](https://andrebnassis.medium.com/automate-tasks-on-windows-with-task-scheduler-93dea7c66bce)

- Modifying the script:

The release day the script checks can be modified in `.env` at Line 5:
````
RELEASE_DATE_DELTA=-1
````
The environmental variable *RELEASE_DATE_DELTA* controls the offset of days from today. E.g. *RELEASE_DATE_DELTA=0* means releases from today, *RELEASE_DATE_DELTA=1* means releases from tomorrow, etc. The recommendation is *RELEASE_DATE_DELTA=-1*, meaning releases from yesterday.

## Contributions

If you want to contribute something that makes this better, please fork the repo and create a pull request. Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'added some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Acknowledgements

Project Resources:
- [Watchmode API](https://api.watchmode.com/)
- [Sending Emails with Python](https://realpython.com/python-send-email/)
- [Simple-README-Template](https://github.com/CormacSharkey/Simple-README-Template)


[linkedin-shield]: https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white
[linkedin-url]: https://www.linkedin.com/in/cormac-sharkey/

[github-shield]: https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white
[github-url]: https://github.com/CormacSharkey

[goodreads-shield]: https://img.shields.io/badge/Goodreads-372213?style=flat&logo=goodreads&logoColor=white
[goodreads-url]: https://www.goodreads.com/user/show/107336829-cormac-sharkey