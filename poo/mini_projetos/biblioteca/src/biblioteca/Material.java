package biblioteca;

public abstract class Material {
	
	public String titulo;
	public String anoPublicacao;
	public boolean emprestado;
	
	public Material(String titulo, String anoPublicacao) {
		this.titulo = titulo;
		this.anoPublicacao = anoPublicacao;
		this.emprestado = false;
	}
	
	public void emprestar() {
		if (!emprestado) {
			emprestado = true;
			System.out.println(titulo + " foi emprestado.");
		} else {
			System.out.println(titulo + " ja está emprestado!");
	    }
	}
	
	public void devolver() {
		if(emprestado) {
			emprestado = false;
			System.out.println(titulo + " foi devolvido.");
		}else {
			System.out.println(titulo + " não estava emprestado.");
		}
	}
}
