# Snapchat Camera Roll Stealth Filter

Snapchat Lens Studio allows developers to "Build, Preview, and Distribute AR" experiences to Snapchat users.

I have identified a bug that allows users to take advantage of the 'Preview' function, allowing users to send items from their device's camera roll without displaying any type of filter to the recipient.
<p align="center">
**There is a risk of getting your account banned by testing this bug. Please do not use this for nefarious reasons.**<br>
Once the account UUID is obtained (**Step 9**), this script may be ran on Linux or other platforms that support Python.
</p>
## Installation - Obtaining serial_uuid with Windows
<p align="center">
Install **Snapchat Lens Studio **- https://ar.snap.com/download
Install** Process Hacker Portable** - https://processhacker.sourceforge.io/downloads.php<br>
</p>
1.  Open up and Sign into **Lens Studio** using the Snapchat account you wish to gain the camera upload filter:
<p align="center"><img  src="https://github.com/reidanb/Snapchat-Camera-Roll-Stealth-Filter/raw/main/docs/login_snap.jpg"></p>
2.  Once logged in, select and open a sample template in Lens Studio:
<p align="center"><img src="https://github.com/reidanb/Snapchat-Camera-Roll-Stealth-Filter/raw/main/docs/template.jpg" width="600" height="300"></p><br>
3.  In the top right, select **Scan Snapcode**:<br>
<p align="center"><img src="https://github.com/reidanb/Snapchat-Camera-Roll-Stealth-Filter/raw/main/docs/pair_pc.jpg" width="300" height="300"></p>
4.  Scan this code using your mobile, then select **Pair**:
<p align="center"><img src="https://github.com/reidanb/Snapchat-Camera-Roll-Stealth-Filter/raw/main/docs/pair_phone.jpg" width="300" height="300"></p>
5.  Go back to **Process Hacker** and find the Lens Studio entry:
<p align="center"><img src="https://github.com/reidanb/Snapchat-Camera-Roll-Stealth-Filter/raw/main/docs/search.jpg" width="600" height="150"></p>
6. Double click the Lens Studio entry, select **Memory**, then **Strings**, set length to **30**, then **OK**:
<p align="center"><img src="https://github.com/reidanb/Snapchat-Camera-Roll-Stealth-Filter/raw/main/docs/memory_string.jpg" width="600" height="150"></p>
7. Press Filter, then **Contains (case insensitive)**...
<p align="center"><img src="https://github.com/reidanb/Snapchat-Camera-Roll-Stealth-Filter/raw/main/docs/memory_search.jpg" width="600" height="150"></p>
...entering **serial_uuid**, then press **OK**:
<p align="center"><img src="https://github.com/reidanb/Snapchat-Camera-Roll-Stealth-Filter/raw/main/docs/uuid.jpg" width="300" height="150"></p>
8. In the results, find the entry containing ***encryption_key***, select this line and press the Copy button:
<p align="center"><img src="https://github.com/reidanb/Snapchat-Camera-Roll-Stealth-Filter/raw/main/docs/search_results.jpg" width="600" height="150"></p>
9. Paste this into a text editor, copying the **serial_uuid** value...
<p align="center"><img src="https://github.com/reidanb/Snapchat-Camera-Roll-Stealth-Filter/raw/main/docs/extract_uuid.jpg" width="600" height="150"></p>
... and adding this value to **config.py**:
<p align="center"><img src="https://github.com/reidanb/Snapchat-Camera-Roll-Stealth-Filter/raw/main/docs/config.jpg" width="440" height="100"></p>
10. Run the python script and if all is well, the lens will be sent to your phone:
<p align="center"><img src="https://github.com/reidanb/Snapchat-Camera-Roll-Stealth-Filter/raw/main/docs/cli_out.jpg" width="600" height="100"></p>
------------





## 🔗 Links
[![snapchat](https://img.shields.io/badge/%F0%9F%94%97-Lens%20Studio-yellow)](https://ar.snap.com/lens-studio)

[![blog](https://img.shields.io/badge/%F0%9F%94%97-reidanb.gitlab.io-yellow)](https://reidanb.gitbook.io/home/blog/snapchat-lens-studio-staging-bug)

## Overview - Snapchat API

