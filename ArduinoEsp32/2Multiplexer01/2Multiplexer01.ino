#define MUX1_S0 0                            
#define MUX1_S1 2                             
#define MUX1_S2 4                             
#define MUX1_S3 16                              
#define MUX1_SIG A0      

#define MUX2_S0 18                            
#define MUX2_S1 19                            
#define MUX2_S2 21                            
#define MUX2_S3 23                              
#define MUX2_SIG A3    

int sensorValues1[16];  // Array to hold sensor values for multiplexer 1
int sensorValues2[16];  // Array to hold sensor values for multiplexer 2

void setup() {
    pinMode(MUX1_S0, OUTPUT);                  
    pinMode(MUX1_S1, OUTPUT);                  
    pinMode(MUX1_S2, OUTPUT);                  
    pinMode(MUX1_S3, OUTPUT);                  
    pinMode(MUX1_SIG, INPUT);                  
  
    pinMode(MUX2_S0, OUTPUT);                  
    pinMode(MUX2_S1, OUTPUT);                  
    pinMode(MUX2_S2, OUTPUT);                  
    pinMode(MUX2_S3, OUTPUT);                  
    pinMode(MUX2_SIG, INPUT);                  
  
    Serial.begin(9600);                   
}

void loop() {
    // Read from Multiplexer 1
    readMultiplexer(MUX1_S0, MUX1_S1, MUX1_S2, MUX1_S3, MUX1_SIG, sensorValues1);

    // Read from Multiplexer 2
    readMultiplexer(MUX2_S0, MUX2_S1, MUX2_S2, MUX2_S3, MUX2_SIG, sensorValues2);

    for (int i = 0; i < 16; i++) {
        Serial.print(4095 - sensorValues1[i]);
        Serial.print(" ");
    }
    

    // Print sensor values for multiplexer 2
    for (int i = 0; i < 16; i++) {
        Serial.print(4095 - sensorValues2[i]);
        Serial.print(" ");

    }
    Serial.println("");
    delay(1000);                          
}

void readMultiplexer(int s0, int s1, int s2, int s3, int sig, int sensorValues[]) {
    int max = 0;
    for (int channel = 0; channel < 16; channel++) {
        selectChannel(channel, s0, s1, s2, s3);
        for (int i = 0; i < 10; i++) {
            int value = analogRead(sig);
            if (value > max) {
                max = value;
            }
            delay(1);
        }
        sensorValues[channel] = max;
        max = 0;
    }
}

void selectChannel(int channel, int s0, int s1, int s2, int s3) {
    digitalWrite(s0, channel & 1 ? HIGH : LOW);
    digitalWrite(s1, channel & 2 ? HIGH : LOW);
    digitalWrite(s2, channel & 4 ? HIGH : LOW);
    digitalWrite(s3, channel & 8 ? HIGH : LOW);
}
