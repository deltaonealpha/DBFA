# DBFA Store Manager <span style="color: #496dd0">INCEPTION 1.0</span>
### Latest release changelog: http://latestdbfa.software.deltaone.tech/
##### 02/11/2020: DBFA INCEPTION 1.0 MAJOR RELEASE (see releases/ changelog)

After a year of continuous and rigid development, we are finally satisfied with what DBFA has become, a mature, stable and secure piece of software which we can pride over. Presenting a brand new DBFA, the INCEPTION 1.0.



A store manager like none other, DBFA handles everything from billing and inventory to employees, payments, shifts and even deliveries, while staying open source! ;) DBFA comes with ultra-light data structures and superior security features, which we take pride over.

NOTE: Please download DBFA from the releases section ONLY. 

A NEW .exe installer is now available for DBFA releases (8.60 & +) which automatically deploys the latest DBFA release with an additional built-in Python installer if the Python installation is unavailable and an updater.



## Release highlights (Inception 1.0):

---

**Quirky Highlights**

---

\-     **Presenting SUPERCACHING**: Unlike other codes which refer db values for every product, thereby adding time delay, DBFA fetches all details each time billing is started, and caches the data in its memory, thereby greatly increasing speed and reliability. SUPERCACHING is dynamically refreshed whenever the source is changed.

\-     DBFA now maintains a “**store group**” with all employees where the schedule is sent daily.

\-     All menu and table **designs are now unified** across DBFA.

\-     Added option - "**View Salary Payment Records**"

\-     The way DBFA handles product listing has been completely revamped: Product listing has been moved to database storage.

\-     You can now **add a new product listing** from DBFA itself.

\-     DBFA now automatically detects the installation directory, even if moved from the default directory.

----

**Time and Speed**

---

\-     Optimized DBFA to **boot 46% faster!** (9.9 seconds faster (19 seconds >>> 10.1 seconds)).

\-     Reduced menu loading time by 2 seconds.

---

**Updater & Deployment**

---

\-     **Presenting DBFA Backup & Switch v2.0** with backup restoration. Restoration needs the backup installation’s admin password to restore. Backup metadata is scanned, and files are updated accordingly.

\-     **UPDATER 2.0** can automatically deploy update files, increment version IDs, and make relevant data structure changes and clean-up post updating DBFA. The update changelog is also shown prior to obtaining update confirmation from the user.

---

**Security & Security Dashboard**

---

\-     **Presenting DBFA Login Accounts:** Multiple accounts can now be used to log into DBFA (1 x admin-level; unlimited cashier-level) with restricted access for non-admins. Login script has a checkbox to choose from, though usernames can still be typed.

\-     **Presenting the DBFA Security Dashboard**: Gives you a visual representation of program and dependencies health, with security-related options (clear records/ change passwords/ encryption toggle, 2FA toggle/ create login accounts)

\-     Employee Manager now needs administrator authentication.

-----

**Quality of Life Improvements**

-----

\-     INCEPTION 1.0’s **boot-screen** incorporates our **new design language**.

\-     Rectified all program/ webhook/ external bugs and reconfigured DBFA to avoid crashes.

\-     “View License” has now been merged with “About DBFA” and service status page has been moved to https://dashboard.deltaone.tech/dbfa.html.

\-     The menu has been reorganized for **better categorical sorting**.

\-     Added check for internet connection (displays helpful info when disconnected instead of crashing out).

\-     All password/ key references have been removed from the driver code.



## Roadmap

- [ ] Convert main authentication to server-based.
- [ ] Start transitioning from CLI to GUI elements.

## Getting Started:
See deployment for notes on how to deploy the project on a live system.
[Not synced with repo] [![Run on Repl.it](https://repl.it/badge/github/deltaonealpha/DBFA)](https://repl.it/github/deltaonealpha/DBFA)

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

## Source Changelog:
<h4><a href = "https://telegra.ph/DBFA-8-Release-Candidate---1-08-16">Click Here</a></h4>

