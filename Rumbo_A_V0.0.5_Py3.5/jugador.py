# -*- coding: utf-8 -*-

# sintaxis for Python 3.5

from random2 import randint
from personage import Personage
from criaturas import Trasgo
from criaturas import Orco

class Jugador(Personage):

    def __init__(self):

        Personage.__init__(self)
        self.modo = 'normal'
        self.salud = 10
        self.salud_max = 10
        self.velocidad = 8
        self.fuerza = 8

    def enemigo_actual(self):
        rand_enemigo = randint(1,6)
        if rand_enemigo != (5 or 6):
            self.enemigo = Trasgo(self)
        else:
            self.enemigo = Orco(self)

    def salir(self):

        print ("%s no puede encontrar el camino de vuelta y muere de hambre."% self.nombre)
        print ("'R.I.P.'")
        self.salud = 0


    def ayuda(self):

        print (Comandos.keys())


    def estado(self):

        if self.modo != 'lucha':
            print ("%s SALUD: %d/%d Fuerza: %d Vel: %d"% (self.nombre, self.salud, self.salud_max,
                self.fuerza, self.velocidad))
        else:
            print ("%s SALUD: %d/%d Fuerza: %d Vel: %d\n%s SALUD: %d/%d Fuerza: %d Vel: %d\n"% (self.nombre, self.salud,
                self.salud_max,self.fuerza, self.velocidad, self.enemigo.nombre, self.enemigo.salud,
                self.enemigo.salud_max, self.enemigo.fuerza, self.enemigo.velocidad))
            print ("%s"% self.enemigo.info)


    def cansado(self):

        print ("%s se siente cansado.\n(pierdes 1 de salud)"% self.nombre)
        self.salud = max(1, self.salud - 1)


    def descanso(self):

        if self.modo != 'normal':
            print ("¡%s no puede descansar ahora!"% self.nombre)
            self.enemigo_ataca()
        else:
            rand_descanso = randint(1, 3)
            if rand_descanso == 1:
                self.enemigo_actual()
                print ("¡¡%s ha sido groseramente despertado por un %s!!"% (self.nombre, self.enemigo.nombre))
                self.modo = 'lucha'
                self.enemigo_ataca()
            else:
                print ("%s ha conseguido descansar"% self.nombre)
                if self.salud < self.salud_max:
                    self.salud = self.salud + 1
                else:
                    print ("%s ha dormido demasiado.(pierdes 1 de salud)"% self.nombre)
                    self.salud = self.salud - 1


    def explorar(self):

        if self.modo != 'normal':
            print ("¡%s está muy ocupado en estos momentos!"% self.nombre)
            self.enemigo_ataca()
        else:
            print ("%s explora un sinuoso páramo."% self.nombre)
            if randint(0, 1):
                self.enemigo_actual()
                print ("%s se encuentra con un %s"% (self.nombre, self.enemigo.nombre))
                self.modo = 'lucha'
            else:
                rand_cansado = randint(1, 3)
                if rand_cansado == 1:
                    self.cansado()


    def huir(self):

        if self.modo != 'lucha':
            print ("%s corre en circulos por un tiempo"% self.nombre)
            self.cansado()
        else:
            dado = 3
            huye_si = randint(1, 6)
            if self.velocidad >= self.enemigo.velocidad:
                dado = dado - 1
            elif self.enemigo.velocidad >= self.velocidad + 2:
                dado = dado + 1
                
            if huye_si > dado:
                print ("%s consigue huir, cobardemente, del %s."% (self.nombre, self.enemigo.nombre))
                self.enemigo = None
                self.modo = 'normal'
            else:
                print ("¡%s se tropieza torpemente y no consigue huir del %s!"% (self.nombre, self.enemigo.nombre))
                self.enemigo_ataca()


    def ataque(self):

        if self.modo != 'lucha':
            print ("%s cierra los ojos y golpea el aire sin sentido"% self.nombre)
            self.cansado()
        else:
            if self.golpea(self.enemigo):
                print ("¡%s ha derrotado al %s!"% (self.nombre, self.enemigo.nombre))

                if randint(0, self.salud) < 10:
                    if self.enemigo == 'Orco':
                        self.salud = self.salud + 2
                        self.salud_max = self.salud_max + 2
                        self.fuerza = self.fuerza + 2
                        self.velocidad = self.velocidad + 2
                    else:
                        self.salud = self.salud + 1
                        self.salud_max = self.salud_max + 1
                        self.fuerza = self.fuerza + 1
                        self.velocidad = self.velocidad + 1
                    print ("¡%s se siente fuerte!"% self.nombre)
                self.enemigo = None
                self.modo = 'normal'
            else:
                self.enemigo_ataca()

    def enemigo_ataca(self):
        if self.enemigo.golpea(self):
            print ("¡¡¡%s ha sido ejecutado por un %s!!!"% (self.nombre, self.enemigo.nombre))


Comandos = {
    'salir': Jugador.salir,
    'ayuda': Jugador.ayuda,
    'estado': Jugador.estado,
    'descanso': Jugador.descanso,
    'explorar': Jugador.explorar,
    'huir': Jugador.huir,
    'ataque': Jugador.ataque,
    }


def linea_punteada(width=72):
    print('-'*width)

"""
{Rumbo A... pretende ser un juego textual de aventuras}
Copyright (C) {2017}  {by Igor Iglesia Gonzalez}

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>
"""
