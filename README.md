# Snapchat Camera Roll Stealth Filter

Snapchat Lens Studio allows developers to **Build, Preview, and Distribute AR** experiences to Snapchat users.

I have identified a bug that allows users to take advantage of the 'Preview' function, sending items from their device's camera roll without displaying any type of filter to the recipient.

> ⚠️ **Warning:** There is a risk of getting your account banned by testing this bug. Please do not use this for nefarious reasons.  
> Once the account UUID is obtained (**Step 9**), this script may be run on Linux or other platforms that support Python.

---

## 📖 Extended Description

Snapchat's Lens Studio enables creators to design and test augmented reality (AR) lenses. One of its core functions is allowing paired mobile devices to preview lenses directly within the Snapchat app. 

During exploration, a security oversight was discovered that lets users send content from their **local camera roll** using the lens preview system, without any visible AR filter or watermark, effectively **spoofing the origin** of the content.

This works by:
- Extracting the `serial_uuid` from system memory using Process Hacker.
- Exploiting the authenticated session between Lens Studio and Snapchat's mobile app.
- Using a custom Python script to mimic a legitimate lens preview request.

This bypass affects how Snapchat handles session previews and content authentication, opening the door to potentially misleading use of shared media.

> ⚠️ Use this tool responsibly. Misuse may violate Snapchat’s terms of service and lead to permanent bans. This project is intended for research and awareness only.

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

## 📡 Overview - Snapchat API

Snapchat’s API for Lens Studio relies on a structured flow that authenticates user sessions and links the desktop editor to the mobile Snapchat app. When a lens is previewed, a token (`serial_uuid`) is passed to validate the user’s session. This preview functionality assumes a trusted environment but lacks robust validation on the origin of the media being sent.

This diagram demonstrates the flow:

<p align="center">
  <img src="https://www.gitbook.com/cdn-cgi/image/dpr=2,width=760,onerror=redirect,format=auto/https%3A%2F%2Ffiles.gitbook.com%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FGhM1LWMMLXupwbzoNCKT%252Fuploads%252FKheEo0Ku89ahW7BvofKI%252Fsnapchat_diagram.png%3Falt%3Dmedia%26token%3Dbc40e35f-fd72-49d3-90a1-e1340d64b260" alt="Snapchat API Diagram">
</p>

### Key Points:
- Lens Studio generates a preview token tied to the session (`serial_uuid`).
- The mobile app accepts this token and prepares a lens preview environment.
- By injecting custom media and skipping watermark/AR checks, the lens preview becomes a **delivery channel** for unfiltered media.

This method exposes a security gap in how Snapchat verifies preview content integrity.

---

## 🔗 Links

[![Lens Studio](https://img.shields.io/badge/%F0%9F%94%97-Lens%20Studio-yellow)](https://ar.snap.com/lens-studio)  
[![Blog](https://img.shields.io/badge/%F0%9F%94%97-reidanb.gitlab.io-yellow)](https://reidanb.gitbook.io/home/blog/snapchat-lens-studio-staging-bug)
