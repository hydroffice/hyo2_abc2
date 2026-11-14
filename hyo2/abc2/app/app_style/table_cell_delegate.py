from PySide6 import QtCore, QtGui, QtWidgets


# This delegate is a workaround for a bug in QtMaterial: https://github.com/UN-GCPDS/qt-material/issues/95

class TableCellDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, parent: QtCore.QObject | None = None) -> None:
        super().__init__(parent)
        self._style = QtWidgets.QStyleFactory.create("Fusion")

    def paint(self, painter: QtGui.QPainter, option: QtWidgets.QStyleOptionViewItem, index: QtCore.QModelIndex) -> None:
        roles = QtCore.Qt.ItemDataRole
        # noinspection PyTypeChecker,PyUnresolvedReferences
        selected = option.state & QtWidgets.QStyle.StateFlag.State_Selected
        has_custom_color = index.data(roles.ForegroundRole) is not None or index.data(roles.BackgroundRole) is not None

        if selected or not has_custom_color:
            super().paint(painter, option, index)
            return

        cell = QtWidgets.QStyleOptionViewItem(option)
        self.initStyleOption(cell, index)
        # noinspection PyUnresolvedReferences
        cell.features &= ~QtWidgets.QStyleOptionViewItem.ViewItemFeature.WrapText
        cell.textElideMode = QtCore.Qt.TextElideMode.ElideRight
        self._style.drawControl(QtWidgets.QStyle.ControlElement.CE_ItemViewItem, cell, painter)

    def sizeHint(self, option: QtWidgets.QStyleOptionViewItem, index: QtCore.QModelIndex) -> QtCore.QSize:
        material_size = super().sizeHint(option, index)
        roles = QtCore.Qt.ItemDataRole

        if index.data(roles.ForegroundRole) is None and index.data(roles.BackgroundRole) is None:
            return material_size

        cell = QtWidgets.QStyleOptionViewItem(option)
        self.initStyleOption(cell, index)
        fusion_size = self._style.sizeFromContents(QtWidgets.QStyle.ContentsType.CT_ItemViewItem, cell, QtCore.QSize())
        return material_size.expandedTo(fusion_size)
