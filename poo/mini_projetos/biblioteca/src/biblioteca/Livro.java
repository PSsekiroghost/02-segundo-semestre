package biblioteca;

public class Livro extends Material {
    public String autor;
    public int numPaginas;

    public Livro(String titulo, String anoPublicacao, String autor, int numPaginas) {
        super(titulo, anoPublicacao);
        this.autor = autor;
        this.numPaginas = numPaginas;
    }
}
