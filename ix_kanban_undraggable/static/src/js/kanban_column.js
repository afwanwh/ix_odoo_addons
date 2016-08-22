odoo.define('ix_kanban_undraggable.ix_kanban_column_undraggable', function (require) {
"use strict";
var KanbanColumn = require('web_kanban.Column');

KanbanColumn.include({
    start: function() {
        this.draggable = false;
        this._super.apply(this, arguments);
    },
});
});
