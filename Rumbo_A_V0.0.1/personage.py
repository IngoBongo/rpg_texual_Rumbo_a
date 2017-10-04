# -*- coding: utf-8 -*-

from random import randint

class Personage:
    # cualidades generales
    def __init__(self):

        self.nombre = ""
        self.salud = 1
        self.salud_max = 1

    def golpea(self, enemigo):

        golpe = min(max(randint(0, self.salud) - randint(0, enemigo.salud), 0), enemigo.salud)
        enemigo.salud = enemigo.salud - golpe

        if golpe == 0:
            print "%s esquiva el ataque de %s."% (enemigo.nombre, self.nombre)
        else:
            print "¡%s ha dañado a %s!"% (self.nombre, enemigo.nombre)
            return enemigo.salud <= 0

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
