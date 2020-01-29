import COMPLEJOS as c
def test_suma():
    assert c.suma([-3,2],[4,1])==[1,3], 'Debe ser 1+3i'
def test_resta():
    assert c.resta([5,2],[7,1])==[-2,-1], 'Debe ser -2-1i'
def test_producto():
    assert c.producto([-7,3],[-2,3]) == [5,-27], 'Debe ser 5-27i'
def test_division():
    assert c.division([-3,-2],[5,4]) == [7/41,-22/41], 'Debe ser 7/41 -22/41 i'
def test_conjugado():
    assert c.conjugado([-3,7]) == [-3,-7], 'Debe ser -3-7i'
def test_modulo():
    assert c.modulo([-3,7]) == [(58)**(1/2)], 'Debe ser (58)^(1/2) '
def test_Bin_polar(self):
    assert c.Bin_polar([5,8]),(9.433981132056603,57.9946167919165))
def test_polar_Bin(self):
    assert c.polar_Bin(78,69),(77.48444961833718,-8.953215475088603))
def test_fas(self):
     assert c.fase([5,8]),57.9946167919165)

if __name__=="__main__":
    test_suma()
    test_producto()
    print('prueba exitosa')
