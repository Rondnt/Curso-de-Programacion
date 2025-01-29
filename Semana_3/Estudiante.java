package semana3;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

public class Estudiante implements Comparable<Estudiante> {
    private String nombre;
    private double nota;
    private int edad;

    public Estudiante(String nombre, double nota, int edad) {
        this.nombre = nombre;
        this.nota = nota;
        this.edad = edad;
    }

    public String getNombre() {
        return nombre;
    }

    public double getNota() {
        return nota;
    }

    public int getEdad() {
        return edad;
    }

    @Override
    public int compareTo(Estudiante otro) {
        return this.nombre.compareTo(otro.nombre);
    }

    @Override
    public String toString() {
        return "Estudiante{" +
                "nombre='" + nombre + '\'' +
                ", nota=" + nota +
                ", edad=" + edad +
                '}';
    }

    public static void main(String[] args) {

        ArrayList<Estudiante> estudiantes = new ArrayList<>();
        estudiantes.add(new Estudiante("Carlos", 15.5, 20));
        estudiantes.add(new Estudiante("Ana", 18.0, 22));
        estudiantes.add(new Estudiante("Luis", 12.5, 19));

        System.out.println("Ordenado por nombre:");
        Collections.sort(estudiantes);
        for (Estudiante e : estudiantes) {
            System.out.println(e);
        }
       
        System.out.println("\nOrdenado por nota:");
        estudiantes.sort(Comparator.comparingDouble(Estudiante::getNota).reversed());
        for (Estudiante e : estudiantes) {
            System.out.println(e);
        }

        System.out.println("\nOrdenado por edad:");
        estudiantes.sort(Comparator.comparingInt(Estudiante::getEdad));
        for (Estudiante e : estudiantes) {
            System.out.println(e);
        }
    }
}
