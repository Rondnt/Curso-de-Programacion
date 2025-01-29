package teoria;

import javax.swing.JOptionPane;

public class EjercicioNotas {
	public static void main(String[] args) {
		String nota_str = JOptionPane.showInputDialog("Bienvenido, ingresa la nota");
		int nota = Integer.parseInt(nota_str);
		
		if(nota < 0 ||nota > 20) {
			JOptionPane.showMessageDialog(null, "Ingrese una nota entre 0 a 20", "Error", JOptionPane.ERROR_MESSAGE);
			return;
		}if(nota < 11.5) {
			JOptionPane.showMessageDialog(null,"Usted esta desaprobado", "Precaucion", JOptionPane.WARNING_MESSAGE);			
		}else if(nota < 16) {
			JOptionPane.showMessageDialog(null, "Usted esta aprobado", "Informacion", JOptionPane.QUESTION_MESSAGE);	
		}else if(nota > 16) {
			JOptionPane.showMessageDialog(null, "¡Felicitaciones! Usted esta aprobado con una de las mejores notas", "Informacion", JOptionPane.INFORMATION_MESSAGE);
		}
	}
}
/* Saludar al usuario y perdir que ingrese su nota
 * indicar si esta desaprobado con un warning
 * o si esta aprobado con menos de 16 un question message
 * si esta aprobado con mas de 16 con un mensaje de felicitacion information message
 * si esta fuera de rango un error message*/
 
