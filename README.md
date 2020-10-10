# DBFA 8 Store Manager <span style="color: #496dd0">#RadicallyNew</span>
##### 09/10/2020: DBFA 8.60 (beta) release (see changelog)
  
A store manager like none other, DBFA handles everything from billing and inventory to employees, payments, shifts and even deliveries, while staying open source! ;)
DBFA comes with ultra-light data structures and superior security features, which we take pride over.

NOTE: DBFA consumer-grade builds are published via GitHub releases while master houses the latest source which may/ may not work at all.

####### [Not synced with repo] [![Run on Repl.it](https://repl.it/badge/github/deltaonealpha/DBFA)](https://repl.it/github/deltaonealpha/DBFA)

## Build Highlights:
<h5>> DBFA Employee Manager v2.1 (auto-shift scheduling, leave applications, automated salary calculation and work monitoring)
<h5>> DBFA Incremental Security Update (09/10/2020)
<h5>> Updated with newly written 8.52docs</h5>

## Roadmap
- [ ] Convert main authentication to server-based.
- [ ] Start transitioning from CLI to GUI elements.

## Getting Started:
See deployment for notes on how to deploy the project on a live system.

### Prerequisites:

```
tabular-print
tabulate
pywin32
reportlab
PySimpleGUI
pandas
opencv-python
tqdm
colorama
win10toast
telegram-send
telegram
python-telegram-bot
PyQRCode
Pillow
spotlib
SwSpotify
pynput
matplotlib
oschmod
```
DBFA's download package has a 'DBFApip' file with all pip commands to straightly pip from.

### Installing:
Get DBFA running on your system this way:

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
<p><a href="https://t.me/deltaonealpha">Pranav Balaji</p>

List of [contributors](https://github.com/deltaonealpha/DBFA/contributors) who participated in this project.

## License:
This project is licensed under the GNU General Public License - Version 1.c, April 2020 - see the [LICENSE.md](LICENSE.md) file for more details.

## Changelog:
<h4>Only recent changes are hosted here. For previous changelogs: https://telegra.ph/DBFA-8-Release-Candidate---1-08-16</h4>

<h3>Changelog 8.60 Donnager (beta)</h3>
- Updated DBFA Employee Manager v(1.0) >>> v(2.1)

- DBFA Smart Shift-Scheduler (Auto-schedules the day before, Telegrams the owner. (Coming soon: Email sched. to all employees))

- Leave Applications: Apply for a leave a day before and DBFA will automatically change the schedule!

- Automatic salary calculations (depends on post, days, weekly hours and overtime worked and applicable bonus-es)

- Rectified detection rules for the webhook.


<h3>Changelog 8.55 Donnager (stable)</h3>

- DBFA Incremental Security Update (03/10/2020): Presenting DBFA Web Hook Security. The admin can now type 'disableDBFA' in our Telegram bot and DBFA access on related installations will be disabled from the next menu cycle/ boot until re-enabled by the admin. DBFA will exit and display a webpage showing operational status and reasons for exiting.

- (v8.56: 24/09/2020): Added GUI-prompt for sending customer invoice emails.

- Presenting delta File Integrity Validation Service (auto-launches on crash)
Error catching across the WHOLE length of the code!
https://telegra.ph/file/da2c8cc43ec658c6c8273.png

- Changed 2FA model from OTP-based to Telegram inline-button validation.

- Presenting login v2 with a synchronous multi-logging with a timeout of a minute.

- Presenting bypass prevention service v2.

- Presenting DBFA employee manager (attendance/ pay salary/ hire/ change details/ fire employee ༼ ●'◡'● ༽つ).

- Improvements to primary login system.

- Improvements to bypass prevention service.

- More in-depth logging.

- Docs have been re-written from scratch.

- Improved updater version tracking (option: "Check for Updates")

- Rectified all general and text formatting bugs.

- More changes and base blobs for future features added.

<h3>Changelog 8.3 Donnager (stable)</h3>

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



