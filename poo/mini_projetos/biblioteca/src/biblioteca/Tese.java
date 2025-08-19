package biblioteca;

public class Tese extends Material {
    public String autor;
    public String curso;

    public Tese(String titulo, String anoPublicacao, String autor, String curso) {
        super(titulo, anoPublicacao);
        this.autor = autor;
        this.curso = curso;
    }
}
