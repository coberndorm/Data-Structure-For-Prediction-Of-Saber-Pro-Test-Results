from codigo import lectura_datos


def test_get_all_students():
    all_students = lectura_datos.get_all_students()
    assert isinstance(all_students, dict)
    for codigo in all_students:
        assert isinstance(all_students[codigo], lectura_datos.Student)
        break
