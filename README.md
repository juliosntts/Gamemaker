# Monitor de FPS em Tempo Real

## Descrição
Este projeto consiste em um servidor web simples desenvolvido em Python que exibe e monitora a taxa de quadros por segundo (FPS) de aplicações em tempo real. O servidor recebe dados de FPS via API e os exibe em uma interface web atualizada dinamicamente.

## Principais Funcionalidades
- API para receber valores de FPS de aplicações externas
- Interface web para visualização em tempo real dos valores de FPS
- Atualização automática do valor exibido a cada segundo

## Instruções de Instalação e Configuração
1. Clone este repositório:
   ```
   git clone https://github.com/seu-usuario/monitor-fps.git
   cd monitor-fps
   ```

2. Crie um ambiente virtual e instale as dependências:
   ```
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Execute o servidor:
   ```
   python Servidor/servidor.py
   ```

4. Acesse a interface web em http://localhost:5000

5. Para enviar dados de FPS para o servidor, faça uma requisição POST para http://localhost:5000/fps com um JSON no formato:
   ```json
   {"fps": 60}
   ```

## Autores
- [ Rodrigo Araújo Gonçalves Ribeiro,
- Caique Kelvin Ferreira de Melo
- Guilherme Santos Toaiari de Moraes
- Júlio Nascimento Santos
 ]
