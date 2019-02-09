
int array[6] = {13, 12, 11, 10, 9, 8};
int array2[6] = {8, 9, 10, 11, 12, 13};
int timeDelay = 40;
int button = 2;
int pressed;
void setup() 
{
  // put your setup code here, to run once:
pinMode(13,OUTPUT);
pinMode(12, OUTPUT);
pinMode(11, OUTPUT);
pinMode(10, OUTPUT);
pinMode(9, OUTPUT);
pinMode(8, OUTPUT);
pinMode(7, OUTPUT);


}

void loop() {
  // put your main code here, to run repeatedly:
 digitalWrite (button, HIGH);
for (int i = 0; i<6; i++)
{
digitalWrite(array[i], HIGH);
delay(timeDelay);
pressed = digitalRead(button);
if (pressed == LOW && i == 5)
{
  timeDelay /= 2;
}

digitalWrite(array[i], LOW);
delay(timeDelay);}

for (int i = 0; i<6; i++)
{digitalWrite(array2[i], HIGH);
delay(timeDelay);
digitalWrite(array2[i], LOW);
delay(timeDelay);}


}
