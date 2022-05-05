#include <iostream>
#include <Particle.h>
#include <math.h>

#define pi 3.14159265

using namespace std;

void Particle::move(){
    t = t + dt;
    vy = vy + a*dt;
    x = x + vx*dt;
    y = y + vy*dt;
}

Particle::Particle(double v0, double theta, double x0, double y0, double korak){
    t = 0;
    x = x0;
    y = y0;
    vx = v0*cos(theta*pi/180);
    vy = v0*sin(theta*pi/180);
    dt = korak;
}

Particle::~Particle(){
}

double Particle::range(){
    while (y >= 0){
        move();
    }
    return x;
}

double Particle::time(){
    while (y >= 0){
        move();
    }
    return t;
}