#include "mbed.h"
#include "TextLCD.h"

// Pins
AnalogIn tmp37(A0);
PwmOut motor(D10);
InterruptIn user_override(D2);
TextLCD lcd(D3, D4, D5, D6, D7, D8, TextLCD::LCD16x2);  // rs, e, d4-d7, LCD type

// Constants
const float pwm_period = 20ms;  // 20 ms period

// Functions
float read_temperature() {
    float voltage = tmp37.read() * 3300.0; // Convert to mV
    return (voltage - 500.0) / 20.0;  // Convert to degrees Celsius
}

void override_motor() {
    motor.period(pwm_period);
    motor.write(0.5);  // 50% duty cycle
    ThisThread::sleep_for(5s);
    motor.write(0);  // Stop motor
}

int main() {
    // Set up the PWM output
    motor.period(pwm_period);

    // Set up the interrupt
    user_override.rise(&override_motor);

    while (1) {
        float temperature = read_temperature();
        lcd.cls();
        lcd.printf("Temp: %.1f C", temperature);

        if (temperature > 35) {
            float duty_cycle = (temperature - 35) / (100 - 35);
            motor.write(duty_cycle);
        } else {
            motor.write(0);
        }

        ThisThread::sleep_for(500ms);
    }
}
