# Module Assembly Center Automatic Particulate Counter Setup

## Parts Needed
For automatic particulate counts, a PMSA003I sensor and microprocessor with wifi are needed at a bare minimum. The notes below describe the specific setup at CMU.
* **Enviro Urban** from [Digikey PN 1778-PIM629-ND](https://www.digikey.com/en/products/detail/pimoroni-ltd/PIM629/16716837)
    * Includes BME280 (humidity and temperature) and  PMSA003I (particulate counter) sensors already connected to a Raspberry Pi Pico W.
    * Also includes a MEMS microphone to monitor sound. However, this capability is not utilized in this specific application.
    * Requires **USB micro-B cable** for initial setup.
* **JST-PH connector** from [Amazon PN B07NWD5NTN](https://www.amazon.com/Upgraded-Connector-Battery-Inductrix-Eachine/dp/B07NWD5NTN/) and **5V source** [Amazon PN B0BV64MHY6](https://www.amazon.com/MTYTOT-Adapter-100V-240V-Converter-Security/dp/B0BV64MHY6/) 
    * Several vendors offer these parts
    * Provides long term power to the Enviro Urban 
    * AA battery pack with  JST-PH connector can be used instead
* **Raspberry Pi 4**
    * Several vendors offer this, RPi 3 or 5 may work as well
    * Raspbian V11 Bullseye OS used, others may work
    * Serves as a broker between sensor readings (publisher) and user asking for readings (subscriber)


## Useful Links
* [How MQTT works and Mosquitto installation](https://randomnerdtutorials.com/how-to-install-mosquitto-broker-on-raspberry-pi/)
* [Enviro Urban datasheet](https://shop.pimoroni.com/products/enviro-urban?variant=40056508252243)
* [Enviro Urban documentation on GitHub](https://github.com/pimoroni/enviro/blob/main/documentation/getting-started.md)
* [Enviro Urban troubleshooting](https://learn.pimoroni.com/article/getting-started-with-enviro#troubleshooting)


## Raspberry Pi Broker Setup
* [Follow instructions here to install Mosquitto on the RPi broker
](https://randomnerdtutorials.com/how-to-install-mosquitto-broker-on-raspberry-pi/) 
* [Follow these instructions to create a topic](https://randomnerdtutorials.com/testing-mosquitto-broker-and-client-on-raspbbery-pi/)
    * In this case, we use *module-assembly* as a topic
* Ensure that the RPi is on a network that can be accessed by the Enviro Urban as well
* Get the RPi wlan IP address

## Enviro Urban Setup
* Follow instructions in the Enviro Urban GitHub link above to get started
* Connect the Enviro Urban to a computer via Micro-B cable
* [Install Thonny on this computer](https://thonny.org/)
* See the troubleshooting link for manually configuring the Enviro Urban files
* The following files were modified:
    * *urban.py* under enviro --> boards
        * Use particles per liters/cubic meters
        * Comment out noise and pressure measurements
    * *config.py*
        * initial setup can be adjusted as needed in this file, such as frequency of readings
        * **NEVER SHARE NETWORK INFORMATION ON GITHUB!**
    * *helpers.py* under boards - timestamps adjusted for timezone
    * *logging.py* under phew - timestamps adjusted for timezone
* After modifying the files, run *main.py* in Thonny. Verify valid measurements.
* Move the Enviro Urban to the 5V source.
* The RPi can now receive the sensor readings from the Enviro Urban.

## What's next?
* Send readings from RPi to phone, email, etc. Consider Node-RED on the RPi.
* Implement test stand dark box humidity sensor onto the same system. 
