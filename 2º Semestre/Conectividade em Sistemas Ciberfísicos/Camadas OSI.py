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
