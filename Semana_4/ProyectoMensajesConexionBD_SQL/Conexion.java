package inicio;
import java.sql.Connection;
import java.sql.DriverManager;


public class Conexion {

	public Connection get_conection() {
		Connection connection = null; 
		try {
			connection = DriverManager.getConnection("jdbc:mysql://sql10.freesqldatabase.com","sql10760148","ZTwrQpnyHr");
			if (connection != null) {
				System.out.println("Conexion exitosa");
			}
		}
		catch(Exception e){
			System.out.println(e);
			
		}
		return connection;
	}
}
