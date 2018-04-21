from Livros import Livros
from Produtos import Produtos

def loja():
    p1 = Produtos()
    p1.setTipo(Livros.Epub)
    p1.precoLivro(Livros.Epub)
    print("O preço do Epub é: ",p1.getTipo()," é: ",p1.getPreco(),"reais")
    p1.setDescription("Epub é divertido")
    print("Descrição EPUB: ",p1.getDescription())

    p2 = Produtos()
    p2.setTipo(Livros.Livro_Fisico)
    p2.precoLivro(Livros.Livro_Fisico)
    print("O ", p2.getTipo(),"custa: ",p2.getPreco()," reais")
    print("Descrição livro físico: ",p2.getDescription())

    p3 = Produtos()
    p3.setTipo(Livros.PDF)
    p3.precoLivro(Livros.PDF)
    print("O preço do ",p3.getTipo()," é: ", p3.getPreco(),"reais")
    p3.setDescription("PDF")
    print("Descrição PDF: ",p3.getDescription())
    
loja()