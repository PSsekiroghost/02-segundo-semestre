package aula3;

public class Main {
	
	public static void main(String[] args) {
		
		Pf pf1 = new Pf();
		pf1.cpf = "053456277890";
		pf1.rg = 12345678;
		pf1.endereco = "Quadra 100 lote 5";
		pf1.nome = "Paulo";
		pf1.dataNacs = "08/08/2006";
		pf1.telefone = "61 99765-6564";
		
		Pj pj1 = new Pj();
		pj1.cnpj = "2435679812";
		pj1.endereco = "Qudra 5 lote 1";
		
		System.out.println(pf1.cpf);
		System.out.println(pj1.endereco);
	}

}
