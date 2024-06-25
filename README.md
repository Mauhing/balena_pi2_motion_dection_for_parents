# Raspberry Pi Motion Detection with Balena

This repository demonstrates how to integrate a Raspberry Pi 2 with a motion sensor using the free Balena cloud service. This setup allows users to access motion detection logs from anywhere in the world, provided there is an internet connection.

## Key Features

- **Remote Access to Motion History:** Track motion activity remotely from any location.
- **Ideal for Privacy-Conscious Monitoring:** Perfect for monitoring when cameras are not preferable, like checking if elderly family members are active at home without intruding on their privacy.

## Getting Started

### Prerequisites

- **Hardware Required:**
  - Raspberry Pi with a minimum of 16GB SD card.
  - Motion sensor ([PIR Motion Sensor - Pyroelectric Infrared Sensor](https://www.digitalimpuls.no/adafruit/134257/pir-motion-sensor-pyroelectric-infrared-sensor))

- **Software Required:**
  - An account on Balena (free for up to 10 devices).
  - Balena OS installed on your SD card.

### Installation

1. **Set Up Balena OS:**
   - Follow the [Balena installation guide](https://www.balena.io/os/docs) to install Balena OS on your SD card. Use your custom fleet name during setup; in this example, we use `Motion_sensor`.

2. **Clone the Repository:**
   ```bash
   cd ~
   git clone [URL of this repo]
   ```

3. **Deploy the Application:**
   ```bash
   balena push Motion_sensor
   ```

### Usage

- After deploying the application to your Raspberry Pi via Balena:
  - Visit your Balena dashboard.
  - Perform a simple test by moving your hand in front of the motion sensor to verify functionality.
  - Motion logs can be found in `/usr/src/app/record`, sorted by day and time.

## Support

For any issues or questions, please submit an issue on the GitHub repository page.
