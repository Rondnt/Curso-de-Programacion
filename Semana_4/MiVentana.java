package teoria;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import java.awt.BorderLayout;
import javax.swing.BoxLayout;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JComboBox;
import javax.swing.SwingConstants;
import java.awt.Font;
import java.awt.Color;
import javax.swing.border.BevelBorder;

public class MiVentana extends JFrame {

	private JPanel contentPane;
	private JTextField tfname;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MiVentana frame = new MiVentana();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MiVentana() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBackground(Color.ORANGE);
		contentPane.setBorder(new BevelBorder(BevelBorder.RAISED, null, null, null, null));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbsaludos = new JLabel("Hola, bienvenido");
		lbsaludos.setBounds(105, 178, 127, 14);
		contentPane.add(lbsaludos);
		
		JButton bt1 = new JButton("Bot\u00F3n 1");
		bt1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				lbsaludos.setText("Cadena 1");
			}
		});
		bt1.setBounds(25, 132, 89, 23);
		contentPane.add(bt1);
		
		JButton btnNewButton_1 = new JButton("Bot\u00F3n 2");
		btnNewButton_1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				lbsaludos.setText("Cadena 2");
			}
		});
		btnNewButton_1.setBounds(25, 200, 89, 23);
		contentPane.add(btnNewButton_1);
		
		JButton btnNewButton_2 = new JButton("Bot\u00F3n 3");
		btnNewButton_2.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				lbsaludos.setText("Cadena 3");
			}
		});
		btnNewButton_2.setBounds(178, 132, 89, 23);
		contentPane.add(btnNewButton_2);
		
		JButton btnNewButton_3 = new JButton("Bot\u00F3n 4");
		btnNewButton_3.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				lbsaludos.setText("Cadena 4");
			}
		});
		btnNewButton_3.setBounds(178, 200, 89, 23);
		contentPane.add(btnNewButton_3);
		
		tfname = new JTextField();
		tfname.setBounds(78, 38, 139, 20);
		contentPane.add(tfname);
		tfname.setColumns(10);
		
		JLabel lbName = new JLabel("Nombre");
		lbName.setBounds(22, 41, 46, 14);
		contentPane.add(lbName);
		
		JLabel lbsaludo = new JLabel("");
		lbsaludo.setBounds(22, 107, 183, 14);
		contentPane.add(lbsaludo);
		
		JButton btnAceptar = new JButton("Aceptar");
		btnAceptar.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				String nombre = tfname.getText();
				lbsaludo.setText("Bienvenido "+ nombre);
			}
		});
		btnAceptar.setBounds(25, 73, 89, 23);
		contentPane.add(btnAceptar);
		
		
	}
}

/*
 * Hacer un programa que pida al usuario su nombre, edad y su nota
 * mostrar un mensaje de bienvenido nombre.usted es mayor o menor de edady luego mostrar
 * una ventana de alerta que indique si esta aprobado o desaprobado.JOptionPane*/
