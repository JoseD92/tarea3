'''
Created on Jan 29, 2015

@author: Jose Daniel
'''
import unittest
from terea3 import reserva


class Test(unittest.TestCase):


    def testName(self):
        pass
    
    def testNoReserva(self):
        reservas = reserva()
        msg = 'no reservas'
        self.assertEqual(True, reservas.validar(), msg)
        
    def testAceptaAdd(self):
        reservas = reserva()
        reservas.addReserva("0900", "1800")
        msg = "agrego"
        self.assertEqual(reservas.lista, [(900,1),(1800,-1)], msg)
        
    def testAceptaAdd2(self):
        reservas = reserva()
        reservas.addReserva("0900", "0900")
        msg = "agrego2"
        self.assertEqual(reservas.lista, [(900,1),(900,-1)], msg)
    
    def testNoAceptaAdd(self):
        reservas = reserva()
        msg = "no debe agregar"
        self.assertRaises(ValueError,reservas.addReserva,"0900","0600")
        
    def testUnaReserva(self):
        reservas = reserva()
        reservas.addReserva("0900", "1800")
        msg = 'una reservas'
        self.assertEqual(True, reservas.validar(), msg)
        
    def testDosReserva(self):
        reservas = reserva()
        reservas.addReserva("0900", "1800")
        reservas.addReserva("0900", "1800")
        msg = 'dos reservas'
        self.assertEqual(True, reservas.validar(), msg)

    def testTresReserva(self):
        reservas = reserva()
        reservas.addReserva("0900", "1800")
        reservas.addReserva("0900", "1800")
        reservas.addReserva("0900", "1800")
        msg = 'tres reservas'
        self.assertEqual(True, reservas.validar(), msg)
        
    def testdiesReserva(self):
        reservas = reserva()
        reservas.addReserva("0900", "1800")
        reservas.addReserva("0900", "1800")
        reservas.addReserva("0900", "1800")
        reservas.addReserva("0900", "1800")
        reservas.addReserva("0900", "1800")
        reservas.addReserva("0900", "1800")
        reservas.addReserva("0900", "1800")
        reservas.addReserva("0900", "1800")
        reservas.addReserva("0900", "1800")
        reservas.addReserva("0900", "1800")
        msg = 'dies reservas'
        self.assertEqual(True, reservas.validar(), msg)
        
    def testOnceReserva(self):
        reservas = reserva()
        reservas.addReserva("0900", "1800")
        reservas.addReserva("0900", "1800")
        reservas.addReserva("0900", "1800")
        reservas.addReserva("0900", "1800")
        reservas.addReserva("0900", "1800")
        reservas.addReserva("0900", "1800")
        reservas.addReserva("0900", "1800")
        reservas.addReserva("0900", "1800")
        reservas.addReserva("0900", "1800")
        reservas.addReserva("0900", "1800")
        msg = 'dies reservas'
        self.assertEqual(True, reservas.validar(), msg)
        reservas.addReserva("0900", "1800")
        msg = 'once reservas'
        self.assertEqual(False, reservas.validar(), msg)
        
    def testOnceReservaNoChocan(self):
        reservas = reserva()
        reservas.addReserva("0900", "1800")
        reservas.addReserva("0900", "1800")
        reservas.addReserva("0900", "1800")
        reservas.addReserva("0900", "1800")
        reservas.addReserva("0900", "1800")
        reservas.addReserva("0900", "1800")
        reservas.addReserva("0900", "1800")
        reservas.addReserva("0900", "1800")
        reservas.addReserva("0900", "1800")
        reservas.addReserva("0900", "1800")
        msg = 'dies reservas'
        self.assertEqual(True, reservas.validar(), msg)
        reservas.addReserva("0600", "0900")
        msg = 'once reservas'
        self.assertEqual(True, reservas.validar(), msg)
        
    def testReservasEntraSale(self):
        reservas = reserva()
        reservas.addReserva("0900", "1800")
        reservas.addReserva("0900", "1800")
        reservas.addReserva("0900", "1800")
        reservas.addReserva("0900", "1800")
        reservas.addReserva("0900", "1800")
        reservas.addReserva("0900", "1800")
        reservas.addReserva("0900", "0900")
        reservas.addReserva("1000", "1000")
        reservas.addReserva("1100", "1100")
        reservas.addReserva("0900", "1800")
        reservas.addReserva("0900", "1800")
        reservas.addReserva("0900", "1800")
        reservas.addReserva("0900", "1800")
        msg = 'dies reservas'
        self.assertEqual(True, reservas.validar(), msg)
        reservas.addReserva("0600", "0900")
        msg = 'once reservas'
        self.assertEqual(True, reservas.validar(), msg)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()