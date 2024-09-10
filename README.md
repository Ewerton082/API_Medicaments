# API de Gestão de Produtos, Tipos e Marcas
Este projeto é uma **API REST** desenvolvida em **Django** e **MySQL** para gerenciar medicamentos, tipos e marcas de uma loja de ração. A API fornece endpoints para criar, listar, editar e excluir esses dados, além de implementar autenticação via **JWT** para proteger as rotas.

### Funcionalidades
+ Gestão de Tipos de Produtos: permite a criação, listagem, atualização e exclusão de diferentes tipos de produtos.
+ Gestão de Marcas: permite a criação, listagem, atualização e exclusão de marcas associadas aos produtos.
+ Gestão de Produtos: permite a criação, listagem, atualização e exclusão de produtos, vinculados a marcas e tipos.
+ Autenticação JWT: tokens são utilizados para acessar as rotas protegidas, como criação e atualização de registros.
### Tecnologias Utilizadas
+ Django: framework web para o back-end.
+ Django REST Framework: para a criação da API RESTful.
+ MySQL: banco de dados utilizado para armazenar as informações.
+ JWT: para autenticação via tokens.
+ Python: linguagem de programação principal.
+ PEP8: boas práticas seguidas no código.

# Fotos do projeto

### Road Map criado para ter um ideia do desenvolvimento

![canvas_api-remedios-240909_0356](https://github.com/user-attachments/assets/bbbbab20-c607-4126-8d95-62977f7dca7d)

### Rotas da API

![Captura de tela 2024-09-09 001215](https://github.com/user-attachments/assets/c9ca5a1e-450f-4bde-a120-97feaa17ea1d)

### Retornos JSON de nossa API

Retorno do produto final utilizando do objeto criado nas outras 2 fotos [brand e type]
+ ![Captura de tela 2024-09-09 004313](https://github.com/user-attachments/assets/2e1c6a04-38cb-4b84-ab1f-12de5baeed0f)

Retorno do Tipo de Medicamento com uma breve explicação do que esse tipo de medicamento faz
+ ![Captura de tela 2024-09-09 004359](https://github.com/user-attachments/assets/aa69e785-f7ce-4dd1-a070-54382896dd87)

Retorno das Empresas que fornecem os medicamentos
+ ![Captura de tela 2024-09-09 004334](https://github.com/user-attachments/assets/d126cdae-5a72-4a75-8a3c-8a60babe1ef0)

### Conclusão

Criei este projeto com o objetivo de validar meu aprendizado no uso de REST APIs, e estou bastante satisfeito com o resultado. Embora seja um projeto pequeno, dediquei-me em cada etapa do desenvolvimento e consegui finalizá-lo em um período relativamente curto. Havia algumas funcionalidades adicionais que gostaria de ter implementado, como a integração com a API do ChatGPT para gerar automaticamente os resumos dos tipos de medicamentos e suas instruções de uso, mas infelizmente, não foi possível nesta versão. Mesmo assim, o processo foi extremamente enriquecedor e me proporcionou uma oportunidade prática de consolidar meus conhecimentos.
