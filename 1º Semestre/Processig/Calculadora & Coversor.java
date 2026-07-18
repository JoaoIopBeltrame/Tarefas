// variaveis 
int tela = 0;
String visor = "";
String visorConv = "";
float num1 = 0;
char operacao = ' ';

// constantes design
final int LARGURA_BOTAO_MENU = 500;
final int ALTURA_BOTAO_MENU = 60;
final int X_BOTAO_MENU = 350;

// config calculadora
final int TAM_BOTAO_CALC = 80;
final float GAP_X_CALC = 25.5;
final int GAP_Y_CALC = 10;
final int INICIO_X_CALC = 402;
final int INICIO_Y_CALC = 160;
final String BOTOES_CALC = "C±%/789X456-123+ 0,=";

// config teclado conversor
final int TAM_BOTAO_CONV = 75;
final float GAP_X_CONV = 15;
final int GAP_Y_CONV = 10;
final int INICIO_X_CONV = 420;
final int INICIO_Y_CONV = 350;
final String BOTOES_CONV = "C±,=789 456 123  0  ";

// config inicial
void setup() {
  size(1200, 890);
  textAlign(CENTER, CENTER);
  textSize(23);
}

// loop render interface
void draw() {
  switch (tela) {
    case 0: desenhaMenu(); break;
    case 1: desenhaCalculadora(); break;
    case 2: desenhaMenuConversor(); break;
    case 3: desenhaTelaConversao("Celsius -----> Fahrenheit"); break;
    case 4: desenhaTelaConversao("Celsius -----> Kelvin"); break;
    case 5: desenhaTelaConversao("Fahrenheit -----> Celsius"); break;
    case 6: desenhaTelaConversao("Fahrenheit -----> Kelvin"); break;
    case 7: desenhaMenuDistancia(); break;
    case 8: desenhaTelaDistancia("Metro -----> Quilômetro"); break;
    case 9: desenhaTelaDistancia("Metro -----> Centímetro"); break;
    case 10: desenhaTelaDistancia("Quilômetro -----> Metro"); break;
    case 11: desenhaTelaDistancia("Quilômetro -----> Centímetro"); break;
    case 12: desenhaTelaDistancia("Centímetro -----> Metro"); break;
    case 13: desenhaTelaDistancia("Centímetro -----> Quilômetro"); break;
  }
}

// detecçao de cliques
void mousePressed() {
  switch (tela) {
    case 0: cliqueMenu(); break;
    case 1: cliqueCalculadora(); break;
    case 2: cliqueMenuConversor(); break;
    case 3: case 4: case 5: case 6:
      cliqueTelaConversao();
      break;
    case 7: cliqueMenuDistancia(); break;
    case 8: case 9: case 10: case 11: case 12: case 13:
      cliqueTelaDistancia();
      break;
  }
}

// === FUNDOS DECORATIVOS ===

void gradiente(color cor1, color cor2) {
  noStroke();
  for (int y = 0; y < height; y++) {
    float t = map(y, 0, height, 0, 1);
    color c = lerpColor(cor1, cor2, t);
    stroke(c);
    line(0, y, width, y);
  }
  noStroke();
}

void circulosDecorativos(color cor) {
  noStroke();
  fill(red(cor), green(cor), blue(cor), 40);
  circle(150, 800, 250);
  circle(1050, 100, 200);
  fill(red(cor), green(cor), blue(cor), 25);
  circle(900, 750, 350);
  circle(250, 200, 180);
  noStroke();
}

// === RENDERIZAÇÃO ===

void desenhaMenu() {
  gradiente(color(180, 230, 210), color(140, 200, 230));
  circulosDecorativos(color(255, 255, 255));
  
  fill(40, 60, 80);
  textSize(48);
  text("Menu Principal", 600, 200);
  textSize(23);

  fill(140, 233, 123);
  rect(X_BOTAO_MENU, 320, LARGURA_BOTAO_MENU, ALTURA_BOTAO_MENU, 100);
  fill(0);
  text("Calculadora", 600, 350);

  fill(233, 140, 123);
  rect(X_BOTAO_MENU, 450, LARGURA_BOTAO_MENU, ALTURA_BOTAO_MENU, 100);
  fill(0);
  text("Conversor de Temperatura", 600, 480);
  
  fill(180, 200, 255);
  rect(X_BOTAO_MENU, 580, LARGURA_BOTAO_MENU, ALTURA_BOTAO_MENU, 100);
  fill(0);
  text("Conversor de Distância", 600, 610);
}

void desenhaCalculadora() {
  gradiente(color(40, 50, 80), color(80, 100, 150));
  circulosDecorativos(color(255, 255, 255));

  fill(240, 245, 250);
  rect(400, 90, 400, 60, 10);
  fill(30, 30, 50);
  textSize(32);
  textAlign(RIGHT, CENTER);
  text(visor, 400 + 400 - 10, 90 + 30);

  textAlign(CENTER, CENTER);
  textSize(23);

  for (int j = 0; j < 5; j++) {
    for (int i = 0; i < 4; i++) {
      float x = INICIO_X_CALC + i * (TAM_BOTAO_CALC + GAP_X_CALC);
      float y = INICIO_Y_CALC + j * (TAM_BOTAO_CALC + GAP_Y_CALC);
      char letra = BOTOES_CALC.charAt(j * 4 + i);

      if (isOperador(letra)) {
        fill(255, 150, 0);
      } else {
        fill(100, 110, 130);
      }

      rect(x, y, TAM_BOTAO_CALC, TAM_BOTAO_CALC, 10);
      fill(255);
      text(letra, x + TAM_BOTAO_CALC/2, y + TAM_BOTAO_CALC/2);
    }
  }
  desenhaVoltar();
}

void desenhaMenuConversor() {
  gradiente(color(255, 220, 200), color(255, 180, 200));
  circulosDecorativos(color(255, 200, 150));

  fill(60, 30, 40);
  textSize(38);
  text("Conversor de Temperatura", 600, 110);
  textSize(23);

  desenhaBotaoConversor(180, color(255, 200, 200), "Celsius -----> Fahrenheit");
  desenhaBotaoConversor(280, color(255, 220, 200), "Celsius -----> Kelvin");
  desenhaBotaoConversor(380, color(255, 240, 200), "Fahrenheit -----> Celsius");
  desenhaBotaoConversor(480, color(220, 255, 200), "Fahrenheit -----> Kelvin");

  desenhaVoltar();
}

void desenhaMenuDistancia() {
  gradiente(color(200, 220, 255), color(160, 190, 240));
  circulosDecorativos(color(180, 200, 255));

  fill(20, 40, 80);
  textSize(38);
  text("Conversor de Distância", 600, 100);
  textSize(23);

  desenhaBotaoConversor(150, color(200, 230, 255), "Metro -----> Quilômetro");
  desenhaBotaoConversor(230, color(210, 230, 255), "Metro -----> Centímetro");
  desenhaBotaoConversor(310, color(220, 240, 255), "Quilômetro -----> Metro");
  desenhaBotaoConversor(390, color(200, 240, 245), "Quilômetro -----> Centímetro");
  desenhaBotaoConversor(470, color(220, 240, 230), "Centímetro -----> Metro");
  desenhaBotaoConversor(550, color(230, 240, 220), "Centímetro -----> Quilômetro");

  desenhaVoltar();
}

void desenhaTelaConversao(String titulo) {
  color corTopo, corBaixo;
  switch (tela) {
    case 3: corTopo = color(170, 210, 240); corBaixo = color(255, 200, 150); break;
    case 4: corTopo = color(170, 210, 240); corBaixo = color(120, 150, 200); break;
    case 5: corTopo = color(255, 200, 150); corBaixo = color(170, 210, 240); break;
    case 6: corTopo = color(255, 200, 150); corBaixo = color(120, 150, 200); break;
    default: corTopo = color(245); corBaixo = color(220);
  }
  gradiente(corTopo, corBaixo);
  circulosDecorativos(color(255, 255, 255));

  desenhaInterfaceConversao(titulo, converteTemperatura(visorConvSafe(), tela));
}

void desenhaTelaDistancia(String titulo) {
  color corTopo, corBaixo;
  switch (tela) {
    case 8:  corTopo = color(200, 230, 255); corBaixo = color(150, 200, 250); break;
    case 9:  corTopo = color(210, 240, 255); corBaixo = color(170, 220, 250); break;
    case 10: corTopo = color(180, 220, 250); corBaixo = color(220, 240, 255); break;
    case 11: corTopo = color(190, 230, 250); corBaixo = color(220, 240, 240); break;
    case 12: corTopo = color(220, 240, 230); corBaixo = color(200, 230, 255); break;
    case 13: corTopo = color(230, 240, 220); corBaixo = color(180, 220, 250); break;
    default: corTopo = color(245); corBaixo = color(220);
  }
  gradiente(corTopo, corBaixo);
  circulosDecorativos(color(255, 255, 255));

  desenhaInterfaceConversao(titulo, converteDistancia(visorConvSafe(), tela));
}

// função compartilhada para desenhar a interface de conversão (entrada + resultado + teclado)
void desenhaInterfaceConversao(String titulo, float resultado) {
  // titulo
  fill(40, 30, 50);
  textSize(28);
  text(titulo, 600, 80);
  textSize(23);

  // visor de entrada
  fill(40, 30, 50);
  textSize(20);
  text("Valor de entrada:", 600, 145);
  textSize(23);
  fill(245, 250, 255);
  rect(400, 160, 400, 60, 10);
  fill(0);
  textSize(28);
  textAlign(RIGHT, CENTER);
  text(visorConv, 790, 190);
  textAlign(CENTER, CENTER);
  textSize(23);

  // visor de resultado
  fill(40, 30, 50);
  textSize(20);
  text("Resultado:", 600, 250);
  textSize(23);
  fill(200, 240, 200);
  rect(400, 265, 400, 60, 10);
  fill(20, 50, 20);
  textSize(28);
  textAlign(RIGHT, CENTER);

  if (visorConv != "" && !visorConv.equals("-") && !visorConv.equals(".")) {
    String resStr;
    if (resultado == int(resultado)) {
      resStr = str(int(resultado));
    } else {
      resStr = nf(resultado, 0, 4); // 4 casas decimais para distância
    }
    text(resStr, 790, 295);
  }

  textAlign(CENTER, CENTER);
  textSize(23);

  // teclado
  for (int j = 0; j < 5; j++) {
    for (int i = 0; i < 4; i++) {
      float x = INICIO_X_CONV + i * (TAM_BOTAO_CONV + GAP_X_CONV);
      float y = INICIO_Y_CONV + j * (TAM_BOTAO_CONV + GAP_Y_CONV);
      char letra = BOTOES_CONV.charAt(j * 4 + i);

      if (letra == ' ') continue; 

      if (letra == 'C') {
        fill(220, 80, 80);
      } else if (letra == '=') {
        fill(80, 180, 100);
      } else if (letra == '±') {
        fill(80, 130, 200);
      } else if (letra == ',') {
        fill(160, 120, 200);
      } else {
        fill(80, 90, 110);
      }

      rect(x, y, TAM_BOTAO_CONV, TAM_BOTAO_CONV, 12);
      fill(255);
      
      String txt;
      if (letra == '=') {
        txt = "OK";
      } else {
        txt = str(letra);
      }
      text(txt, x + TAM_BOTAO_CONV/2, y + TAM_BOTAO_CONV/2);
    }
  }

  desenhaVoltar();
}

// retorna float do visorConv ou 0 se estiver vazio/inválido
float visorConvSafe() {
  if (visorConv == "" || visorConv.equals("-") || visorConv.equals(".")) {
    return 0;
  }
  return float(visorConv);
}

void desenhaBotaoConversor(int y, color cor, String texto) {
  fill(cor);
  rect(X_BOTAO_MENU, y, LARGURA_BOTAO_MENU, ALTURA_BOTAO_MENU, 20);
  fill(0);
  text(texto, 600, y + 30);
}

void desenhaVoltar() {
  fill(200, 100, 100);
  rect(100, 100, 100, 100, 100);
  fill(255);
  textSize(20);
  text("Voltar", 150, 150);
  textSize(23);
}

// === CLIQUES ===

void cliqueMenu() {
  if (checaClique(X_BOTAO_MENU, 320, LARGURA_BOTAO_MENU, ALTURA_BOTAO_MENU)) {
    tela = 1;
  } else if (checaClique(X_BOTAO_MENU, 450, LARGURA_BOTAO_MENU, ALTURA_BOTAO_MENU)) {
    tela = 2;
  } else if (checaClique(X_BOTAO_MENU, 580, LARGURA_BOTAO_MENU, ALTURA_BOTAO_MENU)) {
    tela = 7;
  }
}

void cliqueCalculadora() {
  if (detectaVoltar(0)) return;

  for (int j = 0; j < 5; j++) {
    for (int i = 0; i < 4; i++) {
      float x = INICIO_X_CALC + i * (TAM_BOTAO_CALC + GAP_X_CALC);
      float y = INICIO_Y_CALC + j * (TAM_BOTAO_CALC + GAP_Y_CALC);

      if (checaClique(x, y, TAM_BOTAO_CALC, TAM_BOTAO_CALC)) {
        char letra = BOTOES_CALC.charAt(j * 4 + i);
        processaTecladoCalc(letra);
        return;
      }
    }
  }
}

void cliqueMenuConversor() {
  if (detectaVoltar(0)) return;

  if (checaClique(X_BOTAO_MENU, 180, LARGURA_BOTAO_MENU, ALTURA_BOTAO_MENU)) tela = 3;
  else if (checaClique(X_BOTAO_MENU, 280, LARGURA_BOTAO_MENU, ALTURA_BOTAO_MENU)) tela = 4;
  else if (checaClique(X_BOTAO_MENU, 380, LARGURA_BOTAO_MENU, ALTURA_BOTAO_MENU)) tela = 5;
  else if (checaClique(X_BOTAO_MENU, 480, LARGURA_BOTAO_MENU, ALTURA_BOTAO_MENU)) tela = 6;
}

void cliqueMenuDistancia() {
  if (detectaVoltar(0)) return;

  if (checaClique(X_BOTAO_MENU, 150, LARGURA_BOTAO_MENU, ALTURA_BOTAO_MENU)) tela = 8;
  else if (checaClique(X_BOTAO_MENU, 230, LARGURA_BOTAO_MENU, ALTURA_BOTAO_MENU)) tela = 9;
  else if (checaClique(X_BOTAO_MENU, 310, LARGURA_BOTAO_MENU, ALTURA_BOTAO_MENU)) tela = 10;
  else if (checaClique(X_BOTAO_MENU, 390, LARGURA_BOTAO_MENU, ALTURA_BOTAO_MENU)) tela = 11;
  else if (checaClique(X_BOTAO_MENU, 470, LARGURA_BOTAO_MENU, ALTURA_BOTAO_MENU)) tela = 12;
  else if (checaClique(X_BOTAO_MENU, 550, LARGURA_BOTAO_MENU, ALTURA_BOTAO_MENU)) tela = 13;
}

void cliqueTelaConversao() {
  if (detectaVoltar(2)) {
    visorConv = ""; 
    return;
  }
  processaTeclado();
}

void cliqueTelaDistancia() {
  if (detectaVoltar(7)) {
    visorConv = ""; 
    return;
  }
  processaTeclado();
}

// função compartilhada: processa cliques no teclado das telas de conversão
void processaTeclado() {
  for (int j = 0; j < 5; j++) {
    for (int i = 0; i < 4; i++) {
      float x = INICIO_X_CONV + i * (TAM_BOTAO_CONV + GAP_X_CONV);
      float y = INICIO_Y_CONV + j * (TAM_BOTAO_CONV + GAP_Y_CONV);
      char letra = BOTOES_CONV.charAt(j * 4 + i);

      if (letra == ' ') continue;

      if (checaClique(x, y, TAM_BOTAO_CONV, TAM_BOTAO_CONV)) {
        processaTecladoConv(letra);
        return;
      }
    }
  }
}

void processaTecladoCalc(char letra) {
  if (letra >= '0' && letra <= '9') {
    visor += letra;
  } else if (letra == 'C') {
    visor = "";
    num1 = 0;
    operacao = ' ';
  } else if (letra == '+' || letra == '-' || letra == 'X' || letra == '/') {
    if (visor != "" && operacao != ' ') {
      calcular();
    } else if (visor != "") {
      num1 = float(visor);
    }
    operacao = letra;
    visor = "";
  } else if (letra == ',') {
    visor += ".";
  } else if (letra == '±' && visor != "") {
    visor = str(float(visor) * -1);
  } else if (letra == '%' && visor != "") {
    visor = str(float(visor) / 100);
  } else if (letra == '=') {
    if (visor == "" || operacao == ' ') return;
    calcular();
    num1 = 0;
    operacao = ' ';
  }
}

void processaTecladoConv(char letra) {
  if (letra >= '0' && letra <= '9') {
    visorConv += letra;
  } else if (letra == 'C') {
    visorConv = "";
  } else if (letra == ',') {
    if (!visorConv.contains(".")) {
      if (visorConv.equals("") || visorConv.equals("-")) {
        visorConv += "0.";
      } else {
        visorConv += ".";
      }
    }
  } else if (letra == '±') {
    if (visorConv.equals("") || visorConv.equals("-")) {
      visorConv = "-";
    } else if (visorConv.startsWith("-")) {
      visorConv = visorConv.substring(1);
    } else {
      visorConv = "-" + visorConv;
    }
  } else if (letra == '=') {
    // OK não precisa fazer nada
  }
}

void calcular() {
  float num2 = float(visor);
  float resultado = 0;

  if (operacao == '+') resultado = num1 + num2;
  else if (operacao == '-') resultado = num1 - num2;
  else if (operacao == 'X') resultado = num1 * num2;
  else if (operacao == '/') resultado = num1 / num2;

  if (resultado == int(resultado)) {
    visor = str(int(resultado));
  } else {
    visor = str(resultado);
  }
  num1 = resultado;
}

float converteTemperatura(float valor, int modo) {
  switch (modo) {
    case 3: return valor * 9.0/5.0 + 32;
    case 4: return valor + 273.15;
    case 5: return (valor - 32) * 5.0/9.0;
    case 6: return (valor - 32) * 5.0/9.0 + 273.15;
    default: return valor;
  }
}

// nova: conversão de distância
float converteDistancia(float valor, int modo) {
  switch (modo) {
    case 8:  return valor / 1000.0;     // m -> km
    case 9:  return valor * 100.0;      // m -> cm
    case 10: return valor * 1000.0;     // km -> m
    case 11: return valor * 100000.0;   // km -> cm
    case 12: return valor / 100.0;      // cm -> m
    case 13: return valor / 100000.0;   // cm -> km
    default: return valor;
  }
}

// funções utilitárias

boolean checaClique(float x, float y, float w, float h) {
  return (mouseX > x && mouseX < x + w && mouseY > y && mouseY < y + h);
}

boolean detectaVoltar(int destino) {
  if (checaClique(100, 100, 100, 100)) {
    tela = destino;
    return true;
  }
  return false;
}

boolean isOperador(char c) {
  return (c == 'C' || c == '/' || c == 'X' || c == '-' || c == '+' || c == '=' || c == '±' || c == '%' || c == ',');
}
