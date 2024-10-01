#include <iostream>
#include <string>
using namespace std;

class Vector2{
	private:
		int componente1 = 0;
		int componente2 = 0;
	public:
		//Constructor por defecto
		Vector2(){};	
		//Constructor por ambos componentes
		Vector2(int componentePrimero, int componenteSegundo): componente1(componentePrimero), componente2(componenteSegundo){};
		//Getters
		int getComponente1(){
			return componente1;
		}
		int getComponente2(){
			return componente2;
		}
		//Setter
		void setComponentes(int componentePrimero, int componenteSegundo){
			this->componente1 = componentePrimero;
			this->componente2 = componenteSegundo;
		}
		//Metodos
		Vector2 sumaVectores2(Vector2 vector2sumado){
			int componentex = this->componente1 + vector2sumado.getComponente1();
			int componentey = this->componente2 + vector2sumado.getComponente2();
			Vector2 vector2Nuevo = Vector2(componentex, componentey);
			return vector2Nuevo;
		}
		Vector2 restaVectores2(Vector2 vector2restado){
        int componentex = componente1 - vector2restado.getComponente1();
        int componentey = componente2 - vector2restado.getComponente2();
        return Vector2(componentex, componentey);}
};
class Vector3{
	private:
		int componente1 = 0;
		int componente2 = 0;
		int componente3 = 0;
	public:
		//Constructor por defecto
		Vector3(){};
		//Constructor por ambos componentes
		Vector3(int componentePrimero, int componenteSegundo, int componenteTercero): componente1(componentePrimero), componente2(componenteSegundo), componente3(componenteTercero){};
		//Getters
		int getComponente1(){
			return componente1;
		}
		int getComponente2(){
			return componente2;
		}
		int getComponente3(){
			return componente3;
		}
		//Setter
		void setComponentes(int componentePrimero, int componenteSegundo, int componenteTercero){
			this->componente1 = componentePrimero;
			this->componente2 = componenteSegundo;
			this->componente3 = componenteTercero;
		}
		//Metodos
		Vector3 sumaVectores3(Vector3 vector3sumado){
			int componentex = this->componente1 + vector3sumado.getComponente1();
			int componentey = this->componente2 + vector3sumado.getComponente2();
			int componentez = this->componente3 + vector3sumado.getComponente3();
			return Vector3(componentex, componentey, componentez);
		}
		Vector3 restaVectores3(Vector3 vector3Resta){
			int componentex = this->componente1 - vector3Resta.getComponente1();
			int componentey = this->componente2 - vector3Resta.getComponente2();
			int componentez = this->componente3 - vector3Resta.getComponente3();
			Vector3 vector3Nuevo = Vector3(componentex, componentey, componentez);
			return vector3Nuevo;
		}
};
int main(){
	// Ejemplo de uso de las clases
    Vector2 v1(1, 2);
    Vector2 v2(3, 4);
    Vector2 v3 = v1.sumaVectores2(v2);
    Vector2 v4 = v1.restaVectores2(v2);

    cout << "Vector2 suma: (" << v3.getComponente1() << ", " << v3.getComponente2() << ")" << endl;
    cout << "Vector2 resta: (" << v4.getComponente1() << ", " << v4.getComponente2() << ")" << endl;

    Vector3 u1(1, 2, 3);
    Vector3 u2(4, 5, 6);
    Vector3 u3 = u1.sumaVectores3(u2);
    Vector3 u4 = u1.restaVectores3(u2);

    cout << "Vector3 suma: (" << u3.getComponente1() << ", " << u3.getComponente2() << ", " << u3.getComponente3() << ")" << endl;
    cout << "Vector3 resta: (" << u4.getComponente1() << ", " << u4.getComponente2() << ", " << u4.getComponente3() << ")" << endl;

    return 0;
}