odoo.define('ix_kanban_folding.ix_kanban_folding', function (require) {
"use strict";
var KanbanColumn = require('web_kanban.Column');

KanbanColumn.include({
    start: function() {
        if (this.data_records.length === 0){
            this.folded = true;
        }
        this._super.apply(this, arguments);
    },
});
});
