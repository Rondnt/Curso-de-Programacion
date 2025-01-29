package semana3;

import java.util.ArrayList;
import java.util.Collections;

public class Empleado implements Comparable<Empleado> {
    private String nombre;
    private double salario;
    private int antigüedad;

    public Empleado(String nombre, double salario, int antigüedad) {
        this.nombre = nombre;
        this.salario = salario;
        this.antigüedad = antigüedad;
    }

    public String getNombre() {
        return nombre;
    }

    public double getSalario() {
        return salario;
    }

    public int getAntigüedad() {
        return antigüedad;
    }

    @Override
    public int compareTo(Empleado otro) {
        if (Double.compare(otro.salario, this.salario) == 0) {
            return this.nombre.compareTo(otro.nombre);
        }
        return Double.compare(otro.salario, this.salario);
    }

    @Override
    public String toString() {
        return "Empleado{" +
                "nombre='" + nombre + '\'' +
                ", salario=" + salario +
                ", antigüedad=" + antigüedad +
                '}';
    }

    public static void main(String[] args) {
     
        ArrayList<Empleado> empleados = new ArrayList<>();
        empleados.add(new Empleado("Estefania", 4100.0, 5));
        empleados.add(new Empleado("Isabel", 3500.0, 4));
        empleados.add(new Empleado("Alexis", 1400.0, 3));
        empleados.add(new Empleado("Thalía", 5200.0, 2));
        empleados.add(new Empleado("Carmen", 1400.0, 5));
        empleados.add(new Empleado("Thamara", 4200.0, 2));

        System.out.println("Empleados ordenados por salario descendente (y por nombre si el salario es igual):");
        Collections.sort(empleados);
        for (Empleado e : empleados) {
            System.out.println(e);
        }
    }
}
