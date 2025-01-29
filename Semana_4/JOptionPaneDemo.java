package teoria;

import javax.swing.JOptionPane;

public class JOptionPaneDemo {
	public static void main(String[] args) {
		//JOptionPane.showMessageDialog(null,"�Hola! Bienvenido al sistema.", "Ventana Informativa", JOptionPane.QUESTION_MESSAGE);	
		String edad_str = JOptionPane.showInputDialog("Bienvenido, ingresa tu edad");
		int edad = Integer.parseInt(edad_str);
		
		if(edad < 18) {
			JOptionPane.showMessageDialog(null,"Usted es menor de edad", "Precaucion", JOptionPane.ERROR_MESSAGE);			
		}
	}		
}
/* Saludar al usuario y perdir que ingrese su nota
 * indicar si esta desaprobado con un warning
 * o si esta aprobado con menos de 16 un question message
 * si esta aprobado con mas de 16 con un mensaje de felicitacion information message
 * si esta fuera de rango un error message*/
 
