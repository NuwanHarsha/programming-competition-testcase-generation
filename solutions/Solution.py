PI=3.14159265359

T=int(str(input()).strip())
for t in range(T):
    radius=float(str(input()).strip())
    area=PI*radius*radius
    print("Case {}: {:.3f}".format(t,area))