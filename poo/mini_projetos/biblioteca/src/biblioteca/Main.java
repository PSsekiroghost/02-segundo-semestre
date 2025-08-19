package biblioteca;

public class Main {
    public static void main(String[] args) {
        Livro l1 = new Livro("O bom menino", "2025", "Paulo", 500);
        Revista r1 = new Revista("As novidades de São Paulo", "2025", 5, "Dezembro");
        Tese t1 = new Tese("Sobre a engenharia", "2025", "Karlos", "Engenharia da Computação");
        
        l1.emprestar();
        System.out.println("\n");
        System.out.println("Titulo: " + l1.titulo);
        System.out.println("Ano de publicação: " + l1.anoPublicacao);
        System.out.println("Autor: " + l1.autor);
        System.out.println("Numero de paginas: " + l1.numPaginas);
        System.out.println("Emprestado: " +(l1.emprestado ? "Sim" : "Não"));
        System.out.println("\n");
        
        System.out.println("Titulo: " + r1.titulo);
        System.out.println("Ano de publicaçãp: " + r1.anoPublicacao);
        System.out.println("Edição: " + r1.edicao);
        System.out.println("Mes de Publicação: " + r1.mesPublicacao);
        System.out.println("Emprestado: " + (r1.emprestado ? "Sim" : "Não"));
        System.out.println("\n");
        
        t1.emprestar();
        System.out.println("Titulo:" + t1.titulo);
        System.out.println("Ano de publicação: " + t1.anoPublicacao);
        System.out.println("Autor: " + t1.autor);
        System.out.println("Curso: " + t1.curso);
        
        
    }
}
