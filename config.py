# enviro config file

# you may edit this file by hand but if you enter provisioning mode
# then the file will be automatically overwritten with new details

provisioned = True

# enter a nickname for this board   ### ask Jessica for this info
nickname = ''

# network access details    ### ask Jessica for this info
wifi_ssid = ''
wifi_password = ''

# how often to wake up and take a reading (in minutes)
reading_frequency = 180

# how often to trigger a resync of the onboard RTC (in hours)
resync_frequency = 168

# where to upload to ("http", "mqtt", "adafruit_io", "influxdb")
destination = 'mqtt'

# how often to upload data (number of cached readings)
upload_frequency = 1

# web hook settings
custom_http_url = ''
custom_http_username = ''
custom_http_password = ''

# mqtt broker settings                  ### ask Jessica for this info
mqtt_broker_address = ''
mqtt_broker_username = ''
mqtt_broker_password = ''
# mqtt broker if using local SSL
mqtt_broker_ca_file = None

# adafruit ui settings
adafruit_io_username = ''
adafruit_io_key = ''

# influxdb settings
influxdb_org = ''
influxdb_url = ''
influxdb_token = ''
influxdb_bucket = ''



# grow specific settings
auto_water = False
moisture_target_a = 50
moisture_target_b = 50
moisture_target_c = 50

# compensate for usb power
usb_power_temperature_offset = 4.5
