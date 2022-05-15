#include <iostream>
#include <HarmonicOscillator.h>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main(){
    HarmonicOscillator h1(0.5, 5, 0.1);
    h1.gibanje();

    float x1, v1, a1, t1;
    int n = h1.t_list.size();
    x1 = h1.x_list[0];
    v1 = h1.v_list[0];
    a1 = h1.a_list[0];
    t1 = h1.t_list[0];

    string x_string, v_string, a_string, t_string;

    x_string = to_string(x1);
    v_string = to_string(v1);
    a_string = to_string(a1);
    t_string = to_string(t1);

    for (int i = 1; i < n; i++){
        x_string += "," + to_string(h1.x_list[i]);
        v_string += "," + to_string(h1.v_list[i]);
        a_string += "," + to_string(h1.a_list[i]);
        t_string += "," + to_string(h1.t_list[i]);
    };
    ofstream myfile;
    myfile.open ("x.txt");
    myfile << x_string;
    myfile.close();
    myfile.open ("v.txt");
    myfile << v_string;
    myfile.close();
    myfile.open ("a.txt");
    myfile << a_string;
    myfile.close();
    myfile.open ("t.txt");
    myfile << t_string;
    myfile.close();
    return 0;
}