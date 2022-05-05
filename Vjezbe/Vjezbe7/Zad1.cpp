#include <iostream>
#include <Particle.h>

using namespace std;
float d1, t1, d2, t2;

int main(){
    Particle p1(10, 45, 0, 0);
    Particle p2(40, 60, 0, 0);
    d1 = p1.range();
    t1 = p1.time();
    d2 = p2.range();
    t2 = p2.time();
    cout << "Domet prvog tijela je " << d1 << " metara." << std::endl;
    cout << "Vrijeme gibanja prvog tijela je  " << t1 << " sekundi." << std::endl;
    cout << "Domet drugog tijela je  " << d2 << " metara." << std::endl;
    cout << "Vrijeme gibanja drugog tijela je  " << t2 << " sekundi." << std::endl;
}