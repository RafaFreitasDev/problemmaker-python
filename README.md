# problemmaker-python
Tenho uma filha de 9 anos, e todos os dias passo contas de matemática para o desenvolvimento do seu raciocínio e lógica. Essas contas são desenvolvidas em minha cabeça. Com o intuito de facilitar o processo, resolvi desenvolver a seguinte aplicação.

O programa gera 3 contas de multiplicação e 3 contas de divisão aleatoriamente, enviando os problemas para o celular da minha filha e as respostas para o meu celular, tudo via WhatsApp Web.

Estabeleci os tamanhos dos números gerados, pois ela já enfrentava esse tipo de dificuldade e não queria que fosse aleatório demais.

Os nomes dos contatos buscados no WhatsApp Web foram colocados em variáveis de ambiente para que a aplicação possa ser reaproveitada por outros desenvolvedores ou pais interessados.

## Pré-requisitos

Antes de começar, certifique-se de ter instalado o seguinte:

- Python 3.11: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- Git (opcional, mas útil para clonar o repositório): [https://git-scm.com/downloads](https://git-scm.com/downloads)
- Google Chrome: [https://www.google.com/intl/pt-BR/chrome/](https://www.google.com/intl/pt-BR/chrome/)

## Instalação

Siga os passos abaixo para configurar e executar o projeto:

1. Clone este repositório (ou faça o download do código-fonte):

    ```powershell
    git clone git@github.com:RafaFreitasDev/problemmaker-python.git
    ```

2. Navegue até o diretório do projeto:

    ```powershell
    cd problemmaker-python
    ```

3. Crie um ambiente virtual (recomendado):

    ```powershell
    python -m venv venv
    ```

4. Ative o ambiente virtual:

    - No Windows:

    ```powershell
    venv\Scripts\activate
    ```

    - No macOS e Linux:

    ```powershell
    source venv/bin/activate
    ```

5. Instale as dependências do projeto:

    ```powershell
    pip install -r requirements.txt
    ```

## Uso

É preciso transformar o arquivo .env.example em .env e preencher as variáeis de ambiente seguindo instruções

Para executar o programa, use o seguinte comando:

```powershell
python main.py
```

## Contato

Se você tiver alguma dúvida ou problema, sinta-se à vontade para entrar em contato:

- Rafael Almeida Freitas
- Email: raf.mec.ba@gmail.com
- Obs.: Colocar "Dúvida Projeto Git - nomeDoProjeto" no assunto