<p align="center"><img src="https://your-image-url.com/your-image.jpg"></p>

<p align="center">
    <a href="https://twitter.com/YOUR_TWITTER_HANDLE">
      <img src="https://img.shields.io/badge/-TWITTER-black?logo=twitter&style=for-the-badge">
    </a>
    &nbsp;
    <a href="https://yourwebsite.com/">
      <img src="https://img.shields.io/badge/-YOUR WEBSITE-black?logo=&style=for-the-badge">
    </a>
    &nbsp;
    <a href="https://yourblog.com/">
      <img src="https://img.shields.io/badge/-BLOG-black?logo=dialogflow&style=for-the-badge">
    </a>
</p>

<p align="center">
  <br>
  <b>Available in</b>
  <br>
  <img src="https://your-image-url.com/your-image.png">
</p>

<p>
  <a style="margin-right: 10px;" href="https://github.com/YOUR_USERNAME/YOUR_REPOSITORY#installation">
    <img src="https://dabuttonfactory.com/button.png?t=INSTALL&f=Open+Sans&ts=15&tc=000&hp=25&vp=10&c=5&bgt=unicolored&bgc=00e2ff">
  </a>
  <a style="margin-right: 10px;" href="https://github.com/YOUR_USERNAME/YOUR_REPOSITORY#usage">
    <img src="https://dabuttonfactory.com/button.png?t=USAGE&f=Open+Sans&ts=15&tc=000&hp=25&vp=10&c=5&bgt=unicolored&bgc=00e2ff">
  </a>
  <a href="https://github.com/YOUR_USERNAME/YOUR_REPOSITORY#demo">
    <img src="https://dabuttonfactory.com/button.png?t=DEMO&f=Open+Sans&ts=15&tc=000&hp=25&vp=10&c=5&bgt=unicolored&bgc=00e2ff">
  </a>
</p>

Concept behind YOUR_PROJECT_NAME is simple, just like we host phishing pages to get credentials why not host a fake page that requests your location like many popular location-based websites. Read more on the project page.

* Longitude
* Latitude
* Accuracy
* Altitude - Not always available
* Direction - Only available if the user is moving
* Speed - Only available if the user is moving

Along with Location Information, we also get **Device Information** without any permissions:

* Unique ID using Canvas Fingerprinting
* Device Model - Not always available
* Operating System
* Platform
* Number of CPU Cores - Approximate Results
* Amount of RAM - Approximate Results
* Screen Resolution
* GPU information
* Browser Name and Version
* Public IP Address
* Local IP Address
* Local Port

**Automatic IP Address Reconnaissance** is performed after the above information is received.

**This tool is a Proof of Concept and is for Educational Purposes Only, YOUR_PROJECT_NAME shows what data a malicious website can gather about you and your devices and why you should not click on random links.**

## How is this Different from IP GeoLocation

* Other tools and services offer IP Geolocation which is NOT accurate at all and does not give the location of the target instead it is the approximate location of the ISP.

* YOUR_PROJECT_NAME uses HTML API and gets Location Permission and then grabs Longitude and Latitude using GPS Hardware which is present in the device, so YOUR_PROJECT_NAME works best with Smartphones, if the GPS Hardware is not present or broken, it will not work accurately.

* Generally, if a user accepts location permission, the accuracy of the information received is **accurate to approximately 30 meters**

* Accuracy depends on multiple factors which you may or may not control such as:
  * Device - Won't work on laptops or phones which have broken GPS
  * Browser - Some browsers block JavaScripts
  * GPS Calibration - If GPS is not calibrated you may get inaccurate results and this is very common

## Templates

Available Templates:

* NearYou
* Google Drive (Suggested by @username)
* WhatsApp (Suggested by @username)
* Telegram
* Zoom (Made by @username)
* Google reCAPTCHA (Made by @username)

Create your own template! Steps to let you create your template are described in this [how-to](./createTemplate.md)

Once your template is ready, **do not forget to propose it to the community via a PR (pull request)**

## Tested On:

* Kali Linux
* BlackArch Linux
* Ubuntu
* Fedora
* Kali Nethunter
* Termux
* Parrot OS
* OSX - Monterey v.12.0.1

## Installation

### Kali Linux / Arch Linux / Ubuntu / Fedora / Parrot OS / Termux

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY/
chmod +x install.sh
./install.sh
```

### BlackArch Linux

```bash
sudo pacman -S YOUR_PACKAGE
```

### Docker

```bash
docker pull YOUR_DOCKER_IMAGE
```

### OSX
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY/
python3 your_script.py
```

In order to run in tunnel mode, install ngrok by running this command in the terminal:
```bash
brew install ngrok/ngrok/ngrok

ngrok http 8080