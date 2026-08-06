# Simulador do Modelo OSI em Python

Um programa em Python desenvolvido para simular o processo de descida (encapsulamento) de dados através das camadas do Modelo OSI. O sistema lê uma entrada de texto do usuário, passa a mensagem de forma sequencial pelas diferentes camadas de rede e, por fim, converte o dado para o formato binário, simulando a transmissão física.

---

## Funcionalidades

* **Entrada Interativa:** Utiliza `input()` para capturar a mensagem inicial do usuário de forma simples e direta.
* **Simulação de Encapsulamento:** Demonstra o comportamento de cada camada do Modelo OSI (Aplicação, Apresentação, Sessão, Transporte, Rede e Enlace de Dados) modificando e encapsulando o dado original.
* **Conversão Binária:** Converte os caracteres do texto de entrada em seus respectivos valores binários de 8 bits utilizando funções nativas (`format` e `ord`).
* **Tratamento de Erros:** Previne o encerramento abrupto do programa e exibe uma mensagem amigável caso o usuário interrompa a execução utilizando atalhos como `Ctrl+C` ou `Ctrl+D` (tratamento de `KeyboardInterrupt` e `EOFError`).
* **Saída Formatada:** Exibe o passo a passo no console, detalhando a função de cada camada no processo de transmissão.

---

## Tecnologias Utilizadas

* **Linguagem Python** (Padrão 3.x)
* **Bibliotecas Built-in do Python** (Nenhuma dependência externa necessária)

---

## Código Completo

```python
class Main:
    @staticmethod
    def entrada():
        print("=== DESCIDA PELO MODELO OSI (TRANSMISSÃO) ===")
        data = str(input("Digite alguma coisa\n>> "))
        return data

    @staticmethod
    def aplicacao(dado):
        print("[CAMADA APLICAÇÃO]: O usuário digita. A aplicação cria a mensagem inicial.")
        resultado = f"[CAMADA APLICAÇÃO] -> {dado}"
        return resultado

    @staticmethod
    def apresentacao(dado):
        print("[CAMADA APRESENTAÇÃO]: A mensagem é formatada e codificada (ex: padrão UTF-8 para ser compreendida).")
        resultado = f"[APRESENTAÇÃO] -> {dado}"
        return resultado
        
    @staticmethod
    def sessao(dado):
        print("[CAMADA SESSÃO]: É estabelecida e gerenciada a sessão de comunicação entre os dispositivos.")
        resultado = f"[SESSÃO] -> {dado}"
        return resultado
        
    @staticmethod
    def transporte(dado):
        print("[CAMADA TRANSPORTE]: A mensagem é dividida em segmentos e recebe dados de controle (como a porta de comunicação).")
        resultado = f"[TRANSPORTE] -> {dado}"
        return resultado
        
    @staticmethod
    def rede(dado):
        print("[CAMADA REDE]: Adiciona os endereços lógicos de origem e destino (roteamento entre redes).")
        resultado = f"[REDE] -> {dado}"
        return resultado
       
    @staticmethod
    def enlace_de_dados(dado):
        print("[CAMADA ENLACE DE DADOS]: Adiciona os endereços físicos (MAC) para a entrega direta entre os nós da rede.")
        resultado = f"[ENLANCE DE DADO] -> {dado}"
        return resultado

    @staticmethod
    def binario(dado):
        dado_em_binario = "".join(format(ord(c), '08b') for c in dado)
        return dado_em_binario

    @staticmethod
    def final(entrada, dado):
        print("[CAMADA FÍSICA]: O quadro completo é convertido em sinais elétricos, ópticos ou binários (0s e 1s) para transmissão real.")
        print(f"ENTRADA -> {entrada}")
        print(f"SAIDA -> {dado}")

if __name__ == '__main__':
    try:

        texto = Main.entrada()
        dado = Main.aplicacao(texto)
        dado = Main.apresentacao(dado)
        dado = Main.sessao(dado)
        dado = Main.transporte(dado)
        dado = Main.rede(dado)
        dado = Main.enlace_de_dados(dado)

        valor_em_binario = Main.binario(texto)

        Main.final(texto, valor_em_binario)
        
    except (KeyboardInterrupt, EOFError):
        print("\nO usuário encerrou o sistema.")

```

---

## Como Compilar e Executar

Siga os passos abaixo para executar o código em sua máquina:

1. Certifique-se de ter o **Python** instalado (versão 3.x recomendada).
2. Salve o código em um arquivo chamado `main.py`.
3. Abra o terminal na pasta do arquivo e execute o comando:

```bash
python main.py

```

*(ou `python3 main.py` dependendo do seu sistema operacional)*

---

## Exemplo de Uso

O programa solicitará que você insira um texto e exibirá o percurso simulado pelas camadas do modelo OSI até convertê-lo em binário.

**Entrada:**

```text
Oi

```

**Saída:**

```text
=== DESCIDA PELO MODELO OSI (TRANSMISSÃO) ===
Digite alguma coisa
>> Oi
[CAMADA APLICAÇÃO]: O usuário digita. A aplicação cria a mensagem inicial.
[CAMADA APRESENTAÇÃO]: A mensagem é formatada e codificada (ex: padrão UTF-8 para ser compreendida).
[CAMADA SESSÃO]: É estabelecida e gerenciada a sessão de comunicação entre os dispositivos.
[CAMADA TRANSPORTE]: A mensagem é dividida em segmentos e recebe dados de controle (como a porta de comunicação).
[CAMADA REDE]: Adiciona os endereços lógicos de origem e destino (roteamento entre redes).
[CAMADA ENLACE DE DADOS]: Adiciona os endereços físicos (MAC) para a entrega direta entre os nós da rede.
[CAMADA FÍSICA]: O quadro completo é convertido em sinais elétricos, ópticos ou binários (0s e 1s) para transmissão real.
ENTRADA -> Oi
SAIDA -> 0100111101101001

```

---

## Estrutura do Código

| Função/Método | Tipo de Retorno | Descrição |
| --- | --- | --- |
| `entrada` | `str` | Exibe o menu inicial e captura o texto digitado pelo usuário. |
| `aplicacao` a `enlace_de_dados` | `str` | Uma série de métodos que simulam o encapsulamento, adicionando tags e imprimindo a função de cada camada OSI. |
| `binario` | `str` | Converte o texto de entrada em uma sequência contínua de caracteres binários (0s e 1s). |
| `final` | `None` | Representa a Camada Física, imprimindo o dado original e o seu equivalente em formato binário pronto para "transmissão". |

---

# **PROPOSTA**

<img width="1123" height="677" alt="imagem" src="https://github.com/user-attachments/assets/6f5c02a4-f103-4999-ba04-47a9c5fb127e" />
