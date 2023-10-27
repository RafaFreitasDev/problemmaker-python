from problemmaker import ProblemMaker
from sendmessage import SendMessage

if __name__ == "__main__":
    code = ProblemMaker()
    code.Iniciar()
    mensagens = code.fazer_mensagens()
    msn_problemas = mensagens[0]
    msn_result_multiplicacoes = mensagens[1]
    msn_result_div1 = mensagens[2]
    msn_result_div2 = mensagens[3]
    msn_result_div3 = mensagens[4]
    
    send = SendMessage()
    send.open_website()
    send.enviar_problemas(msn_problemas)
    send.enviar_resultados(msn_result_multiplicacoes,msn_result_div1,msn_result_div2,msn_result_div3)
    