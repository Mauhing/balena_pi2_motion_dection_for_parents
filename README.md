# Raspberry Pi Motion Detection (PIR Motion Sensor) with Balena

This repository demonstrates how to integrate a Raspberry Pi 2 with a motion sensor using the free Balena cloud service. This setup allows users to access motion detection logs from anywhere in the world, provided there is an internet connection.

![](/img/theme.png)

## Key Features

- **Remote Access to Motion History:** Track motion activity remotely from any location.
- **Ideal for Privacy-Conscious Monitoring:** Perfect for monitoring situations where cameras are not preferable, such as ensuring elderly family members are active at home without intruding on their privacy.
- **Minimalist Codebase:** Provides a streamlined, easy-to-understand codebase as a foundation for building your own motion detection software.

## Origins of the Project

Ever tried calling your parents only to find they've turned into undercover ninjas avoiding the phone? That's exactly what inspired this project. It turns out, motion sensors can be just the thing for those of us whose parents have mysteriously become phone-averse. No cameras, just a simple "Hey, they're moving about, all's well!" system.

## Getting Started

### Prerequisites

- **Hardware Required:**
  - Raspberry Pi with a minimum of 16GB SD card.
  - Motion sensor ([PIR Motion Sensor - Pyroelectric Infrared Sensor](https://www.digitalimpuls.no/adafruit/134257/pir-motion-sensor-pyroelectric-infrared-sensor))

- **Software Required:**
  - An account on Balena (free for up to 10 devices).
  - Balena OS installed on your SD card.

### Hardware Setup

Refer to the following image for guidance on connecting the components:
![](/img/setup.png)  

### Installation

1. **Set Up Balena OS:**
   - Follow the [Balena installation guide](https://www.balena.io/os/docs) to install Balena OS on your SD card. Use your custom fleet name during setup; in this example, we use `Motion_sensor`.

2. **Clone the Repository:**
   ```bash
   cd ~
   git clone [URL of this repo]
   cd pi2_motion_detection_balena
   ```

3. **Deploy the Application:**
   ```bash
   balena push Motion_sensor
   ```

### Usage

- After deploying the application to your Raspberry Pi via Balena:
  - Visit your Balena dashboard.
  - Perform a simple test by moving your hand in front of the motion sensor to verify functionality.
  - Adjust settings such as delay and sensitivity by referring to the [Adafruit PIR sensor guide](https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor/).
  - Motion logs are stored in `/usr/src/app/record`, sorted by day and time.

## Support

For any issues or questions, please submit an issue on the GitHub repository page.
