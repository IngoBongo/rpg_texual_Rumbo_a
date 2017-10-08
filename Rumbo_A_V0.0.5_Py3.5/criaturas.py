# -*- coding: utf-8 -*-

from random2 import randint
from personage import Personage

class Trasgo(Personage):

    def __init__(self, jugador):

        Personage.__init__(self)
        self.nombre = 'Trasgo'
        self.salud = randint(3, jugador.salud_max)
        self.salud_max = self.salud
        self.velocidad = self.salud + 2
        self.fuerza = self.salud / 3
        self.info = 'Una criatura pequeña y fétida\nno los menosprecies, son muy rápidos.'


class Orco(Personage):

    def __init__(self, jugador):

        Personage.__init__(self)
        self.nombre = 'Orco'
        self.salud = randint((jugador.salud_max - 4), (jugador.salud_max * 3))
        self.salud_max = self.salud
        self.velocidad = self.salud / 2.5
        self.fuerza = self.velocidad + 2
        self.info = 'El terror causado por su tamaño no es nada\nen comparación con la idea de ser su cena.'

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
