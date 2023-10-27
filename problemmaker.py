import random

class ProblemMaker:
    def Iniciar(self):
        self.fazer_numeros()
        self.fazer_problemas()
        self.fazer_respostas()
        self.fazer_mensagens()
        
    
    def fazer_numeros(self):
        self.n1_dezena = random.randint(10,99)
        self.n2_dezena = random.randint(10,99)

        self.n3_centena = random.randint(100,999)
        self.n4_dezena = random.randint(10,99)
        
        self.n5_centena = random.randint(100,999)
        self.n6_centena = random.randint(100,999)

        self.n7_centena = random.randint(100,999)
        self.n8_unidade = random.randint(2,9)

        self.n9_milhar = random.randint(1000,999999)
        self.n10_unidade = random.randint(2,9)

        self.n11_milhaao = random.randint(1000000,999999999)
        self.n12_unidade = random.randint(2,9)

    def fazer_problemas(self):
        self.problema1 = f'{self.n1_dezena} x {self.n2_dezena}'
        self.problema2 = f'{self.n3_centena} x {self.n4_dezena}'
        self.problema3 = f'{self.n5_centena} x {self.n6_centena}'

        self.problema4 = f'{self.n7_centena} / {self.n8_unidade}'
        self.problema5 = f'{self.n9_milhar} / {self.n10_unidade}'
        self.problema6 = f'{self.n11_milhaao} / {self.n12_unidade}'

    def fazer_respostas(self):
        self.resposta1 = self.n1_dezena*self.n2_dezena
        self.resposta2 = self.n3_centena*self.n4_dezena
        self.resposta3 = self.n5_centena*self.n6_centena

        self.resposta4 = int(self.n7_centena/self.n8_unidade)
        self.resto4 = self.n7_centena%self.n8_unidade

        self.resposta5 = int(self.n9_milhar/self.n10_unidade)
        self.resto5 = self.n9_milhar%self.n10_unidade

        self.resposta6 = int(self.n11_milhaao/self.n12_unidade)
        self.resto6 = self.n11_milhaao%self.n12_unidade

        # print(self.problema1)
        # print(self.resposta1)
        # print()
        # print(self.problema2)
        # print(self.resposta2)
        # print()
        # print(self.problema3)
        # print(self.resposta3)
        # print()
        # print(self.problema4)
        # print(self.resposta4)
        # print(self.resto4)
        # print()
        # print(self.problema5)
        # print(self.resposta5)
        # print(self.resto5)
        # print()
        # print(self.problema6)
        # print(self.resposta6)
        # print(self.resto6)
        # print()

    def fazer_mensagens(self):
        self.msn_problemas = f'QUESTÃO 1:\n{self.problema1}\n\nQUESTÃO 2:\n{self.problema2}\n\nQUESTÃO 3:\n{self.problema3}\n\nQUESTÃO 4:\n{self.problema4}\n\nQUESTÃO 5:\n{self.problema5}\n\nQUESTÃO 6:\n{self.problema6}\n'

        self.msn_respostas_multiplicacao = f'Q1: {self.resposta1}\nQ2: {self.resposta2}\nQ3: {self.resposta3}\n'

        self.msn_resp_divisao1 = f'Q4:\nResult:{self.resposta4}; Resto:{self.resto4}\n'
        self.msn_resp_divisao2 = f'Q5:\nResult:{self.resposta5}; Resto:{self.resto5}\n'
        self.msn_resp_divisao3 = f'Q6:\nResult:{self.resposta6}; Resto:{self.resto6}\n'

        # print(self.msn_problemas)
        # print(self.msn_respostas_multiplicacao)
        # print(self.msn_resp_divisao1)
        # print(self.msn_resp_divisao2)
        # print(self.msn_resp_divisao3)

        return [self.msn_problemas,self.msn_respostas_multiplicacao,self.msn_resp_divisao1,self.msn_resp_divisao2,self.msn_resp_divisao3]





