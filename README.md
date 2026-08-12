# Portfólio de Impressão 3D

Site estático (HTML/CSS/JS puro, sem build) para apresentar seus trabalhos em impressão 3D.

## Estrutura

- `index.html` — conteúdo e estrutura do site
- `styles.css` — visual (cores, tipografia, layout)
- `script.js` — efeito de digitação no título e animação das barras de progresso

## Como personalizar

1. **Trocar as imagens**: cada `.work-card` em `index.html` tem um `<div class="work-image">` com um gradiente de cor no lugar de uma foto. Troque por uma imagem real:
   ```html
   <div class="work-image">
     <img src="imagens/dragao.jpg" alt="Dragão articulado flexível">
   </div>
   ```
   Crie uma pasta `imagens/` na raiz do projeto e coloque suas fotos lá.

2. **Editar textos**: título, descrição, material, tempo de impressão e tamanho de cada peça estão diretamente no HTML, dentro de cada `.work-card`.

3. **Trocar contato**: no final do `index.html`, atualize o e-mail e o link do GitHub na seção `#contato`.

4. **Adicionar mais peças**: copie um bloco `<article class="work-card">...</article>` inteiro e cole antes do card de placeholder ("+ novo projeto").

## Publicar no GitHub Pages

1. Crie um repositório novo no GitHub (ex: `portfolio-3d`).
2. Suba estes três arquivos (`index.html`, `styles.css`, `script.js`) — e a pasta `imagens/`, se você criar uma — para a raiz do repositório.
3. No repositório, vá em **Settings → Pages**.
4. Em **Source**, selecione a branch `main` (ou `master`) e a pasta `/ (root)`.
5. Salve. Em alguns minutos o site fica disponível em:
   ```
   https://SEU-USUARIO.github.io/NOME-DO-REPOSITORIO/
   ```

Se quiser usar um domínio próprio, crie um arquivo `CNAME` na raiz com o domínio dentro, e configure o DNS conforme a documentação do GitHub Pages.
