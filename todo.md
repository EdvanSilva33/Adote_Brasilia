# Lista de Tarefas: Adicionar Funcionalidades ao Site de Doação de Animais (Flask)

- [x] 1. Analisar a estrutura de arquivos HTML, CSS e Flask fornecida.
- [x] 2. Criar o arquivo `como_ajudar.html` na pasta `templates` com a estrutura básica, incluindo o slideshow de 3 fotos e textos fictícios sobre como ajudar sem adotar.
- [x] 3. Criar o arquivo `resgate_gatinho.html` na pasta `templates` com a estrutura básica, incluindo uma foto e um texto emocionante fictício sobre o resgate de um gatinho.
- [x] 4. Integrar as novas páginas ao `app.py`:
    - [x] 4.1. Adicionar rotas para `/como-ajudar` (função `como_ajudar_page`) e `/resgate-gatinho` (função `resgate_gatinho_page`).
    - [x] 4.2. Fazer as funções das rotas renderizarem os respectivos templates HTML.
- [x] 5. Atualizar os links dos botões "Como Ajudar" e "Saiba Mais Sobre Nós" (ou similar) no arquivo `index.html` (que será movido para `templates/index.html`) para direcionarem às novas rotas usando `url_for()`.
- [x] 6. Garantir que os arquivos CSS (`style.css`, `main.css`) estejam na pasta `static/css` e sejam referenciados corretamente nos templates HTML.
- [x] 7. Criar imagens placeholder (`placeholder_ajuda1.jpg`, `placeholder_ajuda2.jpg`, `placeholder_ajuda3.jpg`, `placeholder_gatinho_resgatado.jpg`) na pasta `static/images` e referenciá-las nos novos templates.
- [x] 8. Revisar e corrigir o erro de sintaxe de f-string no `app.py` (uso de aspas simples dentro de f-string delimitada por aspas duplas).
- [x] 9. Revisar e corrigir todos os links `url_for` no `index.html` para garantir que os endpoints e nomes de funções estejam corretos, evitando `BuildError`.
- [x] 10. Revisar se o nome da função da rota e o endpoint realmente batem entre `app.py` e os templates para corrigir `BuildError`.
- [x] 11. Corrigir a tag `{% now %}` nos templates `como_ajudar.html` e `resgate_gatinho.html`, substituindo-a por uma variável de contexto (`current_year`) injetada pelo Flask para exibir o ano atual.
- [x] 12. Validar o funcionamento completo do site: navegação entre todas as páginas, funcionamento dos botões, slideshow, exibição correta das imagens e textos, e consistência dos estilos.
- [x] 13. Compactar a pasta do projeto final (`/home/ubuntu/novo_site_doacao`) em um arquivo .zip.
- [x] 14. Enviar o arquivo .zip final e o `todo.md` atualizado para o usuário.
