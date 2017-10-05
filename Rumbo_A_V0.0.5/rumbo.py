# -*- coding: utf-8 -*-

# sintaxis for Python 2.7

from random import randint
import jugador
from jugador import Jugador

comand = jugador.Comandos

def main():

    jug = Jugador()
    jug.nombre = raw_input("¿Cual es tu nombre viager@? : ")
    print "escribe: 'ayuda' para ver una lista de acciones.\n"
    print "%s se adentra en una oscura cueva, en busca de aventuras."% jug.nombre

    while (jug.salud > 0):

        linea = raw_input("> ")
        arg = linea.split()

        if len(arg) > 0:

            comando_valido = False

            for c in comand.keys():
                if arg[0] == c[: len(arg[0])]:
                    comand[c](jug)
                    comando_valido = True
                    break
            if not comando_valido:
                print "%s no entiende tu sugerencia.\n(escribe 'ayuda' para obtener una lista de opciones.)"% jug.nombre


if __name__ == '__main__':
    main()


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
