# kenzieCommerce

Documentação: https://kenziecommerce-deploy-app.onrender.com/api/docs/swagger-ui/

## Passo 1: Clonar o repositório do GitHub
  1. Abra o terminal ou prompt de comando no seu computador.
  2. Navegue até o diretório onde deseja clonar o repositório.
  3. Execute o seguinte comando para clonar o repositório:
  git clone <git@github.com:KenzieCommerce-G19/kenzieCommerce.git>
  4. Navegue até o diretório do projeto clonado:
  cd caminho/onde/esta/a/pasta/KenzieCommerce
  5. Crie um arquivo chamado `.env` na raiz do projeto e adicione as seguintes linhas:
  SECRET_KEY=<sua_secret_key>
  POSTGRES_USERNAME=<seu_usuário>
  POSTGRES_PASSWORD=<sua_senha>
  POSTGRES_DB_NAME=<seu_nome_do_banco>
  POSTGRES_DB_HOST=<seu_host_do_banco>
  POSTGRES_DB_PORT=<sua_porta_do_banco>
  EMAIL_HOST=smtp.gmail.com 
  EMAIL_PORT=587 
  EMAIL_HOST_USER=<seu_email_de_usuário>
  EMAIL_HOST_PASSWORD=<sua_senha>
  
  EMAIL_HOST: Essa é a configuração padrão desta aplicação. Se você desejar usar outro domínio de email, é necessário consultar a documentação específica para obter as configuração corretas.
  EMAIL_PORT: Senha de aplicativo do email.

  Substitua: <sua_secret_key>, <seu_usuário>, <sua_senha>, <seu_nome_do_banco>, <seu_host_do_banco> e <sua_porta_do_banco> pelos valores apropriados.

## Passo 2: Configurar o arquivo .env
  Configure o arquivo `.env` adicionando as informações necessárias, conforme mencionado no Passo 1.

## Passo 3: Instalar as dependências
  1. Navegue até o diretório do projeto, se ainda não estiver nele:
  cd caminho/onde/esta/a/pasta/KenzieCommerce
  2. Crie um ambiente virtual (opcional, mas recomendado):
  python -m venv myenv
  Você pode substituir `myenv` pelo nome que achar melhor.
  3. Ative o ambiente virtual:
  No Windows:
  myenv\Scripts\activate
  No macOS/Linux:
  source myenv/bin/activate
  4. Instale as bibliotecas necessárias do arquivo "requirements.txt":
  pip install -r requirements.txt
  Isso irá instalar todas as bibliotecas listadas no arquivo "requirements.txt" no seu ambiente virtual.

## Passo 4: Executar as migrações
  1. Navegue até o diretório do projeto, se ainda não estiver nele:
  cd caminho/onde/esta/a/pasta/KenzieCommerce
  2. Execute o seguinte comando para aplicar as migrações:
  python manage.py migrate
  Isso irá criar as tabelas e estruturas de banco de dados necessárias para a aplicação.

## Passo 5: Executar o servidor Django
  1. Navegue até o diretório do projeto, se ainda não estiver nele:
  cd caminho/onde/esta/a/pasta/KenzieCommerce
  2. Execute o seguinte comando para iniciar o servidor Django:
  python manage.py runserver
  Se você seguiu o passo a passo corretamente, o servidor Django será iniciado e você poderá acessar a aplicação em um cliente REST, como por exemplo Insomnia, Postman, ou qualquer outro que preferir, usando o endereço "http://localhost:8000".
