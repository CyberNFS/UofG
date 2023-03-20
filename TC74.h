#ifndef TC74_H
#define TC74_H

#include "mbed.h"

class TC74 {
public:
    // Constructor: takes a pointer to an I2C object and an optional I2C address (default is 0x48)
    TC74(I2C *i2c, uint8_t address = 0x48);
    // Method to read the temperature value from the sensor
    int8_t read();

private:
    I2C *_i2c; // Pointer to the I2C object used for communication
    uint8_t _address; // I2C address of the sensor
};

#endif // TC74_H
