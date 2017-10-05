# -*- coding: utf-8 -*-

from random import randint
from personage import Personage
from criaturas import Enemigo

class Jugador(Personage):

    def __init__(self):

        Personage.__init__(self)
        self.modo = 'normal'
        self.salud = 10
        self.salud_max = 10


    def salir(self):

        print ("%s no puede encontrar el camino de vuelta y muere de hambre.\nR.I.P."% self.nombre)
        self.salud = 0


    def ayuda(self):

        print (Comandos.keys())


    def estado(self):

        print ("%s SALUD: %d/%d"% (self.nombre, self.salud, self.salud_max))


    def cansado(self):

        print ("%s se siente cansado.\n(pierdes 1 de salud)"% self.nombre)
        self.salud = max(1, self.salud - 1)


    def descanso(self):

        if self.modo != 'normal':
            print ("¡%s no puede descansar ahora!"% self.nombre)
            self.enemigo_ataca()
        else:
            if randint(0, 1):
                self.enemigo = Enemigo(self)
                print ("¡¡%s ha sido groseramente despertado por %s!!"% (self.nombre, self.enemigo.nombre))
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
            print ("%s exlora un sinuoso páramo."% self.nombre)
            if randint(0, 1):
                self.enemigo = Enemigo(self)
                print ("%s se encuentra con un %s"% (self.nombre, self.enemigo.nombre))
                self.modo = 'lucha'
            else:
                if randint(0, 1):
                    self.cansado()


    def huir(self):

        if self.modo != 'lucha':
            print ("%s corre en circulos por un tiempo"% self.nombre)
            self.cansado()
        else:
            if randint(1, self.salud + 5) > randint(1, self.enemigo.salud):
                print ("%s consigue huir, cobardemente, de %s."% (self.nombre, self.enemigo.nombre))
                self.enemigo = None
                self.modo = 'normal'
            else:
                print ("¡%s se tropieza torpemente y no consigue huir de %s!"% (self.nombre, self.enemigo.nombre))
                self.enemigo_ataca()


    def ataque(self):

        if self.modo != 'lucha':
            print ("%s cierra los ojos y golpea el aire sin sentido"% self.nombre)
            self.cansado()
        else:
            if self.golpea(self.enemigo):
                print ("¡%s ha derrotado a %s!"% (self.nombre, self.enemigo.nombre))
                self.enemigo = None
                self.modo = 'normal'
                if randint(0, self.salud) < 10:
                    self.salud = self.salud + 1
                    self.salud_max = self.salud_max + 1
                    print ("¡%s se siente fuerte!"% self.nombre)
            else:
                self.enemigo_ataca()

    def enemigo_ataca(self):
        if self.enemigo.golpea(self):
            print ("¡¡¡%s ha sido ejecutado por %s!!!"% (self.nombre, self.enemigo.nombre))


Comandos = {
    'salir': Jugador.salir,
    'ayuda': Jugador.ayuda,
    'estado': Jugador.estado,
    'descanso': Jugador.descanso,
    'explorar': Jugador.explorar,
    'huir': Jugador.huir,
    'ataque': Jugador.ataque,
    }

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
