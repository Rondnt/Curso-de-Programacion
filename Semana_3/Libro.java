package semana3;

import java.util.ArrayList;
import java.util.Collections;

public class Libro implements Comparable<Libro> {
    private String titulo;
    private String autor;
    private int año;
    
    public Libro(String titulo, String autor, int año) {
        this.titulo = titulo;
        this.autor = autor;
        this.año = año;
    }
    
    public String getTitulo() {
        return titulo;
    }

    public String getAutor() {
        return autor;
    }

    public int getAño() {
        return año;
    }
    
    @Override
    public int compareTo(Libro otro) {
        return this.titulo.compareTo(otro.titulo);
    }
    
    @Override
    public String toString() {
        return "Libro{" +
                "titulo='" + titulo + '\'' +
                ", autor='" + autor + '\'' +
                ", año=" + año +
                '}';
    }

    public static void main(String[] args) {
        
        ArrayList<Libro> libros = new ArrayList<>();
        libros.add(new Libro("Orgullo y prejuicio", "Jane Austen", 1813));
        libros.add(new Libro("1984", "George Orwell", 1949));
        libros.add(new Libro("Matar a un ruiseñor", "Harper Lee", 1960));
        libros.add(new Libro("El gran Gatsby", "F. Scott Fitzgerald", 1925));
        libros.add(new Libro("Crimen y castigo", "Fiódor Dostoyevski", 1866));
        libros.add(new Libro("Harry Potter y la piedra filosofal", "J.K. Rowling", 1997));
        libros.add(new Libro("El hobbit", "J.R.R. Tolkien", 1937));
        libros.add(new Libro("Drácula", "Bram Stoker", 1897));
        
        System.out.println("Libros ordenados por título:");
        Collections.sort(libros);
        for (Libro libro : libros) {
            System.out.println(libro);
        }
    }
}
