#include "mbed.h"
#include "TextLCD.h"
#include "TC74.h"

TextLCD lcd(A1, A0, D9, D10, D11, D12, TextLCD::LCD16x2);
I2C i2c(D4, D5); // SDA, SCL
TC74 tc74(&i2c); // Pass the address of the I2C object


int main() {
    i2c.frequency(100000); // Set the I2C frequency to 100kHz
    while (1) {
        float temperature = tc74.read();

        lcd.cls();
        lcd.locate(0, 0);
        lcd.printf("Temp: %d C", (int)temperature);

        // Set the PWM duty cycle based on the temperature
        // Implement your PWM control logic here

        ThisThread::sleep_for(1000ms);
    }
}
