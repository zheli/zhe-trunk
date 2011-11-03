App.views.UsersForm = Ext.extend(Ext.form.FormPanel, {
    defaultInstructions: 'Please enter the information above.',

    initComponent: function(){
        var titlebar, cancelButton, buttonbar, saveButton, deleteButton, fields;

        cancelButton = {
            text: 'cancel',
            ui: 'back',
            handler: this.onCancelAction,
            scope: this
        };

        titlebar = {
            id: 'userFormTitlebar',
            xtype: 'toolbar',
            title: 'Create user',
            items: [ cancelButton ]
        };

        saveButton = {
            id: 'userFormSaveButton',
            text: 'save',
            ui: 'confirm',
            handler: this.onSaveAction,
            scope: this
        };

        deleteButton = {
            id: 'userFormDeleteButton',
            text: 'delete',
            ui: 'decline',
            handler: this.onDeleteAction,
            scope: this
        };

        buttonbar = {
            xtype: 'toolbar',
            dock: 'bottom',
            items: [deleteButton, {xtype: 'spacer'}, saveButton]
        };

        fields = {
            xtype: 'fieldset',
            id: 'userFormFieldset',
            title: 'Item details',
            instructions: this.defaultInstructions,
            defaults: {
                xtype: 'textfield',
                labelAlign: 'left',
                labelWidth: '20%',
                required: false,
                useClearIcon: true,
                autoCapitalize : false
            },
            items: [
                {
                    name : 'item_title',
                    label: 'Title',
                    autoCapitalize : true
                },
                {
                    xtype: 'App.views.ErrorField',
                    fieldname: 'item_title',
                },
                {
                    name : 'item_price',
                    label: 'Price',
                    autoCapitalize : true
                },
                {
                    xtype: 'App.views.ErrorField',
                    fieldname: 'item_price',
                },
                {
                    name: 'lat',
                    label: 'Latitude',
                    xtype: 'field',
                },
                {
                    xtype: 'App.views.ErrorField',
                    fieldname: 'lat',
                },
                {
                    name: 'lon',
                    label: 'Longitude',
                    xtype: 'field',
                },
                {
                    xtype: 'App.views.ErrorField',
                    fieldname: 'lon',
                },
                {
                    name: 'image_url',
                    label: 'Image',
                    xtype: 'field',
                },
                {
                    xtype: 'App.views.ErrorField',
                    fieldname: 'image_url',
                },
                {
                    name: 'thumbnail_url',
                    label: 'Thumbnail',
                    xtype: 'field',
                },
                {
                    xtype: 'App.views.ErrorField',
                    fieldname: 'thumbnail_url',
                },
            ]
        };

        Ext.apply(this, {
            scroll: 'vertical',
            dockedItems: [ titlebar, buttonbar ],
            items: [ fields ],
            listeners: {
                beforeactivate: function() {
                    var deleteButton = this.down('#userFormDeleteButton'),
                        saveButton = this.down('#userFormSaveButton'),
                        titlebar = this.down('#userFormTitlebar'),
                        model = this.getRecord();

                    if (model.phantom) {
                        titlebar.setTitle('Create user');
                        saveButton.setText('create');
                        deleteButton.hide();
                    } else {
                        titlebar.setTitle('Update user');
                        saveButton.setText('update');
                        deleteButton.show();
                    }
                },
                deactivate: function() { this.resetForm() }
            }
        });

        App.views.UsersForm.superclass.initComponent.call(this);
    },

    onCancelAction: function() {
        Ext.dispatch({
            controller: 'Users',
            action: 'index'
        });
    },

    onSaveAction: function() {
        var model = this.getRecord();

        Ext.dispatch({
            controller: 'Users',
            action    : (model.phantom ? 'save' : 'update'),
            data      : this.getValues(),
            record    : model,
            form      : this
        });
    },

    onDeleteAction: function() {
        Ext.Msg.confirm("Delete this user?", "", function(answer) {
            if (answer === "yes") {
                Ext.dispatch({
                    controller: 'Users',
                    action    : 'remove',
                    record    : this.getRecord()
                });
            }
        }, this);
    },

    showErrors: function(errors) {
        var fieldset = this.down('#userFormFieldset');
        this.fields.each(function(field) {
            var fieldErrors = errors.getByField(field.name);

            if (fieldErrors.length > 0) {
                var errorField = this.down('#'+field.name+'ErrorField');
                field.addCls('invalid-field');
                errorField.update(fieldErrors);
                errorField.show();
            } else {
                this.resetField(field);
            }
        }, this);
        fieldset.setInstructions("Please amend the flagged fields");
    },

    resetForm: function() {
        var fieldset = this.down('#userFormFieldset');
        this.fields.each(function(field) {
            this.resetField(field);
        }, this);
        fieldset.setInstructions(this.defaultInstructions);
        this.reset();
    },

    resetField: function(field) {
        var errorField = this.down('#'+field.name+'ErrorField');
        errorField.hide();
        field.removeCls('invalid-field');
        return errorField;
    }
});

Ext.reg('App.views.UsersForm', App.views.UsersForm);
