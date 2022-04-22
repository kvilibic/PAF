import Projectile as pro

p1 = pro.ProjectileDrop(100, 10)
p2 = pro.ProjectileDrop(200, 20)

p1.change_h(300)
p2.change_vx(40)

print("Nova visina prvog aviona je {} m, nakon ubrzanja brzina drugog aviona je jednaka {} m/s.".format(p1.h, p2.vx0))