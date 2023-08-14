# Sistema Bancário em Python - Atualizado com Princípios SOLID

Este projeto oferece uma versão atualizada e simplificada de um sistema bancário em Python, incorporando os princípios do SOLID e seguindo as melhores práticas de design orientado a objetos. A aplicação proporciona funcionalidades básicas para gerenciamento de contas bancárias, incluindo depósitos, saques e a visualização de extratos, tudo isso através de uma interface de texto amigável.

## Principais Características e Princípios

- **Organização Modular:** O projeto foi dividido em diferentes arquivos, cada um com um propósito específico e seguindo o princípio da Responsabilidade Única (SRP).
- **Classes e Herança:** O uso de herança foi aplicado para criar uma estrutura mais coesa e reutilizável. As classes foram organizadas para facilitar a extensão de funcionalidades.
- **Interfaces Claras:** As interfaces foram definidas de forma clara para cada classe, seguindo o princípio da Segregação de Interfaces (ISP), permitindo que cada classe implemente somente o que é relevante.
- **Validações Refinadas:** As operações, como saques, foram implementadas com validações que respeitam as regras de negócio e mantêm o código coeso e seguro.
- **Menu Intuitivo:** O arquivo "main.py" apresenta um menu de interação intuitivo, possibilitando login, acesso ao menu administrativo e realização de operações bancárias.
- **Princípio do Open/Closed:** A estrutura do projeto foi planejada de modo a ser facilmente estendida sem a necessidade de modificar as classes existentes.
  
## Instruções

1. Execute o arquivo "main.py" para iniciar a aplicação.
2. Utilize o menu para fazer login, realizar operações bancárias e explorar as funcionalidades disponíveis.
3. Aproveite para analisar o código-fonte, entender a implementação dos princípios SOLID e fazer ajustes de acordo com suas necessidades.

Este projeto exemplifica o uso dos princípios SOLID para criar um código mais robusto, extensível e de fácil manutenção. Ao explorar o código, você terá a oportunidade de aprender não apenas as funcionalidades bancárias, mas também as boas práticas de programação orientada a objetos.

**Observação:** Este projeto foi desenvolvido como um exercício didático e não é adequado para uso em ambientes de produção ou para tratamento de informações financeiras reais.

Desfrute da jornada de aprendizado e aproveite as vantagens de desenvolver com os princípios SOLID!

## Estrutura do Projeto

O projeto segue uma estrutura baseada na Clean Architecture, onde a organização em camadas facilita a separação de responsabilidades e a escalabilidade do sistema. Abaixo está a descrição das principais pastas e arquivos do projeto:

- **app/domain/models:** Contém as classes de modelos de domínio, como `Cliente`, `ContaBancaria` e `Transacao`.
- **app/domain/repositories:** Responsável por interagir com o banco de dados e realizar operações CRUD nas entidades.
- **app/domain/use_cases:** Contém os casos de uso da aplicação, que encapsulam a lógica de negócios.
- **app/interfaces:** Contém as interfaces de interação com o usuário, como o menu do cliente e do administrador.
- **app/persistence/database.py:** Responsável pela configuração do banco de dados e pela inicialização da sessão.

O arquivo principal **main.py** é o ponto de entrada da aplicação, onde o banco de dados é inicializado e os casos de uso são instanciados para possibilitar a interação do usuário com o sistema.

Lembre-se de explorar cada arquivo e entender como eles se relacionam para formar a estrutura geral do projeto.
