package biblioteca;

public class Revista extends Material {
    public int edicao;
    public String mesPublicacao;

    public Revista(String titulo, String anoPublicacao, int edicao, String mesPublicacao) {
        super(titulo, anoPublicacao);
        this.edicao = edicao;
        this.mesPublicacao = mesPublicacao;
    }
}

