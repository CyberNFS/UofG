#ifndef TC74_H
#define TC74_H

#include "mbed.h"

class TC74 {
public:
    TC74(I2C *i2c, uint8_t address = 0x48);  // Default I2C address is 0x48
    int8_t read();

private:
    I2C *_i2c;
    uint8_t _address;
};

#endif // TC74_H
