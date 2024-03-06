#include <BLEDevice.h>
#include <BLEUtils.h>
#include <BLEScan.h>

BLEScan* Blemon;

class CallbackBLE : public BLEAdvertisedDeviceCallbacks {
    void onResult(BLEAdvertisedDevice perangkat) {
        String data = perangkat.getAddress().toString().c_str() + ":" + perangkat.getName().c_str() + ":" + String(perangkat.getRSSI()); Serial.println(data);
    }
};

void setup() {
  Serial.begin(115200); BLEDevice::init(""); Blemon = BLEDevice::getScan(); Blemon->setAdvertisedDeviceCallbacks(new CallbackBLE()); Blemon->setActiveScan(true); Blemon->start(0);
}

void loop() {
  delay(1000);
}