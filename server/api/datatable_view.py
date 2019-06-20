from django.core.exceptions import FieldDoesNotExist
from django_datatables_view.base_datatable_view import BaseDatatableView


class DatatableView(BaseDatatableView):
    def get_column_names(self):
        column_names = []
        for c in self.columns:
            try:
                column_names.append(self.model._meta.get_field(c)._verbose_name or self._get_verbose_name(c))
            except FieldDoesNotExist:
                column_names.append(self._get_verbose_name(c))

        return column_names

    @staticmethod
    def _get_verbose_name(column):
        column = column.replace("_", " ").title()
        column = column.replace(" Id", " ID")
        return column

    def get_custom_columns(self, row, column):
        return {}

    def render_column(self, row, column):
        custom_columns = self.get_custom_columns(row, column)
        if column in custom_columns:
            return custom_columns[column]()
        return super().render_column(row, column)
