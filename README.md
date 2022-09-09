# Memrise-Solver
> Python and Selenium automation to scrape a course's dictionary and automatically complete the levels

**NOTE - I've included a pre-made dictionary file for [this](https://app.memrise.com/course/47049/5000-words-top-87-sorted-by-frequency/) course**

If this get enough attention I'll recode it into a browser script for way easier usage

# Prerequisites

* Python - https://www.python.org/downloads
* Chrome (or any other browser with the appropriate driver)
* Chromedriver - https://chromedriver.chromium.org
* Selenium - `pip3 install selenium`

# Usage

Open the scripts you'll use and:
 * put the path of your chromedriver into `PATH = `
 * put the ID of your course into `courseid = `


I've split this into 3 sections depending on what you already have and want to acheive

* Properaly format and create the dictionary file - [Create dictionary](#create-dictionary)
* Auto complete levels - [Levels](#levels)
* Auto speed review - [Speed review](#speed-review)

## Create dictionary

You can use or modify my included `dictionaryscraper.py` (it only scrapes up to 16 words per level) or create your own script

If you want to use my included `dictionaryscraper.py`:
  * Create a file named `memrise.json` in the same folder
  * Put your chromedriver path in `PATH = `
  * Put your course's ID in `courseid = `
  * Find `level == ` and change that to the number of total levels in the course
