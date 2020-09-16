# DBFA 8 Store Manager <span style="color: #496dd0">#RadicallyNew</span>
### 16/09/2020: DBFA 8.4 release (see changelog)
  
   
DBFA is a store management system like none other. From billing to inventory-management, order and delivery management to even employee management, literally anything a store could need. Ultra-light data structures, ultimate integrations, its all a store could crave, but open source! ;)

### [Not synced with repo] [![Run on Repl.it](https://repl.it/badge/github/deltaonealpha/DBFA)](https://repl.it/github/deltaonealpha/DBFA)

<h5 align="center">Mark 8.4 Donnager (stable): #RadicallyNew </h5>

## Build Highlights:
<h5>> Updated two-factor-authentication with inline-buttons, leveraging Telegram's BOT API v2. :D</h5>
<h5>> DBFA now has a complete employee management system built-in, with automatic UPI-based payments, attendance keeper and much more!</h5>

## Roadmap
- [ ] Convert main authentication to server-based.
- [ ] Start transitioning from CLI to GUI elements.

## Getting Started:

See deployment for notes on how to deploy the project on a live system.

### Prerequisites:

```
getpass
time
pathlib
sqlite3
sys and os
requests
datetime
shutil
pandas
opencv-python (cv2)
win10toast
pyqrcode
tabularprint
tqdm
colorama
reportlab
```
DBFA's download package has a 'DBFApip' file with all pip commands to straightly pip from.

### Installing:

Get DBFA running on your system this way:

First:
```
Install Python 3.7.4 (preffered due to its architecture)
      (select *get pip* and *add to PATH*)
```

Then:
```
Use this command to pip from the .txt file inside DBFA's package:
  pip install -r DBFApip.txt
```

If you encounter any bugs:
```
Run the program. If you encounter any issues/ crashes, check your environment and edit the code with absolute paths.
```

## Deployment:

DBFA was natively-coded to run on Windows. Use modules compatible with your operating system if you encounter module issues.


## Built With:

* [Python](https://www.python.org/) - Developed in Python
* [Sqlite](https://www.sqlite.org/index.html) - Data handled by Sqlite


## Developer:

<p><a href="https://t.me/DeltaOneAlpha">Pranav Balaji</p>

List of [contributors](https://github.com/deltaonealpha/DBFA/contributors) who participated in this project.

## License:

This project is licensed under the GNU General Public License - Version 1.c, April 2020 - see the [LICENSE.md](LICENSE.md) file for more details.

## Changelog:
<h2>Recent changes are hosted below. For previous changelogs: https://telegra.ph/DBFA-8-Release-Candidate---1-08-16</h2>

<h2>Changelog 8.4 Donnager (stable)</h2>
- Changed 2FA model from OTP-based to Telegram inline-button validation
- Presenting DBFA employee manager (track attendance/ pay salary/ hire/ change details/ fire employee ༼ ●'◡'● ༽つ)
- Rectified all general and text formatting bugs
- Improved primary login system
- Improved the bypass prevention mechanism
- Improved logging
- Updated new docs
- More changes and base blobs for future features added

<h2>Changelog 8.3 Donnager (stable)</h2>

-    Presenting DBFA two-factor-authenication!

-    Completely new logo and menu design (settings toggle to switch to old menu-style)


-    Presenting DBFA Options (settings; adjust every visual aspect to your liking)

-    Presenting DBFA Deliveries 

-    Presenting DBFA Stock Orders

-    Presenting DBFA Sales Analyzer (profit-date plot; also added to the pdf store report)

-    Presenting DBFA Store Music Controls (Thanks to XanderMJ (github.com/XanderMJ/spotilib))

-    Introducing DBFA quick control! (3a, 3b,.... instead of 3 [wait], and then a, b,.... .etc.)



-    Added version 8 boot image

-    Nuked all redundancies from the repo (net package size now under 50mb)

-    New sales logger v2 (sqlite)

-    Now export sales and customer data to CSV files.

-    Now add product-specific low-stock warnings     

-    Enabled invoice ID with retention

-    Updated menu with DBFA upstream changes



