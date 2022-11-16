# include <WiFi.h>
# include <WebServer.h>

const char* ssid = "Internet_Beno";
const char* password = "Beno12345";
const char* html_page = "";
const int ledd = 5;

/* Put IP Address details */
IPAddress ip(192,168,1,106);
IPAddress gateway(192,168,1,1);
IPAddress subnet(255,255,255,0);

// creamos el servidor e indicamos e puerto
WebServer server(80);

//ip?led=0/1
void handleRoot(){

  //devolvemos el argumento del parametro led en un string
  String ledstate;
  ledstate = server.arg("led");
  // visualizamos 
  Serial.print("Argumento Recibido: ");
  Serial.println(ledstate);

  // Ahora definimos lo que va a pasar cuando sea 1 o cuando sea 0
  if(ledstate == "1"){
    digitalWrite(ledd, HIGH);
  }
  if(ledstate == "0"){
    digitalWrite(ledd, LOW);
  }
// el primero, el estado de la comunicacion, luego el tipo de dato, y luego el dato
  //server.send
  server.send(200, "text/html",html_page);
}

void setup() {
  Serial.begin(115200);
  pinMode(ledd, OUTPUT);
  delay(50);
  // con esta funcion creamos la red wifi
  WiFi.softAP(ssid, password);
  WiFi.softAPConfig(ip, gateway, subnet);
  delay(100);
  Serial.println("WiFi listo !!");
  

  Serial.print("Nombre de mi red esp32: ");
  Serial.println(ssid);
  Serial.print("La ip es: ");
  Serial.println(ip);

  server.on("/", handleRoot);

  // iniciamos el server 
  server.begin();
  Serial.println("Servidor HTTP iniciado");

}

void loop() {
   server.handleClient();
   delay(5000);
}
