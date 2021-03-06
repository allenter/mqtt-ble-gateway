TOPIC_PREFIX = "home/MQTTtoBLE"             #MQTT prefix to identify this device
TOPIC_COMMAND = TOPIC_PREFIX + "/command"   #MQTT -> BLE
TOPIC_DEVICE = TOPIC_PREFIX + "/device"     #MQTT <- MQTT

MQTT_HOST = "your_mqtt_host"
MQTT_PORT = 1883
MQTT_KEEPALIVE = 60
MQTT_USERNAME = 'mqtt'
MQTT_PASSWORD = 'mqtt'

BLE_CONNECTION_TRIES = 3					#number of BLE error retries
