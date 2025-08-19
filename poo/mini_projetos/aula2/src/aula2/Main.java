package aula2;

public class Main {
	
	public static void main(String[] args) {
		Carro c1 = new Carro();
		c1.marca = "Pulse";
		c1.modelo = "Fiat";
		c1.preco = 12000;
		c1.ano = 2024;
		c1.autonomia = 15;
		
		System.out.println(c1.modelo);
	}

}
