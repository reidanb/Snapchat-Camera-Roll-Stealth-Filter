# Snapchat Camera Roll Stealth Filter

Snapchat Lens Studio allows developers to **Build, Preview, and Distribute AR** experiences to Snapchat users.

I have identified a bug that allows users to take advantage of the 'Preview' function, sending items from their device's camera roll without displaying any type of filter to the recipient.

> ⚠️ **Warning:** There is a risk of getting your account banned by testing this bug. Please do not use this for nefarious reasons.  
> Once the account UUID is obtained (**Step 9**), this script may be run on Linux or other platforms that support Python.

---

## Installation - Obtaining `serial_uuid` with Windows

1. Install **Snapchat Lens Studio**: [https://ar.snap.com/download](https://ar.snap.com/download)  
2. Install **Process Hacker Portable**: [https://processhacker.sourceforge.io/downloads.php](https://processhacker.sourceforge.io/downloads.php)

---

1. Open and sign in to **Lens Studio** using the Snapchat account you wish to gain the camera upload filter for:

   <p align="center">
     <img src="https://github.com/reidanb/Snapchat-Camera-Roll-Stealth-Filter/raw/main/docs/login_snap.jpg">
   </p>

2. Once logged in, select and open a sample template in Lens Studio:

   <p align="center">
     <img src="https://github.com/reidanb/Snapchat-Camera-Roll-Stealth-Filter/raw/main/docs/template.jpg" width="600" height="300">
   </p>

3. In the top right, select **Scan Snapcode**:

   <p align="center">
     <img src="https://github.com/reidanb/Snapchat-Camera-Roll-Stealth-Filter/raw/main/docs/pair_pc.jpg" width="300" height="300">
   </p>

4. Scan the code with your mobile and select **Pair**:

   <p align="center">
     <img src="https://github.com/reidanb/Snapchat-Camera-Roll-Stealth-Filter/raw/main/docs/pair_phone.jpg" width="300" height="300">
   </p>

5. Open **Process Hacker** and find the Lens Studio process:

   <p align="center">
     <img src="https://github.com/reidanb/Snapchat-Camera-Roll-Stealth-Filter/raw/main/docs/search.jpg" width="600" height="150">
   </p>

6. Double click the process entry, go to **Memory**, then **Strings**, set length to **30**, then press **OK**:

   <p align="center">
     <img src="https://github.com/reidanb/Snapchat-Camera-Roll-Stealth-Filter/raw/main/docs/memory_string.jpg" width="600" height="150">
   </p>

7. Press **Filter**, choose **Contains (case insensitive)**, and enter `serial_uuid`. Then press **OK**:

   <p align="center">
     <img src="https://github.com/reidanb/Snapchat-Camera-Roll-Stealth-Filter/raw/main/docs/memory_search.jpg" width="600" height="150">
     <br>
     <img src="https://github.com/reidanb/Snapchat-Camera-Roll-Stealth-Filter/raw/main/docs/uuid.jpg" width="300" height="150">
   </p>

8. In the results, find the entry containing `encryption_key`. Select the line and press **Copy**:

   <p align="center">
     <img src="https://github.com/reidanb/Snapchat-Camera-Roll-Stealth-Filter/raw/main/docs/search_results.jpg" width="600" height="150">
   </p>

9. Paste the copied content into a text editor and extract the `serial_uuid` value:

   <p align="center">
     <img src="https://github.com/reidanb/Snapchat-Camera-Roll-Stealth-Filter/raw/main/docs/extract_uuid.jpg" width="600" height="150">
   </p>

   Add this value to `config.py`:

   <p align="center">
     <img src="https://github.com/reidanb/Snapchat-Camera-Roll-Stealth-Filter/raw/main/docs/config.jpg" width="440" height="100">
   </p>

10. Run the Python script. If all is well, the lens will be sent to your phone:

   <p align="center">
     <img src="https://github.com/reidanb/Snapchat-Camera-Roll-Stealth-Filter/raw/main/docs/cli_out.jpg" width="600" height="100">
   </p>

---

## 🔗 Links

[![Lens Studio](https://img.shields.io/badge/%F0%9F%94%97-Lens%20Studio-yellow)](https://ar.snap.com/lens-studio)  
[![Blog](https://img.shields.io/badge/%F0%9F%94%97-reidanb.gitlab.io-yellow)](https://reidanb.gitbook.io/home/blog/snapchat-lens-studio-staging-bug)

---

## Overview - Snapchat API

(Section still to be completed...)

