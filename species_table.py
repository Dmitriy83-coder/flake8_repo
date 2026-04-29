from sqlalchemy import create_engine, text
from db_config import CONNECTION_STRING


class SpeciesTable:
    """класс для работы с таблицей species_type"""

    _scripts = {
        "select_all": text(
            "SELECT * FROM species_type ORDER BY type_id"
        ),
        "select_by_id": text(
            "SELECT * FROM species_type WHERE type_id = :species_id"
        ),
        "select_by_name": text(
            "SELECT * FROM species_type WHERE type_name = :name"
        ),
        "insert": text(
            "INSERT INTO species_type (type_id, type_name) "
            "VALUES ((SELECT COALESCE(MAX(type_id), 0) + 1 FROM species_type), :name) "
            "RETURNING type_id"
        ),
        "update": text(
            "UPDATE species_type SET type_name = :name "
            "WHERE type_id = :species_id"
        ),
        "delete": text(
            "DELETE FROM species_type WHERE type_id = :species_id"
        ),
        "delete_by_name": text(
            "DELETE FROM species_type WHERE type_name = :name"
        ),
        "count": text("SELECT COUNT(*) as count FROM species_type"),
    }

    def __init__(self, connection_string):
        """инициализация подключения к БД"""
        self.engine = create_engine(connection_string, echo=False)

    def get_all_species(self):
        """получить все виды"""
        with self.engine.connect() as conn:
            result = conn.execute(self._scripts["select_all"])
            rows = result.mappings().all()
            return rows

    def get_species_by_id(self, species_id):
        """получить по ID"""
        with self.engine.connect() as conn:
            result = conn.execute(
                self._scripts["select_by_id"],
                {"species_id": species_id}
            )
            row = result.mappings().first()
            return row

    def get_species_by_name(self, name):
        """получить вид по названию"""
        with self.engine.connect() as conn:
            result = conn.execute(
                self._scripts["select_by_name"],
                {"name": name}
            )
            row = result.mappings().first()
            return row

    def add_species(self, name):
        """добавить новый вид"""
        with self.engine.connect() as conn:
            result = conn.execute(self._scripts["insert"], {"name": name})
            new_id = result.fetchone()[0]
            conn.commit()
            return new_id

    def update_species(self, species_id, new_name):
        """обновить название вида"""
        with self.engine.connect() as conn:
            result = conn.execute(
                self._scripts["update"],
                {"species_id": species_id, "name": new_name}
            )
            conn.commit()
            return result.rowcount > 0

    def delete_species(self, species_id):
        """удалить вид по ID"""
        with self.engine.connect() as conn:
            result = conn.execute(
                self._scripts["delete"],
                {"species_id": species_id}
            )
            conn.commit()
            return result.rowcount > 0

    def delete_species_by_name(self, name):
        """удалить вид по названию"""
        with self.engine.connect() as conn:
            result = conn.execute(
                self._scripts["delete_by_name"],
                {"name": name}
            )
            conn.commit()
            return result.rowcount > 0

    def get_count(self):
        """получить количество записей"""
        with self.engine.connect() as conn:
            result = conn.execute(self._scripts["count"])
            return result.fetchone()[0]
