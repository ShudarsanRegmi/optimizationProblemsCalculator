#include <iostream>
using namespace std;

double points[5][4];

double* finding_points(double* ar, int j) {
    double temp_x1, temp_x2;
    temp_x2 = *(ar + 2) / (*(ar + 1));
    points[j][0] = 0;
    points[j][1] = temp_x2;

    temp_x1 = *(ar + 2) / (*(ar + 0));
    points[j][2] = temp_x1;
    points[j][3] = 0;
    return &points[j][0];
}

double* find_intersectionpoint(double m1, double n1, double c1, double m2, double n2, double c2) {
    static double ipoint[2];
    double determinant = (m1 * n2) - (m2 * n1);

    if (determinant == 0) {
        cout << "Constraints are parallel or coincident" << endl;
        return NULL; // Use NULL instead of nullptr
    }

    ipoint[0] = (c1 * n2 - c2 * n1) / determinant;
    ipoint[1] = (m1 * c2 - m2 * c1) / determinant;

    cout << "Intersection Point: (" << ipoint[0] << ", " << ipoint[1] << ")" << endl;
    return ipoint;
}

int main() {
    int n,n1,aaa,bbb;
    cout<<"enter coefficients of z function"<<endl;
    cin>>aaa>>bbb;
    cout << "Enter number of constraints (must be 2 for this program): ";
    cin >> n;

    if (n != 2) {
        cout << "This program only supports exactly 2 constraints." << endl;
        return 1;
    }

    double coefficients[2][3];
    int symbol[2];
    
    for (int i = 0; i < n; i++) {
        cout << "Enter coefficient of x1, x2, and constant separated by spaces for constraint " << i + 1 << endl;
        cin >> coefficients[i][0] >> coefficients[i][1] >> coefficients[i][2];
        cout << "Enter 1 for <= and 2 for >=" << endl;
        cin >> symbol[i];
        
        double* arr = &coefficients[i][0];
        double* pr = finding_points(arr, i);
        
        cout << " " << "x" << "   " << "y" << endl;
        cout << " " << *(pr + 0) << " " << *(pr + 1) << endl;
        cout << " " << *(pr + 2) << " " << *(pr + 3) << endl;
    }

    double* r = find_intersectionpoint(
        coefficients[0][0], coefficients[0][1], coefficients[0][2],
        coefficients[1][0], coefficients[1][1], coefficients[1][2]);
	int ca,cb;
    if (r != NULL) { // Check if intersection point was successfully computed
        for (int i = 0; i < n; i++) {
            double feas = (coefficients[i][0] * r[0]) + (coefficients[i][1] * r[1]);
            if ((symbol[i] == 1 && feas <= coefficients[i][2]) || (symbol[i] == 2 && feas >= coefficients[i][2])) {
            	ca=1;
                cout << "Feasible for eq " << i + 1 << endl;
            } else {
            	cb=1;
                cout << "Not feasible for eq " << i + 1 << endl;
                break;
            }
        }
    }
    if(ca==1||cb==1){
    	double z=(aaa*r[0])+(bbb*r[1]);
    	cout<<z<<endl;
	}

    return 0;
}
