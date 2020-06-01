from codigo import gini_impurity

class Student:
    def __init__(self, codigo, data, exito):
        self.codigo = codigo
        self.data = data
        self.exito = exito


def get_all_students(data_location):
    students = {}
    list_students = []
    #creates and fills dictionary of students and their info
    with open(data_location, encoding='utf-8', mode='r') as file:
        next(file)

        for i, row in enumerate(file):
            data = row.split(";")
            # No es necesario prealocar el espacio para el diccionario porque tiene cercano a O(1) de insercion
            list_students.append(data[0])
            students[data[0]] = Student(data[0], data_sorter(data[1:len(data)-1]), data_corrector_boolean(data[len(data)-1]))

    return students, 76, list_students

def data_sorter(data):
    for i, value in enumerate(data):
        if i == 0:
            #estu_exterior, boolean
            data[0] = data_corrector_boolean(value)
        elif i == 1:
            #periodo, ranked
            value = int(value)
            if value == 20143: data[1] = 1
            elif value == 20152: data[1] = 2
            elif value == 20153: data[1] = 3
            elif value == 20162: data[1] = 4
            elif value == 20163: data[1] = 5
            elif value == 20172: data[1] = 6
            elif value == 20173: data[1] = 7
            elif value == 20182: data[1] = 8
            elif value == 20183: data[1] = 9
        elif i == 2:
            #estu_tieneetnia, boolean
            data[2] = data_corrector_boolean(value)
        elif i == 3:
            #estu_tomo_cursopreparacion, boolean
            data[3] = data_corrector_boolean(value)
        elif i == 4:
            #estu_cursodocentesies, ranked
            if value == 'No tomó Curso': data[4] = 1
            elif value == 'Menos de 20 horas': data[4] = 2
            elif value == 'Entre 20 y 30 horas': data[4] = 3
            elif value == 'Más de 30 horas': data[4] = 4
        elif i == 5:
            #estu_cursoiesapoyoexterno, ranked
            if value == 'No tomó Curso': data[5] = 1
            elif value == 'Menos de 20 horas': data[5] = 2
            elif value == 'Entre 20 y 30 horas': data[5] = 3
            elif value == 'Más de 30 horas': data[5] = 4
        elif i == 6:
            #estu_cursoiesexterna, ranked
            if value == 'No tomó curso': data[6] = 1
            elif value == 'Menos de 20 horas': data[6] = 2
            elif value == 'Entre 20 y 30 horas': data[6] = 3
            elif value == 'Más de 30 horas': data[6] = 4
        elif i == 7:
            #estu_simulacrotipoicfes, boolean
            data[7] = data_corrector_boolean(value)
        elif i == 8:
            #estu_actividadrefuerzoareas, boolean
            data[8] = data_corrector_boolean(value)
        elif i == 9:
            #estu_actividadrefuerzogeneric, boolean
            data[9] = data_corrector_boolean(value)
        elif i == 10:
            #fami_trabajolaborpadre, cualitative
            continue
        elif i == 11:
            #fami_trabajolabormadre, cualitative
            continue
        elif i == 12:
            #fami_numlibros, ranked
            if value == '0 A 10 LIBROS': data[12] = 1
            elif value == '11 A 25 LIBROS': data[12] = 2
            elif value == '26 A 100 LIBROS': data[12] = 3
            elif value == 'MÁS DE 100 LIBROS': data[12] = 4
        elif i == 13:
            #estu_inst_cod_departamento, cualititative
            continue
        elif i == 14:
            #estu_tipodocumento.1, cualitativa
            continue
        elif i == 15:
            #estu_nacionalidad.1, cualitativa
            continue
        elif i == 16:
            #estu_genero.1, cualitativa
            continue
        elif i == 17:
            #estu_fechanacimiento.1, revisar
            continue
        elif i == 18:
            # periodo.1, ranked
            value = int(value)
            if value == 20121: data[18] = 1
            elif value == 20122: data[18] = 2
            elif value == 20131: data[18] = 3
            elif value == 20132: data[18] = 4
            elif value == 20132: data[18] = 5
        elif i == 19:
            # estu_estudiante.1, cualitative
            continue
        elif i == 20:
            #estu_pais_reside.1, cualitative
            continue
        elif i == 21:
            #estu_depto_reside.1, cualitative
            continue
        elif i == 22:
            #estu_cod_reside_depto.1, cualitative
            continue
        elif i == 23:
            #estu_mcpio_reside.1, cualitative
            continue
        elif i == 24:
            #estu_cod_reside_mcpio.1, cualitative
            continue
        elif i == 25:
            #estu_areareside, cualitative
            continue
        elif i == 26:
            #estu_valorpensioncolegio, ranked
            if value == 'No paga Pensión': data[26] = 1
            elif value == 'Menos de 87.000': data[26] = 2
            elif value == 'Entre 87.000 y menos de 120.000': data[26] = 3
            elif value == 'Entre 120.000 y menos de 150.000':data[26] = 4
            elif value == 'Entre 150.000 y menos de 250.000': data[26] = 5
            elif value == '250.000 o más': data[26] = 6
        elif i == 27:
            #fami_educacionpadre.1, ranked
            if value == 'Ninguno': data[27] = 0
            elif value == 'Primaria incompleta': data[27] = 1
            elif value == 'Primaria completa': data[27] = 2
            elif value == 'Secundaria (Bachillerato) incompleta': data[27] = 3
            elif value == 'Secundaria (Bachillerato) completa': data[27] = 4
            elif value == 'Técnica o tecnológica incompleta': data[27] = 5
            elif value == 'Educación profesional incompleta': data[27] = 6
            elif value == 'Técnica o tecnológica completa': data[27] = 7
            elif value == 'Educación profesional completa': data[27] = 8
            elif value == 'Postgrado': data[27] = 9
            elif value == 'No sabe': data[27] = ''
        elif i == 28:
            #fami_educacionmadre.1, ranked
            if value == 'Ninguno': data[28] = 0
            elif value == 'Primaria incompleta': data[28] = 1
            elif value == 'Primaria completa': data[28] = 2
            elif value == 'Secundaria (Bachillerato) incompleta': data[28] = 3
            elif value == 'Secundaria (Bachillerato) completa': data[28] = 4
            elif value == 'Técnica o tecnológica incompleta': data[28] = 5
            elif value == 'Educación profesional incompleta': data[28] = 6
            elif value == 'Técnica o tecnológica completa': data[28] = 7
            elif value == 'Educación profesional completa': data[28] = 8
            elif value == 'Postgrado': data[28] = 9
            elif value == 'No sabe': data[28] = ''
        elif i == 29:
            #fami_ocupacionpadre.1, cualitative
            continue
        elif i == 30:
            #fami_ocupacionmadre.1, cualitative
            continue
        elif i == 31:
            #fami_estratovivienda.1, ranked
            if value == 'Estrato 1': data[31] = 1
            elif value == 'Estrato 2': data[31] = 2
            elif value == 'Estrato 3': data[31] = 3
            elif value == 'Estrato 4': data[31] = 4
            elif value == 'Estrato 5': data[31] = 5
            elif value == 'Estrato 6': data[31] = 6
        elif i == 32:
            # fami_nivelsisben, cualitative
            continue
        elif i == 33:
            if value == 'Tierra, arena': data[33] = 1
            elif value == 'Madera burda, tabla, tablón': data[33] = 2
            elif value == 'Cemento, gravilla, ladrillo': data[33] = 3
            elif value == 'Madera pulida, baldosa, tableta, mármol, alfombra': data[33] = 4
        elif i == 34:
            #fami_tieneinternet.1, boolean
            data[34] = data_corrector_boolean(value)
        elif i == 35:
            # fami_tienecomputador.1, boolean
            data[35] = data_corrector_boolean(value)
        elif i == 36:
            # fami_tienemicroondas, boolean
            data[36] = data_corrector_boolean(value)
        elif i == 37:
            # fami_tienehorno, boolean
            data[37] = data_corrector_boolean(value)
        elif i == 38:
            # fami_tieneautomovil.1, boolean
            data[38] = data_corrector_boolean(value)
        elif i == 39:
            # fami_tienedvd, boolean
            data[39] = data_corrector_boolean(value)
        elif i == 40:
            # fami_tiene_nevera.1, boolean
            data[40] = data_corrector_boolean(value)
        elif i == 41:
            # fami_tiene_celular.1, boolean
            data[41] = data_corrector_boolean(value)
        elif i == 42:
            # fami_telefono.1, boolean
            data[42] = data_corrector_boolean(value)
        elif i == 43:
            if value == 'Menos de 1 SMLV': data[43] = 1
            elif value == 'Entre 1 y menos de 2 SMLV': data[43] = 2
            elif value == 'Entre 2 y menos de 3 SMLV': data[43] = 3
            elif value == 'Entre 3 y menos de 5 SMLV': data[43] = 4
            elif value == 'Entre 5 y menos de 7 SMLV': data[43] = 5
            elif value == 'Entre 7 y menos de 10 SMLV': data[43] = 6
            elif value == '10 o más SMLV': data[43] = 7
        elif i == 44:
            if value == 'No': data[44] = 1
            elif value == 'Si, menos de 20 horas a la semana': data[44] = 2
            elif value == 'Si, 20 horas o más a la semana': data[44] = 3
        elif i == 45:
            # estu_antecedentes, boolean
            data[45] = data_corrector_boolean(value)
        elif i == 46:
            # estu_expectativas, boolean
            data[46] = data_corrector_boolean(value)
        elif i == 47:
            # cole_codigo_icfes, cualitative
            continue
        elif i == 48:
            # cole_cod_dane_establecimiento, cualitative
            continue
        elif i == 49:
            # cole_nombre_establecimiento, cualitative
            continue
        elif i == 50:
            # cole_genero, cualitative
            continue
        elif i == 51:
            # cole_naturaleza, cualitative, ask
            continue
        elif i == 52:
            # cole_calendario, cualitative
            continue
        elif i == 53:
            # cole_bilingue, boolean
            data[53] = data_corrector_boolean(value)
            pass
        elif i == 54:
            # cole_caracter, cualitative, ask
            continue
        elif i == 55:
            # cole_cod_dane_sede, cualitative
            continue
        elif i == 56:
            # cole_nombre_sede, cualitative
            continue
        elif i == 57:
            # cole_sede_principal, boolean
            data[57] = data_corrector_boolean(value)
        elif i == 58:
            # cole_area_ubicacion, cualitative
            continue
        elif i == 59:
            # cole_jornada, cualitative
            continue
        elif i == 60:
            # cole_cod_mcpio_ubicacion, cualitative
            continue
        elif i == 61:
            # cole_mcpio_ubicacion, cualitative
            if value == 'BOGOTÁ, D.C.':
                data[61] = 'BOGOTÁ D.C.'
            continue
        elif i == 62:
            # cole_cod_depto_ubicacion, cualitative
            continue
        elif i == 63:
            # cole_depto_ubicacion, cualitative
            continue
        elif i == 64:
            # punt_lenguaje, numeric
            data[64] = (value)
        elif i == 65:
            # punt_matematicas
            data[65] = float(value)
        elif i == 66:
            #punt_biologia
            data[66] = float(value)
        elif i == 67:
            # punt_quimica
            data[67] = float(value)
        elif i == 68:
            # punt_fisica
            data[68] = float(value)
        elif i == 69:
            # punt_ciencias_sociales
            data[69] = float(value)
        elif i == 70:
            # punt_filosofia
            data[70] = float(value)
        elif i == 71:
            # punt_ingles
            data[71] = float(value)
        elif i == 72:
            # desemp_ingles, ranked
            if value == 'A-': data[72] = 1
            elif value == 'A1': data[72] = 2
            elif value == 'A2': data[72] = 3
            elif value == 'B1': data[72] = 4
            elif value == 'B+': data[72] = 5
        elif i == 73:
            # profundiza, cualitative
            continue
        elif i == 74:
            #puntaje_prof
            data[74] = float(value)
        elif i == 75:
            #desemp_prof, cualatative, no idea?
            pass
    return data

def data_corrector_boolean(value):
    #turns SI into true and NO into false
    if value.upper() == 'NO' or value.upper() =='N' or value == '0\n':
        return False
    elif value.upper() == 'SI' or value.upper() =='S' or value.upper() =='SÍ' or value == '1\n':
        return True
    else:
        return ''
