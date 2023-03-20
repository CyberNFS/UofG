#include "TC74.h"

#define TC74_READ_TEMP 0    // Command to read temperature from the sensor
#define TC74_CONFIG 1       // Command to access the configuration register

TC74::TC74(I2C *i2c, uint8_t address)
    // Initialize the I2C object pointer and shift the address
    : _i2c(i2c), _address(address << 1) {
}

int8_t TC74::read() {
    char config_data = 0x00; // Wake up the sensor
    uint8_t config_command = TC74_CONFIG;
    // Write the configuration command to the sensor
    _i2c->write(_address, (const char *)&config_command, 1, true);
    // Write the configuration data (wake up) to the sensor
    _i2c->write(_address, &config_data, 1);

    ThisThread::sleep_for(100ms); // Give the sensor some time to wake up

    char data;
    uint8_t command = TC74_READ_TEMP;
    // Write the read temperature command to the sensor
    _i2c->write(_address, (const char *)&command, 1, true);
    // Read the temperature data from the sensor
    _i2c->read(_address, &data, 1);

    config_data = 0x80; // Put the sensor back to sleep
    // Write the configuration command to the sensor
    _i2c->write(_address, (const char *)&config_command, 1, true);
    // Write the configuration data (sleep) to the sensor
    _i2c->write(_address, &config_data, 1);

    return (int8_t)data;    // Return the temperature value as an int8_t
}

