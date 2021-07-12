# StrawpollBot
A script that automatically sends votes to strawpoll.me, using the tor network to bypass IP duplication checking.

## Requirements:
* [Tor Browser](https://www.torproject.org/download/)
* Python Selenium Library - `pip install selenium`
* [Geckodriver](https://github.com/mozilla/geckodriver/releases) executable

## Usage:
1. Move geckodriver executable to same directory as script
2. Within the script, set `TOR_BINARY` to the path of the tor exeutable.
    - On Windows, this is located at C:\\Users\\\<username>\\Tor Browser\\Browser\\firefox.exe
3. Change `POLL_ID`, `CHOICE`, and `VOTE_COUNT` to desired values
4. Start Tor Browser and connect to the tor network
5. Execute script

![Poll Demonstration](https://i.imgur.com/e1IMrPW.jpg)
