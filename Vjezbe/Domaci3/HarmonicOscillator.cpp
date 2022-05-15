#include <iostream>
#include <HarmonicOscillator.h>

using namespace std;

void HarmonicOscillator::move(){
    t += dt;
    a_list.push_back(-k/m*x_list.back());
    v_list.push_back(v_list.back() + a_list.back()*dt);
    x_list.push_back(x_list.back() + v_list.back()*dt);
    t_list.push_back(t);
}

HarmonicOscillator::HarmonicOscillator(double x0, double K, double M, double korak){
    m = M;
    k = K;
    a_list.push_back(-k/m*x0);
    v_list.push_back(0);
    x_list.push_back(x0);
    t_list.push_back(0);
    dt = korak;
}

HarmonicOscillator::~HarmonicOscillator(){
}

double HarmonicOscillator::gibanje(){
    while (t <= 10){
        move();
    }
    return 0;
}
