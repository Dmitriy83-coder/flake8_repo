import pytest
from species_table import SpeciesTable
from db_config import CONNECTION_STRING


@pytest.fixture
def db():
    species_db = SpeciesTable(CONNECTION_STRING)
    yield species_db

@pytest.fixture
def test_species(db):
    """cоздаём тестовую запись и удаляем после теста"""
    test_name = "насекомые"

    # проверяем, существует ли уже такая запись
    existing = db.get_species_by_name(test_name)
    if existing:
        db.delete_species_by_name(test_name)

    # создаём тестовую запись
    species_id = db.add_species(test_name)

    yield {"id": species_id, "name": test_name}

    # очистка после теста
    try:
        db.delete_species(species_id)
    except:
        pass


def test_get_all_species(db):
    """тестим получение всех видов из таблицы"""
    species_list = db.get_all_species()

    # проверяем, что список не пустой
    assert len(species_list) > 0

    # проверяем наличие ожидаемых данных
    expected_species = ["человек", "животные", "птицы", "рыбы", "цветы", "фрукты", "ягоды"]
    actual_names = [s["type_name"] for s in species_list]

    for expected in expected_species:
        assert expected in actual_names, f"В таблице отсутствует вид '{expected}'"


def test_add_species(db):
    """тестим добавления новой сущности"""
    # Подготовка тестовых данных
    new_species_name = "земноводные"

    # проверяем, что такого вида ещё нет
    existing = db.get_species_by_name(new_species_name)
    if existing:
        db.delete_species_by_name(new_species_name)

    # получаем количество записей до добавления
    count_before = db.get_count()

    # добавляем новый вид
    new_id = db.add_species(new_species_name)

    # проверяем, что ID получен
    assert new_id is not None
    assert new_id > 0

    # что количество записей увеличилось
    count_after = db.get_count()
    assert count_after == count_before + 1

    # что вид добавился с правильными данными
    added_species = db.get_species_by_id(new_id)
    assert added_species is not None
    assert added_species["type_name"] == new_species_name

    # очистка
    db.delete_species(new_id)

    # что вид удалён
    count_final = db.get_count()
    assert count_final == count_before


def test_update_species(db, test_species):
    """тестим изменения существующей сущности"""
    # готовим тест данных
    species_id = test_species["id"]
    old_name = test_species["name"]
    new_name = "членистоногие"

    # проверяем исходное название
    species_before = db.get_species_by_id(species_id)
    assert species_before["type_name"] == old_name

    # обновляем его
    result = db.update_species(species_id, new_name)

    # проверяем успешность
    assert result is True

    # проверяем название
    species_after = db.get_species_by_id(species_id)
    assert species_after is not None
    assert species_after["type_name"] == new_name
    assert species_after["type_name"] != old_name

    # возвращаем исходное название 
    db.update_species(species_id, old_name)


def test_delete_species(db):
    """тестим удаление сущности"""
    # Подготовка тестовых данных
    test_name = "временный_вид"

    # убеждаемся, что такого нет
    existing = db.get_species_by_name(test_name)
    if existing:
        db.delete_species_by_name(test_name)

    # количество записей до добавления
    count_before = db.get_count()

    # добавляем вид для удаления
    new_id = db.add_species(test_name)

    # проверяем, что вид добавился
    added = db.get_species_by_id(new_id)
    assert added is not None
    assert added["type_name"] == test_name

    # проверяем, что количество увеличилось
    count_after_add = db.get_count()
    assert count_after_add == count_before + 1

    # Удаляем вид
    result = db.delete_species(new_id)

    # проверяем успешность
    assert result is True

    # проверяем, что вид удалён
    deleted = db.get_species_by_id(new_id)
    assert deleted is None

    # проверяем, что количество вернулось к исходному
    count_after_delete = db.get_count()
    assert count_after_delete == count_before


def test_add_duplicate_species(db):
    """тестим добавление дубликата (негатив)"""
    test_name = "млекопитающие"

    # убеждаемся, что такого вида нет
    existing = db.get_species_by_name(test_name)
    if existing:
        db.delete_species_by_name(test_name)

    # добавляем первый раз
    first_id = db.add_species(test_name)
    assert first_id is not None

    # пытаемся добавить второй раз (должно вызвать ошибку или None)
    try:
        second_id = db.add_species(test_name)
        # если БД позволяет дубликаты- удаляем второй
        if second_id:
            db.delete_species(second_id)
    except Exception as e:
        print(f"ожидаемая ошибка при дублировании: {e}")

    # очищаем
    db.delete_species(first_id)


def test_get_species_by_id(db):
    """тестим получения вида по ID"""
    # получаем первый вид из таблицы
    all_species = db.get_all_species()

    if len(all_species) > 0:
        first_species = all_species[0]
        species_id = first_species["type_id"]
        expected_name = first_species["type_name"]

        # получаем вид по ID
        found = db.get_species_by_id(species_id)

        assert found is not None
        assert found["type_id"] == species_id
        assert found["type_name"] == expected_name


def test_get_nonexistent_species(db):
    """тестим получение несуществующего вида"""
    nonexistent_id = 99999
    result = db.get_species_by_id(nonexistent_id)
    assert result is None
