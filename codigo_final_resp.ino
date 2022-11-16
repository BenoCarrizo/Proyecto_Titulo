    /* -------------------- LIBRERIAS ------------------*/
  /* CALL AND SMS */
#include <SoftwareSerial.h>
#include <Wire.h>


  /* RELOJ */

#include <ThreeWire.h>  
#include <RtcDS1302.h>

  /* CLIENTE WIFI */

#include <WiFi.h>
#include <WiFiClient.h> // con esta inicializamos get 
#include <HTTPClient.h> // maneja las peticiones

    /* -------------------- DEFINES AND FUNCTIONS ------------------*/
  
  /* CALL AND SMS */

String TARGET =  "56942315588";  // numero de o los parientes
String smsMessage = "";
// Configure TinyGSM library para SIM800L
#define TINY_GSM_MODEM_SIM800      // Modem is SIM800
#define TINY_GSM_RX_BUFFER   1024  // Set RX buffer to 1Kb
#include <TinyGsmClient.h>

// TTGO T-Call pins
#define MODEM_RST            5
#define MODEM_PWKEY          4
#define MODEM_POWER_ON       23
#define MODEM_RX             27
#define MODEM_TX             26
#define I2C_SDA              21
#define I2C_SCL              22

//Se definie monitor serial para sim800l para enviarle los comandos AT  a 115200 baudios
#define SerialAT  Serial1

// Se definne la la consula serial para enviar los prints de pantalla
#define DUMP_AT_COMMANDS Serial

#ifdef DUMP_AT_COMMANDS
#include <StreamDebugger.h>
  StreamDebugger debugger(SerialAT, Serial);
  TinyGsm modem(debugger);
#else
  TinyGsm modem(SerialAT);
#endif


#define IP5306_ADDR          0x75
#define IP5306_REG_SYS_CTL0  0x00

bool setPowerBoostKeepOn(int en){
  Wire.beginTransmission(IP5306_ADDR);
  Wire.write(IP5306_REG_SYS_CTL0);
  if (en) {
    Wire.write(0x37); // Set bit1: 1 enable 0 disable boost keep on
  } else {
    Wire.write(0x35); // 0x37 is default reg value
  }
  return Wire.endTransmission() == 0;
}

// Funcion para envir MSM 
void sms_func(int instr){
  //Serial.println("sms func");
  // To send an SMS, call modem.sendSMS(SMS_TARGET, smsMessage)
  switch(instr){
  case 1:
    smsMessage = "Rapido, el abuelito esta en peligro!!";
    break;
  case 2:
    smsMessage = "El abuelito esta triste, deberias llamarlo";
    break;
  case 3:
    smsMessage = "Te has levantado en la noche, te recomiendo no tomar agua 4 horas antes de irte a acostar. SI aun asi te le vantas, te recomiendo ir al medico.";
    break;
  case 4: 
    smsMessage = "Tu abuelito esta triste o angustiado, podrias llamarl@, hacer una video llamada, o ir a comer con el o ella ";
    break;
  default:
    break;
  
    }
  
  String tardet = "+56942315588"; //+ TARGET;
  if(modem.sendSMS(tardet, smsMessage)){
    Serial.println(smsMessage);
  }
  else{
    //luz de falla
    Serial.println("SMS failed to send");
  }
}
// funcion para corlgalla llamada
void colgar(){
  modem.sendAT("H");
  delay(100);
  }
// funcion para llamar
void call_func(){
  // S e enviar los comando AT para configurar el canal, microfono y el speaker, y se envia el numero al que se llamara
  String target = "D+" + TARGET+ ";";
  modem.sendAT("+CLVL=100");
  delay(100);
  modem.sendAT("+CMIC=1,15");
  delay(100);
  modem.sendAT("+CAAS=0");
  delay(100);
  modem.sendAT("+CHF=0,1");
  delay(100);
  modem.sendAT("D+56942315588;");
  delay(100);
}

  /* RELOJ AND SENSOR ULTRASONIDO */

// Se inicializan los pins para el RTC
ThreeWire myWire(25,18,19); // IO/DATA(5), SCLK, (19)CE/RST
RtcDS1302<ThreeWire> Rtc(myWire);

// Se inicia una nueva tarea, que se ejecutara en paralelo al resto del codigo.
xTaskHandle Task2;

// Se inicializa el estado del rele (el cual activa o descativa el ultrasonido para la nicturia), su pin, los pines de las luces de aviso y los pines del sensonr ultrasonico.
// La duracion y distance son parametros del ultrasonido para medir distancia
bool estado  = false;
const int rele = 15;
const int entro = 33;
const int wifii = 32;
#define echoPin 13 // attach pin D2 Arduino to pin Echo of HC-SR04     modd
#define trigPin 14 //attach pin D3 Arduino to pin Trig of HC-SR04      modd
// defines variables
long duration; // variable for the duration of sound wave travel
int distance = 0; // variable for the distance measurement

// funcion paa medir distancia que se ejecutara en paralelo al codigo principal
// su funcion sera detectar la nicturia con el sensor de ultrasonido
void rele_ultsonido(void *parameter){
  // se inicializa el contador que se encarga de contar cuantas veces se  detecto movimiento en la noche
  float cont = 0.0;
  // guarda valor de distancia anterior
  float distancia;
  // medicion y medicion1 se usaran para detectar los cambios de distancia
  // enviar mensaje informa si se debe o no enviar un mensaje en caso de nicturia
  float medicion = 0.0;
  float medicion1 = 0.0;
  bool enviar_msm = false;
  for(;;){
    // Con "now" obtenemos la hora, la cual activara o desactivara el rele y el ultrasonido
    RtcDateTime now = Rtc.GetDateTime();
  
    switch(now.Second()){
      //A modo de demostracion:
      // Cuando el parametro Second sea 10, se activara el rele, iniciando la funcion del ultrasonido
      case 10:
      Serial.print(now.Hour());     // funcion que obtiene la hora de la fecha completa
      Serial.print(":");        // caracter dos puntos como separador
      Serial.print(now.Minute());     // funcion que obtiene los minutos de la fecha completa
      Serial.print(":");        // caracter dos puntos como separador
      Serial.println(now.Second());   // funcion que obtiene los segundos de la fecha completa
      estado = true;
      digitalWrite(rele, HIGH);
        break;
    // Cuando Second sea igual a 30, se desactivara el rele, el ultrasonido y las variables de medicion.
    // Tambien se envia mensaje con 
    case 30:
        if(cont > 4){
          enviar_msm = true;
          }
        
        estado = false;
        digitalWrite(rele, LOW);
        cont = 0.0;
        medicion = 0.0;
        medicion1 = 0.0;
        break;
     // Aca se le enviara un mensaje al abuelito o parantie a una hora determinada en la tarde
     // con el fin de tomar medidas en caso de nicturia
     case 40:
      if (enviar_msm == true){
        sms_func(3);
        enviar_msm = false;
        }
       break;
    }
    // Dependiendo del estado, se activa la funcion del ultrasonido
    if(estado == true){
      // Clears the trigPin condition
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin HIGH (ACTIVE) for 10 microseconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  // Calculating the distance
  distance = duration * 0.034 / 2; // Speed of sound wave divided by 2 (go and back)
  medicion = distancia - distance;
  medicion1 = distance - distancia;
  // Si la diferencia entre las mediciones mayor a 30 cm, entonces se dice que alguien paso
  // se debe tomar en cuenta que cuando se inicie, al estar los valores en cero, entrara al if
  // por eso el contador al princio tendra falsas "pasadas"
  if (medicion1 > 30){
    cont ++;
    }else if  (medicion > 30){
    cont ++;
    }
  distancia = distance;
  delay(1000);

      }
    
  vTaskDelay(10);
  }
}


  /* WIFI CLEINT */

// Aca iniciamos la comunicacion wifi con el sonoff el cual es un servidor. Nos cominucamos por http como clientes.
const char* ssid = "Internet_Beno";
const char* password = "Beno12345";

const char* host= "http://192.168.1.106"; 

String dato;

void send_respuesta(String link){
  // creamos dos objetos, nombre del client y un objeto http
  WiFiClient client_1;
  HTTPClient http;
  
  
      http.begin(client_1, link);
      int httpCode = http.GET();
  
    //finalizamos 
       http.end();
  }

void setup() {
  // se inicia el monitor serie
  Serial.begin(115200);
  /* CALL AND SMS SETUP*/
  // Se mantiene la energia cuando se ejecuta desde la bateria
  Wire.begin(I2C_SDA, I2C_SCL);
  bool isOk = setPowerBoostKeepOn(1);
  //Serial.println(String("IP5306 KeepOn ") + (isOk ? "OK" : "FAIL"));

  // se inicia el modulo sim800l
  pinMode(MODEM_PWKEY, OUTPUT);
  pinMode(MODEM_RST, OUTPUT);
  pinMode(MODEM_POWER_ON, OUTPUT);
  digitalWrite(MODEM_PWKEY, LOW);
  digitalWrite(MODEM_RST, HIGH);
  digitalWrite(MODEM_POWER_ON, HIGH);

  // Se establecen los baudios del modulo GSMS y los pines UART
  SerialAT.begin(115200, SERIAL_8N1, MODEM_TX, MODEM_RX);
  delay(3000);

  // Se reinicia el modulo sim800l
  modem.restart();
  
  /* RELOJ SETUP*/
  
  pinMode(rele,OUTPUT);
  //En caso que se pierda la hora del RTC, se puede recuperar con el codigo que esta comentado
  // se inicializa el RTC y los pines del ultrasonido

    //Serial.print("compiled: "); // pasar fecha por pc 
    //Serial.print(__DATE__); // pasar fecha por pc 
    //Serial.println(__TIME__); // pasar fecha por pc 
    Rtc.Begin();

    //RtcDateTime compiled = RtcDateTime(__DATE__, __TIME__); // pasar fecha por pc 
    //Serial.println();// pasar fecha por pc 

    //RtcDateTime now = Rtc.GetDateTime();// pasar fecha por pc 
    //if (now < compiled) // pasar fecha por pc 
    //{
        //Serial.println("RTC is older than compile time!  (Updating DateTime)");// pasar fecha por pc 
        //Rtc.SetDateTime(compiled);// pasar fecha por pc 
    //}
    pinMode(trigPin, OUTPUT); // Sets the trigPin as an OUTPUT         modd
    pinMode(echoPin, INPUT); // Sets the echoPin as an INPUT           modd
//    Serial.println("Ultrasonic Sensor HC-SR04 Test"); // print some text in Serial Monitor 

// se inicializa la tarea en segundo plano, pasando los valores de la funcion, nombre de la funcion,
// el tamaño de la pila, el parametro de la funcion que se quiere pasar, , nombre de la tarea, nucleo en que se
// ejecuta la tarea, y nuclo que tendra prioridad de tareas. 
xTaskCreatePinnedToCore(
    rele_ultsonido,
    "Task_2",
    10000,
    NULL,
    1,
    &Task2,
    0);

  /* WIFI CLEINT SETUP*/
  //Serial.println("\nWiFi station setting");
  WiFi.mode(WIFI_STA); // STA = estacion; AP = access point; AP_STA = access ponit y estacion al mismo tiempo
  WiFi.begin(ssid, password); // iniciamos 
  // WiFi.status devuleve el estado de la coneccion (conectado o desconectado)
  // mientras el estado no sea conectado, se repite el bucle
  while(WiFi.status() != WL_CONNECTED){
    // mientras no se conecta con el sonoff se mantendra la luz de alerta encendida 
    digitalWrite(wifii, HIGH);
    delay(500);
  }
  // si se conecto, se apaga la luz
  digitalWrite(wifii, LOW);
  
  
  //Leds wifi y entro
  pinMode(entro, OUTPUT);
  pinMode(wifii, OUTPUT);
}

 //Aca se esperaran las ordenes que se ejectaran del monitor serial (pc o jetson)
 // con "a", envia mensaje de alerta de peligro y llama al familiar
 // con "b" indica estado de animo del abuelito, para que lo llamen
 // con "h" y "g" indica la hora y la fecha
 // con "d" y "e" se enciende y apaga la luz
 // con "f" se cuenga la llamada
 
void loop() {
  //Serial.println("ENTRO...");
  // cuando este todo OK encendera la luz que indidca que esta listo para recibir ordenes
  digitalWrite(entro, HIGH);
  
  /* WIFI CLEINT SETUP LOOP*/
  // creamos dos objetos, nombre del client y un objeto http
  WiFiClient client_1;
  HTTPClient http;
  String getData, link;
  
  /* RELOJ LOOP */
  RtcDateTime now = Rtc.GetDateTime();
  
 
 while(Serial.available()== 0){
  }
  char action = Serial.read();
  //Serial.println(action);
  switch(action){
    
    case 'a':
       digitalWrite(entro, LOW);
       sms_func(1);
       delay(500);
       call_func();
       break;
       
    case 'b':
      digitalWrite(entro, LOW);
      sms_func(2);
      break;

     case 'h':
      digitalWrite(entro, LOW);
      Serial.print(now.Hour());     // funcion que obtiene la hora de la fecha completa
      Serial.print(":");        // caracter dos puntos como separador
      Serial.print(now.Minute());     // funcion que obtiene los minutos de la fecha completa
      Serial.print(":");        // caracter dos puntos como separador
      Serial.println(now.Second());   // funcion que obtiene los segundos de la fecha completa
      break;
      
    case 'g':
      digitalWrite(entro, LOW);
      Serial.print(now.Day());
      Serial.print("/");
      Serial.print(now.Month());      // funcion que obtiene el mes de la fecha completa
      Serial.print("/");        // caracter barra como separador
      Serial.println(now.Year());     // funcion que obtiene el año de la fecha completa
      //Serial.println(" ");        // caracter espacio en blanco como separador      
      break;    
      
    case 'd':
      //Serial.println("Entro a 1");
      digitalWrite(entro, LOW);
      getData = "/?led=1";
      link = host + getData;
      send_respuesta(link);
      break;
      
    case 'e':
      //Serial.println("Entro a 0");
      digitalWrite(entro, LOW);
      getData = "/?led=0";
      link = host + getData;
      send_respuesta(link);
      break;
      
    case 'f':
      digitalWrite(entro, LOW);
      colgar();
      break;
      
    default:
      break;
       
    }
    
  delay(100); 
}
